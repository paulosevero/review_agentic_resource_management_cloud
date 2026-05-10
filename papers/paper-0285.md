---
id: paper-0285
title: Graph Convolutional Reinforcement Learning for Dependent Task Allocation in Edge Computing
authors:
- Ding, Shiyao
- Lin, Donghui
- Zhou, Xin
venue: Proceedings - 2021 IEEE International Conference on Agents, ICA 2021
venue_type: conference
year: 2021
doi: 10.1109/ICA54137.2021.00011
url: https://www.scopus.com/pages/publications/85127658584?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 25--30
keywords:
- Deep reinforcement learning
- Dependent task allocation
- Edge computing
- Graph neural network
- Intelligent agent
- Internet of Things (IoT)
- Markov decision process
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

# paper-0285 — Graph Convolutional Reinforcement Learning for Dependent Task Allocation in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In edge computing, an important problem is how to allocate dependent tasks to resource-limited edge servers, where some tasks can only be performed after accomplishing some other tasks. Most related studies assume that server status remains unchanged, which might be invalid in some real-world scenarios. Thus, this paper studies the new problem of how to dynamically allocate dependent tasks in resource-limited edge computing. This problem poses two challenges: 1) how to cope with dynamic changes in server status and task arrival, and 2) how to handle the dependency information for decisionmaking in task allocation. Our solution is a graph convolutional reinforcement learning-based task-Allocation agent consisting of an encoding part and a decision-making part. The encoding part represents the dependent tasks as directed acyclic graphs and employs a graph convolutional network (GCN) to embed the dependency information of the tasks. It can effectively deal with the dependency and so permit decision-making. The decision-making part formulates the task allocation problem as a Markov decision process to cope with the dynamic changes. Specially, the agent employs deep reinforcement learning to achieve dynamic decision-making for task allocation with the target of optimizing some metric (e.g., minimizing delay costs and energy cost). Experiments verify that our algorithm offers significantly better performance than the existing algorithms examined.  © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0285.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
