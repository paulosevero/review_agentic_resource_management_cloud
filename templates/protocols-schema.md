# Protocols — Schema

This document is the authoritative description of `protocols/screening.yaml`, the per-review file that holds the hierarchical research questions, the inclusion criteria, the per-stage allocation, the default model assignments, and a determinism seed.

The agents that produce or consume this file are:

- `skills/02-define-protocol/SKILL.md` — produces the entire file across the five Half-A levels (RQs → sub-RQs → criteria → weights → validation/lock) and then derives the search string in Half B.
- `skills/04-screen/SKILL.md` — reads the `inclusion_criteria` and `stage_allocation.<stage>` as the conceptual reference for the elicited regex patterns. The runtime classifier rules live in `protocols/classifier-config.json` (see `templates/classifier-config-schema.md`); the LLM reviewer model and the active classifier-config path are read from `CLAUDE.md §6` (`models.<stage>` and `classifier_configs.<stage>` respectively). The `models` block in `screening.yaml` is the default mirror; the screen skill may elicit a different model at first run and commit it to `CLAUDE.md`.
- `skills/05-code-taxonomy/SKILL.md` — reads `research_questions[].sub_rqs[]` to seed candidate taxonomy axes.
- `skills/06-analyze/SKILL.md` — reads `research_questions[]` and `sub_rqs[]` to anchor each analysis view via the `rq_anchor` field.

The deterministic validator is `scripts/validate_protocol.py`. Any change to this schema must be reflected in the validator, in this document, and in the canonical example below.

---

## 1. File location

- `protocols/screening.yaml` — lives in the per-review repo at the root, alongside `CLAUDE.md`.
- The file is created during stage 01 by Half A of `/02-define-protocol` and is locked together with that stage. Subsequent skills read it but do not modify it. Reopening the protocol requires `[01] checkpoint: revisit <level>` on the review repo.

## 2. Top-level structure

```yaml
pattern: thematic_decomposition
research_questions:
  - <RQ entry>
  - ...
inclusion_criteria:
  - <criterion entry>
  - ...
stage_allocation:
  title: <allocation entry>
  abstract: <allocation entry>
  full_text: <allocation entry>
models:
  title: <model assignment>
  abstract: <model assignment>
  full_text: <model assignment>
seed_global: <int>
```

The seven top-level keys are required. No additional top-level keys are permitted; the validator rejects unknown keys with a fail-fast diagnostic.

## 3. Per-field reference

### 3.1 `pattern`

- **Type**: string.
- **Allowed values**: `thematic_decomposition` (sub-RQs cover dimensions of the same phenomenon as the parent RQ).
- **Default**: none — the field must be present.
- **Notes**: Padrão 1 is the only supported pattern as of v2.0.0. Comparative or evidence-of patterns are flagged at stage 01 by the LLM-driven implicit-operator check; the user is asked to either reformulate the RQ to fit Padrão 1 or to abort the review.

### 3.2 `research_questions`

A non-empty list of RQ entries. Each entry has the following fields.

- **`id`** _(string, required)_ — pattern `^RQ\d+$`, e.g., `RQ1`, `RQ2`, `RQ12`. Must be unique within the list.
- **`text`** _(string, required)_ — the RQ verbatim, single-line preferred. Must be answerable by evidence extractable from primary studies.
- **`sub_rqs`** _(list of mappings, required, non-empty)_ — the dimensions the RQ decomposes into.
  - **`id`** _(string, required)_ — pattern `^RQ\d+\.\d+$`, where the prefix matches the parent RQ id, e.g., `RQ1.1`, `RQ1.2`. Must be unique across the entire file.
  - **`text`** _(string, required)_ — the sub-RQ verbatim.

Empty `sub_rqs` is invalid: every RQ in Padrão 1 must decompose into at least one dimension. If the user resists adding a sub-RQ, the agent at stage 01 must surface the conflict with the pattern invariant and ask whether to reformulate.

### 3.3 `inclusion_criteria`

A non-empty list of criterion entries. Each entry has the following fields.

- **`id`** _(string, required)_ — pattern `^C\d+$`, unique within the list.
- **`type`** _(string, required)_ — one of:
  - `thematic_rq` — applies at title stage; ternary scoring (0, 0.5, 1); `weight: null`.
  - `thematic_sub_rq` — applies at abstract and full-text stages; weighted scoring in `[0, 1]`.
  - `qa` — quality assessment; applies at full-text stage; weighted scoring in `[0, 1]`.
- **`refs`** _(list of strings, required, non-empty)_ — RQ or sub-RQ ids the criterion is anchored to.
  - `thematic_rq` may reference only RQ ids (`RQ\d+$`).
  - `thematic_sub_rq` may reference only sub-RQ ids (`RQ\d+\.\d+$`).
  - `qa` may reference RQ or sub-RQ ids.
  - References must point to declared ids in `research_questions`.
