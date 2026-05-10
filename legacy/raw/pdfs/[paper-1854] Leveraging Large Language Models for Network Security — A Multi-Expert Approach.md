---
title: "Leveraging Large Language Models for Network Security: A Multi-Expert Approach"
authors:
  - Tianshun Lin
  - Changgui Xu
  - Jianshan Zhang
  - Nan Lin
  - Yuxin Liu
  - Yuanjun Zheng
affiliations:
  - "State Grid Putian Electric Power Supply Company, Putian, China"
  - "School of Information Science and Technology, ShanghaiTech University, Shanghai, China"
  - "School of Computer and Data Science, Minjiang University, Fuzhou, Fujian, China"
  - "State Grid Fuzhou Electric Power Supply Company, Fuzhou, China"
correspondence: "xuchg2022@shanghaitech.edu.cn"
received: "2025-02-15"
revised: "2025-02-27"
accepted: "2025-03-04"
keywords:
  - "deep reinforcement learning"
  - "industrial edge computing"
  - "large language models"
copyright: "©2025 John Wiley & Sons Ltd."
---

# Leveraging Large Language Models for Network Security: A Multi-Expert Approach

Tianshun Lin 1 | Changgui Xu 2 | Jianshan Zhang 3 | Nan Lin 1 | Yuxin Liu 1 | Yuanjun Zheng 4

# State Grid Putian Electric Power Supply Company, Putian, China | 2 School of Information Science and Technology, ShanghaiTech University, Shanghai, China | 3 School of Computer and Data Science, Minjiang University, Fuzhou, Fujian, China | 4 State Grid Fuzhou Electric Power Supply

Company, Fuzhou, China

Correspondence: Changgui Xu (xuchg2022@shanghaitech.edu.cn)

Received: 15 February 2025 | Revised: 27 February 2025 | Accepted: 4 March 2025

Funding: This research was supported by the Natural Science Foundation of Fujian Province, China (No. 2024J08277).

Keywords: deep reinforcement learning | industrial edge computing | large language models

## ABSTRACT

The optimization of diverse industrial edge computing tasks presents a significant challenge due to the dynamic and heterogeneous nature of industrial operational demands. While deep reinforcement learning (DRL) has shown promise, task-specific DRL models are often required in complex industrial edge networks, such as real-time anomaly detection and latency-sensitive decision-making, increasing computational overhead. This leads to large computational overheads, unstable performance, and increased energy consumption. Such a cost has become a concern in resource-limited industrial edge networks. In this paper, we propose a novel multi-expert optimization approach with the help of powerful large language models (LLMs). Our goals are to dynamically interpret industrial task requirements, activate specialized DRL experts, and synthesize their outputs into context-aware decisions. Specifically, we replace conventional gate networks with an LLM-based orchestrator. LLMs provide the benefits of semantic reasoning and contextual understanding when managing expert selection and collaboration. This approach eliminates the need to train unique DRL models for each industrial optimization task, thereby reducing deployment costs and improving scalability. Our experiments indicate that our approach achieves 13% higher anomaly detection accuracy when compared with traditional DRL methods.

## Introduction

The emergence of sixth-generation (6G) networks [1] rapidly changes industrial edge cloud infrastructures. It enables massive applications such as real-time device maintenance, autonomous, and latency-sensitive industrial automation. In particular, 6G networks promise ultra-reliable connectivity and intelligence. These characteristics support the industrial edge networks that connect smart factories, energy grids, and IoT ecosystems, where computational workloads are increasingly offloaded to resource-constrained edge nodes [2-5].

However, the heterogeneous and dynamic nature of industrial network security operations ranging from time-sensitive control to distributed anomaly detection in manufacturing pipelines needs adaptive optimizations. Those optimizations should be able to reconcile conflicting objectives like energy efficiency, computational scalability, and sub-millisecond latency [6].

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- While deep reinforcement learning (DRL) shows promise [7], task-specific customization (e.g., for real-time anomaly detection) often requires multiple DRL models, increasing computational costs [8].

©2025 John Wiley & Sons Ltd.

FIGURE 1 | Overview of our approach.

