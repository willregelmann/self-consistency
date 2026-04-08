"""
Test emergent unitarity in measure-theoretic PW conditioning.

Two regimes where unitarity may emerge:
1. Large theta: phase variation grows with theta while magnitude variation
   is theta-independent (phase-lock lemma), so unitarity fraction increases.
2. Semiclassical clock: d_clock -> infinity with structured interaction,
   magnitude variation per step -> 0 while total phase evolution stays O(1).

Reference: exploration 2026-03-06-pw-unitarity.md
"""

import numpy as np
from toy_model import CoEmergenceModel
from pw_unitarity_test import (
    conditional_states, magnitude_variation, gram_matrix,
    toeplitz_deviation, unitary_orbit_test, phase_hamiltonian_test,
)


def unitarity_decomposition(phis):
    """Decompose c-dependence into unitary (phase) and non-unitary (magnitude) parts.

    For each c, decompose phi_c into:
    - "unitary approximation": same magnitudes as phi_0, actual phases
    - "classical approximation": actual magnitudes, phases stripped

    Returns
    -------
    unitarity_fractions : list of float
        ||rho_unitary_c - rho_0|| / ||rho_c - rho_0|| for each c > 0
    phase_variations : list of float
        ||rho_unitary_c - rho_0||_F
    mag_variations : list of float
        ||rho_classical_c - rho_classical_0||_F
    total_variations : list of float
        ||rho_c - rho_0||_F
    """
    phi0 = phis[0]
    mag0 = np.abs(phi0)
    rho0 = np.outer(phi0, phi0.conj())

    # Classical rho_0 (phases stripped)
    rho0_class = np.outer(mag0, mag0)
    rho0_class /= np.trace(rho0_class)

    unitarity_fractions = []
    phase_variations = []
    mag_variations = []
    total_variations = []

    for c in range(1, len(phis)):
        phi_c = phis[c]
        mag_c = np.abs(phi_c)
        phase_c = np.angle(phi_c)

        rho_c = np.outer(phi_c, phi_c.conj())
        total_var = np.linalg.norm(rho_c - rho0)

        # Unitary approximation: magnitudes of phi_0, phases of phi_c
        phi_unitary = mag0 * np.exp(1j * phase_c)
        phi_unitary /= np.linalg.norm(phi_unitary)
        rho_unitary = np.outer(phi_unitary, phi_unitary.conj())
        phase_var = np.linalg.norm(rho_unitary - rho0)

        # Classical approximation: actual magnitudes, no phases
        rho_class = np.outer(mag_c, mag_c)
        rho_class /= np.trace(rho_class)
        mag_var = np.linalg.norm(rho_class - rho0_class)

        if total_var > 1e-12:
            unitarity_fractions.append(phase_var / total_var)
        else:
            unitarity_fractions.append(1.0)

        phase_variations.append(phase_var)
        mag_variations.append(mag_var)
        total_variations.append(total_var)

    return unitarity_fractions, phase_variations, mag_variations, total_variations


