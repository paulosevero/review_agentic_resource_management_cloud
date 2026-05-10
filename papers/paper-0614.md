---
id: paper-0614
title: QoS-Aware Task Offloading in Fog Environment Using Multi-agent Deep Reinforcement Learning
authors:
- Jain, Vibha
- Kumar, Bijendra
venue: Journal of Network and Systems Management
venue_type: journal
year: 2023
doi: 10.1007/s10922-022-09696-y
url: https://www.scopus.com/pages/publications/85139713952?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Multi-level feedback queue
- Quality of Service
- Resource allocation
- Task priority
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

# paper-0614 — QoS-Aware Task Offloading in Fog Environment Using Multi-agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the surge of intelligent devices, applications of Internet of Things (IoT) are growing at a rapid pace. As a result, a massive amount of raw data is generated, which must be processed and stored. IoT devices standalone are not enough to handle large amount of data. Hence, to improve the performance, users started to push some jobs to far-situated cloud data centers, which would lead to more complications such as high bandwidth usage, service latency, and energy consumption. Fog computing emerges as a key enabling technology that brings cloud services closer to the end-user. However, owing to the unpredictability of tasks and Quality of Service (QoS) requirements of users, efficient task scheduling and resource allocation mechanisms are needed to balance the demand. To handle the problem efficiently, we have designed the task offloading problem as Markov Decision Process (MDP) by considering various user QoS factors including end-to-end latency, energy consumption, task deadline, and priority. Three different model-free off-policy Deep Reinforcement Learning (DRL) based solutions are outlined to maximize the reward in terms of resource utilization. Finally, extensive experimentation is conducted to validate and compare the efficiency and effectiveness of proposed mechanisms. Results show that with the proposed method, on average 96.23% of tasks can satisfy the deadline with an 8.25% increase. © 2022, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0614.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
