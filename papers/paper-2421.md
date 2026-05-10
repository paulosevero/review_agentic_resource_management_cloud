---
id: paper-2421
title: Bi-Directional Computation Offloading in Caching Enabled UAV-assisted MEC Systems
authors:
- Zhang, Xianzi
- Gao, Ang
- Zhang, Qiong
- Hu, Yansu
venue: 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCC65529.2025.11148633
url: https://www.scopus.com/pages/publications/105017567727?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Heterogeneous MADRL
- Mobile Edge Computing
- Service Caching
- Task Offloading
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

# paper-2421 — Bi-Directional Computation Offloading in Caching Enabled UAV-assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To alleviate the computation resource scarcity of terrestrial wireless devices (WDs), a mobile edge computing (MEC) system with the assistance of unmanned aerial vehicles (UAVs) is envisaged as a promising paradigm where UAVs, acting as aerial relays and mobile MEC servers can provide extensive coverage, line-of-sight (LoS) communication links and supplementary computation resources. However, the high-correlated WDs' mobile applications will incur repeat transmission of programs, which induces a decline in the quality of service. Therefore, the paper considers a service caching enabled UAVs to assist MEC systems with a bi-directional computation offloading scheme, where UAVs can temporarily store the popular service programs from a cloud-like database and move to the vicinity of WDs to establish bi-directional connections for both data uploading and program downloading, thus can be beneficial for saving both the tasks' local and remote execution latency. To fully exploit the potential of such a bi-directional offloading scheme, it is crucial to jointly optimize the offloading decision of multiple WDs, both the downlink and uplink channel allocation, the cache decision of UAVs, the computation resource allocation of each WD, as well as UAVs' trajectory. Therefore, the paper proposes a clustering, heterogeneous multi-agent deep reinforcement learning (MADRL), and successive convex approximation (SCA) combined alternative optimization method to conquer the non-trivial feature of such a non-convex mixed integer non-linear programming (MINLP) problem. Numerical simulation results reveal its effectiveness and superiority in reducing the task latency and saving energy consumption compared to the uni-directional offloading and non-caching-equipped schemes.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2421.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
