---
id: paper-0553
title: 'FLoadNet: Load Balancing in Fog Networks With Cooperative Multiagent Using Actor-Critic Method'
authors:
- Baek, Jungyeon
- Kaddoum, Georges
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2023
doi: 10.1109/TNSM.2022.3210827
url: https://www.scopus.com/pages/publications/85139447790?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 400--414
keywords:
- actor-critic
- computation offloading
- deep-reinforcement learning
- Fog computing
- load balancing
- multi-agent learning
- SDN
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

# paper-0553 — FLoadNet: Load Balancing in Fog Networks With Cooperative Multiagent Using Actor-Critic Method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growing demands of the Internet of Things (IoT) require a platform that supports real-time interactions and high availability of services to devices. In this context, the fog computing paradigm has emerged as an attractive solution for processing the data of IoT applications. Owing to the unpredictable traffic demands and resource heterogeneity in the fog environment, a smart workload distribution is essential to achieve high resource utilization and computing efficiency. To this end, this paper considers a joint link and server load balancing problem with multiple cooperative access points, (APs), in a combined edge-fog-cloud environment. The joint optimization problem is formulated as a stochastic game, and an actor-critic reinforcement learning framework, called FLoadNet, is proposed to optimize the joint policy of the multi-agents. FLoadNet consists of a centralized critic network, with parameter sharing and distributed individual actor networks in all the APs. Due to the learning dynamics and partially observable environment, we propose an extended critic network model, where cooperative APs learn to communicate among themselves while evaluating the value function. Unlike previous studies, the proposed critic network is designed to train both value and message functions, which is shown to significantly reduce the computational cost. The main goal of this work is to advance the development of efficient edge learning and the application of distributed learning algorithms specifically to fog network load balancing. The experimental results show that FLoadNet outperforms baseline load balancing methods.  © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0553.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
