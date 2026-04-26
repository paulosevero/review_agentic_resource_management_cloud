---
id: "paper-491"
title: "Distributed Training for Deep Learning Models On An Edge Computing Network Using Shielded Reinforcement Learning"
authors: ["Sen, Tanmoy", "Shen, Haiying"]
year: 2022
venue: "Proceedings - International Conference on Distributed Computing Systems"
venue_type: "conference"
doi: "10.1109/ICDCS54860.2022.00062"
url: "https://www.scopus.com/pages/publications/85140890520?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "581--591"
keywords: ["Deep learning", "Distributed cloud", "Edge computing", "Fertilizers", "Learning systems", "Multi agent systems", "Centralised", "Cluster nodes", "Cluster-heads", "Edge computing", "Edge nodes", "Learning models", "Multi-agent reinforcement learning", "Reinforcement learnings", "Resources utilizations", "Training time", "Reinforcement learning"]
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

# paper-491 — Distributed Training for Deep Learning Models On An Edge Computing Network Using Shielded Reinforcement Learning

## Metadata

- **Authors:** Sen, Tanmoy and Shen, Haiying
- **Year:** 2022
- **Venue:** Proceedings - International Conference on Distributed Computing Systems
- **DOI:** 10.1109/ICDCS54860.2022.00062
- **URL:** https://www.scopus.com/pages/publications/85140890520?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 581--591
- **Language:** English
- **Keywords:** Deep learning; Distributed cloud; Edge computing; Fertilizers; Learning systems; Multi agent systems; Centralised; Cluster nodes; Cluster-heads; Edge computing; Edge nodes; Learning models; Multi-agent reinforcement learning; Reinforcement learnings; Resources utilizations; Training time; Reinforcement learning

### Abstract

With the emergence of edge devices along with their local computation advantage over the cloud, distributed deep learning (DL) training on edge nodes becomes promising. In such a method, the cluster head of a cluster of edge nodes schedules all the DL training jobs from the cluster nodes. Using such a centralized scheduling method, the cluster head knows all the loads of the cluster nodes, which can avoid overloading the cluster nodes, but the head itself may become overloaded. To handle this problem, we first propose a multi-agent RL (MARL) system that enables each edge node to schedule its own jobs using RL. However, without the coordination between the nodes, action collision may occur, in which multiple nodes may schedule tasks to the same node and make it overloaded. To avoid these problems, we propose a system called Shielded ReinfOrcement learning (RL) based DL training on Edges (SROLE). In SROLE, each edge node schedules its own jobs using multi-agent RL. The shield deployed in a node checks action collisions and provides alternative actions to avoid the collisions. As the central shield node for the entire cluster may become a bottleneck, we further propose a decentralized shielding method, in which different shields are responsible for different regions in the cluster and they coordinate to avoid action collisions on the region boundaries. Our container-based emulation experiments show that SROLE reduces training time by up to 59% with 29% lower median resource utilization and reduces the number of action collisions by up to 48% compared to multi-agent RL and the centralized RL. Our real device experiments show that SROLE still reduces the training time by up to 53% with 28% lower median resource utilization than multi-agent RL and the centralized RL.  © 2022 IEEE.

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
