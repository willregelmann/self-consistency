# Emergent Unitarity in Measure-Theoretic PW Conditioning

**Date:** 2026-03-06
**Program:** co-emergence
**Status:** Positive result — unitarity emerges in the semiclassical clock limit
**Depends on:** 2026-03-06-pw-unitarity.md (negative result for generic parameters)

## Question

The previous exploration showed that the toy model's c-dependence is generically non-unitary (magnitude variation ~0.33, orbit error ~1.0). Are there parameter regimes where unitarity emerges from self-consistency, rather than being assumed?

## Approach

**Script:** `programs/co-emergence/tests/pw_emergent_unitarity.py`

### Unitarity decomposition

Decompose the DM variation between clock values into two components:

- **Phase-driven (unitary):** Replace φ_c with φ^U_c = |φ_0| · exp(i·arg(φ_c)), keeping magnitudes of φ_0 but phases of φ_c. Then ||ρ^U_c − ρ_0|| measures the purely phase-driven variation.
- **Magnitude-driven (non-unitary):** Strip phases from φ_c. Then ||ρ^class_c − ρ^class_0|| measures the purely magnitude-driven variation.

Define the **unitarity fraction** U_frac = ||ρ^U_c − ρ_0|| / ||ρ_c − ρ_0||. When U_frac → 1, the c-dependence is purely phase-driven (approximately unitary).

## Results

### 1. Theta sweep (fixed geometry)

The phase-lock lemma (Lemma 4.1) guarantees that magnitudes |ψ*_σ| are θ-independent. Therefore magnitude variation is constant across θ, while phase variation grows with θ.

| θ    | mag_var | phase_var | U_frac | orbit_err |
|------|---------|-----------|--------|-----------|
| 0.1  | 0.523   | 0.053     | 0.10   | 0.43      |
| 0.5  | 0.523   | 0.262     | 0.45   | 0.62      |
| 1.0  | 0.523   | 0.513     | 0.72   | 0.96      |
| 3.0  | 0.523   | 1.219     | 0.95   | 1.55      |
| 10.0 | 0.523   | 1.308     | 0.97   | 1.57      |

**Key observation:** mag_var = 0.523 is exactly constant (phase-lock lemma confirmed numerically). U_frac rises from 0.10 to 0.97. However, orbit error also grows — high θ makes the c-dependence more unitary in character but stronger in magnitude.

### 2. Semiclassical clock limit (weak coupling)

Structure: h_{(c,s)} = h^S_s + (c/d_clock)·V_s. As d_clock → ∞, the per-step magnitude perturbation ~V/d_clock → 0 while total phase evolution θ·V stays O(1).

| d_clock | mag_var | U_frac | orbit_err | lin_err  |
|---------|---------|--------|-----------|----------|
| 3       | 0.205   | 0.783  | 0.039     | 0.00048  |
| 8       | 0.203   | 0.785  | 0.031     | 0.00042  |
| 16      | 0.202   | 0.786  | 0.018     | 0.00031  |
| 32      | 0.202   | 0.786  | 0.009     | 0.00023  |

**Key observation:** Orbit error → 0 as d_clock → ∞. The conditional states converge to a one-parameter unitary orbit. But mag_var plateaus at ~0.20 because the total magnitude perturbation V is O(1).

### 3. Hamiltonian extraction

In the semiclassical limit, extract H_eff from the phase slope of φ_c(s)/φ_0(s).

| d_clock | H_eff / (θV/d_clock) | Mean fidelity | Min fidelity |
|---------|----------------------|---------------|--------------|
| 16      | 0.993–1.003          | 0.976         | 0.938        |
| 32      | 0.996–1.002          | 0.975         | 0.935        |

H_eff converges to θV/d_clock to ~1% accuracy. The reconstruction error comes from the finite magnitude variation, not from the phase structure.

### 4. Small V, large θ (perturbative regime)

Fix θ·V_scale = 1.0 so total phase evolution is O(1). As V_scale → 0 (and θ → ∞), the magnitude perturbation vanishes while the phase structure is preserved.

| V_scale | θ    | mag_var | U_frac | orbit_err | end_fid  |
|---------|------|---------|--------|-----------|----------|
| 1.000   | 1.0  | 0.202   | 0.786  | 0.018     | 0.938    |
| 0.100   | 10.0 | 0.023   | 1.004  | 0.003     | 0.999    |
| 0.010   | 100  | 0.002   | 1.001  | 0.002     | 0.99999  |

**This is the strongest result.** As V_scale → 0:
- mag_var → 0 (magnitude profiles become c-independent)
- U_frac → 1 (c-dependence becomes purely phase-driven)
- orbit_err → 0 (states lie on a unitary orbit)
- end_fid → 1 (Hamiltonian reconstruction is exact)

