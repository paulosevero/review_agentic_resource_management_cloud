---
id: paper-0277
title: Cooperatively improving data center energy efficiency based on multi-agent deep reinforcement learning†
authors:
- Chi, Ce
- Ji, Kaixuan
- Song, Penglei
- Marahatta, Avinab
- Zhang, Shikui
- Zhang, Fa
- Qiu, Dehui
- Liu, Zhiyong
venue: Energies
venue_type: journal
year: 2021
doi: 10.3390/en14082071
url: https://www.scopus.com/pages/publications/85106324078?origin=resultslist
publisher: MDPI AG
pages: ''
keywords:
- Cooling system
- Data center
- Deep reinforcement learning
- Energy efficiency
- Multi-agent
- Scheduling algorithm
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
    my_justification: RL
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

# paper-0277 — Cooperatively improving data center energy efficiency based on multi-agent deep reinforcement learning†

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The problem of high power consumption in data centers is becoming more and more prominent. In order to improve the energy efficiency of data centers, cooperatively optimizing the energy of IT systems and cooling systems has become an effective way. In this paper, a model-free deep reinforcement learning (DRL)-based joint optimization method MAD3C is developed to overcome the high-dimensional state and action space problems of the data center energy optimization. A hybrid AC-DDPG cooperative multi-agent framework is devised for the improvement of the cooperation between the IT and cooling systems for further energy efficiency improvement. In the framework, a scheduling baseline comparison method is presented to enhance the stability of the framework. Meanwhile, an adaptive score is designed for the architecture in consideration of multi-dimensional resources and resource utilization improvement. Experiments show that our proposed approach can effectively reduce energy for data centers through the cooperative optimization while guaranteeing training stability and improving resource utilization. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0277.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
