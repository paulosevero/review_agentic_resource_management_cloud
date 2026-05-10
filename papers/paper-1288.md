---
id: paper-1288
title: 'Cooperative Sensing and Heterogeneous Information Fusion in VCPS: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Xu, Xincao
- Liu, Kai
- Dai, Penglin
- Xie, Ruitao
- Cao, Jingjing
- Luo, Jiangtao
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2024
doi: 10.1109/TITS.2023.3340334
url: https://www.scopus.com/pages/publications/85181835097?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4876--4891
keywords:
- cooperative sensing
- edge computing
- heterogeneous information fusion
- multi-agent deep reinforcement learning
- Vehicular cyber-physical system
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1288 — Cooperative Sensing and Heterogeneous Information Fusion in VCPS: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cooperative sensing and heterogeneous information fusion are critical to realize vehicular cyber-physical systems (VCPSs). This paper makes the first attempt to quantitatively measure the quality of VCPS by designing a new metric called Age of View (AoV). Specifically, we first present the system architecture where heterogeneous information can be cooperatively sensed and uploaded via vehicle-to-infrastructure (V2I) communications in vehicular edge computing (VEC). Logical views are constructed by fusing the heterogeneous information at edge nodes. Further, we formulate the problem by deriving a cooperative sensing model based on the multi-class M/G/1 priority queue, and defining the AoV by modeling the timeliness, completeness and consistency of the logical views. On this basis, a multi-agent difference reward based actor-critic with V2I bandwidth allocation (MDRAC-VBA) solution is proposed. In particular, the system state includes vehicle sensed information, edge cached information and view requirements. The vehicle action space consists of the sensing frequencies and uploading priorities of information. A difference-reward-based credit assignment is designed to divide the system reward, which is defined as the VCPS quality, into the difference reward for vehicles. Edge node allocates V2I bandwidth to vehicles based on predicted vehicle trajectories and view requirements. Finally, we build the simulation model and give a comprehensive performance evaluation, which conclusively demonstrates the superiority of MDRAC-VBA. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1288.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
