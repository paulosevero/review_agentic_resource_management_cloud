---
id: paper-0537
title: Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing
authors:
- Zhao, Nan
- Ye, Zhiyang
- Pei, Yiyang
- Liang, Ying-Chang
- Niyato, Dusit
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2022
doi: 10.1109/TWC.2022.3153316
url: https://www.scopus.com/pages/publications/85125735198?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6949--6960
keywords:
- cooperative offloading
- deep reinforcement learning
- Mobile edge computing
- task offloading
- UAV networks
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

# paper-0537 — Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing can effectively reduce service latency and improve service quality by offloading computation-intensive tasks to the edges of wireless networks. Due to the characteristic of flexible deployment, wide coverage and reliable wireless communication, unmanned aerial vehicles (UAVs) have been employed as assisted edge clouds (ECs) for large-scale sparely-distributed user equipment. Considering the limited computation and energy capacities of UAVs, a collaborative mobile edge computing system with multiple UAVs and multiple ECs is investigated in this paper. The task offloading issue is addressed to minimize the sum of execution delays and energy consumptions by jointly designing the trajectories, computation task allocation, and communication resource management of UAVs. Moreover, to solve the above non-convex optimization problem, a Markov decision process is formulated for the multi-UAV assisted mobile edge computing system. To obtain the joint strategy of trajectory design, task allocation, and power management, a cooperative multi-agent deep reinforcement learning framework is investigated. Considering the high-dimensional continuous action space, the twin delayed deep deterministic policy gradient algorithm is exploited. The evaluation results demonstrate that our multi-UAV multi-EC task offloading method can achieve better performance compared with the other optimization approaches.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0537.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
