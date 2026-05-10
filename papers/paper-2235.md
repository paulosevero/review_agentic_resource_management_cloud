---
id: paper-2235
title: Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions
authors:
- Vamja, Tirth
- Ray, Kaustabha
- George, Felix
- Devi, Umamaheswari
venue: 2025 5th International Conference on AI-ML-Systems, AIMLSystems 2025
venue_type: conference
year: 2025
doi: 10.1109/AIMLSYSTEMS67835.2025.11330349
url: https://www.scopus.com/pages/publications/105034890127?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 135--143
keywords:
- Computer hardware
- Electric power utilization
- Graphics processing unit
- Green computing
- Information management
- Partitions (building)
- Power management
- Program processors
- Cloud data centers
- Data driven
- Efficient power managements
- Machine-learning
- Model method
- Partition levels
- Power
- Power estimations
- Power modeling
- Reducing costs
- Aggregates
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
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

# paper-2235 — Data-driven Partitioning of Aggregate GPU Power among GPU (MIG) Partitions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient power management in cloud data centers is essential for reducing costs, enhancing performance, and minimizing environmental impact. GPUs, critical for tasks like machine learning (ML) and GenAI, are major contributors to power consumption. NVIDIA's Multi-Instance GPU (MIG) technology improves GPU utilization by enabling isolated partitions with per-partition resource tracking, facilitating GPU sharing by multiple tenants. However, accurately apportioning GPU power consumption among MIG instances, which is required for proper energy and carbon accounting and management, remains challenging due to lack of hardware support. This paper addresses this challenge by developing software methods to estimate power usage per MIG partition. We find that light-weight methods with good accuracy can be difficult to construct and hence explore the use of ML-based power models to enable accurate, partition-level power estimation. Our exploration reveals that a single generic offline power model or modeling method is not applicable across diverse workloads, especially with concurrent MIG usage, and that workload-specific models constructed using partition-level utilization metrics of workloads under execution can significantly improve accuracy. We also propose scaling the MIG power predicted by the models using total measured GPU power, when available, to eliminate aggregate error and reduce error in per-MIG estimations. Using NVIDIA A100 GPUs, we demonstrate and evaluate our approach for accurate partition-level power estimation for workloads including matrix multiplication and Large Language Model inference. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2235.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