def theta_sweep(dims=(3, 4), clock_idx=0, seed=42, verbose=True):
    """Sweep theta to test if unitarity fraction increases.

    Key insight: magnitude profiles are theta-independent (phase-lock lemma),
    so magnitude variation is constant while phase variation grows with theta.
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"THETA SWEEP: dims={dims}, clock=subsystem {clock_idx}")
        print(f"{'='*70}")

    N = int(np.prod(dims))
    rng = np.random.RandomState(seed)
    h = rng.uniform(0.5, 1.5, size=N)
    alphas = [0.5, 0.3] + [0.4] * (len(dims) - 2)
    alphas = alphas[:len(dims)]

    thetas = [0.1, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0]

    if verbose:
        print(f"\n  {'theta':>8} {'mag_var':>10} {'phase_var':>10} "
              f"{'total_var':>10} {'U_frac':>8} {'orbit_err':>10}")
        print(f"  {'-'*58}")

    results = []
    for theta in thetas:
        gamma = -1.0 + 1j * theta
        model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.4, gamma=gamma)
        np.random.seed(seed)
        psi, err, iters = model.find_fixed_point()
        if err > 1e-10:
            if verbose:
                print(f"  {theta:>8.1f}  NOT CONVERGED (err={err:.2e})")
            continue

        phis, probs = conditional_states(psi, dims, clock_idx)
        u_fracs, p_vars, m_vars, t_vars = unitarity_decomposition(phis)

        mean_u_frac = np.mean(u_fracs)
        mean_p_var = np.mean(p_vars)
        mean_m_var = np.mean(m_vars)
        mean_t_var = np.mean(t_vars)

        d_clock = dims[clock_idx]
        orbit_err = None
        if d_clock >= 3:
            orbit_errors, _ = unitary_orbit_test(phis)
            orbit_err = max(orbit_errors) if orbit_errors else None

        if verbose:
            oe_str = f"{orbit_err:>10.4f}" if orbit_err is not None else f"{'N/A':>10}"
            print(f"  {theta:>8.1f} {mean_m_var:>10.6f} {mean_p_var:>10.6f} "
                  f"{mean_t_var:>10.6f} {mean_u_frac:>8.4f} {oe_str}")

        results.append({
            'theta': theta, 'u_frac': mean_u_frac,
            'p_var': mean_p_var, 'm_var': mean_m_var, 't_var': mean_t_var,
            'orbit_err': orbit_err,
        })

    return results


def semiclassical_clock_test(d_sys=4, clock_idx=0, seed=42, verbose=True):
    """Test emergent unitarity in the semiclassical clock limit.

    Use structured interaction: h_{(c,s)} = h^S_s + (c/d_clock) * V_s
    Increase d_clock while keeping d_sys and total interaction fixed.

    In this limit:
    - Magnitude variation per step ~ V/d_clock -> 0
    - Total phase evolution ~ theta * V = O(1)
    - Evolution should become approximately unitary
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"SEMICLASSICAL CLOCK LIMIT: d_sys={d_sys}")
        print(f"h_{{(c,s)}} = h^S_s + (c/d_clock) * V_s")
        print(f"{'='*70}")

    rng = np.random.RandomState(seed)
    h_S = rng.uniform(0.5, 1.5, size=d_sys)
    V = rng.uniform(-0.5, 0.5, size=d_sys)
    theta = 1.0

    d_clocks = [2, 3, 4, 6, 8, 12, 16, 24, 32]

    if verbose:
        print(f"\n  {'d_clock':>8} {'mag_var':>10} {'U_frac':>8} "
              f"{'orbit_err':>10} {'lin_err':>10} {'toep_dev':>10}")
        print(f"  {'-'*58}")

    results = []
    for d_clock in d_clocks:
        dims = (d_clock, d_sys)
        N = d_clock * d_sys

        # Build structured h
        h = np.zeros(N)
        for c in range(d_clock):
            for s in range(d_sys):
                h[c * d_sys + s] = h_S[s] + (c / d_clock) * V[s]

        # Use weak self-coupling to minimize nonlinear feedback
        alphas = [0.05, 0.05]
        gamma = -1.0 + 1j * theta
        model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.05, gamma=gamma)
        np.random.seed(seed)
        psi, err, iters = model.find_fixed_point()
        if err > 1e-10:
            if verbose:
                print(f"  {d_clock:>8}  NOT CONVERGED (err={err:.2e}, iters={iters})")
            continue

        phis, probs = conditional_states(psi, dims, clock_idx)
        u_fracs, p_vars, m_vars, t_vars = unitarity_decomposition(phis)
        mean_u_frac = np.mean(u_fracs)
        mean_m_var = np.mean(m_vars)

        orbit_err = None
        toep_dev = None
        lin_err = None
        if d_clock >= 3:
            orbit_errors, _ = unitary_orbit_test(phis)
            orbit_err = max(orbit_errors) if orbit_errors else None
            toep_dev = toeplitz_deviation(gram_matrix(phis))[0]
            _, lin_err = phase_hamiltonian_test(phis, psi, dims, clock_idx)

        if verbose:
            oe_str = f"{orbit_err:>10.4f}" if orbit_err is not None else f"{'N/A':>10}"
            td_str = f"{toep_dev:>10.6f}" if toep_dev is not None else f"{'N/A':>10}"
            le_str = f"{lin_err:>10.6f}" if lin_err is not None else f"{'N/A':>10}"
            print(f"  {d_clock:>8} {mean_m_var:>10.6f} {mean_u_frac:>8.4f} "
                  f"{oe_str} {le_str} {td_str}")

        results.append({
            'd_clock': d_clock, 'u_frac': mean_u_frac, 'mag_var': mean_m_var,
            'orbit_err': orbit_err, 'lin_err': lin_err, 'toep_dev': toep_dev,
        })

    return results


