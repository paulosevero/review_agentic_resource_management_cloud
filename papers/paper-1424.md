---
id: paper-1424
title: 'GraphCC: A practical graph learning-based approach to Congestion Control in datacenters'
authors:
- Bernárdez, Guillermo
- Suárez-Varela, José
- Shi, Xiang
- Xiao, Shihan
- Cheng, Xiangle
- Barlet-Ros, Pere
- Cabellos-Aparicio, Albert
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2024.110981
url: https://www.scopus.com/pages/publications/85212587690?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Congestion control
- Datacenters
- Graph neural networks
- Multi-agent reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1424 — GraphCC: A practical graph learning-based approach to Congestion Control in datacenters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Congestion Control (CC) plays a fundamental role in optimizing traffic in Datacenter Networks (DCNs). Currently, DCNs implement two main CC protocols: DCTCP and DCQCN. Both protocols are based on Explicit Congestion Notification (ECN), where switches mark packets when they detect congestion. Nowadays, network experts carefully set ECN parameters to optimize the average network performance. However, today's DCNs experience rapid and abrupt changes that severely affect the network state (e.g., dynamic workloads, incasts), which leads to under-utilization and sub-optimal performance. In this paper we present GraphCC, a framework for in-network CC optimization. GraphCC relies on Multi-agent Reinforcement Learning (MARL) and Graph Neural Networks (GNN), and is compatible with widely deployed ECN-based CC protocols. The proposed solution deploys distributed agents on switches that communicate with their neighbors to cooperate and optimize the global ECN configuration. In our evaluation, we test GraphCC with three real-world traffic workloads, focusing on its capability to accommodate scenarios unseen during training (e.g., traffic changes, failures). We compare GraphCC with a state-of-the-art MARL solution for ECN tuning, and observe that our method outperforms the state-of-the-art baseline in all evaluation scenarios, with improvements up to 20% in average Flow Completion Time, similar mean throughput (within 1%), and significant reductions in buffer occupancy (38.0–85.7%). © 2024 The Authors

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1424.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
