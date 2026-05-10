---
id: paper-1445
title: Reliable DC Power Monitoring for Data Communication Center Via Carrier Communication and Topology Mapping
authors:
- Cao, Xiaodong
- Zeng, Run
- Yu, Yong
- Liu, Zhicong
venue: Proceedings of the International Conference on Electrical, Electronics, and Computer Science with Advance Power Technologies - A Future Trends, ICE2CPT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICE2CPT66440.2025.11340455
url: https://www.scopus.com/pages/publications/105033344699?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Carrier communication
- DC power monitoring
- Graph neural networks
- Reinforcement learning
- Topology mapping
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1445 — Reliable DC Power Monitoring for Data Communication Center Via Carrier Communication and Topology Mapping

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The present study has suggested a feasible DC power monitoring system in data communication centers via carrier communication technique and smart topology mapping technique. The modern data center became extremely complex, and the delivery of uninterrupted power is extremely important, which is why the given framework combines the Power Line communication (PLC) Orthogonal Frequency Division Multiplexing (OFDM) grounded on the powerful transmission of signals along DC power lines. It has a hybrid monitoring architecture, which includes Supervisory Control and Data Acquisition (SCADA) and the multi-agent decision-making algorithm to encourage faster fault detection and reaction time. Topology mapping module: this is a graph neural networks (GNNs)-based algorithm that can represent and analyze both dynamically physical and logical relationships in the power distribution network. This enables real life and load adaptation anomalies to be detected. Also, Reinforcement Learning (that is, Proximal Policy Optimization) is provided to learn how to route the communication signals when the load condition is timevarying, and power goes off. Namely, the solution is extensively applicable to smart grid implementation in data center applications and industrial control systems where reliability, speed and predictive maintenance is an important factor. The article is a step toward the development of intelligent and sustainable power plants since real-time analytics, AI, and communication engineering collide. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1445.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
