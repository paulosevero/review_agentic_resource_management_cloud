---
title: Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented Generation
authors: Xiongjie Zhou, Xin Guan, Ning Wang, Hongyang Chen, Tomoaki Ohtsuki, and Yan Zhang
date: 2024
keywords:
  - task offloading
  - edge computing
  - retrieval-augmented generation
  - Internet of Energy
  - resource allocation
---

## Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented Generation

[Image]

[Image]

Xiongjie Zhou , Xin Guan , Ning Wang, Hongyang Chen , Tomoaki Ohtsuki , and Yan Zhang

## Abstract

Traditional task offloading in Internet of Energy (IoE) edge environments struggles to accommodate heterogeneous user tasks and dynamic system conditions. Although Large Language Models (LLMs) offer potential solutions, their deployment is hindered by the dynamic resource constraints and stringent Quality of Service (QoS) requirements of IoE. Retrieval-augmented generation (RAG) enables LLM to overcome these limitations. In this paper, we propose an RAGempowered adaptive task offloading framework. First, the framework transforms raw IoE-collected data into LLM-comprehensible textual inputs. Second, we design an intelligent preference-matching module that guides RAG to retrieve relevant knowledge and cases using key QoS features. Third, we build a composite knowledge vector database with both positive and negative experiences. We introduce a failure severity value to quantify the importance of counterexamples and enhance decision-making robustness. Finally, we design a hybrid knowledge prompt generation module. It utilizes a hierarchical filtering strategy and optimizes the ranking of retrieved knowledge for comprehensive prompts. Experimental results demonstrate that our proposed framework significantly outperforms baselines, increasing cumulative reward by 48.4% while reducing latency and energy consumption by 44.8% and 50.9%, respectively.

## IntroductIon

With the rapid development of the Internet of Energy (IoE), the energy system is undergoing a key transformation [1]. IoE integrates energy production, consumption, and communication for multi-energy complementarity and efficient coordination [2]. However, IoE faces challenges from massive heterogeneous data and complex computing tasks, overburdening traditional cloud architectures. Edge computing (EC) is a key technology addressing these challenges. EC moves resources closer to the network edge, reducing data transmission latency and improving system responsiveness. Task offloading is a critical EC technique. It transfers tasks from user devices to edge servers, ensuring efficient resource allocation and performance.

[Image]

[Image]

[Image]

However, existing artificial intelligence-based task offloading struggles with key IoE challenges. First, dynamic and heterogeneous environments lead to constantly changing resources and network conditions [3]. This challenges static or rule-based offloading strategies. Second, diverse user tasks have differentiated quality of service (QoS) requirements, including latency, energy, and security. This diversity makes it difficult for a single optimization objective to suit all scenarios, resulting in a lack of fine-grained adaptability [4]. Finally, achieving an optimal balance among multiple conflicting QoS objectives, while ensuring real-time and accurate decision-making, remains a critical and unresolved problem [5].

Large language model (LLM) has demonstrated strong capabilities in language understanding and reasoning by learning rich world knowledge from large-scale text corpora. However, applying LLM directly to task offloading in the IoE remains challenging due to hallucination issues, lack of real-time data support, and limitations in interpreting domain-specific numerical information. Retrieval-augmented generation (RAG) is a promising solution [6]. RAG integrates updatable knowledge into the LLM inference process. This enhances access to accurate, real-time domain knowledge [7]. It also improves reasoning accuracy and interpretability. In task offloading, RAG enables the LLM to perceive network states and historical knowledge. This supports timely and reliable decision-making.

RAG-empowered LLMs show great potential for IoE offloading. However, several challenges persist [8]. First, converting heterogeneous states into LLM-interpretable inputs is non-trivial. Second, achieving accurate and QoS-aware knowledge retrieval under diverse and time-varying conditions is difficult. Third, constructing a knowledge base that accumulates experience and quantifies failure severity to improve robustness remains challenging. Finally, efficient retrieval of both positive and negative historical experiences is essential to improve decision accuracy and professionalism.

To address these challenges, this paper proposes an RAG-empowered adaptive task

