---
id: paper-0577
title: Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning
authors:
- Danino, Tom
- Ben-Shimol, Yehuda
- Greenberg, Shlomo
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12122614
url: https://www.scopus.com/pages/publications/85163810011?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- actor–critic
- cloud computing
- Deep-RL
- Kubernetes
- multi-agent
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

# paper-0577 — Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, many computation tasks are carried out using cloud computing services and virtualization technology. The intensive resource requirements of virtual machines have led to the adoption of a lighter solution based on containers. Containers isolate packaged applications and their dependencies, and they can also operate as part of distributed applications. Containers can be distributed over a cluster of computers with available resources, such as the CPU, memory, and communication bandwidth. Any container distribution mechanism should consider resource availability and their impact on overall performance. This work suggests a new approach to assigning containers to servers in the cloud, while meeting computing and communication resource requirements and minimizing the overall task completion time. We introduce a multi-agent environment using a deep reinforcement learning-based decision mechanism. The high action space complexity is tackled by decentralizing the allocation decisions among multiple agents. Considering the interactions among the agents, we introduce a new cooperative mechanism for a state and reward design, resulting in efficient container assignments. The performances of both long short term memory (LSTM) and memory augmented-based agents are examined, for solving the challenging container assignment problem. Experimental results demonstrated an improvement of up to 28% in the execution runtime compared to existing bin-packing heuristics and the common Kubernetes industrial tool. © 2023 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0577.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
