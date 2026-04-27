---
id: "paper-2571"
title: "Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network"
authors: ["Fernando Pakpahan, Andrew", "Hwang, I-Shyan"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3651558"
url: "https://www.scopus.com/pages/publications/105027048568?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "7649--7668"
keywords: ["DBA", "edge computing", "LLM inference", "OANs", "QoS", "SDN", "TWDM-PON"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2571 — Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network

## Metadata

- **Authors:** Fernando Pakpahan, Andrew and Hwang, I-Shyan
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3651558
- **URL:** https://www.scopus.com/pages/publications/105027048568?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 7649--7668
- **Language:** English
- **Keywords:** DBA; edge computing; LLM inference; OANs; QoS; SDN; TWDM-PON

### Abstract

The rapid expansion of large language models (LLMs) has shifted inference workloads from centralized cloud servers toward distributed execution across fog and edge environments. As this trend accelerates, existing broadband infrastructures, particularly passive optical networks (PONs), must evolve to meet the stringent latency, bandwidth, and coordination demands of real-time LLM inference. Therefore, it is essential to enhance the access network with intelligence and programmability to support efficient, scalable, and low-latency inference delivery across multiple network layers. This paper presents a software-defined architecture for enabling tiered LLM inference over Time and Wavelength Division Multiplexed Passive Optical Networks (TWDM-PON). The proposed system incorporates LLM-integrated Optical Line Terminals (OLTs) and Optical Network Units (ONUs), each equipped with processing and queuing capabilities to execute portions of LLM inference tasks locally. These intelligent nodes collaborate under centralized Software-Defined Networking (SDN) control to manage inference-related traffic and optimize resource allocation across the network. Through inference-aware dynamic bandwidth allocation, time and wavelength slicing, and queue-level traffic isolation, the architecture prioritizes LLM traffic to provide low and consistent latency for LLM inference tasks for prompt and token streams without degrading conventional broadband services. Simulation results show that the proposed architecture reduces average inference latency by up to 50%, improves throughput by up to 7%, and lowers jitter and packet drop probability by up to 32% and 25.01%, respectively, while maintaining end-to-end Quality of Service (QoS) under mixed broadband and LLM traffic. © 2013 IEEE.

## 04 — Title Screening

**Title:** Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Enabling Software-Defined Tiered LLM Inference Continuum on Passive Optical Network
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
