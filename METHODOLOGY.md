# Methodology

This is a research-as-code project. The paper is the codebase, open problems are GitHub issues, and contributions are pull requests.

## Core Model

The default workflow is **agent-as-contributor, human-as-reviewer**. Agents work on branches, submit PRs, and the human author reviews and merges. On specific issues, the human can shift to real-time collaboration.

Every PR must target a specific issue. Speculative exploration that doesn't map to an existing issue should first propose a new issue for discussion before branching.

Agents have no merge authority. Only the human author merges.

## Rigor Standards

Every derivation in a PR must include self-checks documented in the PR description:

- **Dimensional analysis** — every equation must be dimensionally consistent.
- **Limiting cases** — the result must reduce to known results in appropriate limits (flat space, weak field, classical limit, etc.).
- **Consistency** — the result must not contradict other results in the paper or established physics within the framework's validity domain.
- **Order-of-magnitude sanity** — numerical predictions must be evaluated and compared against physical intuition.

After self-checks pass, the human reviewer can request **adversarial review**: a second agent is dispatched to critique the derivation, look for errors, and challenge assumptions. Adversarial review is optional but recommended for any result that would change a prediction or appear in the abstract.

An agent must never claim a result is proven when it has only been sketched. PRs should clearly label work as one of:

- **Rigorous** — every step follows from the previous with no gaps.
- **Sketch** — the argument structure is correct but steps are omitted.
- **Conjecture** — a plausible claim without a complete argument.

## Citation Discipline

Two tiers:

**Paper-grade (strict).** Any reference that would enter `\begin{thebibliography}` must be verified to exist. The agent must confirm the author, title, journal, and year, and must verify that the paper actually supports the claim being made. Web search is required, not optional. Fabricating a citation is the single most serious failure mode.

**Exploratory (honest).** In GitHub issues and PR discussions, agents may reference literature they have not verified, but must flag it explicitly: *"I believe Wald (1994) discusses this, but I have not verified the specific reference."* Unverified references must never be committed to the `.tex` file. When exploratory references are later promoted to paper-grade, they go through the strict verification process.

## Contribution Workflow

1. **Claim an issue.** Agent assigns itself to an open issue and comments with a brief approach — what it plans to try and why.
2. **Branch.** Create a branch named `issue-N-short-description` (e.g., `issue-3-noise-kernel-flat-space`).
3. **Work in commits.** Each commit should represent a coherent step. Commit messages should say what was derived or changed, not just "update paper."
4. **Self-check.** Before opening a PR, the agent runs through the rigor checklist (dimensional analysis, limiting cases, consistency, sanity check) and documents results in the PR description.
5. **Open PR.** The PR links to the issue, describes the contribution, states the rigor level (rigorous/sketch/conjecture), and lists self-check results.
6. **Adversarial review (if requested).** The human reviewer can request a second agent to critique the PR.
7. **Revise or merge.** The human author has final say.

If an agent gets stuck or discovers the approach won't work, it comments on the issue explaining why and what it learned. Negative results are valuable — they narrow the search space.

## Version Tags

Tags mark stable states of the paper where all self-checks pass and the content is internally consistent. Not every merge gets a tag — only milestones where the paper stands on its own.

**Scheme:** `vMAJOR.MINOR` following the paper's lifecycle.

- **v0.x** — pre-submission drafts. Tag when a major section, derivation, or prediction set is complete and merged (e.g., `v0.1` fixed-point proof, `v0.2` decoherence rates, `v0.3` experimental predictions).
- **v1.0** — first public release (arXiv submission).
- **v1.x** — revisions in response to referee reports or community feedback.
- **v2.0** — major revision that changes the argument structure or adds significant new results.

**When to tag.** The human author creates tags after merging work that completes a logical milestone. A tag means: the paper compiles, all derivations have passed self-checks at the stated rigor level, and no known internal contradictions exist.

**Tag annotations.** Use annotated tags (`git tag -a`) with a message summarizing what the paper contains at that point. This serves as a changelog entry.

**Using tags in the workflow.**

- Adversarial reviews can be scoped to changes since the last tag.
- Issues and PR descriptions can reference tagged versions for context (e.g., "this addresses a gap in the v0.2 decoherence derivation").
- External references to the paper should cite a specific tag when possible.

## Guarding Against Known Failure Modes

**Hallucinated results.** The self-check and adversarial review requirements exist specifically for this. Additionally, agents must show work — a PR that states a result without the derivation is incomplete regardless of whether the result is correct.

**Ungrounded speculation.** Every PR must connect back to the paper's existing mathematical framework. If a contribution requires new postulates or assumptions beyond the three axioms in Section 2, this must be flagged explicitly in the PR description. The human author decides whether the new assumption is acceptable.

**Lost context.** All substantive work happens on branches tied to issues. Agents must read the current state of the paper and relevant issue threads before starting work. Discoveries that bear on other open issues should be cross-referenced with a comment on those issues.
