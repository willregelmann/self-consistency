# Position A: The θ↔signature identification is the co-emergence critical path — add CE-10 at the top of OBJECTIVES

**Author:** position agent A (governor debate, 2026-06-11) · **Model:** claude-fable-5

## Thesis

Issue #81 / PR #89 — derive the complex self-consistency weight from metric signature, or document the obstruction — is the single most load-bearing open problem in the co-emergence program, and it currently maps to **no milestone** in `programs/co-emergence/OBJECTIVES.md`. The experimenter has already routed it into the loop via `experimenter-priority`, the worker has already produced a substantive PR (#89, in quorum), and the experimenter's own issue text nominates it as "a candidate `OBJECTIVES.md` milestone (CE-10)". The governor's job this month is to make OBJECTIVES reflect reality: add CE-10, place it first in the ordering, and thereby (i) make the topic-drift metric count this work as on-objective instead of as drift, and (ii) unlock the scout to open the follow-on issues that PR #89 has already generated.

## The case

### 1. It is the program's weakest load-bearing link (research claim)

**(Sketch — structural assessment, grounded in issue #81 and `programs/co-emergence/index.tex` §3.)** The paper's signature-selection mechanism rests on the passage at `index.tex` lines 269–289: complex weights come from the Lorentzian action *by analogy* with the path integral ("the weight $e^{iS/\hbar}$ is a complex phase… On a Riemannian manifold, the corresponding weight $e^{-S_E/\hbar}$ is real and positive"). Nothing in the model derives the complex weight from a metric; θ≠0 is *identified* with Lorentzian signature by stipulation. Issue #81 (experimenter-authored) states this plainly: "This is the paper's weakest load-bearing link… A skeptic reads the headline result as 'complex weights in, complex amplitudes out.'"

Every headline numerical and rigorous result in the program inherits its physical *interpretation* from this identification:

- CE-1's interference metric $I_S = S(\mathrm{Re}\,\rho) - S(\rho)$ (merged PR #74, red-team audited clean 2026-06-11) certifies that the entropy excess is *quantum*; that this quantumness has anything to do with *signature* is exactly the θ↔signature link.
- CE-2 (imaginary-fraction rank dependence) and CE-7 (Level 3 dynamics) study the phase structure whose origin #81 interrogates.
- The README's headline ("self-consistency with a time-like geometry *forces* the wavefunction to develop complex phases") is true as advertised only if the complex weight follows *from* the geometry. **(Sketch)** — this dependence reading is structural, not a theorem, but it is the same reading the experimenter committed to in #81.

A program whose ordered objective list omits its own weakest load-bearing link is mis-ordered. The OBJECTIVES header itself says "Ordering reflects priority: prefer the checkable frontier (proofs, numerics)" — and #81 *is* checkable frontier: PR #89 delivers Rigorous lemmas (elliptic positivity, polarization-independent hyperbolic cancellation), a Rigorous algebraic identity recovering the stipulated weight exactly at $\varepsilon = 1/(1+\theta)$, numerics to 1e−13, and 18 new pytest tests (PR #89 description). This is not interpretive framework work; it is precisely the kind of work the ordering rubric says to prefer.

### 2. The experimenter has already signaled direction; OBJECTIVES is lagging the record (process claim)

Grounded in the record:

- `AUTONOMY.md` defines `experimenter-priority` as "issue jumps the worker's ranking; **the human entry point into the loop**." Issue #81 carries it. This is the only experimenter-priority research issue in play at T+2, immediately following an experimenter-authored demotion wave (#71–#73, #84) that demoted the Banach anchor and withdrew the Planck-boundary claim. The human's direction signal could not be clearer: after stress damaged the Level-2 anchor, the experimenter pointed the program at its other foundational soft spot.
- Issue #81's closing section is literally addressed to this debate: "**Note for the governor** — If claimed, this is a candidate `OBJECTIVES.md` milestone (CE-10: 'Signature → complex weight: derivation or documented obstruction') — currently it maps to no listed milestone." The experimenter pre-named the milestone ID and title. Adding CE-10 is the lowest-risk governance edit available: it ratifies an explicit human nomination through exactly the channel `AUTONOMY.md` prescribes (governance-labeled PR, @-mention, quorum-gated, watched by T4 per `EXPERIMENT.md` design-risk #2).
- The governor is "the only routine that edits OBJECTIVES files" (`AUTONOMY.md`). If the governor does not act this cycle, the lag persists for a month — a third of the demonstrated half-life of the program's rigor labels.

### 3. The topic-drift metric and tripwire T4 will misfire without this edit (process claim)

Grounded in `EXPERIMENT.md`: health metric 5 measures "distribution of merged work across OBJECTIVES milestones vs. work outside any milestone," and tripwire T4 fires at ">50% of merged PR volume in a trailing 4-week window outside any OBJECTIVES milestone."

The merged record at T+2 comprises three agent result-PRs: #78 (SCB-1), #74 (CE-1), #90 (salvage sign fix, issue #88). PR #89 is large — a dated exploration, a numerics module, 18 tests (PR #89 description) — and is in quorum now. If it merges with #81 mapped to no milestone, a substantial fraction of trailing-4-week merged volume is mechanically classified as off-objective. Whatever the exact volume arithmetic (see underspecification below), the *direction* of the error is certain and perverse: **work the human explicitly prioritized would be scored as drift.** T4's stated rationale is "topic drift / objective decay." Experimenter-priority work is the opposite of drift — it is the one place the human steers. A metric that counts the steering signal as decay measures the negation of what it was built to detect. The designed remedy is already written into `EXPERIMENT.md` (risk #2): OBJECTIVES changes are the sanctioned, T4-watched mechanism by which the objective function tracks genuine direction. This is that mechanism's textbook use case.

### 4. Without a milestone, the scout cannot feed this direction (process claim)

Grounded in `AUTONOMY.md` ("The scout opens issues only for OBJECTIVES milestones") and PR #89's own findings. The PR is generative, not terminal:

- The **polarization fork** (gap (c): real-crossing junction transport selects the real mode; the complex weight requires the Wick-contour polarization) is named as "the precise residue of the path-integral analogy" — an immediate, well-posed follow-on.
- **Lemma 3 robustness** (any real junction condition preserves reality) is explicitly left at Sketch — a candidate promotion issue.
- The **paper-framing update** (§3, abstract) is designated by both issue #81 and PR #89 as a follow-up issue-and-PR, deliberately excluded from #89's scope.
- PR #89 declares **informs #88** (θ→−θ as orientation reversal) and **informs #32/CE-1** (what $I_S$ does and does not detect).

Under the current OBJECTIVES, *none* of these follow-ons can be opened by the scout; every one requires the experimenter to hand-file it. The agent-ready queue (#91 cosmetic, #66 FPE-1, #33 CE-2, #29 CE-3) shows the system is not starving in general — it is starving *specifically in the direction the human pointed*. That failure mode converts the autonomous loop back into a human-driven one on exactly the program's critical path, defeating the experiment's purpose.

### 5. The demotion wave makes this more urgent, not less (process claim)

The 2026-06-10 demotions (#72: Banach contraction Rigorous→Sketch, Planck-boundary claim withdrawn; #84: propagation into co-emergence) weakened the Level-2 anchor that co-emergence cites (README: "Level 2 is signature-blind (massive) — Sketch"). The program's defensible core has contracted toward Section 3's phase results — which is precisely the section whose physical interpretation hangs on the θ↔signature link. When a program's anchor is demoted, the rational response is to harden the remaining load-bearing member. That is #81.

## Concrete proposed OBJECTIVES edit

A `governance`-labeled PR against `programs/co-emergence/OBJECTIVES.md`, @-mentioning the experimenter, making three changes:

**(1) Insert a new first row** in the milestone table (before the current CE-1 row):

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| CE-10 | Signature → complex weight: derive the θ↔signature identification or document the obstruction | Either (a) a merged Sketch-level derivation that the complex self-consistency weight follows from hyperbolic (Lorentzian) temporal mode structure, with every remaining gap named — in particular the polarization fork (real-crossing vs. Wick-contour) resolved or explicitly stated as the residual support of the path-integral analogy — or (b) a merged documented obstruction; AND in either case a follow-up PR updates §3 framing and abstract to state the derived-vs-stipulated status of the identification | Open (PR #89 in quorum) | #81 |

**(2) Reorder:** CE-10 first. Rationale recorded in the PR: it is upstream of the *interpretation* of CE-1, CE-2, and CE-7; it sits on the checkable frontier per the file's own ordering rubric; it carries the run's only `experimenter-priority` signal.

**(3) Bookkeeping correction (same PR):** CE-1's Status is stale — it reads "Open" although PR #74 merged the interference metric into Section 3 and the red team audited it clean on 2026-06-11, satisfying CE-1's stated done-condition. Update CE-1 Status to "Done (PR #74; red-team audit 2026-06-11)". This is grounded in the merged record and corrects the same defect (OBJECTIVES lagging reality) that motivates the CE-10 addition.

Note the Done= for CE-10 is deliberately *wider* than issue #81's done-condition: #81 closes on the exploration alone, but the milestone closes only when the paper says what the exploration found. This keeps the scout authorized to open the designated follow-up issues (paper reframing; polarization-fork attack; Lemma 3 robustness) under CE-10 rather than leaving them orphaned the day #89 merges.

## Where this position is underspecified

1. **T4 arithmetic is asserted directionally, not computed.** I have not verified how the metrics tooling defines "merged PR volume" (PR count vs. diff lines), whether experimenter-authored demotion PRs (#71–#73, #84) count in the denominator, or what the actual off-objective fraction would be if #89 merges unmapped. The claim that the fraction would be *misleadingly inflated* stands regardless; the claim that T4 would actually *fire* does not, and I do not make it.
2. **PR #89 has not passed quorum.** If the reviewer returns `revise` or `reject`, the milestone case survives (the issue and its experimenter nomination stand; milestones track problems, not PRs), but the "in quorum, about to distort the metric" urgency weakens, and the proposed Status cell would need rewording.
3. **The generalization is the real risk.** My position generalizes from "ratify this nomination" to "OBJECTIVES must catch up whenever `experimenter-priority` appears." `EXPERIMENT.md` metric 5 exists partly to detect "governor reward-hacking" — a governor that reflexively appends a milestone for whatever just merged turns OBJECTIVES into a trailing log and destroys the metric's independence. I distinguish this case by the experimenter's *explicit, pre-filed* CE-10 nomination in the issue body; but I have not specified the rule for the next case, where the signal is only the label. A synthesis should pin down whether label-alone suffices or an in-issue governor note is required.
4. **The Done= wording is mine, not the experimenter's.** Issue #81 nominated the ID and title; the (a)/(b)+paper-framing closure condition and the decision to scope follow-on issues under CE-10 (rather than as a separate CE-11) are my drafting judgments and are legitimately contestable.
5. **The downstream-dependence claim is a reading, not a theorem.** That CE-2 and CE-7 are "downstream" of the θ↔signature identification (Sketch, §1 above) is a structural assessment of how the paper's claims chain together. A defender of the current ordering could argue CE-2's rank-dependence question is well-posed for the stipulated weight regardless of its origin. I think the *physical significance* transfer still routes through #81, but I flag the distinction.
6. **Top-of-list placement vs. insertion below CE-1.** With CE-1 marked Done, "first open milestone" and "first row" coincide and the question is cosmetic; if the synthesis rejects my CE-1 status correction, the reordering claim must be re-argued against a live CE-1.
