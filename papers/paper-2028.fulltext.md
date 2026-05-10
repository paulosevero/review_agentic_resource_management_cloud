---
title: LLM-based cost-aware task scheduling for cloud computing systems
authors:
  - name: Haoran Pei
    affiliation: School of Control and Computer Engineering, North China Electric Power University, Beijing, China
  - name: Yan Gu
    affiliation: School of Control and Computer Engineering, North China Electric Power University, Beijing, China
  - name: Yajuan Sun
    affiliation: Network and Information Office, North China Electric Power University, Beijing, China
  - name: Qingle Wang
    affiliation: School of Control and Computer Engineering, North China Electric Power University, Beijing, China
  - name: Cong Liu
    affiliation: NOVA Information Management School, Nova University of Lisbon, Lisbon, Portugal
  - name: Xiaomin Chen
    affiliation: Department of Computer Science, University of Reading, Reading, UK
  - name: Long Cheng
    affiliation: School of Control and Computer Engineering, North China Electric Power University, Beijing, China
abstract: |
  Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings.
keywords:
  - Cloud computing
  - Task scheduling
  - Deep reinforcement learning
  - Large language models
publication_date: 2025
license: Creative Commons Attribution 4.0 International License
---

## RESEARCH

## LLM-based cost-aware task scheduling for cloud computing systems

Haoran Pei 1 , Yan Gu 1 , Yajuan Sun 2\* , Qingle Wang 1 , Cong Liu 3 , Xiaomin Chen 4 and Long Cheng 1,2

## Abstract

Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings.

Keywords Cloud computing, Task scheduling, Deep reinforcement learning, Large language models

## Introduction

Cloud computing has emerged as a transformative paradigm that enables a wide range of users, including enterprises and individual developers, to access a shared pool of configurable computing resources such as servers, storage, and networks on an on-demand basis. These resources are dynamically allocated and virtualized, allowing for scalable, cost-effective, and flexible service delivery. With its inherent advantages in elasticity, reliability, scalability, and sustainability, cloud computing not only reduces capital and operational costs but also significantly simplifies system management and maintenance [1]. As a result, an increasing number of users are choosing to deploy their applications and services in cloud environments.]. As a result, an increasing number of users are choosing to deploy their applications and services in cloud environments.

\*Correspondence: Yajuan Sun syj@ncepu.edu.cn 1 School of Control and Computer Engineering, North China Electric Power University, Beijing, China 2 Network and Information Office, North China Electric Power University, Beijing, China 3 NOVA Information Management School, Nova University of Lisbon, Lisbon, Portugal

# Department of Computer Science, University of Reading, Reading, UK

<!-- image -->

Task scheduling plays a central role in cloud computing, as it determines how computational workloads are allocated across virtualized resources. An effective scheduling mechanism must maximize resource utilization, reduce operational expenses, and improve diverse Quality of Service (QoS) [2, 3]. However, meeting these objectives is complicated by the inherently dynamic and heterogeneous nature of cloud environments, which comprise virtual machines (VMs) with varying processing capabilities, fluctuating cost models, and irregular

© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s), and the source, provide a link to the original publication's license. For the full license text, see https://creativecommons.org/licenses/by/4.0/.

## Open Access

<!-- image -->

task arrival patterns [4-6]. Moreover, such variability often leads to resource contention and uneven load distribution, degrading system responsiveness and service reliability [2, 7]. Therefore, it is imperative to develop intelligent and adaptive scheduling strategies to ensure efficient and dependable cloud service delivery.

Traditional scheduling approaches, including heuristic and rule-based methods, frequently fall short in dynamic environments due to their inherent rigidity and inability to adapt swiftly to evolving workloads or unexpected changes in resource states [4]. Recently, deep reinforcement learning (DRL) has emerged as a promising alternative by enabling adaptive scheduling decisions through interactions with the environment [8, 9]. DRLbased scheduling has demonstrated substantial advantages, automatically learning near-optimal strategies to significantly improve metrics such as makespan, operational cost, and resource utilization compared to traditional heuristics [10, 11]. Despite these successes, DRL still faces critical limitations. First, training DRL models typically requires extensive computational resources and large volumes of interaction data, making it computationally expensive and impractical for rapid deployment [4]. Second, DRL schedulers are susceptible to overfitting to specific training scenarios, severely restricting their generalization to new or evolving environments [9]. Third, the performance of DRL models heavily depends on manually crafted reward functions, and inappropriate reward designs can lead to convergence to suboptimal solutions or slow convergence, limiting real-world applicability.

