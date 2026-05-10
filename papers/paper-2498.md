---
id: paper-2498
title: Decentralized Computation Offloading Strategy via Multi-Agent Deep Reinforcement Learning for Multi-Access Edge Computing Systems
authors:
- Adu, Emmanuella
- Lee, Yeongmuk
- Moon, Jihwan
- Jang, Sooyoung
- Bang, Inkyu
- Kim, Taehoon
venue: Sensors
venue_type: journal
year: 2026
doi: 10.3390/s26030914
url: https://www.scopus.com/pages/publications/105030065937?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- grant-free access
- multi-access edge computing
- offloading
- task completion latency
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

# paper-2498 — Decentralized Computation Offloading Strategy via Multi-Agent Deep Reinforcement Learning for Multi-Access Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) has been widely recognized as a promising solution for alleviating the computational burden on edge devices, particularly in supporting fast and real-time processing of resource-intensive applications. In this paper, we propose a decentralized offloading decision strategy based on multi-agent deep reinforcement learning (MADRL), aiming to minimize the overall task completion latency experienced by edge devices. Our proposed scheme adopts a grant-free access mechanism during the initialization of offloading in a fully decentralized manner, which serves as the key feature of our strategy. As a result, determining the optimal offloading factor becomes significantly more challenging due to the simultaneous access attempts from multiple edge devices. To resolve this problem, we consider a discrete action space-based deep reinforcement learning (DRL) approach, termed deep Q network (DQN), to enable each edge device to learn a decentralized computation offloading policy based solely on its local observation without requiring global network information. In our design, each edge device dynamically adjusts its offloading factor according to its observed channel state and the number of active users, thereby balancing local and remote computation loads adaptively. Furthermore, the proposed MADRL-based framework jointly accounts for user association and offloading decision optimization to mitigate access collisions and computation bottlenecks in a multi-user environment. We perform extensive computer simulations using MATLAB R2023b to evaluate the performance of the proposed strategy, focusing on the task completion latency under various system configurations. The numerical results demonstrate that our proposed strategy effectively reduces the overall task completion latency and achieves faster convergence of learning performance compared with conventional schemes, confirming the efficiency and scalability of the proposed decentralized approach. © 2026 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2498.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
