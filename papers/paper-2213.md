---
id: paper-2213
title: Energy-Efficient and QoS-Guaranteed Distributed Scheduling for Computing Power Networks Powered by Smart Grids
authors:
- Tian, Di
- Chen, Wei
- Han, Yuxing
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TGCN.2025.3604857
url: https://www.scopus.com/pages/publications/105015101090?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 933--948
keywords:
- computer power networks
- data center
- dynamic pricing
- green computing and AI
- Green networking
- quality-of-service
- smart grid
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2213 — Energy-Efficient and QoS-Guaranteed Distributed Scheduling for Computing Power Networks Powered by Smart Grids

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computing power networks (CPN) powered by smart grids are expected to play a vital role in the era of artificial intelligence (AI), because datacenters are now experiencing a dramatic increase in power consumption, especially with the vast deployments and applications of large language models (LLM). Consequently, efficient and low-latency offloading of computational tasks such as model training in smart grid powered CPN becomes a challenging but yet critical issue that has attracted considerable recent attention. In this paper, we aim at optimizing the energy efficiency of CPN with quality-of-service (QoS) requirements. To achieve this goal, we present a mixed integer programming (MIP) to minimize the overall cost given the time-varying power supply along with its price induced by the dynamic nature of renewable energy. A distributed algorithm for solving the MIP is judiciously conceived, which allows the datacenters and data owners to efficiently schedule the transmission of raw data and the computation for model training in a decentralized manner under a delay constraint guaranteeing QoS. Simulations demonstrate that the distributed protocol is capable of adapting to the dynamic energy price, time-varying supply of renewable energy, and even the line outage in smart grids with negligible latency and small signaling overhead. © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2213.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
