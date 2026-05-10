---
id: paper-0541
title: Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers
authors:
- Zhou, Amelie Chi
- Luo, Juanyun
- Qiu, Ruibo
- Tan, Haobin
- He, Bingsheng
- Mao, Rui
venue: Proceedings - International Conference on Data Engineering
venue_type: conference
year: 2022
doi: 10.1109/ICDE53745.2022.00256
url: https://www.scopus.com/pages/publications/85136418941?origin=resultslist
publisher: IEEE Computer Society
pages: 2818--2830
keywords:
- geo-distributed DCs
- graph partitioning
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

# paper-0541 — Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Graph partitioning is an important problem to the performance and cost optimization of graph analytics in geo-distributed environments. Modern hybrid-cut model is expected to obtain better performance and cost optimizations than traditional partitioning models, but can further complicate geo-distributed graph partitioning which is already a challenging problem due to large graph sizes and network heterogeneities of geo-distributed DCs. Existing studies usually adopt heuristic-based methods to achieve fast partitioning for large graphs, which unfortunately sacrifices optimization effectiveness. Further, graph structures of many applications can change at various frequencies. Dynamic partitioning methods usually focus on achieving low latency to quickly adapt to changes, which may again sacrifice partitioning effectiveness. Also, such methods are not aware of the dynamicity of graphs and can over sacrifice effectiveness for unnecessarily low latency. In this paper, we propose RLCut, which uses Reinforcement Learning (RL) to help taming the complexity of the problem. Specifically, RLCut uses multi-agent learning which is more efficient than single agent RL and incorporates a sampling based optimization to adaptively control the training process to satisfy required trade-off between partitioning effectiveness and efficiency according to graph dynamicity. Experiments using real cloud DCs and real-world graphs show that, compared to state-of-the-art static partitioning methods, RLCut improves the performance of geo-distributed graph analytics by 10%-100% with comparable overhead. When users tolerate longer partitioning overhead, we can further improve the performance by up to 43%. With varying graph changing frequencies, RLCut can improve the performance by up to 60% compared to state-of-the-art dynamic partitioning.  © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0541.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
