---
id: "paper-1758"
title: "Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation"
authors: ["Lakshmanan, Murugan"]
year: 2025
venue: "2025 8th International Conference on Circuit, Power and Computing Technologies, ICCPCT 2025"
venue_type: "conference"
doi: "10.1109/ICCPCT65132.2025.11176777"
url: "https://www.scopus.com/pages/publications/105020171206?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1085--1091"
keywords: ["Asynchronous communication", "Dense Passage Retrieval", "large language models", "Retrieval-Augmented Generation"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1758 — Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation

## Metadata

- **Authors:** Lakshmanan, Murugan
- **Year:** 2025
- **Venue:** 2025 8th International Conference on Circuit, Power and Computing Technologies, ICCPCT 2025
- **DOI:** 10.1109/ICCPCT65132.2025.11176777
- **URL:** https://www.scopus.com/pages/publications/105020171206?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1085--1091
- **Language:** English
- **Keywords:** Asynchronous communication; Dense Passage Retrieval; large language models; Retrieval-Augmented Generation

### Abstract

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by integrating external knowledge through retrieval mechanisms, thereby improving the contextual relevance and accuracy of generated responses. However, conventional RAG systems often encounter challenges related to high latency, limited scalability, and the complexity of managing infrastructure particularly in real-time streaming environments. To overcome these barriers, this work proposes a novel serverless RAG-Stream architecture, designed to deliver low-latency, highly scalable, and cost-effective data processing. The architecture employs AWS Kinesis for real-time data ingestion, Dense Passage Retrieval (DPR) for semantic search, and cloud-based LLMs for dynamic response generation. Workflow orchestration is achieved using serverless functions and asynchronous communication, ensuring optimal resource utilization and simplified management. Experimental evaluations, performed using the WikiText-103 dataset alongside four subsets of the Pile benchmark such as Enron Emails, HackerNews, NIH ExPorter, and YouTube Subtitles, reveal significant performance gains. The serverless RAGStream system achieved an average latency of 150 ms, sustained a throughput of 500 requests per second, and produced highquality outputs, as validated by BLEU, ROUGE, METEOR, and BERTScore metrics. Compared to baseline models, the proposed architecture demonstrates superior scalability, reduced operational complexity, and maintained generation quality, positioning it as a robust solution for real-time, AIpowered applications. © 2025 IEEE.

## 04 — Title Screening

**Title:** Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation
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
