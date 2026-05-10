---
id: paper-2935
title: 'Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach'
authors:
- Zhong, Liang
- Tian, Shen
- Zeng, Deze
- Qu, Zhihao
- Hu, Chengyu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3658536
url: https://www.scopus.com/pages/publications/105028895133?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15976--15988
keywords:
- Deep reinforcement learning
- depth of discharge (DoD)
- Lyapunov optimization
- satellite edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2935 — Battery Lifetime Extension in Heterogeneous Satellite Edge Computing: A Lyapunov-DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low Earth orbit (LEO) satellite mobile edge computing (SMEC) has emerged as a pivotal technology for delivering low-latency communication and computational services to underserved regions. However, ensuring sustainable operation of SMEC systems remains challenging due to limited onboard energy and battery degradation, which is critically influenced by the depth of discharge (DoD). This article investigates the collaborative DoD optimization problem in heterogeneous SMEC, formulating it as a long-term stochastic optimization aimed at minimizing DoD while maintaining system stability under dynamic energy supply and stochastic task arrivals. To address the computational intractability of this problem, we propose a Lyapunov-guided optimization framework that integrates Lyapunov optimization with a multiagent deep reinforcement learning algorithm. Specifically, due to the inability to predict the future state of the system, we employ Lyapunov optimization to transform the long-term objective into a sequence of per-time-slot subproblems. Subsequently, given the high complexity of minimizing the derived Lyapunov drift function directly, we utilize a multiagent deep deterministic policy gradient (MADDPG) algorithm to solve these subproblems. This approach leverages MADDPG's proven capability in handling complex sequential decision-making processes while enabling real-time adaptive optimization in dynamic environments. Extensive simulations demonstrate that the proposed framework achieves significant reduction in DoD, bounded delays, and stable queue dynamics in diverse scenarios, outperforming baseline methods to substantially extend the lifetime of the SMEC service while maintaining the required service quality.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2935.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
