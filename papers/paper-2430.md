---
id: paper-2430
title: Energy and Fairness Optimization in RIS-Assisted Multi-UAV AMEC Based on Multi-Agent Reinforcement Learning
authors:
- Zhang, Chao
- Wang, Junxuan
- Zhang, Yanyan
- Chen, Jiale
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2025
doi: 10.1117/12.3093872
url: https://www.scopus.com/pages/publications/105026838433?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- MEC
- Multi-Agent Deep Reinforcement Learning (MADRL)
- RIS
- UAV
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2430 — Energy and Fairness Optimization in RIS-Assisted Multi-UAV AMEC Based on Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In Mobile Edge Computing (MEC), Unmanned Aerial Vehicles (UAVs) have shown great promise—especially in emergency communication scenarios—thanks to their flexible deployment and on-demand service capabilities. Meanwhile, Reconfigurable Intelligent Surfaces (RIS), as an emerging technology, can effectively extend MEC network coverage and optimize the wireless propagation environment. This paper proposes a novel RIS-assisted multi-UAV aerial MEC (AMEC) system, aiming jointly to maximize system fairness and minimize total energy consumption by optimizing UAV flight trajectories, RIS phase-shift configurations, task-offloading strategies, and resource allocation. To tackle this mixed nonconvex optimization problem, we develop the BPMADDPG algorithm: in the first phase, block coordinate descent (BCD) is used to optimize RIS phase shifts; in the second phase, a modified multi-agent deep deterministic policy gradient (MADDPG) framework enhanced with prioritized experience replay (PER) achieves coordinated multi-agent scheduling. Simulation results demonstrate that, compared with several benchmark schemes, the proposed method achieves significant reductions in energy consumption and notable improvements in fairness. © 2025 SPIE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2430.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
