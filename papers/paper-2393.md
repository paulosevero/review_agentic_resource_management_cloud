---
id: paper-2393
title: Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip
authors:
- Yu, Xingmao
- Jiang, Dingcheng
- Deng, Jinyi
- Liu, Jingyao
- Li, Chao
- Yin, Shouyi
- Hu, Yang
venue: Proceedings - International Symposium on Computer Architecture
venue_type: conference
year: 2025
doi: 10.1145/3695053.3731016
url: https://www.scopus.com/pages/publications/105009587404?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 631--645
keywords:
- Computing and hardware architecture
- Datacenter
- Wafer-scale integration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2393 — Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancements in large language models (LLMs) have significantly increased hardware demands. Wafer-scale chips, which integrate numerous compute units on an entire wafer, offer a highdensity computing solution for data centers and can extend Moore's Law at system level. However, current wafer-scale data center architectures face inefficiencies, such as uncoordinated resource allocation and lack of co-optimization for system area, preventing optimal integration density and performance within given cost and physical constraints. We propose a co-exploration approach of computing and hardware architectures to bridge this gap. We first develop an optimized wafer-scale single-cabinet data center model, integrating configurable on-chip memory dies and employing a vertically stacked hardware architecture. Based on this model, we introduce Titan, an automated exploration framework for intra-chip and inter-chip architecture design and optimization. Based on the architecture features of wafer-scale systems with optimal integration density, Titan establishes parameter dependencies to co-design the computing and hardware architectures. To reduce the design cycle for wafer-scale systems, Titan introduces vertical area constraints and pre-checks physical limits by integrating a series of reliability prediction models. It also integrates hardware capacity and cost evaluations to enable multi-objective optimization. Under the same cost constraint, on average, Titan's cabinet design architecture improves system computing capacity by 2.90×, communication bandwidth by 2.11×, and memory bandwidth by 11.23× compared to the state-of-the-art Dojo-like wafer-scale single tray architecture. Simulated in different scenarios, Titan's design delivers 3.17× and 10.66× performance improvement for Llama2-7B and Llama2-72B. Moreover, we leverage Titan to uncover insights into the optimal single-chip area choice within a cabinet under different cost constraints.  © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2393.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
