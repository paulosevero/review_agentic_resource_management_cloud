---
id: paper-1328
title: Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning
authors:
- Zhang, Fan
- Han, Guangjie
- Liu, Li
- Zhang, Yu
- Peng, Yan
- Li, Chao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3306803
url: https://www.scopus.com/pages/publications/85168749751?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5526--5544
keywords:
- Cooperative task offloading (TO)
- improved soft actor-critic (SAC)
- Industrial Internet of Things (IIoT)
- multiagent deep reinforcement learning (MADRL)
- resource allocation (RA)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1328 — Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing has become increasingly important to fulfill the diversified Quality-of-Service (QoS) or Quality-of-Experience (QoE) demands for Industrial Internet of Things (IIoT) applications, such as machine condition monitoring, fault diagnosis, intelligent production scheduling, and production quality control. Due to the heterogeneity of IIoT systems, it is of urgent necessity to concentrate on the cloud-edge-end cooperative partial task offloading and resource allocation (CPTORA) problem for realizing workload balancing, efficient resource utilization, and better QoS/QoE of IIoT applications. However, the challenge lies in how to make real-time, accurate, decentralized task offloading (TO) and resource allocation (RA) decisions for dynamic and device-intensive IIoT. Therefore, this work examines the CPTORA problem for IIoT, aiming at minimizing its long-run overall delay and energy costs. To lower the problem complexity, this problem is decomposed into the TO subproblem and the RA subproblem. Then, an improved soft actor-critic-based decentralized multiagent deep reinforcement learning (MADRL) algorithm is proposed to address the TO subproblem, where each IIoT device can learn its globally optimal policy and make its decisions independently. This algorithm innovatively combines the divergence regularization, the distributional reinforcement learning, and the value function decomposition methods to improve convergence speed and accuracy of the existing MADRL methods. After receiving the TO decisions of every IIoT device, every edge server employs the Lagrange multiplier method and Karush-Kuhn-Tucker condition to solve its RA subproblem. The experimental results show that the proposed algorithm decreases the overall delay and energy costs more effectively, compared to the other state-of-the-art MADRL approaches.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1328.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
