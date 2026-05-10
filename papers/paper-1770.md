---
id: paper-1770
title: Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters
authors:
- Lettich, Francesco
- Carlini, Emanuele
- Nardini, Franco Maria
- Perego, Raffaele
- Trani, Salvatore
venue: Proceedings - 2025 IEEE 25th International Symposium on Cluster, Cloud and Internet Computing, CCGrid 2025
venue_type: conference
year: 2025
doi: 10.1109/CCGRID64434.2025.00015
url: https://www.scopus.com/pages/publications/105010817541?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 43--52
keywords:
- GPU Datacenter
- GPU Fragmentation
- GPU-sharing
- Green Computing
- Online Scheduling
- Power-aware Scheduling
- Sustainable Computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1770 — Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rise of Artificial Intelligence and Large Language Models is driving increased GPU usage in data centers for complex training and inference tasks, impacting operational costs, energy demands, and the environmental footprint of large-scale computing infrastructures. This work addresses the online scheduling problem in GPU datacenters, which involves scheduling tasks without knowledge of their future arrivals. We focus on two objectives: minimizing GPU fragmentation and reducing power consumption. GPU fragmentation occurs when partial GPU allocations hinder the efficient use of remaining resources, especially as the datacenter nears full capacity. A recent scheduling policy, Fragmentation Gradient Descent (FGD), leverages a fragmentation metric to address this issue. Reducing power consumption is also crucial due to the significant power demands of GPUs. To this end, we propose PWR, a novel scheduling policy to minimize power usage by selecting power-efficient GPU and CPU combinations. This involves a simplified model for measuring power consumption integrated into a Kubernetes score plugin. Through an extensive experimental evaluation in a simulated cluster, we show how PWR, when combined with FGD, achieves a balanced trade-off between reducing power consumption and minimizing GPU fragmentation.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1770.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
