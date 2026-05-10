---
id: paper-1487
title: Energy Consumption Optimization of UAV-Assisted Edge Computing Network via Tiny-MADDPG
authors:
- Cheng, Jialei
- Yan, Ming
- Lei, Ling
- Li, Lifen
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Spring65109.2025.11174492
url: https://www.scopus.com/pages/publications/105019039481?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- energy consumption optimization
- mobile edge computing
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1487 — Energy Consumption Optimization of UAV-Assisted Edge Computing Network via Tiny-MADDPG

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapidly growing demand for mobile edge computing (MEC), unmanned aerial vehicles (UAVs) are increasingly used in task offloading and area coverage. However, high energy consumption and computational complexity become the key challenges limiting their development. In this paper, we propose the tiny multi-agent deep deterministic policy gradient (Tiny-MADDPG) algorithm based on deep reinforcement learning (DRL), which aims to optimize the energy consumption of multi-UAV-assisted MEC systems. By constructing a multi-agent deep deterministic policy gradient (MADDPG) framework and combining it with a lightweight network design, the algorithm achieves joint optimization of flight paths, task offloading and resource allocation. For the multi-UAV collaboration scenario, a comprehensive reward function containing energy consumption, delay and coverage is designed to ensure the overall improvement of system performance. Simulation experiments show that TinyMADDPG achieves significant results in minimizing energy consumption compared with other benchmark algorithms. The results validate the dual advantages of multi-agent collaboration and lightweight design, and provide a valuable reference for energy consumption optimization of multi-UAV systems. © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1487.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
