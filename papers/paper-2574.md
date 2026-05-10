---
id: paper-2574
title: 'GR-MADRL: a multi-agent deep reinforcement learning framework with hamiltonian optimization for task offloading in vehicular fog computing'
authors:
- Frimpong, Samuel Akwasi
- Han, Mu
- Zheng, Wenyi
- Quansah, Andrew
venue: Autonomous Agents and Multi-Agent Systems
venue_type: journal
year: 2026
doi: 10.1007/s10458-025-09727-3
url: https://www.scopus.com/pages/publications/105025461932?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Edge intelligence
- Hamiltonian optimization
- Multi-agent deep reinforcement learning
- Task offloading
- Vehicular fog computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2574 — GR-MADRL: a multi-agent deep reinforcement learning framework with hamiltonian optimization for task offloading in vehicular fog computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient task offloading strategies face considerable implementation barriers in vehicular fog computing (VFC) network contexts, due to dynamic vehicular mobility, fluctuating network conditions, and varying fog resource distribution. These complexities hinder efficient task offloading and resource utilization, leading to suboptimal quality of service (QoS) in terms of latency and energy efficiency. Existing deep reinforcement learning and optimization techniques struggle to adapt to these dynamic conditions, necessitating a more robust approach. This paper proposes an advanced task offloading framework that integrates gated recurrent unit-based multi-agent deep reinforcement learning (GR-MADRL) and dynamic Hamiltonian optimization (DHO). Our framework employs an attention-enhanced GRU network to process complex temporal network states, enabling effective feature prioritization and state prediction. Vehicles and fog nodes collaborate as autonomous agents through a multi-agent reinforcement learning system, supported by a central coordinator that constructs a global network view and computes optimal policies for local implementation. Additionally, we formulate the task offloading problem as a dynamic Hamiltonian optimization to maximize long-term rewards and ensure system stability. Extensive simulations demonstrate that GR-MADRL integrated with DHO significantly reduces task latency by 28.3%, lowers energy consumption by 35.1%, and improves task offloading success rates to 94.2%, outperforming baseline methods. These results highlight the potential of this approach to improve scalability, efficiency, and real-time decision making in VFC networks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2574.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