Xiongjie Zhou and Xin Guan (corresponding author) are with the School of Computer and Big Data, Heilongjiang University, Harbin 150080, China; Ning Wang is with State Grid Heilongjiang Electric Power Company Ltd., Harbin 150080, China; Hongyang Chen is with Zhejiang Laboratory, Hangzhou, Zhejiang 311121, China; Tomoaki Ohtsuki is with the Department of Information and Computer Science, Keio University, Yokohama 223-8522, Japan; Yan Zhang is with the School of Information and Communication Engineering, University of Electronic Science and Technology of China, Chengdu 611731, China.

Digital Object Identifier: 10.1109/MNET.2026.3665502

offloading framework in EC for the IoE. The framework efficiently transforms dynamic data into LLM-understandable inputs. It incorporates a novel hybrid retrieval mechanism. This matches positive and negative historical experiences precisely. This design enables LLM to generate professional, reliable, and risk-aware strategies. The main contributions are as follows.

1. In this paper, we propose an RAG-empowered adaptive task offloading framework for the IoE. The framework converts numerical environment states and task demands into LLM-comprehensible semantic inputs, thereby enabling sophisticated reasoning and intelligent decision-making.
2. We design an intelligent preference-aware retrieval module. It integrates semantic similarity between knowledge entries, contextual queries, and task QoS preferences. This module prioritizes knowledge aligned with task requirements to enhance retrieval accuracy and system adaptability in dynamic, heterogeneous environments.
3. Our proposed composite knowledge base incorporates both positive and negative experiences, utilizing a novel failure severity metric to quantify negative cases. This mechanism enhances decision-making robustness by guiding the LLM to avoid high-risk strategies.
4. We develop a hybrid prompt generation module that employs hierarchical filtering and dual-ranking strategies for positive and negative cases. By optimizing knowledge ranking based on relevance and failure severity, the module constructs comprehensive prompts that yield reliable offloading decisions.

The rest of this paper is organized as follows. The section 'Related Work' details the application and latest progress of RAG technology in the IoE. The section 'RAG-Empowered Adaptive Task Offloading Framework' presents the proposed RAG-empowered adaptive task offloading framework, and its core modules. The section 'Performance Evaluation' presents the experiment design and performance evaluation results. Finally, section 'Conclusion and Future Work' summarizes the work and outlines future research directions.

## relAted Work

RAG effectively addresses the limitations of LLMs in accessing real-time and domain-specific knowledge. Huang et al. [6] propose a 6G-oriented RAG deployment framework to enhance service quality via data fusion and dynamic knowledge base management. However, the real-time integration of heterogeneous multi-source data for knowledge base updates remains challenging. Ouyang et al. [9] propose an adaptive RAG framework, balancing LLM quality and latency in edge environments. This uses multi-level retrievers and online optimization. Managing this complexity may introduce considerable system overhead. Liu et al. [10] propose an adaptive context caching framework using deep reinforcement learning (DRL). It improves cache hit rates and reduces retrieval latency. However, its performance highly depends on accurate user demand prediction. Alabbasi et al. [7] propose a telecom RAG system using a two-stage retriever. It enhances context retrieval and open-domain query performance. Handling ultra-long contexts still poses computational challenges on edge devices.

The integration of RAG has emerged as a promising approach to enhance LLM-based decision-making in complex task offloading scenarios. He et al. [11] utilized active reasoning with reward-free guidance to optimize LLM-based offloading, though its generalization in volatile IoE environments remains unverified. Zeeshan et al. [8] propose an RAG framework that integrates LLM with domain knowledge such as wireless standards and research publications to achieve resource optimization in 6G and future networks. Challenges persist, including real-time knowledge base updates and unbiased retrieval. Mitigating LLM hallucinations also remains unresolved. Zhang et al. [12] propose an interactive AI framework that includes pluggable LLM and RAG modules for constructing knowledge bases and contextual memory. It supports optimization problem design in next-generation networks. However, it faces computational overhead and real-time efficiency bottlenecks in large-scale scenarios.

Although existing studies have made significant progress in applying LLM to task offloading, several critical challenges remain.

- Low Robustness: Most methods still lack generalizability and robustness when deployed in complex and dynamic edge environments.
- Retrieval Inaccuracy: Retrieval timeliness and accuracy are insufficient. This leads to information staleness and potential LLM biases.
- Static Knowledge: Knowledge base construction and dynamic updating require further exploration.

