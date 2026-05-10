---
id: paper-2856
title: 'SGICPNOM: A computation offloading mechanism for 6G space-ground integrated computing power network'
authors:
- Xiao, Yi
- Xu, Xiaolong
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112082
url: https://www.scopus.com/pages/publications/105029078526?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- 6G
- Computation offloading
- Computing power network
- Multi-agent reinforcement learning
- Quality of experience
- Space-ground integrated
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2856 — SGICPNOM: A computation offloading mechanism for 6G space-ground integrated computing power network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Space-Air-Ground Integrated Computing Power Network (SGICPN) faces significant challenges in computation offloading, primarily stemming from the dynamic mobility of Low Earth Orbit (LEO) satellites, heterogeneous resource constraints, stringent Quality of Experience (QoE) requirements, and the lack of effective satellite-terrestrial coordination mechanisms. Existing approaches suffer from inflexible resource allocation, inadequate adaptation to satellite coverage dynamics, neglect of user-centric energy-latency tradeoffs, and absence of coordinated satellite-ground collaboration. To address these challenges, we propose SGICPNOM, a novel computation offloading mechanism featuring three key innovations: 1) A battery-level-driven adaptive weighting strategy that dynamically optimizes latency-energy coefficients to enhance user satisfaction across diverse device states. 2) A unified optimization framework that jointly considers LEO satellite mobility, time-varying coverage patterns, and remote cloud data center resources to enable efficient multi-layer task partitioning. 3) An enhanced multi-agent deep reinforcement learning (MADRL) approach incorporating Prioritized Experience Replay (PER) and hybrid centralized-distributed training, with final allocation decisions refined through our load-aware satellite-cloud coordination mechanism. Results from real environment simulations demonstrate that, compared with state-of-the-art methods, such as Multi-Agent Deep Deterministic Policy Gradient (MADDPG), game-theoretic approaches, hierarchical reinforcement learning, and graph reinforcement learning solutions, SGICPNOM achieves an approximate 22.7% reduction in the weighted sum of latency and energy consumption, while exhibiting strong robustness. The system maintains stability under high network loads while improving overall utilization of both satellite and cloud computing resources, sustaining task success rates above 89%. These results validate SGICPNOM's potential to advance computation offloading technologies in next-generation SGICPN. © 2026 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2856.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
