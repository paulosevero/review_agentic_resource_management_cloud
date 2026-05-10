---
id: paper-1151
title: Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing
authors:
- Rafiq, Ahsan
- Wei, Min
- Wang, Ping
- Jain, Deepak Kumar
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2024
doi: 10.1109/TCE.2024.3414324
url: https://www.scopus.com/pages/publications/85196510264?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5911--5928
keywords:
- 6TiSCH
- and migration
- artificial intelligence (AI)
- edge computing
- federated learning (FL)
- hybrid scheduling
- Industrial Internet of Things (IIoT)
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1151 — Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Standardizing the Industrial Internet of Things (IIoT) with 6TiSCH enables the IIoT nodes to utilize low power with high reliability. It ensures the allocation of resources for IIoT nodes with minimal power consumption. The existing work focused on various issues in the 6TiSCH-based IIoT in terms of network formation, and scheduling. However, security, energy efficiency, and latency remain challenging issues. The aforementioned issues are resolved by adopting different technologies in the 6TiSCH IIoT environment such as edge computing and federated learning named AIFed-6TiSCH IIoT. In the 6TiSCH layer, all IIoT nodes are authenticated to the Trusted Authority (TA) to reduce unwanted malicious traffic using Hybrid Authentication Algorithm (HAS) named Mchacha-poly 1305 algorithm based on several credentials. The authenticated nodes are allowed to form the network, for that we utilized a multicast CORONA-based DODAG structure using the Dijkstra algorithm. Eventually, new node joining is initiated by an already joined node which transmits Enhanced Beacons (EBs) in adaptive time intervals for synchronizing the new node. The synchronized nodes aim to select the optimal parent for transmitting data to the root node using an Enhanced Sea Gull (ESG) optimization algorithm based on mobility and several information. After that, optimal channel selection and scheduling are done using a Multi Criteria Decision Making (MCDM) algorithm named TOPSIS and a hybrid scheduling algorithm (i.e., Autonomous, and centralized scheduling) based on federated learning. By Performing channel selection, the congestion rate is reduced and federated learning ensures privacy and communication reliability. In the edge layer, data from the root are forwarded via a smart gateway to the edge servers for local processing. The security and latency issues in the edge layer are mitigated by performing Deep Reinforcement Learning (DRL) based migration named Enhanced Multi-Agent Deep Deterministic Policy Gradient (EMADDPG) that runs based on three policies. In addition, a virtual edge server is deployed in case of excess search time and overloading. The simulation of the proposed work is carried out using Cooja simulation based on Contiki 3x OS, and the simulation results are validated with existing works in terms of several validation metrics. The validation results show that the proposed work outperforms the existing works.  © 2024 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1151.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
