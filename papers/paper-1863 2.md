---
id: "paper-1863"
title: "A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents"
authors: ["Liu, Ya", "Yang, Kai", "Zhu, Yu", "Yang, Keying", "Jian, Chengtao", "Ni, Wuguang", "Ye, Xiaozhou", "Ouyang, Ye"]
year: 2025
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-96-8186-0_1"
url: "https://www.scopus.com/pages/publications/105009402614?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "3--15"
keywords: ["Fine-tuning", "Large language models", "Zeroth-order optimization"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1863 — A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents

## Metadata

- **Authors:** Liu, Ya and Yang, Kai and Zhu, Yu and Yang, Keying and Jian, Chengtao and Ni, Wuguang and Ye, Xiaozhou and Ouyang, Ye
- **Year:** 2025
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-96-8186-0_1
- **URL:** https://www.scopus.com/pages/publications/105009402614?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 3--15
- **Language:** English
- **Keywords:** Fine-tuning; Large language models; Zeroth-order optimization

### Abstract

Large Language Models (LLMs) are transforming the landscape of generative AI. Yet, their immense model sizes tether most LLMs to cloud environments, hindering their adaptability to specific downstream tasks and presenting challenges for scenarios involving private data. To address these issues, we propose a novel fine-tuning approach for end-to-end collaboration between a cloud-hosted LLM and an edge-based LLM agent, leveraging a Sandwiched Tuning framework. This approach not only boosts flexibility and scalability but also empowers users with heightened security and compliance, allowing tradeoffs between performance and cost. The proposed framework models cloud-edge collaboration as a nested optimization problem, which is under a grey-box constraint due to the cloud LLM’s parameters’ unavailability. Tailored to the unique problem structure, we introduce a computationally efficient nested Zeroth-order Cutting Plane (ZoCP) algorithm. We explore various collaboration modes, both parallel and serial, and conduct experiments to verify our effectiveness in each mode. Our extensive experiments reveal that our method delivers up to a 47.9% performance improvement over traditional methods. Additionally, we establish a convergence rate for ZoCP that is independent of the number of optimization parameters, highlighting its scalability on large-scale edge LLMs. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

## 04 — Title Screening

**Title:** A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents
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
