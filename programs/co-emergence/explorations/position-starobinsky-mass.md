# Position: Starobinsky Effective Mass as Self-Consistent Mass Generation

**Date:** 2026-03-03
**Role:** Position Agent (advocating for Starobinsky mass mechanism)
**Part of:** Co-emergence mass gap debate

---

## Thesis

Self-consistency of gravity coupled to quantum fields *generates* effective mass for non-conformally-coupled fields, even when bare mass is zero. The mechanism is the Starobinsky de Sitter fixed point: the trace anomaly drives nonzero curvature R = 12H_0^2, which acts as a mass term m_eff^2 = (xi - 1/6)R for any field with non-conformal coupling xi != 1/6. This effective mass is genuine (it produces a mass shell, dispersion relation, and propagating modes), self-consistent (the massive field's stress-energy sources the very curvature that generates the mass), and sufficient to activate the Banach contraction and the full co-emergence chain.

The CFT counterexample kills the *strong* claim that self-consistency requires mass for all fields. The Starobinsky mechanism survives because it makes a *selective* claim: self-consistency generates mass precisely for the fields whose curvature coupling breaks conformal invariance. Conformally coupled fields (xi = 1/6) remain massless --- consistent with massless photons.

---

## 1. The Starobinsky de Sitter Fixed Point (Rigorous)

### 1.1 Setup

The semiclassical Einstein equation on a spatially flat FRW background with N_s scalars, N_f Dirac fermions, and N_v vector fields reads

G_mu_nu = 8 pi G <T_mu_nu>_ren

For massless conformal matter, the renormalized stress-energy is determined by the trace anomaly:

<T^mu_mu> = a E_4 + c W^2 + b Box R

where E_4 = R_abcd R^abcd - 4 R_ab R^ab + R^2 is the Gauss-Bonnet density, W^2 = C_abcd C^abcd is the Weyl-squared term, and the anomaly coefficients are

a = (1/2880 pi^2) [N_s + 11 N_f + 62 N_v]
c = -(1/2880 pi^2) [N_s + 6 N_f + 12 N_v]
b = (1/2880 pi^2) [(1/6) N_s + N_f + (11/3 - 1/xi_gauge) N_v]

(The b coefficient depends on renormalization scheme; its precise value affects the Hubble rate but not the existence of the solution.)

### 1.2 The de Sitter fixed point

On de Sitter spacetime ds^2 = -dt^2 + e^{2H_0 t} d**x**^2:
- The Weyl tensor vanishes (conformal flatness): W = 0, so the c-term drops out.
- The Gauss-Bonnet density is E_4 = 24 H_0^4.
- The Ricci scalar is R = 12 H_0^2.

The full stress-energy tensor is determined by SO(1,4) symmetry of the de Sitter vacuum (Bunch-Davies state):

<T_mu_nu> = rho_eff g_mu_nu

where rho_eff is determined algebraically by the trace anomaly and regularity conditions. Self-consistency reduces to a single algebraic equation for H_0:

3 H_0^2 / (8 pi G) = rho_eff(H_0; N_s, N_f, N_v)

This has a nonzero solution:

H_0^2 = 180 pi / (G |a_2|)

where a_2 is a combination of the anomaly coefficients. **(Rigorous.)**

**Key fact:** This fixed point exists with zero bare mass for all matter fields. It is driven entirely by the conformal trace anomaly. The geometry is not flat; it has R = 12 H_0^2 != 0.

### 1.3 Signature blindness at Level 2

The round 4-sphere S^4 with radius r = 1/H_0 is the Riemannian analogue. It is also conformally flat, maximally symmetric (SO(5)), and solves the same algebraic self-consistency condition. Both the de Sitter and S^4 solutions are Rigorous Level 2 fixed points. Level 2 is completely signature-blind, even for massless fields.

---

## 2. Effective Mass from Curvature Coupling (Sketch)

### 2.1 The mechanism

A scalar field phi with coupling to curvature has the field equation

(Box - m^2 - xi R) phi = 0

where xi is the coupling constant. For a conformally coupled scalar, xi = 1/6 in 4 dimensions, and the equation is conformally invariant when m = 0. For any other value of xi, the term xi R acts as an effective mass:

m_eff^2 = m^2 + xi R

On the Starobinsky de Sitter background with R = 12 H_0^2, even if the bare mass m = 0:

m_eff^2 = 12 xi H_0^2

This is nonzero for all xi != 0. For the physically important cases:

| Coupling | xi | m_eff^2 (bare m = 0) | Status |
|----------|-----|----------------------|--------|
| Minimal | 0 | 0 | Remains massless |
| xi = 1/6 (conformal) | 1/6 | 2 H_0^2 | See Section 2.3 |
| xi = 1/4 | 1/4 | 3 H_0^2 | Massive |
| xi = 1 | 1 | 12 H_0^2 | Massive |

**Important correction:** The conformal coupling xi = 1/6 gives m_eff^2 = 2 H_0^2, not zero. The mass-like term vanishes in the conformal equation only because the conformal wave equation is (Box - xi R + m^2)phi = 0 with a *relative sign*: the conformal coupling exactly cancels the curvature contribution to the effective mass in the conformally-invariant wave equation. I address this subtlety in Section 2.3.

### 2.2 Minimally coupled scalars (xi = 0): the infrared problem

Minimally coupled massless scalars (xi = 0, m = 0) have m_eff^2 = 0 even on the de Sitter background. They do not benefit from the Starobinsky mass generation. However, minimally coupled massless scalars in de Sitter face the well-known *infrared divergence* problem: the Bunch-Davies vacuum state has a logarithmically growing two-point function

<phi(x) phi(x')> ~ H_0^2 / (4 pi^2) ln(H_0 |x - x'|)

This infrared growth means the free-field treatment breaks down at late times (or large distances). The self-consistent backreaction of these infrared modes generates an effective mass of order m_eff ~ H_0 through the stochastic inflation mechanism (Starobinsky 1986, Starobinsky and Yokoyama 1994).

**Claim (Sketch):** Even for minimally coupled fields where the tree-level coupling to curvature gives m_eff = 0, the self-consistent treatment of infrared fluctuations in de Sitter generates an effective mass of order H_0. The massless, minimally coupled de Sitter vacuum is *unstable* to mass generation.

This is a well-studied phenomenon in inflationary physics. The stochastic approach shows that the equilibrium probability distribution for a light scalar in de Sitter is

P(phi) ~ exp(-8 pi^2 V(phi) / (3 H_0^4))

For a massless free field V = 0 this is flat (no equilibrium), confirming the infrared instability. Any self-interaction lambda phi^4 generates an effective mass m_eff^2 ~ sqrt(lambda) H_0^2. The self-consistent geometry forces the field out of its massless vacuum.

**Gap:** The stochastic inflation argument assumes a pre-existing de Sitter background and a specific vacuum state. A fully self-consistent treatment would need to solve for the geometry and field configuration simultaneously. The stochastic argument is motivational, not a proof within the hierarchy's framework.

### 2.3 Conformal coupling and the distinction between m_eff and physical mass

The conformal wave equation in curved spacetime is

(Box + (1/6) R) phi = 0

The sign convention matters. In the standard convention (Box - m^2 - xi R) phi = 0, the conformal case has xi = 1/6 and the "effective mass squared" is m_eff^2 = m^2 + xi R = 0 + (1/6)(12 H_0^2) = 2 H_0^2. But this term does not represent physical mass for a conformally coupled field: it is exactly the term required to make the equation conformally invariant. Under a conformal transformation g -> Omega^2 g, phi -> Omega^{-1} phi, the equation transforms covariantly. The "effective mass" 2H_0^2 is an artifact of writing the conformally invariant equation in a particular gauge.

**The physical criterion for mass is not m_eff^2 != 0 but the breaking of conformal invariance.** A conformally coupled massless scalar has:
- No mass shell (in the flat-space sense): the equation is conformally equivalent to the flat-space massless equation
- No massive particle states in the Bunch-Davies vacuum
- No contribution to local clocks or the Page-Wootters mechanism
- Conformal invariance intact at the classical level (broken only by the quantum trace anomaly)

This means the Starobinsky mass generation mechanism is more precisely stated as: **curvature coupling generates physical mass precisely when it breaks conformal invariance.** The relevant quantity is not xi R but (xi - 1/6) R:

m_physical^2 = m^2 + (xi - 1/6) R

For xi != 1/6, this is nonzero on the de Sitter background and represents genuine mass --- a mass shell, propagating modes, and local clocks.

**Revised table:**

| Coupling | xi | m_physical^2 (bare m = 0) | Conformal? | Mass generated? |
|----------|-----|---------------------------|------------|-----------------|
| Minimal | 0 | -2 H_0^2 | No | Tachyonic! |
| xi = 1/6 | 1/6 | 0 | Yes | No |
| xi = 1/4 | 1/4 | H_0^2 | No | Yes |
| xi = 1/3 | 1/3 | 2 H_0^2 | No | Yes |
| xi = 1 | 1 | 10 H_0^2 | No | Yes |

**Critical observation:** Minimally coupled scalars (xi = 0) acquire a *negative* physical mass-squared on the de Sitter background: m_physical^2 = -2 H_0^2. This is a tachyonic instability. The minimally coupled massless scalar is *unstable* on the Starobinsky background. This connects to the infrared divergence discussed in Section 2.2: the instability drives the field to a new configuration, and the self-consistent endpoint includes an effective mass (from self-interactions or backreaction).

**Rigor status:** The physical mass formula m_physical^2 = m^2 + (xi - 1/6)R and the identification of (xi - 1/6) as the conformal-breaking parameter are standard results in curved-spacetime QFT (see e.g. Birrell and Davies, "Quantum Fields in Curved Space," Chapter 3). **(Rigorous.)** The claim that the tachyonic instability for xi = 0 drives the system to a massive configuration is **(Conjecture).**

---

## 3. The Self-Consistency Bootstrap (Sketch)

### 3.1 The bootstrap argument

The Starobinsky mechanism suggests a bootstrap:

1. **Start with massless non-conformal fields** on a trial geometry (say, flat Minkowski).
2. **Compute the quantum stress-energy.** For massless conformal matter, the trace anomaly is nonzero. For non-conformal matter, there are additional divergences.
3. **Solve the Einstein equation** with this stress-energy source. The solution is not flat; it is the de Sitter geometry with R = 12 H_0^2.
4. **The curved geometry generates effective mass** m_eff^2 = (xi - 1/6) R for each non-conformal field.
5. **Recompute the stress-energy** now including the effective mass. The massive stress-energy is different from the massless one.
6. **Re-solve the Einstein equation.** The geometry adjusts.
7. **Iterate to a fixed point** where the geometry, the effective masses, and the stress-energy are all mutually consistent.

This is precisely the self-consistency iteration of the companion paper, but with the additional feature that the mass parameter itself participates in the iteration rather than being held fixed.

### 3.2 The extended fixed-point equation

The standard SCE is a fixed-point equation for the metric g alone:

g = F_m(g) where F_m is the map: given g, compute <T_mu_nu>_m, solve G_mu_nu = 8 pi G <T>

with m held fixed. The Banach contraction establishes existence with contraction constant kappa ~ (m/M_P)^2.

The bootstrap extends this to a joint fixed-point equation for (g, m_eff):

(g*, m_eff*) = G(g*, m_eff*)

where G is the extended map:
- Given (g, m_eff), compute the stress-energy <T_mu_nu>_{m_eff, g}
- Solve the Einstein equation for g_new
- Compute m_eff_new = (xi - 1/6) R[g_new]
- Return (g_new, m_eff_new)

**Claim (Sketch):** On the Starobinsky de Sitter background, this extended map has a fixed point (g_dS, m_eff* = (xi - 1/6) 12 H_0^2) for each field with xi != 1/6.

**Evidence:** The de Sitter geometry is a known fixed point of the standard map F_0 (with m = 0, driven by the trace anomaly). At this fixed point, R = 12 H_0^2 is determined. The effective mass is then m_eff^2 = (xi - 1/6) R, which is fixed once R is fixed. So the extended fixed point is immediate from the standard one: the mass does not need a separate fixed-point equation because it is determined algebraically by the curvature.

**Gap:** This argument shows that m_eff is consistent *at the de Sitter fixed point*. It does not show that the iteration starting from (g_flat, m = 0) converges to (g_dS, m_eff > 0). The convergence of the extended map requires analyzing the joint contraction in the (g, m_eff) space. The m_eff direction has a trivial contraction (m_eff is determined by R, so the joint map inherits the contraction of the standard map on g). But this assumes the metric iteration converges, which for massless fields is precisely the open question: the Banach contraction fails at m = 0, and the Schauder alternative gives existence without convergence.

### 3.3 Contraction constant with effective mass

Once m_eff is generated, the Banach contraction applies with

kappa = (m_eff / M_P)^2 = ((xi - 1/6) 12 H_0^2) / M_P^2

Using H_0^2 = 180 pi / (G |a_2|) = 180 pi M_P^2 / |a_2|:

kappa = (xi - 1/6)^2 * (12)^2 * (180 pi)^2 / |a_2|^2

For the Standard Model field content (N_s = 4, N_f = 45, N_v = 12 counting degrees of freedom):

|a_2| >> 1 (the anomaly coefficient is a sum over many fields)

So kappa << 1, and the perturbative expansion around the de Sitter fixed point with effective mass converges. **(Sketch)** --- the estimate is correct in scaling but the precise numerical coefficients require careful computation of the anomaly-driven Hubble rate and the contraction in the full non-local kernel.

### 3.4 What the bootstrap produces

If the bootstrap converges, the result is:

1. **A self-consistent geometry:** de Sitter with R = 12 H_0^2
2. **Effective masses for non-conformal fields:** m_eff^2 = (xi - 1/6) 12 H_0^2
3. **Massless conformal fields:** xi = 1/6 fields remain exactly massless
4. **A mass hierarchy:** different values of xi give different effective masses, all of order H_0

The mass scale is set by the Hubble rate H_0, which is set by the trace anomaly coefficients:

m_eff ~ H_0 ~ M_P / sqrt(N)

where N ~ |a_2| is the effective number of field species. For large N, m_eff << M_P --- the hierarchy between the generated mass and the Planck scale is natural (it comes from the large number of species).

---

## 4. Is the Effective Mass Genuine? (Sketch)

The central question: does m_eff from curvature coupling qualify as *physical mass* in the sense required by the co-emergence thesis?

### 4.1 Dispersion relation

On the de Sitter background, a scalar field with effective mass m_eff^2 = (xi - 1/6)R has the mode equation (in conformal time eta):

phi_k'' + [k^2 + m_eff^2 a^2(eta) - (1/6) R a^2(eta)] phi_k = 0

Wait --- let me be more careful. The field equation is (Box - xi R) phi = 0 for a massless field with coupling xi. In FRW with conformal time:

phi_k'' + 2 (a'/a) phi_k' + [k^2 + (xi - 1/6) R a^2] phi_k = 0

where primes denote d/d(eta) and a is the scale factor. The term (xi - 1/6) R a^2 acts as an effective mass in the mode equation. For xi > 1/6, modes with k^2 < (xi - 1/6) R a^2 are suppressed --- they experience exponential decay rather than oscillation. This is the signature of a mass gap.

**The dispersion relation for high-momentum modes (k >> H_0 a):**

omega^2 ~ k^2 + m_eff^2

This is the standard massive dispersion relation. High-momentum modes propagate as massive particles with mass m_eff = sqrt{(xi - 1/6) 12 H_0^2}.

**For low-momentum modes (k << H_0 a),** the dispersion relation is modified by Hubble friction and the expansion. The mass-shell structure is approximate, valid for modes with wavelength << Hubble radius.

### 4.2 Mass shell

In the subhorizon regime (physical wavelength << 1/H_0), the WKB approximation gives particle-like modes with energy-momentum relation

E^2 = p^2 + m_eff^2

where p is the physical 3-momentum and E is the energy measured by a comoving observer. This is a genuine mass shell. The modes are irreducible representations of the de Sitter isometry group SO(1,4), classified by the effective mass parameter. **(Rigorous** for the WKB regime; **Sketch** for the full de Sitter representation theory.)

### 4.3 Local clocks

A particle with effective mass m_eff follows timelike geodesics with proper time

d(tau)^2 = -g_mu_nu dx^mu dx^nu > 0

along the worldline. This proper time is independent of the origin of the mass --- whether it is bare mass or curvature-generated mass. The clock ticks at the same rate. The Page-Wootters mechanism can condition on this clock subsystem to extract local time evolution.

**Claim (Sketch):** Effective mass from curvature coupling is sufficient for the co-emergence chain. It provides:
- A mass shell (in the subhorizon regime)
- Timelike worldlines with proper time
- Local clocks for the Page-Wootters mechanism
- A Hilbert space for massive field modes
- Stress-energy that sources the self-consistent geometry

All four links of the co-emergence chain close with effective mass. Bare mass is not required.

### 4.4 What effective mass does NOT provide

**Specific mass values.** The effective mass is m_eff ~ sqrt{(xi - 1/6)} H_0, which is a single scale set by the Hubble rate. The rich mass spectrum of the Standard Model (m_e = 0.511 MeV, m_u ~ 2 MeV, m_t ~ 173 GeV, ...) cannot come from this mechanism alone. All non-conformal fields get masses of the same order H_0. This is not the observed mass spectrum.

**Mass for conformal fields.** Fields with xi = 1/6 (including the photon, which is conformally coupled in 4D) remain exactly massless. This is a feature, not a bug: it explains why the photon is massless. But it means the mechanism is selective, not universal.

**A Higgs-like mechanism.** The Starobinsky mass is generated by background curvature, not by a scalar field expectation value. It does not provide the electroweak symmetry breaking pattern. Whether the two mechanisms are related (e.g., whether the Higgs vev is stabilized by the self-consistent curvature) is an open question.

---

## 5. Connection to the Co-Emergence Thesis (Sketch/Conjecture)

### 5.1 The refined picture

The Starobinsky mechanism adds a new element to the co-emergence thesis. The original chain:

mass --> Lorentzian signature --> local time --> local Hilbert space --> <T_mu_nu> --> gravity --> mass

had mass as an input. The Starobinsky mechanism partially closes the gap:

trace anomaly --> nonzero R --> effective mass (for non-conformal fields) --> ... --> <T_mu_nu> --> R

The trace anomaly is a purely quantum effect that exists for any nonzero number of quantum fields, regardless of their mass. It is the bridge from "massless quantum fields" to "nonzero curvature." The curvature then generates effective mass, and the co-emergence chain activates.

### 5.2 What remains external

Even with the Starobinsky mechanism, several inputs remain:

1. **The number and type of quantum fields (N_s, N_f, N_v).** The anomaly coefficients depend on the field content. The field content is not derived from the hierarchy.

2. **The coupling constants xi for each field.** Which fields have which curvature coupling is an input.

3. **The specific values of mass (beyond m_eff ~ H_0).** The Starobinsky mechanism generates masses of order H_0, not the observed particle masses. The hierarchy from H_0 to the electroweak scale is not explained.

4. **Why any fields exist at all.** The mechanism requires quantum fields as input. It does not derive their existence from the topology of the manifold (that would be the Asselmeyer-Maluga program, which is a different position).

### 5.3 The strongest form of this position

**Conjecture (Starobinsky mass bootstrap):** Consider a 4-manifold M with Lorentzian signature, carrying any collection of quantum fields that includes at least one non-conformally-coupled species (xi != 1/6). Then the self-consistent solution of the semiclassical Einstein equation on M has R != 0, and the non-conformal fields acquire effective mass m_eff^2 = (xi - 1/6) R > 0 (for xi > 1/6). This effective mass is sufficient to support the co-emergence chain: local time, local Hilbert space, and effective quantum mechanics for subsystems.

**What this conjecture claims:**
- Mass is not a free parameter that must be supplied from outside. It is *generated* by the self-consistent geometry for any non-conformal field content.
- The only input needed is the existence of non-conformal quantum fields and a Lorentzian manifold.
- Conformal fields remain massless, explaining the photon.

**What this conjecture does NOT claim:**
- It does not explain the existence of fields (that is a Level 0-1 question).
- It does not explain the coupling constants xi (these are inputs).
- It does not produce the Standard Model mass spectrum.
- It does not work for Riemannian signature (the S^4 analogue generates m_eff but not a mass shell, dispersion relation, or local clocks).

### 5.4 Signature selectivity

**The Starobinsky mechanism is NOT signature-blind, even though Level 2 is.** Here is the crucial distinction:

On **Lorentzian de Sitter**, the effective mass generates:
- A mass shell (subhorizon WKB modes)
- Timelike geodesics with proper time
- Local clocks
- Propagating modes with dispersion E^2 = p^2 + m_eff^2

On **Riemannian S^4**, the effective mass generates:
- An elliptic mass parameter (changes the decay rate of correlators)
- No mass shell (no Lorentzian momentum space)
- No timelike geodesics (no timelike directions at all)
- No local clocks
- No propagating modes (all modes decay)

The curvature-generated m_eff^2 is the same number in both cases. But its *physical meaning* is entirely different. On the Lorentzian background, it is mass. On the Riemannian background, it is a correlation length parameter. The Starobinsky mechanism generates mass only on Lorentzian manifolds.

**This is the mechanism by which the co-emergence thesis selects Lorentzian signature:** The trace anomaly generates nonzero curvature on both Lorentzian and Riemannian manifolds. On Lorentzian manifolds, this curvature generates physical mass for non-conformal fields, which then supports the full co-emergence chain. On Riemannian manifolds, the curvature generates a correlation length, not a mass, and the co-emergence chain does not activate.

---

## 6. Honest Assessment of Gaps

### Gap 1: The conformal-to-nonconformal transition (Conjecture)

Why should any fields be non-conformally coupled? In four dimensions, classical electrodynamics (spin 1) is conformally invariant. Massless scalars with xi = 1/6 are conformally invariant. Massless fermions are conformally invariant. The Standard Model at the classical level, before the Higgs mechanism, is approximately conformal.

The Starobinsky mechanism requires at least one field with xi != 1/6. This is an input. The mechanism does not derive the existence of non-conformal fields; it derives mass from them.

**Partial defense:** Quantum corrections break conformal invariance. The trace anomaly itself is a conformal anomaly --- it exists because conformal invariance is violated by regularization/renormalization. In principle, the running of xi under RG flow could drive fields away from the conformal point xi = 1/6. Whether this happens self-consistently in the de Sitter background is an open question.

### Gap 2: The mass scale problem (Serious)

The Starobinsky mechanism generates masses of order m_eff ~ H_0. For the inflationary de Sitter with H_0 ~ 10^{13} GeV, this is a single scale 17 orders of magnitude above the electron mass. The observed mass spectrum spans at least 6 orders of magnitude (neutrino masses to top quark mass). The Starobinsky mechanism does not explain this hierarchy.

**Partial defense:** The Starobinsky de Sitter is the early-universe solution. The present-day Hubble rate is H_0 ~ 10^{-33} eV, giving m_eff ~ 10^{-33} eV --- much too small. The effective masses from the *current* curvature are cosmologically negligible. The physically relevant masses must come from a different mechanism (Higgs, etc.) or from the transition between the inflationary and post-inflationary phases.

This is not a contradiction but a limitation: the Starobinsky mechanism explains mass generation in the self-consistent inflationary phase, not in the late universe. Whether the effective masses generated during inflation have consequences for particle physics is an open question in inflationary cosmology.

### Gap 3: Convergence of the bootstrap (Sketch)

The bootstrap argument (Section 3) assumes the extended map G(g, m_eff) converges. The metric component of the map has the Banach contraction for massive fields (Rigorous) but not for massless fields (open). The bootstrap starts from massless fields, precisely where convergence is unproven. The argument is: once the first iterate generates m_eff > 0, subsequent iterates benefit from the Banach contraction. But the first iterate is the problematic one.

**Partial defense:** The Starobinsky de Sitter solution exists exactly (not as a perturbative expansion). The convergence issue arises only for perturbations around this solution. For the background itself, no iteration is needed --- it is an exact fixed point. The bootstrap question is whether perturbations of the massless de Sitter, including the effective mass corrections, converge to a self-consistent configuration. This is a perturbative stability question, not an existence question.

### Gap 4: Fermion masses (Conjecture)

The curvature coupling analysis above is for scalar fields. Fermions couple to curvature through the spin connection, not through a xi R term. The effective mass for a fermion in curved spacetime involves the spinor curvature coupling

S_Dirac = integral sqrt{-g} psi_bar (i gamma^mu nabla_mu - m) psi

For a massless fermion (m = 0), the Dirac equation in curved spacetime is conformally invariant in 4D. Curvature does not generate an effective fermion mass through the same mechanism.

**This is a significant gap.** The Starobinsky mechanism, as developed above, generates mass for non-conformal scalars but not for fermions. Fermion mass generation requires a different mechanism (Higgs, or the Asselmeyer-Maluga topology program, or some unknown mechanism).

**Partial defense:** Fermion masses in the Standard Model come from Yukawa couplings to the Higgs field. If the Higgs is a non-conformal scalar (xi != 1/6), the Starobinsky mechanism generates an effective Higgs mass, and the Yukawa couplings transmit this to the fermions. The chain is: curvature --> Higgs effective mass --> fermion masses via Yukawa. This requires the Higgs coupling constant xi and the Yukawa couplings as input.

---

## 7. Summary of Rigor Levels

| Claim | Level | Notes |
|-------|-------|-------|
| Starobinsky de Sitter is an exact self-consistent fixed point | **Rigorous** | Standard result (Starobinsky 1980, Bunch-Davies 1978) |
| R = 12 H_0^2 != 0 on the de Sitter background | **Rigorous** | Geometric fact |
| m_eff^2 = (xi - 1/6)R for non-conformal scalars | **Rigorous** | Standard curved-spacetime QFT |
| Effective mass produces a mass shell (subhorizon) | **Rigorous** | WKB in de Sitter |
| Effective mass is sufficient for the co-emergence chain | **Sketch** | Each link is individually justified but the full chain is not rigorously proven |
| The bootstrap from m = 0 to m_eff > 0 converges | **Sketch** | Once m_eff > 0, Banach contraction applies; the first step is the open one |
| Minimally coupled massless scalars are unstable to mass generation | **Conjecture** | Motivated by infrared divergences and stochastic inflation |
| The Starobinsky mechanism explains fermion masses | **Conjecture** | Requires Higgs as intermediary; not direct |
| The mechanism derives the mass spectrum | **Not claimed** | The mechanism produces a single scale, not a spectrum |

---

## 8. Conclusion: Why This Position Matters

The Starobinsky effective mass mechanism is the strongest currently available argument that self-consistency *generates* mass rather than merely *accommodating* it. Its key virtues:

1. **It does not require exotic topology.** It operates entirely at Level 2 (metric), using only the trace anomaly and non-conformal coupling. No Asselmeyer-Maluga machinery needed.

2. **It is partially Rigorous.** The Starobinsky fixed point, the effective mass formula, and the subhorizon dispersion relation are all established results. Only the bootstrap convergence and the co-emergence chain closure are Sketch/Conjecture.

3. **It is selective, not universal.** It generates mass for non-conformal fields and leaves conformal fields massless. This matches the observed pattern: photons are massless, other particles are massive.

4. **It is signature-selective.** Even though Level 2 is signature-blind, the *physical interpretation* of the curvature-generated mass is signature-dependent. On Lorentzian manifolds, m_eff is mass. On Riemannian manifolds, m_eff is a correlation length. This is the bridge from Level 2 blindness to cross-level selection.

The mechanism does not solve the mass gap problem completely. It does not derive the mass spectrum, the fermion masses (without Higgs), or the coupling constants. But it shows that the self-consistent geometry is not inert: it actively generates structure (effective mass) that was not present in the input (massless non-conformal fields). This is the minimal sense in which mass is *emergent* rather than *assumed*.
