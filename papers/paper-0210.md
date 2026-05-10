---
id: paper-0210
title: Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge
authors:
- Jaleel, Abdul
- Hassan, Muhammad Awais
- Mahmood, Tayyeb
- Ghani, Muhammad Usman
- Ur Rehman, Atta
venue: IEEE Access
venue_type: journal
year: 2020
doi: 10.1109/ACCESS.2020.3037348
url: https://www.scopus.com/pages/publications/85102812386?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 205396--205410
keywords:
- Artificial intelligence
- Collaborative signaling
- Deep Q-networks
- Distributed computing
- Embedded machine learning
- Proximal Policy Optimization
- Traffic congestion
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0210 — Reducing congestion in an intelligent traffic system with collaborative and adaptive signaling on the edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advancements in Edge computing have paved the way for deep learning in real-time systems. One of the beneficiaries is an adaptive traffic control system that responds to real-time traffic observations by governing the signal phase and timings. Reinforcement Learning (RL) is extensively utilized in the literature in order to decrease traffic congestion in a road network. However, most of the previous works leverage centralized and cloud-based RL due to the computational complexity of underlying deep neural networks (DNN). Therefore, a persistent challenge towards adopting Edge learning is in devising a Multi-Agent RL in which agents are simplified, and their state spaces are localized but they perform comparable to the centralized RL. This article presents a Collaborative and Adaptive Signaling on the Edge (CASE), a novel Multi-Agent RL approach to control the traffic signals' phase and timing. Each signalized intersection in the road network is provided with an Edge Learning Platform which hosts an RL-Agent that observes local traffic states and learns an optimum signal policy. Moreover, CASE allows collaboration among RL-Agents by sharing their signal phase and timings to achieve convergence and performance. This collaboration is limited to one's direct neighbours only to minimize the computational complexity. We performed rigorous evaluations in terms of the choice of RL methods and their state space/reward and found that our collaborative state-space has resulted in a performance comparable to a centralized RL yet with a cost similar to the decentralized RL. Finally, a performance comparison of the CASE controller ported to the state-of-the-art Edge learning platforms is presented in this article. The results show that the proposed CASE controller can achieve real-time performance when ported to a general-purpose GPU-based platform. This arrangement achieves more than 8 times improvement in computational time over conventional embedded platforms. © 2020 Institute of Electrical and Electronics Engineers Inc.. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0210.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