Recent advancements in large language models (LLMs) offer a complementary solution. Pretrained on vast text corpora, LLMs provide powerful semantic reasoning and deep contextual insight, enabling them to generate human-like heuristics and explanatory guidance for complex scheduling decisions [12-14]. However, standalone LLM-based scheduling solutions also face several challenges: their outputs may sometimes lack reliability, producing inaccurate or contextually inappropriate recommendations, thus undermining scheduling robustness [15]. Moreover, directly translating linguistic reasoning to actionable scheduling decisions or quantitative rewards remains non-trivial, limiting the direct applicability of purely LLM-based approaches [12, 13].

To address these challenges, we propose LarS, a cloud task scheduling framework that leverages an LLM as a high-level decision agent. In LarS, GPT-4o generates scheduling decisions with reasoning trajectories for given environments and states. Trained DRL agents evaluate these trajectories, and only the validated ones are retained to form a high-quality dataset. This dataset is then used to fine-tune the LLM via LoRA, enhancing its generalization capability and enabling optimization of cost and QoS across diverse cloud environments. In summary, the key contributions of this paper are as follows:

- We introduce LarS, an efficient framework that integrates LLM-based reasoning with DRL-based verification for intelligent cloud task scheduling.
- We propose a hybrid data generation pipeline where GPT-4o produces reasoning trajectories and DRL agents serve as evaluators to curate high-quality supervision data.
- We present the detailed design and implementation of LarS, and experimental results show that it outperforms existing approaches while maintaining strong generalization across diverse settings.

The remainder of this paper is organized as follows. Section 'Related work' reviews related work on cloud scheduling methods. Section 'System model and problem formulation' describes the system models and optimization objectives. Section 'The proposed LarS' details the design and implementation of LarS. Section 'Experiments evaluation' presents the experimental evaluation of LarS's performance, and Section 'Conclusion' concludes the paper.

## Related work

## Conventional methods for cloud task scheduling

Traditional scheduling approaches in cloud computing rely heavily on heuristic and meta-heuristic algorithms to find near-optimal solutions within reasonable time. Evolutionary algorithms and swarm intelligence techniques are prominent in this domain. For instance, Ismayilov and Topcuoglu propose a dynamic workflow scheduling method using a neural-network enhanced evolutionary algorithm to handle multiple objectives under changing conditions [16]. Similarly, Shukri et al. introduce an enhanced Multi-Verse Optimizer that significantly improves task scheduling performance in terms of makespan and resource utilization [17]. On the swarm intelligence side, researchers have leveraged algorithms like Particle Swarm Optimization and Whale Optimization. Nabi et al. present an adaptive PSO-based scheduling approach (AdPSO) which dynamically adjusts to workload changes, achieving better load balancing and reducing completion time [18]. Mangalampalli et al. propose a trust-aware task scheduler based on the Whale Optimization algorithm to jointly minimize execution time and SLA violations, demonstrating superior results over basic heuristics in cloud environments [19]. While these specialized solutions can optimize particular objectives, they typically focus on a restricted set of requirements; consequently, their performance may deteriorate when the cloud environment diverges from expected conditions or when additional objectives must be incorporated.

## DRL methods for cloud task scheduling

Deep reinforcement learning (DRL) has emerged as a promising approach for cloud task scheduling due to its ability to simultaneously optimize multiple objectives, including cost efficiency, makespan minimization, and QoS compliance [20]. Instead of relying on predefined heuristic rules, DRL-based schedulers can adapt to complex dynamics and optimize long-term rewards (such as response time or cost). Siddesha et al. propose a DRL scheme for cloud scheduling that learns to allocate tasks to VMs, yielding improvements in makespan and energy consumption compared to traditional algorithms [21]. In a similar vein, Islam et al. leverage deep Q-learning techniques to develop a scheduling policy for Spark jobs in cloud computing, achieving both performance gains and cost efficiency over baseline scheduling strategies [22]. Advanced variants of DRL have also been explored; for example, Xiu et al. introduce a meta-reinforcement learning framework (MRLCC) that enables a scheduler to quickly adapt to new cloud environments by learning a meta-policy, resulting in higher sample efficiency and robust performance across varying conditions [23].

These works illustrate that DRL approaches can dynamically learn from the cloud system's state and feedback, often outperforming static heuristics especially in

Table 1 Summary of cloud task scheduling methods and main

