"""
Interference metric separating quantum (phase) coherence from classical
(real off-diagonal) redistribution.

Issue #32 / milestone CE-1. The earlier diagnostic compared the rotated-basis
populations of rho to those of diag(rho); it fired for *both* signatures
because real off-diagonal elements -- classical correlations from partial
tracing a pure state -- also redistribute probability across rotated bases
(see programs/co-emergence/explorations/2026-03-05-mixed-dimensions.md, "Interference
metric: needs refinement").

This module implements a metric that is *identically zero* on any real density
matrix and strictly positive only when the state carries genuine imaginary
coherence:

    I_S(rho) = S(Re rho) - S(rho) = S(rho || Re rho),

the von Neumann relative entropy between rho and its entrywise real part
Re rho = (rho + conj(rho))/2. For a Hermitian rho, Re rho is the
time-reversal-symmetrized state: a valid density matrix (PSD, trace-preserving),
real and symmetric. Properties (proved in
programs/co-emergence/explorations/2026-06-10-interference-metric.md):

  * I_S(rho) >= 0, with equality iff Im rho = 0          (faithful, nonnegative)
  * I_S(rho) = S(rho || Re rho)                          (relative-entropy identity)

A companion Hilbert-Schmidt metric, I_HS(rho) = ||Im rho||_F, is provided as a
simpler (non-entropic) witness of the same imaginary content.

Reference: programs/co-emergence/index.tex, Section "Lorentzian phases and the
entropy excess".
"""

import numpy as np

_EV_TOL = 1e-12


def von_neumann_entropy(rho, tol=_EV_TOL):
    """Von Neumann entropy S(rho) = -Tr(rho log rho), natural log.

    Hermitizes the input defensively and drops eigenvalues below ``tol``.
    """
    herm = (rho + rho.conj().T) / 2.0
    ev = np.linalg.eigvalsh(herm).real
    ev = ev[ev > tol]
    return float(-np.sum(ev * np.log(ev)))


def real_part_state(rho):
    """Entrywise real part Re rho = (rho + conj(rho))/2.

    For Hermitian rho this is the time-reversal-symmetrized density matrix:
    real, symmetric, PSD, and trace-preserving (the diagonal of a Hermitian
    matrix is already real).
    """
    return (rho + rho.conj()) / 2.0


def interference_relative_entropy(rho, tol=_EV_TOL):
    """Relative entropy of imaginarity I_S(rho) = S(Re rho) - S(rho).

    Identically zero for any real rho; strictly positive iff Im rho != 0.
    Equal to the von Neumann relative entropy S(rho || Re rho).
    """
    return von_neumann_entropy(real_part_state(rho), tol) - von_neumann_entropy(rho, tol)


def interference_hs(rho):
    """Hilbert-Schmidt interference witness I_HS(rho) = ||Im rho||_F.

    Simpler companion to :func:`interference_relative_entropy`: also exactly
    zero for real rho and positive otherwise, but not an entropy.
    """
    return float(np.linalg.norm(rho.imag, "fro"))


def relative_entropy(rho, sigma, tol=_EV_TOL):
    """Von Neumann relative entropy S(rho || sigma) = Tr rho(log rho - log sigma).

    Used to check the identity I_S(rho) = S(rho || Re rho). Returns +inf if the
    support condition supp(rho) <= supp(sigma) is violated.
    """
    er, Ur = np.linalg.eigh((rho + rho.conj().T) / 2.0)
    es, Us = np.linalg.eigh((sigma + sigma.conj().T) / 2.0)

    log_er = np.array([np.log(x) if x > tol else 0.0 for x in er])
    # support check: any weight of rho on a null eigenvector of sigma -> +inf
    proj = np.abs(Us.conj().T @ Ur) ** 2  # proj[a, i] = |<s_a | r_i>|^2
    for i, ri in enumerate(er):
        if ri <= tol:
            continue
        if np.any((es <= tol) & (proj[:, i] > tol)):
            return np.inf
    log_es = np.array([np.log(x) if x > tol else 0.0 for x in es])

    log_rho = Ur @ np.diag(log_er) @ Ur.conj().T
    log_sigma = Us @ np.diag(log_es) @ Us.conj().T
    return float(np.real(np.trace(rho @ (log_rho - log_sigma))))


# ── Global pure-state version (size-robust) ─────────────────────────────────


def align_global_phase(psi):
    """Fix the global phase so the largest-modulus component is real positive."""
    k = int(np.argmax(np.abs(psi)))
    return psi * np.exp(-1j * np.angle(psi[k]))


def interference_global(psi, tol=_EV_TOL):
    """Global interference content I_S(|psi><psi|) = S(Re |psi><psi|).

    For a pure state the reduced-state metric is suppressed by partial-trace
    averaging as the environment grows; the global version is size-robust.

    Writing the (global-phase-aligned, normalized) state psi = a + i b with a, b
    real, Re |psi><psi| = a a^T + b b^T has rank <= 2, so this equals the binary
    entropy of the eigenvalues of the 2x2 real-imaginary Gram matrix
    G = [[a.a, a.b], [a.b, b.b]] (closed form, see :func:`interference_global_closed_form`).
    Zero iff b is parallel to a after phase alignment, i.e. iff psi is real up to
    a global phase.
    """
    psi = align_global_phase(psi)
    rho = np.outer(psi, psi.conj())
    return von_neumann_entropy(real_part_state(rho), tol)


def interference_global_closed_form(psi, tol=_EV_TOL):
    """Closed form of :func:`interference_global` via the 2x2 real-imaginary Gram matrix."""
    psi = align_global_phase(psi)
    psi = psi / np.linalg.norm(psi)
    a, b = psi.real, psi.imag
    G = np.array([[a @ a, a @ b], [a @ b, b @ b]])
    ev = np.linalg.eigvalsh(G)
    ev = ev[ev > tol]
    return float(-np.sum(ev * np.log(ev)))


if __name__ == "__main__":  # pragma: no cover - manual validation runner
    import sys
    import os

    sys.path.insert(0, os.path.dirname(__file__))
    from toy_model import CoEmergenceModel

    print("Interference metric I_S = S(Re rho) - S(rho)\n")

    h4 = np.array([1.0, 0.7, 0.5, 1.2])
    for theta, lab in [(0.0, "Riem"), (1.0, "Lor ")]:
        m = CoEmergenceModel(dims=(2, 2), h=h4, alphas=[0.5, 0.3], beta=0.4,
                             gamma=-1.0 + 1j * theta)
        np.random.seed(42)
        fp = m.find_fixed_points(n_starts=20)[0]
        rho = CoEmergenceModel.partial_trace(fp, (2, 2), (0,))
        print(f"  N=4 {lab}: I_S={interference_relative_entropy(rho):.4e}  "
              f"I_HS={interference_hs(rho):.4e}  I_global={interference_global(fp):.4e}")

    print("\n  theta-scaling (N=8, reduced to one subsystem):")
    rng = np.random.RandomState(123)
    h8 = rng.uniform(0.5, 1.5, 8)
    for theta in [0.0, 0.25, 0.5, 1.0, 2.0]:
        m = CoEmergenceModel(dims=(2, 2, 2), h=h8, alphas=[0.5, 0.3, 0.4],
                             beta=0.4, gamma=-1.0 + 1j * theta)
        np.random.seed(42)
        fp = m.find_fixed_points(n_starts=20)[0]
        rho = CoEmergenceModel.partial_trace(fp, (2, 2, 2), (0,))
        print(f"    theta={theta:.2f}: I_S={interference_relative_entropy(rho):.6e}")
