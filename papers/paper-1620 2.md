---
id: "paper-1620"
title: "A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing"
authors: ["Han, Chengzhuo", "Yang, Tingting", "Cui, Zhengqi", "Sun, Xin"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3583764"
url: "https://www.scopus.com/pages/publications/105009419811?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "51877--51891"
keywords: ["Federated learning", "Internet of Things (IoT) security", "large language models (LLMs) deployment", "privacy preservation", "trustworthy inference"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1620 — A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing

## Metadata

- **Authors:** Han, Chengzhuo and Yang, Tingting and Cui, Zhengqi and Sun, Xin
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3583764
- **URL:** https://www.scopus.com/pages/publications/105009419811?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 51877--51891
- **Language:** English
- **Keywords:** Federated learning; Internet of Things (IoT) security; large language models (LLMs) deployment; privacy preservation; trustworthy inference

### Abstract

This article addresses the challenges of privacy protection, device constraints, resource heterogeneity, and trusted inference in the integration of large language models (LLMs) with Internet of Things (IoT) devices, proposing a hierarchical federated collaborative computing (HFCC) framework. Unlike traditional federated learning, HFCC employs horizontal splitting + chunking to reduce LLMs computation overhead. The framework dynamically splits LLMs into: 1) global shared layers optimized by edge servers and 2) device-local layers trained on private data, ensuring raw data remains on-device. During inference, chunking of shared layers and dynamic task allocation adjust computational loads based on real-time device states, mitigating high-load security risks. Furthermore, leveraging the hierarchical federated learning architecture, the system employs an anonymized parameter aggregation mechanism during training to achieve multilevel privacy protection. Simultaneously, a cross-device consensus verification mechanism performs trusted validation of distributed intermediate results, effectively identifying malicious node behavior. Experiments show 58% faster inference in resource-constrained environments, significantly reduced data exposure risks, and 94% malicious node detection accuracy versus traditional federated learning. This lays a solid foundation for building an intelligent, efficient, and secure IoT ecosystem. © 2014 IEEE.

## 04 — Title Screening

**Title:** A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing
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
