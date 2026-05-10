---
id: paper-2832
title: Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method
authors:
- Wang, Yingxin
- Feng, Binbin
- Ding, Zhijun
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-5012-8_20
url: https://www.scopus.com/pages/publications/105028325820?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 267--281
keywords:
- ensemble inference
- function-as-a-service
- instance autoscaling
- serverless computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Review
    winning_category: review
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2832 — Multi-agent-Driven Dual-Layer Serverless Adaptive Ensemble Inference Method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Ensemble learning achieves superior performance and generalization capabilities by leveraging multiple base models to collaboratively obtain prediction results, while the concurrent execution of multiple models also introduces significant latency and resource overhead challenges. Serverless computing frameworks have emerged as a popular choice for supporting ensemble inference services due to their on-demand dynamic allocation of computational resources. However, existing serverless scheduling methods suffer from prominent issues such as static request scheduling leading to high response latency and independent function scaling causing frequent bottlenecks. To address these challenges, this paper proposes a multi-agent-driven serverless dual-mode adaptive ensemble inference method to achieve end-to-end joint optimization of request distribution, model composition, and instance scaling. Specifically, 1) Heterogeneous feature-enhanced ensemble service dynamic route method, which realizes heuristic combination of user group portrait and base model through offline unsupervised log clustering, and considers the real-time resource status online to achieve rapid request distribution with O(1) time complexity; 2) Master-slave instance autoscaling algorithm based on multi-agent reinforcement learning, which realizes dynamic balance between local resource awareness and global bottleneck optimization through modeling collaboration and competition relationship between master-slave inference nodes. Finally, experimental validation on real-world clusters using public datasets has demonstrated the performance and overhead advantages of the proposed method. Our approach reduces latency by 13.4%, improves accuracy by 9.1%, and lowers CPU and memory occupancy by 19.4% and 3.9% compared to state-of-the-art inference serving systems. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_abs_state_of_the_art, matched_substring: "state-of-the-art in" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Ensemble learning achieves sup" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2832.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
