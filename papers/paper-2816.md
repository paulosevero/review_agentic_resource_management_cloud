---
id: "paper-2816"
title: "A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system"
authors: ["Wang, Chen", "Qian, Zhen", "Li, Guanghui"]
year: 2026
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2026.112117"
url: "https://www.scopus.com/pages/publications/105030549555?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Age of information", "Byzantine attack", "Digital twin", "Task offloading", "Vehicular edge computing"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2816 — A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system

## Metadata

- **Authors:** Wang, Chen and Qian, Zhen and Li, Guanghui
- **Year:** 2026
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2026.112117
- **URL:** https://www.scopus.com/pages/publications/105030549555?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Age of information; Byzantine attack; Digital twin; Task offloading; Vehicular edge computing

### Abstract

Digital Twin (DT)-assisted vehicular edge computing (VEC) presents significant potential for Intelligent Transportation Systems (ITS), yet faces three interconnected challenges in practical implementation. Existing architectures exhibit insufficient adaptability to dynamically optimize physical-layer models in rapidly evolving vehicular environments. At the same time, conventional latency-driven optimization strategies inadequately exploit distributed edge resources and neglect information freshness requirements. Furthermore, global information sharing enabled by DTs introduces critical security vulnerabilities, as malicious agents can exploit this characteristic to launch Byzantine attacks, destabilizing the system. We propose an adaptive vehicular edge computing system (AVECS) in which the DT layer is synchronized with real-world vehicles, and the physical layer models are continuously optimised as the system evolves. A Byzantine resilience mechanism is integrated into the DT layer to improve reliability. We incorporate Age of Information (AoI) into the optimization process to improve the efficiency of task execution. The secure task offloading problem is formulated as a Decentralized Partially Observable Markov Decision Process (DEC-POMDP), and we develop a DT-assisted multi-agent proxy policy optimization (MAPPO) algorithm to learn optimal offloading actions that minimize task completion delay and the average AoI of the entire system. Extensive experiments demonstrate that AVECS reduces task completion delay and improves overall system throughput. The source code of AVECS is available at https://github.com/Gavan-Github/AVECS.git. © 2026 Elsevier B.V.

## 04 — Title Screening

**Title:** A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
