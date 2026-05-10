---
id: paper-1186
title: DRL-Based Multidimensional Resource Management in SWIPT-NOMA-Enabled MEC
authors:
- Shi, Zhaoyuan
- Xie, Xianzhong
- Lu, Huabing
- Yang, Helin
- Xiong, Zehui
- Cai, Jun
- Ding, Zhiguo
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2023.3306880
url: https://www.scopus.com/pages/publications/85168652957?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3252--3266
keywords:
- MADDPG
- MEC
- multidimensional resource management
- NOMA
- SWIPT
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

# paper-1186 — DRL-Based Multidimensional Resource Management in SWIPT-NOMA-Enabled MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) enables communication users with limited computation power to offload computation-intensive tasks to the edge server, thus dramatically enhancing the limited computing capabilities of the users. As the reality of scarce spectrum resources and the energy-constrained nature of communication users, this paper introduces non-orthogonal multiple access (NOMA) and simultaneous wireless information and power transfer (SWIPT) techniques to achieve more efficient task offloading in MEC. To minimize the number of computationally failed tasks while simultaneously satisfying different quality of service (QoS) requirements of users, a joint resource management problem of the spectrum, computation, and energy resources is formulated. Due to the non-convexity of the offloading optimization problem and the stochastic nature of the constructed MEC environment, a multiple agents deep deterministic policy gradient (MADDPG)-based resource management algorithm is proposed to manage each user's multidimensional resources without collaborating. The simulation results show that compared to other benchmark schemes, the proposed algorithm can effectively improve both the communication and computational performances in MEC.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1186.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