features large-scale or non-stationary cloud scenarios. However, current DRL approaches face several limitations. These include limited generalization across diverse scenarios, computationally expensive training procedures, and policies that are susceptible to overfitting. As a result, retraining is necessary when workload patterns or cloud configurations change [4]. Furthermore, DRL models often exhibit inadequate explainability, unpredictable worst-case behavior, and difficulties in optimally balancing multiple competing objectives, highlighting the need for more adaptive and robust scheduling paradigms that extend beyond conventional DRL methods.

| Reference | Method                          | Suc- cess rate | Generalization | Inter- pret- ability |
| --------- | ------------------------------- | -------------- | -------------- | -------------------- |
| [22]      | DQN+Policy Gradient             | ✓              | -              | -                    |
| [18]      | Adaptive PSO                    | ✓              | -              | -                    |
| [21]      | DQN+LSTM                        | ✓              | -              | -                    |
| [20]      | Deep Q-Learning                 | ✓              | -              | -                    |
| [17]      | Enhanced Multi-Verse Optimizer  | -              | -              | -                    |
| [16]      | NN-based Evolutionary Algorithm | ✓              | ✓              | -                    |
| [19]      | Whale Optimization              | ✓              | -              | -                    |
| [23]      | Meta Rein- forcement Learning   | ✓              | -              | -                    |
| [14]      | LLM-guided SARSA                | -              | -              | ✓                    |
| [24]      | LLM-assisted RL                 | ✓              | -              | -                    |
| LarS      | DQN+LLM                         | ✓              | ✓              | ✓                    |

## Large language models for cloud task scheduling

The rapid advancement of LLMs has created opportunities for addressing complex optimization problems, including scheduling tasks, by leveraging their powerful sequence modeling and reasoning capabilities. Recent studies demonstrate that LLMs, pretrained on extensive corpora, can effectively learn intricate scheduling constraints and objectives. For example, Abgaryan et al. [25] demonstrated that with minimal fine-tuning techniques like LoRA, LLMs achieve competitive performance on static job shop scheduling problems. Krishnamurthy and Shiva propose an LLM-guided approach using a SARSA reinforcement learning agent for dynamic task scheduling in the cloud [14]. Similarly, Tang et al. [24] developed a scheduling expert dataset to fine-tune a lightweight LLM for task assignment decisions in multi-cloud environments, showing that LLM-based agents can learn effective scheduling policies from expert demonstrations. However, current LLM-based schedulers primarily operate in offline or semi-static contexts, providing heuristic guidance or refining existing solutions rather than participating in the continuous, real-time decision-making required for dynamic cloud environments [26].

We summarize the related works mentioned above in Table 1. While task scheduling has been extensively studied, traditional heuristic methods often lack flexibility and adaptability to dynamic conditions. DRLbased schedulers, though adaptive, suffer from limited generalization and high computational costs. Existing LLM-driven approaches exhibit strong generalization capabilities, yet they have not fully demonstrated their potential in handling online adaptive scheduling scenarios with streaming workloads and evolving objectives. To remedy these shortcomings, this paper proposes LarS, an effective framework that leverages LLM as cloud task scheduling agent to achieve adaptive, explainable, and efficient cloud task scheduling.

Fig. 1 Task scheduling in cloud computing systems

<!-- image -->

## System model and problem formulation

This section presents the formal mathematical framework underlying our cost-aware cloud job scheduling methodology. We provide definitions of the cloud environment, job characteristics, VM configurations and the job scheduling strategy.

## The overall framework

We model a cloud computing environment comprising VMs analogous to commercial IaaS offerings (such as AWS EC2 instances and Google Compute Engine) that operate on a pay-as-you-go pricing model. In this environment, users submit computational jobs to applications hosted on these VMs, while the scheduling system dynamically allocates incoming jobs to suitable VMs for execution.

Fig. 1 illustrates the architecture of our cloud job scheduling framework. Upon job arrival from multiple application users, each job initially enters the scheduling portal, where it undergoes prompt engineering for proper input formatting and parameter extraction. Subsequently, an LLM combined with CoT reasoning executes decisionmaking to assign each job optimally to an appropriate VM. Each VM maintains a local queue and executes the assigned jobs following a first-come, first-served (FCFS) scheduling policy. The resource manager performs three key functions: processing job metadata, monitoring cloud resource pool status and tracking job execution states. For clarity of presentation, we summarize the key mathematical notations employed in our framework in Table 2.

Table 2 Notations used in our scheduling model

| Notation | Meaning                         |
| -------- | ------------------------------- |
| ID i     | The id of the -th job           |
| aT i     | The arrival time of the -th job |
