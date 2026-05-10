---
id: paper-2905
title: Asynchronous Task Scheduling and Resource Allocation for UAV-Enabled Mobile Edge Computing Networks
authors:
- Zhang, Xiuling
- Jia, Riheng
- Yin, Quanjun
- Zheng, Zhonglong
- Li, Minglu
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2025.3645776
url: https://www.scopus.com/pages/publications/105025676014?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 167--180
keywords:
- asynchronous system operation
- Mobile edge computing
- multi-agent reinforcement learning
- resource allocation
- task scheduling
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

# paper-2905 — Asynchronous Task Scheduling and Resource Allocation for UAV-Enabled Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is promising in handling delay-sensitive or resource-intensive tasks in mobile internet. Existing system schedulers in MEC networks usually schedule all service providers in a synchronous manner, which may not suit the practical scenario where tasks are randomly generated and require different computational resources and service times. In this work, we jointly optimize the task scheduling and resource allocation in an unmanned aerial vehicle (UAV)-enabled MEC network, where multiple UAVs asynchronously and cooperatively deliver task offloading and computing services to edge devices (EDs), for maximizing the average per-UAV energy utility and minimizing the overall task missing ratio. To enhance scheduling efficiency and jointly optimize task scheduling and resource allocation, we develop an asynchronous layered multi-agent proximal policy optimization (AL-MAPPO) algorithm, by incorporating the multi-UAV asynchronous action execution mechanism and a discrete-continuous layered action space into the general MAPPO framework. AL-MAPPO enables each UAV to perform flexible task scheduling and fine-grained resource allocation asynchronously. Extensive trace-driven simulations based on Alibaba Cluster Data V2017 validate the effectiveness of AL-MAPPO, compared with several baseline algorithms. © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2905.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