def semiclassical_strong_coupling(d_sys=4, clock_idx=0, seed=42, verbose=True):
    """Same as semiclassical_clock_test but with standard (strong) couplings.

    Tests whether the semiclassical limit works even with O(1) self-coupling.
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"SEMICLASSICAL CLOCK (STRONG COUPLING): d_sys={d_sys}")
        print(f"alpha=0.5, beta=0.4 (standard parameters)")
        print(f"{'='*70}")

    rng = np.random.RandomState(seed)
    h_S = rng.uniform(0.5, 1.5, size=d_sys)
    V = rng.uniform(-0.5, 0.5, size=d_sys)
    theta = 1.0

    d_clocks = [2, 3, 4, 6, 8, 12, 16, 24, 32]

    if verbose:
        print(f"\n  {'d_clock':>8} {'mag_var':>10} {'U_frac':>8} "
              f"{'orbit_err':>10} {'lin_err':>10}")
        print(f"  {'-'*48}")

    for d_clock in d_clocks:
        dims = (d_clock, d_sys)
        N = d_clock * d_sys

        h = np.zeros(N)
        for c in range(d_clock):
            for s in range(d_sys):
                h[c * d_sys + s] = h_S[s] + (c / d_clock) * V[s]

        alphas = [0.5, 0.3]
        gamma = -1.0 + 1j * theta
        model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.4, gamma=gamma)
        np.random.seed(seed)
        psi, err, iters = model.find_fixed_point()
        if err > 1e-10:
            if verbose:
                print(f"  {d_clock:>8}  NOT CONVERGED (err={err:.2e})")
            continue

        phis, probs = conditional_states(psi, dims, clock_idx)
        u_fracs, _, m_vars, _ = unitarity_decomposition(phis)

        orbit_err = None
        lin_err = None
        if d_clock >= 3:
            orbit_errors, _ = unitary_orbit_test(phis)
            orbit_err = max(orbit_errors) if orbit_errors else None
            _, lin_err = phase_hamiltonian_test(phis, psi, dims, clock_idx)

        if verbose:
            oe_str = f"{orbit_err:>10.4f}" if orbit_err is not None else f"{'N/A':>10}"
            le_str = f"{lin_err:>10.6f}" if lin_err is not None else f"{'N/A':>10}"
            print(f"  {d_clock:>8} {np.mean(m_vars):>10.6f} {np.mean(u_fracs):>8.4f} "
                  f"{oe_str} {le_str}")


def hamiltonian_extraction(d_clock=16, d_sys=4, seed=42, verbose=True):
    """Extract the effective Hamiltonian in the semiclassical limit and verify.

    If evolution is approximately unitary with H_eff, then:
    phi_c(s) ≈ exp(-i H_eff c/d_clock) phi_0(s)

    Extract H_eff from the phase slope, reconstruct all conditional states,
    and measure the reconstruction error.
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"HAMILTONIAN EXTRACTION: d_clock={d_clock}, d_sys={d_sys}")
        print(f"{'='*70}")

    dims = (d_clock, d_sys)
    N = d_clock * d_sys
    rng = np.random.RandomState(seed)
    h_S = rng.uniform(0.5, 1.5, size=d_sys)
    V = rng.uniform(-0.5, 0.5, size=d_sys)
    theta = 1.0

    h = np.zeros(N)
    for c in range(d_clock):
        for s in range(d_sys):
            h[c * d_sys + s] = h_S[s] + (c / d_clock) * V[s]

    alphas = [0.05, 0.05]
    gamma = -1.0 + 1j * theta
    model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.05, gamma=gamma)
    np.random.seed(seed)
    psi, err, iters = model.find_fixed_point()
    assert err < 1e-10

    phis, probs = conditional_states(psi, dims, clock_idx=0)

    # Extract H_eff from phase slopes
    phases = np.zeros((d_clock, d_sys))
    for c in range(d_clock):
        ratio = phis[c] / phis[0]
        phases[c, :] = np.angle(ratio)
    for s in range(d_sys):
        phases[:, s] = np.unwrap(phases[:, s])

    # Linear fit: phase_c(s) = H_eff(s) * c
    H_eff = np.zeros(d_sys)
    for s in range(d_sys):
        c_vals = np.arange(d_clock)
        coeffs = np.polyfit(c_vals, phases[:, s], 1)
        H_eff[s] = coeffs[0]

    if verbose:
        print(f"  H_eff = {['%.6f' % h for h in H_eff]}")
        print(f"  theta * V / d_clock = {['%.6f' % (theta * V[s] / d_clock) for s in range(d_sys)]}")
        print(f"  H_eff / (theta*V/d_clock) = {['%.4f' % (H_eff[s] / (theta * V[s] / d_clock)) if abs(V[s]) > 1e-10 else 'N/A' for s in range(d_sys)]}")

    # Reconstruct conditional states using H_eff
    # Use phi_0 as baseline (not mag0), so reconstruction is exact at c=0
    phi0 = phis[0]
    reconstruction_errors = []
    fidelities = []
    for c in range(d_clock):
        # Predicted: phi_0 rotated by exp(i H_eff c) element-wise
        phi_pred = phi0 * np.exp(1j * H_eff * c)
        phi_pred /= np.linalg.norm(phi_pred)

        # Fidelity (phase-invariant)
        fid = np.abs(np.vdot(phi_pred, phis[c])) ** 2
        fidelities.append(fid)

        # DM error
        rho_pred = np.outer(phi_pred, phi_pred.conj())
        rho_actual = np.outer(phis[c], phis[c].conj())
        reconstruction_errors.append(np.linalg.norm(rho_pred - rho_actual))

    if verbose:
        print(f"\n  Reconstruction fidelity |<pred|actual>|^2:")
        # Show a few representative values
        indices = [0, d_clock // 4, d_clock // 2, 3 * d_clock // 4, d_clock - 1]
        for i in indices:
            print(f"    c={i:>3}: fidelity={fidelities[i]:.8f}, "
                  f"DM_err={reconstruction_errors[i]:.8f}")
        print(f"  Mean fidelity: {np.mean(fidelities):.8f}")
        print(f"  Min fidelity:  {np.min(fidelities):.8f}")
        print(f"  Mean DM error: {np.mean(reconstruction_errors):.8f}")
        print(f"  Max DM error:  {np.max(reconstruction_errors):.8f}")

    return H_eff, fidelities, reconstruction_errors


def small_V_large_theta(d_clock=16, d_sys=4, seed=42, verbose=True):
    """Sweep V_scale with theta*V_scale = const to push into the perturbative regime.

    As V_scale -> 0 (and theta -> infinity), the interaction becomes perturbative
    in magnitudes while total phase evolution stays O(1). This should push
    fidelity -> 1.
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"SMALL V, LARGE THETA: d_clock={d_clock}, d_sys={d_sys}")
        print(f"theta * V_scale = 1.0 (fixed)")
        print(f"{'='*70}")

    rng = np.random.RandomState(seed)
    h_S = rng.uniform(0.5, 1.5, size=d_sys)
    V_unit = rng.uniform(-0.5, 0.5, size=d_sys)  # unit interaction shape

    V_scales = [1.0, 0.5, 0.1, 0.05, 0.01]

    if verbose:
        print(f"\n  {'V_scale':>8} {'theta':>8} {'mag_var':>10} {'U_frac':>8} "
              f"{'orbit_err':>10} {'end_fid':>10}")
        print(f"  {'-'*60}")

    results = []
    for V_scale in V_scales:
        theta = 1.0 / V_scale
        V = V_unit * V_scale

        dims = (d_clock, d_sys)
        N = d_clock * d_sys
        h = np.zeros(N)
        for c in range(d_clock):
            for s in range(d_sys):
                h[c * d_sys + s] = h_S[s] + (c / d_clock) * V[s]

        alphas = [0.05, 0.05]
        gamma = -1.0 + 1j * theta
        model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.05, gamma=gamma)
        np.random.seed(seed)
        psi, err, iters = model.find_fixed_point()
        if err > 1e-10:
            if verbose:
                print(f"  {V_scale:>8.4f}  NOT CONVERGED (err={err:.2e})")
            continue

        phis, probs = conditional_states(psi, dims, clock_idx=0)
        u_fracs, _, m_vars, _ = unitarity_decomposition(phis)

        # Extract H_eff and compute end fidelity
        phases = np.zeros((d_clock, d_sys))
        for c in range(d_clock):
            ratio = phis[c] / phis[0]
            phases[c, :] = np.angle(ratio)
        for s in range(d_sys):
            phases[:, s] = np.unwrap(phases[:, s])
        H_eff = np.zeros(d_sys)
        for s in range(d_sys):
            coeffs = np.polyfit(np.arange(d_clock), phases[:, s], 1)
            H_eff[s] = coeffs[0]

        phi_pred = phis[0] * np.exp(1j * H_eff * (d_clock - 1))
        phi_pred /= np.linalg.norm(phi_pred)
        end_fid = np.abs(np.vdot(phi_pred, phis[-1])) ** 2

        orbit_err = None
        if d_clock >= 3:
            orbit_errors, _ = unitary_orbit_test(phis)
            orbit_err = max(orbit_errors) if orbit_errors else None

        if verbose:
            oe_str = f"{orbit_err:>10.4f}" if orbit_err is not None else f"{'N/A':>10}"
            print(f"  {V_scale:>8.4f} {theta:>8.1f} {np.mean(m_vars):>10.6f} "
                  f"{np.mean(u_fracs):>8.4f} {oe_str} {end_fid:>10.6f}")

        results.append({
            'V_scale': V_scale, 'theta': theta, 'end_fid': end_fid,
            'mag_var': np.mean(m_vars), 'u_frac': np.mean(u_fracs),
            'orbit_err': orbit_err,
        })

    return results


def fixed_theta_scaled_clock(d_sys=4, seed=42, verbose=True):
    """Fixed theta=1, scale d_clock while keeping V_scale * d_clock = const.

    This keeps the total phase evolution fixed while making the per-step
    interaction weaker. Tests whether unitarity emerges at the physical
    value theta=1 (not just in the large-theta limit).
    """
    if verbose:
        print(f"\n{'='*70}")
        print(f"FIXED THETA=1, SCALED CLOCK: d_sys={d_sys}")
        print(f"V_scale * d_clock = 16 (fixed)")
        print(f"{'='*70}")

    rng = np.random.RandomState(seed)
    h_S = rng.uniform(0.5, 1.5, size=d_sys)
    V_unit = rng.uniform(-0.5, 0.5, size=d_sys)
    theta = 1.0
    V_d_product = 16.0

    configs = [
        (1.0, 16),
        (0.5, 32),
        (0.25, 64),
        (0.125, 128),
        (0.0625, 256),
    ]

    if verbose:
        print(f"\n  {'V_scale':>8} {'d_clock':>8} {'mag_var':>10} {'U_frac':>8} "
              f"{'orbit_err':>10} {'end_fid':>10}")
        print(f"  {'-'*60}")

    results = []
    for V_scale, d_clock in configs:
        V = V_unit * V_scale
        dims = (d_clock, d_sys)
        N = d_clock * d_sys

        h = np.zeros(N)
        for c in range(d_clock):
            for s in range(d_sys):
                h[c * d_sys + s] = h_S[s] + (c / d_clock) * V[s]

        alphas = [0.05, 0.05]
        gamma = -1.0 + 1j * theta
        model = CoEmergenceModel(dims=dims, h=h, alphas=alphas, beta=0.05, gamma=gamma)
        np.random.seed(seed)
        psi, err, iters = model.find_fixed_point()
        if err > 1e-10:
            if verbose:
                print(f"  {V_scale:>8.4f}  NOT CONVERGED (err={err:.2e}, iters={iters})")
            continue

        phis, probs = conditional_states(psi, dims, clock_idx=0)
        u_fracs, _, m_vars, _ = unitarity_decomposition(phis)

        # H_eff extraction and end fidelity
        phases = np.zeros((d_clock, d_sys))
        for c in range(d_clock):
            ratio = phis[c] / phis[0]
            phases[c, :] = np.angle(ratio)
        for s in range(d_sys):
            phases[:, s] = np.unwrap(phases[:, s])
        H_eff = np.zeros(d_sys)
        for s in range(d_sys):
            coeffs = np.polyfit(np.arange(d_clock), phases[:, s], 1)
            H_eff[s] = coeffs[0]

        phi_pred = phis[0] * np.exp(1j * H_eff * (d_clock - 1))
        phi_pred /= np.linalg.norm(phi_pred)
        end_fid = np.abs(np.vdot(phi_pred, phis[-1])) ** 2

        orbit_err = None
        if d_clock >= 3:
            orbit_errors, _ = unitary_orbit_test(phis)
            orbit_err = max(orbit_errors) if orbit_errors else None

        if verbose:
            oe_str = f"{orbit_err:>10.4f}" if orbit_err is not None else f"{'N/A':>10}"
            print(f"  {V_scale:>8.4f} {d_clock:>8} {np.mean(m_vars):>10.6f} "
                  f"{np.mean(u_fracs):>8.4f} {oe_str} {end_fid:>10.6f}")

        results.append({
            'V_scale': V_scale, 'd_clock': d_clock, 'end_fid': end_fid,
            'mag_var': np.mean(m_vars), 'u_frac': np.mean(u_fracs),
            'orbit_err': orbit_err,
        })

    return results


def main():
    print("=" * 70)
    print("EMERGENT UNITARITY IN MEASURE-THEORETIC PW CONDITIONING")
    print("=" * 70)

    # --- Test 1: theta sweep ---
    theta_sweep(dims=(3, 4))
    theta_sweep(dims=(4, 4))

    # --- Test 2: semiclassical clock (weak coupling) ---
    semiclassical_clock_test(d_sys=4)

    # --- Test 3: semiclassical clock (strong coupling) ---
    semiclassical_strong_coupling(d_sys=4)

    # --- Test 4: Hamiltonian extraction ---
    hamiltonian_extraction(d_clock=16, d_sys=4)
    hamiltonian_extraction(d_clock=32, d_sys=4)

    # --- Test 5: small V, large theta ---
    small_V_large_theta(d_clock=16, d_sys=4)

    # --- Test 6: fixed theta=1, scaled clock ---
    fixed_theta_scaled_clock(d_sys=4)

    # --- Summary ---
    print(f"\n{'='*70}")
    print("CONCLUSIONS")
    print(f"{'='*70}")
    print("""
1. THETA SWEEP: Unitarity fraction should increase with theta because
   magnitude variation is theta-independent (phase-lock lemma) while
   phase variation scales with theta.

2. SEMICLASSICAL CLOCK: With structured interaction h = h^S + (c/d_clock)*V,
   unitarity should improve as d_clock -> infinity because magnitude
   variation per step ~ 1/d_clock -> 0 while total phase evolution ~ O(1).

3. HAMILTONIAN EXTRACTION: In the semiclassical limit, the phase slope
   H_eff should converge to theta * V / d_clock, and reconstruction
   fidelity should approach 1.
""")


if __name__ == "__main__":
    main()
