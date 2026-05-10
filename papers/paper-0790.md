---
id: paper-0790
title: 'Joint Energy and Workload Scheduling for Fog-Assisted Multimicrogrid Systems: A Deep Reinforcement Learning Approach'
authors:
- Zhang, Tingjun
- Yue, Dong
- Yu, Liang
- Dou, Chunxia
- Xie, Xiangpeng
venue: IEEE Systems Journal
venue_type: journal
year: 2023
doi: 10.1109/JSYST.2022.3171534
url: https://www.scopus.com/pages/publications/85130498873?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 164--175
keywords:
- Deep reinforcement learning
- energy management
- fog-assisted
- Markov game
- multimicrogrid
- operating cost
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0790 — Joint Energy and Workload Scheduling for Fog-Assisted Multimicrogrid Systems: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the fluctuation of renewable energy, the uncertainty of electrical loads, and the complexity of networked microgrids, it is challenging to dispatch multiple resources to minimize the operating cost of multi-microgrid system (MMGS). In this article, a fog-assisted operating cost minimization problem of MMGS is investigated with the consideration of source-grid-load-storage-computing coordination. Since there are strong couplings among multiple resources, it is difficult to solve the problem directly. Therefore, the above problem is reformulated as a Markov game. Then, a novel energy management algorithm is proposed to solve Markov game based on multiagent deep reinforcement learning. It is worth mentioning that the proposed energy management algorithm can support local real-time decisions for each microgrid without knowing any prior knowledge of uncertain parameters and private information of other microgrids. Simulation results indicate that the proposed algorithm can reduce the long-term cost of each microgrid by 0.09%-8.02% compared with baselines.  © 2007-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0790.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
