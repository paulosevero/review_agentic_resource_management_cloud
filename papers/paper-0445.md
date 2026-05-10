---
id: paper-0445
title: Optimal resource allocation with deep reinforcement learning and greedy adaptive firefly algorithm in cloud computing
authors:
- Karat, Chitharanjan
- Senthilkumar, Radha
venue: 'Concurrency and Computation: Practice and Experience'
venue_type: journal
year: 2022
doi: 10.1002/cpe.6657
url: https://www.scopus.com/pages/publications/85116034454?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- Bioluminescence
- Cloud computing
- Learning algorithms
- Multi agent systems
- Network security
- Optimization
- Quality of service
- Reinforcement learning
- Resource allocation
- Virtual machine
- Cloud-computing
- Dynamic resource allocations
- Greedy adaptive firefly
- Multi agent
- Optimal resource allocation
- Quality-of-service
- Resource allocation schemes
- Resource allocation techniques
- Resource management techniques
- Resources allocation
- Deep learning
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

# paper-0445 — Optimal resource allocation with deep reinforcement learning and greedy adaptive firefly algorithm in cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The allocation of resources is a foremost demanding task in cloud computing. Scholars are yet finding it difficult to allocate appropriate resources to the set of user tasks. Our objective is to provide a platform that optimizes a dynamic resource allocation scheme. Multi-agent deep reinforcement learning-based greedy adaptive firefly algorithm (MAD-GAF) has been proposed herein includes both the resource management and allocation techniques. This chooses the best Quality of Service (QoS) measured host for a group of tasks efficiently and subsequently minimize the task execution time. The proposed cloud brokering architecture comprises a multi-agent system, the cloud provider and the user. Initially, deep reinforcement learning has been built to recreate the request of cloud customers by forecasting the value of unused resources. Then the recreated customer request is forwarded to the global broker agent, which maps the virtual machine (VM) to the most appropriate cluster of physical machine (PM). The virtual machine monitor (VMM) selects VMs by managing and accessing the physical resources. The global utility agent allocates VMs using the GAF optimization algorithm, which specifies the best QoS measured host to decrease the whole tasks' average response time, thus optimizing resource allocation compared to the current approaches. © 2021 John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0445.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
