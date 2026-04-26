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
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
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

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
