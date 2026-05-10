<!--
Schema for `protocols/classifier-config.json` — the per-review configuration consumed by
`scripts/deterministic_classifier.py` (pass 1 of stages 04/05/06) and by the LLM reviewer
(pass 2). Generated from scratch via Q&A by `agents/_screening-classifier-runner.md`.
NO default rules are shipped with the plugin; the config emerges entirely from the dialog
between the user and the runner agent.

This file is the authoritative spec. The classifier and the LLM reviewer must conform.
-->

# `protocols/classifier-config.json` — Schema

`protocols/classifier-config.json` is the single source of truth for the deterministic regex classifier (pass 1) at every screening stage. It encodes domain-specific inclusion and exclusion patterns elicited from the user via Q&A. The same file is consumed by the LLM reviewer (pass 2) for the textual summary of criteria embedded in the cached prompt prefix.

The plugin ships **no default rules**. The runner agent (`agents/_screening-classifier-runner.md`) generates the file on first invocation of stage 04 from scratch by interviewing the user about the review's domain. Stage 05 may reuse the same file unchanged or refine specific patterns; stage 06 may use either the same file or a separate `protocols/classifier-config-fulltext.json` (see §11.1 of `templates/CLAUDE.md.template`, key `classifier_configs`).

---

## Top-level shape

