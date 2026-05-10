---
id: paper-2675
title: 'JTOLP-MADRL: A MADRL-Based Joint Optimization Algorithm of Task Offloading Location and Proportion for Latency-Sensitive Tasks in Vehicle Edge Computing Network'
authors:
- Liao, Chengwei
- Yan, Guofeng
- Tan, Hengliang
- Du, Jiao
- Deng, Xia
- Wu, Heng
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2026
doi: 10.1109/TNSM.2026.3669913
url: https://www.scopus.com/pages/publications/105032146172?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3088--3104
keywords:
- deep reinforcement learning
- quality of service
- Task offloading
- vehicular edge computing
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

# paper-2675 — JTOLP-MADRL: A MADRL-Based Joint Optimization Algorithm of Task Offloading Location and Proportion for Latency-Sensitive Tasks in Vehicle Edge Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In Vehicle Edge Computing Network (VECN), task offloading is a key technique to provide the satisfactory quality of service (QoS) for latency-sensitive tasks. However, the diversity of computational resources in edge nodes (i.e., RSU and idle vehicles) and the mobility of vehicles present significant challenges to task offloading. Hence, to address these challenges, we propose an offloading scheme that jointly allocates RSU nodes (including MEC servers) and idle service vehicle resources in this paper. We first prioritize these tasks based on their maximum tolerable latency and design a utility function to capture the executing cost for latency-sensitive tasks. Then, we propose a joint optimization algorithm of task offloading location and proportion based on Multi-agent Deep Reinforcement Learning (jTOLP-MADRL algorithm) for latency-sensitive tasks in VECN, which consists of two sub-algorithms: the Offloading Location Selection (OLS) algorithm and the Offloading Proportion Allocation (OPA) algorithm. Additionally, we design a Convolutional Recurrent Actor-Critic Network (CRACN) to enhance the learning efficiency of the OLS algorithm. Finally, we indicate our algorithm is effective based on simulation results. Compared with the other benchmark algorithms, jTOLP-MADRL can significantly reduce latency and enhance system utility.  © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2675.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