More precisely, a critical bottleneck lies in the cost of customization. Pre-trained DRL models often fail to generalize to new tasks. Hence, the adoption of new tasks requires retraining, which consumes multiple time cycles. For instance, a DRL policy optimized for real-time anomaly detection in DDoS defense may perform poorly when repurposed for dynamic resource allocation in multi-access edge computing (MEC) nodes [9, 10]. This limitation exacerbates computational overheads and constrains industrial AI deployments. Thus, we ask: how can industrial edge networks achieve adaptive optimizations without training task-specific DRL models?

Recent advances in multi-expert frameworks provide a promising path [11]. By coordinating specialized DRL models, each of which is fine-tuned for a specific task, these frameworks enable collaborative decision-making and avoid reliance on monolithic single-task AI systems. In particular, a gate network governs expert selection. However, its static training paradigm can hardly adapt to the dynamics of industrial edge networks, such as bursts in sensor data streams or ad-hoc IoT device deployments.

In response, we harness large language models (LLMs) to overcome the limitations of existing multi-expert frameworks (Figure 1). LLMs' semantic reasoning and contextual grounding perform well when parsing unstructured industrial security task requirements, for example, interpreting security logs, service-level agreements, or real-time traffic telemetry [7, 11]. Such capabilities allow LLMs to become a dynamic orchestrator that achieves adaptive and human-aligned decision-making in multi-expert systems.

### Contributions

This paper makes three contributions:

- We introduce a multi-expert approach tailored for industrial edge cloud networks. This approach enables DRL model coordination to address heterogeneous network security tasks without retraining.
- We design an LLM-based orchestrator that interprets operational constraints (e.g., energy budgets, latency thresholds) and dynamically assembles specialized DRL models.
- We validate our approach through an industrial case study of real-time anomaly detection. It achieves 13% higher accuracy over conventional DRL.

This paper is organized as follows. Section 2 illustrates our LLM-empowered multi-expert approach. Section 3 presents an industrial case study that uses and evaluates our approach. Section 4 concludes this paper and discusses future works.

## LLM-Empowered Multi-Expert Approach

In this section, we introduce the LLM-empowered multi-expert approach for network security tasks in industrial edge networks. We first formulate the problem of optimizing the deployment of an arbitrary network security task in each DRL model. Then we introduce our LLM-empowered multi-expert approach that assembles the decisions of multiple DRL experts via LLM orchestration to yield the optimal deployment decisions. Finally, we analyze the convergence of our approach. Table 1 summarizes the notation of symbols used by our paper.

### Problem Formulation

Consider a network security optimization task modeled as a Markov Decision Process (MDP) with:

- State space  = { /u1D460 1 , /u1D460 2 , . . . , /u1D460 /u1D441 } representing network conditions (e.g., data plane switch states, traffic loads).
- Action space  = { /u1D44E 1 , /u1D44E 2 , . . . , /u1D44E /u1D440 } denoting optimization decisions (e.g., switch resource allocation, variables deciding which switches to run which tasks, and traffic routing paths).
- Reward function /u1D445 ∶  ×  → ℝ mapping state-action pairs to quality of service (QoS) metrics.

The objective is to find an optimal policy /u1D70B ∗ ∶  →  that maximizes the expected discounted return:

where, /u1D6FE ∈ [ 0 , 1 ) is the discount factor.

### Multi-Expert Approach

#### Multiple Experts

Let { /u1D70B 1 , /u1D70B 2 , . . . , /u1D70B /u1D43E } denote /u1D43E specialized DRL experts, each trained for a distinct type of network security tasks with unique reward functions { /u1D445 1 , /u1D445 2 , . . . , /u1D445 /u1D43E } . For an input state /u1D460 /u1D461 , the k th expert produces action probabilities:

|

