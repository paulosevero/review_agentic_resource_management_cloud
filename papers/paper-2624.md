---
id: paper-2624
title: Joint Channel Estimation and Computation Offloading in Fluid Antenna-assisted MEC Networks
authors:
- Ju, Ying
- Li, Mingdong
- Wang, Haoyu
- Liu, Lei
- Qu, Youyang
- Dong, Mianxiong
- Leung, Victor C.M.
- Yuen, Chau
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3672942
url: https://www.scopus.com/pages/publications/105032759910?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- channel estimation
- compressed sensing
- computation offloading
- deep reinforcement learning
- Fluid antenna
- mobile edge computing
- multi-agent
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

# paper-2624 — Joint Channel Estimation and Computation Offloading in Fluid Antenna-assisted MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of fluid antenna (FA) in wireless communications, the capability to dynamically adjust port positions offers substantial benefits in spatial diversity and spectrum efficiency, which are particularly valuable for mobile edge computing (MEC) systems. Therefore, we propose an FA-assisted MEC offloading framework to minimize system delay. This framework faces two severe challenges, which are the complexity of channel estimation due to dynamic port configuration and the inherent non-convexity of the joint optimization problem. Firstly, we propose Information Bottleneck Metric-enhanced Channel Compressed Sensing (IBM-CCS), which advances FA channel estimation by integrating information relevance into the sensing process and capturing key features of FA channels effectively. Secondly, to address the non-convex and high-dimensional optimization problem in FA-assisted MEC systems, which includes FA port selection, beamforming, power control, and resource allocation, we propose a game theory-assisted Hierarchical Twin-Dueling Multi-agent Algorithm (HiTDMA) based offloading scheme, where the hierarchical structure effectively decouples and coordinates the optimization tasks between the user side and the base station side. Crucially, the game theory effectively reduces the dimensionality of power control variables, allowing deep reinforcement learning (DRL) agents to achieve improved optimization efficiency. Numerical results confirm that the proposed scheme significantly reduces system delay and enhances offloading performance, outperforming benchmarks. Additionally, the IBM-CCS channel estimation demonstrates superior accuracy and robustness under varying port densities, contributing to efficient communication under imperfect CSI. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2624.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
