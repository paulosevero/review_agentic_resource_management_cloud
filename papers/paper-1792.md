---
id: paper-1792
title: Edge Computing Task Offloading Algorithm Based on Distributed Multi-Agent Deep Reinforcement Learning
authors:
- Li, Hui
- Zhu, Zhilong
- Li, Yingying
- Huang, Wanwei
- Wang, Zhiheng
venue: Electronics (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/electronics14204063
url: https://www.scopus.com/pages/publications/105020238025?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- distributed multi-agent deep q-network
- edge computing
- low-Earth-orbit satellite network
- resource allocation
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

# paper-1792 — Edge Computing Task Offloading Algorithm Based on Distributed Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As an important supplement to ground computing, edge computing can effectively alleviate the computational burden on ground systems. In the context of integrating edge computing with low-Earth-orbit satellite networks, this paper proposes an edge computing task offloading algorithm based on distributed multi-agent deep reinforcement learning (DMADRL) to address the challenges of task offloading, including low transmission rates, low task completion rates, and high latency. Firstly, a Ground–UAV–LEO (GUL) three-layer architecture is constructed to improve offloading transmission rate. Secondly, the task offloading problem is decomposed into two sub-problems: offloading decisions and resource allocation. The former is addressed using a distributed multi-agent deep Q-network, where the problem is formulated as a Markov decision process. The Q-value estimation is iteratively optimized through the online and target networks, enabling the agent to make autonomous decisions based on ground and satellite load conditions, utilize the experience replay buffer to store samples, and achieve global optimization via global reward feedback. The latter employs the gradient descent method to dynamically update the allocation strategy based on the accumulated task data volume and the remaining resources, while adjusting the allocation through iterative convergence error feedback. Simulation results demonstrate that the proposed algorithm increases the average transmission rate by 21.7%, enhances the average task completion rate by at least 22.63% compared with benchmark algorithms, and reduces the average task processing latency by at least 11.32%, thereby significantly improving overall system performance. © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1792.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
