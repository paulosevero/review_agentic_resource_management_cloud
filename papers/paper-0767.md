---
id: paper-0767
title: Learning-Based Collaborative Computation Offloading in UAV-Assisted Multi-Access Edge Computing
authors:
- Xu, Zikun
- Liu, Junhui
- Guo, Ying
- Dong, Yunyun
- He, Zhenli
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12204371
url: https://www.scopus.com/pages/publications/85175192459?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- multi-agent deep deterministic policy gradient
- multi-agent reinforcement learning
- task offloading
- UAV-assisted MEC
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0767 — Learning-Based Collaborative Computation Offloading in UAV-Assisted Multi-Access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) have gained considerable attention in the research community due to their exceptional agility, maneuverability, and potential applications in fields like surveillance, multi-access edge computing (MEC), and various other domains. However, efficiently providing computation offloading services for concurrent Internet of Things devices (IOTDs) remains a significant challenge for UAVs due to their limited computing and communication capabilities. Consequently, optimizing and managing the constrained computing, communication, and energy resources of UAVs are essential for establishing an efficient aerial network infrastructure. To address this challenge, we investigate the collaborative computation offloading optimization problem in a UAV-assisted MEC environment comprising multiple UAVs and multiple IODTs. Our primary objective is to obtain efficient offloading strategies within a multi-heterogeneous UAV environment characterized by limited computing and communication capabilities. In this context, we model the problem as a multi-agent markov decision process (MAMDP) to account for environmental dynamics. We employ a multi-agent deep deterministic policy gradient (MADDPG) approach for task offloading. Subsequently, we conduct simulations to evaluate the efficiency of our proposed offloading scheme. The results highlight significant improvements achieved by the proposed offloading strategy, including a notable increase in the system completion rate and a significant reduction in the average energy consumption of the system. © 2023 by the authors.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0767.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
