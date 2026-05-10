---
id: paper-0755
title: Computation Offloading Method Using Stochastic Games for Software-Defined-Network-Based Multiagent Mobile Edge Computing
authors:
- Wu, Guowen
- Wang, Hui
- Zhang, Hong
- Zhao, Yuhan
- Yu, Shui
- Shen, Shigen
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3277541
url: https://www.scopus.com/pages/publications/85160261089?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17620--17634
keywords:
- Computation offloading
- mobile edge computing (MEC)
- multiagent reinforcement learning (MARL)
- resource allocation
- stochastic game
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
    my_justification: Out of scope
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

# paper-0755 — Computation Offloading Method Using Stochastic Games for Software-Defined-Network-Based Multiagent Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the scenario of Industry 4.0, mobile smart devices (SDs) on production lines have to process massive amounts of data. These computing tasks sometimes far exceed the computing capability of SDs and require lots of energy and time to process. How to effectively reduce energy consumption and latency is necessary to be solved. To this end, we first propose a software-defined network (SDN)-based mobile edge computing (MEC) system. In the MEC system, SDs can offload computation tasks to edge servers to decrease the processing latency and avoid the waste of energy. At the same time, taking advantage of SDN's programmability, scalability, and isolation of the control plane and the data plane, an SDN controller can manage edge devices within the MEC system. Second, based on a stochastic game, we study the computation offloading and resource allocation problems in the MEC system and establish a stochastic game-based computation offloading model. Furthermore, we prove that the multiuser stochastic game in this system can achieve Nash Equilibrium. We further consider each SD as an independent agent and design a stochastic game-based resource allocation algorithm with prioritized experience replays (SGRA-PERs) to minimize energy consumption and processing latency with Multiagent Reinforcement Learning. Experiment results demonstrate that the proposed SGRA-PER is superior to MADDPG, Q-Mix, and MAPPO algorithms, which can significantly reduce the processing delay and energy consumption with dynamic resource allocation. Moreover, SGRA-PER can still keep a higher performance under the increase of SDs, which can be applied in a large-scale MEC system.  © 2014 IEEE.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0755.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
