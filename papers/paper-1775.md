---
id: paper-1775
title: A Multi-Agent Deep Reinforcement Learning Algorithm for Task Offloading in Future 6G V2X Network
authors:
- Li, Jiakun
- Li, Jiajian
- Shi, Yanjun
- Lian, Hui
- Wu, Haifan
venue: IEICE Transactions on Information and Systems
venue_type: journal
year: 2025
doi: 10.1587/transinf.2024IIP0005
url: https://www.scopus.com/pages/publications/105009870035?origin=resultslist
publisher: Institute of Electronics Information Communication Engineers
pages: 697--708
keywords:
- cloud-edge-vehicle system
- mobile edge computing
- multi-agent deep reinforcement learning
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1775 — A Multi-Agent Deep Reinforcement Learning Algorithm for Task Offloading in Future 6G V2X Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In future 6G Vehicle-to-Everything (V2X) Network, task offloading of mobile edge computing (MEC) systems will face complex challenges in high mobility, dynamic environment. We herein propose a Multi-Agent Deep Reinforcement Learning algorithm (MADRL) with cloud-edge-vehicle collaborations to address these challenges. Firstly, we build the model of the task offloading problem in the cloud-edge-vehicle system, which meets low-latency, low-energy computing requirements by coordinating the computational resources of connected vehicles and MEC servers. Then, we reformulate this problem as a Markov Decision Process and propose a digital twin-assisted MADRL algorithm to tackle it. This algorithm tackles the problem by treating each connected vehicle as a agent, where the observations of agents are defined as the current local environmental state and global digital twin information. The action space of agents comprises discrete task offloading targets and continuous resource allocation. The objective of this algorithm is to improve overall system performance, taking into account collaborative learning among the agents. Experimental results show that the MADRL algorithm performed well in computational efficiency and energy consumption compared with other strategies. Copyright © 2025 The Institute of Electronics, Information and Communication Engineers.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1775.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
