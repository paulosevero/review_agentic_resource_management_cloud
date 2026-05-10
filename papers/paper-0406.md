---
id: paper-0406
title: Multi-protocol Aware Federated Matching for Architecture Design in Heterogeneous IoT
authors:
- Esmat, H.H.
- Xia, X.
- Lorenzo, B.
- Guo, L.
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2022
doi: 10.1109/GLOBECOM48099.2022.10000972
url: https://www.scopus.com/pages/publications/85146933024?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6277--6282
keywords:
- Age of Information (Aol)
- federated learning
- heterogeneous IoT
- mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0406 — Multi-protocol Aware Federated Matching for Architecture Design in Heterogeneous IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Enabling timely data collection in heterogeneous IoT networks under different protocols and spectrum bands (e.g., WiFi, Bluetooth, Zigbee, LoR a) is crucial to implementing large-scale IoT systems. This paper presents a federated matching framework for heterogeneous IoT networks in which an intermediate layer of multi-protocol mobile gateways (M-MGs) is deployed by different service providers (SPs) to collect and relay data from IoT objects and perform computing tasks. The aim is to develop collaborative strategies between M-MGs and SPs to minimize the average weighted sum of the age-of-information and energy consumption. A novel collaborative framework based on a 2-level multi-protocol multi-agent actor-critic (MP-MAAC) is presented, where M-MGs and SPs can learn the interactive strategies through their own observations. The M-MGs strategies include the selection of IoT objects for data collection, execution, and offloading t o S Ps' a ccess points while SPs decide on the spectrum allocation. Moreover, we incorporate federated matching (Fed-Match) into the multi-agent collaborative framework to improve the convergence of the learning process. The numerical results show that our Fed-Match algorithm reduces the Aol by factor 4, collects twice more packets than existing approaches and establishes design principles for the stability of the training process. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0406.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
