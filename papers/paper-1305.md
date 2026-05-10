---
id: paper-1305
title: Multiagent Reinforcement Learning Based Distributed Channel Access for Industrial Edge-Cloud Web 3.0
authors:
- Yang, Chen
- Wang, Yushi
- Lan, Shulin
- Zhu, Liehuang
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3377441
url: https://www.scopus.com/pages/publications/85188440003?origin=resultslist
publisher: IEEE Computer Society
pages: 3943--3954
keywords:
- channel access
- edge computing
- edge-cloud collaboration
- multiagent reinforcement learning
- Smart factory
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

# paper-1305 — Multiagent Reinforcement Learning Based Distributed Channel Access for Industrial Edge-Cloud Web 3.0

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the emerging Web 3.0 applications for mass customized and personalized manufacturing, smart mobile resources need to interact with each other and other resources to achieve efficient collaborative manufacturing. Existing wireless communication solutions cannot leverage multiantenna technology and the movement direction of smart mobile resources to meet the high requirements for communication rate and reliability in high-performance manufacturing processes. Therefore, this paper proposes a task-aware distributed channel access scheme for multiantenna smart mobile resources in a factory. First, this paper introduces an edge-cloud collaboration framework for smart factories to support autonomous wireless access point selection for mobile resources. Second, a user-centric active wireless channel access scheme is proposed and a channel resource allocation optimization problem is formulated for mobile resources to leverage multiple antennas and movement direction to address the unstable connection problem. Third, a centralized-training-and-distributed-execution multiagent reinforcement learning (MARL) model with a specially designed neural network architecture is built for smart mobile resources, effectively using important input information of the next interaction objects for mobile resources. Simulation results show that the proposed MARL scheme outperforms common schemes of 3GPP LTE, traditional reinforcement learning schemes, and random selection schemes in improving communication rate and stability.  © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1305.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
