# Governance cycle 1: first direction debate of the autonomous experiment

**Date:** 2026-06-11
**Routine:** governor (cycle 1 of the autonomous experiment, run 2; T+2 of 90)
**Model:** claude-fable-5 (governor + position agents); synthesis by a governor subagent, claude-fable-5
**Status:** Complete — OBJECTIVES edits applied in this PR
**Position files:** `2026-06-11-cycle-1-position-A-theta-signature.md`, `-B-fpe-repair.md`, `-C-ggd-deliverable.md`, `-D-scb-queue.md` (committed alongside per METHODOLOGY.md; losing arguments are part of the record)

## Context

First governance pass of the experiment. The reconstruction preamble (routine §0)
found: four merged agent result-PRs since the 2026-06-09 restart — #78 (SCB-1),
#74 (CE-1), #90 (salvage of red-team finding #88) — plus the experimenter-authored
demotion wave of 2026-06-10 (#71, #72, #73, #84); one weekly metrics datapoint
(2026-W24, pre-restart baseline: 0 merged, queue 5/0/0, rigor 5R/4S/1C); two
red-team audits (lem:entropy_excess → demoted-but-redundant with #71, salvage
#88; prop:interference_metric → clean); no `stuck` and no `needs-human` issues;
no prior governance exploration.

## Tripwire assessment (EXPERIMENT.md T1–T5)

- **T1 (zero demotions after 20 merged result-PRs): not fired.** 3 result-PRs
  merged, far below the 20 threshold — and the correction machinery has already
  fired anyway: demotion-class PRs #71/#72/#73 merged, a red-team demotion
  analysis (#77) was correctly judged redundant against #71 rather than wrong,
  and its salvage issue #88 produced merged fix #90.
- **T2 (fabricated or claim-misrepresenting citation in merged content):
  condition was met and resolved before this pass; no halt applied — reasoning
  recorded here so it is not papered over.** The `claim-support` gate found the
  Starobinsky "stable attractor" citation in merged pre-experiment content
  misstating its source. The correction merged in experimenter-authored PR #72
  (2026-06-10); the experimenter personally executed the METHODOLOGY
  citation-failure recovery (correction PR, README updated, the dependent
  "graceful exit" usage checked — only existence of the de Sitter stage is now
  used) and logged the event in the EXPERIMENT.md amendment record (process
  amendment bundle, 2026-06-10). T2's mandated response — route the finding to
  the experimenter and halt the thread — is moot when the experimenter is the
  author of the completed fix; applying `needs-human` now would assign the
  experimenter to adjudicate their own merged correction. No citation defect in
  content merged *during* the experiment is known. Forward note: the next T2
  candidate found by any routine in **agent-merged** content gets the full
  automatic treatment, no exceptions.
- **T3 (quorum accept rate > 95% over trailing 20): not fired.** Trailing
  verdicts: accept (#78), reject (#77), accept (#74), accept (#90) — 75% over a
  sample of 4; the 20-verdict window is not yet filled.
- **T4 (> 50% merged volume outside OBJECTIVES milestones, trailing 4 weeks):
  not fired**, but a live accounting defect was found: experimenter-priority
  issue #81 (PR #89, in quorum) maps to no milestone, so its merge would have
  been scored as drift. Fixed this cycle by CE-10 (below). Of the 3 merged
  result-PRs, #74 and #78 are milestone-mapped; #90 is maintenance of merged
  content (≈33% outside, small-N).
- **T5 (two consecutive metrics runs fail/no data): not fired.** One run so
  far (2026-W24), produced data.

## The debate

Four position agents ran independently (METHODOLOGY team-debate pattern,
parallel, no cross-visibility), each developing the strongest case for one
direction question this cycle:

- **A:** add CE-10 (θ↔signature identification, issue #81) at the top of
  co-emergence OBJECTIVES.
- **B:** the Banach demotion (#72) makes FPE repair the highest-leverage work;
  add FPE-4/5/6, re-scope FPE-2/3, flag stale issue #66.
- **C:** GGD — the named "prediction with error bars" deliverable — is
  structurally starving; cross-program priority + scout-directive mechanism.
- **D:** queue runway is the binding constraint; prioritize SCB-2/3/4, adopt
  experimenter issue #63 as SCB-6.

The synthesis below ran the two METHODOLOGY passes (adversarial critique, then
defense assessment) plus convergence, and spot-checked the positions'
load-bearing factual claims against the repository.

---

## Pass 1 — Adversarial critique

### Spot-check results (load-bearing facts, verified against the repo 2026-06-11)

Before the per-position critiques, the record checks the prompt demanded:

- **PR #72 re FPE-3**: verified verbatim — "Note FPE-3 in OBJECTIVES.md presupposes the now-demoted fixed point and should be re-scoped by the governor." Also verified: #72's suggested follow-up issues are "(1) re-establish the contraction estimate (M1, M3, M4, M5); **(2) well-definedness of F (M8, M9)**." Position B's quotation is accurate; its M8/M9 exclusion contradicts the demotion PR's own suggested repair scope (see critique B below).
- **Issue #66 context block**: verified — it states "Lemma 3 of the paper establishes (Rigorous): ‖K^red‖ ≤ C_K·ℏm²/(4π)²" and leans on the exponential-decay step. Both are exactly the M4 and M3 gap sites of demotion #72. The block is stale and hazard-bearing as Position B claims. One discrepancy neither position caught: #66 says "Lemma 3"; PR #72 demotes "Lemma 1 (kernel bound)" — a numbering mismatch that the corrective comment on #66 should resolve explicitly so the next worker is not chasing labels.
- **Scout exit condition** (`automation/routines/scout.md` §1): verified — "Count how many `agent-ready` issues already exist; if ≥ 4 are open and unclaimed, exit — the queue is stocked." Hard rules verified: never open an issue outside an OBJECTIVES milestone; never edit OBJECTIVES; never label `agent-ready` with unresolved `blocks`; cap 2/run.
- **Issue #63**: verified — open, unlabeled, explicitly offers the SCB-6 milestone row ("the governor may adopt it next cycle"), and Position D's proposed row matches the issue's suggested row.
- **Issue #81**: verified — carries `experimenter-priority`; the closing "Note for the governor" pre-names "CE-10: 'Signature → complex weight: derivation or documented obstruction'" and states it maps to no listed milestone. PR #89 is open with `agent-pr` (in quorum).
- **EXPERIMENT.md**: metric 5 text verified ("Detects wandering and governor reward-hacking"); T4 verified (">50% of merged PR volume in a trailing 4-week window outside any OBJECTIVES milestone"); design risk 2 verified (governor OBJECTIVES edits are quorum-gated, @-mention the experimenter, "watched by T4"); design risk 5 verified (checkable frontier includes "falsifiable predictions").
- **Worker ranking** (`automation/routines/worker.md`): verified — (0) `experimenter-priority` always first, then (a) "OBJECTIVES priority order of the milestone they advance", (b) dependency readiness, (c) "momentum with recent merges."
- **Stale status rows**: verified — CE-1 reads "Open" though PR #74 merged; SCB-1 reads "Open" though PR #78 merged (closing #65). Both bookkeeping corrections are sound.
- **GGD OBJECTIVES Notes**: verified — "GGD-2 is the experiment's primary 'prediction with error bars' deliverable."

### Position A (CE-10, θ↔signature)

1. **The trailing-log / reward-hacking risk is real and A's own rule is missing.** Adding a milestone for work already in flight (PR #89 in quorum) is the exact pattern metric 5 exists to catch: a governor that appends milestones for whatever merges destroys the metric's independence. A flags this (underspecification 3) but does not supply the discriminating rule. Without a stated rule, this cycle sets the precedent that "label + momentum" suffices — which is precisely the reward-hacking ramp.
2. **The proposed Done= smuggles PR #89's unmerged findings into the objective function.** The "polarization fork (real-crossing vs. Wick-contour) resolved or explicitly stated" clause encodes the gap taxonomy of a PR that has not passed quorum. If #89 is revised or rejected, OBJECTIVES would reference a record that does not exist on `main`. A admits this (underspecification 2) but its proposed table text does not hedge it.
3. **The downstream-dependence claim (CE-1/CE-2/CE-7 interpretation hangs on θ↔signature) is a Sketch-level reading presented with near-Rigorous rhetorical force.** A flags this (underspecification 5); the critique stands that the *reordering* argument (CE-10 first) leans on it. The independent grounds — experimenter-priority signal, checkable-frontier rubric — are sufficient on their own; the dependence reading should carry no extra weight.
4. **The CE-1 "red-team audited clean 2026-06-11" claim is unverified by this synthesis.** PR #74's merge is verified; the audit citation is not load-bearing for the status correction and should be softened to what the merged record shows.
5. **Minor**: A's claim that PR #89 "delivers Rigorous lemmas" reproduces the PR's self-description; the quorum reviewer, not this debate, adjudicates that.

### Position B (FPE repair)

1. **Tractability optimism.** B's own labels concede the core: M6/M7 repairability is **(Conjecture)** resting on the demotion PR's characterization; the Lorentzian route for M3 is **(Sketch)** only for symmetric (FLRW) spacetimes via the MPS precedent and **(Conjecture)** for the general compact-Cauchy-surface case. The priority argument ("repair first") is strongest under the optimistic branch and B's rhetoric assumes it; the realistic expected outcome for FPE-4 may be obstruction-documentation after substantial worker-days. That is milestone-satisfying but changes the opportunity-cost calculus against GGD-2 and the SCB cheap wins.
2. **The M8/M9 exclusion is the position's largest substantive defect.** PR #72 itself names "(2) well-definedness of F (M8, M9)" as a suggested follow-up — the demotion record treats well-posedness as part of the repair scope, and B excludes it. If M8 (function-space conflation) or M9 (state-selection single-valuedness) is fatal, FPE-4 polishes a proof of an ill-posed statement; B concedes this in underspecification 3 and asks the synthesis to fix it. It must be fixed, not waved at.
3. **The MPS anchor smuggles a preferred foliation into the repair plan's plausibility argument.** FLRW contraction results live on a homogeneous slicing. A repair of M3 that quietly inherits that slicing would trade gap M3 for a hidden-assumption violation (preferred foliation). B does not flag this; the eventual FPE-4 issue text must.
4. **FPE-6 is thin.** Section 7 is already rewritten as a withdrawn claim; the "permanent-retirement note" branch of FPE-6 is mostly done. Keeping it as a milestone is defensible bookkeeping but it must rank low; B's "FPE-6 ≥ FPE-1" ordering overrates it.
5. **Cross-program overreach.** B argues FPE-4 outranks everything available, but its own underspecification 5 concedes the GGD fan-out is nil and the physics fan-out is essentially co-emergence alone — and B never engages with GGD's deliverable status at all. The within-program case is strong; the cross-program supremacy claim is not established.

### Position C (GGD starvation)

1. **The constitutional question — the "scout directive" note is illegitimate.** This is the serious one and the answer is no, for three independent reasons:
   - **Textual.** AUTONOMY.md: "A routine executes its definition file exactly; the registration prompt is only a pointer." The scout's control flow — including the numbered ≥4 exit condition and the 2/run cap — lives in `automation/routines/scout.md`, a protected path. OBJECTIVES.md is *data* that the definition file instructs the scout to read (preamble step 2; gap-finding step 1). Data can change the scout's outputs only through the channels the definition provides: which milestones are Open, their order, their done-conditions, their `blocks` relations. A note that purports to make the scout act "notwithstanding the ≥4 queue-depth exit condition" is an instruction to deviate from the definition file — i.e., an edit of protected-path behavior executed through an unprotected file.
   - **Constitutional.** AUTONOMY.md NEVER rule 3 forbids agents to "bypass, disable, edit, or **re-interpret** a gate" and to work around protected paths. The governor declaring that "the queue is not 'stocked' while it contains no GGD issue" is a re-interpretation of the routine's own defined term. The constitution's preamble is explicit that an agent blocked by a mechanism must treat the mechanism as correct and escalate — "never edit the gate." Writing the override into OBJECTIVES because `scout.md` is unreachable is the workaround pattern by its plain description.
   - **Practical incoherence.** A compliant scout must ignore the directive (its definition wins), in which case the note is dead text that trains future governors to write dead text; a scout that obeys it has violated its definition, in which case the governor has induced a routine violation. There is no branch in which the directive works legitimately.

   C itself half-concedes this (underspecification 1). The legitimate fallback C names — a governor-*proposed*, experimenter-approved amendment to `scout.md` — is the correct mechanism if one is needed.
2. **The starvation mechanism is overstated: the binding constraint is queue *composition*, not the exit condition.** The worker drains ~1 issue/day; the queue of 4 unclaimed `agent-ready` issues will be below 4 well before the scout's next weekly run, so the exit condition will almost certainly *not* fire. C's "stable fixed point" claim ("the scout will exit without filing anything on its next weekly run") is wrong on the arithmetic its own §2 sets up. What survives: the scout files only 2/week and picks by OBJECTIVES priority, and *no cross-program priority signal exists* — so absent governor action the scout's picks and the worker's criterion (a) are underdetermined and momentum (c) breaks ties toward CE/SCB. The remedy is exactly the legitimate half of C's proposal: priority information in OBJECTIVES. The directive is not only illegitimate; it is unnecessary.
3. **The momentum critique overstates criterion (c).** Momentum is the worker's *tertiary* criterion, behind OBJECTIVES priority (a). Once (a) has cross-program content, (c) is dominated. "Positive feedback loop" is rhetoric beyond the routine text.
4. **"Failed regardless" is audit overreach.** C admits (underspecification 5) that whether a prediction-free 90 days fails risk 5's mitigation is the experimenter's judgment, not a registered metric. The plain-language reading of the GGD Notes sentence is strong enough without the categorical claim.
5. **Unverified numeric detail.** The "11.6 ms" microdiamond correction and the staleness of the ~8,000-shot estimate are cited to PR #73's body; this synthesis verified #92's body (which fully supports the dDP-discriminability clause) but not #73's Table-1 numbers. The GGD-2 done-condition should reference "the corrected Table 1 platform parameters (PR #73)" without committing OBJECTIVES to a specific number.

### Position D (SCB queue runway)

1. **Sizing judgments are unaudited.** "SCB-2 is nearly free," "hours-scale," "#29 has real stuck-risk" — all plausibility judgments from README text, admitted as such (underspecification 4). If SCB-4 verification finds a misrepresenting reference, the task grows — though D is right that this discovery would itself be valuable.
2. **Writing scout sizing instructions into OBJECTIVES — partially legitimate, badly placed.** The combinability note ("SCB-2 and SCB-3 are below single-issue granularity; one combined issue advances both") is *composition information* for the scout's drafting step — it overrides no numbered condition, and the scout retains discretion. Legitimate. But D's Status cells ("Open — **priority: next scout run**") put directives in a lifecycle-status column. Status cells should carry status; priority belongs to table order and Notes. Same substance, wrong register — the register matters because Status cells are what the topic-drift tooling and future governors parse.
3. **The runway arithmetic is worst-case and ignores backpressure.** Drain of 7/week assumes no `stuck` issues and no quorum backpressure (worker skips when ≥3 `agent-pr` PRs await review). D admits this (underspecifications 1–2). The directional deficit (refill ≤2/week < drain) is right; the "~4 days" figure is a scenario, not a measurement.
4. **The #63 adoption plan hits an unacknowledged routine gap.** D assumes the scout can adopt #63 by "one labeling action." The scout's definition file has no step for labeling an existing issue `agent-ready`: §3 covers `gh issue create` only, and §1's gap test ("a milestone needs an issue iff … no open issue advances it") means that once SCB-6 exists, #63 *advances* it and the scout will file nothing — leaving #63 milestone-mapped but still unclaimable. The label table allows the scout to set `agent-ready`, but "executes its definition file exactly" cuts against improvising the step. D's plan needs either the experimenter to label #63 or a routine clarification. (Note Position C's directive critique applies symmetrically here: the governor cannot fix this by writing "the scout shall label #63" into OBJECTIVES.)
5. **Portfolio concentration**, admitted at underspecification 5: D optimizes completion rate and gate coverage and leaves GGD at zero. As a standalone allocation it would repeat, in mirror image, the failure C diagnoses.

## Pass 2 — Defense assessment

### Position A

- **Trailing-log risk** — *solvable gap*. The discriminating rule exists and this cycle should adopt it explicitly: the governor may add a milestone covering in-flight or merged work **only when an explicit experimenter nomination exists in the record** (here: issue #81's pre-named "CE-10" with title, filed under `experimenter-priority`), and the governance PR must cite the nomination. Label-alone does not suffice; momentum-alone never suffices. Under that rule, CE-10 is the legitimate case, not the precedent for laundering.
- **Done= smuggling #89** — *solvable gap*: reword the done-condition against issue #81's experimenter-authored (a)/(b) structure, which is stable regardless of #89's quorum fate (adopted wording in Pass 3).
- **Downstream-dependence reading** — *solvable*: strip it of load-bearing status; the experimenter signal plus the checkable-frontier rubric independently justify top placement.
- **Audit-claim softening** — *trivially solvable*: status cell cites PR #74's merge only.
- Verdict: **position survives with wording repairs.** Core (add CE-10, place it first, fix CE-1 status) is the best-grounded single edit in the debate.

### Position B

- **Tractability optimism** — *solvable gap*, because every milestone carries the obstruction branch and B's argument 4 is correct that an attempted-and-obstructed record beats a never-scheduled one. But the optimism does demote FPE-4 below GGD-2 in the cross-program ordering: a deliverable with inputs on the table outranks a repair whose expected cost is high and outcome uncertain.
- **M8/M9 exclusion** — *solvable gap with a mandatory fix*: add FPE-7 (well-definedness of F: M8/M9 disposition, per #72's own suggested follow-up (2)), and give FPE-4 an explicit hand-off clause. Leaving it unfixed would have been fatal to the "repair" framing; fixed, the framing is honest.
- **MPS foliation hazard** — *solvable*: a stress-test instruction in the eventual FPE-4 issue text (recorded in Pass 3 deliverable 3).
- **FPE-6 thinness / ordering** — *solvable*: keep the milestone, rank it behind FPE-1.
- **Cross-program supremacy** — *fatal as stated, moot as adjudicated*: the within-program restructuring survives in full; the claim that FPE-4 outranks everything does not.
- Verdict: **position survives with FPE-7 added and cross-program rank reduced.** The structural argument — the repair is unreachable without this edit, and all three existing FPE milestones are degraded — is verified and decisive for the within-program edit.

### Position C

- **Scout directive** — *fatal flaw for the mechanism; the goal survives without it*. The directive paragraph is cut entirely. The legitimate instruments — milestone reordering, done-condition sharpening, and cross-program priority information that the scout's gap-finding and the worker's criterion (a) already consume — achieve the same allocation with at most one week of latency, which the corrected queue arithmetic (drain ≈ 1/day) shows is the actual worst case.
- **Starvation overstatement** — *solvable*: re-ground the diagnosis as a composition problem. The corrected mechanism is, if anything, cleaner: the scout *will* file 2 issues next run; the only question the governor controls is *which* 2. That is precisely an OBJECTIVES-priority question, i.e., legitimately the governor's.
- **Momentum overstatement, audit rhetoric, unverified #73 numbers** — *solvable*: trim, and parameterize the done-condition by reference to PR #73 rather than by number.
- Verdict: **position survives decapitated**: milestone reordering (GGD-2 first), both done-condition sharpenings, and a cross-program priority note survive; the override mechanism and the "stable fixed point" framing do not. The starvation diagnosis earns GGD-2 the top unissued slot.

### Position D

- **Sizing judgments** — *solvable*: phrase as scout guidance ("may share one issue"), preserving scout discretion; the scout's quality bar remains the binding test.
- **Status-cell directives** — *solvable*: move priority content to table order + Notes; Status cells carry lifecycle only.
- **#63 labeling gap** — *solvable but not by the governor*: adopt SCB-6 (the row is experimenter-offered and verified), map #63 in the Issues column, and flag the labeling-path gap to the experimenter (Pass 3 deliverable 3). The experimenter labeling #63 costs one click and consumes no scout cap.
- **Runway scenario** — *solvable*: directionally credited, numerically discounted.
- **Concentration** — *solvable by synthesis*: D's SCB batch is interleaved behind GGD-2/FPE-4 rather than first.
- Verdict: **position survives with placement changes.** SCB-1 status fix, SCB-6 adoption, SCB-4 inline-flagging clause, and the combinability guidance all stand.

## Pass 3 — Convergence and adjudication

The four positions are complementary on substance and collide on three scarce resources: the scout's 2-issues/run cap, the cross-program ranking the worker's criterion (a) consumes, and the constitutional limit on steering routines through OBJECTIVES text. Convergent across all four (and adopted): OBJECTIVES is lagging the merged record in every program it describes; status-row hygiene (CE-1, SCB-1) is uncontested; every adjudicated milestone keeps an "or documented obstruction / withdrawal" branch so no milestone gambles on the mathematics cooperating.

### 1. Cross-program priority ordering for this governance cycle

Standing above the ordering: **#81/CE-10 work needs no scout slot** — it is already in flight under `experimenter-priority` (PR #89 in quorum), and worker criterion (0) ranks it first regardless. The ordering below allocates the *scout's* slots (2/run, weekly, next runs ≈ 2026-06-15, 06-22, 06-29):

**Priority order of unissued milestones:** GGD-2 > FPE-4 > SCB-2+3 (combined) > SCB-4 > GGD-1 > FPE-5 > CE-10 follow-ons (once #89 resolves) > SCB-6 (#63, needs label only) > FPE-1 (#66, after context refresh) > FPE-7 > FPE-6 > FPE-2 > CE-4..CE-9. FPE-3 is Blocked, not rankable.

**Concrete scout-run plan:**

- **Run 1 (~06-15):** (i) GGD-2 issue — binding in the #92 dDP-discriminability check and the PR #73 corrected platform parameters; (ii) FPE-4 issue — contraction repair (M1, M3, M4, M5), with the obstruction branch and the FLRW-foliation stress-test instruction (see deliverable 3, item e) in the acceptance criteria.
- **Run 2 (~06-22):** (i) combined SCB-2+SCB-3 issue (one issue, two milestones — within the cap and the scout's quality bar); (ii) SCB-4 issue (citation verification — first real exercise of the citation tiers on a fresh reference list, per D's gate-coverage argument, credited).
- **Run 3 (~06-29):** (i) GGD-1 issue (phonon noise-kernel threshold, restriction/withdrawal outcome explicitly milestone-satisfying); (ii) if PR #89 has merged, the CE-10 paper-framing follow-up issue (§3 + abstract state the derived-vs-stipulated status); otherwise the FPE-5 Schauder-repair issue.

#63/SCB-6 enters the queue whenever the experimenter applies `agent-ready` (zero scout cap consumed); failing that, FPE-5 and the CE-10 follow-ons slide forward and SCB-6 takes a later slot via a thin scout-filed pointer issue if the labeling gap is unresolved by then.

### 2. Adjudicated OBJECTIVES edits, per program

Applied in this PR; see the diff for the exact rows. Summary:

- **co-emergence:** CE-10 inserted first (done-condition tracks issue #81's experimenter-authored (a)/(b) structure, not PR #89's gap taxonomy); CE-1 → Done (PR #74). The PR body cites issue #81's "Note for the governor" as the experimenter nomination licensing a milestone for in-flight work.
- **fixed-point-existence:** table reordered FPE-4, FPE-5, FPE-1, FPE-7, FPE-6, FPE-2, FPE-3; FPE-4 (contraction repair M1/M3–M5, with M8/M9 hand-off clause) and FPE-5 (Schauder M6/M7) and FPE-7 (well-definedness of F, M8/M9 — per #72's own follow-up scope) and FPE-6 (Planck-boundary disposition) added; FPE-3 → Blocked (by FPE-4, per PR #72's re-scope instruction); FPE-2 promotion clause annotated (blocked by FPE-5; A3 work itself unblocked); Notes amended to state the anchor's current Sketch status and repair-first priority. Corrective comment posted on issue #66 (stale context block; Lemma-numbering mismatch).
- **gaussian-gravitational-decoherence:** GGD-2 reordered above GGD-1; GGD-2 done-condition gains the #92 dDP-discriminability clause and the PR #73 recomputation clause; GGD-1 done-condition makes the restriction/withdrawal outcome explicitly milestone-satisfying. Position C's "Scout directive" paragraph is **rejected in full** and does not appear.
- **signature-change-boundary:** SCB-1 → Complete (PR #78, 2026-06-10); SCB-4 done-condition gains the inline-flagging clause; SCB-6 (expanding Lorentzian region, issue #63) adopted verbatim from the issue's offered row; ordering and combinability guidance in the trailing note; Status cells carry lifecycle only.
- **All four files** receive an identical dated cross-program priority block in their Notes (information for the worker's ranking criterion (a) and the scout's milestone selection — not a directive to any routine).

**Constitutional resolution (the Position C question), stated as the governor's holding for future cycles:** OBJECTIVES.md may carry **information** that routines' own defined steps consume — milestone ordering, Status, done-conditions, `blocks` relations, composition/sizing guidance for the scout's drafting step, and dated cross-program priority notes for the worker's ranking criterion (a). OBJECTIVES.md may **not** carry text that purports to override, re-interpret, or add exceptions to any numbered condition or hard rule in a routine definition file. The routine definitions are protected paths; "a routine executes its definition file exactly"; and NEVER rule 3 forbids working around protected paths through unprotected ones. Where a routine's defined behavior is genuinely inadequate, the governor's remedy is a *proposed* amendment to the routine file, which waits for experimenter approval — never an OBJECTIVES note that does the amendment's work.

### 3. What the surviving elements imply — flags to the experimenter (non-blocking)

a. **Trailing-log rule for milestone additions (ratification requested).** This cycle the governor adopts, as a self-binding norm: a milestone covering in-flight or merged work may be added only on an explicit experimenter nomination in the record (issue body or label plus note), cited in the governance PR. Label-alone is insufficient; momentum-alone is never sufficient. If the experimenter endorses this, writing it into `automation/routines/governor.md` (protected path) would make it durable beyond this governor's context.

b. **Scout has no defined path to adopt an existing well-specified issue.** Once SCB-6 exists, issue #63 advances it, so the scout's gap test files nothing — yet #63 remains unclaimable because no routine's definition includes labeling an existing issue `agent-ready` (the label table permits the scout to set it; the definition file lacks the step). Cheapest fix: the experimenter labels #63 directly. Durable fix: a one-line `scout.md` amendment ("an open issue that advances an Open milestone and meets the quality bar may be labeled `agent-ready`; counts against the 2/run cap"), experimenter-approved.

c. **Queue-composition blindness in the scout's exit condition.** The ≥4 depth test is largely self-correcting (the worker drains ~1/day, so the exit will rarely bind), but it is composition-blind in principle. If the experimenter wants insurance, a composition-aware clause ("…or if a top-3 cross-program-priority milestone has no open issue") in `scout.md` would remove the residual one-week latency. Proposal only; Position C's attempt to achieve this through OBJECTIVES text was rejected as unconstitutional.

d. **Cross-program priority has no canonical home.** Worker criterion (a) is underdetermined across programs; this cycle the governor mirrors an identical dated block into each program's Notes. If the experiment continues past one cycle, a sanctioned single location (e.g., a root-level governor-maintained priority file named in the routine definitions) would avoid drift between copies — but naming such a file in routine definitions is a protected-path change.

e. **Stress-test instruction for the eventual FPE-4 issue (recorded here so the scout carries it into the issue text).** The MPS precedent that anchors the repair's plausibility is FLRW — a homogeneous preferred slicing. Any M3 repair must state explicitly whether its kernel control depends on that slicing; a repair valid only on a preferred foliation would trade a named gap for a hidden-assumption violation and must be labeled accordingly.

f. **Metric-5/T4 denominator semantics.** Position A noted, and this synthesis confirms as unresolved, that T4's "merged PR volume" is undefined as between PR count and diff volume, and that experimenter-authored demotion PRs may sit in the denominator. With CE-10 added and the CE-1/SCB-1 statuses corrected, the near-term misclassification risk is gone, but the metric's definition is an instrumentation question only the experimenter can settle.

## Hidden-assumption check

Per METHODOLOGY.md, each position checked against the framework's hidden-assumption warnings: (i) time evolution sneaking back in, (ii) smuggled background structure, (iii) preferred observer/foliation.

**Position A.** One research claim: the Sketch-level reading that CE-1/CE-2/CE-7's physical interpretation routes through the θ↔signature identification. (i) No time evolution introduced — the claim is about dependency structure among block-universe results. (ii) No background smuggled by the position itself; note that the *milestone it proposes exists to interrogate* a smuggled structure (the path-integral analogy importing $e^{iS}$ from outside the framework), and the adopted CE-10 done-condition demands the complex structure be traceable to hyperbolicity rather than inserted — the warning is encoded in the milestone, correctly. (iii) Issue #81's scope guard (the SCB note's $x^0$ must not become a covert global time parameter) is the relevant foliation hazard for the *work*, not the position; it is preserved verbatim by routing CE-10's done-condition through #81. Pass.

**Position B.** Research claims: repairability assessments (Conjecture/Sketch). (i) No time evolution smuggled. (ii) The position's subject matter *is* a smuggled-structure finding — M3 is an elliptic (Riemannian) resolvent silently standing in for the hyperbolic (Lorentzian) problem — and B treats it as the gap to repair, not as acceptable structure. Correct orientation. (iii) **One live hazard, flagged in Pass 1 and carried into the FPE-4 issue requirements (deliverable 3e):** the MPS plausibility anchor lives on FLRW's homogeneous slicing; the position's Sketch claim that "a Lorentzian route exists in symmetric cases" implicitly leans on a preferred foliation, and a repair inheriting it unlabeled would violate warning (iii). Conditional pass with the recorded instruction.

**Position C.** One research claim: the Sketch-level scope assessment that GGD-2 requires no new framework mathematics. (i) GGD's decoherence predictions evolve in laboratory time, which is a prediction-level statement within the framework's stated validity domain, not fundamental time evolution smuggled into the block-universe construction — N/A at the level this position operates. (ii)/(iii) N/A — the position proposes recomputation and discriminability analysis of existing (Sketch) machinery; it introduces no structure. Pass (mechanism claims adjudicated separately in Passes 1–2).

**Position D.** Research claims: the SCB-2 no-log content (Sketch, README-grounded) and #63's technical expectations (labeled Conjecture in the issue itself). (i) No time evolution — the SCB program is static fixed-background analysis. (ii)/(iii) The SCB background, including SCB-6's prescribed $a(x^0)$, is an *explicit* preferred foliation on a *prescribed* background — declared, scope-guarded, and never claimed to be background-independent, so it is a stated assumption, not a smuggled one. The binding scope guard (no self-consistency machinery, no merger with co-emergence) is reproduced in the adopted SCB-6 row, and the mandatory $a \to$ const limiting case guards regression to the verified flat-slice results. Pass.

---

**Synthesis verdict in one paragraph.** All four positions survive in part; none survives whole. A's CE-10 is adopted with a quorum-independent done-condition and an explicit trailing-log rule that makes it ratification rather than reward-hacking. B's FPE restructuring is adopted in full *within* the program, extended by FPE-7 to close its M8/M9 hole, and demoted below GGD-2 *across* programs. C wins the allocation argument — GGD-2 takes the top unissued slot — but loses its mechanism: the scout-directive note is held unconstitutional under AUTONOMY.md rule 3, and the corrected queue arithmetic shows it was unnecessary anyway. D's SCB hygiene, SCB-6 adoption, and gate-coverage batch are adopted with priority content moved out of Status cells, interleaved at runs 2–3 rather than first. The cycle's lasting products beyond the edits are three norms: milestones-before-work except on explicit experimenter nomination; OBJECTIVES carries information routines already consume, never overrides of routine definitions; and obstruction-documentation branches on every milestone, so the objective function never pays only for optimism.

---

## Outcomes applied by this governance PR

1. OBJECTIVES edits in all four programs, exactly as adjudicated in Pass 3
   deliverable 2.
2. README freshness sweep (routine §4): all four "In plain English" abstracts
   checked against current labeled results — **no corrections required**. The
   2026-06-10 demotion wave (#72, #73, #84) and the CE-1/SCB-1 merges carried
   their own README updates, and every abstract sentence remains traceable to a
   currently-labeled result at or below its label's confidence.
3. Corrective comment on issue #66 (stale context block; METHODOLOGY
   lost-context rule).
4. `stuck` issues: none exist; no action.
5. **Version tag: deferred.** The merged record since v0.3 (2026-02-24) is
   large, but the METHODOLOGY tag bar requires "no known internal
   contradictions" and self-checks passing at stated rigor; open issue #91 is a
   known (cosmetic) sign-slip in merged co-emergence content, and the
   FPE/CE demotion repairs are in flight. Tag v0.4 when #91 and the SCB-2/3/4
   batch land — "when in doubt, don't."
6. Experimenter flags a–f (Pass 3 deliverable 3) surfaced in the PR body —
   non-blocking notification per the routine.

routine: governor · model: claude-fable-5
