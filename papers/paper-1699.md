---
id: paper-1699
title: 'DeAOff: Dependence-Aware Offloading of Decoder-Based Generative Models for Edge Computing'
authors:
- Jiahong, Ning
- Tingting, Yang
- Ce, Zheng
- Xinghan, Wang
- Ping, Feng
- Xiufeng, Zhang
venue: China Communications
venue_type: journal
year: 2025
doi: 10.23919/JCC.fa.2024-0691.202507
url: https://www.scopus.com/pages/publications/105015573410?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 14--29
keywords:
- dependency-aware offloading (DeAOff)
- directed acyclic graph (DAG)
- generative AI (Gen-AI)
- mobile edge computing (MEC)
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
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1699 — DeAOff: Dependence-Aware Offloading of Decoder-Based Generative Models for Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents an algorithm named the dependency-aware offloading framework (DeAOff), which is designed to optimize the deployment of Gen-AI decoder models in mobile edge computing (MEC) environments. These models, such as decoders, pose significant challenges due to their inter-layer dependencies and high computational demands, especially under edge resource constraints. To address these challenges, we propose a two-phase optimization algorithm that first handles dependency-aware task allocation and subsequently optimizes energy consumption. By modeling the inference process using directed acyclic graphs (DAGs) and applying constraint relaxation techniques, our approach effectively reduces execution latency and energy usage. Experimental results demonstrate that our method achieves a reduction of up to 20% in task completion time and approximately 30% savings in energy consumption compared to traditional methods. These outcomes underscore our solution’s robustness in managing complex sequential dependencies and dynamic MEC conditions, enhancing quality of service. Thus, our work presents a practical and efficient resource optimization strategy for deploying models in resource-constrained MEC scenarios. © 2013 China Institute of Communications.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen-AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Gen-AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_gen_ai, matched_substring: "Gen-AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_generative_model, matched_substring: "Generative Models" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_decoder_generative, matched_substring: "Decoder-Based Generative" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1699.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
