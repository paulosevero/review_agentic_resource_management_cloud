---
id: paper-0363
title: Collaborative Edge and Cloud Offloading for Internet of Vehicles Using Multi-Agent Reinforcement Learning
authors:
- Ye, Peiwen
- Jia, Xiangdong
- Yang, Xiaorong
- Niu, Chunyu
venue: Jisuanji Gongcheng/Computer Engineering
venue_type: journal
year: 2021
doi: 10.19678/j.issn.1000-3428.0058323
url: https://www.scopus.com/pages/publications/85133160367?origin=resultslist
publisher: Editorial Office of Computer Engineering
pages: 13--20
keywords:
- Collaborative edge and cloud computing
- Internet of Vehicles (IoV)
- Multi-agent reinforcement learning
- Resource allocation
- Stochastic geometry theory
- Task offloading strategy
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

# paper-0363 — Collaborative Edge and Cloud Offloading for Internet of Vehicles Using Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing for Internet of Vehicles (IoV) is key to realizing highly reliable and low-latency IoV systems. However, existing methods generally have the problems of scene convergence and system modeling limitations, and are faced with complex training processes and disaster maintenance risks.By combining the cloud computing technology, this paper proposes a collaborative edge and cloud offloading scheme based on multi-agent reinforcement learning.The strategy uses the stochastic geometry theory to calculate the coverage probability of the offloading nodes and pre-match the vehicular nodes to offloading objects.On this basis, the linear Q function decomposition method is used to reflect the mapping relationship between each agent’s multi-utility factor and task decision.Then through the collaborative cloud and edge computing mech anism, each agent’s decision records are uploaded to the cloud as experience, and the more comprehensively trained neural network is returned to the edge nodes.The results of simulation show that the proposed scheme outperforms the computing strategies using only fixed edge servers in terms of power consumption and latency.The method reduces the algorithm complexity, and can significantly improve the collaborative edge and cloud offloading ability to realize highly reliable and low-latency task offloading. © 2021, Editorial Office of Computer Engineering. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0363.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
