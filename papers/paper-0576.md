---
id: paper-0576
title: Multiagent Reinforcement Learning-Based Cooperative Multitype Task Offloading Strategy for Internet of Vehicles in B5G/6G Network
authors:
- Cui, Yuya
- Li, Honghu
- Zhang, Degan
- Zhu, Aixi
- Li, Yang
- Qiang, Hao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3245721
url: https://www.scopus.com/pages/publications/85149387253?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12248--12260
keywords:
- B5G/6G
- computation offloading
- Internet of Vehicles (IoV)
- multiaccess edge computing (MEC)
- multiagent deep reinforcement learning (DRL)
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

# paper-0576 — Multiagent Reinforcement Learning-Based Cooperative Multitype Task Offloading Strategy for Internet of Vehicles in B5G/6G Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of intelligent transportation, various computation intensive and delay sensitive applications are emerging in the Internet of Vehicles (IoV). The B5G/6G (Beyond 5th generation mobile communication technology/6th generation mobile communication technology) network has the characteristics of ultralow latency and ultra many connections. The deployment of the network in boxes (NIBs) supporting B5G/6G network in the vehicle can realize the real-time communication with the edge server (ES) and offload the task to the ES. However, the current multiaccess edge computing (MEC) lacks research on cooperative processing among multiple ESs, and the efficiency of data-intensive computation tasks is still insufficient. In this article, we investigate the cooperative offloading of multitype tasks among ESs in B5G/6G networks under a dynamic environment. In order to minimize the delay of task execution, we regard cooperative offloading as a Markov decision process (MDP), and improve the convergence speed and stability of traditional soft actor-critic (SAC) algorithm by the adaptive weight sampling mechanism. Finally, an offline centralized training distributed execution framework based on improved soft actor critical (OCTDE-ISAC) is proposed to optimize the cooperative offloading strategy. The experimental results show that the proposed algorithm is better than the existing algorithm in terms of latency. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0576.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
