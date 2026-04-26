---
id: "paper-942"
title: "EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning"
authors: ["Hao, Yijun", "Yang, Shusen", "Li, Fang", "Zhang, Yifan", "Wang, Shibo", "Ren, Xuebin"]
year: 2024
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM52122.2024.10621305"
url: "https://www.scopus.com/pages/publications/85201792059?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "671--680"
keywords: ["adaptive timescales", "Mobile edge computing", "reinforcement learning", "resource scheduling"]
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

# paper-942 — EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning

## Metadata

- **Authors:** Hao, Yijun and Yang, Shusen and Li, Fang and Zhang, Yifan and Wang, Shibo and Ren, Xuebin
- **Year:** 2024
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM52122.2024.10621305
- **URL:** https://www.scopus.com/pages/publications/85201792059?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 671--680
- **Language:** English
- **Keywords:** adaptive timescales; Mobile edge computing; reinforcement learning; resource scheduling

### Abstract

In mobile edge computing (MEC), resource scheduling is crucial to task requests' performance and service providers' cost, involving multi-layer heterogeneous scheduling decisions. Existing schedulers typically adopt static timescales to regularly update scheduling decisions of each layer, without adaptive adjustment of timescales for different layers, resulting in potentially poor performance in practice.We notice that the adaptive timescales would significantly improve the trade-off between the operation cost and delay performance. Based on this insight, we propose EdgeTimer, the first work to automatically generate adaptive timescales to update multi-layer scheduling decisions using deep reinforcement learning (DRL). First, EdgeTimer uses a three-layer hierarchical DRL framework to decouple the multi-layer decision-making task into a hierarchy of independent sub-tasks for improving learning efficiency. Second, to cope with each sub-task, EdgeTimer adopts a safe multi-agent DRL algorithm for decentralized scheduling while ensuring system reliability. We apply EdgeTimer to a wide range of Kubernetes scheduling rules, and evaluate it using production traces with different workload patterns. Extensive trace-driven experiments demonstrate that EdgeTimer can learn adaptive timescales, irrespective of workload patterns and built-in scheduling rules. It obtains up to 9:1 more profit than existing approaches without sacrificing the delay performance. © 2024 IEEE.

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
