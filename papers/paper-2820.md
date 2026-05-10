---
id: paper-2820
title: 'Cooperative decision-making of unmanned aerial vehicles: A multi-agent reinforcement learning approach'
authors:
- Wang, Ziyi
- Ma, Guoliang
- Guo, Jian
- Qian, Chen
- Gao, Yang
- Huang, Zhuo
venue: Engineering Applications of Artificial Intelligence
venue_type: journal
year: 2026
doi: 10.1016/j.engappai.2026.113980
url: https://www.scopus.com/pages/publications/105029232099?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Cooperative decision making
- Flexible observation
- Multi-agent reinforcement learning
- Proximal policy optimization
- Unmanned aerial vehicle swarm
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2820 — Cooperative decision-making of unmanned aerial vehicles: A multi-agent reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cooperative decision-making of unmanned aerial vehicles (UAVs) for military missions is a crucial research topic. However, the ability constraints of heterogeneous UAVs in real-world scenarios bring significant challenges to the cooperative decision-making process. To address these issues, this paper proposes a multi-agent proximal policy optimization (MAPPO) algorithm with a flexible observation feature encoding (FOFE) mechanism and a Mamba-based memory structure. Firstly, the cooperative decision-making problem for reconnaissance-strike integrated fixed-wing UAV (RSUAV) swarms is formulated as a distributed partially observable Markov decision process (Dec-POMDP). Secondly, to address the variability and incompleteness in observation inputs, an FOFE strategy is introduced. This allows the network to process multi-channel and variable-length data effectively. Furthermore, the Mamba model is incorporated to capture temporal dependencies in historical observations. This enhances decision-making in prolonged missions. Under this multi-agent reinforcement learning (MARL) framework, each RSUAV can make autonomous decisions in a decentralized manner. The simulation results show that the proposed algorithm improves the completion ratio (>10.1%), survival ratio (>14.8%), and reduces completion time (>21.5%) compared to baselines. It also exhibits strong generalization capability and holds practical feasibility for deployment on edge computing devices. Therefore, this approach enables effective cooperative decision-making under the ability constraints of heterogeneous RSUAVs. Copyright © 2026. Published by Elsevier Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2820.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
