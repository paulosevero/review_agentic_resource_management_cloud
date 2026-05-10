---
id: paper-2571
title: Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network
authors:
- Fernando Pakpahan, Andrew
- Hwang, I-Shyan
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3651558
url: https://www.scopus.com/pages/publications/105027048568?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7649--7668
keywords:
- DBA
- edge computing
- LLM inference
- OANs
- QoS
- SDN
- TWDM-PON
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2571 — Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of large language models (LLMs) has shifted inference workloads from centralized cloud servers toward distributed execution across fog and edge environments. As this trend accelerates, existing broadband infrastructures, particularly passive optical networks (PONs), must evolve to meet the stringent latency, bandwidth, and coordination demands of real-time LLM inference. Therefore, it is essential to enhance the access network with intelligence and programmability to support efficient, scalable, and low-latency inference delivery across multiple network layers. This paper presents a software-defined architecture for enabling tiered LLM inference over Time and Wavelength Division Multiplexed Passive Optical Networks (TWDM-PON). The proposed system incorporates LLM-integrated Optical Line Terminals (OLTs) and Optical Network Units (ONUs), each equipped with processing and queuing capabilities to execute portions of LLM inference tasks locally. These intelligent nodes collaborate under centralized Software-Defined Networking (SDN) control to manage inference-related traffic and optimize resource allocation across the network. Through inference-aware dynamic bandwidth allocation, time and wavelength slicing, and queue-level traffic isolation, the architecture prioritizes LLM traffic to provide low and consistent latency for LLM inference tasks for prompt and token streams without degrading conventional broadband services. Simulation results show that the proposed architecture reduces average inference latency by up to 50%, improves throughput by up to 7%, and lowers jitter and packet drop probability by up to 32% and 25.01%, respectively, while maintaining end-to-end Quality of Service (QoS) under mixed broadband and LLM traffic. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2571.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
