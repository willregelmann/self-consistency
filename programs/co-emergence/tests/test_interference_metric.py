"""Tests for the interference metric (issue #32 / CE-1).

The metric I_S(rho) = S(Re rho) - S(rho) must:
  * be identically zero on Riemannian fixed points (real density matrices),
  * be strictly positive on Lorentzian fixed points (theta != 0),
  * be nonnegative and faithful on arbitrary states,
  * equal the relative entropy S(rho || Re rho),
  * scale monotonically with theta (quadratically at small theta),
  * have a size-robust global-state version with the stated closed form.
"""

import numpy as np
import pytest

from .toy_model import CoEmergenceModel
from .interference_metric import (
    interference_relative_entropy,
    interference_hs,
    interference_global,
    interference_global_closed_form,
    real_part_state,
    relative_entropy,
    von_neumann_entropy,
)


# ── Acceptance criterion 1: identically zero on Riemannian fixed points ──────

class TestZeroOnRiemannian:
    """Real density matrices carry no imaginary coherence: I_S == 0 exactly."""

    def test_n4_riemannian(self, fp_n4_riem):
        rho = CoEmergenceModel.partial_trace(fp_n4_riem, (2, 2), (0,))
        assert interference_relative_entropy(rho) < 1e-12
        assert interference_hs(rho) < 1e-12

    def test_n8_riemannian_all_subsystems(self, fp_n8_riem):
        for keep in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]:
            rho = CoEmergenceModel.partial_trace(fp_n8_riem, (2, 2, 2), keep)
            assert interference_relative_entropy(rho) < 1e-12, f"keep={keep}"
            assert interference_hs(rho) < 1e-12, f"keep={keep}"

    def test_n16_riemannian(self, fp_n16_riem):
        rho = CoEmergenceModel.partial_trace(fp_n16_riem, (2, 2, 2, 2), (0,))
        assert interference_relative_entropy(rho) < 1e-12

    def test_global_riemannian(self, fp_n4_riem, fp_n8_riem, fp_n16_riem):
        for fp in (fp_n4_riem, fp_n8_riem, fp_n16_riem):
            assert abs(interference_global(fp)) < 1e-12


# ── Acceptance criterion 2: strictly positive on Lorentzian fixed points ─────

class TestPositiveOnLorentzian:
    def test_n4_lorentzian(self, fp_n4_lor):
        rho = CoEmergenceModel.partial_trace(fp_n4_lor, (2, 2), (0,))
        assert interference_relative_entropy(rho) > 1e-8
        assert interference_hs(rho) > 1e-8

    def test_n8_lorentzian(self, fp_n8_lor):
        rho = CoEmergenceModel.partial_trace(fp_n8_lor, (2, 2, 2), (0,))
        assert interference_relative_entropy(rho) > 1e-8

    def test_global_lorentzian_sizes(self, fp_n4_lor, fp_n8_lor, fp_n16_lor):
        # Size-robust: the global metric does not decay to zero with system size.
        for fp in (fp_n4_lor, fp_n8_lor, fp_n16_lor):
            assert interference_global(fp) > 1e-3


# ── Properties: nonnegativity, faithfulness, relative-entropy identity ───────

class TestProperties:
    @staticmethod
    def _random_density(n, rng):
        A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        rho = A @ A.conj().T
        return rho / np.trace(rho).real

    def test_nonnegative_random(self):
        rng = np.random.RandomState(0)
        for _ in range(200):
            n = rng.randint(2, 8)
            rho = self._random_density(n, rng)
            assert interference_relative_entropy(rho) > -1e-10

    def test_real_part_is_valid_density_matrix(self):
        rng = np.random.RandomState(1)
        for _ in range(50):
            n = rng.randint(2, 7)
            rho = self._random_density(n, rng)
            sigma = real_part_state(rho)
            assert np.allclose(sigma, sigma.real)             # real
            assert np.allclose(sigma, sigma.T)                # symmetric
            assert abs(np.trace(sigma).real - 1.0) < 1e-10    # trace preserved
            ev = np.linalg.eigvalsh(sigma)
            assert ev.min() > -1e-10                          # PSD

    def test_faithfulness_zero_iff_real(self):
        rng = np.random.RandomState(2)
        # real PSD -> exactly zero
        for _ in range(20):
            n = rng.randint(2, 7)
            B = rng.standard_normal((n, n))
            rho = B @ B.T
            rho = rho / np.trace(rho)
            assert interference_relative_entropy(rho) < 1e-12
        # generic complex -> strictly positive
        for _ in range(20):
            rho = self._random_density(rng.randint(2, 7), rng)
            assert interference_relative_entropy(rho) > 1e-8

    def test_relative_entropy_identity(self):
        rng = np.random.RandomState(3)
        for _ in range(50):
            rho = self._random_density(rng.randint(2, 7), rng)
            lhs = interference_relative_entropy(rho)
            rhs = relative_entropy(rho, real_part_state(rho))
            assert abs(lhs - rhs) < 1e-9

    def test_concavity_bound_holds(self):
        # I_S >= 0 is exactly the statement S(Re rho) >= S(rho); check directly.
        rng = np.random.RandomState(4)
        for _ in range(50):
            rho = self._random_density(rng.randint(2, 7), rng)
            assert von_neumann_entropy(real_part_state(rho)) >= von_neumann_entropy(rho) - 1e-10


# ── Acceptance criterion 3: scales meaningfully with theta ───────────────────

class TestThetaScaling:
    def _reduced_metric(self, theta, seed=123):
        rng = np.random.RandomState(seed)
        h = rng.uniform(0.5, 1.5, 8)
        m = CoEmergenceModel(dims=(2, 2, 2), h=h, alphas=[0.5, 0.3, 0.4],
                             beta=0.4, gamma=-1.0 + 1j * theta)
        np.random.seed(42)
        fp = m.find_fixed_points(n_starts=20)[0]
        rho = CoEmergenceModel.partial_trace(fp, (2, 2, 2), (0,))
        return interference_relative_entropy(rho)

    def test_monotone_in_theta(self):
        vals = [self._reduced_metric(t) for t in [0.0, 0.25, 0.5, 1.0, 2.0]]
        assert vals[0] < 1e-12
        for lo, hi in zip(vals, vals[1:]):
            assert hi > lo

    def test_quadratic_at_small_theta(self):
        # I_S ~ c theta^2 at small theta: halving theta should quarter I_S.
        i_half = self._reduced_metric(0.25)
        i_full = self._reduced_metric(0.5)
        ratio = i_full / i_half
        assert 3.0 < ratio < 5.0  # ~4 with subleading corrections


# ── Global-state closed form ─────────────────────────────────────────────────

class TestGlobalClosedForm:
    def test_closed_form_matches_random(self):
        rng = np.random.RandomState(5)
        for _ in range(100):
            n = rng.randint(2, 12)
            psi = rng.standard_normal(n) + 1j * rng.standard_normal(n)
            psi /= np.linalg.norm(psi)
            assert abs(interference_global(psi) - interference_global_closed_form(psi)) < 1e-9

    def test_closed_form_matches_fixed_points(self, fp_n4_lor, fp_n8_lor, fp_n16_lor):
        for fp in (fp_n4_lor, fp_n8_lor, fp_n16_lor):
            assert abs(interference_global(fp) - interference_global_closed_form(fp)) < 1e-9