|                                               | State space representing network conditions (e.g., channel states, traffic loads)                                 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
|                                               | Action space denoting optimization decisions (e.g., power allocation, routing paths)                              |
| /u1D445 ( /u1D460, /u1D44E )                   | Reward function mapping state-action pairs to QoS metrics                                                         |
| /u1D6FE                                        | Discount factor for expected discounted return                                                                    |
| /u1D70B ∗                                      | Optimal policy maximizing /u1D53C [∑ ∞ /u1D461 = 0 /u1D6FE /u1D461 /u1D445 ( /u1D460 /u1D461 , /u1D44E /u1D461 )] |
| /u1D70B /u1D458                                | Specialized DRL expert policy for task /u1D458                                                                    |
| /u1D444 /u1D458 ( /u1D460, /u1D44E )           | Q -value estimate of expert /u1D458 for state-action pair ( /u1D460, /u1D44E )                                    |
| /u1D70F                                        | Temperature parameter in softmax action probability                                                               |
| /u1D443 /u1D458 ( /u1D44E \| /u1D460 /u1D461 ) | Action probability distribution from expert /u1D458 at state /u1D460 /u1D461                                      |
| Φ(  )                                         | Latent task requirements parsed from user input  by LLM                                                          |
| /u1D719 /u1D456                                | Semantic feature extracted from user input (e.g., latency, throughput)                                            |
| /u1D6FC /u1D458                                | Attention-based weight for expert /u1D458                                                                         |
| W /u1D6FC                                      | Learnable projection matrix for computing expert weights                                                          |
| /u1D713 /u1D458                                | Metadata of expert /u1D458 (e.g., task specialization, performance history)                                       |
| /u1D70B final                                  | Fused policy combining weighted expert outputs                                                                    |
| /u1D460 /u1D461                                | Current network state at time /u1D461                                                                             |
| /u1D44E /u1D461                                | Optimal action selected at time /u1D461                                                                           |
|                                               | User input describing task requirements (textual or structured)                                                   |
| /u1D443 /u1D461 - 1                            | Previous transmit power allocation                                                                                |
|  /u1D461 - 1                                  | Previous QoS metric (e.g., outage probability, data rate)                                                         |
| /u1D488 /u1D461                                | Wireless channel conditions at time /u1D461                                                                       |
| /u1D6FD 1 , /u1D6FD 2                          | Coefficients in NSP utility function (revenue vs. energy cost)                                                    |
|  min ,  max                                  | Minimum and maximum QoS bounds for constraints                                                                    |
| /u1D449 /u1D70B ( /u1D460 )                    | Value function representing expected return under policy /u1D70B at state /u1D460                                 |
| /u1D700                                        | Suboptimality bound of expert policies                                                                            |

where, /u1D444 /u1D458 ( /u1D460 /u1D461 , /u1D44E ) is the expert's Q -value estimate and /u1D70F is the temperature parameter.

#### LLM-Based Orchestration

The LLM orchestrates expert collaboration through three mathematical operations.

1. Objective parsing : For user input  , extract latent task requirements

where, /u1D719 /u1D456 represents semantic features (e.g., 'low latency' → /u1D719 latency ).

2. Expert weighting : Compute attention-based weights for experts

where, /u1D713 /u1D458 denotes expert k 's metadata and W /u1D6FC is a learnable projection matrix.

3. Decision fusion : Combine expert outputs through weighted voting

#### Optimization

Once the LLM completes its collaboration, our approach makes the optimal decisions based on the current state, user input, and expert policies. More precisely, given the input of current state /u1D460 /u1D461 , user input  , expert policies { /u1D70B /u1D458 } /u1D43E /u1D458 = 1 , our approach aims to produce the optimal action /u1D44E /u1D461 . Its workflow contains: (1) Parse requirements: Φ ← LLM (  ) . (2) Retrieve expert metadata { /u1D713 /u1D458 } /u1D43E /u1D458 = 1 . (3) Compute weights: /u1D6FC /u1D458 ← /u1D70E ( W /u1D6FC [ Φ; /u1D713 /u1D458 ]) . (4) Sample actions: /u1D44E /u1D458 ∼ /u1D70B /u1D458 ( ⋅ | /u1D460 /u1D461 ) . (5) Fuse decisions: /u1D44E /u1D461 = arg max /u1D44E ∑ /u1D43E /u1D458 = 1 /u1D6FC /u1D458 /u1D540 ( /u1D44E /u1D458 = /u1D44E ) .

