---
id: paper-1113
title: Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]
authors:
- Pan, Xi'an
- Ai, Xin
- Hu, Junjie
- Wang, Kunyu
- Wang, Haoyang
venue: Diangong Jishu Xuebao/Transactions of China Electrotechnical Society
venue_type: journal
year: 2024
doi: 10.19595/j.cnki.1000-6753.tces.231352
url: https://www.scopus.com/pages/publications/85211429124?origin=resultslist
publisher: China Machine Press
pages: 6104--6118
keywords:
- deep reinforcement learning
- Distributed smart grid
- edge-cloud collaboration
- flexible resources
- network safety constrain
language: Chinese
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1113 — Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing penetration of distributed generation and the growing demand for power system flexibility, issues like voltage rise at the edge of distribution networks and network congestion under bidirectional power flow are becoming more prominent. Integrating and coordinating flexible resources at the user side through Distributed Smart Grids (DSG) is significant for enhancing the accommodation of distributed generation and the real-time supply-demand balancing capability of distribution systems. Considering the large quantity and high dispersion of flexible resource devices and the distinct characteristics of different prosumers, traditional centralized optimization and dispatch schemes as well as distributed computing methods will face greater challenges in solving efficiency and decision delivery timeliness. Against this background, this paper aims to develop a DSG system collaborative optimization and dispatch method that takes into account operational economy, energy network security, and decision timeliness concurrently. Firstly, mapping real-world prosumers who control and own flexible resources to intelligent agents in reinforcement learning, the optimization and dispatch of flexible resources in DSG is formulated as a multi-agent collaborative optimization model. The existing edge-cloud collaborative framework is extended to the optimization of flexible resources considering energy network security constraints, and a hierarchical optimization and dispatch framework of flexible resource-prosumer-DSG is established. Secondly, considering the differentiated characteristics of prosumers in aspects like types of flexible resource devices, photovoltaics (PV) is taken as distributed generation, and electric vehicles (EV), heating, ventilation and air conditioning (HVAC) of buildings, and energy storage systems (ESS) are taken as demand-side flexible resources. A heterogeneous intelligent agent interactive environment model is built based on the operational characteristics of different flexible resources. Meanwhile, to balance flexible resource operational requirements, overall economic efficiency and energy network security of the DSG system, user satisfaction evaluation of EV and HVAC operation and ESS operation cost are considered as local rewards, while system energy cost and energy network security evaluation are taken as global rewards, and a combined global-local reward mechanism for heterogeneous intelligent agents is proposed. Finally, to adapt to the collaborative training task of the heterogeneous intelligent agent system, an improved multi-agent proximal policy optimization (MAPPO) algorithm is proposed based on asynchronous update of agent policies in random order. Case studies on the IEEE 33-node system are conducted for analysis. Firstly, the proposed improved MAPPO algorithm is compared with existing multi-agent collaborative training schemes in the offline training stage. Secondly, the differences in flexible resource prosumers' power decisions with and without considering energy network constraints are analyzed in the online dispatch stage. Finally, the proposed method is compared with traditional mathematical programming and particle swarm optimization methods regarding optimization performance in real-time dispatch. The main conclusions are: (1) The edge-cloud collaborative hierarchical optimization and dispatch framework for DSG systems is established, which can obtain dispatch decisions faster in real-time dispatch compared to traditional centralized optimization and thus improve the timeliness of DSG power dispatch decisions. (2) The combined global-local reward mechanism for heterogeneous intelligent agents can achieve overall DSG system optimization and collaborative training objectives of balancing user comfort, economic efficiency and energy network security. (3) The proposed improved MAPPO algorithm adapted for heterogeneous intelligent agent training can maintain independent decision spaces for each agent while ensuring environment state stability in collaborative training through asynchronous policy updates in random order. © 2024 China Machine Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1113.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
