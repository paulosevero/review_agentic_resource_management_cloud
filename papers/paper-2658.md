---
id: paper-2658
title: Deep Reinforcement Learning Enabled Joint Task Offloading and Trajectory Optimization in Multi-UAV Systems
authors:
- Li, Ju
- Shang, Fengjun
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2026
doi: 10.1109/TCE.2026.3679687
url: https://www.scopus.com/pages/publications/105034666077?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- multi-agent deep reinforcement learning
- task offloading
- trajectory planning
- unmanned aerial vehicles
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2658 — Deep Reinforcement Learning Enabled Joint Task Offloading and Trajectory Optimization in Multi-UAV Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> UAV-assisted multi-access edge computing (MEC) enables flexible task offloading in emergency communication networks, but joint trajectory planning and task offloading optimization remain challenging due to UAV mobility and dynamic network conditions. This paper proposes a multi-agent deep deterministic policy gradient (MADDPG)-based framework to jointly optimize UAV trajectory planning and task offloading decisions. The proposed approach follows a centralized training with decentralized execution (CTDE) paradigm, enabling UAVs to learn coordinated computation and communication strategies in dynamic environments. Each UAV is modeled as an autonomous agent, and an actor–critic architecture is designed, where distributed actors generate offloading and movement policies, while a centralized critic evaluates global state–action values to guide cooperative learning. To improve training stability and convergence efficiency, experience replay and soft update mechanisms are incorporated. Extensive simulation results demonstrate that the proposed MADDPG framework significantly reduces task offloading latency and computational overhead while improving system throughput, outperforming conventional optimization methods, and validating its effectiveness in emergency communication networks. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2658.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
