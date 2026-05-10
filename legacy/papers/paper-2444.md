---
id: "paper-2444"
title: "LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration"
authors: ["Zhang, Yingyi", "Jia, Pengyue", "Li, Xianneng", "Xu, Derong", "Wang, Maolin", "Wang, Yichao", "Du, Zhaocheng", "Guo, Huifeng", "Liu, Yong", "Tang, Ruiming", "Zhao, Xiangyu"]
year: 2025
venue: "Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining"
venue_type: "conference"
doi: "10.1145/3711896.3737036"
url: "https://www.scopus.com/pages/publications/105014588850?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "3889--3900"
keywords: ["cloud-device framework", "large language model", "privacy-preserving"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2444 — LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration

## Metadata

- **Authors:** Zhang, Yingyi and Jia, Pengyue and Li, Xianneng and Xu, Derong and Wang, Maolin and Wang, Yichao and Du, Zhaocheng and Guo, Huifeng and Liu, Yong and Tang, Ruiming and Zhao, Xiangyu
- **Year:** 2025
- **Venue:** Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining
- **DOI:** 10.1145/3711896.3737036
- **URL:** https://www.scopus.com/pages/publications/105014588850?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 3889--3900
- **Language:** English
- **Keywords:** cloud-device framework; large language model; privacy-preserving

### Abstract

Cloud-device collaboration leverages on-cloud Large Language Models (LLMs) for handling public user queries and on-device Small Language Models (SLMs) for processing private user data, collectively forming a powerful and privacy-preserving solution. However, existing approaches often fail to fully leverage the scalable problem-solving capabilities of on-cloud LLMs while underutilizing the advantage of on-device SLMs in accessing and processing personalized data. This leads to two interconnected issues: 1) Limited utilization of the problem-solving capabilities of on-cloud LLMs, which fail to align with personalized user-task needs, and 2) Inadequate integration of user data into on-device SLM responses, resulting in mismatches in contextual user information. In this paper, we propose a Leader-Subordinate Retrieval framework for Privacy-preserving cloud-device collaboration (LSRP), a novel solution that bridges these gaps by: 1) enhancing on-cloud LLM guidance to on-device SLM through a dynamic selection of task-specific leader strategies named as user-to-user retrieval-augmented generation (U-U-RAG), and 2) integrating the data advantages of on-device SLMs through small model feedback Direct Preference Optimization (SMFB-DPO) for aligning the on-cloud LLM with the on-device SLM. Experiments on two datasets demonstrate that LSRP consistently outperforms state-of-the-art baselines, significantly improving question-answer relevance and personalization, while preserving user privacy through efficient on-device retrieval. Our code is available at: https://github.com/Applied-Machine-Learning-Lab/LSRP. © 2025 ACM.

## 04 — Title Screening

**Title:** LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
