---
id: paper-1700
title: A two-layer UAV cooperative computing offloading strategy based on deep reinforcement learning
authors:
- Jianfei, Zhang
- Zhen, Wang
- Yun, Hu
- Zheng, Chang
venue: China Communications
venue_type: journal
year: 2025
doi: 10.23919/JCC.ja.2024-0650
url: https://www.scopus.com/pages/publications/105021848290?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 251--268
keywords:
- cooperative computational offloading
- deep reinforcement learning
- mobile edge computing
- prioritized experience replay
- two-layer unmanned aerial vehicles
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1700 — A two-layer UAV cooperative computing offloading strategy based on deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the wake of major natural disasters or human-made disasters, the communication infrastructure within disaster-stricken areas is frequently damaged. Unmanned aerial vehicles (UAVs), thanks to their merits such as rapid deployment and high mobility, are commonly regarded as an ideal option for constructing temporary communication networks. Considering the limited computing capability and battery power of UAVs, this paper proposes a two-layer UAV cooperative computing offloading strategy for emergency disaster relief scenarios. The multi-agent twin delayed deep deterministic policy gradient (MATD3) algorithm integrated with prioritized experience replay (PER) is utilized to jointly optimize the scheduling strategies of UAVs, task offloading ratios, and their mobility, aiming to diminish the energy consumption and delay of the system to the minimum. In order to address the aforementioned non-convex optimization issue, a Markov decision process (MDP) has been established. The results of simulation experiments demonstrate that, compared with the other four baseline algorithms, the algorithm introduced in this paper exhibits better convergence performance, verifying its feasibility and efficacy.  © 2013 China Institute of Communications.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1700.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
