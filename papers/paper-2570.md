---
id: paper-2570
title: Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning
authors:
- Farabegoli, Nicolas
- Domini, Davide
- Aguzzi, Gianluca
- Viroli, Mirko
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2026.108539
url: https://www.scopus.com/pages/publications/105036172040?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Aggregate computing
- Collective adaptive systems
- Edge-cloud computing
- Heterogeneous graph neural networks
- Multi-agent reinforcement learning
- Task offloading
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

# paper-2570 — Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading in edge-cloud computing systems requires determining optimal allocation of application components across heterogeneous infrastructure while balancing multiple objectives, like energy consumption, latency, or cost. This problem becomes particularly complex in large-scale deployments (e.g., smart cities, industrial IoT) where existing approaches fail to address collective phenomena, namely emergent system-wide behaviors like network congestion that arise from multi-device interactions, leading to suboptimal offloading decisions in large-scale deployments. To address these challenges this paper introduces a multi-agent learning framework for collective component offloading that decomposes applications into a directed acyclic graph of macro-components, enabling partial offloading where individual components can be selectively executed locally or migrated to edge/cloud servers. Our system model represents the infrastructure as a heterogeneous graph of application devices and infrastructure nodes, supporting decentralized offloading decisions while maintaining component interdependencies. In particular, we propose Informed Deep Hetero Graph Q-Learning (IDHGQL), which combines: (1) Heterogeneous Graph Neural Networks (HeteroGNNs) for policy representation that naturally handle diverse device types and relationships; (2) Aggregate computing to enrich device observations with collective system state information; and (3) a multi-agent Deep Q-Learning algorithm based on centralized training with decentralized execution that balances individual constraints with emergent collective phenomena. Experimental evaluation demonstrates IDHGQL’s effectiveness in multi-objective optimization scenarios, successfully learning policies that balance battery consumption, latency, and infrastructure costs. In density-aware scenarios, agents learn spatially-adaptive strategies that dynamically adjust offloading decisions based on local congestion: favoring local execution in high-density areas to avoid network bottlenecks while leveraging edge/cloud resources in sparse regions. Ablation studies confirm that collective information integration is essential for learning such context-aware policies, with IDHGQL consistently outperforming static baselines across all evaluated metrics. © 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2570.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
