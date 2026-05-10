---
id: paper-2197
title: Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning
authors:
- Tan, Ling
- Song, Jing
- Sun, Lei
- Wang, Haifeng
- Xu, Hai
venue: Physical Communication
venue_type: journal
year: 2025
doi: 10.1016/j.phycom.2025.102916
url: https://www.scopus.com/pages/publications/105021850374?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- DPTL inspection network
- Edge computing
- Load balancing
- Multi-agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2197 — Energy-saving and load-aware optimization of power grid inspection based on MEC and multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The high dense power transmission line (DPTL), as transmission hubs, are characterized by complex line layouts and difficulty in inspection. We have designed a DPTL inspection network, in which obstacle-traversable inspection robots (OTIR) move on transmission lines and act as sensing and computing nodes to achieve full-coverage inspection of transmission lines. To improve inspection efficiency, the network integrates Mobile Edge Computing (MEC) and Device-to-Device (D2D) communication technologies to facilitate task offloading. We formulate an optimization problem for task offloading to achieve energy consumption balance and minimization objectives. Considering the dynamic and time-varying environment, we use the Lyapunov dynamic energy queue optimization scheme to transform the stochastic optimization problem into independent decisions for each time slot. In addition, we propose a multi-agent reinforcement learning algorithm based on an adaptive reward mechanism. This algorithm integrates digital twin technology to real-time perceive the dynamic states of the DPTL network, optimizing task scheduling through collaborative communication, thereby improving the overall efficiency and stability of the system. The simulation results demonstrate that the proposed algorithm exhibits good convergence performance. Compared with adaptive reward multi-agent advantage actor-critic(AR-MAA2C) and the deep deterministic policy gradient (DDPG) algorithms, the total inspection energy consumption of OTIRs is reduced by approximately 10.4% and 13.7%, respectively. Moreover, energy utilization efficiency is improved by about 5.6% and 7.3%, and the energy consumption balance reaches nearly 0.98, indicating that the proposed method effectively achieves high energy optimization and load balancing. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2197.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
