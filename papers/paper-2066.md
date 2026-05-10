---
id: paper-2066
title: Reinforcement Learning-Optimized Resource Allocation Framework for Edge Computing
authors:
- Rajyaguru, Mihirharishbhai
- Gupta, Devdas
- Rekha, G. Sunitha
- Manu, Y.M.
- Rakshitha Kiran, P.
- Schhajed, Ajay
venue: Proceedings of 2025 10th International Conference on Science Technology, Engineering and Mathematics, ICONSTEM 2025
venue_type: conference
year: 2025
doi: 10.1109/ICONSTEM65670.2025.11374913
url: https://www.scopus.com/pages/publications/105034463699?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Centralized Training Decentralized Execution
- Distributed Optimization
- Edge Computing
- Multi-Agent Actor-Critic
- Ray RLlib
- Reinforcement Learning
- Resource Allocation
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

# paper-2066 — Reinforcement Learning-Optimized Resource Allocation Framework for Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The research introduces a Reinforcement Learning-Optimized Framework of Resource Allocation in Edge Computing based on the Centralized Training, Decentralized Implementation (CTDE) Multi-Agent Actor-Critic algorithm, which is applied in Ray RLlib with Ray Cluster. The objective of the framework is to optimize dynamic resource distribution among heterogeneous edge nodes and minimize the latency, energy use and communication overheads. The system assumes the efficient coordination and quick adaptation to changing workloads through the employment of centralized critic in case of global policy learning and a decentralized actor in case of local decision-making. Experimental assessments show the proposed model is better than the classic model which is DQN, PPO, and FDRL with significant gains in the reduction of task latency, resource usage and scalability. Much more efficiency in distributed training and robustness in large-scale edge networks is achieved with the integration with Ray Cluster. Altogether, the suggested CTDE framework has the potential to be utilized as a scalable, intelligent, energy-demanding solution to the next-generation edge computing environment. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2066.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
