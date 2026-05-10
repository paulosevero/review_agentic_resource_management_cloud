---
id: paper-0812
title: Deep Reinforcement Learning Based Resource Allocation Strategy in Cloud-Edge Computing System
authors:
- Adhoni, Zameer Ahmed
- Habelalmateen, Mohammed I
- Janardhana, D.R.
- Sattar, Khalid Nazim Abdul
- Audah, Lukman
venue: International Conference on Distributed Computing and Optimization Techniques, ICDCOT 2024
venue_type: conference
year: 2024
doi: 10.1109/ICDCOT61034.2024.10515480
url: https://www.scopus.com/pages/publications/85193230753?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- allocation
- cloud-edge resource
- deep reinforcement learning
- resource allocation
- reward
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

# paper-0812 — Deep Reinforcement Learning Based Resource Allocation Strategy in Cloud-Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A lot of real time processing as well as resource-intensive apps is what is needed more and thus, cloud-edge computing systems require compelling resource allocation schemes. This research focuses on the utility of Multiagent Learning framework with Deep Reinforcement Learning (MAL-DRL) which is used for solution deployment concerning resource allocation in such systems, such that the end user enjoys optimization while operators optimize resource utilization. In this work, the research focus on the simulation testing of the MAL-DRL algorithm against classical Random Allocation (RA) and singe agent DRL methods. This exhibition shows that MAL-DRL improves the average latency more (44% savings) and at the same time more resources are used (35% increase) compared both the alternatives with a combined reward measure score of 0.80. These results show that distributed decision-making and learning styles of MAL-DRL brings together faster resource allocation which can be interpreted as a reduction of users' delay experience and therefore lead to better performance of whole system. Although the article limits simulations in areas to be covered and complexity in training, it brings the prospective benefits of MAL-DRL in the management of cloud-edge resources on the spot. In the course of this undertake, the effect of ensuring communication goals, moving learning strategies, and security measures for the ultimate goal of boosting this method's applicability in real-world antics can be explored.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0812.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
