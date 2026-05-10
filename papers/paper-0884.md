---
id: paper-0884
title: Multi-Hop Task Routing in Vehicle-Assisted Collaborative Edge Computing
authors:
- Deng, Yiqin
- Zhang, Haixia
- Chen, Xianhao
- Fang, Yuguang
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2023.3312142
url: https://www.scopus.com/pages/publications/85171545736?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2444--2455
keywords:
- Collaborative edge computing
- computation offloading
- deep reinforcement learning (DRL)
- multi-hop routing
- vehicular networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0884 — Multi-Hop Task Routing in Vehicle-Assisted Collaborative Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Collaborative edge computing has emerged as a novel paradigm that allows edge servers (ESs) to share data and computing resources, effectively mitigating network congestion in traditional multi-access edge computing (MEC) scenarios. However, existing research in collaborative edge computing often limits offloading to only one hop, which may lead to suboptimal computing resource sharing due to challenges such as poor channel conditions or high computing workload at ESs located just one hop away. To address this limitation and enable more efficient computing resource utilization, we propose a multi-hop MEC approach that leverages omnipresent vehicles in urban areas to create a data transportation network for task delivery. Here, we propose a general multi-hop task offloading framework for vehicle-assisted collaborative edge computing where tasks from users can be offloaded to powerful ESs via potentially multi-hop transmissions. Under the proposed framework, we formulate an aggregated service throughput maximization problem by designing the task routing path subject to end-to-end latency requirements, spectrum, and computing resources. To efficiently address the curse of dimensionality problem due to vehicular mobility and channel variability, we develop a deep reinforcement learning, i.e., multi-agent deep deterministic policy gradient, based multi-hop task routing approach. Numerical results demonstrate that the proposed algorithm outperforms existing benchmark schemes.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0884.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
