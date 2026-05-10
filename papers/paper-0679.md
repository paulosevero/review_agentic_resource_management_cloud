---
id: paper-0679
title: Multi-Agent Deep Reinforcement Learning for D2D-Assisted MEC system with Energy Harvesting
authors:
- Mi, Xin
- He, Huaiwen
venue: International Conference on Advanced Communication Technology, ICACT
venue_type: conference
year: 2023
doi: 10.23919/ICACT56868.2023.10079275
url: https://www.scopus.com/pages/publications/85152194711?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 145--153
keywords:
- D2D communication
- energy harvesting
- MEC
- multi-Agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0679 — Multi-Agent Deep Reinforcement Learning for D2D-Assisted MEC system with Energy Harvesting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> It is challenging for delay-sensitive task offloading in a Device-To-Device(D2D) assisted MEC system with energy harvesting devices due to the dynamic load level at each edge node and the fluctuation of harvested energy. In this paper, we investigate the joint task assignment and frequency control problem for MEC system integrated with D2D communication and energy harvesting. D2D link is leveraged to reduce the traffic load of the cellular base station and improve the utilization of computing resources in MEC. The main objective is to minimize the long-Term average task delay with battery energy constraint. We first formulate a large scale non-linear integer programming problem that makes task assignment and CPU frequency decisions for each active device at each time slot. To solve the sequential decision problem with huge multi-dimensional discrete action space, we propose a multi-Agent reinforcement learning algorithm based on Multi-Agent Proximal Policy Optimization (MAPPO) technique. Our algorithm can work efficiently under non-stationary environment and convergence fast. Experimental results show that our proposed algorithm outperforms other baseline algorithms. © 2023 Global IT Research Institute (GiRI).

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0679.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
