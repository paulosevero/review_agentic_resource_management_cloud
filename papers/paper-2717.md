---
id: paper-2717
title: Distributed Diffusion Policy for Cooperative Resource Orchestration in IIoT Edge Networks
authors:
- Meng, Jiayi
- Rui, Lanlan
- Chen, Zixuan
- Yang, Yang
- Guo, Shaoyong
- Qiu, Xuesong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3660474
url: https://www.scopus.com/pages/publications/105029469352?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16722--16739
keywords:
- Diffusion model
- distributed reinforcement learning (RL)
- edge computing
- industrial Internet of Things (IIoT)
- resource orchestration
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

# paper-2717 — Distributed Diffusion Policy for Cooperative Resource Orchestration in IIoT Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid proliferation of industrial Internet of Things (IIoT) devices, massive delay-sensitive and computation-intensive (DSCI) tasks are generated. Traditional mobile edge computing (MEC) systems face limitations like intercell interference at cell edges, degrading quality of service (QoS). To address this, cooperative access edge networks (CAENs) enable dynamic access point (AP) clusters for enhanced transmission reliability in IIoT. However, challenges arise from multiuser interference, bandwidth contention, dynamic environments, and heterogeneous resources, complicating joint resource orchestration. This article proposes EdgeDiffuse, a diffusion-enhanced distributed resource orchestration algorithm, which optimizes task offloading selection, transmission power control, and computational resource allocation to minimize long-term task completion time while promoting system load balancing. EdgeDiffuse enables adaptive and hierarchical coordination between user agents and edge servers. It integrates diffusion models under a multiagent deep reinforcement learning (MADRL) framework for improved policy exploration in high-dimensional offloading decision spaces, and further uses convex optimization for server-side resource allocation. The experimental results demonstrate that EdgeDiffuse achieves 28.17% reduction in task completion time, 7.40% improvement in task transmission rates, and 15.71% enhancement in load balancing compared to advanced baselines, showcasing superior performance in multiuser and resource-constrained scenarios.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2717.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