#### Deployment

After solving the above problem, which maximizes the network service provider (NSP) utility, define: (1) State /u1D460 /u1D461 = ( /u1D443 /u1D461 -1 ,  /u1D461 -1 , /u1D488 /u1D461 ) ; (2) Action /u1D44E /u1D461 = /u1D443 /u1D461 ∈ { /u1D443 ( 1 ) , . . . , /u1D443 ( /u1D43F ) } ; (3) Reward /u1D445 ( /u1D460 /u1D461 , /u1D44E /u1D461 ) = /u1D6FD 1  (  /u1D461 ) -/u1D6FD 2 /u1D443 /u1D461 . The LLM resolves conflicting QoS requirements when deploying network security tasks through constrained optimization:

where,  min ,  max refer to the minimum and maximum QoS bounds for constraints.

This formulation enables automatic adaptation to novel requirements, like:

### Theoretical Analysis

Our approach's convergence follows from:

Theorem 1. For /u1D43E experts with ϵ -optimal policies , the fused policy satisfies :

Proof. Let Δ /u1D458 = /u1D449 /u1D70B final -/u1D449 /u1D70B /u1D458 . From Bellman equations:

The result follows from a convex combination of experts. ◽

Such convergence guarantees performance within bounded optimality loss.

## Industrial Case Study: Real-Time Anomaly Detection

In this section, we explain how to apply our approach in practical network security scenarios. Consider a mobile network in a factory where IoT sensors monitor vibrations, temperatures, and pressures in the data plane connecting 50 robotic assembly lines. These sensors periodically report these data to the control plane via mobile transmission. In this case, the industrial anomalies incurred by network security events such as DDoS attacks can be: (1) Type A : Sudden vibration spikes ( &gt; 15 g) indicating bearing failures. (2) Type B : Thermal gradients ( Δ /u1D447 &gt; 25 ˚ C ∕ min) indicating device overloads. (3) Type C : Pressure drops ( &lt; 0.8 /u1D443 nominal ) indicating pneumatic leaks. Our approach must detect the above anomalies within 50 ms latency to enable automated shutdowns, minimizing revenue loss. It operates as follows:

- Step 1 : Expert specialization:
- Step 2 : LLM orchestration:

- /u1D70B 1 ∶ Vibration pattern analysisviaLSTM-DQN

- /u1D70B 2 ∶ Thermaltransient modelingviaproximal policy optimization ( PPO )

- /u1D70B 3 ∶ Pressure dynamics trackingviaasynchronous advantage actor-critic ( A3C )

- Step 3 : Decision fusion

### Simulation

#### Setup

Then we conducted a simulation to evaluate the above approach. Our simulation was conducted in a server with 16 cores, with a 3.7 GHz clock speed, and 4 GB of RAM running Ubuntu 22.04.

TABLE 2 | Comparison of anomaly detection performance. Metric

| Metric                  | SingleDRL | Gate  | LLM(ours) |
| ----------------------- | --------- | ----- | --------- |
| Accuracy (%)            | 82.3      | 87.1  | 94.6      |
| F 1-score               | 0.791     | 0.841 | 0.927     |
| False positive rate (%) | 8.2       | 6.3   | 1.9       |
| Latency (ms)            | 41        | 53    | 38        |
| Energy (W)              | 18.7      | 22.4  | 15.2      |

For datasets, we choose a 6-month factory telemetry trace (1M samples) with 12 351 labeled anomalies:

Then for state representation /u1D460 /u1D461 and reward function /u1D445 ( /u1D460, /u1D44E ) in our approach, we employ the following general settings borrowed from prior studies:

For training parameters, we set (1) batch size: 512 sequences (128-time steps); (2) discount factor: /u1D6FE = 0.99; (3) LLM: GPT-4-1106-preview with 32k token context.

#### Numerical Results

