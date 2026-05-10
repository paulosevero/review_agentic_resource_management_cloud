---
id: paper-1553
title: Decentralized Smart EV Charging with Multi-Agent System Communication and Energy Coordination
authors:
- Dwivedi, Priyansh
- Tiwari, Himanshu
- Yadav, Pradhyumna
- Kumar, Murari
- Shanthi Swarup, K.
venue: International Conference on Power Systems, ICPS
venue_type: conference
year: 2025
doi: 10.1109/ICPS67276.2025.11364838
url: https://www.scopus.com/pages/publications/105035160977?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Electric Vehicle (EV)
- Energy Management System
- IoT
- Load Balancing
- Power Distribution
- Real-Time Monitoring
- Renewable Energy
- Smart Charging
- Sustainable Transportation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1553 — Decentralized Smart EV Charging with Multi-Agent System Communication and Energy Coordination

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a decentralized smart electric vehicle (EV) charging framework that integrates Raspberry Pi and Arduino-based controllers with multi-agent coordination for efficient and scalable operation. The system leverages IoT-enabled edge computing to support adaptive load balancing, real-time monitoring, and cloud synchronization. Unlike centralized approaches, the proposed architecture employs a Raspberry Pi server to manage distributed charging nodes through MQTT-based communication, ensuring resilience in bandwidth-constrained environments. Hardware prototyping and MATLAB/Simulink simulations validate the feasibility of the design, demonstrating improvements in load management and fault handling. Experimental results show balanced power allocation among multiple EVs with reduced grid stress and reliable user interaction through a local dashboard. While future extensions such as bidirectional Vehicle-to-Grid (V2G) and Demand Response (DR) integration are envisioned, the present work provides a cost-effective and modular prototype suitable for urban, semi-urban, and rural deployments.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1553.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
