---
id: paper-2503
title: Mission-Aware Resource Allocation and Safe Trajectory Control for Multi-UAV Edge-Enabled Sensing Networks
authors:
- Alazzwi, Abee
- Tshakwanda, Petro M.
- Tsegaye, Henok B.
- Devetsikiotis, Michael
- Kumar, Harsh
venue: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
venue_type: conference
year: 2026
doi: 10.1109/CCWC67433.2026.11393718
url: https://www.scopus.com/pages/publications/105035600726?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 633--639
keywords:
- edge computing
- hierarchical PPO
- mission-aware resource allocation
- multi-agent reinforcement learning (MARL)
- Multi-UAV networks
- safe trajectory control
- safety-critical systems
- zeroing control barrier functions (ZCBF)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2503 — Mission-Aware Resource Allocation and Safe Trajectory Control for Multi-UAV Edge-Enabled Sensing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present HSPPO (Hierarchical Safe Proximal Policy Optimization), a mission-aware multi-agent reinforcement learning (MARL) framework that integrates resource allocation and safe trajectory control for cooperative unmanned aerial vehicles (UAVs) in edge-enabled sensing networks. Rather than introducing new barrier-function theory, HSPPO tightly couples discrete-time zeroing control barrier functions (ZCBFs) with PPO training by embedding safety filtering directly within rollouts and augmenting policy updates with a safety-imitation loss. This design aligns learning with formally safe actions while optimizing deadline-driven latency, energy consumption, and mission utility. Each UAV autonomously selects motion, missionzone association, and computation-communication splitting via a safety-constrained actor-critic, while a hierarchical structure combines a mission-aware scheduler with low-level controllers under centralized training and decentralized execution. We evaluate HSPPO in a simulation-based multi-UAV MEC environment across varying fleet sizes, mission-zone scales, priority distributions, and propagation conditions. In a nominal 1000 × 1000 m scenario with six UAVs and eight mission zones, HSPPO achieves an 83.7% mission completion rate with only 0.5 safety violations per episode, yielding 96% fewer collisions than a greedy heuristic baseline. It further attains 0.72 normalized latency and 0.75 normalized energy, improving completion by 9.2 percentage points relative to PPO without safety (83.7% vs. 74.5%) and reducing latency and energy by approximately 15-16%. Ablation and scalability studies, including safety-parameter sweeps, fallback-mechanism variants, and mission-context removal, indicate that safety-in-the-loop MARL can enable reliable and deadline-compliant coordination for multi-UAV edge-sensing missions under realistic system constraints. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2503.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
