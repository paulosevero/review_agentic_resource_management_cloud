---
id: paper-2159
title: Dynamic Task Scheduling and Smart Caching in Fog-Cloud Architectures Using Advantage Actor-Critic Agents
authors:
- Solhdar, Mohammad Hassan Nataj
- Esnaashari, Mohamad Mehdi
venue: Proceedings of 2025 9th International Conference on Internet of Things and Applications, IoT 2025
venue_type: conference
year: 2025
doi: 10.1109/IoT69654.2025.11297605
url: https://www.scopus.com/pages/publications/105031371402?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Advantage Actor-Critic (A2C)
- Fog-Cloud Environment
- Reinforcement Learning
- Result Caching
- Task Scheduling
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

# paper-2159 — Dynamic Task Scheduling and Smart Caching in Fog-Cloud Architectures Using Advantage Actor-Critic Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this work, we introduce History-aware Scheduling and Caching with Advantage Actor-Critic (HiSC-A2C), a novel dual-agent reinforcement learning framework designed for efficient task scheduling and intelligent result caching in fog-cloud computing environments. By decoupling the decision processes for task execution and caching, our method leverages two independent Advantage Actor-Critic (A2C) agents: one selects the optimal node for executing each task, while the other determines the most suitable location for caching results, taking into account task frequency, data freshness, and user proximity. This history-aware approach enables the system to adapt dynamically to fluctuating workloads and heterogeneous network conditions, ensuring that frequently requested tasks are cached closer to end users and resources are utilized efficiently. Extensive simulation results demonstrate that HiSCA2C significantly reduces response latency and enhances computational efficiency compared to existing methods, including A3C-R2N2 and DDQN. By integrating historical task data and decoupling scheduling from caching, our framework provides a scalable and robust solution for real-time service delivery in distributed fog-cloud infrastructures.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2159.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
