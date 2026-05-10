---
id: paper-0337
title: Multi-agent reinforcement learning for intelligent resource allocation in IIoT networks
authors:
- Rosenberger, Julia
- Urlaub, Michael
- Schramm, Dieter
venue: 2021 IEEE Global Conference on Artificial Intelligence and Internet of Things, GCAIoT 2021
venue_type: conference
year: 2021
doi: 10.1109/GCAIoT53516.2021.9692913
url: https://www.scopus.com/pages/publications/85126761659?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 118--119
keywords:
- deep reinforcement learning
- industrial internet of things
- load balancing
- multi-agent-system
- resource allocation
- streaming data
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0337 — Multi-agent reinforcement learning for intelligent resource allocation in IIoT networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the industrial Internet of Things (IIoT), a high number of devices with limited resources, like computational power, memory, bandwidth and, in case of wireless sensor networks, also energy, communicate. At the same time, the amount of data as well as the demand for data processing in the edge is rapidly increasing. To enable Industry 4.0 (I4.0) and the IIoT, an intelligent resource allocation is required to make optimal use of the available resources. For this purpose, a multi-agent system (MAS) based on deep reinforcement learning (DRL) is proposed. Multi-agent reinforcement learning (MARL) is already taken into account in different communication networks, e.g. for intelligent routing. Despite its great potential, little attention is paid to these methods in industry so far. In this work, DRL is applied for resource allocation and load balancing for industrial edge computing. An optimal usage of the available resources of the IIoT devices should be achieved. Due to the structure of IIoT systems as well as for security reasons, a MAS is preferred for decentralized decision making. In subsequent steps, it is planned to add and remove devices during runtime, to change the number of tasks to be executed as well as evaluations on single- and multi-policy-approaches. The following aspects will be considered for evaluation: (1) improvement of the resource usage of the devices and (2) overhead due to the MAS. © 2021 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0337.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
