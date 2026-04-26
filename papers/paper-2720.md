---
id: "paper-2720"
title: "Joint edge offloading and resource provisioning for SLA-aware MEC: a two-timescale graph-attentive TD3 approach"
authors: ["Mohajer, Amin", "Mirzaei, Abbas", "Bavaghar, Maryam", "Darabi, Mostafa", "Fernando, Xavier"]
year: 2026
venue: "Wireless Networks"
venue_type: "journal"
doi: "10.1007/s11276-026-04117-3"
url: "https://www.scopus.com/pages/publications/105035298154?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Graph attention network (GAT)", "Multi-access edge computing (MEC)", "Resource provisioning", "SLA-aware orchestration", "Task offloading"]
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

# paper-2720 — Joint edge offloading and resource provisioning for SLA-aware MEC: a two-timescale graph-attentive TD3 approach

## Metadata

- **Authors:** Mohajer, Amin and Mirzaei, Abbas and Bavaghar, Maryam and Darabi, Mostafa and Fernando, Xavier
- **Year:** 2026
- **Venue:** Wireless Networks
- **DOI:** 10.1007/s11276-026-04117-3
- **URL:** https://www.scopus.com/pages/publications/105035298154?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Graph attention network (GAT); Multi-access edge computing (MEC); Resource provisioning; SLA-aware orchestration; Task offloading

### Abstract

SLA-aware multi-access edge computing (MEC) must jointly decide (i) how much radio/compute capacity to provision per region and (ii) where to execute each task (local edge, neighboring edge, or cloud) under bursty, non-stationary demand. These coupled decisions are difficult because the system is large-scale, partially observable, and has a continuous, high-dimensional action space (per-user bandwidth/CPU shares) while still requiring strict delay compliance. To address this challenge, we propose EdgeMind, a two-timescale orchestration framework. At the long timescale, a Transformer-based traffic predictor forecasts per-service demand and guides slice leasing (bandwidth and CPU) from the infrastructure provider to control cost while preventing congestion. At the short timescale, we design a graph-attentive multi-agent TD3 controller (TD3-GAT) that performs decentralized offloading and fine-grained resource provisioning using centralized training and decentralized execution. A GAT module encodes neighbor states and cooperation opportunities, while TD3’s twin critics and delayed policy updates stabilize learning in continuous control. In addition, we introduce a confidence-aware neighbor policy distillation term that transfers peer behaviors only when the estimated advantage is reliably positive, improving stability and sample efficiency in dense deployments. Extensive simulations in a realistic multi-edge setting with heterogeneous service profiles and non-stationary arrivals show that EdgeMind improves SLA satisfaction, reduces average completion delay, and increases service provider profit compared to representative baselines (DQN, greedy delay minimization, centralized DDPG with static slicing, and FC-MADDPG). © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.

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
