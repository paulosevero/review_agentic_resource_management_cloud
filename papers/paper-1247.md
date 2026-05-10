---
id: paper-1247
title: Fairness-Aware Computation Offloading with Trajectory Optimization and Phase-Shift Design in RIS-Assisted Multi-UAV MEC Network
authors:
- Wang, Shumo
- Song, Xiaoqin
- Song, Tiecheng
- Yang, Yang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3371395
url: https://www.scopus.com/pages/publications/85187017081?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20547--20561
keywords:
- Deep reinforcement learning (DRL)
- fairness
- mobile-edge computing (MEC)
- reconfigurable intelligent surface (RIS)
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

# paper-1247 — Fairness-Aware Computation Offloading with Trajectory Optimization and Phase-Shift Design in RIS-Assisted Multi-UAV MEC Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) are regarded as a promising solution for mobile-edge computing (MEC) systems due to their flexibility and capability to provide computing services to ground terminals (GTs). By leveraging UAVs, the latency in computation tasks can be reduced significantly, particularly in disaster scenarios. Additionally, reconfigurable intelligent surfaces (RISs) have emerged as a novel technology for enhancing the wireless propagation environment in wireless networks. This article proposes a multi-UAV-assisted MEC system where computation tasks of GTs can be computed locally or partially offloaded to UAVs. Furthermore, practical RIS phase shift designs are considered to enhance the communication performance between GTs and UAVs. To minimize the system delay and achieve fairness among GTs, the computation offloading strategy, trajectory of the UAVs are optimized using a Markov decision process. Simultaneously, the RIS phase shift is optimized through an alternating optimization algorithm. Additionally, a cooperative multiagent deep reinforcement learning framework is developed to obtain a optimal solution by employing the multiagent twin delayed deep deterministic policy gradient (MATD3) algorithm. Numerical results indicate that MATD3 can effectively improve the system delay and fairness performance of the RIS-assisted multi-UAV MEC system, as compared to benchmark solutions.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1247.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
