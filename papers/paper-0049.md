---
id: paper-0049
title: Toward a hybrid SDN architecture for V2V communication in IoV environment
authors:
- Alouache, Lylia
- Nguyen, Nga
- Aliouat, Makhlouf
- Chelouah, Rachid
venue: 2018 5th International Conference on Software Defined Systems, SDS 2018
venue_type: conference
year: 2018
doi: 10.1109/SDS.2018.8370428
url: https://www.scopus.com/pages/publications/85048884253?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 93--99
keywords:
- Availability
- Communication
- IoT
- IoV
- QoS
- Reliability
- Routing Protocol
- SDN
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

# paper-0049 — Toward a hybrid SDN architecture for V2V communication in IoV environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet of Vehicles (IoV) represents the evolution of Vehicular Ad-hoc Networks into Internet of Things paradigm using cloud computing as support. In IoV, Vehicle-To-Vehicle is the principal communication mode where the vehicles are either data transmitter, relay or receiver. This type of communication is subject to disturbances which deteriorate connectivity and hence the quality of service as it prevents access to cloud services on board vehicle. In this paper, we propose a robust routing protocol for the transmission of data packets satisfying the evolution of the topology and the mobility of the network by adopting a hybrid Software-Defined Networking architecture. This is done by disassociating the control plane that makes decisions about where data is sent from the data plane that forwards data to the selected destination. The control decisions are based on different criteria, namely the contact duration, the free load and the communication errors, which are carried out by each vehicle, in a decentralized mode. However, the error logs are handled within clusters, by an elected cluster head node, in a locally centralized mode. An implementation of this proposed hybrid protocol on a multi-Agent platform with a comparative study is presented in this paper. © 2018 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0049.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
