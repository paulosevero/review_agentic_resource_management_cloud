---
id: "paper-2434"
title: "Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning"
authors: ["Zhang, Jiaqiang", "Yu, Xianjia", "Westerlund, Tomi"]
year: 2025
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s25165067"
url: "https://www.scopus.com/pages/publications/105014289956?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["edge computing", "Kubernetes", "LSTM", "multi-robot relative position", "ROS 2", "UWB"]
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

# paper-2434 — Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning

## Metadata

- **Authors:** Zhang, Jiaqiang and Yu, Xianjia and Westerlund, Tomi
- **Year:** 2025
- **Venue:** Sensors
- **DOI:** 10.3390/s25165067
- **URL:** https://www.scopus.com/pages/publications/105014289956?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; Kubernetes; LSTM; multi-robot relative position; ROS 2; UWB

### Abstract

ROS (Robot Operating System) has become the de facto standard in robotics research and development, with ROS 2, in particular, offering enhanced support for real-time communication, distributed systems, and scalable multi-robot applications. These capabilities have driven its widespread adoption across academia, industry, and the open-source community. However, deploying ROS 2 applications across heterogeneous hardware platforms remains a complex task—especially in scenarios that require tightly coordinated, multi-agent systems. In such cases, the failure of a single agent can propagate disruptions throughout the system. A representative example is Ultra-wideband (UWB)-based multi-robot relative localization, where inter-robot dependencies are essential for maintaining accurate relative positioning. While Kubernetes offers powerful features for automated deployment and orchestration, its integration with ROS 2 has not yet been thoroughly evaluated within the context of specific robotic applications. This paper addresses this gap by integrating Kubernetes with ROS 2 in a UWB-based multi-robot localization system, using UWB ranging error mitigation as a representative application. An edge cluster comprising five NVIDIA Jetson Nano devices and one laptop is orchestrated using Kubernetes, with a Jetson Nano node mounted on each robot. We deploy Long Short-Term Memory (LSTM)-based error mitigation modules on the edge nodes and systematically induce failures in various combinations of these modules. The system’s resilience and robustness are then assessed by analyzing position errors under different failure scenarios. © 2025 by the authors.

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
