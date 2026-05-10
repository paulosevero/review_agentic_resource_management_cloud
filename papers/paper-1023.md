---
id: paper-1023
title: Edge server deployment strategy based on multi-agent reinforcement learning in the internet of vehicles; [车联网中基于多智能体强化学习的边缘服务器选址策略]
authors:
- Li, Chuang
- Ji, Jianqiao
- Hu, Zhigang
- Zhou, Zhou
venue: Zhongnan Daxue Xuebao (Ziran Kexue Ban)/Journal of Central South University (Science and Technology)
venue_type: journal
year: 2024
doi: 10.11817/j.issn.1672-7207.2024.07.011
url: https://www.scopus.com/pages/publications/85200632329?origin=resultslist
publisher: Central South University of Technology
pages: 2567--2577
keywords:
- edge computing
- load balancing
- reinforcement learning
- server deployment
- vehicle networking
language: Chinese
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

# paper-1023 — Edge server deployment strategy based on multi-agent reinforcement learning in the internet of vehicles; [车联网中基于多智能体强化学习的边缘服务器选址策略]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To solve the hard problem of edge server deployment in internet of vehicle environments, an edge server deployment strategy based on multi-agent reinforcement learning(CKM−MAPPO) was proposed. It focuses on optimizing the load balancing among edge servers and minimizing edge servers' delay and energy consumption. Firstly, the Canopy and K−means algorithms were used to determine the number and initial location of edge server deployment. Then, the multi-agent reinforcement learning algorithm was leveraged to determine the optimal deployment location of the edge server. Finally, the accuracy and effectiveness of the proposed algorithm were evaluated through a series of experiments. The results show that compared with the benchmark algorithm, the proposed method improves load balancing by 26.5%, and the time delay and energy consumption are reduced by 12.4% and 17.9%, respectively. © 2024 Central South University of Technology. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1023.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