To bridge these gaps, we propose an RAGempowered adaptive task offloading framework. Unlike prior works, our framework integrates numerical-to-semantic conversion, QoS-aware matching, and a failure-aware composite knowledge base to ensure precise, risk-aware, and robust decision-making in the IoE.

## rAG-empoWered AdAptIve tAsk offloAdInG frAmeWork

We propose an innovative RAG-empowered adaptive task offloading framework. As illustrated in Fig. 1, it adopts a modular design. This framework integrates LLM reasoning with RAG knowledge enhancement to address IoE dynamic challenges. This facilitates intelligent strategy generation. The system uses a centralized edge intelligence architecture. The RAG-LLM module is deployed on a centralized edge server. It generates and distributes strategies to local EC servers time-slottedly. In this architecture, communication between the EC server and user equipment relies on wireless links, while communication between EC servers uses wired connections. Existing studies have shown that the communication overhead between edge servers negligible in most task offloading scenarios [13].

The framework's operation proceeds as follows: We first convert real-time environmental states, task parameters, and QoS preferences into a semantic query text, Q . Leveraging a pre- constructed vectorized knowledge base containing fundamental knowledge and historical cases, the system then performs QoS-aware relevance matching to retrieve the most pertinent base knowledge, successful (Positive), and failed (Negative) historical cases. These retrieved texts are structured and integrated with Q to form a comprehensive contextual prompt, P . This P is fed into the LLM, which analyzes the scenario and contextual knowledge to output the optimal offloading strategy S (including selection, resource allocation, and power control) and its interpretable rationale R . Finally, after execution, the system monitors outcomes and evaluates the failure degree. The execution context and performance feedback update the knowledge base.

FIGURE 1. RAG-empowered adaptive task offloading framework in EC for the IoE.

[Image]

The four key innovative modules of our framework are detailed below.

## IntellIGent context-AWAre Query GenerAtIon module

In the IoE, EC environments continuously generate massive heterogeneous real-time data, typically in the form of numerical arrays, images, or videos. However, LLMs have inherent limitations in processing such unstructured or non-textual data, hindering understanding and reasoning. We focus on numerical array data, including device states and task states. To bridge the semantic gap between numerical data and the textual processing capabilities of LLM, we propose an intelligent context-aware query generation module. As illustrated in Fig. 2, this module transforms data through the following steps:

1. Predefined Query Templates and Semantic Mapping: This module uses structured query templates. For each numerical input feature, the module establishes fine-grained semantic mapping rules. For example, based

FIGURE 2. Schematic diagram of intelligent context awareness and QoS-aware intelligent tendency matching module.

[Image]

on the value range of the device's residual energy, it maps the value to qualitative descriptions such as 'sufficient energy' or 'insufficient energy'.

2. QoS Preference Emphasis: The module highlights the primary optimization objectives in the generated query texts according to the explicit QoS weight factors provided in the input data. For instance, if the weight for latency is higher than that for energy consumption, the query will explicitly state that 'the primary objective of this task offloading is to minimize latency, where reducing latency is more critical.'

Through these mechanisms, the intelligent context- aware query generation module successfully transforms complex raw data into structured and semantically interpretable inputs for LLM. The resulting semantic query texts are then encoded into context query embedding vectors, denoted as E original .

## Qos-AWAre IntellIGent tendency mAtchInG module

Sole reliance on semantic similarity challenges accurate knowledge retrieval. We propose the QoS-aware intelligent tendency matching module. It biases retrieval toward entries highly aligned with task QoS objectives. The module dynamically combines similarities between the original query and the QoS preference query. This steers results toward matching QoS goals. The specific implementation steps are as follows:

1. Generation of QoS-Preference Query Embeddings: Based on the task's QoS preference, we predefine two typical descriptions representing distinct QoS orientations: minimizing latency and minimizing energy consumption. The descriptions are given as follows:

- This task highly prioritizes minimizing latency and requires extremely fast response times.
- This task highly prioritizes minimizing energy consumption and requires high energy efficiency.

These textual descriptions are embedded using a sentence embedding model to generate the corresponding QoS-preference query embedding vector, denoted as E QoS.

