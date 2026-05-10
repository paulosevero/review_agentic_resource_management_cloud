---
id: paper-1067
title: 'RL-MR: Multipath Routing Based on Multi-Agent Reinforcement Learning for SDN-Based Data Center Networks'
authors:
- Liu, Peixin
- Bai, Xiangyu
- Cheng, Haoran
- Gao, Xiaochen
- Su, Jingwen
venue: Proceedings - 2024 IEEE International Symposium on Parallel and Distributed Processing with Applications, ISPA 2024
venue_type: conference
year: 2024
doi: 10.1109/ISPA63168.2024.00141
url: https://www.scopus.com/pages/publications/105000195744?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1065--1072
keywords:
- Data Center Networks
- Multipath Routing
- Reinforcement Learning
- Software Defined Networks
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1067 — RL-MR: Multipath Routing Based on Multi-Agent Reinforcement Learning for SDN-Based Data Center Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advent of the 5G era and the rapid development of emerging industries such as cloud computing and big data, data centers, as resource management platforms and key transmission hubs, are experiencing a dramatic increase in business data volume. Therefore, efficient routing optimization algorithms are needed. Improvements in Software Defined Networks (SDN) and programmable network devices allow different data traffic to be transmitted through various network paths, enabling fine-grained network performance optimization. In this paper, we utilize the emerging Hybrid Knowledge-Defined Network (KDN) architecture to propose a Multi-Agent Reinforcement Learning (MARL)-based multipath routing algorithm, termed RL-MR. RL-MR organizes intelligent agents to generate routes in a hop-by-hop manner, offering excellent scalability. The algorithm comprehensively considers flow latency, flow transmission rate, and packet loss rate to formulate routing strategies. To ensure reliability and accelerate the learning process, we introduce an auxiliary learning mechanism into RL-MR. Experiments conducted using Ryu and Mininet demonstrate that the RL-MR algorithm significantly outperforms baseline methods in terms of network throughput, link bandwidth utilization, and latency. Additionally, it exhibits excellent adaptability and reliability in scenarios involving flow changes, unknown large topologies, and partial deployments.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1067.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
