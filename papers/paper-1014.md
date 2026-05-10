---
id: paper-1014
title: Cost-AoI Aware Task Scheduling in Industrial IOT Based on Serverless Edge Computing
authors:
- Li, Mingchu
- Wang, Zhihua
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2024
doi: 10.1109/WCNC57260.2024.10570806
url: https://www.scopus.com/pages/publications/85198855028?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- edge computing
- Industrial IoT
- serverless computing
- task schedule
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1014 — Cost-AoI Aware Task Scheduling in Industrial IOT Based on Serverless Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wireless Industrial IoT plays a crucial role in smart factories, where many sensors are rapidly generating task requests scheduled for timely responses. Maintaining information freshness is necessary but challenging. Edge networks that combine emerging serverless feathers can enable significant improvements in development efficiency and more flexible adaptation to workloads. However, the cost of scheduling cannot be ignored. Most of the present work in serverless edge computing does not consider the impact of the age of information (AoI) and cost in task scheduling. In this paper, we consider the relationship between AoI in users and cost in service providers in practical scenarios. We model the task scheduling problem in a serverless edge computing scenario as a Markov Decision Process (MDP) and consider multi-hop forwarding task scheduling with guaranteed AoI and costs under different pressures of workloads. To solve the highly dynamic problem, we design a multi-agent deep reinforcement learning algorithm based on Proximal Policy Optimization (PPO), validate it on real datasets, and experiments show that our algorithm reduces 10% cost in low workload and up to 16% AoI in the high workload situation.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1014.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
