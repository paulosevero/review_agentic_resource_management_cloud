---
id: paper-2696
title: Maximizing Computation Efficiency and Fairness of Multi-UAV Assisted MEC System Supported by RIS
authors:
- Lu, Zekun
- Zhai, Linbo
- Zhou, Wenjie
- Jia, Yujuan
- Jin, Meiyu
- Sun, Jiande
- Liu, Zhiquan
venue: IEEE Transactions on Communications
venue_type: journal
year: 2026
doi: 10.1109/TCOMM.2025.3624168
url: https://www.scopus.com/pages/publications/105019666942?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 854--869
keywords:
- computation efficiency
- flight trajectory
- FMAI
- GUAIFCM
- MADDPGAI
- MEC
- RIS
- UAV
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2696 — Maximizing Computation Efficiency and Fairness of Multi-UAV Assisted MEC System Supported by RIS

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, unmanned aerial vehicles (UAVs) have been widely used in mobile edge computing (MEC) systems to compute part of the computing tasks offloaded from ground equipments (GEs) due to their high mobility and flexibility. In addition, reconfigurable intelligent surfaces (RIS), as an emerging technology, can enhance the wireless propagation environment in wireless networks and improve the computation efficiency of the system. In this paper, we propose a multi-UAV-assisted MEC system supported by RIS, where GEs can partially offload tasks to UAVs for computation. A joint optimization problem is formulated to maximize the weighted computation efficiency and fairness by optimizing the user association state, offloading ratio, computing resource allocation, the trajectory of UAVs and the actual RIS phase shift design. To solve the problem, a Fuzzy C-Means-Multi-Agent Deep Deterministic Policy Gradient Alternating Iterative (FMAI) algorithm is designed. In this algorithm, we firstly design a GE-UAV Association and Variable Initialization Combine Fuzzy C-Means Clustering (GUAIFCM) algorithm to solve GE-UAV association strategy. Then we introduce the multi-agent deep deterministic policy gradient alternating iteration (MADDPGAI) algorithm to solve the computation resource allocation, the trajectory of UAVs, task allocation and RIS phase shift. The simulation results show that the proposed scheme can significantly improve the computation efficiency and fairness of RIS-assisted multi-UAV MEC system compared with the benchmark scheme. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2696.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
