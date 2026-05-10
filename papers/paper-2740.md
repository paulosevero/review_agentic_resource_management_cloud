---
id: paper-2740
title: 'GreenAccounter: A toolkit for carbon-aware orchestration of deep learning workloads in geo-distributed clouds'
authors:
- Park, Jeonghyeon
- Kim, Jaekyeong
- Son, Wonseok
- Chun, Sejin
venue: SoftwareX
venue_type: journal
year: 2026
doi: 10.1016/j.softx.2026.102550
url: https://www.scopus.com/pages/publications/105029704956?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Carbon-aware
- Deep learning
- Multi-cloud environments
- Workload migration
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2740 — GreenAccounter: A toolkit for carbon-aware orchestration of deep learning workloads in geo-distributed clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deep learning workloads generate substantial carbon emissions in data centers, largely because training is both time-consuming and energy-intensive. To address this challenge, previous studies have explored either temporal workload shifting or spatial workload migration. Still, these approaches remain limited for long-running workloads, such as Large Language Models (LLMs), because they fail to adapt to continuous fluctuations in regional carbon intensity. In this paper, we introduce GreenAccounter , a toolkit for carbon-aware orchestration of deep learning workloads across multi-cloud environments. It integrates real-time carbon intensity monitoring with checkpoint-based migration, allowing training to continue seamlessly while reducing emissions. A unified dashboard visualizes regional carbon intensity, cumulative emissions, and power consumption, providing operators with a single pane of glass for managing distributed cloud resources. GreenAccounter serves as both (i) a reproducible research platform for carbon-aware scheduling and (ii) a practical operational toolkit for emissions reduction in AI training. As an open-source release, it promotes sustainable, transparent, and data-driven practices for large-scale deep learning. © 2026 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2740.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
