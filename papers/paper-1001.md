---
id: paper-1001
title: 'Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning'
authors:
- Lei, Chengjia
- Wu, Shaohua
- Yang, Yi
- Xue, Jiayin
- Zhang, Qinyu
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3388499
url: https://www.scopus.com/pages/publications/85190735681?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12328--12344
keywords:
- automatic surface vehicle (ASV)
- efficiency
- fault-tolerant communication
- Maritime search and rescue (SAR)
- multi-agent reinforcement learning (MARL)
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

# paper-1001 — Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, multiple types of equipment, including unmanned aerial vehicles (UAVs) and automatic surface vehicles (ASVs), have been deployed in maritime search and rescue (SAR). However, due to the lack of base stations (BSs), how to complete rescue while maintaining communication between vehicles is an unresolved challenge. In this paper, we design an efficient and fault-tolerant communication solution by jointly optimizing vehicles' trajectory, offloading scheduling, and routing topology for a heterogeneous vehicle system. First, we model several essential factors in maritime SAR, including the impact of ocean currents, the observational behavior of UAVs, the fault tolerance of relay networks, resource management of mobile edge computing (MEC), and energy consumption. A multi-objective optimization problem is formulated, aiming at minimizing time and energy consumption while increasing the fault tolerance of relay networks. Then, we transfer the objective into a decentralized partially observable Markov Decision Process (Dec-POMDP) and introduce multi-agent reinforcement learning (MARL) to search for a collaborative strategy. Specifically, two MARL approaches with different training styles are evaluated, and three techniques are added for improving performance, including sharing parameters, normalized generalized-advantage-estimation (GAE), and preserving-outputs-precisely-while-adaptively-rescaling-targets (Pop-Art). Experimental results demonstrate that our proposed approach, named heterogeneous vehicles multi-agent proximal policy optimization (HVMAPPO), outperforms other baselines in efficiency and fault tolerance of communication. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1001.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
