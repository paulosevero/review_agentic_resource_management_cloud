---
id: "paper-1971"
title: "LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning"
authors: ["Moshiri, Parisa Fard", "Zhu, Xinyu", "Lohan, Poonam", "Kantarci, Burak", "Janulewicz, Emil"]
year: 2025
venue: "Proceedings of the 16th International Conference on Network of the Future, NoF 2025"
venue_type: "conference"
doi: "10.1109/NoF66640.2025.11223314"
url: "https://www.scopus.com/pages/publications/105024948569?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "28--36"
keywords: ["BART", "DRL", "FLAN-T5", "Language Model", "Network State Monitoring", "SFC provisioning", "VNF placement"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: ""
    human_justification: ""

---

# paper-1971 — LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning

## Metadata

- **Authors:** Moshiri, Parisa Fard and Zhu, Xinyu and Lohan, Poonam and Kantarci, Burak and Janulewicz, Emil
- **Year:** 2025
- **Venue:** Proceedings of the 16th International Conference on Network of the Future, NoF 2025
- **DOI:** 10.1109/NoF66640.2025.11223314
- **URL:** https://www.scopus.com/pages/publications/105024948569?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 28--36
- **Language:** English
- **Keywords:** BART; DRL; FLAN-T5; Language Model; Network State Monitoring; SFC provisioning; VNF placement

### Abstract

Effective management of Service Function Chains (SFCs) and optimal Virtual Network Function (VNF) placement are critical challenges in modern Software-Defined Networking (SDN) and Network Function Virtualization (NFV) environments. Although Deep Reinforcement Learning (DRL) is widely adopted for dynamic network decision-making, its inherent dependency on structured data and fixed action rules often limits adaptability and responsiveness, particularly under unpredictable network conditions. This paper introduces LiLM-RDB-SFC, a novel approach combining Lightweight Language Model (LiLM) with Relational Database (RDB) to answer network state queries to guide DRL model for efficient SFC provisioning. Our proposed approach leverages two LiLMs, Bidirectional and Auto-Regressive Transformers (BART) and the Fine-tuned Language Net T5 (FLAN-T5), to interpret network data and support diverse query types related to SFC demands, data center resources, and VNF availability. Results demonstrate that FLAN-T5 outperforms BART with a lower test loss (0.00161 compared to 0.00734), higher accuracy (9 4. 7 9% compared to 8 0. 2%), and less processing time (2h 2min compared to 2h 38min). Moreover, when compared to the large language model SQLCoder, FLAN-T5 has almost same accuracy while cutting processing time by 96% (SQLCoder: 54 h 43 min; FLAN-T5: 2 h 2 min).  © 2025 IEEE.

## 04 — Title Screening

**Title:** LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LiLM-RDB-SFC: Lightweight Language Model with Relational Database-Guided DRL for Optimized SFC Provisioning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