Weuse our approach and comparison solutions to detect anomalies in our dataset. The comparison solutions comprise: (1) single DRL that uses a single DRL model to infer anomalies and (2) gate that coordinates multiple DRL-based expert models via the conventional gate network. Table 2 summarizes the performance of these solutions and our approach. It indicates that our approach achieves superior performance. The reasons are as follows: (1) The LLM correlates textual maintenance logs such as unusual noise with sensor patterns. Thus, it correctly increases vibration expert weighting from 0.41 to 0.79. (2) The experts for thermal and pressure collaborate when detecting Type B anomalies, for example, their joint contribution ( /u1D6FC 2 + /u1D6FC 3 = 0.63 ) during device overload events. (3) The LLM deactivates pressure experts during normal operation ( /u1D6FC 3 &lt; 0.1 ) . Thus, it reduces computation energy consumption by 19% when compared to static gate networks.

#### Ablation Study

Wefurther conduct an ablation study on our approach in Table 3. Wedisable some critical techniques used by our approach in this case study, including LLM parsing, expert fusion, and thermal expert. We also present the results when using static weights. The results indicate that (1) the 10.2% F 1-score drop when removing LLM parsing confirms its critical role for interpreting contextual

|

| Configuration | Full model | w/o LLMparsing | w/o Expert fusion | w/o Thermal expert | Static weights |
| ------------- | ---------- | -------------- | ----------------- | ------------------ | -------------- |
| F 1-score     | 0.927      | 0.841          | 0.782             | 0.901              | 0.813          |

cues and (2) the 15.5% drop when removing expert fusion highlights the necessity of dynamic collaboration between specialized models.

## Conclusion and Future Work

In this paper, we propose a novel LLM-empowered multi-expert approach. Our approach dynamically interprets industrial requirements in input tasks. It then activates specialized DRL experts and synthesizes context-aware decisions through semantic reasoning. By replacing conventional gate networks with an LLM-based orchestrator, our approach eliminates the need to train and deploy unique DRL models for every network security task. Experimental results indicate that our approach achieves 13% higher accuracy over single-task DRL baselines.

Our proposed LLM-driven multi-expert approach demonstrates significant promise for addressing security challenges in industrial edge networks. However, several open questions remain:

Leveraging in-network techniques . In recent years, the literature has proposed several in-network techniques by utilizing the powerful programming capabilities of data plane devices to offload traditional computation tasks. A typical example refers to network measurement, that is, building measurement data structures such as sketches inside switch ASIC pipelines to capture traffic dynamics [12-17]. We plan to update the substrate of industrial edge networks to further enhance security.

Federated learning for distributed intelligence . While the LLM centralizes expert orchestration, our future work plans to integrate federated learning into collaborative model training among distributed edge nodes [18-20]. This brings the benefits of improving data privacy, reducing communication costs, and handling device heterogeneity.

Energy-aware LLM optimization . While our approach reduces energy consumption when compared with traditional systems, LLM inference remains computationally intensive. Thus, our future work plans to explore LLM quantization, that is, using 4-bit quantized LLMs to reduce memory footprint, context window pruning, that is, dynamically pruning irrelevant historical contexts, and hardware-aligned sparsity, that is, exploiting NVIDIA Ampere architecture's 2:4 sparse tensor cores.

Ethical considerations . When we adopt LLMs, addressing emerging ethical challenges becomes critical. First, we should develop audit systems toward LLM decisions to prevent malicious or unsafe behaviors. Second, we also need to ensure fairness during expert selection in view of heterogeneous expert capabilities. We plan to explore these directions in our future work.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Peer Review

