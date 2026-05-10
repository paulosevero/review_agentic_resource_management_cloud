---
id: paper-0752
title: Behavior-Based Formation Control Digital Twin for Multi-AUG in Edge Computing
authors:
- Wen, Jiabao
- Yang, Jiachen
- Li, Yang
- He, Jingyi
- Li, Zhengjian
- Song, Houbing
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2023
doi: 10.1109/TNSE.2022.3198818
url: https://www.scopus.com/pages/publications/85136730793?origin=resultslist
publisher: IEEE Computer Society
pages: 2791--2801
keywords:
- AUG behavior
- Digital twin
- maritime communication
- multi-AUG cooperative
- path planning
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

# paper-0752 — Behavior-Based Formation Control Digital Twin for Multi-AUG in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The new generation of artificial intelligence technology has improved the autonomous monitoring capabilities of marine equipment. The ocean monitoring platform based on edge computing realizes the autonomous collaboration of multi-agent equipment groups. Autonomous Underwater Glider (AUG) is a new type of energy-saving marine equipment that can realize long-range ocean exploration. However, the non-negligible power constraints, time delays, communication failures and other unfavorable factors in the special underwater working environment have brought great challenges to the underwater monitoring operations of multi-AUG systems. This research establishes an improved artificial potential field method scheme based on the Maritime Internet of Things, which is based on the AUG leader's edge device to control multi-AUGs. In this process, an improved artificial potential field method is designed to solve the local optimal problem through behavior-based path optimization. Then, multi-AUGs are controlled to adapt to the task team plan based on the edge computing of the AUG leader. From the experimental results, it effectively realizes the AUG group cooperative control in the leader mode. Meanwhile, we established a marine communication model and AUG physics engine control model to complete a digital twin of multi-AUG monitoring tasks. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0752.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
