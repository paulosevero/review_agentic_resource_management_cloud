---
id: paper-2539
title: QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems
authors:
- Chen, Xuyang
- Feng, Daquan
- Jiang, Wei
- Luo, Qu
- Chen, Gaojie
- Sun, Yao
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2026.3662899
url: https://www.scopus.com/pages/publications/105030557637?origin=resultslist
publisher: IEEE Computer Society
pages: 7100--7117
keywords:
- Mobile edge computing
- resource allocation
- semantic-aware
- task offloading
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2539 — QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) provides low-latency offloading solutions for computationally intensive tasks, effectively improving the computing efficiency and battery life of mobile devices. However, for data-intensive tasks or scenarios with limited uplink bandwidth, network congestion might occur due to massive simultaneous offloading nodes, increasing transmission latency, and affecting task performance. In this paper, we propose a semantic-aware multi-task offloading framework to address the challenges posed by limited uplink bandwidth. By introducing a semantic extraction factor, we balance the tradeoff among transmission latency, computation energy consumption, and task performance. To measure the offloading performance of different tasks, we design a unified and fair quality of experience (QoE) metric that includes execution latency, energy consumption, and task performance. We formulate the QoE optimization problem as a Markov decision process (MDP) and exploit the semantic-aware multi-agent proximal policy optimization (MAPPO) reinforcement learning algorithm to jointly optimize the semantic extraction factor and communication and computing resources allocation to maximize overall QoE. Experimental results show that the proposed method achieves a 12.68% improvement in user QoE compared with the semantic-unaware approach. Moreover, the proposed approach can be easily extended to models with different user preferences. © 2026 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2539.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
