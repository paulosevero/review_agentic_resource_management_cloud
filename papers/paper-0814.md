---
id: paper-0814
title: 'Latency and Energy Minimization in NOMA-Assisted MEC Network: A Federated Deep Reinforcement Learning Approach'
authors:
- Ahmadi, Arian
- Host-Madsen, Anders
- Xiong, Zixiang
venue: Proceedings - IEEE Symposium on Computers and Communications
venue_type: conference
year: 2024
doi: 10.1109/ISCC61673.2024.10733563
url: https://www.scopus.com/pages/publications/85209229477?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computation offloading
- Deep reinforcement learning
- Energy utilization
- Integer linear programming
- Integer programming
- Linear programming
- Mixed-integer linear programming
- Reinforcement learning
- Resource allocation
- Edge computing
- Emerging applications
- Energy minimization
- Energy-consumption
- Low latency
- Multiaccess
- Multiple access
- Non-orthogonal
- Reinforcement learning approach
- Weighted Sum
- Federated learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0814 — Latency and Energy Minimization in NOMA-Assisted MEC Network: A Federated Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) is seen as a vital component of forthcoming 6G wireless networks, aiming to support emerging applications that demand high service reliability and low latency. However, ensuring the ultra-reliable and low-latency performance of MEC networks poses a significant challenge due to uncertainties associated with wireless links, constraints imposed by communication and computing resources, and the dynamic nature of network traffic. Enabling ultra-reliable and low-latency MEC mandates efficient load balancing jointly with resource allocation. In this paper, we investigate the joint optimization problem of offloading decisions, computation and communication resource allocation to minimize the expected weighted sum of delivery latency and energy consumption in a non-orthogonal multiple access (NOMA)-assisted MEC network. Given the formulated problem is a mixed-integer non-linear programming (MINLP), a new multi-agent federated deep reinforcement learning (FDRL) solution based on double deep Q-network (DDQN) is developed to efficiently optimize the offloading strategies across the MEC network while accelerating the learning process of the Internet-of-Thing (IoT) devices. Simulation results show that the proposed FDRL scheme can effectively reduce the weighted sum of delivery latency and energy consumption of IoT devices in the MEC network and outperform the baseline approaches.  © 2024 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0814.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
