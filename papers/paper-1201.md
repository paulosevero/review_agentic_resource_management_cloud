---
id: "paper-1201"
title: "STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning"
authors: ["Song, Boxuan", "Wang, Fei"]
year: 2024
venue: "Ad Hoc Networks"
venue_type: "journal"
doi: "10.1016/j.adhoc.2023.103370"
url: "https://www.scopus.com/pages/publications/85178585212?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["DDPG", "MADRL", "Mobile edge computing", "Multi-cell communication systems", "Secure communications", "STAR-RISs"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1201 — STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning

## Metadata

- **Authors:** Song, Boxuan and Wang, Fei
- **Year:** 2024
- **Venue:** Ad Hoc Networks
- **DOI:** 10.1016/j.adhoc.2023.103370
- **URL:** https://www.scopus.com/pages/publications/85178585212?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** DDPG; MADRL; Mobile edge computing; Multi-cell communication systems; Secure communications; STAR-RISs

### Abstract

The poor propagation environment between user equipments (UEs) and mobile edge computing (MEC) servers may lead to UEs’ high energy consumptions and task delay. Reconfigurable intelligent surface (RIS) can significantly improve the quality of wireless propagation environment by intelligently adjusting the phase-shifts and amplitudes of its reflecting elements. However, the passive or active RISs can only reflect signals, i.e., the transmitters and receivers must be located on the same side of RISs. Simultaneous transmitting and reflecting (STAR) RIS, which can transmit and reflect incident signals simultaneously, has been recognized a promising solution to solve the above problem. For STAR-RIS-aided multi-cell secure communications MEC systems, we first formulate an optimization problem to minimize the sum of weighted delay and energy consumptions of all UEs, by jointly optimizing the phase-shifts and amplitudes of STAR-RISs and system spectrum and computation resource allocations. Second, under the practical coupled phase-shift model of STAR-RIS, we develop a multi-agent deep reinforcement learning (MADRL) based scheme, where the access point (AP) in each cell acts an agent to decide phase-shifts, amplitudes, computation task offloading proportions, etc, for the STAR-RIS and UEs within its coverage based on deep deterministic policy gradient (DDPG), by taking into account interference among multiple cells and possible information leakage of UEs. Finally, we verify and evaluate the performance of the proposed scheme through extensive simulations. The simulation results show that our proposed MADRL-based scheme outperforms the existing benchmarks by employing multiple agents and considering co-channel interference among cells. Moreover, simulation results also show that the performance of our developed scheme can indeed be improved by using STAR-RISs. © 2023 Elsevier B.V.

## 04 — Title Screening

**Title:** STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
