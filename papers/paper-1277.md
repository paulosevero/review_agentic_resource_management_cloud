---
id: paper-1277
title: 'Beyond Efficiency: Scaling AI Sustainably'
authors:
- Wu, Carole-Jean
- Acun, Bilge
- Raghavendra, Ramya
- Hazelwood, Kim
venue: IEEE Micro
venue_type: journal
year: 2024
doi: 10.1109/MM.2024.3409275
url: https://www.scopus.com/pages/publications/85195420787?origin=resultslist
publisher: IEEE Computer Society
pages: 37--46
keywords:
- Carbon dioxide
- Cost effectiveness
- Deep learning
- Energy efficiency
- Life cycle
- AI applications
- Carbon emissions
- Computational modelling
- Cost effective
- Datacenter
- Energy
- Energy efficient
- Hardware
- Scalings
- Task analysis
- Carbon footprint
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1277 — Beyond Efficiency: Scaling AI Sustainably

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Barrosoâs seminal contributions in energy-proportional warehouse-scale computing launched an era where modern data centers have become more energy efficient and cost-effective than ever before. Simultaneously, modern AI applications have driven ever-increasing demands in computing, highlighting the importance of optimizing efficiency across the entire deep learning model development cycle. This article characterizes the carbon impact of AI, including both operational carbon emissions from training and inference and embodied carbon emissions from data center construction and hardware manufacturing. We highlight key efficiency optimization opportunities for cutting-edge AI technologies, from deep learning recommendation models to multimodal generative AI tasks. To scale AI sustainably, we must also go beyond efficiency and optimize across the lifecycle of computing infrastructures, from hardware manufacturing to data center operations and end-of-life processing for the hardware.  © 1981-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1277.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
