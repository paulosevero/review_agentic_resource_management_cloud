---
id: "paper-1340"
title: "Automatic Mapping of Heterogeneous DNN Models on Adaptive Multiaccelerator Systems"
authors: ["Zhao, Jieru", "Shen, Guan", "Ding, Wenchao", "Chen, Quan", "Guo, Minyi"]
year: 2024
venue: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
venue_type: "journal"
doi: "10.1109/TCAD.2024.3410841"
url: "https://www.scopus.com/pages/publications/85195426215?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4701--4714"
keywords: ["Heterogeneous DNNs", "mapping framework", "multiaccelerator systems", "parallelism strategy", "Transformers"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-1340 — Automatic Mapping of Heterogeneous DNN Models on Adaptive Multiaccelerator Systems

## Metadata

- **Authors:** Zhao, Jieru and Shen, Guan and Ding, Wenchao and Chen, Quan and Guo, Minyi
- **Year:** 2024
- **Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- **DOI:** 10.1109/TCAD.2024.3410841
- **URL:** https://www.scopus.com/pages/publications/85195426215?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4701--4714
- **Language:** English
- **Keywords:** Heterogeneous DNNs; mapping framework; multiaccelerator systems; parallelism strategy; Transformers

### Abstract

As DNNs are developing rapidly, the computational and memory burden imposed on hardware systems grows exponentially. This becomes even more severe for large language models (LLMs) and multimodal models. As a promising solution that achieves high scalability and low manufacturing cost, multiaccelerator systems widely exist in data centers, cloud platforms, and mobile SoCs. Thus, a challenging problem arises: selecting a proper combination of accelerators from available designs and searching for efficient DNN mapping strategies, to fully exploit computation resources and communication bandwidth in the system. To this end, we propose MARS, a novel mapping framework that performs computation-aware accelerator selection and applies communication-aware sharding strategies to maximize parallelism. We also provide optimizations to overlap the computation and communication latency. Considering the high complexity of the design space, we propose two effective mapping algorithms to explore it. Experiments show that MARS achieves 34.3% latency reduction for DNN workloads compared to the baseline and 63.0% latency reduction on heterogeneous models compared to the corresponding state-of-the-art method. © 2024 IEEE.

## 04 — Title Screening

**Title:** Automatic Mapping of Heterogeneous DNN Models on Adaptive Multiaccelerator Systems

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Automatic Mapping of Heterogeneous DNN Models on Adaptive Multiaccelerator Systems
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Automatic Mapping of Heterogeneous DNN Models on Adaptive Multiaccelerator Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
