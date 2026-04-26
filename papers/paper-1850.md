---
id: "paper-1850"
title: "Federated Slicing Resource Management in Edge Computing Networks based on GAN-assisted Multi-Agent Reinforcement Learning; [基于生成对抗网络辅助多智能体强化学习的边缘计算网络联邦切片资源管理]"
authors: ["Lin, Yan", "Xia, Kaiyuan", "Zhang, Yijin"]
year: 2025
venue: "Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology"
venue_type: "journal"
doi: "10.11999/JEIT240773"
url: "https://www.scopus.com/pages/publications/105002050980?origin=resultslist"
publisher: "Science Press"
pages: "666--677"
keywords: ["Edge Computing (EC)", "Federated Learning (FL)", "Generative Adversarial Network (GAN)", "Multi-Agent Reinforcement Learning (MARL)", "Network Slicing"]
language: "Chinese"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-1850 — Federated Slicing Resource Management in Edge Computing Networks based on GAN-assisted Multi-Agent Reinforcement Learning; [基于生成对抗网络辅助多智能体强化学习的边缘计算网络联邦切片资源管理]

## Metadata

- **Authors:** Lin, Yan and Xia, Kaiyuan and Zhang, Yijin
- **Year:** 2025
- **Venue:** Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
- **DOI:** 10.11999/JEIT240773
- **URL:** https://www.scopus.com/pages/publications/105002050980?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 666--677
- **Language:** Chinese
- **Keywords:** Edge Computing (EC); Federated Learning (FL); Generative Adversarial Network (GAN); Multi-Agent Reinforcement Learning (MARL); Network Slicing

### Abstract

Objective To meet the differentiated service requirements of users in dynamic Edge Computing (EC) network scenarios, network slicing technology has become a crucial enabling approach for EC networks to offer differentiated edge services. It facilitates flexible allocation and customized management of communication and computation resources by dividing network resources into multiple independent sub-slices. However, traditional slicing resource management methods cannot handle the time-varying wireless channel conditions and the randomness of service arrivals in EC networks. Additionally, existing intelligent slicing resource management schemes based on deep reinforcement learning face challenges, including the need for extensive information sharing, privacy leakage, and unstable training convergence. To address these challenges, the integration of Multi-Agent Reinforcement Learning (MARL) and Federated Learning (FL) allows for experience sharing among agents while protecting users’ privacy. Furthermore, Generative Adversarial Network (GAN) is used to generate state-action value distributions, improving the ability of traditional MARL methods to learn state-value information. By modeling the joint bandwidth and computing slicing resource management optimization problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP), collaborative decision-making for slicing resource management is achieved by sharing only the generator network parameters of each agent through the combination of FL and GAN. This study provides a federated collaborative decision-making framework for addressing the slicing resource management problem in EC scenarios and offers theoretical support for enhancing the utilization efficiency of edge slicing resources while preserving users’ privacy. Methods The core concept of the proposed federated slicing resource management scheme is to first employ both GAN technology and the D3QN algorithm for local training within a multi-agent framework. The FL architecture is then used to share the generator network parameters of each agent, facilitating collaborative decision-making for joint bandwidth and computing slicing resource management. In this approach, each Access Point (AP) agent collects data on the total number of tasks to be transmitted and the number of Central Processing Unit (CPU) cycles required for computing tasks in each associated slice as local observations during each training time slot. Each agent subsequently selects the optimal local bandwidth and computing resource management action, obtaining the system reward, which consists of the average service waiting delay and service satisfaction rate, as well as the observation for the next time slot to train the local network. During the training process, each AP agent maintains its own main generator network, target generator network, and discriminator network. In each training episode, the D3QN algorithm is applied to decompose the state-action values, and GAN is used to perform multi-modal learning of the state value distribution, thus completing the local training. After each training episode, the AP agents upload their main generator network parameters for federated aggregation and receive the global main generator network parameters for the next training episode. Results and Discussions By employing the D3QN algorithm and integrating the advantages of GAN within the MARL framework, alongside leveraging FL to share learning experiences among agents while protecting users’ privacy, the proposed scheme reduces the long-term service waiting delay and improves the long-term average service satisfaction rate. Simulation results demonstrate that the proposed scheme achieves the highest average cumulative reward after approximately 500 episodes (Fig. 3), with a notable improvement of at least 10% in convergence performance compared to the baselines. Furthermore, the scheme strikes a better balance between average service waiting delay and average service satisfaction rate (Fig. 4). Additionally, it delivers superior performance in terms of user average service satisfaction rate, with at least an 8% improvement under varying user numbers (Fig. 5), highlighting its effectiveness in resource management under different task loads. Moreover, the proposed scheme reduces the average service waiting delay by at least 28% (Fig. 6) under varying numbers of agents. Conclusions This paper investigates the joint bandwidth and computing slicing resource management problem in dynamic, unknown EC network scenarios and proposes a federated slicing resource management scheme based on GAN-assisted MARL. The proposed scheme enhances the agents’ ability to learn state-value information and promotes collaborative learning by sharing the training network parameters of agents, which ultimately reduces long-term service waiting delays and improves long-term average service satisfaction rates, while protecting users’ privacy. Simulation results show that: (1) The cumulative reward convergence performance of the proposed scheme improves by at least 10% compared to the baselines; (2) The average service satisfaction rate of the proposed scheme is more than 8% higher than that of the baselines under varying user numbers; (3) The average service waiting delay of the proposed scheme is reduced by at least 28% compared to the baselines under varying agent numbers. However, this study only considers ideal, static user scenarios and interference-free communication conditions. Future work should incorporate more real-world dynamics, such as time-varying user mobility and complex multi-user interference. © 2025 Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Federated Slicing Resource Management in Edge Computing Networks based on GAN-assisted Multi-Agent Reinforcement Learning; [基于生成对抗网络辅助多智能体强化学习的边缘计算网络联邦切片资源管理]

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Federated Slicing Resource Management in Edge Computing Networks based on GAN-assisted Multi-Agent Reinforcement Learning; [基于生成对抗网络辅助多智能体强化学习的边缘计算网络联邦切片资源管理]
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Federated Slicing Resource Management in Edge Computing Networks based on GAN-assisted Multi-Agent Reinforcement Learning; [基于生成对抗网络辅助多智能体强化学习的边缘计算网络联邦切片资源管理]
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
