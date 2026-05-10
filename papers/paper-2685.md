---
id: paper-2685
title: Latency-Aware Optimization of UAV Deployment, Computation Offloading, and Resource Allocation for IoRT in Space-Air-Ground Integrated Networks
authors:
- Liu, Xiaomin
- Peng, Yujie
- Song, Xiaoqin
- Song, Tiecheng
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2025.3617111
url: https://www.scopus.com/pages/publications/105017691025?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6448--6461
keywords:
- computation offloading
- multi-agent deep reinforcement learning
- Space-air-ground integrated networks (SAGIN)
- time slot resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2685 — Latency-Aware Optimization of UAV Deployment, Computation Offloading, and Resource Allocation for IoRT in Space-Air-Ground Integrated Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The unmanned aerial vehicle (UAV)-assisted space-air-ground integrated networks (SAGIN) can provide communication and computing services for Internet of Remote Things (IoRT) in the absence of ground cellular network coverage. In this paper, we propose an edge computing architecture based on SAGIN, comprising three parts: a satellite, UAVs, and ground-based IoRT devices. The satellite is responsible for providing access to cloud computing resources. UAVs are equipped with mobile edge computing (MEC) servers. And IoRT devices generate latency-sensitive tasks but possess limited computing capabilities. Our objective is to minimize task processing delays by jointly optimizing UAV deployment, computation offloading, and time slot resource allocation to meet the increasing demands of IoRT devices. Specifically, the proposed problem is decomposed into two components. First, for the deployment of multiple UAVs, we propose a multi-agent softmax deep double deterministic policy gradient (MASD3) approach, which enables UAVs to adjust their flight trajectories based solely on observed information for adaptive deployment. Second, for the computation offloading and time slot resource allocation problems in SAGIN, we employ a numerical computation-based iterative optimization method to minimize the occupation of time slots by computation offloading. Simulation results demonstrate that our proposed solution significantly reduces overall delay compared to alternative benchmark schemes. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2685.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