2. Multi-Dimensional Similarity Evaluation and Weighted Fusion of Knowledge Entries: For each knowledge entry Ki in the vector knowledge base, with embedding vector E K i , we simultaneously compute its similarity with two query vectors. First, the cosine similarity between the knowledge entry embedding E K i and the original contextual query embedding E original is calculated, denoted as Sim original ( Ki ). Then, the cosine similarity between the knowledge entry embedding E K i and the QoS preference query embedding E QoS is computed, denoted as SimQoS( Ki ).
3. Computation of Combined Similarity Score: To comprehensively consider both

FIGURE 3. Dynamic knowledge base with positive and negative experiences for intelligent prompt generation module.

[Image]

contextual matching and QoS preference, we perform a weighted combination of these two similarity measures to obtain the combined similarity for each knowledge entry, denoted as Sim combined ( Ki ).

This module ensures that the LLM generates task offloading strategies that are more precise and highly adaptive. It significantly enhances decision-making performance in the IoE.

## dynAmIc AdAptIve hybrId knoWledGe bAse constructIon And mAnAGement

To enable continuous learning from historical experience and enhance decision-making capabilities, the proposed framework constructs a dynamic and adaptive composite vector knowledge base. This knowledge base incorporates predefined expert base knowledge and dynamically accumulates both positive and negative historical experiences generated during system operation. As shown in Fig. 3, the implementation steps are as follows:

1. Knowledge Base Initialization and Base Knowledge Injection: At framework startup, an empty vector knowledge base is initialized. Preorganized expert base knowledge texts are transformed into high-dimensional vectors using an embedding model. These vectors are added to the knowledge base as entries of the 'Base knowledge' type. These entries provide general principles and common sense within the domain.
2. Real-time Case Data Capture and Processing and Failure Degree Quantification: After each task offloading decision is executed, the system captures the complete

decision context, the execution action generated by the LLM, and the total reward feedback. The failure degree is based on the normalized reward, which is determined by first subtracting the global minimum possible reward from the total reward, and then dividing this difference by the total range of possible rewards. The failure degree is then obtained by subtracting the normalized reward from 1.0, ensuring that 0.0 signifies optimal performance and 1.0 signifies complete failure relative to the system's reward bounds. A decision is classified as a positive case if the failure degree is low (less than or equal to 0.3). A decision is classified as a negative case if the Failure Degree is high (greater than 0.3). Negative cases are further categorized into moderate failure cases (failure degree between 0.3 and 0.7) and severe failure Cases (failure degree greater than 0.7).

3. Historical Case Textualization and Embedding: The captured real-time case data is processed into a structured natural language text block. This block details the scenario, decision, outcome, rationale and performance metrics of the current task offloading. Each case is labeled according to its failure degree, with failed cases further classified as severe, moderate, or minor. The text block is then converted into a embedding vector using the embedding model.
4. Dynamic Knowledge Base Update and Deduplication : The generated historical case embedding vectors, corresponding texts, failure degrees, and total rewards are dynamically added to the knowledge base. The knowledge base performs deduplication

