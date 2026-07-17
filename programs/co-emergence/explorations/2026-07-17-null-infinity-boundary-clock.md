# CE-7: Null-Infinity / Carrollian Boundary Structure as a Level-3 Clock — Scoping Exploration

**Date:** 2026-07-17
**Role:** Synthesis Agent (adversarial critique + defense assessment of two independent position debates)
**Inputs:**
1. Literature packet — celestial/Carrollian null-infinity survey (researcher agent, this debate)
2. Position A — "Yes, a specific mechanism exists" (independent, did not see Position B)
3. Position B — "No, at least one postulate beyond Axioms 1–3 is required" (independent, did not see Position A)
**Context:** `programs/co-emergence/index.tex` §time_hilbert (L909–963), Level-3 subsection (L1749–1774), Conjecture `conj:qm` (L1550–1576); `programs/co-emergence/README.md` Open Problem 3; `programs/fixed-point-existence/index.tex` L85; `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md`. Issue #166.

---

## Executive summary

**Verdict: blocked on a precisely-named, currently-nonexistent prerequisite — not a fatal no-go, and not yet a viable milestone.**

Both position agents, working from disjoint document sets and blind to each other, independently converged on the identical finding: **the co-emergence program currently has no self-consistent Level-2 fixed point of the right causal type for any boundary-clock mechanism to attach to.** Position A found this by noting the program's one known massless Level-2 solution (Starobinsky/de Sitter) has a *spacelike* future conformal boundary (Λ>0, cosmological) — not the *null* infinity $\mathcal I^+$ that Carrollian/celestial structure requires. Position B found this independently by reading `fixed-point-existence/index.tex` directly: the program's Level-2 anchor result explicitly and structurally excludes asymptotically flat spacetimes (L85: "does not cover Minkowski space or asymptotically flat backgrounds"), for a reason (Gap M3) diagnosed as mass-independent and geometric, not incidental.

This is a genuine convergence, not a coincidence of framing: one position ruled out the *only known example*; the other ruled out the *general existence machinery* that would need to produce a new one. Together they close both routes by which a witness could currently be found. Neither position, nor this synthesis, has a no-go theorem — Gap M3 is a permanently-Sketch obstruction of a *specific proof technique* (Banach contraction requiring a compact Cauchy surface), not a proof that no asymptotically-flat self-consistent solution can exist by any method. The M3 exploration itself names a plausible (if harder) forward path: a foliation-restricted, MPS-style repair.

Everything downstream of this — the Level-3 mechanism itself (Bondi mass aspect as clock), the axiom compatibility questions, the Level-0 manifold-class check — is real, carefully argued, and worth preserving as a record. But none of it has anything to act on until the prerequisite is resolved one way or the other. Per issue #166's acceptance criteria, this Conjecture-level negative finding is the complete deliverable.