- **`text`** _(string, required)_ — the criterion verbatim. Phrased as an inclusion test: "the paper reports …", "the study evaluates …".
- **`weight`** _(float or null, required)_:
  - For `thematic_rq`: must be `null`.
  - For `thematic_sub_rq` and `qa`: must be a float in `(0, 1]`. Sums are not enforced to equal 1; normalization happens by `Σ wᵢ` at evaluation time when weighted scoring is used.

Bottom-up coverage rule: every sub-RQ must be referenced by at least one `thematic_sub_rq` or `qa` criterion. The validator enforces this; if a sub-RQ is left dangling, the user is asked at stage 01 to either add a criterion or remove the sub-RQ.

### 3.4 `stage_allocation`

A mapping with exactly three keys: `title`, `abstract`, `full_text`. Each value is a mapping with the following fields.

- **`criteria_types`** _(list of strings, required, non-empty)_ — subset of the allowed criterion types for this stage.
  - `title`: must be `[thematic_rq]`.
  - `abstract`: must be `[thematic_sub_rq]`.
  - `full_text`: must be `[thematic_sub_rq, qa]` (order irrelevant; validator compares as sets).
- **`scale`** _(string, required)_ — `ternary` for title, `weighted` for abstract and full-text.
- **`threshold`** _(float, required)_ — decision threshold in `(0, 1)`. Defaults follow the asymmetric permissive doctrine (permissive early, strict late):
  - `title`: 0.5
  - `abstract`: 0.6
  - `full_text`: 0.6 (project default; the user may override in dialog at stage 06).

Stages whose `criteria_types` reference a type not declared in `inclusion_criteria` are invalid. The validator catches this case explicitly because it usually means the user dropped a level (e.g., declared no `qa` criteria but kept `qa` in `full_text.criteria_types`).

### 3.5 `models`

A mapping with exactly three keys: `title`, `abstract`, `full_text`. Each value is a single model id (string) — the default LLM reviewer for that stage. The screening stage agents at runtime read the active model from `CLAUDE.md §6.models.<stage>`; the value here is the default written at stage 01 lock and may be overridden by the stage agent at its first run.

- **`title`** _(string, required)_ — model id, e.g., `claude-haiku-4-5-20251001` (high-volume, low-stakes per-paper).
- **`abstract`** _(string, required)_ — model id, e.g., `claude-sonnet-4-6` (mid-volume, mid-stakes).
- **`full_text`** _(string, required)_ — model id, e.g., `claude-sonnet-4-6` or `claude-opus-4-7` (low-volume, high-stakes; QA reasoning over long bodies).

Defaults aligned with the asymmetric cost of mistakes per stage are recommended (haiku → sonnet → opus or sonnet across the three stages). The user may override at stage 01 if budget or latency considerations demand it. The runtime model decision lives in `CLAUDE.md §6.models.<stage>`; this block is consulted only when `CLAUDE.md` is silent.

### 3.6 `seed_global`

- **Type**: integer.
- **Required**: yes.
- **Notes**: a determinism seed pinned at stage 01 for reproducibility. The pass-1 deterministic regex classifier is a pure function of `(input, config)` and does not consume this seed; it is preserved for forward compatibility (e.g., Phase 4 sampling, Phase 5 few-shot selection). Keep it pinned to make analyses repeatable.

## 4. Validation rules

`scripts/validate_protocol.py` enforces the following rules. Failure is fail-fast: the script exits with code 1 and prints a structured JSON diagnostic with one entry per violated rule.

1. **Top-level shape**: exactly the seven keys listed in §2; no extras; all present.
2. **Pattern invariant**: `pattern == "thematic_decomposition"`.
3. **RQ ids**: match `^RQ\d+$`; unique within `research_questions`.
4. **Sub-RQ ids**: match `^RQ\d+\.\d+$`; unique across the file; the prefix matches the parent RQ id.
5. **RQ decomposition (top-down)**: every RQ has `len(sub_rqs) ≥ 1`.
6. **Criterion ids**: match `^C\d+$`; unique within `inclusion_criteria`.
7. **Criterion type**: ∈ `{thematic_rq, thematic_sub_rq, qa}`.
8. **Type × ref**: `thematic_rq` references only RQ ids; `thematic_sub_rq` references only sub-RQ ids; `qa` references RQ or sub-RQ ids; every reference resolves to a declared id.
9. **Bottom-up coverage**: every declared sub-RQ is referenced by ≥1 criterion of type `thematic_sub_rq` or `qa`.
10. **Weights**: `thematic_rq.weight == null`; `thematic_sub_rq.weight` and `qa.weight` are floats in `(0, 1]`.
11. **Stage allocation**: keys are exactly `{title, abstract, full_text}`; each entry has `criteria_types`, `scale`, `threshold`; per-stage type sets match §3.4; scales match §3.4; thresholds in `(0, 1)`.
12. **Stage allocation × declared criteria**: if a stage references `qa` in its `criteria_types`, at least one `qa` criterion must exist in `inclusion_criteria`. Same for `thematic_rq` and `thematic_sub_rq`.
13. **Models**: keys are exactly `{title, abstract, full_text}`; each entry has `sub_agent_1` and `sub_agent_2` as non-empty strings.
14. **`seed_global`**: integer (any sign; the halo function takes the absolute value modulo `len(criteria)`).

