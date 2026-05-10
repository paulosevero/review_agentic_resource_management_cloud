---
id: paper-0391
title: Hybrid Decision Based Multi-Agent Deep Reinforcement learning for Task Offloading in Collaborative Edge-Cloud Computing
authors:
- Chen, Juan
- Wu, Zongling
- Wu, Lei
- Xia, Yunni
- Wang, Yang
- Xiong, Ling
- Shi, Canghong
venue: Proceedings - 24th IEEE International Conference on High Performance Computing and Communications, 8th IEEE International Conference on Data Science and Systems, 20th IEEE International Conference
  on Smart City and 8th IEEE International Conference on Dependability in Sensor, Cloud and Big Data Systems and Application, HPCC/DSS/SmartCity/DependSys 2022
venue_type: conference
year: 2022
doi: 10.1109/HPCC-DSS-SmartCity-DependSys57074.2022.00062
url: https://www.scopus.com/pages/publications/85152231984?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 228--235
keywords:
- deep reinforcement learning
- edge-cloud computing
- hybrid decision
- task offloading
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

# paper-0391 — Hybrid Decision Based Multi-Agent Deep Reinforcement learning for Task Offloading in Collaborative Edge-Cloud Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To support computing-intensive and latency-sensitive Internet-of-Things (IoT) applications, we establish a three-layer collaborative edge-cloud computing network, in which multiple IoT devices, edge servers and cloud servers are allocated at IoT layer, edge layer and cloud layer, respectively.However, it is still challenging to satisfy the service requests with inevitable resource competition among task offloading. To solve the joint computation offloading and resource allocation problem, we formulate it as a multi-agent Markov decision process (MAMDP), where action space of each agent contains discrete-continuous hybrid decision. Firstly, we relax the discrete action to a continuous set by developing a probabilistic method. Then, by taking advantage of a continuous action based centralized training and distributed execution strategy, a cooperative multi-agent deep reinforcement learning (MADRL) based framework with each IoT device acts as an agent is established. The objective function is to minimize the total system cost in terms of the energy consumption of IoT device and the renting charge of edge/cloud servers. The simulation results demonstrate the advantageous of the proposed MADRL over the three state-of-the-art DRL based agents in reducing the system cost.  © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0391.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
