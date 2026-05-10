---
id: paper-1848
title: Deep Reinforcement Learning-Based Intelligent Resource Management in Multi-UAVs-Assisted MEC Emergency Communication System
authors:
- Lin, Yuanmo
- Xu, Zhiyong
- Li, Jianhua
- Wang, Jingyuan
- Li, Cheng
venue: IET Communications
venue_type: journal
year: 2025
doi: 10.1049/cmu2.70063
url: https://www.scopus.com/pages/publications/105013960955?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- deep reinforcement learning (DRL)
- emergency communication
- mobile edge computing (MEC)
- non-orthogonal multiple access (NOMA)
- unmanned aerial vehicle (UAV)
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

# paper-1848 — Deep Reinforcement Learning-Based Intelligent Resource Management in Multi-UAVs-Assisted MEC Emergency Communication System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates a multi unmanned aerial vehicles (UAVs) assisted mobile edge computing (MEC) emergency communication system in which each UAV acts as a mobile MEC server for computing tasks offloaded by ground sensor users. Considering the stochastic dynamic characteristics of multi-UAVs-assisted MEC systems and the precision of spectrum resources, the deep reinforcement learning (DRL) algorithm and the non-orthogonal multiple access (NOMA) techniques are introduced. Specifically, we design an offloading algorithm based on a multi-agent deep deterministic policy gradient that jointly optimizes the UAVs' flight trajectories, the sensors' offloading powers, and the dynamic spectrum access to maximize the number of successfully offloaded tasks. The algorithm employs the Gumbel-Softmax method to effectively control both the discrete sensor access action and the continuous offloading power action. Sufficient simulation results show that the proposed algorithm performs significantly better than other benchmark algorithms. © 2025 The Author(s). IET Communications published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1848.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
