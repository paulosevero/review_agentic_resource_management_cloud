---
id: paper-0930
title: Deploying Stateful Network Functions Efficiently using Large Language Models
authors:
- Ghasemirahni, Hamid
- Farshin, Alireza
- Scazzariello, Mariano
- Chiesa, Marco
- Kostić, Dejan
venue: EuroMLSys 2024 - Proceedings of the 2024 4th Workshop on Machine Learning and
  Systems
venue_type: conference
year: 2024
doi: 10.1145/3642970.3655836
url: https://www.scopus.com/pages/publications/85192276579?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 28--38
keywords:
- Intra-Server Load Balancing
- LLMs
- RSS Configuration
- Stateful Network Functions
- Static Code Analysis
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_with_llm
    - ovr_using_llm
    - ovr_via_llm
    - ovr_llm_modifier
    - ovr_abs_llm_decides
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-0930 — Deploying Stateful Network Functions Efficiently using Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Stateful network functions are increasingly used in data centers. However, their scalability remains a significant challenge since parallelizing packet processing across multiple cores requires careful configuration t o avoid compromising the application’s semantics or performance. This challenge is particularly important when deploying multiple stateful functions on multi-core servers. This paper proposes FlowMage, a system that leverages Large Language Models (LLMs) to perform code analysis and extract essential information from stateful network functions (NFs) prior to their deployment on a server. FlowMage uses this data to find an efficient configuration of an NF chain that maximizes performance while preserving the semantics of the NF chain. Our evaluation shows that, utilizing GPT-4, FlowMage is able to find and apply optimized configuration when deploying stateful NFs chain on a server, resulting in significant p erformance i mprovement (up t o 1 1×) in comparison to the default configuration of the system. © 2024 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) t" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_via_llm', 'ovr_llm_modifier', 'ovr_abs_llm_decides']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "fine-tuning of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) to perform code analysis and extract essential information from statefu" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs RSS Configuration Stateful Network Functions Static Code Analysis 
 ---
title: \"Deploying" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs\"
  - \"Static Code Analysis\"
  - \"RSS Configuration\"
---

# Deploying" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) to perform code analysis and extract essential information from statefu" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs in the context of packet processing and (ii) address the challenges of deploying" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs before deploying a chain of stateful NFs;
- Evaluated FlowMage and showed the benefits of optim" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs help to efficiently deploy" }`


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
