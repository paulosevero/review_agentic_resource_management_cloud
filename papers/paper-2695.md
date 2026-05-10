---
id: paper-2695
title: Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation
authors:
- Lu, Nan
- Yao, Ruiyang
- Wang, Zhaoyang
- Yan, Yuejun
- Wang, Yi
venue: Applied Energy
venue_type: journal
year: 2026
doi: 10.1016/j.apenergy.2025.127132
url: https://www.scopus.com/pages/publications/105024717054?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Computing power
- Data center
- Deep reinforcement learning
- Low-carbon operation
- Task scheduling
- Task splitting
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2695 — Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Artificial intelligence (AI) techniques have shown impressive performance in both industry and academia. In recent years, the energy consumption of AI tasks has experienced exponential growth, and how to schedule arriving AI tasks in a low-carbon manner is worth investigating for data centers. However, due to the computationally intensive and resource-demanding properties of AI tasks, current deferral-based scheduling methods cannot efficiently fit a large AI task (e.g., training a large language model) into low-carbon periods, so the temporal flexibility cannot be fully utilized to reduce carbon emissions. To this end, we propose a low-carbon and quality-of-service (QoS)-aware operation framework for data centers based on AI task splitting and allocation. Specifically, a fine-grained estimation approach is first designed for computing resource requirements of AI tasks under various split strategies; on this basis, each AI task is then split into a varying number of subtasks that can satisfy heterogeneous resource constraints and be smoothly fitted into low-carbon time slots, which is done by our proposed DRL-based scheduler. Extensive comparison experiments are conducted on a publicly available dataset to validate the superiority of the proposed framework, verifying that our proposed method can achieve a significant reduction in carbon emissions and an improvement in QoS. © 2025 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2695.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