```json
{
  "version": "1.0",
  "default_decision": "Exclude",
  "default_justification": "Sem pistas de inclusão.",
  "proximity_window": 200,
  "priority_order": ["<category_id_1>", "<category_id_2>", "..."],
  "categories": [ /* objects per the schema below */ ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `version` | string | yes | Currently `"1.0"`. Bump only on breaking schema changes. |
| `default_decision` | `"Include"` \| `"Exclude"` | yes | Verdict when no category matches. Conventionally `"Exclude"`. |
| `default_justification` | string | yes | Verbatim PT-BR justification written to `My Justification` when `default_decision` fires. |
| `proximity_window` | integer ≥200 | yes | Max characters allowed between two tokens in proximity-style patterns (`token_a [^.,]{0,N} token_b`). Smaller values silently miss long titles. |
| `priority_order` | string array | yes | `category.id` in the order the classifier evaluates them. **First match wins** subject to override. Must list every `category.id` exactly once. |
| `categories` | object array | yes | One entry per category. ≥1 with `kind: "include"` and ≥1 with `kind: "exclude"` are required. |

---

## Category object

```json
{
  "id": "<category_id>",
  "label": "<display label>",
  "kind": "include" | "exclude",
  "justification": "<verbatim PT-BR string>",
  "priority_index": <int>,
  "patterns": [ /* pattern objects */ ],
  "overrides": [ /* override objects */ ]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable identifier referenced by `priority_order` and `evidence_trail`. snake_case recommended. |
| `label` | string | yes | Human-readable label (any language; the user picks). |
| `kind` | `"include"` \| `"exclude"` | yes | Whether matching this category produces an Include or an Exclude verdict. |
| `justification` | string | yes | **Verbatim PT-BR** written to `My Justification` when this category wins. Part of the user's controlled vocabulary; downstream tooling references it literally. **Must not be translated.** |
| `priority_index` | integer | yes | Mirrors the position in `priority_order`. Redundant on purpose to make the JSON self-documenting; `validate` checks consistency. |
| `patterns` | object array | yes | ≥1 pattern. Each pattern can match the input string. |
| `overrides` | object array | no (default `[]`) | Patterns that, when matched, suppress this category and pass control to the next priority slot. |

### Pattern object

```json
{
  "id": "<pattern_id>",
  "regex": "<case-insensitive regex>",
  "description": "<what concept this pattern captures>",
  "applicable_stages": ["title", "abstract", "full_text"],
  "differential_reliability": "<optional notes per stage>",
  "notes": "<optional user notes>"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable identifier surfaced in `evidence_trail`. snake_case recommended. |
| `regex` | string | yes | Compiled with `re.IGNORECASE`. Hyphenation handling is **not** automatic — use `[-\s]+` between tokens for compound terms (see Pitfalls). |
| `description` | string | yes | One-line description of the concept matched. Used by the runner agent during Q&A and by the LLM reviewer prefix. |
| `applicable_stages` | string array | no (default all three) | Subset of `["title", "abstract", "full_text"]`. Lets a pattern be active in some stages and idle in others (useful for subtitle-only patterns reliable on title stage). |
| `differential_reliability` | string | no | Free-text notes on how the pattern's precision varies per stage. Surfaced in xlsx tooltips when present. |
| `notes` | string | no | Free-form notes from the user (e.g., "regex variant suggested on 2026-04-15"). |

### Override object

```json
{
  "id": "<override_pattern_id>",
  "regex": "<regex>",
  "description": "<when matched, suppresses this category>"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | yes | Stable identifier surfaced in `overrides_applied`. |
| `regex` | string | yes | Same compilation rules as pattern regex. |
| `description` | string | yes | Why a match here suppresses the parent category. The LLM reviewer reads this when it diverges from the regex verdict. |

Override semantics: if any `pattern` in the category matched **and** any `override` also matched, the category is suppressed for this paper, the override id is appended to `overrides_applied`, and evaluation continues to the next entry in `priority_order`. Conservative doctrine: when both a positive trigger and an override fire, prefer Include unless the override is itself a positive *for inclusion* (e.g., an exclude-category overridden by a stronger include signal).

---

## Validation rules (enforced by the runner; `validate_protocol.py` may be extended later)

1. Every `category.id` listed in `priority_order` exists in `categories`. Every `category.id` in `categories` is listed in `priority_order` exactly once.
2. `category.priority_index == priority_order.indexOf(category.id)`.
3. `categories` contains ≥1 with `kind: "include"` and ≥1 with `kind: "exclude"`.
4. `proximity_window ≥ 200`.
5. Every `regex` compiles under `re.IGNORECASE`. Compilation failure is fatal; the runner names the offending `pattern_id` or `override.id`.
6. `justification` is non-empty and contains at least one PT-BR word. Translation to other languages is rejected.
7. `applicable_stages`, when present, is a subset of `["title", "abstract", "full_text"]`.

---

## Pitfalls (non-negotiable; the runner Q&A enforces them)

- **Hyphenation.** Compound terms must use `[-\s]+` between tokens, not `\s+`. Otherwise `Multi-Agent-Deep-Reinforcement-Learning-Enabled` silently fails to match `\bmulti\s+agent\b`. The Q&A confirms the pattern shape with the user before writing.
- **Distance windows.** Patterns of the form "token A near token B" must use `[^.,]{0,N}` with `N = proximity_window`. The runner refuses smaller `N` (long titles drop matches).
- **Subtitle anchors.** Patterns anchored to `:\s*` should not include the `:\s*` in the substring exposed to the user. The classifier strips leading punctuation when serializing `matched_substring`.
- **Case-insensitive only.** The classifier compiles every regex with `re.IGNORECASE`. Patterns relying on case sensitivity must encode it via character classes (e.g., `[A-Z]{2,}` for ALL-CAPS acronyms).
- **Determinism.** The classifier is a pure function of `(input, config)`. No system time, no random seeds, no environment variables, no network, no file order, no hash randomization. The order of evaluation is exactly `priority_order`.

---

## Conservative doctrine (inherited by the runner and the LLM reviewer)

When in doubt, keep `Include`. False negatives (wrongful exclusions) cost more than false positives (the user catches false positives in the next round by tightening criteria). This applies during Q&A (when the user hesitates between "always exclude" and "depends"), at runtime (when a trigger and an override both fire), and at LLM review (when the regex says Exclude but the LLM finds inclusion-aligned signal the regex missed).

---

## Canonical example (for reference; the runner does **not** ship this)

```json
{
  "version": "1.0",
  "default_decision": "Exclude",
  "default_justification": "Sem pistas de inclusão sobre Agentic AI ou Stateful Edge.",
  "proximity_window": 240,
  "priority_order": ["off_topic_domain", "non_research_artifact", "agentic_ai_core", "stateful_edge"],
  "categories": [
    {
      "id": "off_topic_domain",
      "label": "Domínio fora de escopo",
      "kind": "exclude",
      "justification": "Foco em domínio fora do escopo (e.g., bioinformática, clínica) sem ponte para Edge ou Agentic AI.",
      "priority_index": 0,
      "patterns": [
        {
          "id": "bioinformatics_focus",
          "regex": "\\b(bioinform[a\\u00e1]tic[ao]s?|gen[oô]mic[ao]s?|prote[oô]m(?:ic[ao]|e))\\b",
          "description": "Estudos bioinformáticos sem ligação com computação de borda."
        }
      ],
      "overrides": [
        {
          "id": "bioinformatics_at_edge",
          "regex": "\\b(edge|fog)\\s+(deployment|inference|computing)\\b",
          "description": "Bioinformática implementada em infraestrutura de borda — relevante."
        }
      ]
    },
    {
      "id": "agentic_ai_core",
      "label": "Agentic AI no núcleo da contribuição",
      "kind": "include",
      "justification": "Trabalho cuja contribuição central é Agentic AI (planejamento, ferramentas, multi-agente) com aplicação a sistemas distribuídos.",
      "priority_index": 2,
      "patterns": [
        {
          "id": "agentic_terms",
          "regex": "\\b(agentic[-\\s]+ai|llm[-\\s]+agents?|tool[-\\s]+use|multi[-\\s]+agent[-\\s]+(orchestrat\\w+|planning))\\b",
          "description": "Termos canônicos de Agentic AI."
        }
      ],
      "overrides": []
    }
  ]
}
```

This example illustrates the schema only; it is **not** loaded by the plugin. Each review must elicit its own categories from scratch.
