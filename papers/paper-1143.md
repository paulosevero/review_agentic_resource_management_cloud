---
id: paper-1143
title: MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network
authors:
- Qin, Peng
- Wang, Yifei
- Cai, Ziyuan
- Liu, Jiayan
- Li, Jinghan
- Zhao, Xiongwen
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2024
doi: 10.1109/TITS.2023.3342271
url: https://www.scopus.com/pages/publications/85181580632?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6716--6729
keywords:
- Air-ground vehicular cooperative computing network (AVA2N)
- multi-agent deep reinforcement learning (MADRL)
- task offloading
- URLLC-aware
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

# paper-1143 — MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of 5G and Internet of Vehicles (IoV) technologies, vehicles have evolved from mere transportation devices to mobile living spaces for humans. Thus, the complexity of data processing is growing along with the increasing of vehicle applications, which makes relying solely on on-board processing capabilities insufficient. Traditional Roadside Units (RSUs)-based edge computing has limitations such as high deployment cost and finite coverage. To address those issues, we construct an Air-Ground Vehicular Cooperative Computing Network (AVC2N ) that introduces Cooperative Vehicles (CVs) to reduce deployment cost while incorporating Unmanned Aerial Vehicles (UAVs) to expand communication coverage. We aim to balance offloading efficiency and environmental sustainability by proposing a system cost minimization problem with weighted sum of delay and energy consumption. However, it faces new challenges such as the lack of Global State Information (GSI), and the Ultra-Reliable Low-Latency Communications (URLLC) queue delay constraints, rendering traditional methods inadequate. To address the coupling between immediate decision and long-term queuing constraints, we employ Lyapunov optimization to partition the initial problem into two distinct sub-problems. The first focuses on optimizing the system transmission cost, which is tackled using a collaborative Deep Reinforcement Learning (DRL) framework. Specifically, we design an algorithm based on Multi Agent Deep Deterministic Policy Gradient (MADDPG), which effectively addresses GSI uncertainty and ensures URLLC awareness. The second sub-problem addresses server-side computing resource optimization, and we propose a greedy algorithm to tackle it. Experimental results showcase the effectiveness of our approach, demonstrating notable achievement in terms of learning convergence speed, overall system cost, queue delay, and queue backlog.  © 2000-2011 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1143.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