[1 https://huggingface.co/ BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)

during this process to ensure each text entry is unique and to avoid redundancy. To maintain retrieval efficiency and prevent memory bottlenecks in large-scale deployments, an upper limit is set on the size of the knowledge base, where the oldest cases are retired when this limit is reached.

Through the above procedures, the composite knowledge base continuously evolves with system operation, accumulating complex real-world experience. Introducing the failure degree quantifies the severity of negative cases, transforming the knowledge base from a simple information repository into a system embedding quantitative risk awareness. This significantly enhances the LLM's proactive risk avoidance capability during decision-making.

## hybrId knoWledGe-bAsed prompt GenerAtIon module

To overcome the limitation of incomplete prompt knowledge caused by single semantic retrieval methods in traditional RAG frameworks, we propose a hybrid knowledge-based prompt generation module. This module ensures that the LLM accurately acquires and utilizes both positive and negative experiences. The core of this module is to achieve precise hierarchical retrieval based on the QoS-aware intelligent tendency matching module. It performs refined filtering and ranking on the retrieved results to finally construct a high-quality comprehensive prompt. The specific implementation steps are as follows:

1. Hierarchical Knowledge Retrieval Based on QoS-aware Similarity:

This module performs multi-channel retrieval on the knowledge base based on the QoS-aware intelligent tendency matching module. This mechanism divides the retrieval process into three independent and guaranteed channels:

- Base Knowledge Retrieval: The module filters entries labeled as base knowledge and retrieves several base knowledge items most relevant to the current context and QoS preferences. To ensure sufficient coverage, as many results as possible are returned within availability even if the number of retrieved items is limited.
- Positive Historical Case Retrieval: Historical records marked as successful cases are filtered, and several success cases most relevant to the current context and QoS preferences are retrieved. To avoid dominance by one case type leading to lack of the other, a baseline similarity threshold is set to guarantee a minimum number of positive cases (if available), ensuring balanced experience representation.
- Negative Historical Case Retrieval: Historical records marked as failed cases are filtered, and several failure cases most relevant to the current context and QoS preferences are retrieved. Similarly, a baseline similarity threshold is set to ensure a minimum number of negative cases (if available), providing comprehensive lessons from failures.

2. Fine-Grained Ranking and Filtering: The module further ranks and filters the knowledge retrieved from each channel to

ensure that the highest quality prompt is ultimately provided to the LLM.

- Base Knowledge: The top relevant items are directly selected as prompt for the LLM.
- Positive Historical Cases: The retrieved positive cases are ranked by a weighted score that combines QoS-aware composite similarity, semantic similarity, and historical total reward. Specifically, each component is assigned an empirical weight, and the weighted score is calculated as the sum of each component multiplied by its corresponding weight. The weights are set based on preliminary experiments to balance the influence of similarity and historical reward. Top cases according to this ranking are selected.
- Negative Historical Cases: The retrieved negative cases are ranked in descending order by failure degree. Cases with higher failure severity are ranked higher as they provide more critical lessons for the LLM to learn from.

3. Comprehensive Prompt Construction: The filtered and optimized base knowledge, positive cases, and negative cases are integrated into a comprehensive and structured prompt.

Through this hybrid knowledge-based prompt generation module, the proposed framework enables the LLM to receive highly relevant information containing both positive and negative experiences during decision making.

## performAnce evAluAtIon

## experImentAl setup

The experiments are conducted on a server equipped with an NVIDIA RTX 3090 GPU. To simulate the dynamics and complexity in EC for the IoE, a custom simulation environment is established with key parameters configured according to [14]. The scenario consists of a centralized edge server, a edge server, and five user devices. When a user device offloads a task and the edge server accepts it, the task is processed by one of the server's computing units. The channel gain ranges from 5 dB to 14 dB, and the wireless bandwidth is set to 40 MHz. The edge server has a computing capacity of 4 GHz and a storage capacity of 400 MB. The local computing capacity of user devices ranges from 0.4 GHz to 1.5 GHz. Task data sizes range from 1 MB to 50 MB, and task deadlines range from 0.1 s to 1 s. The transmission power of user devices is set between 1 dBm and 24 dBm, and their energy reserves range from 0.5 MJ to 3.2 MJ. To ensure reproducibility, the random seed is set to 35. The simulation is executed over multiple episodes to evaluate long-term cumulative rewards and system stability.

The implementation details of the framework are elaborated below. The BAAI/bge-base-en-v1.5 model 1 serves as the embedding model across all modules of the framework [15]. To align with the real-world physical constraints identified in

[14], the algorithm parameters are heuristically configured to balance decision accuracy and system overhead. The retriever initially fetches the topK = 5 candidates for base knowledge, positive experiences, and negative counterexamples based on a weighted similarity score (0.8 for semantic relevance and 0.2 for QoS alignment to balance context and constraints). Subsequently, a re-ranking process filters these candidates, selecting the top-2 most critical entries from each category for the final prompt construction to prevent prompt redundancy ( K prompt = 2 for each type). Positive cases are re-ranked by historical reward, while negative cases are sorted by failure severity to prioritize risk mitigation. For the LLM generation, we utilize a deterministic setting with temperature T = 0.2 to ensure decision stability. The capacity of the knowledge base is capped at 10,000 historical cases. We compare the proposed framework with the following four baseline approaches:

- Proposed Framework: In the experiments, we test with various LLM application programming interfaces (APIs), including Gemini series 2 , Ernie series 3 , and Qwen series 4 . These models are chosen for their diversity in architecture and their position as widely recognized and highperforming LLMs, enabling the thorough evaluation of our framework's generalizability across different scales.
- Conservative Strategy: This baseline processes all tasks locally on user devices without any offloading. The same environmental settings and simulation parameters as the proposed framework are used to ensure fair comparison.
- Aggressive Strategy: This baseline offloads all tasks to the idle edge server for processing. It also shares the same simulation configuration as the proposed framework to guarantee fair evaluation.
- DRL Baselines: We employ three DRL algorithms for comparative analysis. The deep deterministic policy gradient (DDPG) serves as a classical DRL benchmark. The agent learns optimal policies through continuous environment interaction. Its hyperparameters are: actor learning rate 0.0001, critic learning rate 0.001, discount factor 0.99, soft update coefficient 0.005, replay buffer capacity 10000, and batch size 64. The twin delayed deep deterministic policy gradient (TD3) is included as an advanced DRL baseline. TD3 mitigates DDPG's overestimation bias using twin Critic networks, delayed policy updates, and target policy smoothing. The federated reinforcement learning (FRL) employs a standard FRL framework for distributed task offloading comparison. FRL clients utilize the DDPG algorithm locally, periodically aggregating parameters via federated averaging at the edge server, with the federation period set to 50 time steps.

To quantitatively evaluate the performance of each method, we focus on the following metrics. The total reward reflects the comprehensive benefit of task offloading strategies and is a weighted function of QoS metrics such as latency and energy consumption. The average latency refers to the mean time taken from task generation to completion. The average energy consumption indicates the mean energy used during task execution.

## experImentAl results And AnAlysIs

Fig. 4 presents the total reward performance of the proposed framework. The proposed framework uses Gemini-2.5-Flash as the core LLM. The total reward reflects the effectiveness of task offloading in balancing latency and energy consumption. In Fig. 4(a), the framework using Gemini-2.5-Flash achieves faster convergence and higher rewards than other LLMs. Even with alternative LLMs, as shown in Fig. 4(c), the proposed framework outperforms traditional approaches, verifying its ability in contextual understanding and reasoning through retrieved knowledge. In Fig. 4(c), the proposed method surpasses conservative, aggressive, and DDPG-based strategies. Fig. 4(b) and (d) reveal that removing RAG or QoS-aware guidance causes significant performance decay, validating that retrieved knowledge rectifies LLM reasoning biases and aligns decisions with strict task constraints. The proposed framework achieves an average reward improvement of 48.4% over 12 methods. Our reward standard deviation (0.40) is lower than DDPG (0.59), demonstrating that knowledge-based reasoning provides better decision stability than the stochastic exploration typical of traditional DRL methods. These improvements are attributed to the synergy between the hybrid RAG mechanism and QoSaware guidance. By integrating complementary positive and negative historical experiences, the framework enables the LLM to proactively identify high-risk decisions. This synergy empowers the LLM to synthesize context-sensitive and risk-aware policies, facilitating faster convergence and robust adaptability. Consequently, the framework bridges the gap between raw environment data and optimal offloading decisions, yielding superior rewards across dynamic IoE scenarios.

Fig. 5(a) illustrates the average latency, where our framework achieves the lowest delay across all evaluated methods. Unlike DRL baselines that rely on inefficient stochastic exploration, our framework leverages historical knowledge to bypass sub-optimal state-action trials. Ablation confirms RAG and QoS-aware knowledge are vital. Our method achieves a 44.8% latency reduction over methods lacking these enhancements. Thus, the framework effectively lowers latency, enhancing IoE system responsiveness. Fig. 5(b) compares energy consumption, where our framework yields a 50.9% reduction by intelligently balancing computation and transmission costs. This efficiency is primarily attributed to the RAG architecture, which empowers the LLM to synthesize a comprehensive understanding of current system states and historical experiences. By leveraging this retrieved knowledge, the LLM can identify energy-optimal strategies that traditional DRL baselines fail to capture, effectively minimizing resource waste in dynamic environments.

Fig. 6 demonstrates the robustness and scalability of our proposed framework by comparing its performance against DDPG, TD3 and FRL under increased system complexity. In Fig. 6(a), although all methods experience performance degradation due to heightened resource contention, our framework consistently achieves the lowest average latency and demonstrates the slowest rate of decline. This resilience stems from the semantic abstraction capability of RAG, which allows the LLM to effectively manage high-dimensional state information that often leads to policy collapse in DRL-based methods. Similarly, Fig. 6(b) confirms the superior energy efficiency of our method, which achieves the lowest average energy consumption with the shallowest growth curve compared to the baselines. This advantage is attributed to the RAG architecture's ability to synthesize a comprehensive understanding of system states and historical experiences, enabling energy-conscious orchestration even as the network scale expands. Collectively, these results underscore the inherent scalability of the RAG-LLM paradigm and its capacity to mitigate the curse of dimensionality in large-scale, resource-constrained IoE environments.

[2 https://gemini.google. com/app](https://gemini.google.com/app)

[3 https://console.bce.baidu. com/qianfan/modelcenter/ model/buildIn/detail/ am-bg7n2rn2gsbb?tab=version](https://console.bce.baidu.com/qianfan/modelcenter/model/buildIn/detail/am-bg7n2rn2gsbb?tab=version)

[4 https://bailian.console.aliyun.com/?tab=model#/model-market?provider=aliyun](https://bailian.console.aliyun.com/?tab=model#/model-market?provider=aliyun)

FIGURE 4. Total reward performance analysis. a) Impact of different LLM models on the proposed framework's reward. b) Comparison of rewards between the proposed framework and LLM baselines without RAG. c) Comparison of rewards between the proposed framework and traditional baseline methods. d) Comparison of rewards between the proposed framework and methods without QoS knowledge assistance.

[Image]

FIGURE 5. Performance comparison of task offloading metrics. a) Comparison of average latency performance under different methods. b) Comparison of average energy consumption performance under different methods.

[Image]

FIGURE 6. Performance comparison across varying user device numbers. a) Comparison of average task offloading latency performance. b) Comparison of average energy consumption performance.

