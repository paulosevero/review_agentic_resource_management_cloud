---
id: paper-0531
title: Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms
authors:
- Zafeiropoulos, Anastasios
- Fotopoulou, Eleni
- Filinis, Nikos
- Papavassiliou, Symeon
venue: Simulation Modelling Practice and Theory
venue_type: journal
year: 2022
doi: 10.1016/j.simpat.2021.102461
url: https://www.scopus.com/pages/publications/85122667567?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Autoscaling
- Intelligent orchestration
- Reinforcement learning
- Serverless application
- Serverless computing
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

# paper-0531 — Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing is emerging as a cloud computing paradigm that provisions computing resources on demand, while billing is taking place based on the exact usage of the cloud resources. The responsibility for infrastructure management is undertaken by cloud providers, enabling developers to focus on the development of the business logic of their applications. For managing scalability, various autoscaling mechanisms have been proposed that try to optimize the provisioning of resources based on the posed workload. These mechanisms are configured and managed by the cloud provider, imposing non negligible administration overhead. A set of challenges are identified for introducing automation and optimizing the provisioning of resources, while in parallel respecting the agreed Service Level Agreement between cloud and application providers. To address these challenges, we have developed autoscaling mechanisms for serverless applications that are powered by Reinforcement Learning (RL) techniques. A set of RL environments and agents have been implemented (based on Q-learning, DynaQ+ and Deep Q-learning algorithms) for driving autoscaling mechanisms, able to autonomously manage dynamic workloads with Quality of Service (QoS) guarantees, while opting for efficient usage of resources. The produced environments and agents are evaluated in real and simulated environments, taking advantage of the Kubeless open-source serverless platform. The evaluation results validate the suitability of the proposed mechanisms to efficiently tackle scalability management for serverless applications. © 2022 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0531.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
