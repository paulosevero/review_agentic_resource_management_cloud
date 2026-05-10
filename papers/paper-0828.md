---
id: paper-0828
title: 'CAPP-GPT: A computer-aided process planning-generative pretrained transformer framework for smart manufacturing'
authors:
- Azab, Ahmed
- Osman, Hany
- Baki, Fazle
venue: Manufacturing Letters
venue_type: journal
year: 2024
doi: 10.1016/j.mfglet.2024.09.009
url: https://www.scopus.com/pages/publications/85206250479?origin=resultslist
publisher: Elsevier Ltd
pages: 51--62
keywords:
- CAPP-GPT
- Machine Learning
- Macro-CAPP
- Maintenance 4.0
- Micro-CAPP
- Quality 4.0
- Scheduling
- Smart Manufacturing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0828 — CAPP-GPT: A computer-aided process planning-generative pretrained transformer framework for smart manufacturing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Smart manufacturing (SM) constitutes the backbone of Industry 4.0 (I4.0), allowing for heightened autonomy of the various interacting cyber-physical systems, making the various entities on the production floor. Connectivity, a vital enabler, plays a crucial role through state-of-the-art Digital Twinning (DT) technologies driven by underlying innovations like the industrial Internet of Things, Cloud Computing, and advancements in sensory devices. DT, which plays a vital role in the various planning functions under the production and operations management umbrella, is being used in the developed combined CAPP-GPT (Computer-Aided Process Planning-Generative Pretrained Transformer) and production scheduling approach to address disruptions on the shopfloor and in self-healing of the manufacturing processes at a micro-CAPP level by optimally adapting the process parameters and the developed toolpath on the fly based on online process signature measurements. In a leap commensurate with that which has taken place in Natural Language Processing-Large Language Models (Chat-GPT), similar efforts are currently being undertaken to parse CAD data structures and blueprints, fusing operations research and predictive analytics algorithms to carry out setup planning as well as sequencing and grouping manufacturing sub-operations. A hybridized Optimization and Machine Learning (ML) approach is employed where Logical Analysis of Data is used to solve the problem heuristically, exploiting various generative and variant methods at heart. Another extension of this macro-CAPP problem is being tackled by integrating the problem with delayed product differentiation, lot-sizing, and transfer line balance for futuristic batch-production shops employing Hybrid Manufacturing (HM) and Smart Assembly. At the micro-CAPP level, HM process parameters are optimized using a comprehensive approach employing the Taguchi loss function to assess surface roughness, internal failure costs, and other criteria, including greenhouse gas emissions and expended energy. Online measurements of the process signatures are also employed to adapt the initial set of process parameters using different automatic control schemes. ML is used to identify the process parameters carrying simulations on Simulink before the system is deployed. © 2024 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0828.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
