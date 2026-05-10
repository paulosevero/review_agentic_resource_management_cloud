---
id: paper-0750
title: Research on task offloading optimization strategies for vehicular networks based on game theory and deep reinforcement learning
authors:
- Wang, Lei
- Zhou, Wenjiang
- Xu, Haitao
- Li, Liang
- Cai, Lei
- Zhou, Xianwei
venue: Frontiers in Physics
venue_type: journal
year: 2023
doi: 10.3389/fphy.2023.1292702
url: https://www.scopus.com/pages/publications/85175365139?origin=resultslist
publisher: Frontiers Media SA
pages: ''
keywords:
- cooperative game
- deep reinforcement learning
- multi-access edge computing
- proximate policy optimization
- task offloading
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

# paper-0750 — Research on task offloading optimization strategies for vehicular networks based on game theory and deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous development of the 6G mobile network, computing-intensive and delay-sensitive onboard applications generate task data traffic more frequently. Particularly, when multiple intelligent agents are involved in tasks, limited computational resources cannot meet the new Quality of Service (QoS) requirements. To provide a satisfactory task offloading strategy, combining Multi-Access Edge Computing (MEC) with artificial intelligence has become a potential solution. In this context, we have proposed a task offloading decision mechanism (TODM) based on cooperative game and deep reinforcement learning (DRL). A joint optimization problem is presented to minimize both the overall task processing delay (OTPD) and overall task energy consumption (OTEC). The approach considers task vehicles (TaVs) and service vehicles (SeVs) as participants in a cooperative game, jointly devising offloading strategies to achieve resource optimization. Additionally, a proximate policy optimization (PPO) algorithm is designed to ensure robustness. Simulation experiments confirm the convergence of the proposed algorithm. Compared with benchmark algorithms, the presented scheme effectively reduces delay and energy consumption while ensuring task completion. Copyright © 2023 Wang, Zhou, Xu, Li, Cai and Zhou.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0750.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
