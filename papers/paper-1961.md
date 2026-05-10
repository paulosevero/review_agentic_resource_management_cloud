---
id: paper-1961
title: 'Optimizing Task Offloading in Vehicular Network (OTO): A Game Theory Approach Integrating Hybrid Edge and Cloud Computing'
authors:
- Mohanapriya, M.
- Anusuya, V.
- Aravindhan, K.
- Krishnaveni, N.
- Santhosh, R.
- Gowthami, D.
venue: Journal of Cybersecurity and Information Management
venue_type: journal
year: 2025
doi: 10.54216/JCIM.150110
url: https://www.scopus.com/pages/publications/85204204443?origin=resultslist
publisher: American Scientific Publishing Group (ASPG)
pages: 115--132
keywords:
- Game Theory
- Hybrid Deep Learning (HDL)
- Multi-agent Deep Reinforcement Learning (MA-DRL)
- Resource Allocation
- Task Classification
- Task Scheduling
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1961 — Optimizing Task Offloading in Vehicular Network (OTO): A Game Theory Approach Integrating Hybrid Edge and Cloud Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In VANETs, user equipment (UE) schedules tasks by prioritizing them based on urgency and resource availability to ensure timely and efficient communication and processing. Effective task scheduling and resource allocation in VANET are crucial for maintaining low latency, high reliability, and optimal resource utilization for real-time vehicular communications. However, existing works often face limitations such as inadequate handling of dynamic network conditions, leading to increased latency and suboptimal resource usage. In this paper, we introduced a precise model by proposing Optimizing Task Offloading in Vehicular Network named as OTO framework. Initially, UEs are clustered using an Improved Fuzzy Algorithm (IFA) to reduce latency and energy consumption, with optimal clusters determined by a cluster validity index. Clustering considers distance, location, RSSI, link stability, and trust values, and cluster heads (CH) chosen based on distance, trust, and link stability. Following this, tasks from UE are classified using a Hybrid Deep Learning (HDL) algorithm, with LiteCNN for classification into emergency and non-emergency tasks and LiteLSTM for scheduling to reduce the weight matrix and overfitting. Dual scheduling based on task length, delay sensitivity, QoS, priority, resource consumption, and queue length reduces execution time and latency. Finally, the scheduled tasks are allocated to the optimal edge server based on task load, resource availability, waiting time, and distance using the RL-based Multi-agent Deep Reinforcement Learning (MA-DRL) algorithm, where edge servers act as sellers and users as buyers, reducing latency due to high convergence. In order to, evaluate and prove the efficacy of proposed OTO framework, we performed comparative analysis in terms of several performance metrics where our proposed OTO model outperforms other existing approaches. © 2025, American Scientific Publishing Group (ASPG). All rights reserved.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1961.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
