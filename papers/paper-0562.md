---
id: paper-0562
title: Joint Edge Computing and Caching Based on D3QN for the Internet of Vehicles
authors:
- Chen, Geng
- Sun, Jingli
- Zeng, Qingtian
- Jing, Gang
- Zhang, Yudong
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12102311
url: https://www.scopus.com/pages/publications/85160651815?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- cache
- Dueling Double Deep Q Network (D3QN)
- edge computing
- offloading
- revenue
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0562 — Joint Edge Computing and Caching Based on D3QN for the Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the Internet of Vehicles (IOV), a lot of self-driving vehicles (SDVs) need to handle a variety of tasks but have very seriously limited computing and storage resources, meaning they cannot complete intensive tasks timely. In this paper, a joint edge computing and caching based on a Dueling Double Deep Q Network (D3QN) is proposed to solve the problem of the multi-task joint edge calculation and caching process. Firstly, the processes of offloading tasks and caching them to the base station are modeled as optimization problems to maximize system revenues, which are limited by system latency and energy consumption as well as cache space for computing task constraints. Moreover, we also take into account the negative impact of the number of unfinished tasks in relation to the optimization problem—the higher the number of unfinished tasks, the lower the system revenue. Secondly, we use the D3QN algorithm together with the cache models to solve the formulated NP-hard problem and select the optimal caching and offloading action by adopting an e-greedy strategy. Moreover, two cache models are proposed in this paper to cache tasks, namely the active cache, based on the popularity of the task, and passive cache, based on the D3QN algorithm. Additionally, tasks which deal with cache space are updated by computing the expulsion value based on type of popularity. Finally, simulation results show that the proposed algorithm has good performance in terms of the latency and energy consumption of the system and that it improves utilization of cache space and reduces the probability of unfinished tasks. Compared to the Deep Q Network with caching policy, with the Double Deep Q Network with caching policy and Dueling Deep Q Network with caching policy, the system revenue of the proposed algorithm is improved by 65%, 35% and 66%, respectively. The scenario of the IOV proposed in this article can be expanded to larger-scale IOV systems by increasing the number of SDVs and base stations, and the content caching and download functions of the Internet of Things can also be achieved through collaboration between multiple base stations. However, only the cache model is focused on in this article, and the design of the replacement model is not good enough, resulting in a low utilization of cache resources. In future work, we will analyze how to make joint decisions based on multi-agent collaboration for caching, offloading and replacement in IOV scenarios with multiple heterogeneous services to support different Vehicle-to-Everything services. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0562.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
