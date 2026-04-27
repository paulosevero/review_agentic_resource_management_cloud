---
id: "paper-845"
title: "Crux: GPU-Efficient Communication Scheduling for Deep Learning Training"
authors: ["Cao, Jiamin", "Guan, Yu", "Qian, Kun", "Gao, Jiaqi", "Xiao, Wencong", "Dong, Jianbo", "Fu, Binzhang", "Cai, Dennis", "Zhai, Ennan"]
year: 2024
venue: "ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference"
venue_type: "conference"
doi: "10.1145/3651890.3672239"
url: "https://www.scopus.com/pages/publications/85202298875?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "1--15"
keywords: ["communication scheduling", "data center network", "deep learning"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-845 — Crux: GPU-Efficient Communication Scheduling for Deep Learning Training

## Metadata

- **Authors:** Cao, Jiamin and Guan, Yu and Qian, Kun and Gao, Jiaqi and Xiao, Wencong and Dong, Jianbo and Fu, Binzhang and Cai, Dennis and Zhai, Ennan
- **Year:** 2024
- **Venue:** ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference
- **DOI:** 10.1145/3651890.3672239
- **URL:** https://www.scopus.com/pages/publications/85202298875?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 1--15
- **Language:** English
- **Keywords:** communication scheduling; data center network; deep learning

### Abstract

Deep learning training (DLT), e.g., large language model (LLM) training, has become one of the most important services in multitenant cloud computing. By deeply studying in-production DLT jobs, we observed that communication contention among different DLT jobs seriously influences the overall GPU computation utilization, resulting in the low efficiency of the training cluster. In this paper, we present Crux, a communication scheduler that aims to maximize GPU computation utilization by mitigating the communication contention among DLT jobs. Maximizing GPU computation utilization for DLT, nevertheless, is NP-Complete; thus, we formulate and prove a novel theorem to approach this goal by GPU intensity-aware communication scheduling. Then, we propose an approach that prioritizes the DLT flows with high GPU computation intensity, reducing potential communication contention. Our 96-GPU testbed experiments show that Crux improves 8.3% to 14.8% GPU computation utilization. The large-scale production trace-based simulation further shows that Crux increases GPU computation utilization by up to 23% compared with alternatives including Sincronia, TACCL, and CASSINI.  © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** Crux: GPU-Efficient Communication Scheduling for Deep Learning Training

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Crux: GPU-Efficient Communication Scheduling for Deep Learning Training
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Crux: GPU-Efficient Communication Scheduling for Deep Learning Training
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
