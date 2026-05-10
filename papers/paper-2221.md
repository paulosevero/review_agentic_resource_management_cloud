---
id: paper-2221
title: Task offloading of IOT device in fog-enabled architecture using deep reinforcement learning approach
authors:
- Tomar, Abhinav
- Sharma, Megha
- Agarwal, Ashwarya
- Jha, Aditya Nath
- Jaiswal, Jai
venue: Pervasive and Mobile Computing
venue_type: journal
year: 2025
doi: 10.1016/j.pmcj.2025.102067
url: https://www.scopus.com/pages/publications/105006998655?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Energy efficiency
- Fog computing
- Multi-agent systems
- Quality of Service
- Reinforcement Learning
- Task offloading
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

# paper-2221 — Task offloading of IOT device in fog-enabled architecture using deep reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of IoT devices has strained traditional cloud-centric architectures, revealing limitations in latency, bandwidth, and reliability. Fog computing addresses these issues by decentralizing resources closer to data sources, but task offloading and resource allocation remain challenging due to dynamic workloads, heterogeneous resources, and strict QoS requirements. This study models task offloading as a multi-objective optimization problem, considering task priority, energy efficiency, latency, and deadlines. Using a Markov Decision Process (MDP), it applies three Deep Reinforcement Learning (DRL) algorithms — DQN, DDPG, and SAC — in a multi-agent fog computing setup. Unlike prior work focused on single-agent or isolated metrics, this approach captures inter-node dependencies to improve overall resource use. Simulations show SAC achieves a 97.3% task deadline success rate and improves resource efficiency by 10.1%, highlighting its effectiveness in managing dynamic fog environments. These results advance scalable, adaptive offloading strategies for future IoT systems. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2221.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
