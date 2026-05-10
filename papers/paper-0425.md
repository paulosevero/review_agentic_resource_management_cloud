---
id: paper-0425
title: Multi-Agent DRL-Based Computation Offloading in Multiple RIS-Aided IoV Networks
authors:
- Hazarika, Bishmita
- Singh, Keshav
- Li, Chih-Peng
- Biswas, Sudip
venue: Proceedings - IEEE Military Communications Conference MILCOM
venue_type: conference
year: 2022
doi: 10.1109/MILCOM55135.2022.10017765
url: https://www.scopus.com/pages/publications/85147333194?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1--6
keywords:
- Internet of vehicles (IoV)
- multi-access edge computing (MEC)
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

# paper-0425 — Multi-Agent DRL-Based Computation Offloading in Multiple RIS-Aided IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper considers an internet of vehicles (IoV) network consisting of vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) architecture aided by multi-access edge computing (MEC) servers deployed at base stations (BSs). The V2I communication is also assisted by multiple reconfigurable intelligent surfaces (RISs) for both uplink and downlink transmission. An intelligent task offloading methodology is designed to optimize the resource allocation scheme in the vehicular network which is based on the condition of the network and the priority and size of tasks. Furthermore, we also propose a multi-agent deep reinforcement learning (MA-DRL) algorithm for optimizing task offloading decision strategy and then compare its performance with benchmark DRL algorithms such as soft actor-critic (SAC), deep deterministic policy gradient (DDPG), twin delayed DDPG (TD3). Additionally, we compare the performance of the vehicle-to-BS or V2I offloading system with and without the presence of RIS in the proposed framework. Extensive numerical results are performed that demonstrate that the proposed MA-DRL-based RIS-assisted IoV network achieves higher utility, while improving the offloading rate of the tasks as well as ensuring that a higher percentage of offloaded tasks are completed compared to that of other DRL based and non-RIS assisted IoV frameworks.  © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0425.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
