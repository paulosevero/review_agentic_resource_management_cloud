---
id: paper-0956
title: 'Joint Offloading and Resource Allocation for Hybrid Cloud and Edge Computing in SAGINs: A Decision Assisted Hybrid Action Space Deep Reinforcement Learning Approach'
authors:
- Huang, Chong
- Chen, Gaojie
- Xiao, Pei
- Xiao, Yue
- Han, Zhu
- Chambers, Jonathon A.
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2024
doi: 10.1109/JSAC.2024.3365899
url: https://www.scopus.com/pages/publications/85186068958?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1029--1043
keywords:
- deep reinforcement learning
- edge computing
- resource allocation
- Space-air-ground integrated networks
- unmanned aerial vehicle
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

# paper-0956 — Joint Offloading and Resource Allocation for Hybrid Cloud and Edge Computing in SAGINs: A Decision Assisted Hybrid Action Space Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, the amalgamation of satellite communications and aerial platforms into space-air-ground integrated network (SAGINs) has emerged as an indispensable area of research for future communications due to the global coverage capacity of low Earth orbit (LEO) satellites and the flexible Deployment of aerial platforms. This paper presents a deep reinforcement learning (DRL)-based approach for the joint optimization of offloading and resource allocation in hybrid cloud and multi-access edge computing (MEC) scenarios within SAGINs. The proposed system considers the presence of multiple satellites, clouds and unmanned aerial vehicles (UAVs). The multiple tasks from ground users are modeled as directed acyclic graphs (DAGs). With the goal of reducing energy consumption and latency in MEC, we propose a novel multi-agent algorithm based on DRL that optimizes both the offloading strategy and the allocation of resources in the MEC infrastructure within SAGIN. A hybrid action algorithm is utilized to address the challenge of hybrid continuous and discrete action space in the proposed problems, and a decision-assisted DRL method is adopted to reduce the impact of unavailable actions in the training process of DRL. Through extensive simulations, the results demonstrate the efficacy of the proposed learning-based scheme, the proposed approach consistently outperforms benchmark schemes, highlighting its superior performance and potential for practical applications.  © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0956.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
