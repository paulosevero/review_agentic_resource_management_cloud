---
id: paper-0786
title: Cooperative DNN partitioning for accelerating DNN-empowered disease diagnosis via swarm reinforcement learning
authors:
- Yuan, Xiaohan
- Sun, Chuan
- Chen, Shuyu
venue: Applied Soft Computing
venue_type: journal
year: 2023
doi: 10.1016/j.asoc.2023.110844
url: https://www.scopus.com/pages/publications/85172890382?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Cooperative DNN partitioning
- DNN-empowered disease diagnosis
- Multi-access edge computing
- Swarm reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0786 — Cooperative DNN partitioning for accelerating DNN-empowered disease diagnosis via swarm reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As the most promising machine learning technology, deep neural networks (DNNs) have garnered significant attention in the field of disease diagnosis, i.e., DNN-empowered disease diagnosis. DNN-empowered disease diagnostic models with complex neural network structures are generally computation-intensive and latency-sensitive. To reduce latency, the partitioning and offloading of DNN-empowered disease diagnostic models in edge computing networks has emerged as a potential solution. However, DNN partitioning still faces two key challenges: the limitation of edge resources and the dynamic of network environments. To address these challenges, we propose a cooperative DNN partitioning system aimed at accelerating the processing of the model in multi-access edge computing networks. Specifically, we model the cooperative DNN partitioning offloading problem as a multi-agent Markov decision process with the goal of minimizing the long-term service latency (i.e., accelerating DNN-empowered disease diagnosis). To tackle this optimization problem, we further propose a swarm reinforcement learning (SRL) algorithm. Each agent of the proposed SRL can learn from local data and generate a judicious offloading action independently. Numerous simulation results show that the proposed SRL outperforms existing offloading algorithms and can significantly accelerate DNN-empowered disease diagnosis. © 2023 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0786.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
