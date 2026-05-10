---
id: paper-1558
title: 'Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach'
authors:
- Fan, Xiaokun
- Chen, Yali
- Liu, Min
- Zhu, Yuchen
- Li, Zhongcheng
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2025.111540
url: https://www.scopus.com/pages/publications/105011040057?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Edge computing
- Joint sensing and computing
- Multi-agent deep reinforcement learning
- Unmanned aerial vehicle
- Video surveillance
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1558 — Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) are increasingly used for surveillance applications to take videos for Points of Interests (PoIs). Then, the sampled video data is fed into deep neural networks (DNNs) for inference. Due to the high computational complexity of DNNs, directly running DNN inference tasks on resource-constrained UAVs is intractable. To alleviate this issue, edge computing provides a promising solution by offloading tasks to the ground edge servers (ESs). However, how to flexibly schedule and tradeoff various resources for high-accuracy and low-delay inference is a challenge, especially in the complex scenario where video data sensing and DNN task processing are tightly coupled. Thus, this paper studies joint optimization for data sensing and computing in the air–ground collaborative inference framework. Specifically, the models for multi-UAV collaborative data sensing and collaborative inference between multiple UAVs and multiple ESs are designed. Then, we formulate an inference delay minimization problem by jointly optimizing UAVs’ 3D trajectories, number of sampled video frames and computation offloading, while satisfying accuracy, UAV energy budget and sensing mission requirements. Considering mixed continuous–discrete optimization variables, we propose a multi-agent proximal policy optimization (MAPPO) algorithm with a hybrid action space, called “MAPPO-HA”, to learn the optimal policies. Finally, simulation results demonstrate that our algorithm can achieve better performance compared with other optimization approaches. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1558.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