**A citation-integrity finding surfaced during this synthesis, reported in full in §1, materially affects how much weight the rest of the literature packet should carry:** of 6 modern-era arXiv citations in the research packet that I independently re-verified by direct fetch, 4 carry fabricated or wrong author attributions on genuinely real, correctly-titled papers. This does not change the physics conclusions above (which rest on this repo's own committed text, not on the packet), but it means no citation from the packet may be used at paper-grade, or trusted at exploratory-tier, without independent re-verification of the specific claim being attributed.

---

## 1. Literature survey summary, with citation-integrity finding

### 1.1 What the literature establishes (content-level claims, Rigorous as established external results; citation status handled separately in §1.2)

- **Carrollian geometry** is the $c\to 0$ (ultra-relativistic) contraction of Lorentzian geometry: a triple $(N, h_{ab}, n^a)$ with $h_{ab}$ a *degenerate*, positive-semidefinite rank-2 tensor and $n^a$ a nonvanishing kernel vector field, $h_{ab}n^b=0$. This structure arises naturally on null hypersurfaces, most notably null infinity $\mathcal I^\pm$, and on black-hole and cosmological horizons.
- **BMS symmetry.** The asymptotic symmetry group of asymptotically flat gravity at $\mathcal I^\pm$ is not the 10-dimensional Poincaré group but an infinite-dimensional group containing *supertranslations* $u \to u + f(z,\bar z)$ — direction-dependent time shifts. The conformal Carrollian symmetry group is isomorphic to BMS.
- **Soft theorem / memory / BMS triangle.** Weinberg's soft graviton theorem is equivalent to the Ward identity of BMS supertranslation invariance of the gravitational S-matrix; this is the same statement encoded, via conservation of supermomentum, in the gravitational memory effect. This is the "critical unification" result the packet leans on to establish that $\mathcal I^+$ carries genuine, non-trivial dynamical structure.
- **Bondi mass-loss formula.** $\partial_u M(u,z,\bar z) = -\tfrac18 N_{AB}N^{AB} + (\text{matter flux})$, monotonically non-increasing under the null energy condition. Standard GR (Rigorous as a GR fact; exact normalization not independently rederived this session).
- **Retarded time $u$ as a boundary dynamical coordinate** is already standard in the celestial/Carrollian literature: correlators depend on $(u,z,\bar z)$, Bondi mass evolves in $u$, supertranslations form an infinite-dimensional algebra of "time translations." **Critically, no paper found by the researcher (nor by either position agent) frames this $u$-dependence as a Page–Wootters-style clock, or attempts to reconstruct bulk time evolution by conditioning on boundary data.** This is confirmed absence, not merely unexplored — the researcher explicitly searched for it. This absence is itself informative for the axiom analysis in §7: nothing in the literature already does the work either position needs.

### 1.2 Citation-integrity finding (own finding, not inherited from either position)

I independently re-fetched 6 of the packet's modern-era (post-2000) arXiv citations directly from arxiv.org to check author attribution, since the paper this program treats citation fabrication as "the single most serious failure mode" (METHODOLOGY.md). Results:

| arXiv ID | Packet's claimed authors | Actual authors (verified by direct fetch) | Title match? | Verdict |
|---|---|---|---|---|
| 2510.21651 | Ciambellia, Jai-akson (2024) | **Luca Ciambelli, Puttarak Jai-akson** | Yes, exact | Correct paper; minor transcription errors (name spelling, year — arXiv ID indicates Oct 2025, not 2024) |
| 2602.02644 | Ruzziconi, R. (2026) | **Romain Ruzziconi** | Yes, exact | **Correct** |
| 2407.03432 | de Boer, Papadodimas, Sheikh-Jabbari et al. | **Andrea Calcinari, Steffen Gielen** | Yes, exact | **Fabricated author attribution** — real paper, real authors (matching Position A's independent characterization of its content), wrong names entirely substituted |
| 1712.03211 | Strominger, A. (2017–2018) | **Atreya Chatterjee, David A. Lowe** | Yes, exact | **Fabricated author attribution.** This citation was used to support the packet's single most load-bearing claim (§B, "the critical result": Strominger showed soft theorem ≡ BMS Ward identity) |
| 1411.5745 | He, S., Mitra, P., Strominger, A. (2014) | **Andrew Strominger, Alexander Zhiboedov** | Yes, exact | **Fabricated co-authors** (He, Mitra invented; Zhiboedov omitted; Strominger correctly present) |
| 2402.14062 | Bagchi, Basu, Mehra, Tan (2024) | **Stephan Stieberger, Tomasz R. Taylor, Bin Zhu** | Yes, exact | **Fabricated author attribution** |

**4 of 6 sampled citations (67%) carry fabricated or wrong author lists on real, correctly-titled, on-topic papers.** The pattern is specific: titles and arXiv IDs are accurate (these appear to have been genuinely looked up), but author lists were substituted with plausible, prominent, topically-adjacent researcher names rather than the papers' actual (sometimes less famous) authors.

**A sharper finding, found only by chasing this down:** the packet's own "critical result" — that Strominger established the soft-theorem/BMS equivalence — is *not actually supported by either citation given for it*. The real paper making this claim is **arXiv:1401.7026**, "BMS supertranslations and Weinberg's soft graviton theorem," by **He, Lysov, Mitra, Strominger** (verified by direct fetch: abstract confirms "we show that this supertranslation Ward identity is precisely equivalent to Weinberg's soft graviton theorem"). This paper is **absent from the packet's citation list entirely**. Its author list ("He... Mitra... Strominger") appears to be exactly what got garbled and reattached to the wrong arXiv ID (1411.5745, actually Strominger & Zhiboedov) — a plausible mechanism for how the error happened, though the practical consequence is what matters: the packet's central claim is currently supported by two wrong citations, while the one that actually supports it was never found.

**Implication for this Exploration and for any future work drawing on this packet:** The *topical* content summary in §1.1 (Carrollian geometry's definition, the BMS/soft/memory triangle's existence, the "no boundary-clock precedent exists" finding) is corroborated by real, correctly-titled papers and I treat it as reliable exploratory-tier content. But **no specific author attribution, and no specific claim-to-citation pairing, in the packet may be trusted without independent re-verification** — this includes citations I did not personally re-check (the 1962 Bondi/Sachs papers and the 1965 Penrose paper are extremely well-established canonical GR references and were not re-verified this session for time reasons, but per the same discipline should still go through `tools/verify_citations.py`-style checking before any paper-grade use, not assumed safe by virtue of fame). None of these citations enter `index.tex` in this Exploration, consistent with issue #166's acceptance criteria.

This is a **haiku-model, search-specialist-role finding**: the packet was produced by a `claude-haiku-4-5` search-specialist subagent. This is worth naming as a process observation for future routines that dispatch literature surveys to fast/cheap models — the failure mode here (correct paper identification, fabricated attribution) is exactly the kind of error that is easy to miss on a skim and easy to catch by direct re-fetch, and it did not previously surface anywhere in the task chain until this synthesis pass checked it.

---

## 2. The causal/geometric category of the Carrollian null-infinity boundary

**(Sketch — standard differential-geometric characterization, argument structure complete, not independently rederived from first principles this session.)**

$\mathcal I^\pm$ is **neither Lorentzian-interior nor Euclidean-timeless**; it is a third causal category, Carrollian, and this is not merely descriptive novelty:

- **Not Lorentzian-interior.** $\mathcal I^+$ is a null hypersurface, not a timelike one. It carries no interior proper-time parameter — no massive worldline reaches it, only massless (null) geodesics terminate there, and $d\tau=0$ along any curve confined to it. The induced metric is degenerate, not indefinite.
- **Not Euclidean.** A positive-definite metric admits no nonzero vector $n^a$ with $h_{ab}n^b=0$ — the defining Carrollian degeneracy is structurally impossible in Euclidean signature. This is not a subtle point; it is a direct algebraic obstruction (a positive-definite form has trivial kernel).
- **What it is instead.** The $c\to 0$ Carroll contraction of the Poincaré algebra: a degenerate spatial metric $h_{ab}$ plus a preferred kernel direction $n^a$ whose flow is "Carrollian time" (ultra-local, ultra-slow in the sense that Carrollian time translations decouple from spatial dynamics). The conformal Carrollian symmetry group at $\mathcal I^\pm$ is isomorphic to BMS.

**The synthesis-level point neither position stated quite this way:** this third category is exactly as real and exactly as much "extra structure" as it sounds. Position B's Attack 1 Site B is correct that $n^a$ is a preferred-direction structure by construction, not an emergent one — this is the honest cost of adopting Carrollian boundary geometry at all. Whether this cost is *acceptable* relative to Axiom `ax:nobackground` is addressed in §7, not resolved here; §2's job is only to state precisely what kind of object is being proposed, and the answer is: a specific, non-generic, degenerate causal structure that exists only given (a) asymptotic flatness and (b) a chosen conformal completion. It is not "no structure," and issue #166's framing of it as "interesting novel category" (true) should not be read as "therefore free of the axioms' concerns" (not established).

---

## 3. Adversarial critique — hidden assumptions, axiom-by-axiom

### 3.1 Position A's mechanism, restated precisely

Clock subsystem: $M(u, z_0, \bar z_0)$, the Bondi mass aspect at one *fixed angle* on the celestial sphere, treated as the conditioning variable $c$ in Definition `measure_pw`, with the rest of the radiative data ($S$ = news tensor at all other angles/$u$, mass aspect at other angles) as the conditioned system. $u$ itself is explicitly *not* the clock (Position A rejects this framing as a category error against `measure_pw`'s $\Sigma$-indexing). Retarded time is emergent, recovered as "the reading of this clock." The mechanism routes through the marginal-Hilbert-space Conjecture `conj:qm`'s field-configuration-space language, taking $\mathcal R \to \mathcal I^+$ as a limit, rather than through the smooth-structure-indexed `measure_pw` literally.

### 3.2 Hidden assumptions and smuggled structure — checked against all three axioms

**`ax:nohilbert` (no fundamental Hilbert space).** The mechanism's formal machinery (Definition `measure_pw`, a complex measure with no presupposed inner product) is reused unmodified — this is a genuine strength, not a new construction. **But there is a live trap, and Position A named it before I could:** celestial holography *as practiced* in the mainstream literature (celestial CFT correlators, OPEs, primary operators) is built on the S-matrix Hilbert space of asymptotically flat QFT — exactly what `ax:nohilbert` forbids. Position B's Attack 5 independently demonstrates what happens if this trap is not avoided: importing GFT-style fixed kinematical Hilbert-space scaffolding (Branch 1) reintroduces, verbatim, the same problem the paper already rejects for the standard Page–Wootters mechanism (L928–931: presupposes $\mathcal H = \mathcal H_{\text{clock}}\otimes\mathcal H_{\text{system}}$). **This is where the two positions' independent work directly interlocks rather than merely coexists:** Position A pre-emptively disclaims exactly the move Position B shows to be fatal — A's own §3 states the mechanism must use "only the classical/geometric content of the celestial-Carrollian literature... never the celestial CFT's operator-algebra/Hilbert-space content," and treats the Calcinari–Gielen GFT precedent as "structural evidence the strategy isn't obviously inconsistent," explicitly not as a proof template being imported. **Given this, Attack 5 Branch 1 is correct in general but does not land on Position A's actual (already-hedged) proposal — A never proposed importing the fixed Hilbert space.** Attack 5 Branch 2 (once the Hilbert space is stripped, the Calcinari–Gielen precedent no longer proves anything, and the citation reduces to weak circumstantial evidence) is the version that actually engages A's claim, and A already concedes exactly this weight ("not a technical template I'm importing"). **Verdict: `ax:nohilbert` compatibility is Sketch-level defensible, contingent on a discipline both positions — independently — converge on requiring.** No postulate is needed here *if* that discipline holds; whether it can be maintained through a full derivation (rather than an intention) is untested.

**`ax:nobackground` (no fixed metric, foliation, or presupposed dimensionality/signature).** Two distinguishable structures are in play, and they should not be graded the same:
- *The conformal completion + asymptotic-flatness fall-off class.* Genuinely extra structure beyond a generic Lorentzian 4-manifold: a falloff condition plus a choice of conformal factor $\Omega$ ($\Omega=0,\,d\Omega\neq0$ at the boundary). Position A argues, and I agree, this is weaker in *kind* than what the paper already treats as an outright `ax:nobackground` violation for Osterwalder–Schrader reconstruction (L1784–1788: OS needs a *global* flat Euclidean background with full $E(4)$ invariance — the entire bulk geometry is fixed, not merely its asymptotics). Asymptotic flatness constrains only the falloff at infinity; the bulk remains dynamical. This is a real distinction, not a rhetorical softening — but "lighter than the worst case already rejected" is not "zero cost," and neither position shows Level 0–1 self-consistency *selects* this falloff class rather than it being imposed by hand.
- *The Carrollian kernel vector $n^a$.* Position B's Attack 1 Site B is the sharper of the two: $n^a$ is not incidental machinery, it is the definition of what makes the boundary geometry Carrollian at all — a preferred direction, structurally comparable in kind (though forced by, not freely chosen atop, the null geometry) to a preferred foliation. I do not find a clean resolution to this in either position. It is mitigated, but not dissolved, by noting that the paper's general modus operandi already provisionally fixes structure (e.g., a signature) as scaffolding for a Level-2 derivation, with that structure itself understood as eventually Level-0-emergent — $n^a$ being *forced by* the asymptotically-flat/null choice, rather than independently posited, places it in the same category as that already-tolerated pattern, *provided* the falloff-class-selection gap above is eventually closed. Until it is, $n^a$'s status is parasitic on an open question, not independently resolved.

**`ax:timeless` (no preferred slicing).** The $u$-slicing of $\mathcal I^+$ is gauge under BMS supertranslations, and this is genuinely well-defended — it parallels how the paper already licenses clock-choice-dependence as a feature (Kuchař/Marletto–Vedral, L1766–1773). **But this defense applies cleanly only to Position A's actual, localized design** ($M$ at one fixed angle $(z_0,\bar z_0)$), not to $u$ treated as a bulk-wide structure. Position B's sharpened Attack 2 (locality/universality disanalogy: proper time $\tau$ is worldline-relative from the outset; $u$ at $\mathcal I^+$ is shared by the entire boundary, reintroducing exactly the universal time `sec:signature_time` rejects, L902–904) is a real critique of the *naive* "condition on $u$" framing — but Position A's mechanism was never that framing; A explicitly rejected "$u$ itself as the clock" as a category error in its own §2, for independent reasons, before B's attack existed to answer. **The two positions' independent design choices converge here too, in a smaller way:** A's insistence on a single-point angular localization is functionally a response to exactly the globality problem B later names, arrived at from the opposite direction (a formal type-checking requirement against `measure_pw`, not a `sec:signature_time` universality worry). This is a second, smaller instance of the same evidential pattern as the headline Level-2 convergence: independent lines of attack landing on the same fix. **What survives as still-open:** B's residual point that unbroken BMS supertranslation gauge freedom means "the clock value" isn't well-defined without an additional frame choice — is that frame choice reducible to "pick a subsystem $\mathcal R$" (already licensed) or does it require something categorically new (e.g., an asymptotic Poincaré subgroup / origin choice never needed by the massive-clock story)? Neither position resolves this. **Verdict: survivable specifically for A's localized design, with one genuinely open technical question (BMS-frame selection) left unanswered by either side.**

### 3.3 Time evolution sneaking back in — explicit check

Requested explicitly by the assignment: can time evolution sneak back in? The honest answer is *partially, and named*. The generator of $u$-dependence in Position A's mechanism is the Bondi mass-loss/constraint equation — a genuine constraint relating $M$ and the news tensor, not a Hamiltonian on a fixed background, which is the right shape of object per `ax:timeless`. But Position A's own item 4 in its gap list is exactly this concern: nothing shows this generator "reduces to something Schrödinger-equation-like upon marginalization" in the sense of the existing Remark on why marginalization produces quantum statistics (L1585–1598) — it is asserted plausible by analogy, not derived. This is the same gap structure the massive-clock Level-3 story itself has not fully closed either (that Remark is explicitly about *why* the analogy should work, not a completed derivation) — so this is a pre-existing open question in the program's Level-3 machinery generally, not a new defect specific to the boundary-clock proposal. Noted, not resolved, not counted against this proposal specifically.

### 3.4 Preferred observer or foliation — explicit check

Covered above (`ax:nobackground`/`ax:timeless` analysis): the angular choice $(z_0,\bar z_0)$ is licensed as clock-relativity (a feature); the BMS-frame ambiguity is a genuinely open question; the conformal completion and $n^a$ are real, only partially mitigated costs. No hidden foliation beyond what is named.

---

## 4. Defense assessment — fatal vs. solvable

| Attack | Fatal or solvable? | Reasoning |
|---|---|---|
| Position A: "$u$ itself as clock" doesn't type-check against `measure_pw` | **Self-refuted correctly by A** — not an attack, a design correction A made against its own first instinct | — |
| `ax:nohilbert`: celestial-CFT operator content is a trap | **Solvable, contingent on discipline** | Both positions independently converge on requiring this discipline (§3.2); untested through a full derivation, not shown fatal |
| Attack 5 Branch 1 (import fixed kinematical Hilbert space) | **Would be fatal if attempted, but doesn't touch A's actual proposal** | A explicitly disclaims this move; Branch 1 is correct as a general warning, moot as an attack on A's stated design |
| Attack 5 Branch 2 (GFT precedent evaporates once stripped) | **Solvable / already conceded** | A already treats the precedent as weak circumstantial evidence, not a proof; B's point is correct but not damaging beyond what A already admitted |
| `ax:nobackground`: conformal completion + falloff class | **Open, unresolved, not shown fatal** | Weaker in kind than the already-rejected OS precedent; no derivation shows the falloff class is selected rather than assumed |
| `ax:nobackground`: Carrollian kernel $n^a$ | **Open, unresolved, not shown fatal** | Real preferred-direction structure; partially mitigated by "forced-not-free" framing, contingent on the falloff-class gap above |
| `ax:timeless`: bare "$u$ is global time" | **Refuted** (proves too much, symmetric with proper time $\tau$) | Position B's own counter-defense |
| `ax:timeless`: sharpened locality/universality of $u$ | **Solvable — already partially addressed by A's design** | A's single-point angular localization is a real (independently arrived-at) answer; residual BMS-frame-selection question remains open |
| Attack 3: Level-2 anchor incompatibility (asymptotic flatness excluded by fixed-point-existence L85/M3) | **Not fatal by logical necessity, but currently a hard, undischarged blocker in practice** | Nothing forces the boundary and the Level-2-established bulk region to coincide (B's own counter-defense) — but no example or general argument currently supplies *any* self-consistent, asymptotically-flat, radiating Level-2 fixed point for the boundary to attach to, from either direction (§5) |
| Attack 4(a): $i^+$ vs $\mathcal I^+$, bulk reconstruction unbuilt | **Currently unfilled, not shown unfillable** | Both positions independently name this as missing machinery (A's own gap-list item 7; B's own counter-defense to its own attack) |
| Attack 4(b): $\mathcal I^\pm$ data is global vs. `conj:qm`'s bounded-region scope | **Open, unresolved** | A's own gap-list item 2: `conj:qm` is stated for bounded intermediate regions; nothing shows it survives the $\mathcal R\to\mathcal I^+$ limit |

**No attack from either side is a clean, standalone fatal flaw against a properly-hedged version of Position A's specific mechanism.** But the cumulative weight of the open items, combined with §5's finding, means the mechanism currently has no target to be tested against even if every open item above were resolved favorably.

---

## 5. Structural convergence — the headline finding

**Position A**, working only from `programs/co-emergence/index.tex`, its README, OBJECTIVES, and the two 2026-03-03 co-emergence explorations, named as its single biggest blocker: *the program's only known self-consistent massless Level-2 fixed point — Starobinsky/de Sitter — has a spacelike future conformal boundary (cosmological, $\Lambda>0$), not the null boundary $\mathcal I^+$ Carrollian/celestial structure requires.* This is standard GR (de Sitter/FRW with $\Lambda>0$ has spacelike $\mathcal I^\pm$; only $\Lambda=0$ asymptotically flat spacetimes have null $\mathcal I^\pm$) and is independently corroborated by direct reading of `programs/co-emergence/explorations/2026-03-03-massless-fixed-point.md`, which states the Starobinsky solution is "consistent at Level 2 but empty at Level 3" for the *massive-clock* reason — Position A adds, correctly, that it is *also* the wrong causal type for a boundary-clock mechanism, independent of the mass question entirely.

**Position B**, working from `programs/fixed-point-existence/index.tex` and its M3 exploration — documents the assignment packet did not point either agent to, and which Position B found by following the co-emergence README's own citation of its Level-2 anchor — independently found: the program's general Level-2 existence machinery (the Banach-contraction argument) explicitly and structurally excludes asymptotically flat spacetimes (`fixed-point-existence/index.tex` L85, verified verbatim by this synthesis: *"The estimate also requires a compact Cauchy surface, so it does not cover Minkowski space or asymptotically flat backgrounds"*), for a reason (Gap M3) diagnosed in the M3 exploration as mass-independent — the obstruction is about the causal (Lorentzian Green-operator) character of the non-local response kernel, not about field mass.

**These are not the same fact restated — they are two independent facts that jointly close off both possible routes to a witness:**
- A shows the *one solution the program already has* is disqualified by causal type.
- B shows the *general method that would prove existence of a new one* cannot currently reach the required manifold class at all, for a structural reason unrelated to mass.

Neither position saw the other's evidence. That this same conclusion was reached from a cosmological-solutions document and a functional-analysis existence-proof document, independently, is stronger evidence than either finding alone that this is the actual, real bottleneck — not an artifact of how either position happened to frame the question. I treat this convergence as **Rigorous as a textual/logical fact** (both source claims are direct quotes/citations of committed repo text, verified by this synthesis directly against the files) and **Sketch as a "this is the binding obstruction" interpretive claim** (it is not proven that no other route to a witness exists — e.g., a method other than Banach contraction, per the M3 exploration's own suggested foliation-restricted repair, might eventually supply one).

**Secondary convergence, lower stakes but worth recording:** both positions, entirely independently, also flagged that boundary-to-bulk reconstruction (extending radiative boundary data to a statement about bulk unitary evolution — CE-7's actual done-condition) is currently unbuilt machinery for this program (Position A's gap-list item 7; Position B's own counter-defense to Attack 4(a)). This is a second, smaller instance of the same "genuinely independent replication" pattern, and is a distinct blocking item from the causal-type one — closing the causal-type gap does not by itself close this one.

---

## 6. Synthesized assessment: could this boundary structure supply the L1573–1576 "temporal reference"?

**(Conjecture, honestly not upgradable to Sketch given the open items in §4.)**

The mechanism itself — Bondi mass aspect at a fixed celestial angle, $M(u,z_0,\bar z_0)$, as the clock subsystem $c$ in Definition `measure_pw`'s field-configuration-space route, generated by the Bondi mass-loss constraint rather than a Hamiltonian — is specific, non-trivial, and not obviously wrong. It is the first proposal in this program's record to engage null infinity, Carrollian geometry, or celestial holography at all (confirmed zero prior hits by the literature search, §1.1). It correctly avoids the most obvious failure mode (treating $u$ itself as the clock) and, independently, avoids the failure mode Position B's Attack 5 would have caught (importing celestial-CFT Hilbert-space content). Its multi-fingered supertranslation-frame structure is a genuine, non-forced point of alignment with the paper's existing Kuchař-informed stance on clock-relativity.

It is also, honestly, **untested at every load-bearing step**: $\rho_{S|c}$ has not been computed; nothing shows it produces anything resembling unitary evolution in a semiclassical limit; the extension of `conj:qm` from bounded regions to the $\mathcal R\to\mathcal I^+$ limit is asserted, not shown; mutual consistency across different angular clock choices is not demonstrated; the bulk-reconstruction step (boundary radiative data → bulk unitary evolution, which is CE-7's actual done-condition) is not attempted.

Most importantly: **it currently has no self-consistent solution to apply itself to** (§5). A mechanism this underspecified, applied to a manifold class the program cannot currently construct, cannot be promoted past Conjecture regardless of how well-motivated its individual design choices are. This is the correct rigor label, not a hedge.

---

## 7. Does adopting this require a postulate beyond Axioms 1–3?

**Explicit finding, per issue #166 item 4, axiom-by-axiom (see §3.2 for full reasoning):**

- **`ax:nohilbert`**: **No new postulate required**, *conditional on* never importing celestial-CFT operator/Hilbert-space content — a discipline both positions independently converge on, but which is a design requirement going forward, not a proven-maintainable property of any completed derivation. Sketch-level defense.
- **`ax:timeless`**: **No new postulate required** for Position A's specific localized design (angle-fixed mass aspect); the naive "condition on global $u$" framing *would* smuggle back universal time, but that was never the actual proposal. One open technical question (BMS-frame selection) is unresolved and could yet turn into new unaxiomatized input — undetermined either way.
- **`ax:nobackground`**: **The honest answer is not yet determined.** Two distinct pieces of extra structure are required to even state the mechanism — the conformal completion/asymptotic-flatness class, and the Carrollian kernel $n^a$. Both are lighter, in a precisely stated sense, than the OS-reconstruction violation the paper already treats as an outright `ax:nobackground` failure elsewhere in this same section of the paper (L1784–1788). Neither position, nor this synthesis, can show that Level 0–1 self-consistency *selects* the asymptotically-flat falloff class rather than the class being adopted by hand. **This is the one place where "requires a postulate beyond the axioms" remains a live, unresolved possibility** — not established, not ruled out.

**Overall: not shown to require a new postulate, but not shown to avoid one either — a genuinely open finding on the framework's hardest axiom (`ax:nobackground`) for this specific proposal**, which is itself moot in practice until §5's prerequisite is resolved, since there is currently nothing to check the falloff-class-selection question against.

---

## 8. Level-0 manifold-class compatibility

**(Conjecture; small/large exotic-$\mathbb R^4$ distinction explicitly flagged unverified this session, per Position A — not independently checked by this synthesis either, for the same reason: it does not affect the §5 verdict and further search budget was better spent on the citation-integrity check in §1.)**

Against README Open Problem 3's alternatives (verified verbatim: *"non-compact (exotic $\mathbb R^4$), manifolds with boundary, non-simply-connected"*):

- The mechanism requires a non-compact manifold admitting a genuine null conformal boundary (asymptotically flat / "asymptotically simple" in the standard Penrose/Hawking–Ellis sense). This is **incompatible** with the closed-simply-connected branch (independently obstructed, $\chi\ge3$) and, on a plain reading, does not obviously match "manifolds with boundary" as that phrase appears to intend finite interior boundaries (e.g. horizons) rather than conformal infinity — **this reading is itself unverified**; nothing in the record establishes what open problem 3's third alternative was originally meant to cover, and this should be checked against whatever motivated that line before anyone relies on it either way.
- **Best fit: the non-compact/exotic-$\mathbb R^4$ branch**, with a load-bearing sub-condition Position A named precisely and flagged unverified: differential topology distinguishes "small" exotic $\mathbb R^4$s (standard smooth structure recovered at large radius, exotic-ness confined to a compact core) from "large" exotic $\mathbb R^4$s (non-standard even asymptotically). Only the *small* case is compatible with a standard Bondi-type falloff; the *large* case would break the entire mechanism. This distinction is standard in the Gompf-style exotic-smoothness literature by Position A's own account, but was not verified by citation search this session by either Position A or this synthesis — **exploratory-tier, unverified, flagged explicitly per Methodology.**
- This is a genuine **bet against the program's own open mass-gap/topology direction**, not a neutral compatibility note: if the eventual topology-to-mass mechanism (the Asselmeyer–Maluga-adjacent direction surveyed in the 2026-03-03 mass-gap synthesis) turns out to need "large" exotic structure or a compact manifold, this Level-3 mechanism has no home regardless of how §5's prerequisite resolves. Not resolved here; flagged as a second, independent dependency the boundary-clock direction carries beyond the one named in §5.

---

## 9. Recommendation

**Do not open a CE-7 sub-milestone issue for the boundary-clock mechanism itself yet.** The mechanism is well-specified enough to be worth keeping on record (per Methodology, losing/blocked positions and their reasoning are not deleted — they may become relevant again), but it has nothing to act on, and working it now would be researching a mechanism against a manifold class the program cannot currently construct or has an explicit exclusion result against.

**The precisely-named next step, per both positions independently and this synthesis's own verification of the underlying texts (§5):**

> Establish or rule out a self-consistent, asymptotically flat, non-trivially-radiating (news tensor $N_{AB}\neq0$) Level-2 fixed point.

This is a `fixed-point-existence`-scoped question, informed by (not blocked by) the existing M3 obstruction, and directly relevant to the already-open, already-tracked `CE-12` milestone (signature-dependence of M3 vs. the Level-2 signature-blindness remark) — the two should very likely be coordinated rather than opened as fully independent issues, since CE-12 is already probing exactly the boundary of what the M3-obstructed proof technique can and cannot reach. I recommend the governor (not this synthesis) make the call on whether this becomes a new issue, an addition to CE-12's scope, or a new milestone informed by CE-12 — that adjudication is outside a synthesis agent's role per Methodology.

If and when that prerequisite is resolved favorably, this Exploration's §3–§8 constitute a ready-made starting map for the actual Level-3 mechanism work: the specific design (angle-localized Bondi mass aspect, not global $u$), the specific trap to avoid (`ax:nohilbert` via celestial-CFT operator content), the specific open technical questions (BMS-frame selection, `conj:qm`'s bounded-region-to-boundary-limit extension, bulk reconstruction), and the specific unverified sub-claims requiring a citation check before reliance (small-vs-large exotic $\mathbb R^4$, the meaning of README Open Problem 3's third alternative).

If resolved unfavorably (no such Level-2 fixed point exists, or existence is shown obstructed for a reason that also rules out asymptotic flatness generally), this entire direction should be recorded as **Withdrawn** at that point, not before — the current state is Conjecture-level negative, not disproven.

---

## Rigor label summary

| Claim | Label |
|---|---|
| Carrollian geometry, BMS symmetry, soft/memory/BMS triangle exist as described in the literature | Rigorous as established external results; citations exploratory-tier, several requiring correction (§1.2) before any reliance |
| Bondi mass-loss formula and NEC monotonicity | Rigorous (standard GR; exact normalization not independently rederived) |
| $\mathcal I^+$ is neither Lorentzian-interior nor Euclidean (§2) | Sketch |
| de Sitter/Starobinsky has spacelike, not null, future boundary | Rigorous (standard GR fact) |
| `fixed-point-existence` Level-2 anchor excludes asymptotically flat backgrounds (quoted L85 fact) | Rigorous (verified verbatim against repo text) |
| The two positions' convergent finding is the actual binding obstruction (not an artifact of framing) | Sketch |
| Position A's mechanism ($M(u,z_0,\bar z_0)$ as clock) is well-specified and internally consistent as a proposal | Sketch |
| The mechanism produces anything resembling unitary bulk evolution | **Not shown — Conjecture, untested at every load-bearing step** |
| `ax:nohilbert` compatibility (conditional on discipline) | Sketch |
| `ax:timeless` compatibility (for the localized design specifically) | Sketch, with one named open question (BMS-frame selection) |
| `ax:nobackground` compatibility | **Open — genuinely undetermined**, not resolved by either position |
| Overall answer to issue #166's core question | **Conjecture-level negative: blocked on a named, currently-nonexistent Level-2 prerequisite, not disproven** |
| Level-0 small/large exotic-$\mathbb R^4$ compatibility sub-claim | Conjecture, exploratory-tier, unverified this session |
| Citation-integrity finding (§1.2: 4/6 sampled author attributions fabricated) | Rigorous (independently verified by direct arXiv fetch, this synthesis) |

---

*Internal references: `programs/co-emergence/index.tex` (axioms §2 L164–186, `sec:signature_time` L882–907, `sec:time_hilbert`/`def:measure_pw` L909–963, `conj:qm` L1542–1576, Level-3 subsection L1749–1774, OS-reconstruction discussion L1770–1790), `programs/co-emergence/README.md` (Open Problem 3, L60), `programs/co-emergence/OBJECTIVES.md` (CE-7 L20, CE-12 L24), `programs/fixed-point-existence/index.tex` (L85), `programs/fixed-point-existence/explorations/2026-06-16-FPE4-M3-structural-obstruction.md`, `programs/co-emergence/explorations/2026-03-03-massless-fixed-point.md`, `programs/co-emergence/explorations/2026-03-03-mass-gap-synthesis.md`. External citations per §1.2 table; corrected author attributions verified by direct arXiv fetch (arXiv:2510.21651, 2602.02644, 2407.03432, 1712.03211, 1411.5745, 2402.14062, 1401.7026) during this synthesis session, 2026-07-17.*

**Process note (interactive-mode disclosure):** This Exploration was produced by a human-directed multi-agent debate (search-specialist researcher → two independent position agents → synthesis) run in an interactive Claude Code session, as a mock/dry-run of the `worker` routine against issue #166 — not by an autonomy-mode routine. No GitHub claim, comment, or PR was made by any agent in the pipeline; the human author reviewed and committed this file directly per METHODOLOGY.md's base Exploration process.

routine: interactive · model: claude-sonnet-5 (synthesis agent, human-directed dry run per issue #166 — not an autonomy-mode routine)
