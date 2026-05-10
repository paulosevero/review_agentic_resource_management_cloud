---
id: paper-2515
title: A review of ship fire detection technologies in maritime transportation
authors:
- Bai, Xiangen
- Tao, Zhe
- Xu, Xiaofeng
- Zhou, Changyu
- Wang, Yan
venue: Ocean Engineering
venue_type: journal
year: 2026
doi: 10.1016/j.oceaneng.2025.123989
url: https://www.scopus.com/pages/publications/105025937901?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Deep learning
- Image processing
- Lightweighting
- Multi-sensor fusion
- YOLO
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
    my_justification: Review
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

# paper-2515 — A review of ship fire detection technologies in maritime transportation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Ship fires pose a persistent threat to maritime safety owing to severe consequences, necessitating continuous innovation in detection technologies. This study systematically evaluates the current research landscape in ship fire detection. It analyzes the technological evolution from traditional sensors and image processing to intelligent methods, particularly deep learning(DL) – notably You Only Look Once (YOLO) -series algorithms – and multi-modal fusion, assessing the performance, advantages, and limitations of each. Analysis reveals DL as the predominant research direction, significantly enhancing detection in complex scenarios via model optimizations like lightweight design and attention mechanisms. Furthermore, fusing multi-modal data (e.g., visual, infrared, gas) is recognized for enhancing system robustness. However, critical bottlenecks remain: the scarcity of high-quality, diverse public datasets; poor model generalization in complex maritime environments; and pronounced efficiency-accuracy trade-offs, particularly for edge computing. Future directions include constructing comprehensive datasets, developing models with improved environmental adaptability, and exploring novel paradigms such as multi-agent collaborative detection and early fire signature analysis, aiming for more efficient and reliable ship fire detection and warning. © 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2515.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
