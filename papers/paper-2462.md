---
id: paper-2462
title: Multiagent Deep-Reinforcement-Learning-Based Cooperative Perception and Computation in VEC
authors:
- Zhao, Liang
- Li, Longjia
- Tan, Zhiyuan
- Hawbani, Ammar
- He, Qiang
- Liu, Zhi
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3546915
url: https://www.scopus.com/pages/publications/86000475391?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 21350--21363
keywords:
- Connected and autonomous vehicles (CAVs)
- cooperative perception (CP)
- multiagent deep reinforcement learning (MDRL)
- vehicular edge computing (VEC)
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

# paper-2462 — Multiagent Deep-Reinforcement-Learning-Based Cooperative Perception and Computation in VEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Connected and autonomous vehicles (CAVs) are an important paradigm of intelligent transportation systems. Cooperative perception (CP) and vehicular edge computing (VEC) enhance CAVs’ perception capacity of the region of interest (RoI) while alleviating the pressure of intensive computation on onboard resources. However, existing CP and computation schemes are based on inefficient broadcast communications and still face challenges, such as highly dynamic communication link channel conditions caused by vehicle mobility, and limited computing resources in VEC environments. Considering the delay sensitivity of CAVs’ perception tasks and the need for enhanced perception, we propose a unicast-based cooperative perception and computation scheme to achieve more efficient resource utilization and perception task execution in VEC scenarios. Our goal is to maximize CP gain and minimize task execution delay by optimizing the decision of each ego CAVs. To solve the sequential decision-making problem of multiobjective optimization, we propose a solution based on improved multiagent proximal policy optimization deep reinforcement learning, where CAVs agents make adaptive decisions distributed based on partial observations. Simulation results show that compared with the baseline algorithm, our proposed scheme effectively reduces the execution delay of ego CAVs perception tasks and ensures a high perception gain. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2462.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
