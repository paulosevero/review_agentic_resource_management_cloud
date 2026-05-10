---
id: paper-2879
title: Computational Resource Management of Edge Clouds for Vehicle-to-Network Services With Resource Limit
authors:
- Yang, Lei
- Liu, Baochang
- Liu, Jinhui
- Guo, Wangyi
- Wu, Jiang
- Xu, Zhanbo
- Guan, Xiaohong
venue: IEEE Transactions on Automation Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TASE.2026.3676133
url: https://www.scopus.com/pages/publications/105033691937?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7379--7395
keywords:
- edge computing
- Markov decision process
- Resource management
- service migration
- vehicle-to-network (V2N)
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

# paper-2879 — Computational Resource Management of Edge Clouds for Vehicle-to-Network Services With Resource Limit

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper studies the online management of the computational resources between multiple edge clouds to minimize the operational cost for a vehicle-to-network (V2N) service provider, subject to stochastic trajectories of vehicles, the quality-of-service (QoS) and the resource limit. Due to the random mobility of vehicles, it poses challenges in real-time migration management when the computational capacity of each edge cloud and the stringent delay requirement of V2N services are both constrained, resulting in strong temporal-spatial coupling of the migration decisions. The problem could even be intractable to solve as the number of vehicles grows. To tackle these issues, we first propose a multi-layered cloud framework to gather and coordinate migration information between vehicles. Then, a multi-agent rollout with feasibility construction approach is developed, where the migration decision can be optimized sequentially for each vehicle based on the coordinated migration information from the central cloud. To handle the potentially infeasible solutions caused by the computational resource constraint, we propose a heuristic method to determine the migration priority at each overloading edge cloud, and an integer program is constructed that can be easily solved to produce feasible solutions. The numerical results show the efficiency of the proposed approach in both economical performance and computational complexity compared to the benchmarks. Note to Practitioners - This paper addresses an important practical problem of managing the computational resources of edge clouds to support delay-sensitive V2N services for a large number of vehicular clients for V2N service providers. Specifically, we propose an edge-based information framework where the computational data of V2N services can be migrated by virtual machines between edge computing facilities at eNodeBs. The practical difficulty lies in that the physical capacities of edge servers are limited, which couples the migration decision for each vehicle. Another issue is the strict delay requirement of the V2N service. Simply migrating the virtual machines near the vehicles would easily make edge clouds overloaded, and thus more complex migration strategies should be considered. To tackle these issues, we first relax the resource constraint and develop a multi-agent rollout algorithm based on a simple base policy. Then a priority-based heuristic with an integer problem is constructed to compute feasible decisions where the number of virtual machines has exceeded the capacity, and this can be easily solved by the mainstream commercial solvers. The numerical tests are based on the dataset collected from China Mobile Group. The proposed approach shows more than 10% savings over the base policy when the vehicle trajectories are random, and reduces the computing time by 60% when compared to the centralized method. However, practical experiments on the proposed approach has yet been tested. The future research would concentrate on the parallel computing algorithm for the virtual machine migration. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2879.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
