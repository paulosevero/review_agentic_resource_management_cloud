---
id: paper-2831
title: 'MA-PF-AD3PG: A Multi-Agent DRL Algorithm for Latency Minimization and Fairness Optimization in 6G IoV-Oriented UAV-Assisted MEC Systems'
authors:
- Wang, Yitian
- Wang, Hui
- Yu, Haibin
venue: Drones
venue_type: journal
year: 2026
doi: 10.3390/drones10010009
url: https://www.scopus.com/pages/publications/105028777967?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- 6G Internet of Vehicles (IoV)
- fairness-aware resource allocation
- multi-agent deep reinforcement learning (MADRL)
- task offloading optimization
- UAV-assisted Mobile Edge Computing (MEC)
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

# paper-2831 — MA-PF-AD3PG: A Multi-Agent DRL Algorithm for Latency Minimization and Fairness Optimization in 6G IoV-Oriented UAV-Assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Highlights: What are the main findings? We develop a priority–fairness coupled optimization framework together with a multi-agent DRL algorithm (MA-PF-AD3PG) to jointly optimize latency, fairness, and task priority in UAV-assisted 6G IoV MEC systems. The proposed algorithm incorporates an occlusion-aware dynamic deadline model, fairness-aware preprocessing, and an adaptive delayed update mechanism, achieving significantly improved convergence stability and scheduling performance. What are the implication of the main findings? The results demonstrate that fairness-driven multi-UAV cooperation can sustain near-perfect service fairness while reducing latency under dynamic vehicular environments. The findings offer practical insights for designing next-generation UAV-assisted drone communication systems that require balanced QoS, priority awareness, and system-wide efficiency. The rapid proliferation of connected and autonomous vehicles in the 6G era demands ultra-reliable and low-latency computation with intelligent resource coordination. Unmanned Aerial Vehicle (UAV)-assisted Mobile Edge Computing (MEC) provides a flexible and scalable solution to extend coverage and enhance offloading efficiency for dynamic Internet of Vehicles (IoV) environments. However, jointly optimizing task latency, user fairness, and service priority under time-varying channel conditions remains a fundamental challenge.To address this issue, this paper proposes a novel Multi-Agent Priority-based Fairness Adaptive Delayed Deep Deterministic Policy Gradient (MA-PF-AD3PG) algorithm for UAV-assisted MEC systems. An occlusion-aware dynamic deadline model is first established to capture real-time link blockage and channel fading. Based on this model, a priority–fairness coupled optimization framework is formulated to jointly minimize overall latency and balance service fairness across heterogeneous vehicular tasks. To efficiently solve this NP-hard problem, the proposed MA-PF-AD3PG integrates fairness-aware service preprocessing and an adaptive delayed update mechanism within a multi-agent deep reinforcement learning structure, enabling decentralized yet coordinated UAV decision-making. Extensive simulations demonstrate that MA-PF-AD3PG achieves superior convergence stability, 13–57% higher total rewards, up to 46% lower delay, and nearly perfect fairness compared with state-of-the-art Deep Reinforcement Learning (DRL) and heuristic methods. © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2831.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
