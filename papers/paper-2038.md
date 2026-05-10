---
id: paper-2038
title: Multi-Agent Reinforcement Learning for Workload Distribution in FaaS-Edge Computing Systems
authors:
- Petriglia, Emanuele
- Filippini, Federica
- Ciavotta, Michele
- Savi, Marco
venue: Proceedings - 2025 IEEE International Parallel and Distributed Processing Symposium Workshops, IPDPSW 2025
venue_type: conference
year: 2025
doi: 10.1109/IPDPSW66978.2025.00176
url: https://www.scopus.com/pages/publications/105015492477?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1128--1131
keywords:
- Edge Computing
- Function as a Service
- Load Balancing
- Reinforcement Learning
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

# paper-2038 — Multi-Agent Reinforcement Learning for Workload Distribution in FaaS-Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge Computing has emerged as a response to the growing adoption of the Internet of Things, reducing latency and enabling real-time data processing by shifting computation from centralized cloud servers to the network edge. Adopting the Function-as-a-Service model at edge nodes would further increase flexibility and cost-efficiency, but comes with several challenges related to resource constraints and unpredictable traffic patterns. In addition, efficient task offloading approaches are critical in distributed edge environments. Reinforcement Learning (RL) can be beneficial in this context, outperforming traditional heuristic methods due to its ability to dynamically optimize workload distribution. In this preliminary study, we investigate the potential of multi-agent RL for workload management in federated FaaS-Edge environments. By comparing the widely-used Proximal Policy Optimization (PPO) and Soft Actor-Critic RL methods with two heuristic baselines, we highlight how PPO holds promise in increasing the processed load by exploiting requests forwarding to neighboring nodes.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2038.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
