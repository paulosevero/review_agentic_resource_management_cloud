---
id: paper-0948
title: Task Scheduling and Trajectory Optimization Based on Fairness and Communication Security for Multi-UAV-MEC System
authors:
- He, Yejun
- Xiang, Kun
- Cao, Xiaowen
- Guizani, Mohsen
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3412825
url: https://www.scopus.com/pages/publications/85196074209?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 30510--30523
keywords:
- Fairness
- mobile edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- multiunmanned aerial vehicles (UAVs)
- offloading strategy
- security
- transmit power
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

# paper-0948 — Task Scheduling and Trajectory Optimization Based on Fairness and Communication Security for Multi-UAV-MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) show significant potential in enhancing communication services within the mobile edge computing (MEC) system by taking their advantages on the flexible mobility and reliable line-of-sight links. However, in the scenarios with multiple UAV-MECs (UMs) operating concurrently, potential conflicts in their trajectories need to be mitigated. Thus, the 3-D trajectory needs to be properly designed in a highly reliable manner. Besides, such an infrastructure-free communication paradigm also exposes a potential risk of misuse by malicious parties, which allows them to eavesdrop on private communications, posing a threat to the security and privacy. Therefore, we consider a multi-UAV-assisted MEC communication system, where a UAV maliciously eavesdrops on the data transmission from the user devices (UDs) while a jammer is deployed on the ground to interfere with the eavesdropping channel. In specific, our objective is to minimize the energy consumption and latency while incorporating fairness metrics by optimizing the 3-D trajectories of UMs, transmission power of UDs, and the offloading strategies under the constraints of ensuring communication security and load fairness. Given the complexity of this mixed-integer nonconvex programming problem, we decompose the formulated problem into three subproblems. Specifically, at each time slot, we optimize the transmit power and offloading strategies using theoretical derivation and mathematical analysis, respectively. Additionally, a multiagent deep deterministic policy gradient (MADDPG) algorithm is employed to optimize the trajectories of UMs. Simulation results demonstrate that our proposed joint optimization algorithm successfully minimizes the system energy consumption and delay as compared to benchmarking schemes.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0948.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
