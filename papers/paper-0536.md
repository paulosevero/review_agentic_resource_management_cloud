---
id: paper-0536
title: Large-Scale Machine Learning Cluster Scheduling via Multi-Agent Graph Reinforcement Learning
authors:
- Zhao, Xiaoyang
- Wu, Chuan
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2022
doi: 10.1109/TNSM.2021.3139607
url: https://www.scopus.com/pages/publications/85122580602?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4962--4974
keywords:
- AI for management
- cluster scheduling
- distributed machine learning
- graph neural network
- multi-agent reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0536 — Large-Scale Machine Learning Cluster Scheduling via Multi-Agent Graph Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient scheduling of distributed deep learning (DL) jobs in large GPU clusters is crucial for resource efficiency and job performance. While server sharing among jobs improves resource utilization, interference among co-located DL jobs occurs due to resource contention. Interference-aware job placement has been studied, with white-box approaches based on explicit interference modeling and black-box schedulers with reinforcement learning. In today's clusters containing thousands of GPU servers, running a single scheduler to manage all arrival jobs in a timely and effective manner is challenging, due to the large workload scale. We adopt multiple schedulers in a large-scale cluster/data center, and propose a multi-agent reinforcement learning (MARL) scheduling framework to cooperatively learn fine-grained job placement policies, towards the objective of minimizing job completion time (JCT). To achieve topology-aware placements, our proposed framework uses hierarchical graph neural networks to encode the data center topology and server architecture. In view of a common lack of precise reward samples corresponding to different placements, a job interference model is further devised to predict interference levels in face of various co-locations, for training of the MARL schedulers. Testbed and trace-driven evaluations show that our scheduler framework outperforms representative scheduling schemes by more than 20% in terms of average JCT, and is adaptive to various machine learning cluster topologies.  © 2004-2012 IEEE.

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
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0536.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
