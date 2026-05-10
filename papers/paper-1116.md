---
id: paper-1116
title: A Hybrid Optimization Algorithm for Efficient Virtual Machine Migration and Task Scheduling Using a Cloud-Based Adaptive Multi-Agent Deep Deterministic Policy Gradient Technique
authors:
- Panesar, Gurpreet Singh
- Chadha, Raman
venue: International Journal of Intelligent Systems and Applications in Engineering
venue_type: journal
year: 2024
doi: ''
url: https://www.scopus.com/pages/publications/85181524637?origin=resultslist
publisher: Ismail Saritas
pages: 30--45
keywords:
- Adaptive Multi-Agent System (AMS)
- Deep Deterministic Policy Gradient (DDPG)
- Iterative Concept of War and Rat Swarm (ICWRS)
- Rat Swarm Optimizer (RSO)
- System Optimization
- War Strategy Optimization (WSO)
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: RL
    winning_category: rl
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

# paper-1116 — A Hybrid Optimization Algorithm for Efficient Virtual Machine Migration and Task Scheduling Using a Cloud-Based Adaptive Multi-Agent Deep Deterministic Policy Gradient Technique

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To achieve optimal system performance in the quickly developing field of cloud computing, efficient resource management— which includes accurate job scheduling and optimized Virtual Machine (VM) migration—is essential. The Adaptive Multi-Agent System with Deep Deterministic Policy Gradient (AMS-DDPG) Algorithm is used in this study to propose a cutting-edge hybrid optimization algorithm for effective virtual machine migration and task scheduling. An sophisticated combination of the War Strategy Optimization (WSO) and Rat Swarm Optimizer (RSO) algorithms, the Iterative Concept of War and Rat Swarm (ICWRS) algorithm is the foundation of this technique. Notably, ICWRS optimizes the system with an amazing 93% accuracy, especially for load balancing, job scheduling, and virtual machine migration. The VM migration and task scheduling flexibility and efficiency are greatly improved by the AMS-DDPG technology, which uses a powerful combination of deterministic policy gradient and deep reinforcement learning. By assuring the best possible resource allocation, the Adaptive Multi-Agent System method enhances decision-making even more. Performance in cloud-based virtualized systems is significantly enhanced by our hybrid method, which combines deep learning and multi-agent coordination. Extensive tests that include a detailed comparison with conventional techniques verify the effectiveness of the suggested strategy. As a consequence, our hybrid optimization approach is successful. The findings show significant improvements in system efficiency, shorter job completion times, and optimum resource utilization. Cloud-based systems have unrealized potential for synergistic optimization, as shown by the integration of ICWRS inside the AMS-DDPG framework. Enabling a high-performing and sustainable cloud computing infrastructure that can adapt to the changing needs of modern computing paradigms is made possible by this strategic resource allocation, which is attained via careful computational utilization. © 2024, Ismail Saritas. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "To achieve optimal system perf" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1116.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
