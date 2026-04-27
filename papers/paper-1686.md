---
id: "paper-1686"
title: "Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications"
authors: ["Jain, Aditi M", "Jain, Ayush"]
year: 2025
venue: "2025 6th International Conference on Artificial Intelligence, Robotics, and Control, AIRC 2025"
venue_type: "conference"
doi: "10.1109/AIRC64931.2025.11077484"
url: "https://www.scopus.com/pages/publications/105012182372?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "8--16"
keywords: ["Benchmarking", "Chatbot Systems", "Cost-Efficiency", "Distributed Inference", "Edge Computing", "Hybrid Architectures", "Large Language Models", "Microservices Architecture", "Performance Optimization", "Scalability Analysis"]
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
    human_justification: "LLM as workload"

---

# paper-1686 — Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications

## Metadata

- **Authors:** Jain, Aditi M and Jain, Ayush
- **Year:** 2025
- **Venue:** 2025 6th International Conference on Artificial Intelligence, Robotics, and Control, AIRC 2025
- **DOI:** 10.1109/AIRC64931.2025.11077484
- **URL:** https://www.scopus.com/pages/publications/105012182372?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 8--16
- **Language:** English
- **Keywords:** Benchmarking; Chatbot Systems; Cost-Efficiency; Distributed Inference; Edge Computing; Hybrid Architectures; Large Language Models; Microservices Architecture; Performance Optimization; Scalability Analysis

### Abstract

This paper presents a systematic evaluation of architectural patterns for Large Language Model (LLM) inference in production chatbot applications, addressing the critical challenge of balancing performance, cost, and scalability. We analyze five distinct architectures-monolithic, microservices, edge computing, event-driven, and hybrid edge-microservices-using a novel experimental framework with 100 concurrent users as a baseline. Our methodology incorporates precise measurements of latency profiles, throughput, resource utilization, and cost metrics, employing GPT-3.5-turbo with vLLM optimization. Key findings reveal that hybrid edge-microservices architecture offers 46% lower P99 latency and 67% higher throughput compared to monolithic approaches, while edge computing demonstrates 37% lower CPU usage. We introduce a scaling factor analysis methodology for accurate performance predictions at larger scales, validated through controlled experiments. This research contributes: (1) a systematic evaluation methodology for LLM inference architectures, (2) empirical evidence for architectural decision-making, (3) novel scaling factors for performance prediction, and (4) a detailed cost-benefit analysis across architectural patterns. These insights advance the scientific understanding of LLM deployment strategies and provide crucial guidance for both researchers and practitioners in optimizing large-scale neural inference systems.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