[Image]

## conclusIon And future Work

To address the challenges in the IoE, this paper develops a robust RAG-empowered adaptive task offloading framework. Our framework overcomes the rigidity of traditional heuristic and RL-based methods through four synergistic technical pillars. First, a novel RAG-empowered adaptive task offloading framework is introduced to transform dynamic task and environment data into structured semantic inputs, enabling intelligent decision-making. Second, an intelligent preference matching mechanism dynamically weights task QoS features to guide knowledge retrieval. Third, a composite knowledge base incorporating both positive and negative cases is constructed, where failure severity is quantified to enhance robustness. Fourth, a hybrid knowledge-based prompt generation module is proposed, employs hierarchical retrieval with channel-specific thresholds and ranking optimization to ensure relevant and professional prompts. Experiments demonstrate that our framework achieves a 48.4% improvement in cumulative reward compared to baselines. Most notably, the framework significantly mitigates system bottlenecks, yielding 44.8% and 50.9% reductions in task latency and energy consumption, respectively, which confirms its superior resource efficiency in high-load scenarios. These results substantiate that integrating LLM with RAG provides a highly reliable and risk-sensitive solution for offloading orchestration. This work contributes a versatile RAG-empowered paradigm that bridges the semantic gap between numerical IoE data and intelligent decision-making. Despite these advancements, future research will address current limitations in two directions. First, we will explore model compression and lightweight LLMs to reduce computational overhead on resource-constrained edge devices. Second, we aim to investigate decentralized RAG and hybrid reasoning methods to enhance system scalability and robustness in extreme or unseen scenarios.

