---
id: paper-1607
title: Backscatter communication and multi-agent reinforcement learning enable low-power digital twin system for rural elderly care
authors:
- Guo, Xiaoyan
venue: Discover Internet of Things
venue_type: journal
year: 2025
doi: 10.1007/s43926-025-00232-3
url: https://www.scopus.com/pages/publications/105020264323?origin=resultslist
publisher: Springer Nature
pages: ''
keywords:
- Community resilience
- Digital twin
- Dynamic optimization
- Reinforcement learning
- Rural smart elderly care
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
    my_justification: RL
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

# paper-1607 — Backscatter communication and multi-agent reinforcement learning enable low-power digital twin system for rural elderly care

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Confronted by the global challenge of ageing and the paucity of elderly care resources in rural areas, a novel smart elderly care ecosystem model integrating digital twins and reinforcement learning is proposed. A digital twin platform for elderly care in rural areas has been constructed, combining multi-source IoT and edge computing nodes. This has enabled the resolution of low-bandwidth data fusion issues. The core innovation of this study lies in the deep integration of backscatter communication and multi-agent deep reinforcement learning (MADDPG) into a cohesive system. This integration empowers the dynamic resource scheduling engine to perform real-time service optimisation and emergency response while simultaneously adapting to hardware energy constraints. Specifically, the backscatter communication module provides energy-efficient data links, the status of which is fed as real-time state inputs to the reinforcement learning agents. In return, the MADDPG algorithm output dynamically guides the adjustment of communication parameters. In the pilot areas of Shandong, a significant reduction in the response time to medical emergencies was observed, from 34.7 s to 8.9 s. Furthermore, the service continuity in disaster situations was recorded at 89.2%, indicating a notable enhancement in the effectiveness of emergency response systems. The device’s backscatter communication technology has been demonstrated to ensure a battery life of 68 h when subjected to ± 15% voltage fluctuations, with a 3.2% loss of communication packets. The community resilience index demonstrated a marked increase from 0.72 to 0.94 over a 12-month period, while user satisfaction levels attained 9.6. The cost-benefit analysis of the platform indicates a 2.8-year investment payback period, attributable to reduced medical expenses and enhanced service efficiency. The present study validates the technical solution’s efficacy in addressing the digital divide in rural elderly care, thereby establishing a replicable “technology - policy - community” model for global ageing governance. © The Author(s) 2025.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1607.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
