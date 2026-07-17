# M3 Repair Attempt: Hyperboloidal Slicing on Asymptotically Flat, Radiating Backgrounds

**Date:** 2026-07-17
**Issue:** #167 (`co-emergence` CE-7's blocking prerequisite — does a self-consistent, asymptotically flat, non-trivially-radiating Level-2 fixed point exist?)
**Method:** construction attempt (Position agent) followed by independent adversarial stress-test (Verifier), per METHODOLOGY's agent-team pattern. Both full transcripts retained below per METHODOLOGY (losing/partial positions are part of the record); the construction's self-reported labels are superseded where the verifier found a genuine error, not silently corrected.
**Context:** `programs/fixed-point-existence/index.tex` (base theorem, assumptions A1–A6), `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md` (Gap M3 diagnosis: the response kernel is a Lorentzian hyperbolic Green operator with causal-past support; the existing proof's spatial-resolvent strategy on a compact Cauchy surface cannot reduce it; the only known repair, Meda–Pinamonti–Siemssen (MPS) on FLRW, exploits homogeneous spacelike slicing for a Volterra-type contraction, local-in-time, on a preferred foliation).

---

## Executive summary

**Verdict: genuine Sketch-level partial progress, not a completed existence result.** A hyperboloidal-slicing instantiation of M3's own prescribed repair shape (a controlled global foliation, foliation-restricted, local-in-time) closes at Sketch level for the **massless, conformally-coupled matter sector**, with several honestly-named and now more precisely located gaps. The **massive sector hits a confirmed, robust obstruction**: the naive conformal-rescaling route has an essential $\Omega^{-2}$ singularity at $\mathcal I^+$ for $m\ne0$ — independently re-derived by the verifier via a route immune to a sign-convention ambiguity the paper doesn't pin down, and corroborated by an independent physical argument (massive worldlines terminate at timelike infinity $i^+$, not null infinity $\mathcal I^+$). A named workaround (weighted, non-rescaled Sobolev control) is plausible but unconstructed.

The stress-test pass found the construction's own gap-accounting to be honest and mostly correctly labeled, but found two things the construction itself missed: a genuine incompleteness in the §2 energy identity (non-fatal, foldable into the existing error budget, but the display as written is wrong), and a mislabeled **Rigorous** claim that must be downgraded — the claim that Hadamard renormalization "needs no redefinition under a change of foliation" is true only for the local point-splitting *formula*; it does not address state-selection/vacuum ambiguity at a genuinely radiating $\mathcal I^+$, which the standard BMS-supertranslation-vacuum-ambiguity literature (memory effect, soft theorems) says is a real, unresolved freedom — the same freedom the construction's own Gap G4 already named for the energy-estimate side. This sharpens the paper's own pre-existing Gap M9 (Hadamard-state non-uniqueness) into a concrete, named mechanism specific to this manifold class (new gap **G7** below), rather than opening genuinely new territory.

This does not contradict M3's diagnosis. It instantiates M3's own stated repair shape for a manifold class (asymptotically flat, radiating) the base M3 exploration never attempted, and inherits the same foliation-restricted, local-in-time character MPS's FLRW repair already has. Per this program's own new "What This Program Produces" section: this is exactly the kind of construction — attempted directly, with every gap named, independent of whether prior literature has done it — the framework's rigor lifecycle is built to evaluate.

---

## 1. The construction

### 1.1 Setup

Physical spacetime $(M,g)$, $n=4$, asymptotically flat, globally hyperbolic, vacuum in a neighborhood of $\mathcal I^+$ (Bondi–Sachs radiating setting, matter confined to a bounded region — consistent with issue #167's framing). Conformal completion $\tilde g_{ab}=\Omega^2g_{ab}$, $\Omega=0$, $d\Omega\ne0$ along $\mathcal I^+$ (Penrose asymptotic simplicity — established background).

**Hyperboloidal slicing** (Zenginoğlu 2008, "Hyperboloidal foliations and scri-fixing," *Class. Quant. Grav.* 25, 195025, arXiv:0712.4333 — verified): a height function $h(r)\to r$ as $r\to\infty$ defines surfaces $\Sigma_\tau$ that are spacelike everywhere, including at their transversal intersection with $\mathcal I^+$ at a compact 2-sphere cross-section — unlike Bondi retarded-time slices ($u=\text{const}$), which are null and cannot serve as Cauchy surfaces for a Volterra-type argument (established by a prior research pass on this issue, not repeated here).

### 1.2 Kernel definition survives; the field-rescaling route does not, for massive fields (Sketch, confirmed)

Hadamard renormalization of $\langle\hat T_{\mu\nu}\rangle$ is a purely local construction (point-splitting against the Hadamard parametrix — Radzikowski, Hollands–Wald, already the paper's own (A1)/(A2)); it references no global foliation, so the response kernel's *formula* needs no redefinition under a change of foliation — this narrow claim is **Rigorous, confirmed**. (The broader question of which physical state this formula is evaluated on is a separate matter — see §1.4/G7.)

For a scalar field $(\Box_g+m^2+\xi R)\phi=0$ under $\tilde g=\Omega^2g$, $\phi=\Omega\tilde\phi$ ($n=4$), the transformed equation is
$$\Big(\Box_{\tilde g} - \xi_c\tilde R + (m^2+\delta\xi R_g)\,\Omega^{-2}\Big)\tilde\phi = 0, \qquad \delta\xi\equiv\xi-\xi_c,$$
where $\xi_c=1/6$ is the conformal coupling. **Independently re-derived by the verifier from the standard Yamabe/conformal-Laplacian covariance identity** (a route more robust than the construction's own constant-$\Omega$ consistency check, and shown to be independent of the paper's unpinned Ricci-sign convention — the $\Omega^{-2}$ divergence on the mass term survives either sign choice).

**For $m=0,\,\xi=1/6$:** the equation extends regularly across $\Omega=0$ — standard, and, per the verifier's bonus finding, actually holds for *any* $\xi$ in the vacuum-near-$\mathcal I^+$ region this construction already assumes, since $R\equiv0$ there kills the $\delta\xi R\,\Omega^{-2}$ term identically. The "conformally coupled" restriction is thus narrower than necessary for the stated domain — worth tightening in any follow-up, not an error.

**For $m\ne0$:** the potential term diverges as $\Omega^{-2}$ — an essential singularity, not removable. **Confirmed, robustly, by the verifier**, and corroborated by an independent physical argument: massive-field data does not reach $\mathcal I^+$ at all (it asymptotes toward timelike infinity $i^+$, a different point of the conformal completion), so the divergence correctly encodes real physics rather than signaling an inconsistency.

### 1.3 The massive-sector workaround (named, not built — Conjecture)

Since the kernel's *definition* needs no rescaling (§1.2, first paragraph), the actual tool needed is **weighted Sobolev norms on the non-compact physical slice** $\Sigma_\tau$ (Melrose/b-calculus- or Hintz–Vasy-style scattering-Sobolev spaces — named as the right class of tool, not confirmed applicable here), using $\Omega$ purely as an analytic weight rather than a field redefinition. This sidesteps the eq. (2) divergence since it asks only for controlled polynomially-weighted decay as $\Omega\to0^+$, not a regular equation *at* $\Omega=0$. Composing this with the non-local kernel's coincidence-limit structure is **not shown** — Gap **G3**, unbuilt.

### 1.4 The energy estimate: Volterra/Bielecki-norm contraction, corrected

The multiplier-method mechanism — energy identity on the hyperboloidal foliation → Grönwall bound → Bielecki-weighted norm → Volterra quasi-nilpotency giving a genuine contraction for $\sigma$ large — is **standard and correctly invoked as an abstract mechanism** (confirmed independently).

**Correction to the displayed energy identity (found by the verifier, not the original construction):** the divergence identity as displayed, $\nabla^\mu T^{[u]}_{\mu\nu}=J\nabla_\nu u$, is incomplete. The EOM-consistent stress tensor (fixing a sign inconsistency with the paper's own $(\Box+m^2+\xi R)\phi=0$ convention) satisfies
$$\nabla^\mu T_{\mu\nu} = J\,\nabla_\nu u + \tfrac12\xi u^2\,\nabla_\nu R,$$
picking up a residual term from $R$'s explicit spacetime dependence that the original construction omitted. **Assessed non-fatal:** the extra term is quadratic in $u$, foldable into the same Grönwall constant $\Lambda(\tau)$ already absorbing the deformation-tensor term, and vanishes identically in the vacuum-near-$\mathcal I^+$ region ($R\equiv0\Rightarrow\nabla R=0$ there) — it only bites in the bulk, exactly the region Gaps G1/G2 (below) already flag as unresolved. Read as sharpening those gaps with a concrete mechanism, not a new fatal flaw — but the identity as originally displayed should not be taken as verified without this correction.

Resulting bound: $\|u\|_\sigma\le\frac{C}{\sigma-\Lambda_{\sup}}\|J\|_\sigma$ for $\sigma>\Lambda_{\sup}\equiv\sup_\tau\Lambda(\tau)$ — the hyperboloidal instantiation of the M3 exploration's own named **A7** ("uniform causal-slab control"), here called **A7′**. Whether $\Lambda_{\sup}<\infty$ once $J$ is built from $\delta g$ through the coincidence-limit renormalization operator (not external data) is **not shown** — Gap **G1**, the single biggest open risk, now more precisely located via the correction above. Uniformity of A7′ over the compactness region $K_\rho$ is likewise not derived — Gap **G2**.

---

## 2. Resulting statement and limiting-case checks (confirmed)

**Candidate statement (Sketch, gaps named):** on an asymptotically flat, globally hyperbolic, vacuum-near-$\mathcal I^+$ background admitting a hyperboloidal Cauchy foliation satisfying A7′ uniformly on $K_\rho$, the self-consistency map satisfies a Volterra-type contraction in the $\sigma$-weighted hyperboloidal energy norm for massless, conformally-coupled matter, existence "Rigorous on a controlled hyperboloidal foliation, local in $\tau\in[0,T]$" — not the general theorem. Massive content requires Gap G3 closed first.

**Non-containment of the compact-$\Sigma$ theorem — confirmed by the verifier, independently checked.** Hyperboloidal slices of asymptotically flat spacetimes are topologically non-compact ($\mathbb R^3$); the base theorem's $\Sigma$ is compact without boundary (e.g. $S^3$). Genuinely different topological classes; no limit connects them.

**Non-containment of MPS/FLRW — confirmed by the verifier, independently checked.** FLRW with $\Lambda>0$ has a *spacelike* future conformal boundary (standard, and independently verified elsewhere in this repo, `programs/co-emergence/explorations/2026-07-17-null-infinity-boundary-clock.md` §2/§5); hyperboloidal slicing specifically reaches a *null* $\mathcal I^+$. These are parallel, non-overlapping instantiations of the same generic A7-template — **the M3 repair is a family of foliation-specific theorems, not one theorem to be filled in.** Worth flagging to the governor as a structural observation about how future M3-adjacent work should be scoped.

**Flat-space limit:** as $R\to0$, $N_{AB}\to0$, reduces to stationary hyperboloidal slicing of Minkowski — exactly the established hyperboloidal numerical-relativity literature's home turf (Zenginoğlu's Minkowski papers). Dependence of $\Lambda_{\sup}$ on the radiation amplitude is not derived.

**Dimensional analysis:** redone independently by the verifier — $[\Omega]$ dimensionless, $[\tau]$=length, $[\Lambda]$=mass, mass term in the transformed equation has dimension mass², consistent with the other Klein–Gordon-operator terms. No inconsistency found (the pre-existing, separate M1 dimensional issue in the base paper is untouched by this construction).

---

## 3. Hidden-assumption checks

**Foliation choice (height function):** licensed the same way choosing $\Sigma$ or FLRW's cosmological time was already licensed in the base theorem and MPS respectively — *provided* the final statement doesn't secretly depend on which one is picked. Unlike FLRW's essentially-unique homogeneous time, hyperboloidal height functions related by (a subgroup of) BMS supertranslations give inequivalent but equally valid foliations, and foliation-independence of $\Lambda_{\sup}$/$\kappa_\sigma$ is **not shown** — Gap **G4**. The verifier assessed this as **separable, not fatal**, because the candidate statement in §2 is already existentially quantified ("admitting *a* hyperboloidal foliation satisfying A7′"), structurally parallel to the base theorem's own "admitting a compact Cauchy surface" hypothesis. G4 becomes fatal only if a future strengthening claims the *result itself* (the fixed point, or $\kappa_\sigma$) is foliation-independent — at which point it is the same obstruction as the paper's own existing **Gap M8** (Σ-gauge-equivalence) recurring in a new guise. Any follow-up should note this connection explicitly.

**State selection / vacuum ambiguity at $\mathcal I^+$ (new gap G7, found by the verifier, required downgrade of a Rigorous claim):** the construction's claim that Hadamard renormalization "needs no redefinition under a change of foliation" is **Rigorous only for the local point-splitting formula** (§1.2) — it does not establish that the *physical state* being renormalized is foliation/frame-independent. On a genuinely radiating (non-stationary) asymptotically flat background, there is no canonical vacuum state the way there is on stationary backgrounds; the standard mechanism (asymptotic quantization at $\mathcal I^+$, BMS-supertranslation vacuum ambiguity, tied to the memory effect and soft theorems in the established literature) makes the natural reference state depend on a choice of Bondi frame/cut of $\mathcal I^+$ — the *same* freedom Gap G4 already names for the energy estimate. The construction drew a sharp line ruling the kernel/state's foliation-dependence *out* while ruling the energy norm's *in*; that line does not survive scrutiny. This sharpens the paper's own pre-existing, already-disclosed **Gap M9** (Hadamard-state non-uniqueness — "the perturbation prescription is assumed, not constructed") into a concrete, named mechanism specific to the radiating/asymptotically-flat case, rather than opening a new category of problem. **Required correction: the "needs no redefinition" claim is downgraded from Rigorous to Open/Conjecture for its broader (state-selection) reading; the narrow point-splitting-formula reading remains Rigorous.**

**Time evolution:** sneaks back in openly via the $\tau$-parametrized Grönwall estimate — the same accepted cost the base theorem already pays for FLRW/MPS, not a new one. Confirmed by the verifier; no additional smuggling found beyond G4 and G7.

---

## 4. Consistency with the M3 diagnosis

This construction instantiates, and does not contradict or attempt to route around, M3's own stated repair shape ("a controlled global foliation beyond A1–A6... foliation-restricted... local in time") for a manifold class the base M3 exploration never attempted. It inherits M3's own caveat that **Gap M5** (the self-mapping/displacement bound) would still need discharging for any foliation-restricted repair, in whatever norm that repair uses — named **G5** here, unresolved, inherited rather than introduced.

---

## 5. Gap summary (final, post-verification)

| Gap | Description | Status |
|---|---|---|
| **G1** | $\Lambda_{\sup}<\infty$ for the composed, non-local, Hadamard-renormalized source (not external data) | Open — single biggest risk, sharpened by the §1.4 energy-identity correction |
| **G2** | Uniformity of A7′ over $K_\rho$ | Open — not derived |
| **G3** | Massive-sector weighted-Sobolev workaround | Named, not constructed — Conjecture-level plausibility |
| **G4** | Foliation-covariance under height-function (BMS-supertranslation-type) freedom | Open; separable not fatal as currently scoped (connects to existing Gap M8 if strengthened) |
| **G5** | M5 self-mapping/displacement bound, in the $\sigma$-weighted norm | Inherited from the base M3 exploration, unresolved |
| **G6** | The $(G_{lin})^{-1}$ factor's own hyperboloidal well-posedness | Likely tractable via Frauendiener (1998) but not independently checked |
| **G7** | State-selection / vacuum ambiguity at a radiating $\mathcal I^+$ under BMS-frame freedom | **New, found by the verifier.** Sharpens the base paper's existing Gap M9 into a concrete mechanism for this manifold class. Required the downgrade of a Rigorous claim — see §3. |

---

## Rigor label summary (final, post-verification)

| Claim | Label |
|---|---|
| Causal structure is conformal-invariant (hence $J^-(x)$-support undisturbed by change of foliation) | Rigorous, standard |
| Hadamard renormalization's local point-splitting formula needs no redefinition under change of foliation | Rigorous (narrow reading only) |
| The physical state being renormalized is foliation/frame-independent on a radiating background | **Open/Conjecture** (downgraded from an incorrect Rigorous claim — G7) |
| Massless, conformally-coupled scalar equation extends regularly across $\mathcal I^+$ under conformal rescaling | Sketch (standard machinery; holds for any $\xi$ in the vacuum-near-$\mathcal I^+$ region specifically, per the verifier's bonus finding) |
| Massive/non-conformally-coupled equation has an essential $\Omega^{-2}$ singularity at $\mathcal I^+$ | Sketch, confirmed robustly by an independent re-derivation immune to the paper's unpinned Ricci-sign convention |
| Volterra/Bielecki-norm contraction mechanism, given $\Lambda_{\sup}<\infty$ | Rigorous as a general abstract mechanism |
| The displayed §2 energy (divergence) identity, as originally written | **Incomplete/incorrect as displayed** — corrected in §1.4; the correction is non-fatal and foldable into existing gaps |
| $\Lambda_{\sup}<\infty$ for the composed non-local-kernel estimate (A7′) | Conjecture (G1, G2) |
| Massive-sector repair via weighted Sobolev spaces | Conjecture (G3) |
| Foliation-covariance under height-function freedom | Open, not attempted (G4) — separable, not fatal, as currently scoped |
| Non-containment of the compact-$\Sigma$ theorem and of MPS/FLRW | Rigorous, independently confirmed |
| Overall existence statement (massless sector) | **Sketch**, contingent on G1, G2, G4–G7 |
| Massive sector | **Obstructed** (confirmed), workaround Conjecture-level (G3) |

---

## Recommendation

This is genuine Sketch-level progress toward issue #167's outcome (a), not a completed answer. It does not by itself resolve #167 — it establishes that the hyperboloidal-slicing route is a real, technically grounded candidate with precisely located remaining gaps, several of which (G1, G3, G7) look like the natural next targets; G4/G5/G6 are lower priority (separable, inherited, or likely-tractable respectively). Per this program's own "What This Program Produces" section, the correct next step is not to wait for external literature to close these gaps (none exists — confirmed by a prior research pass) but to attempt closing G1 or G7 directly, or to document either as a further structural obstruction if they resist. This Exploration's §1–§5 are a ready-made starting map for that work.

Recommend keeping issue #167 open, with this Exploration linked as substantial partial progress, and a follow-up issue scoped narrowly to Gap G1 (does $\Lambda_{\sup}$ stay finite once the source is the coincidence-limit-derived kernel rather than external data?) as the highest-value next target — this is the gap the verifier's correction most directly sharpened, and closing or refuting it would determine whether the massless-sector Sketch can be promoted further or needs its own documented-obstruction treatment.

---

*Internal references: `programs/fixed-point-existence/index.tex` (base theorem, assumptions A1–A6), `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md` (Gap M3, M5, M8, M9 diagnoses, the A7/MPS precedent), `programs/co-emergence/explorations/2026-07-17-null-infinity-boundary-clock.md` (§2/§5, spacelike-vs-null future boundary distinction, independently corroborated here). External citations: Zenginoğlu, "Hyperboloidal foliations and scri-fixing," Class. Quant. Grav. 25, 195025 (2008), arXiv:0712.4333 — verified; Ma & Huang, "A conformal-type energy inequality on hyperboloids...," J. Differential Equations 263(6), 3387–3415 (2017), arXiv:1711.00498 — verified; Frauendiener, Phys. Rev. D 58, 064003 (1998) — established background, not independently re-verified this session; Meda–Pinamonti–Siemssen (2021), Ann. Henri Poincaré 22(12), 3965–4015, arXiv:2007.14665 — verified in a prior session pass. Standard QFT-in-curved-spacetime conformal-transformation identities (Yamabe/conformal-Laplacian covariance) treated as established textbook material (Birrell–Davies; Wald), not independently verified against a primary source this session — flagged per METHODOLOGY exploratory tier; any paper-grade use requires formal verification.*

**Process note (interactive-mode disclosure):** produced by a human-directed construction-then-adversarial-verification pass (Position agent → Verifier, per METHODOLOGY's agent-team pattern) in an interactive Claude Code session, continuing the mock worker-pipeline exercise from issue #166/#167. No GitHub claim, comment, or PR was made by either agent in the pipeline; the human author reviewed and committed this file directly per METHODOLOGY.md's base Exploration process.

routine: interactive · model: claude-sonnet-5 (construction + verification agents, human-directed dry run per issue #167 — not an autonomy-mode routine)
