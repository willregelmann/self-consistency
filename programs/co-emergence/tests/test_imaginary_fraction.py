"""Tests for the imaginary-fraction reduction (issue #33 / CE-2).

The imaginary fraction of the Lorentzian fixed point is a deterministic
functional of the Born magnitudes and theta.  After global-phase alignment to
the max-magnitude component (the convention of mixed_dimensions.py),

    im_frac^2 = sum_sigma p_sigma sin^2( (theta/2) log(p_max / p_sigma) ),

with p_sigma = |psi*_sigma|^2.  This file pins:
  * the closed form reproduces the directly computed im_frac to machine
    precision (the rigorous core),
  * the Riemannian fixed point (theta = 0) has im_frac == 0 exactly,
  * at fixed total dimension N the imaginary fraction does not depend on the
    subsystem rank min(d_1, d_2) (refuting the earlier "rank dependence"),
  * the fixed-point im_frac lies well below the Haar-random baseline.
"""

import numpy as np
import pytest

from .toy_model import CoEmergenceModel
from .imaginary_fraction import (
    im_frac_max,
    im_frac_formula,
    fixed_point,
    haar_im_frac,
    limit_max_align,
)


# ── Rigorous core: the closed form is exact ──────────────────────────────────

class TestExactReduction:
    @pytest.mark.parametrize("dims", [(2, 2), (2, 5), (3, 3), (4, 5),
                                      (6, 6), (2, 2, 2, 2)])
    @pytest.mark.parametrize("seed", [42, 123])
    def test_formula_matches_direct(self, dims, seed):
        psi = fixed_point(dims, seed, theta=1.0)
        assert psi is not None
        direct = im_frac_max(psi)
        formula = im_frac_formula(psi, 1.0)
        assert abs(direct - formula) < 1e-12


# ── Riemannian fixed point is exactly real ───────────────────────────────────

class TestRiemannianZero:
    @pytest.mark.parametrize("dims", [(2, 2), (3, 4), (2, 2, 2)])
    def test_theta_zero_real(self, dims):
        psi = fixed_point(dims, seed=7, theta=0.0)
        assert psi is not None
        assert im_frac_max(psi) < 1e-10


# ── Rank independence at fixed N ─────────────────────────────────────────────

class TestRankIndependence:
    """At fixed N the imaginary fraction is set by N (and theta, h), not by
    the subsystem rank min(d_1, d_2)."""

    @pytest.mark.parametrize("configs", [
        [(2, 8), (4, 4), (2, 2, 2, 2)],          # N = 16, ranks 2, 4, 2
        [(8, 8), (16, 4), (2, 2, 2, 2, 2, 2)],   # N = 64, ranks 8, 4, 2
    ])
    def test_fixed_N_independent_of_rank(self, configs):
        seeds = list(range(12))
        means = []
        for dims in configs:
            vals = [im_frac_max(p) for s in seeds
                    if (p := fixed_point(dims, s, theta=1.0)) is not None]
            means.append(np.mean(vals))
        spread = max(means) - min(means)
        # ranks differ by up to 6 here; if rank were the driver the spread
        # would be ~0.1 (cf. the old 0.26->0.34 claim). It is far smaller.
        assert spread < 0.02, f"means={means}, spread={spread}"


# ── Fixed point sits below the Haar baseline ─────────────────────────────────

class TestBelowHaar:
    @pytest.mark.parametrize("N", [16, 64])
    def test_fixed_point_below_haar(self, N):
        # square bipartition with total dimension N
        k = int(round(N ** 0.5))
        assert k * k == N
        seeds = list(range(12))
        vals = [im_frac_max(p) for s in seeds
                if (p := fixed_point((k, k), s, theta=1.0)) is not None]
        fp_mean = np.mean(vals)
        assert fp_mean < haar_im_frac(N) - 0.05


# ── Analytic large-N limit matches numerics ──────────────────────────────────

class TestAnalyticLimit:
    def test_large_N_matches_limit(self):
        seeds = list(range(20))
        vals = [im_frac_max(p) for s in seeds
                if (p := fixed_point((2,) * 7, s, theta=1.0)) is not None]
        # N = 128 should be close to the analytic asymptote ~0.40
        assert abs(np.mean(vals) - limit_max_align()) < 0.03
