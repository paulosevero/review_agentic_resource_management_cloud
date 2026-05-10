---
id: paper-1254
title: Modeling on Resource Allocation for Age-Sensitive Mobile-Edge Computing Using Federated Multiagent Reinforcement Learning
authors:
- Wang, Cong
- Yao, Tianye
- Fan, Tingshan
- Peng, Sancheng
- Xu, Changming
- Yu, Shui
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3294535
url: https://www.scopus.com/pages/publications/85164686560?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3121--3131
keywords:
- Federated learning (FL)
- mobile-edge computing (MEC)
- multiagent deep reinforcement learning (MARL)
- resource allocation
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

# paper-1254 — Modeling on Resource Allocation for Age-Sensitive Mobile-Edge Computing Using Federated Multiagent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Existing mobile-edge computing (MEC) systems are facing the challenges of limited resources and highly dynamic network environments. How to allocate resources to maintain the efficiency and timeliness of data and tasks is still an open issue. To address this problem, we propose a novel framework for unmanned aerial vehicle-Assisted MEC systems using federated multiagent reinforcement learning (RL). First, we formulate a joint optimization problem as a multiagent Markov decision process by jointly minimizing the average age of information and maximizing the number of recent tasks. Second, we design a novel scheduling algorithm for online collaborative resources by adopting multiple agents to learn and make decisions in accordance with the overall interests through federal learning. Finally, an experience replay mechanism for the internal experience pool is introduced to further improve learning efficiency. Experimental results show that our proposed algorithm is superior to the recent typical RL-based algorithms. It not only has higher efficiency in task processing and data freshness but also has more stable performance and adaptability across diverse experimental conditions.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1254.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
