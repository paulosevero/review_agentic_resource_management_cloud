---
id: paper-1128
title: 'Decentralized Multi-UAV Management in Mobile Edge Computing: A Hierarchical Reinforcement Learning Approach'
authors:
- Peng, Ziling
- Liu, Shuai
- Jaber, Al
- Jian, Lim W.E.I.
- Li, Hui
- Qian, Jin
venue: Proceedings - 2024 3rd International Conference on Computing, Communication, Perception and Quantum Technology, CCPQT 2024
venue_type: conference
year: 2024
doi: 10.1109/CCPQT64497.2024.00062
url: https://www.scopus.com/pages/publications/105000745616?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 287--291
keywords:
- Hierarchical Reinforcement Learning
- Mobile Edge Computing
- Multi-Agent Deep Reinforcement Learning
- Multi-UAV
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
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

# paper-1128 — Decentralized Multi-UAV Management in Mobile Edge Computing: A Hierarchical Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of drones in Mobile Edge Computing (MEC) has opened new possibilities for enhancing network performance in various fields, such as agriculture, environmental monitoring, and disaster management. However, effective coordination of multiple Unmanned Aerial Vehicles (UAVs) in dynamic and distributed environments poses significant challenges, especially in mobility management and resource allocation. To address these issues, we propose a Decentralized Hierarchical Policy Framework inspired by hierarchical reinforcement learning. This framework employs a two-level structure, consisting of high-level communication coordinators and low-level executors, allowing UAVs to make decentralized decisions based on local observations and partial communication. Our approach models the multi-UAV MEC problem as a Decentralized Partially Observable Markov Decision Process with communication, enabling efficient task allocation and resource management. Experimental evaluations demonstrate that the proposed method improves MEC service coverage, reduces latency, and optimizes UAV energy consumption. Compared to state-of-the-art Multi-Agent Reinforcement Learning methods, our approach achieves superior performance in dynamic and large-scale environments. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1128.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
