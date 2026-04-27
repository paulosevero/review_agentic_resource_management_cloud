---
id: "paper-288"
title: "An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models"
authors: ["Ganiev, Amir", "Chapin, Colt", "de Andrade, Anderson", "Liu, Chen"]
year: 2021
venue: "NAACL-HLT 2021 - 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Industry Papers"
venue_type: "conference"
doi: "10.18653/v1/2021.naacl-industry.21"
url: "https://www.scopus.com/pages/publications/85137339310?origin=resultslist"
publisher: "Association for Computational Linguistics (ACL)"
pages: "163--169"
keywords: ["Computational linguistics", "Development process", "Emotion analysis", "Language model", "Large volumes", "Large-scales", "Learning architectures", "Machine-learning", "Performance", "Probability: distributions", "Running time", "Probability distributions"]
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
    human_justification: "LLM as workload"

---

# paper-288 — An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models

## Metadata

- **Authors:** Ganiev, Amir and Chapin, Colt and de Andrade, Anderson and Liu, Chen
- **Year:** 2021
- **Venue:** NAACL-HLT 2021 - 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Industry Papers
- **DOI:** 10.18653/v1/2021.naacl-industry.21
- **URL:** https://www.scopus.com/pages/publications/85137339310?origin=resultslist
- **Publisher:** Association for Computational Linguistics (ACL)
- **Pages:** 163--169
- **Language:** English
- **Keywords:** Computational linguistics; Development process; Emotion analysis; Language model; Large volumes; Large-scales; Learning architectures; Machine-learning; Performance; Probability: distributions; Running time; Probability distributions

### Abstract

This work demonstrates the development process of a machine learning architecture for inference that can scale to a large volume of requests. In our experiments, we used a BERT model that was fine-tuned for emotion analysis, returning a probability distribution of emotions given a paragraph. The model was deployed as a gRPC service on Kubernetes. Apache Spark was used to perform inference in batches by calling the service. We encountered some performance and concurrency challenges and created solutions to achieve faster running time. Starting with 3.3 successful inference requests per second, we were able to achieve as high as 300 successful requests per second with the same batch job resource allocation. As a result, we successfully stored emotion probabilities for 95 million paragraphs within 96 hours. © 2021 Association for Computational Linguistics.

## 04 — Title Screening

**Title:** An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models
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
