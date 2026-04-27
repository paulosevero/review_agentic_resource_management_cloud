---
id: "paper-2040"
title: "A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks"
authors: ["Picano, Benedetta", "Hoang, Dinh Thai", "Nguyen, Diep N."]
year: 2025
venue: "IEEE Open Journal of the Communications Society"
venue_type: "journal"
doi: "10.1109/OJCOMS.2025.3561605"
url: "https://www.scopus.com/pages/publications/105002837963?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3795--3805"
keywords: ["distributed inference", "edge intelligence", "Foundation models", "matching theory"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2040 — A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks

## Metadata

- **Authors:** Picano, Benedetta and Hoang, Dinh Thai and Nguyen, Diep N.
- **Year:** 2025
- **Venue:** IEEE Open Journal of the Communications Society
- **DOI:** 10.1109/OJCOMS.2025.3561605
- **URL:** https://www.scopus.com/pages/publications/105002837963?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3795--3805
- **Language:** English
- **Keywords:** distributed inference; edge intelligence; Foundation models; matching theory

### Abstract

With the growing demand for computational and storage capabilities of modern learning models, performing their computation exclusively in a centralized manner has become increasingly impractical. Executing the inference of foundation models in a distributed manner presents significant challenges, particularly in optimizing both computing and communication resources. This work introduces a novel deployment scheme for large language model (LLM) layers that jointly considers computation and communication efficiency within an edge network environment to address these issues. Specifically, we resort to the matching theory to effectively orchestrate the distributed deployment of the LLM layers across the edge nodes of the networks, where nodes have varying computational capacities and communication speed. This framework is based on a two-sided game, enabling each layer to express its individual preferences for node allocation while allowing nodes to prioritize their preferred layers. This mutual selection process minimizes inference latency in the learning process and models the bubble time as game externalities, assuming a sequential pipeline execution. The algorithmic solution reaches a stable matching outcome. Performance evaluation was conducted considering both simulations and a small-scale testbed to measure the effectiveness of the proposed algorithm compared to state-of-the-art alternatives. In particular, the small-scale testbed was developed to distribute an LLM to support autonomous driving, leveraging the vision-language model paradigm. The results highlight performance improvements of up to around 10% in comparison to the Koklata game alternative. © 2020 IEEE.

## 04 — Title Screening

**Title:** A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
