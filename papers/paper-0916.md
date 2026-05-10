---
id: paper-0916
title: 'Reinforcement Learning for Resource Allocation in Edge Computing: Challenges and Future Directions'
authors:
- Ganesh, Devalla Bhaskar
- Nilesh, Dokuparthi
- Sai Tarun Reddy, Chittela Venkata
- Reddy, Jonnala HarshaVardhan
- Gangashetty, Suryakanth V
- Vurukonda, Naresh
venue: 5th International Conference on Sustainable Communication Networks and Application, ICSCNA 2024 - Proceedings
venue_type: conference
year: 2024
doi: 10.1109/ICSCNA63714.2024.10864001
url: https://www.scopus.com/pages/publications/85219613240?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 930--936
keywords:
- Dynamic Resource Management
- Edge Computing
- Multi-Agent Systems
- Reinforcement Learning
- Resource Allocation
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

# paper-0916 — Reinforcement Learning for Resource Allocation in Edge Computing: Challenges and Future Directions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Real time IoT and 5G applications are dependent on edge computing to reduce latency and increase Bandwidth efficiency. The main challenge for one of them is dynamic resource allocation, like CPU and band width, that traditional methods cannot cope with. Adaptive, real time resource management in dynamic edge environments can be achieved with reinforcement learning (RL). The resource allocation in edge computing based on resource type, application domain, and algorithm is reviewed in this survey using the perspective of using RL in the area. This presents discussion of the performance, advantages, and limitations of these methods, as well as key challenges such as scalability, training overhead, and real time decision making. Also, it explores the use of emerging techniques, namely multia agent RL and hybrid models. Finally, future research directions include the usage of transfer learning, energy efficient RL Models and deployment of RL in real world scenario in edge computing environments. It turns out to be a guide to the improvement of subsequent RL approaches for resource management. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0916.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