### 5. Fixed θ=1, scaled clock (physical regime)

Fix θ = 1 (the physical Lorentzian value). Scale V_scale·d_clock = 16 so total phase evolution is fixed. As V_scale → 0 and d_clock → ∞, each clock tick is a smaller perturbation.

| V_scale | d_clock | mag_var | orbit_err | end_fid |
|---------|---------|---------|-----------|---------|
| 1.000   | 16      | 0.202   | 0.018     | 0.938   |
| 0.250   | 64      | 0.056   | 0.0004    | 0.994   |
| 0.0625  | 256     | 0.014   | 0.0000    | 0.9996  |

**Critical for the thesis:** Unitarity emerges at θ = 1 (the physical value). No large-θ limit needed. The semiclassical clock limit alone suffices.

## Mechanism

### Why unitarity emerges

The fixed point has ψ*_σ ∝ exp((−1 + iθ)R_σ), so:
- |φ_c(s)| ∝ exp(−R_{(c,s)})
- arg(φ_c(s)) = θ·R_{(c,s)}

With h_{(c,s)} = h^S_s + (c/d_clock)·V_s:
- R_{(c,s)} = R^0_s + (c/d_clock)·V_s + O(V²/d_clock²) + nonlinear corrections
- |φ_c(s)| ≈ |φ_0(s)|·exp(−(c/d_clock)·V_s) — multiplicative perturbation per step ~V/d_clock
- arg(φ_c(s)) ≈ arg(φ_0(s)) + θ·(c/d_clock)·V_s — linear phase accumulation

As V/d_clock → 0:
- Magnitude perturbation vanishes: |φ_c(s)| → |φ_0(s)|
- Phase accumulation is preserved: Δarg ≈ θ·V_s·c/d_clock
- This IS unitary evolution with H_eff(s) = θ·V_s/d_clock

### Physical interpretation

**The semiclassical clock limit in the toy model is the analogue of the WKB limit in quantum gravity.** When the clock subsystem is large (d_clock → ∞) and the per-tick interaction is weak (V/d_clock → 0), the clock provides a good time reference: its back-reaction on the system is negligible, and the system evolves unitarily with respect to the clock.

The key insight: **unitarity is not assumed — it emerges from self-consistency when the clock is semiclassical.** The self-consistency fixed point, which makes no reference to unitarity or Hamiltonians, produces approximately unitary c-dependence in the appropriate limit. The effective Hamiltonian H_eff = θV/d_clock is determined by the self-consistency condition, not imposed.

### The role of θ

The phase-lock lemma (magnitudes are θ-independent) means θ controls the *ratio* of phase to magnitude variation. At θ = 0 (Riemannian), there is no phase variation at all — no unitarity is possible. At θ > 0 (Lorentzian), the phase structure provides the unitary component. At θ = 1 with a semiclassical clock, unitarity emerges without any additional tuning.

This is the dynamical consequence of Lorentzian signature: **Lorentzian signature is what makes time evolution unitary, not just quantum.**

## Implications for the paper

### What is now established

1. **Algebraic PW structure** (Propositions 4.4–4.6, Rigorous): Measure-theoretic conditioning produces c-dependent quantum states, with mixture consistency and Lorentzian requirement.

2. **Emergent unitarity** (this exploration, Sketch): In the semiclassical clock limit (d_clock → ∞, V/d_clock → 0), the c-dependence converges to unitary evolution generated by H_eff = θV/d_clock. The effective Hamiltonian is self-consistently determined.

3. **Lorentzian requirement for dynamics** (this exploration, Sketch): Unitarity requires θ > 0 (Lorentzian signature). At θ = 0, there is no phase structure and no unitary evolution. At θ = 1, the physical Lorentzian value, unitarity emerges with a semiclassical clock.

### What remains open

1. **Rigorous convergence proof:** Show that ||ρ_c − U^c ρ_0 (U†)^c|| → 0 as d_clock → ∞ with appropriate scaling.
2. **Connection to physical Hamiltonians:** The toy model V_s is an artificial interaction potential. In the full theory, V should emerge from the curvature coupling.
3. **Beyond the perturbative regime:** The current results are in the regime V/d_clock << 1. What happens for strong clock-system coupling?

## Verdict

**Positive.** Unitarity emerges from self-consistency in the semiclassical clock limit. The effective Hamiltonian is self-consistently determined, not imposed. This completes the dynamical content of the Page-Wootters mechanism within the measure-theoretic framework: conditioning on a semiclassical clock produces approximately unitary time evolution, with the Hamiltonian determined by the self-consistency fixed point. Lorentzian signature (θ > 0) is required.
