---
id: "paper-2879"
title: "Computational Resource Management of Edge Clouds for Vehicle-to-Network Services With Resource Limit"
authors: ["Yang, Lei", "Liu, Baochang", "Liu, Jinhui", "Guo, Wangyi", "Wu, Jiang", "Xu, Zhanbo", "Guan, Xiaohong"]
year: 2026
venue: "IEEE Transactions on Automation Science and Engineering"
venue_type: "journal"
doi: "10.1109/TASE.2026.3676133"
url: "https://www.scopus.com/pages/publications/105033691937?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "7379--7395"
keywords: ["edge computing", "Markov decision process", "Resource management", "service migration", "vehicle-to-network (V2N)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2879 — Computational Resource Management of Edge Clouds for Vehicle-to-Network Services With Resource Limit

## Metadata

- **Authors:** Yang, Lei and Liu, Baochang and Liu, Jinhui and Guo, Wangyi and Wu, Jiang and Xu, Zhanbo and Guan, Xiaohong
- **Year:** 2026
- **Venue:** IEEE Transactions on Automation Science and Engineering
- **DOI:** 10.1109/TASE.2026.3676133
- **URL:** https://www.scopus.com/pages/publications/105033691937?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 7379--7395
- **Language:** English
- **Keywords:** edge computing; Markov decision process; Resource management; service migration; vehicle-to-network (V2N)

### Abstract

This paper studies the online management of the computational resources between multiple edge clouds to minimize the operational cost for a vehicle-to-network (V2N) service provider, subject to stochastic trajectories of vehicles, the quality-of-service (QoS) and the resource limit. Due to the random mobility of vehicles, it poses challenges in real-time migration management when the computational capacity of each edge cloud and the stringent delay requirement of V2N services are both constrained, resulting in strong temporal-spatial coupling of the migration decisions. The problem could even be intractable to solve as the number of vehicles grows. To tackle these issues, we first propose a multi-layered cloud framework to gather and coordinate migration information between vehicles. Then, a multi-agent rollout with feasibility construction approach is developed, where the migration decision can be optimized sequentially for each vehicle based on the coordinated migration information from the central cloud. To handle the potentially infeasible solutions caused by the computational resource constraint, we propose a heuristic method to determine the migration priority at each overloading edge cloud, and an integer program is constructed that can be easily solved to produce feasible solutions. The numerical results show the efficiency of the proposed approach in both economical performance and computational complexity compared to the benchmarks. Note to Practitioners - This paper addresses an important practical problem of managing the computational resources of edge clouds to support delay-sensitive V2N services for a large number of vehicular clients for V2N service providers. Specifically, we propose an edge-based information framework where the computational data of V2N services can be migrated by virtual machines between edge computing facilities at eNodeBs. The practical difficulty lies in that the physical capacities of edge servers are limited, which couples the migration decision for each vehicle. Another issue is the strict delay requirement of the V2N service. Simply migrating the virtual machines near the vehicles would easily make edge clouds overloaded, and thus more complex migration strategies should be considered. To tackle these issues, we first relax the resource constraint and develop a multi-agent rollout algorithm based on a simple base policy. Then a priority-based heuristic with an integer problem is constructed to compute feasible decisions where the number of virtual machines has exceeded the capacity, and this can be easily solved by the mainstream commercial solvers. The numerical tests are based on the dataset collected from China Mobile Group. The proposed approach shows more than 10% savings over the base policy when the vehicle trajectories are random, and reduces the computing time by 60% when compared to the centralized method. However, practical experiments on the proposed approach has yet been tested. The future research would concentrate on the parallel computing algorithm for the virtual machine migration. © 2026 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
