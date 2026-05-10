---
id: paper-0777
title: 'Cooperative Task Offloading and Service Caching for Digital Twin Edge Networks: A Graph Attention Multi-Agent Reinforcement Learning Approach'
authors:
- Yao, Zhixiu
- Xia, Shichao
- Li, Yun
- Wu, Guangfu
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2023.3310080
url: https://www.scopus.com/pages/publications/85170529488?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3401--3413
keywords:
- digital twin
- graph attention network
- Mobile edge computing
- multi-agent reinforcement learning
- service caching
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0777 — Cooperative Task Offloading and Service Caching for Digital Twin Edge Networks: A Graph Attention Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) enables various services to be cached in close proximity to the user equipments (UEs), thereby reducing the service delay of many emerging applications. However, the limitation of storage, computation, and radio resources, the dynamics of the decentralized MEC environment, and the complex spatial relationships of service request types and wireless network states between edge nodes make it difficult to realize efficient edge computing services. To address these challenges, this paper integrates the digital twin (DT) technology with a multi-cell MEC network to study an intelligent cooperative task offloading and service caching scheme, aiming at maximizing a quality of services (QoE)-based system utility. Specifically, we first construct a digital twin edge network (DITEN) to reflect the physical MEC system in real-time and provide data for training. With the help of DT technology, it is easy to access data resources in the DITEN to improve the simulation ability and reduce the communication cost. Then, we propose a graph attention-based multi-agent reinforcement learning (GatMARL) algorithm to learn the optimal task offloading and service caching strategies in the DITEN. The GatMARL employs a graph attention-based value decomposition network to capture the potential spatial relationships between edge nodes to learn better attentive cooperation policy. Simulation results demonstrate that the proposed GatMARL algorithm exhibits an effective performance improvement compared with state-of-the-art benchmarks.  © 1983-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0777.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