The validator may emit warnings (non-fatal, exit 0) for:

- Asymmetric model pairings within a stage (different `sub_agent_1` vs `sub_agent_2`).
- Total weight per criterion type far from 1 (e.g., sum > 5 or sum < 0.1) — purely a heuristic to flag accidental data entry.

## 5. Example

The example below is the canonical reference. It is also the fixture used by the validator's self-test (`scripts/validate_protocol.py --self-test`).

```yaml
pattern: thematic_decomposition

research_questions:
  - id: RQ1
    text: "How do existing systems schedule stateful tasks at the edge under bandwidth-constrained conditions?"
    sub_rqs:
      - id: RQ1.1
        text: "Which scheduling objectives are considered (latency, energy, SLA, cost)?"
      - id: RQ1.2
        text: "Which state-management mechanisms are used (replication, migration, caching)?"
  - id: RQ2
    text: "What evaluation methodologies are used to validate edge schedulers?"
    sub_rqs:
      - id: RQ2.1
        text: "Which workloads and traces are reused across studies?"
      - id: RQ2.2
        text: "Which metrics are reported beyond mean latency?"

inclusion_criteria:
  - id: C1
    type: thematic_rq
    refs: [RQ1]
    text: "The paper proposes or evaluates a scheduler for stateful tasks running at the edge."
    weight: null
  - id: C2
    type: thematic_rq
    refs: [RQ2]
    text: "The paper reports an empirical evaluation of an edge scheduling approach."
    weight: null
  - id: C3
    type: thematic_sub_rq
    refs: [RQ1.1]
    text: "The paper articulates one or more scheduling objectives explicitly."
    weight: 0.4
  - id: C4
    type: thematic_sub_rq
    refs: [RQ1.2]
    text: "The paper describes a mechanism to manage application state across edge nodes."
    weight: 0.4
  - id: C5
    type: thematic_sub_rq
    refs: [RQ2.1]
    text: "The paper specifies the workload or trace used in the evaluation."
    weight: 0.3
  - id: C6
    type: thematic_sub_rq
    refs: [RQ2.2]
    text: "The paper reports at least one metric beyond mean latency (e.g., tail latency, energy, SLA violations)."
    weight: 0.3
  - id: C7
    type: qa
    refs: [RQ1, RQ2]
    text: "The paper provides sufficient detail to reproduce the experimental setup (hardware, software, parameters)."
    weight: 0.2
  - id: C8
    type: qa
    refs: [RQ2.2]
    text: "The paper reports variance or confidence intervals for the headline metric."
    weight: 0.2

stage_allocation:
  title:
    criteria_types: [thematic_rq]
    scale: ternary
    threshold: 0.5
  abstract:
    criteria_types: [thematic_sub_rq]
    scale: weighted
    threshold: 0.6
  full_text:
    criteria_types: [thematic_sub_rq, qa]
    scale: weighted
    threshold: 0.6

models:
  title:
    sub_agent_1: claude-haiku-4-5
    sub_agent_2: claude-haiku-4-5
  abstract:
    sub_agent_1: claude-sonnet-4-6
    sub_agent_2: claude-sonnet-4-6
  full_text:
    sub_agent_1: claude-opus-4-7
    sub_agent_2: claude-opus-4-7

seed_global: 20260425
```

## 6. How the schema evolves

Schema changes follow the same protocol as `reference-reviews/index.yaml`:

- **Backwards-compatible additions** (new optional fields, new allowed criterion types) — update this document, the validator, and the example in the same commit. No migration script needed.
- **Backwards-incompatible changes** (renaming or removing required fields, dropping `pattern: thematic_decomposition` as the only allowed pattern) — add a migration script under `scripts/` and a `[v2] phase X: protocol-schema-vY` commit on the plugin repo. Existing reviews reopen stage 01 via `[01] checkpoint: schema-migration` and re-run the validator before locking.
