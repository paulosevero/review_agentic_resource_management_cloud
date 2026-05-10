---
id: paper-1949
title: 'Optimizing Resource Allocation Challenges in Cloud-Edge Collaborative Systems: A Deep Q-Learning and Genetic Algorithm Approach'
authors:
- Meng, De-Yu
- Jin, Ye
- Li, Wen-Xiang
- Huang, Xin-Yi
- Cui, Ling-Xiao
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-5006-4_117
url: https://www.scopus.com/pages/publications/105022975156?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 1361--1369
keywords:
- Cloud-Edge collaboration
- Deep Q-Learning
- Genetic algorithm
- Resource allocation
- Task scheduling
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
  04-title-screening: exclude
  05-abstract-screening: pending
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
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-1949 — Optimizing Resource Allocation Challenges in Cloud-Edge Collaborative Systems: A Deep Q-Learning and Genetic Algorithm Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we find that an innovative approach to cloud-edge collaborative task scheduling optimization is presented, integrating Deep Q-Learning (DQN) with Genetic Algorithms (GA). By utilizing DQN for real-time decision-making and GA for global optimization, this method effectively handles challenges including latency, load balancing, and resource utilization. In addition, we designed a multi-agent task scheduling environment using OpenAI's Gym framework to model cloud-edge systems with dynamic task migration, aiming to balance loads and reduce delays. Experiments reveal that the combined method outperforms traditional algorithms—including Greedy Algorithm, Genetic Algorithm, Particle Swarm Optimization, and Simulated Annealing—in enhancing latency, load balancing, and resource allocation. These results validate the model's robustness in optimizing task distributions and adapting to changing workloads, which means providing an effective solution for complex cloud-edge computing challenges. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1949.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
