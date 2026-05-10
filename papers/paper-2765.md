---
id: paper-2765
title: Toward Efficient Orchestration of GenAI Workloads in Modern Container Clouds
authors:
- Santos, José
- Wang, Chen
- Tantawi, Asser
- Tardieu, Olivier
- Maniotis, Pavlos
- Wauters, Tim
- De Turck, Filip
venue: IEEE Communications Magazine
venue_type: journal
year: 2026
doi: 10.1109/MCOM.001.2500262
url: https://www.scopus.com/pages/publications/105031104728?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud platforms
- Containers
- Deep learning
- Digital storage
- Distributed cloud
- Life cycle
- Program processors
- Cloud applications
- Cloud environments
- Communication pattern
- Diverse communications
- Intelligence models
- Network requirements
- Performance and scalabilities
- Real-time inference
- State of the art
- Storage requirements
- Clouds
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2765 — Toward Efficient Orchestration of GenAI Workloads in Modern Container Clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Artificial Intelligence (AI) continues to drive innovation across multiple industries and verticals, the efficient orchestration of AI workloads in modern containerized cloud environments is becoming increasingly crucial. In contrast to traditional cloud applications, modern Generative Artificial Intelligence (GenAI) models and widely used Deep Learning (DL) workloads - particularly those involving real-time inference and distributed training - have unique and highly demanding compute, storage, and network requirements. This article presents our vision for efficient orchestration of diverse AI workloads in container clouds, including a set of orchestration strategies designed to meet the dynamic and resource-intensive needs of state-of-the-art AI applications while ensuring performance and scalability. We discuss the open challenges in orchestrating AI workloads with diverse communication patterns, such as the need for low-latency communication, high-throughput data pipelines, and efficient resource allocation across highly distributed systems. This work also highlights the importance of integrating AI-specific optimizations into popular container orchestration platforms such as Kubernetes (K8s), leveraging modern technologies, including GPU scheduling mechanisms and strategies for distributed training and inference. We envision a future in which container clouds not only scale seamlessly to accommodate the growing demands of AI workloads, but also incorporate AI-driven orchestration mechanisms that intelligently adapt to workload fluctuations, predict resource requirements, and mitigate bottlenecks. This article aims to provide a foundational framework for efficient life-cycle management of AI workloads in modern cloud infrastructures, paving the way for future research in this rapidly evolving field. © 1979-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2765.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
