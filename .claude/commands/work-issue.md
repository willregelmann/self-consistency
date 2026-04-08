---
description: "Select and work on a GitHub issue — recommends based on dependencies and impact"
arguments:
  - name: program
    description: "Program name (directory under programs/). If omitted, infer from open issues."
    required: false
---

You are selecting a GitHub issue to work on and setting up the contribution workflow defined in METHODOLOGY.md.

## Step 1: Gather context

Run these in parallel:

1. **Open issues**: `gh issue list --state open --json number,title,body,labels,assignees`
2. **Recent commits**: `git log --oneline -20`
3. **Current branches**: `git branch --list`
4. **Program README**: If $ARGUMENTS is provided, read `programs/$ARGUMENTS/README.md`. Otherwise, infer the program from the issues.

## Step 2: Analyze and recommend

For each open issue, assess:

- **Readiness**: Are its dependencies (blocks/blockedBy/informs) satisfied? Can it be started now?
- **Impact**: Does it fix a known error, prove an open conjecture, or unblock other issues?
- **Scope**: Is it a focused task (single PR) or a large research direction?
- **Momentum**: Does it build on work done in recent commits or explorations?

Rank the issues and recommend one. Present the recommendation with a brief justification, then list the other viable issues. Use this format:

```
## Recommended: #N — Title
[2-3 sentences: why this issue, what it builds on, what it unblocks]

## Other options
- #M — Title: [one sentence]
- #K — Title: [one sentence]
```

Ask the user which issue they want to work on (default to the recommendation).

## Step 3: Set up the workspace

Once the user selects an issue:

1. **Read the issue body** carefully for acceptance criteria, relations, and context
2. **Read the current paper** (`programs/<program>/index.tex`) — at minimum the relevant sections
3. **Read related explorations** mentioned in the issue body
4. **Create a branch**: `<program-name>/issue-<N>-<short-description>` from main
5. **Comment on the issue**: brief approach statement (what you plan to try and why)

## Step 4: Plan the work

Enter plan mode to design the approach before making changes. The plan should:

- Identify the specific sections/files that will change
- State the rigor level of the expected output (Rigorous/Sketch/Conjecture)
- List self-checks that will be performed (dimensional analysis, limiting cases, consistency, sanity)
- Note whether adversarial review should be requested

Present the plan for approval before proceeding.

## Step 5: Open a PR

After the work is complete and committed:

1. **Run self-checks** (dimensional analysis, limiting cases, consistency, order-of-magnitude sanity) and document results
2. **Push the branch**: `git push -u origin <branch-name>`
3. **Open a PR** linking to the issue, using this format:

```
gh pr create --title "<concise title>" --body "$(cat <<'EOF'
Closes #N

## Summary
<What was derived/changed and why>

## Rigor level
<Rigorous / Sketch / Conjecture — for each result>

## Self-checks
- [ ] Dimensional analysis: <result>
- [ ] Limiting cases: <result>
- [ ] Consistency: <result>
- [ ] Order-of-magnitude sanity: <result>

## Adversarial review
<Recommended / Not needed — and which mode: verification, stress testing, or both>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

4. **Report the PR URL** to the user

## Important constraints

- **Do not start work without user selection.** The recommendation is a suggestion, not a decision.
- **Follow METHODOLOGY.md exactly.** Branch naming, commit style, self-checks, PR format.
- **Read before writing.** Always read the current state of files before proposing changes.
- **Claim the issue.** Comment on the selected issue with your approach before branching.
