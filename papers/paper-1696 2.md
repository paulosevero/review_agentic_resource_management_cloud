---
id: "paper-1696"
title: "Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach"
authors: ["Jia, Difei", "Hu, Fengye", "Ling, Zhuang", "Li, Hailong", "Gao, Yang"]
year: 2025
venue: "IEEE Transactions on Communications"
venue_type: "journal"
doi: "10.1109/TCOMM.2025.3577638"
url: "https://www.scopus.com/pages/publications/105008030172?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "11528--11544"
keywords: ["computation offloading", "deep reinforcement learning (DRL)", "High-speed railway (HSR)", "resource allocation", "symbiotic radio (SR)"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1696 — Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach

## Metadata

- **Authors:** Jia, Difei and Hu, Fengye and Ling, Zhuang and Li, Hailong and Gao, Yang
- **Year:** 2025
- **Venue:** IEEE Transactions on Communications
- **DOI:** 10.1109/TCOMM.2025.3577638
- **URL:** https://www.scopus.com/pages/publications/105008030172?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 11528--11544
- **Language:** English
- **Keywords:** computation offloading; deep reinforcement learning (DRL); High-speed railway (HSR); resource allocation; symbiotic radio (SR)

### Abstract

This paper investigates a symbiotic radio (SR)-assisted mobile edge computing (MEC) network for railway Internet of Things (RIoT) services, where IoT devices parasitize in a train-ground primary network for passively modulating their computation tasks over computation offloading by associating a mobile relay (MR) on the high-speed railway (HSR). The multi-antenna base station (BS) integrated with the MEC server recovers computation task data from MRs and IoT devices through joint decoding. With the objective of maximizing the total computation efficiency (CE) of all MRs while satisfying the computation requirements of IoT devices, we formulate a computation offloading and resource allocation problem that jointly optimizes the association strategy between MRs and IoT devices, the received beamforming of the BS, the transmission power and computation frequency of MRs. However, since the rapid variation of channel conditions in HSRs poses difficulties to centralized optimization methods in terms of both accurate model acquisition and computation overhead, we utilize a model-free deep reinforcement learning (DRL) approach to propose a fingerprint-based distributed dueling double deep Q-network (FD<sup>4</sup>QN)-based computation offloading and resource allocation scheme to solve the above problem. In particular, this scheme describes the original problem as a partially observable Markov decision process (POMDP), and then incorporates low-dimensional fingerprint markers in each computing agent to stabilize the experience replay mechanism in a multi-agent environment, thereby enhancing training robustness. Moreover, each agent makes a decision for each MR at each time frame by using a dueling double deep Q-network (D3QN) framework based on the local observation state. Simulation results show that the proposed scheme achieves superior performance compared to other benchmark schemes. © 1972-2012 IEEE.

## 04 — Title Screening

**Title:** Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
