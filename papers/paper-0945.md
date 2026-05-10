---
id: paper-0945
title: Multi-Agent DRL-Based Task Offloading in Multiple RIS-Aided IoV Networks
authors:
- Hazarika, Bishmita
- Singh, Keshav
- Biswas, Sudip
- Mumtaz, Shahid
- Li, Chih-Peng
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2023.3302010
url: https://www.scopus.com/pages/publications/85176125685?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1175--1190
keywords:
- Internet of vehicles (IoV)
- multi-access edge computing (MAEC)
- multi-agent deep reinforcement learning (MA-DRL)
- reconfigurable intelligent surface (RIS)
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

# paper-0945 — Multi-Agent DRL-Based Task Offloading in Multiple RIS-Aided IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article considers an internet of vehicles (IoV) network, where multi-access edge computing (MAEC) servers are deployed at base stations (BSs) aided by multiple reconfigurable intelligent surfaces (RISs) for both uplink and downlink transmission. An intelligent task offloading methodology is designed to optimize the resource allocation scheme in the vehicular network which is based on the state of criticality of the network and the priority and size of tasks. We then develop a multi-agent deep reinforcement learning (MA-DRL) framework using the Markov game for optimizing the task offloading decision strategy. The proposed algorithm maximizes the mean utility of the IoV network and improves communication quality. Extensive numerical results were performed that demonstrate that the RIS-assisted IoV network using the proposed MA-DRL algorithm achieves higher utility than current state-of-the art networks (not aided by RISs) and other baseline DRL algorithms, namely soft actor-critic (SAC), deep deterministic policy gradient (DDPG), twin delayed DDPG (TD3). The proposed method improves the offloading data rate of the tasks, reduces the mean delay and ensures that a higher percentage of offloaded tasks are completed compared to that of other DRL-based and non-RIS-assisted IoV frameworks.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0945.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
