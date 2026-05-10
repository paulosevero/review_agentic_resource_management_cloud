---
id: paper-1979
title: 'Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks'
authors:
- Nagabushnam, Ganesan
- Kim, Kyong Hoon
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-025-05435-5
url: https://www.scopus.com/pages/publications/105008077643?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Aperiodic
- Asynchronous advantage actor-critic
- Cloud
- Deadline task
- Deep multi-agent reinforcement learning
- Heterogeneous fog
- IoT
- Task scheduling
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

# paper-1979 — Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing has become essential for real-time applications in domains such as autonomous driving, smart cities, Industry 4.0, and large-scale IoT ecosystems, where low latency and efficient resource utilization are critical. However, scheduling aperiodic tasks in fog environments remains a significant challenge, particularly when ensuring strict deadline adherence, energy efficiency, and optimized use of heterogeneous low-power devices. This challenge is further intensified by the dynamic and unpredictable nature of fog networks, making the problem NP-hard. To address these issues, we propose FADDEER (fog adaptive deadline-driven energy efficient reinforcement), a novel deep multi-agent reinforcement learning (Deep MARL)-based scheduling algorithm that integrates earliest deadline first (EDF) and asynchronous advantage actor-critic (A3C) to enable adaptive, scalable, and deadline-aware task scheduling. FADDEER intelligently allocates aperiodic tasks to distributed fog nodes, dynamically balancing task makespan, energy consumption, and resource utilization. Experiments were conducted using the COSCO simulation framework with workloads ranging from 100 to 1,000 aperiodic tasks distributed across fog networks of 10 to 100 nodes, respectively. The results demonstrate that FADDEER consistently outperforms state-of-the-art algorithms, including A3C, multi-agent deep deterministic policy gradient (MADDPG), genetic algorithm, particle swarm optimization (PSO), EDF achieving up to 4% higher deadline adherence and up to 55% lower energy consumption compared to the next best alternatives. Moreover, FADDEER achieved up to 19.4% lower makespan under high task loads and significantly reduced scheduling time, validating its efficiency and responsiveness in dynamic fog environments. These outcomes highlight FADDEER’s robustness, scalability, and effectiveness for real-time IoT task scheduling in fog computing frameworks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1979.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
