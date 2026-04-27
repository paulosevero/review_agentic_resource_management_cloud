---
id: "paper-1727"
title: "Evaluating the Performance of Kubernetes-Orchestrated Multi-Agent Systems: A Case Study on University Course Timetabling"
authors: ["Kaziz, Alisher", "Kumalakov, Bolatzhan"]
year: 2025
venue: "SIST 2025 - 2025 IEEE 5th International Conference on Smart Information Systems and Technologies, Conference Proceedings"
venue_type: "conference"
doi: "10.1109/SIST61657.2025.11139200"
url: "https://www.scopus.com/pages/publications/105016844055?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Cloud Computing", "Container Orchestration", "Kubernetes", "Multi-Agent Systems", "Timetabling Problem"]
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

# paper-1727 — Evaluating the Performance of Kubernetes-Orchestrated Multi-Agent Systems: A Case Study on University Course Timetabling

## Metadata

- **Authors:** Kaziz, Alisher and Kumalakov, Bolatzhan
- **Year:** 2025
- **Venue:** SIST 2025 - 2025 IEEE 5th International Conference on Smart Information Systems and Technologies, Conference Proceedings
- **DOI:** 10.1109/SIST61657.2025.11139200
- **URL:** https://www.scopus.com/pages/publications/105016844055?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud Computing; Container Orchestration; Kubernetes; Multi-Agent Systems; Timetabling Problem

### Abstract

Paper evaluates cloneMap, a Kubernetes-orchestrated Multi-Agent System framework, applied to the University Course Timetabling Problem. The study examines how adjusting the number of containers and clusters impacts system performance, scalability, and resource utilization. By leveraging Kubernetes' automated scaling and resource management, the framework enhances MAS efficiency in distributed cloud environments. Experiments show execution time improved by 45.8% when scaling from 10 to 50 containers, while communication latency increased by 166% when using up to 5 clusters. Results show that increasing containers significantly reduces execution time up to an optimal threshold, beyond which communication overhead limits further gain. Multi-cluster scaling reduces resource contention but increases communication latency, affecting overall efficiency. Findings indicate that Kubernetes provides a strong foundation for scalable MAS deployments, though careful resource allocation is needed to avoid diminishing returns. This study offers insights into optimizing Multi-Agent System performance in cloud-native environments, with future work focusing on improved communication protocols and adaptive scaling strategies.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Evaluating the Performance of Kubernetes-Orchestrated Multi-Agent Systems: A Case Study on University Course Timetabling

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Evaluating the Performance of Kubernetes-Orchestrated Multi-Agent Systems: A Case Study on University Course Timetabling
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Evaluating the Performance of Kubernetes-Orchestrated Multi-Agent Systems: A Case Study on University Course Timetabling
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
