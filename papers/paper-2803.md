---
id: paper-2803
title: Research on Smart Wireless Aerial Networks Facilitating Digital Twin Construction
authors:
- Tran, Gia Khanh
- Nakazato, Jin
- Suto, Katsuya
- So, Hideya
- Iwamoto, Hiroki
venue: IEICE Transactions on Communications
venue_type: journal
year: 2026
doi: 10.23919/transcom.2025SCI0001
url: https://www.scopus.com/pages/publications/105034897942?origin=resultslist
publisher: Institute of Electronics Information Communication Engineers
pages: 573--585
keywords:
- autonomous placement
- digital twin
- meshed network
- mmWave
- NFV/SDN
- semantic communication
- UAV
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2803 — Research on Smart Wireless Aerial Networks Facilitating Digital Twin Construction

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper proposes a comprehensive framework for constructing smart wireless aerial networks to support high-fidelity digital twin (DT) systems. To meet the stringent data rate demands of airborne Light Detection and Ranging (LiDAR) sensing, we analyze the required throughput for point cloud transmission and design a millimeter-wave (mmWave) aerial link budget model. A software-defined architecture integrating Network Function Virtualization/Software Defined Networking (NFV/SDN) is introduced to enable dynamic Unmanned Aerial Vehicle (UAV) orchestration, routing, and network slicing. To enhance robustness and efficiency, we propose two application-layer innovations: a multi-route redundant communication framework and a semantic image transmission protocol using deep joint source-channel coding (DJSCC) with feature-based elastic compression. Furthermore, we implement a multi-agent reinforcement learning strategy to enable autonomous UAV placement and relay network formation in dynamic environments. Simulation results demonstrate the proposed system’s scalability, adaptability, and potential to enable reliable and efficient DT construction across diverse deployment scenarios. Copyright © 2026 The Institute of Electronics, Information and Communication Engineers.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2803.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
