---
id: paper-0178
title: A cloud resource management framework for multiple online scientific workflows using cooperative reinforcement learning agents
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
- Yaghmaee, Farzin
venue: Computer Networks
venue_type: journal
year: 2020
doi: 10.1016/j.comnet.2020.107340
url: https://www.scopus.com/pages/publications/85086700229?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cloud computing
- Cooperative agents
- Dependent tasks
- Markov game
- Reinforcement learning
- Resource management
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

# paper-0178 — A cloud resource management framework for multiple online scientific workflows using cooperative reinforcement learning agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud is a common distributed environment to share strong and available resources to increase the efficiency of complex and heavy calculations. In return for the cost paid by cloud users, a variety of services have been provided for them, the quality of which has been guaranteed and the reliability of their corresponding resources have been supplied by cloud service providers. Due to the heterogeneity of resources and their several shared applications, efficient scheduling can increase the productivity of cloud resources. This will reduce users’ costs and energy consumption, considering the quality of service provided for them. Cloud resource management can be conducted to obtain several objectives. Reducing user costs, reducing energy consumption, load balancing of resources, enhancing utilization of resources, and improving availability and security are some of the key objectives in this area. Several methods have been proposed for cloud resource management, most of which are focused on one or more aspects of these objectives of cloud computing. This paper introduces a new framework consisting of multiple cooperative agents, in which, all phases of the task scheduling and resource provisioning is considered and the quality of service provided to the user is controlled. The proposed integrated model provides all task scheduling and resource provisioning processes, and its various parts serve the management of user applications and more efficient use of cloud resources. This framework works well on dependent simultaneous tasks, which have a complicated process of scheduling because of the dependence of its sub-tasks. The results of the experiments show the better performance of the proposed model in comparison with other cloud resource management methods. © 2020 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0178.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