[The peer review history for this article is available at https://www. webofscience.com/api/gateway/wos/peer-review/10.1002/itl2.70016.](https://www.webofscience.com/api/gateway/wos/peer-review/10.1002/itl2.70016)

## References

1. S. Dang, O. Amin, B. Shihada, and M. S. Alouini, 'What Should 6G Be?,' Nature Electronics 3, no. 1 (2020): 20-29.
2. Z. Chen, J. Zhang, G. Min, Z. Ning, and J. Li, 'Traffic-Aware Lightweight Hierarchical Offloading Toward Adaptive Slicing-Enabled SAGIN,' IEEE Journal on Selected Areas in Communications 42, no. 12 (2024): 3536-3550.
3. J. Zhang, H. Luo, X. Chen, H. Shen, and L. Guo, 'Minimizing Response Delay in UAV-Assisted Mobile Edge Computing by Joint UAV Deployment and Computation Offloading,' IEEE Transactions on Cloud Computing 12, no. 4 (2024): 1372-1386.
4. J. Ali, S. K. Singh, W. Jiang, et al., 'A Deep Dive Into Cybersecurity Solutions for AI-Driven IoT-Enabled Smart Cities in Advanced Communication Networks,' Computer Communications 229 (2025): 108000, https://doi.org/10.1016/j.comcom.2024.108000.
5. H. A. Ammar, R. Adve, S. Shahbazpanahi, G. Boudreau, and K. V. Srinivas, 'User-Centric Cell-Free Massive MIMO Networks: A Survey of Opportunities, Challenges and Solutions,' IEEE Communication Surveys and Tutorials 24, no. 1 (2021): 611-652.
6. N. C. Luong, D. T. Hoang, S. Gong, et al., 'Applications of Deep Reinforcement Learning in Communications and Networking: A Survey,' IEEE Communication Surveys and Tutorials 21, no. 4 (2019): 3133-3174.
7. L. P. Kaelbling, M. L. Littman, and A. W. Moore, 'Reinforcement Learning: A Survey,' Journal of Artificial Intelligence Research 4 (1996): 237-285.
8. H. Du, R. Zhang, D. Niyato, et al., 'User-Centric Interactive AI for Distributed Diffusion Model-Based AI-Generated Content,' arXiv Preprint arXiv:2311.11094, 2023.
9. H. Du, J. Liu, D. Niyato, et al., 'Attention-Aware Resource Allocation and QoE Analysis for Metaverse xURLLC Services,' IEEE Journal on Selected Areas in Communications 41 (2023): 2158-2175.
10. D. H. Nguyen, Y. Zhang, and Z. Han, 'Contract-Based Spectrum Allocation for Wireless Virtualized Networks,' IEEE Transactions on Wireless Communications 17, no. 11 (2018): 7222-7235.
11. W. X. Zhao, K. Zhou, J. Li, et al., 'A Survey of Large Language Models,' arXiv Preprint arXiv:2303.18223, 2023.
12. X. Chen, Q. Xiao, H. Liu, et al., 'Eagle: Toward Scalable and Near-Optimal Network-Wide Sketch Deployment in Network Measurement,' in ACMSIGCOMMConference (ACM, 2024), 291-310.
13. Q. Huang, S. Sheng, X. Chen, et al., 'Toward Nearly-Zero-Error Sketching via Compressive Sensing,' in USENIX NSDI (USENIX, 2021), 1027-1044.

14. X. Chen, Q. Huang, P. Wang, et al., 'MTP: Avoiding Control Plane Overload With Measurement Task Placement,' in IEEE INFOCOM Conference (IEEE, 2021), 1-10.
15. X. Chen, H. Du, W. Liu, et al., 'Virtualizing Next-Generation Programmable Networks: Techniques, Use Cases, and Promising Future Directions,' IEEE Network (2024): 1-8.
16. X. Chen, C. Wu, X. Liu, et al., 'Empowering Network Security With Programmable Switches: A Comprehensive Survey,' IEEE Communication Surveys and Tutorials 25, no. 3 (2023): 1653-1704.
17. X. Chen, H. Liu, D. Zhang, et al., 'Empowering DDoS Attack Mitigation With Programmable Switches,' IEEE Network 37, no. 3 (2023): 112-117.
18. D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, and H. V. Poor, 'Federated Learning for Internet of Things: A Comprehensive Survey,' IEEE Communications Surveys &amp; Tutorials 23, no. 3 (2021): 1622-1658.
19. D. M. Manias and A. Shami, 'Making a Case for Federated Learning in the Internet of Vehicles and Intelligent Transportation Systems,' IEEE Network 35, no. 3 (2021): 88-94.
20. J. Liu, J. Huang, Y. Zhou, et al., 'From Distributed Machine Learning to Federated Learning: A Survey,' Knowledge and Information Systems 64, no. 4 (2022): 885-917.

24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
