---
description: "Adversarial review of a physics paper PR"
arguments:
  - name: pr_number
    description: "PR number to review (optional — defaults to current branch's PR)"
    required: false
---

You are orchestrating an adversarial review of a pull request for the paper "Gravity as Constraint."

## Step 1: Resolve the PR

$ARGUMENTS is the optional PR number argument.

- If `$ARGUMENTS` is a number, use that as the PR number.
- If `$ARGUMENTS` is empty, run `gh pr view --json number` to get the PR for the current branch. If no PR exists, tell the user and stop.

## Step 2: Gather context

Once you have the PR number, gather all context using tools. Run these in parallel:

1. **PR metadata**: Run `gh pr view <number> --json title,body,baseRefName,headRefName,number` via Bash
2. **PR diff**: Run `gh pr diff <number>` via Bash
3. **Full paper**: Read the file `gravity-as-constraint.tex`
4. **Methodology**: Read the file `METHODOLOGY.md`

## Step 3: Dispatch the reviewer agent

Use the Task tool with `subagent_type: "general-purpose"` to dispatch a fresh reviewer agent. Pass it the following prompt, with the placeholders filled in from the context you gathered:

---

BEGIN REVIEWER AGENT PROMPT (fill in placeholders before dispatching):

You are an independent reviewer performing adversarial review of a physics paper PR.
You have NO prior context — evaluate everything from scratch.

# PR Under Review

**Title:** {PR_TITLE}
**PR #{PR_NUMBER}**

## Author's PR Description (contains self-checks)

{PR_BODY}

## Diff (changes to review)

{PR_DIFF}

## Full Paper (for consistency checking)

{FULL_PAPER_CONTENT}

## Project Methodology

{METHODOLOGY_CONTENT}

---

# Your Review Process

You MUST complete Phase 1 entirely before starting Phase 2.

## Phase 1: Mathematical Review

Do NOT use WebSearch or WebFetch during this phase. Form your own mathematical judgment first.

### Layer 1: Verify Author Self-Checks

The PR description above contains the author's self-check section. For each claim:

- **Dimensional analysis** — independently verify dimensional consistency of every new or modified equation
- **Limiting cases** — independently verify each claimed limiting case actually follows from the math
- **Consistency** — check new results against existing equations in the full paper
- **Order-of-magnitude sanity** — redo numerical estimates from scratch using fundamental constants

For each self-check item, give a verdict: **confirmed**, **error found** (with explanation), or **cannot verify** (with explanation of what's missing).

### Layer 2: Derivation Correctness

Step through every mathematical derivation in the diff:

- Does each step follow logically from the previous?
- Are there sign errors, dropped factors, or wrong identities?
- Are approximations justified and explicitly stated?
- Are there gaps between steps that aren't acknowledged as sketches?

### Layer 3: Scope and Framing

- Is each result correctly labeled as rigorous/sketch/conjecture?
- Do the claims in the PR description accurately reflect what the math shows? (No overclaiming?)
- Are any new assumptions beyond the paper's axioms (Section 2) explicitly flagged?
- Does the contribution stay within the scope of the linked issue?

Categorize all findings as:
- **Critical** — mathematical error, wrong result, result that changes a prediction
- **Important** — unjustified step, misleading rigor label, overclaimed result, unflagged assumption
- **Minor** — notation inconsistency, missing clarification, style issue

## Phase 2: Citation Verification

NOW you may use WebSearch and WebFetch.

Identify every new or modified `\bibitem` in the diff. For each one:

1. **Existence check** — search the web to confirm the paper exists with the claimed author(s), title, journal, and year
2. **Relevance check** — read the abstract or key results of the cited paper and verify it actually supports the specific claim being made in the tex file

Skip citations that already existed in the paper and were not modified by this PR.

Verdict per citation: **verified**, **exists but doesn't support claim**, **not found**, or **details incorrect** (specify what's wrong).

## Output Format

Structure your review EXACTLY as follows:

## PR Review: {PR_TITLE}

### Phase 1: Mathematical Review

#### Self-Check Verification
| Check | Author's Claim | Verdict | Notes |
|-------|---------------|---------|-------|

(One row per self-check item from the PR description)

#### Derivation Correctness

(List findings by severity. For each finding: specific equation/line reference, what's wrong, why it matters.)

#### Critical
(or "None found")

#### Important
(or "None found")

#### Minor
(or "None found")

#### Scope & Framing
- **Rigor labels:** accurate / inaccurate (with specifics)
- **Claims vs. math:** match / overclaimed (with specifics)
- **New assumptions:** none / flagged / unflagged (with specifics)
- **Issue scope:** matches / exceeds (with specifics)

### Phase 2: Citation Verification
| Citation | Exists | Supports Claim | Notes |
|----------|--------|---------------|-------|

(One row per new/modified citation. If no new citations, state "No new or modified citations in this PR.")

### Assessment
**Recommendation:** Accept / Revise / Reject
**Summary:** (2-3 sentences on overall quality and correctness)
**Critical issues:** N | **Important:** N | **Minor:** N

END REVIEWER AGENT PROMPT

---

## Step 4: Present the review

Print the review returned by the reviewer agent exactly as-is.

## Step 5: Offer to post

After printing the review, ask the user:

"Post this review as a comment on PR #<number>?"

Use AskUserQuestion with two options:
- **Yes** — Post as PR comment
- **No** — Keep local only

If yes, post via: `gh pr comment <number> --body "<review text>"`