## AcknoWledGment

This work was supported by Management and Consulting Projects of State Grid Corporation of China under Grant SGHL0000DKJS2310205.

## RefeRences

- [1] T. Gong et al., 'Edge intelligence in intelligent transportation systems: A survey,' IEEE Trans. Intell. Transp. Syst. , vol. 24, no. 9, pp. 8919-8944, Sep. 2023.
- [2] A. Naghib, F. S. Gharehchopogh, and A. Zamanifar, 'A comprehensive and systematic literature review on intrusion detection systems in the Internet of Medical Things: Current status, challenges, and opportunities,' Artif. Intell. Rev. , vol. 58, no. 4, p. 114, Jan. 2025.
- [3] M. Yan et al., 'Two-timescale hierarchical contract for joint computation offloading and energy management in edge computing system,' IEEE Trans. Netw. Sci. Eng. , vol. 12, no. 3, pp. 1745-1760, May 2025.
- [4] X. Zhou et al., 'Digital twin empowered task offloading for mobile-edge computing in 6G Internet of Vehicles,' IEEE Internet Things J. , vol. 12, no. 15, pp. 29189-29202, Aug. 2025.
- [5] J. Liu et al., 'VLC-enabled UAV network for IoT with co-channel interference: Joint spatial deployment and resource allocation,' IEEE Internet Things J. , vol. 12, no. 12, pp. 20707-20721, Jun. 2025.
- [6] X. Huang et al., 'Toward effective retrieval augmented generative services in 6G networks,' IEEE Netw. , vol. 38, no. 6, pp. 459-467, Nov. 2024.
- [7] N. Alabbasi et al., 'TeleOracle: Fine-tuned retrieval-augmented generation with long-context support for networks,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13170-13182, May 2025.
- [8] H. M. A. Zeeshan et al., 'LLM-based retrieval-augmented generation: A novel framework for resource optimization in 6G and beyond wireless networks,' IEEE Commun. Mag. , vol. 63, no. 10, pp. 60-67, Oct. 2025.
- [9] T. Ouyang et al., 'AdaRAG: Adaptive optimization for retrieval augmented generation with multilevel retrievers at the edge,' in Proc. IEEE INFOCOM Conf. Comput. Commun. , London, U.K., May 2025, pp. 1-10.
- [10] G. Liu et al., 'Adaptive contextual caching for mobile edge large language model service,' 2025, arXiv:2501.09383 .

