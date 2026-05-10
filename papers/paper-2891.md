---
id: paper-2891
title: Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV
authors:
- Yin, Peng
- Liang, Wentao
- Wen, Jinbo
- Kang, Jiawen
- Chen, Junlong
- Niyato, Dusit
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3672525
url: https://www.scopus.com/pages/publications/105032780889?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6G
- DM-MAPPO
- IoV
- LSTM-based Transformer
- multi-objective VT migration
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

# paper-2891 — Multi-Agent DRL for Multi-Objective Twin Migration Routing with Workload Prediction in 6G-enabled IoV

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Sixth Generation (6G)-enabled Internet of Vehicles (IoV) facilitates efficient data synchronization through ultra-fast bandwidth and high-density connectivity, enabling the emergence of Vehicle Twins (VTs). As highly accurate replicas of vehicles, VTs can support intelligent vehicular applications for occupants in 6G-enabled IoV. Thanks to the full coverage capability of 6G, resource-constrained vehicles can offload VTs to edge servers, such as roadside units, unmanned aerial vehicles, and satellites, utilizing their computing and storage resources for VT construction and updates. However, communication between vehicles and edge servers with limited coverage is prone to interruptions due to the dynamic mobility of vehicles. Consequently, VTs must be migrated among edge servers to maintain uninterrupted and high-quality services for users. In this paper, we introduce a VT migration framework in 6G-enabled IoV. Specifically, we first propose a Long Short-Term Memory (LSTM)-based Transformer model to accurately predict long-term workloads of edge servers for migration decision-making. Then, we propose a Dynamic Mask Multi-Agent Proximal Policy Optimization (DM-MAPPO) algorithm to identify optimal migration routes in the highly complex environment of 6G-enabled IoV. Finally, we develop a practical platform to validate the effectiveness of the proposed scheme using real datasets. Simulation results demonstrate that the proposed DM-MAPPO algorithm significantly reduces migration latency by 20.82% and packet loss by 75.07% compared with traditional deep reinforcement learning algorithms. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2891.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
