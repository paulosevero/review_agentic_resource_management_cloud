---
id: paper-2526
title: Cooperative Multi-Agent Deep Reinforcement Learning for Service-Aware Energy Optimization at the Network Edge
authors:
- Chari, Shreya K.
- Vardakas, John S.
- Ramantas, Kostas
- Verikoukis, Christos
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3633581
url: https://www.scopus.com/pages/publications/105022778935?origin=resultslist
publisher: IEEE Computer Society
pages: 4124--4137
keywords:
- energy management
- multi- access edge computing (MEC)
- Multi-agent deep reinforcement learning (MADRL)
- resource orchestration
- sustainable technologies
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2526 — Cooperative Multi-Agent Deep Reinforcement Learning for Service-Aware Energy Optimization at the Network Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Colossal expansion of network services has increased the need for faster and efficient allocation of network resources to user applications. Moving forward, the energy generated at the network edge will impact the offloading of tasks. A Multi-access Edge Computing (MEC) unit now faces the challenging task of optimizing the network resource orchestration while maintaining sustainable energy emissions. In this paper, an application-aware cooperative Multi-Agent Deep Reinforcement Learning (MADRL) algorithm is proposed to mitigate the problem of energy and delay management at the MEC. Each agent within the system uses the Soft-Actor Critic (SAC) as the learning policy while maintaining an overall approach of centralized training and decentralized execution. Network delay and energy consumption using CPU and memory resources in the MEC are used as performance indicators. The performance of the MADRL algorithm is measured against that of a single-agent Actor-Critic (AC) algorithm, Multi-Agent Proximal Policy Optimization (MAPPO) and Monte-Carlo Simulations (MCS). The results illustrate a significantly finer performance by the proposed MADRL algorithm leading to reduced energy consumption and lower delay values. Further, the need for application-aware resource management for green computing in rapidly expandable networks in the future is established. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2526.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
