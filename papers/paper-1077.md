---
id: paper-1077
title: A multi-edge jointly offloading method considering group cooperation topology features in edge computing networks
authors:
- Lyu, Zengwei
- Li, Pengfei
- Wei, Zhenchun
- Fan, Yuqi
- Xu, Juan
- Shi, Lei
venue: Peer-to-Peer Networking and Applications
venue_type: journal
year: 2024
doi: 10.1007/s12083-024-01766-z
url: https://www.scopus.com/pages/publications/85200023633?origin=resultslist
publisher: Springer
pages: 3507--3525
keywords:
- Computation offloading
- Cooperative topology
- Load balancing
- Mobile edge computing
- Multi-agent deep reinforcement learning
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

# paper-1077 — A multi-edge jointly offloading method considering group cooperation topology features in edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) is a new computing paradigm that has shown great potential. How to extract the cooperative topological relationship between MEC servers to realize jointly computing is the key problem to solve the bottleneck of MEC computational capability. In previous studies, multi-MEC servers are regarded as unit computing nodes with the same cooperation relationship to jointly schedule offloading tasks, without considering the hierarchical and clustered topology of the server collaborative work. As a result, in the scenario of unbalanced distribution of computing resources, it is difficult to obtain the optimal joint scheduling strategy for offloading tasks according to the cooperation relationship and resource differences among MEC servers. Therefore, this paper considers introducing the topological relationship of group cooperation among multi-MEC servers to optimize the joint scheduling strategy, and proposes a Multi-Agent Hierarchical Graph Attention Soft Actor-Critic algorithm (MHSAC). Firstly, based on the differences in their own resources and the demands of the tasks they undertake, MEC servers are divided into series clusters. Then, a Hierarchical Graph Attention Network (HGAT) is used to model each agent to extract the physical communication topology information of the MEC server and the group topology information of multi-edge cooperation. The multi-agent soft Actor-Critic algorithm is used to obtain the offloading scheduling decision of multi-edge cooperation. Experiments show that the MHSAC algorithm that considering the topological relationship of multi-edge group cooperation can optimize load distribution under low latency and resource-limited requirements, achieving optimal load balancing values and task drop rates. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1077.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
