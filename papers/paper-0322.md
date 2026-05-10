---
id: paper-0322
title: 'Semi-distributed resource management in UAV-aided MEC systems: A multi-agent federated reinforcement learning approach'
authors:
- Nie, Yiwen
- Zhao, Junhui
- Gao, Feifei
- Yu, F. Richard
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2021
doi: 10.1109/TVT.2021.3118446
url: https://www.scopus.com/pages/publications/85117121951?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13162--13173
keywords:
- Deep reinforcement learning (DRL)
- Federated learning (FL)
- Multi-access edge computing (MEC)
- Resource allocation
- Unmanned aerial vehicle (UAV)
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

# paper-0322 — Semi-distributed resource management in UAV-aided MEC systems: A multi-agent federated reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, unmanned aerial vehicle (UAV)-enabled multi-access edge computing (MEC) has been introduced as a promising edge paradigm for the future space-aerial-terrestrial integrated communications. Due to the high maneuverability of UAVs, such a flexible paradigm can improve the communication and computation performance for multiple user equipments (UEs). In this paper, we consider the sum power minimization problem by jointly optimizing resource allocation, user association, and power control in an MEC system with multiple UAVs. Since the problem is nonconvex, we propose a centralized multi-agent reinforcement learning (MARL) algorithm to solve it. However, the centralized method ignores essential issues like distributed framework and privacy concern. We then propose a multi-agent federated reinforcement learning (MAFRL) algorithm in a semi-distributed framework. Meanwhile, we introduce the Gaussian differentials to protect the privacy of all UEs. Simulation results show that the semi-distributed MAFRL algorithm achieves close performances to the centralized MARL algorithm and significantly outperform the benchmark schemes. Moreover, the semi-distributed MAFRL algorithm costs 23% lower opeartion time than the centralized algorithm. 0018-9545 © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0322.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
