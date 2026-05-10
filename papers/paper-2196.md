---
id: paper-2196
title: Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers
authors:
- Tan, Haobin
- Xiao, Yao
- Zhou, Amelie Chi
- Lu, Kezhong
- Yang, Xuan
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2025
doi: 10.1109/TPDS.2025.3557610
url: https://www.scopus.com/pages/publications/105003272052?origin=resultslist
publisher: IEEE Computer Society
pages: 1161--1174
keywords:
- geo-distributed data centers
- Graph partitioning
- reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2196 — Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Graph partitioning is of great importance to optimizing the performance and cost of geo-distributed graph analytics applications. However, it is non-trivial to obtain efficient and effective partitioning due to the challenges brought by the large graph scales, dynamic graph changes and the network heterogeneity in geo-distributed data centers (DCs). Existing studies usually adopt heuristic-based methods to achieve fast and balanced partitioning for large graphs, which are not powerful enough to address the complexity in our problem. Further, graph structures of many applications can change at various frequencies. Dynamic partitioning methods usually focus on achieving low latency to quickly adapt to changes, which unfortunately sacrifices partitioning effectiveness. Also, such methods are not aware of the dynamicity of graphs and can over sacrifice effectiveness for unnecessarily low latency. To address the limitations of existing studies, we propose DistRLCut, a novel graph partitioner which leverages Multi-Agent Reinforcement Learning (MARL) to solve the complexity of the partitioning problem. To achieve fast partitioning for large graphs, DistRLCut adapts MARL to a distributed implementation which significantly accelerates the learning process. Further, DistRLCut incorporates two techniques to trade-off between partitioning effectiveness and efficiency, including local training and agent sampling. By adaptively tuning the number of local training iterations and the agent sampling rate, DistRLCut is able to achieve good partitioning results within an overhead constraint required by graph dynamicity. Experiments using real cloud DCs and real-world graphs show that, compared to state-of-the-art static partitioning methods, DistRLCut improves the performance of geo-distributed graph analytics by 11%-95%. DistRLCut can partition over 28 million edges per second, showcasing its scalability for large graphs. With varying graph changing frequencies, DistRLCut can improve the performance by up to 71% compared to state-of-the-art dynamic partitioning. © 1990-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2196.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
