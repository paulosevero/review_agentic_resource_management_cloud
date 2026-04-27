---
id: "paper-1205"
title: "Titanic: Towards Production Federated Learning with Large Language Models"
authors: ["Su, Ningxin", "Hu, Chenghao", "Li, Baochun", "Li, Bo"]
year: 2024
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM52122.2024.10621164"
url: "https://www.scopus.com/pages/publications/85197038129?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "611--620"
keywords: ["Data privacy", "Differential privacy", "Integer programming", "Modeling languages", "Natural language processing systems", "Problem oriented languages", "Client devices", "Communication overheads", "Computation costs", "Datacenter", "Fine tuning", "Language model", "Local training", "Performance", "Private data", "Research interests", "Federated learning"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1205 — Titanic: Towards Production Federated Learning with Large Language Models

## Metadata

- **Authors:** Su, Ningxin and Hu, Chenghao and Li, Baochun and Li, Bo
- **Year:** 2024
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM52122.2024.10621164
- **URL:** https://www.scopus.com/pages/publications/85197038129?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 611--620
- **Language:** English
- **Keywords:** Data privacy; Differential privacy; Integer programming; Modeling languages; Natural language processing systems; Problem oriented languages; Client devices; Communication overheads; Computation costs; Datacenter; Fine tuning; Language model; Local training; Performance; Private data; Research interests; Federated learning

### Abstract

With the recent surge of research interests in Large Language Models (LLMs), a natural question that arises is how pre-trained LLMs can be fine-tuned to tailor to specific needs of enterprises and individual users, while preserving the privacy of data used in the fine-tuning process. On the one hand, sending private data to cloud datacenters for fine-tuning is, without a doubt, unacceptable from a privacy perspective. On the other hand, conventional federated learning requires each client to perform local training, which is not feasible for LLMs with respect to both computation costs and communication overhead, since they involve billions of model parameters. In this paper, we present Titanic, a new distributed training paradigm that allows LLMs to be fine-tuned in a privacy-preserving fashion directly on the client devices where private data is produced, while operating within the resource constraints on computation and communication bandwidth. Titanic first optimally selects a subset of clients with an efficient solution to an integer optimization problem, then partitions an LLM across multiple client devices, and finally fine-tunes the model with no or minimal losses in training performance. A primary focus in the design of Titanic is its feasibility in real-world systems: it is first and foremost designed for production-quality systems, featuring a model-agnostic partitioning mechanism that is fully automated. Our experimental results show that Titanic achieves superior training performance as compared to conventional federated learning, while preserving data privacy and satisfying all constraints on local computation and bandwidth resources. © 2024 IEEE.

## 04 — Title Screening

**Title:** Titanic: Towards Production Federated Learning with Large Language Models

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Titanic: Towards Production Federated Learning with Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Titanic: Towards Production Federated Learning with Large Language Models
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
