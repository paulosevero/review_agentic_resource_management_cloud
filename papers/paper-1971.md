---
id: paper-1971
title: 'LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning'
authors:
- Moshiri, Parisa Fard
- Zhu, Xinyu
- Lohan, Poonam
- Kantarci, Burak
- Janulewicz, Emil
venue: Proceedings of the 16th International Conference on Network of the Future, NoF 2025
venue_type: conference
year: 2025
doi: 10.1109/NoF66640.2025.11223314
url: https://www.scopus.com/pages/publications/105024948569?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 28--36
keywords:
- BART
- DRL
- FLAN-T5
- Language Model
- Network State Monitoring
- SFC provisioning
- VNF placement
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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

# paper-1971 — LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Effective management of Service Function Chains (SFCs) and optimal Virtual Network Function (VNF) placement are critical challenges in modern Software-Defined Networking (SDN) and Network Function Virtualization (NFV) environments. Although Deep Reinforcement Learning (DRL) is widely adopted for dynamic network decision-making, its inherent dependency on structured data and fixed action rules often limits adaptability and responsiveness, particularly under unpredictable network conditions. This paper introduces LiLM-RDB-SFC, a novel approach combining Lightweight Language Model (LiLM) with Relational Database (RDB) to answer network state queries to guide DRL model for efficient SFC provisioning. Our proposed approach leverages two LiLMs, Bidirectional and Auto-Regressive Transformers (BART) and the Fine-tuned Language Net T5 (FLAN-T5), to interpret network data and support diverse query types related to SFC demands, data center resources, and VNF availability. Results demonstrate that FLAN-T5 outperforms BART with a lower test loss (0.00161 compared to 0.00734), higher accuracy (9 4. 7 9% compared to 8 0. 2%), and less processing time (2h 2min compared to 2h 38min). Moreover, when compared to the large language model SQLCoder, FLAN-T5 has almost same accuracy while cutting processing time by 96% (SQLCoder: 54 h 43 min; FLAN-T5: 2 h 2 min).  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Transformers" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Language Model" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1971.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