- [11] Y. He et al., 'Large language models (LLMs) inference offloading and resource allocation in cloud-edge computing: An active inference approach,' IEEE Trans. Mobile Comput. , vol. 23, no. 12, pp. 11253-11264, Dec. 2024.
- [12] R. Zhang et al., 'Interactive AI with retrieval-augmented generation for next generation networking,' IEEE Netw. , vol. 38, no. 6, pp. 414-424, Nov. 2024.
- [13] S. Song et al., 'Joint bandwidth allocation and task offloading in multi-access edge computing,' Expert Syst. Appl. , vol. 217, May 2023, Art. no. 119563.
- [14] T. Z. Gebrekidan, S. Stein, and T. J. Norman, 'Combinatorial client-master multiagent deep reinforcement learning for task offloading in mobile edge computing,' in Proc. Int. Joint Conf. Auto. Agents Multiagent Syst. , May 2024, pp. 2273-2275.
- [15] S. Xiao et al., 'C-pack: Packaged resources to advance general Chinese embedding,' in Proc. Int. ACM SIGIR Conf. Res. Dev. Inf. Retr. (SIGIR) , Washington, DC, USA, May 2024, pp. 2273-2275.

## BiogRaphies

Xiongjie Zhou (zxj2221896@gmail.com) is with Heilongjiang University, China. His current research interests include the Internet of Things, edge computing, and large language model.

Xin guan (Member, IEEE) (guanxin.hlju@gmail.com) is currently a Professor with Heilongjiang University, China. His research interests include the Internet of Things, energy internet, and machine learning.

ning Wang (wn007@126.com) currently works as the Deputy Director with the Dispatching and Control Center, State Grid Heilongjiang Electric Power Company Ltd., China. His research interests include electrical operation of power plant, power dispatching management, power grid operation technology, and renewable energy operation management.

hongyang Chen (Senior Member, IEEE) (dr.h.chen@ieee.org) is currently a Senior Research Expert with Zhejiang Laboratory, China. His research interests include the Internet of Things, data-driven intelligent networking and systems, machine learning, localization, location-based big data, B5G, and statistical signal processing.

Tomoaki ohTsuki (Senior Member, IEEE) (ohtsuki@ics.keio. ac.jp) is currently a Professor at Keio University, Japan. His research interests include wireless communications, optical communications, signal processing, and information theory.

yan Zhang (Fellow, IEEE) (yanzhang@ieee.org) is currently a Full Professor with the University of Electronic Science and Technology of China, China. His current research interests include next-generation wireless networks leading to 5G beyond and green and secure cyber-physical systems (e.g., smart grid, healthcare, and transport).
