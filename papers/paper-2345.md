---
id: paper-2345
title: Dynamic Task Offloading and Resource Allocation for Air-Ground Integrated Networks Based on MADDPG
authors:
- Xue, Jianbin
- Mao, Peipei
- Wang, Luyao
- Yu, Qingda
- Fan, Changwang
venue: Journal of Beijing Institute of Technology (English Edition)
venue_type: journal
year: 2025
doi: 10.15918/j.jbit1004-0579.2024.124
url: https://www.scopus.com/pages/publications/105012397904?origin=resultslist
publisher: Beijing Institute of Technology
pages: 243--267
keywords:
- air-ground integrated network (AGIN)
- dynamic task offloading
- multi-agent deep deterministic policy gradient (MADDPG)
- non-orthogonal multiple access (NOMA)
- resource allocation
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

# paper-2345 — Dynamic Task Offloading and Resource Allocation for Air-Ground Integrated Networks Based on MADDPG

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of connected devices, traditional edge-cloud systems are under overload pressure. Using mobile edge computing (MEC) to assist unmanned aerial vehicles (UAVs) as low altitude platform stations (LAPS) for communication and computation to build air-ground integrated networks (AGINs) offers a promising solution for seamless network coverage of remote internet of things (IoT) devices in the future. To address the performance demands of future mobile devices (MDs), we proposed an MEC-assisted AGIN system. The goal is to minimize the long-term computational overhead of MDs by jointly optimizing transmission power, flight trajectories, resource allocation, and offloading ratios, while utilizing non-orthogonal multiple access (NOMA) to improve device connectivity of large-scale MDs and spectral efficiency. We first designed an adaptive clustering scheme based on K-Means to cluster MDs and established communication links, improving efficiency and load balancing. Then, considering system dynamics, we introduced a partial computation offloading algorithm based on multi-agent deep deterministic policy gradient (MADDPG), modeling the multi-UAV computation offloading problem as a Markov decision process (MDP). This algorithm optimizes resource allocation through centralized training and distributed execution, reducing computational overhead. Simulation results show that the proposed algorithm not only converges stably but also outperforms other benchmark algorithms in handling complex scenarios with multiple devices. © 2025 Beijing Institute of Technology. All rights reserved.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2345.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
