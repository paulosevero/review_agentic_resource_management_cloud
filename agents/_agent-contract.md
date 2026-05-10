<!--
Shared contract referenced by every macro skill and internal sub-agent in this plugin:

  skills/01-bootstrap/SKILL.md
  skills/02-define-protocol/SKILL.md  (fuses v2's research-questions + search-string)
  skills/03-import-results/SKILL.md
  skills/04-screen/SKILL.md           (unified across title/abstract/full-text)
  skills/05-code-taxonomy/SKILL.md
  skills/06-analyze/SKILL.md
  skills/07-report/SKILL.md
  skills/prepare-pdf/SKILL.md         (auxiliary)
  skills/refine-bolding/SKILL.md      (auxiliary)
  skills/sheets-sync/SKILL.md         (auxiliary, opt-in Google Sheets)
  agents/add-reference-review.md
  agents/_router.md                   (state-aware fallback)
  agents/_screening-protocol.md       (shared by /04-screen)
  agents/_screening-classifier-runner.md
  agents/_screening-llm-reviewer.md

Each skill / sub-agent opens with:
  "Follow the shared agent contract in `agents/_agent-contract.md`.
   Stage-specific rules below override it when in conflict."

This file centralizes behavior that would otherwise be duplicated:
required structural sections, the canonical dialog flow, the textual-confirmation
rule, the rationale-recording rule, the lock/checkpoint discipline, and the
optional consultation of `reference-reviews/index.yaml`.
-->

# Agent Contract (shared)

Every pipeline agent in this plugin conforms to this contract. The goal is a
coherent user experience across stages, with predictable preconditions, dialog
shape, and exit behavior. Stage-specific rules override the contract only when
explicitly stated in the agent's own file.

## 1. Required structural sections

Every agent file must include the following sections, in this order. Section
titles must match exactly so that future automation can parse them.

1. `## What this stage does` — one paragraph, plain prose, naming the artifact
   the stage produces and the role it plays in the pipeline.
2. `## Preconditions` — bullet list of conditions that must hold before the
   agent does any work. Each bullet states the condition and the file or lock
   that proves it.
3. `## Inputs` — bullet list of artifacts the agent reads (CLAUDE.md sections,
   `protocols/screening.yaml`, `papers/paper-NNN.md`, `raw/exports/`, etc.).
4. `## Procedure` — numbered steps the agent follows. Each step is self-
   contained and references the dialog phases described in §2 of this contract.
5. `## Exit criteria` — bullet list naming what must be true for the stage to
   lock. Always includes a final textual-confirmation step (see §3).
6. `## Next step` — one short paragraph naming the next recommended command and
   the condition under which the user might want a different one.

## 2. Canonical dialog flow

Every agent runs the same six-phase dialog. Stage-specific procedures slot
their work into phases iii–iv; phases i, ii, v, and vi are invariant.

i. **Opening summary.** The agent's first message states (a) what the current
stage does in one or two sentences, (b) the criteria for advancing past it,
and (c) the next step the user should expect after the lock. This is non-
negotiable: the user must know where they are and where they are going
before any work begins.

ii. **Precondition check with fail-fast.** The agent verifies every entry in
its `## Preconditions` section. If any precondition fails, the agent stops
and reports each failing condition with the file path or lock value that
proves the failure. The agent does not attempt partial work to "make
progress" — it asks the user to resolve the precondition or to invoke the
appropriate prior command.

iii. **Elicitation.** The agent collects whatever information it needs from the
user (research questions, criteria, weights, target databases, etc.).
Elicitation is iterative: the agent proposes, the user edits or confirms,
the agent persists. The agent never silently picks a default; if a value
is unspecified, it asks.

iv. **Execution.** The agent performs the work documented in `## Procedure`,
writing artifacts to disk and committing intermediate progress when the
procedure says so. Long-running stages emit incremental commits per logical
step (`[NN] <step>: draft`) so that later levels can be reopened without
losing earlier work.

v. **Summary.** Before requesting the lock confirmation, the agent prints a
concise summary of what was produced: file paths created or modified, the
key decisions recorded, and any open warnings. The summary is not a sales
pitch; it is an audit trail in miniature.

vi. **Pause-before-lock with textual confirmation.** The agent pauses and asks
the user to confirm the lock. See §3 for the confirmation rule. After
confirmation, the agent creates the `[NN] lock` commit. Without
confirmation, no lock commit is made.

## 3. Textual-confirmation rule

A confirmation is valid only if the user types one of the following strings,
verbatim and as a complete reply:

- `pronto`
- `done`
- `confirmo`

Anything else — `ok`, `vai`, `pode prosseguir`, an emoji, an empty message, a
follow-up question, silence — is **not** a confirmation. The agent treats
ambiguous replies as "wait" and asks again. This rule applies to every lock
commit and to any irreversible action the agent performs (push to remote,
overwriting an existing file, deleting tracked content).

When the agent must wait on an external action (the user filling a spreadsheet
tab, pasting exports into `raw/exports/`, placing PDFs in `raw/pdfs/`), the
pause is double: one explicit instruction message, then a wait for the
textual-confirmation string. The agent does not infer completion from any
other signal.

## 4. Structured rationale

Every important decision the agent records on behalf of the user is accompanied
by a short rationale, written in a structured location:

- Scope, RQs, sub-RQs, criteria, weights, taxonomy axes → CLAUDE.md sections.
- Per-paper decisions (include / exclude / promote-to-next-stage) → the paper's
  own `papers/paper-NNN.md` frontmatter or section.
- Protocol parameters → `protocols/screening.yaml` (with prose summaries
  reflected back into CLAUDE.md so the human reviewer can read the protocol
  without parsing YAML).

The agent never embeds rationale exclusively in the chat transcript. The chat
is ephemeral; the artifact is permanent.

## 5. Lock and checkpoint discipline

The pipeline uses a numbered lock per stage, recorded in CLAUDE.md §1
(`locks.NN-<stage>` ∈ `{pending, iterating, locked}`) and reflected by commit
messages.

- A stage may emit any number of `[NN] <step>: draft` commits during execution
  to capture incremental progress (RQs draft, sub-RQs draft, criteria draft,
  etc.). These do not flip the lock.
- The lock flips to `locked` only when the agent issues the final `[NN] lock`
  commit, which requires the user's textual confirmation (§3).
- A locked stage can only be reopened by an explicit checkpoint commit:
  `[NN] checkpoint: <reason>`. The checkpoint flips the lock back to
  `iterating`. Later locks remain on disk in earlier commits and can be
  recovered, so reopen never loses prior work.
- Subsequent stages must verify both their own precondition lock and the locks
  of every prior stage they depend on.

## 6. Reference reviews — optional consultation

Agents that produce protocol artifacts (01–02) or screening decisions (04–06)
or taxonomy axes (07) may consult `reference-reviews/index.yaml` to inform
their suggestions. The rules:

- Consultation is opt-in and announced. The agent says "I see N relevant
  entries in the reference-reviews index; would you like me to use them as
  prior art?" before reading the index.
- The agent never replicates a reference verbatim. Suggestions are adapted to
  the user's topic; the agent cites the influencing entry by `citation_key`
  when a suggestion was shaped by a reference.
- PDFs linked in the index (`local_pdf` field) are read only on explicit user
  request. The default flow uses the YAML index entries alone to keep context
  small.

## 7. Failure modes the agent must refuse

The agent stops and asks for help — never improvises — in any of the following
situations:

- A precondition fails and the user has not provided a remediation.
- A YAML artifact (`protocols/screening.yaml`, `reference-reviews/index.yaml`)
  fails its validator with a non-trivial diagnostic.
- An external artifact expected by the procedure (export file, PDF, filled
  spreadsheet) is missing or malformed.
- The user's reply is ambiguous and the next step is irreversible (lock,
  push, file overwrite).

In all four cases the agent prints the specific blocker and the path or
filename the user needs to inspect, then waits.

## 8. Anti-patterns the agent must avoid

- Inferring user confirmation from anything other than the strings in §3.
- Bundling the work of two stages into one turn (e.g., proposing search-string
  terms during scope dialog).
- Editing files outside the stage's documented scope.
- Using `git --force`, `git reset --hard`, or `git push --force` without an
  explicit textual confirmation that names the destructive operation.
- Writing rationale into the chat transcript only.
- Proposing a default when the procedure requires elicitation.
