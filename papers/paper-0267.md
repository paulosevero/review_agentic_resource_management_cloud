---
id: paper-0267
title: 'Reliability-aware: Task scheduling in cloud computing using multi-agent reinforcement learning algorithm and neural fitted q'
authors:
- Balla, Husamelddin
- Sheng, Chen
- Weipeng, Jing
venue: International Arab Journal of Information Technology
venue_type: journal
year: 2021
doi: 10.34028/iajit/18/1/5
url: https://www.scopus.com/pages/publications/85098751900?origin=resultslist
publisher: Zarka Private University
pages: 36--47
keywords:
- Cloud computing
- Multi-agent scheduler
- Neural fitted Q
- Queuing theory
- Reinforcement learning
- Reliability
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

# paper-0267 — Reliability-aware: Task scheduling in cloud computing using multi-agent reinforcement learning algorithm and neural fitted q

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing becomes the basic alternative platform for the most users application in the recent years. The complexity increasing in cloud environment due to the continuous development of resources and applications needs a concentrated integrated fault tolerance approach to provide the quality of service. Focusing on reliability enhancement in an environment with dynamic changes such as cloud environment, we developed a multi-agent scheduler using Reinforcement Learning (RL) algorithm and Neural Fitted Q (NFQ) to effectively schedule the user requests. Our approach considers the queue buffer size for each resource by implementing the queue theory to design a queue model in a way that each scheduler agent has its own queue which receives the user requests from the global queue. A central learning agent responsible of learning the output of the scheduler agents and direct those scheduler agents through the feedback claimed from the previous step. The dynamicity problem in cloud environment is managed in our system by employing neural network which supports the reinforcement learning algorithm through a specified function. The numerical result demonstrated an efficiency of our proposed approach and enhanced the reliability. © 2021, Zarka Private University. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0267.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
