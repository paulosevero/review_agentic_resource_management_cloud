---
id: paper-0652
title: Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning
authors:
- Lin, Shaofu
- Chen, Yingying
- Li, Shuopeng
venue: Sensors
venue_type: journal
year: 2023
doi: 10.3390/s23239541
url: https://www.scopus.com/pages/publications/85178943481?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- mobile edge computing (MEC)
- multi-agent deep reinforcement learning (MADRL)
- multi-objective optimization (MOO)
- unmanned aerial vehicle (UAV)
- wireless power transfer (WPT)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-0652 — Multi-Objective Optimization in Air-to-Air Communication System Based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advantages of real-time data processing and flexible deployment, unmanned aerial vehicle (UAV)-assisted mobile edge computing systems are widely used in both civil and military fields. However, due to limited energy, it is usually difficult for UAVs to stay in the air for long periods and to perform computational tasks. In this paper, we propose a full-duplex air-to-air communication system (A2ACS) model combining mobile edge computing and wireless power transfer technologies, aiming to effectively reduce the computational latency and energy consumption of UAVs, while ensuring that the UAVs do not interrupt the mission or leave the work area due to insufficient energy. In this system, UAVs collect energy from external air-edge energy servers (AEESs) to power onboard batteries and offload computational tasks to AEESs to reduce latency. To optimize the system’s performance and balance the four objectives, including the system throughput, the number of low-power alarms of UAVs, the total energy received by UAVs and the energy consumption of AEESs, we develop a multi-objective optimization framework. Considering that AEESs require rapid decision-making in a dynamic environment, an algorithm based on multi-agent deep deterministic policy gradient (MADDPG) is proposed, to optimize the AEESs’ service location and to control the power of energy transfer. While training, the agents learn the optimal policy given the optimization weight conditions. Furthermore, we adopt the K-means algorithm to determine the association between AEESs and UAVs to ensure fairness. Simulated experiment results show that the proposed MODDPG (multi-objective DDPG) algorithm has better performance than the baseline algorithms, such as the genetic algorithm and other deep reinforcement learning algorithms. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0652.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
