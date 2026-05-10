---
id: paper-0612
title: 'EMS-SLAM: Edge-Assisted Multi-Agent System Simultaneous Localization and Mapping'
authors:
- Hu, Kai
- Zhan, Lei
- Zou, Longhao
- Chen, Zuozhou
- Muntean, Gabriel-Miro
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2023
doi: 10.1109/VTC2023-Spring57618.2023.10201031
url: https://www.scopus.com/pages/publications/85169841080?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- cooperating multi-agent system
- data fusion
- edge computing
- self-adaptation
- simultaneous localization and mapping
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0612 — EMS-SLAM: Edge-Assisted Multi-Agent System Simultaneous Localization and Mapping

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, there has been a growing demand for robotic environment perception and autonomous driving due to the increasing popularity of visual and geometry-based localization and mapping techniques, such as simultaneous localization and mapping (SLAM). To address this trend, this paper proposes the EMS-SLAM framework, which utilizes cooperative adaptive wireless communication between servers and multi-robot agents to enhance environment perception and self-localization efficiency and accuracy. EMS-SLAM can reduce mapping time and CPU and memory utilization of individual robots while maintaining high accuracy OctoMap based on multi-map fusion and optimization. EMS-SLAM's effectiveness and real-time performance have been validated and tested on publicly available datasets and real robots for real-world operations. The experimental results demonstrate that EMS-SLAM can reduce the CPU utilization of a single robot by approximately 10% and improve the efficiency of large-scale SLAM. The constructed OctoMap achieves centimeter-level accuracy. EMS-SLAM provides reliable, agile, and energy-efficient assistance for large-scale environment perception of robots.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0612.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
