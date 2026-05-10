---
id: paper-2835
title: Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems
authors:
- Wang, Shanshan
- Luo, Zhiyong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3663103
url: https://www.scopus.com/pages/publications/105029975118?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning (DRL)
- mobile edge computing (MEC)
- resource allocation
- service reliability
- trajectory planning
- Unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2835 — Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cellular-connected unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has emerged as a key enabler for the low-altitude economy network (LAEN), supporting task offloading from UAVs to ground base stations (GBSs) in aerial Internet of Things (IoT) applications. However, existing studies focus on conventional stochasticity such as fading channels and random task arrivals, while largely overlooking the dynamic service availability of rapidly deployed ad-hoc GBSs in extreme, high-demand scenarios, characterized by a stress-driven lifecycle including resource depletion, probabilistic service disruptions, and delayed recovery. Such dynamics may cause severe energy inefficiency and queue backlogs, undermining system reliability. To address these issues, we formulate a joint optimization problem of resource allocation and 3D trajectory planning, which explicitly integrates a multi-dimensional GBS reliability-aware model to capture this service lifecycle, aiming to minimize the weighted energy–delay system cost while ensuring long-term queue stability. We develop a dual-layer online optimization framework: the outer layer reformulates the objective function using a time-adaptive velocity-triggered penalty term (TA-VTPT) to suppress energy spikes from abrupt velocity changes, then leverages Lyapunov drift-plus-penalty to decompose the original problem into per-slot subproblems; the inner layer proposes a Lyapunov-guided multi-agent dual actor-critic (LyMADAC) algorithm to generate real-time decentralized decisions without future information. Simulations show that our approach effectively reduces the system cost while ensuring queue stability across heterogeneous traffic patterns and extreme stress scenarios, and further demonstrates robustness under representative non-idealities (e.g., wind disturbance and battery aging). © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2835.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
