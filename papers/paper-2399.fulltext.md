---
title: A Human-in-Multi-Agent-Loop Intent Refinement Method for Task Offloading in Mobile Edge Computing
authors:
  - Shao Yuan
  - Weichen Ni
  - Boxiao Han
  - Zuojun Dai
  - Yang Yu
affiliations:
  - Jiangsu University of Technology, Changzhou, China
  - China Mobile Research Institute, China Mobile Communications Group Co., Ltd., Beijing, China
  - ZGC Institute of Ubiquitous-X Innovation and Applications, Beijing, China
keywords: MEC, HIMAL, Task Offloading, QoSE, LLM
abstract: "In mobile edge computing (MEC), intent recognition plays a pivotal role in task offloading. To address this challenge, this paper proposes a Human-in-Multi-Agent-Loop (HIMAL) intent refinement method for MEC that synergistically integrates multi-agent collaboration with human judgment to enhance resource allocation and task scheduling efficiency, thereby facilitating the advancement of the Industrial Internet of Things (IIoT). The proposed HIMAL system enhances AI decision-making through continuous integration of human feedback into the AI's learning process, thereby enhancing both the precision of AI outputs and contextual awareness. Experimental results demonstrate that our approach achieves significant performance improvements by embedding human guidance within large language model (LLM) workflows, where human operators serve as contextual interpreters to refine AI responses."
---

## A Human-in-Multi-Agent-Loop Intent Refinement Method for Task Offloading in Mobile Edge Computing

## 1st Shao Yuan

Jiangsu University of Technology Changzhou, China ZGC Institute of Ubiquitous-X Innovation and Applications Beijing, China 2023655164@smail.jsut.edu.cn

## 3rd Boxiao Han

ZGC Institute of Ubiquitous-X Innovation and Applications Beijing, China hanboxiao@zgc-xnet.com

5th Yang Yu \*

Jiangsu University of Technology

Changzhou, China dxyy@jsut.edu.cn

Abstract -In mobile edge computing (MEC), intent recognition plays a pivotal role in task offloading. To address this challenge, this paper proposes a Human-in-Multi-AgentLoop (HIMAL) intent refinement method for MEC that synergistically integrates multi-agent collaboration with human judgment to enhance resource allocation and task scheduling efficiency, thereby facilitating the advancement of the Industrial Internet of Things (IIoT). The proposed HIMAL system enhances AI decision-making through continuous integration of human feedback into the AI ' s learning process, thereby enhancing both the precision of AI outputs and contextual awareness. Experimental results demonstrate that our approach achieves significant performance improvements by embedding human guidance within large language model (LLM) workflows, where human operators serve as contextual interpreters to refine AI responses.

Keywords-MEC;HIMAL;Task Offloading;QoSE;LLM

## I. INTRODUCTION

5G and the upcoming 6G technologies [1] are crucial for the IIoT [2], as they provide high-speed data transmission, ultra-low latency, and massive connectivity. MEC [3] further enhances IIoT systems by enabling distributed computation at the network edge, thereby reducing latency and bandwidth consumption while improving real-time decision-making. As cloud-based wireless networks become a major trend in 6G, the network edge will integrate more capabilities with MEC, such as communications, sensing, and computation. By processing data closer to the source, MEC supports critical applications such as autonomous control, predictive maintenance, and lowlatency industrial automation. In this context, Quality of Service and Experience (QoSE) is essential for ensuring reliable device interconnectivity, while intent recognition helps dynamically adjust resource allocation to meet real-

## 2nd Weichen Ni

China Mobile Research Institute China Mobile Communications Group Co.,Ltd Beijing, China niweichen@chinamobile.com

4th Zuojun Dai ZGC Institute of Ubiquitous-X Innovation and

Applications Beijing, China george.dai@bupt.edu.cn

time demands, thereby enhancing both system performance and user satisfaction.

In recent years, the rapid development of the IIoT has led scholars to focus on assessing and optimizing QoSE. Gajjar et al. [4] proposed a framework linking service quality and user experience, while Zhao et al. [5] surveyed the Quality of Experience (QoE) in IIoT but lacked quantitative measurement standards, resulting in subjective assessments that overlooked the multidimensional nature of user intent. Minovski et al. [6] suggested a four-layer framework for objective user experience assessment. However, their framework fails to address both the functional differences among IoT devices and the varying impacts of network conditions, which may significantly affect QoSE.

Meanwhile, LLMs are increasingly being applied in communication systems. Shao et al. [7] proposed a framework called WirelessLLM, which was specifically designed to adapt and enhance LLMs for addressing the unique challenges and requirements of wireless communication networks. Kalita et al. [8] developed a framework and its corresponding modules where LLMs can be effectively utilized under the protection of semantic communication at the network edge to achieve efficient communication in IoT networks. However, their approach failed to effectively integrate natural language processing with communication scheduling. Jiang et al. [9] proposed a multi-agent system equipped with domain-specific communication knowledge and tools to handle communication-related tasks using natural language processing. Nevertheless, due to LLMs' limited capability in understanding dynamic changes in devices and environments, their comprehension of the physical world remains inadequate. Consequently, such multi-agent system may suffer from degraded communication efficiency or information loss when facing sudden network traffic surges.

Therefore, this paper proposes a HIMAL intent refinement method based on the HITL [10] framework to overcome the challenges of task offloading in MEC. The main contributions of this paper are summarized as follows:

- We propose a HIMAL intent refinement method based on the HITL framework, accompanied by a HIMAL system architecture specifically designed for edge-cloud deployment. By synergistically integrating HITL with multi-agent collaboration, our method effectively maps human intent into utility functions, thereby optimizing scheduling decisions with improved accuracy.
- Within the HIMAL system architecture, we introduce an agent model consisting of five core components: a centered agent, memory, action, perception, and brain. This edge-optimized design enables agents to efficiently process data locally while maintaining effective coordination with centralized cloud resources.
- We design a novel prompt method in the HIMAL system architecture to align task scheduling with user intentions. This approach significantly enhances deployment adaptability in edge-cloud environments, particularly in dynamic scenarios where real-time data and evolving user preferences critically influence scheduling performance.

The remainder of this paper is organized as follows. Section II presents the system model of the MEC and the HIMAL system architecture. Section III details the experimental methodology and presents a thorough analysis of the results. Finally, Section IV concludes the paper and discusses future research directions.

## II. SYSTEM STRUCTURE

## A. System Model of the MEC

The system model of the MEC comprises three distinct layers: the User Device Layer, the Edge Server Layer, and the Cloud Data Center Layer. The User Device Layer forms the foundation of the system, incorporating various end-user equipment such as IoT sensors and wearable devices. These devices generate service requests and offload computationintensive tasks to proximal edge servers.

The Edge Server Layer serves as the intermediate tier, composed of computing nodes deployed at base stations, access points, and network edge locations. These servers provide localized processing capabilities for latency-critical tasks, substantially reducing dependence on remote cloud infrastructure. For computationally demanding workloads, edge servers maintain seamless interoperability with upperlayer cloud resources.

The Cloud Data Center Layer constitutes the uppermost tier of the system, delivering high-performance, elastic computing and storage resources. This layer specializes in executing resource-intensive operations, including largescale machine learning training, comprehensive big data analytics, and persistent data archiving.

## B. System Architecture

## 1) System Architecture

This paper proposes a HIMAL intent refinement method to address the discrepancies between task scheduling execution and user intent in the MEC. Existing large language models (LLMs) struggle to comprehend the physical world due to their lack of real-world perception, which hinders their ability to accurately understand user intent in complex scenarios and leads to suboptimal decision-making. The HIMAL intent refinement method mitigates these challenges by incorporating human participation throughout the AI training process, enabling continuous feedback that enhances model's understanding of user intent and improves decision accuracy. Building upon the HIMAL intent refinement method, we further propose the HIMAL system architecture, as illustrated in Figure. 1. In this architecture, the LLM generates task offloading strategies by analyzing user intentions, environmental constraints and resource availability in MEC. Humans provide iterative feedback to the LLM, enabling it to refine its understanding of user-specific delay and energy consumption requirements. Additionally, the architecture incorporates a multi-agent collaboration method, a HIMAL workflow and a prompt method.

Figure. 1. HIMAL System Architecture

<!-- image -->

## 2) Multi-Agent Collaboration Method

In the HIMAL System Architecture, we propose an agent model centered around the agent and comprising four additional components: memory, action, perception, and brain. The specific descriptions of each component are as follows:

- Agent: The agent serves as a proxy for the LLM, interacting with users.
- Brain: The brain acts as the agent's core, encompassing various LLMs. It is responsible for defining QoSE goals, analyzing evaluation results, and adjusting those goals based on the results and user feedback.
- Memory: The memory module consists of longterm memory, medium-term memory, and shortterm memory. Long-term memory is accessed through Retrieval-Augmented Generation (RAG) [11], medium-term memory is retrieved through word slots, and short-term memory is directly obtained from historical records.
- Action: The action module executes tasks, utilizing various tools such as simulation tools, querying tools, and others.
- Perception: The perception module serves as the agent's sensory component, involving system model design and prompt methods.

Additionally, we propose a method for multi-agent collaboration. We define four agents -the maintenance engineer, the dispatcher, the analyst, and the customer. The maintenance engineer collects and summarizes information about system users and network conditions. The dispatcher utilizes this data for initial scheduling and makes subsequent adjustments based on updates from the maintenance engineer, analysis from the analyst, customer requests, and previous scheduling results. The analyst is responsible for analyzing the scheduling results provided by the dispatcher and, in conjunction with technical solutions, evaluating the guarantees for various users, businesses, and metrics. The customer reviews the analysis, considers contextual information, and provides adjustment suggestions when necessary.

## 3) HIMAL Workflow

We have studied and proposed the fundamental workflow of HIMAL, as presented below. The HIMAL workflow demonstrates the interaction between the user and the multi-agent system, continuing until the user' s requirements are fully satisfied.

## HIMAL Workflow

## Step:

1. The user inputs task-related descriptions, including the type, arrival rate, priority, and performance metrics (e.g., delay, energy consumption), as well as a description of the target formula.
2. The multi-agent system uses RAG to query the knowledge base, retrieves the interaction history, constructs prompts, and queries the LLM.
3. The LLM generates the query results.
4. The multi-agent system extracts result information and generates an optimization objective function.
5. The multi-agent system analyzes the results and calls the most suitable optimization simulation tool to conduct the simulation, extracts the simulation results and forms new prompts to request that the LLM analyzes the results.
6. The LLM analyzes the results.
7. The multi-agent system compiles the interaction process for this round, incorporates historical data, and provides feedback to the user.
8. The user reviews and adjusts the results.
9. Steps 2-8 are repeated until the user is satisfied with the results.

## 4) Prompt Method

Prompt engineering enhances the response quality of LLMs through optimized prompts. Notable methods include the Chain of Thought (CoT) proposed by Wei et al. [12], which decomposes tasks into sub-problems for sequential processing. Wang et al. [13] improved this approach with a self-consistent method, while Yao et al. [14] introduced the Tree of Thought (ToT) framework leveraging heuristic searches. This paper proposes a novel prompt method -SRR-CoT, which advances CoT through three key enhancements:

- Added structured reasoning requirements: Complex tasks may lead to erratic or disorganized reasoning in LLMs, compromising output accuracy. To mitigate this issue, we explicitly require the model to follow a structured three-step reasoning process (understand, analyze and output) within the prompt. This ensures logical clarity in the reasoning process and improves the reliability of the results.
- Added role information of interaction objects: In multi-role scenarios, LLMs must distinguish the tasks and intentions of different roles. Thus, we enhance prompts by incorporating role-specific information (e.g., interaction objects, modes, and formats) to mitigate response bias caused by role ambiguity.
- Added the current round of interaction: In multiround interactions, LLMs may encounter repetitive input-output pairs, risking comprehension deviations. To address this, we embed the current interaction round number in the prompt, enabling the model to maintain temporal awareness and reduce redundancyinduced errors.

## III. SCHEDULING DECISION EXPERIMENT BASED ON PROMPT

## A. Simulation Setup

This paper established a simulation environment with wireless battery management systems (WBMS) [15] and classified WBMS terminals into four types based on QoE: n=1 (normal, sufficient energy), n=2 (critical, sufficient energy), n=3 (normal, insufficient energy), and n=4 (critical, insufficient energy). Additionally, the task offloading of the WBMS is based on QoE. The overall utility function of the WBMS is shown in Formula (1):

<!-- formula-not-decoded -->

where 𝜏 denotes the delay, 𝜀 represents the energy consumption, 𝜔𝑛,1 and 𝜔𝑛,2 are the weight of delay and energy consumption respectively, and q is a parameter bounded within the interval (0, 1).

## B. Prompt Experiment

First, we designed corresponding prompts for four agents using SRR-CoT. Take the dispatcher as an example, its prompt template is presented below.

You are a dispatcher responsible for conducting the first round of scheduling based on the following summary information from the maintenance engineer. You need to output the simulation results and perform the following steps:

1. Understand the current status of users, networks, etc., in the wireless battery management system.
2. Analyze how to set the initial parameters for the wireless battery management system based on the understood status of users, networks, and resources.
3. Output the simulation results obtained from the simulation conducted using the initial parameters.

Interaction Object: Maintenance engineer

Interaction Mode: Output

Interaction Format: {

Interaction Mode: Output

Interaction Format: {

Input: Summary information from the operations engineer

Output: Scheduling results from this round of the scheduler }

Current Round of Interaction: Round 1

Furthermore, we conducted comparative experiments evaluating the SRR-CoT against the standard CoT. The experimental setup and the results generated by each prompting method are illustrated in Figure. 2.

Figure. 2. The problem and the results generated by CoT and SRRCoT.

<!-- image -->

The comparison of results demonstrates that the CoT outlines scheduling in stages. In contrast, the SRR-CoT not only details the dispatcher 's process of understanding, analyzing, and outputting but also summarizes its inputs and outputs, thereby providing richer content than CoT.

Finally, We further designed a comparative experiment for the scenarios of WBMS deployment in medium enterprise to investigate the impact of CoT and SRR-CoT methods on the accuracy of QoE evaluation of LLMs. The experiment systematically tested four representative LLM models (ChatGPT-4o-mini, Llama38B, Qwen2.5-72B-Instruct, and DeepSeek-V3).The experimental results are illustrated in Figure. 3.

Experimental results show that SRR-CoT has significantly higher QoE evaluation accuracy compared to CoT across the four models. Furthermore, we quantitatively compared the computational overhead between SRR-CoT and CoT on the same hardware. The results demonstrate that SRR-CoT introduces an additional 25%-30% inference time compared to standard CoT. However, this overhead is justified by an average accuracy improvement of 46%, particularly in MEC environments where high precision is critical. Therefore, we argue that such a trade-off is reasonable for accuracysensitive scenarios like MEC.

Figure. 3. Comparison of QoE evaluation accuracy of LLMs in medium enterprise using CoT and SRR-CoT

<!-- image -->

## C. Experiment 1: Basic Scheduling Process

After designing prompts for the four agents, we conducted basic scheduling. Taking on the role of the dispatcher, the scheduling is performed based on the summary information provided by the maintenance engineer. The prompts, inputs, and output results for the dispatcher are illustrated in Figure. 4.

Figure. 4. The prompt and input and output of the dispatcher (first round).

<!-- image -->

## D. Experiment 2: Refining Process

Then, we focus on intent refinement. First, the role of the analyst is assumed to analyze the results of the first round of scheduling. Next, the role of the customer is taken to provide feedback on the analyst's results based on the current background information and to make adjustment requests. Then, the second round begins with the dispatcher 's role, consolidating the previous scheduling results, the maintenance engineer's summary information, the analysis results, and the adjustment requests to draw conclusions on scheduling criteria and call the scheduling tool for the next round of scheduling. Finally, the above three processes are repeated until the customer is satisfied with the analysis results. The prompts, inputs, and output results for the analyst, the customer, the dispatcher are illustrated in Figure. 5, 6, 7.

<!-- image -->

Figure. 5. The prompt and input and output of the analyst.

Figure. 6. The prompt and input and output of the customer.

<!-- image -->

Figure. 7. The prompt and input and output of the dispatcher (second round).

<!-- image -->

After multiple interaction rounds in the experiment, we summarized the weight adjustments, illustrated in Figure. 8,9. Initially, all weights fluctuated with increased interactions. However, after 15 rounds, they stabilized as the customer, satisfied with the analyst's results, made fewer suggestions on delay and energy consumption for different battery types.

Figure. 8. Delay weight summary after multiple rounds of interaction.

<!-- image -->

Figure. 9. Energy consumption summary after multiple rounds of interaction.

<!-- image -->

## E. Experiment on the Accuracy of QoE Evaluation of LLMs

To investigate the impact of the HIMAL intent refinement method on the WBMS deployment across enterprises of different scales (small, medium, and large), we designed a comparative experiment to analyze its effect on the accuracy of QoE evaluation in LLMs. The experiment employed ChatGPT-4o-mini and Llama3-8B as test models, comparing their performance before and after applying the HIMAL intent refinement method. The experimental results are illustrated in Figure. 10.

Figure. 10. Comparison of the accuracy of QoE evaluation of LLMs before and after using HIMAL intent refinement method

<!-- image -->

The experimental results demonstrate that the QoE evaluation accuracy of both models shows significant improvement after implementing the HIMAL intent refinement method across enterprises of all scales (small, medium, and large).

## IV. SUMMARY

This paper proposes a HIMAL intent refinement method for task offloading in MEC. First, we establish a comprehensive system model for MEC. Second, we design a HIMAL system architecture. Finally, we conduct scheduling decision experiments using our proposed prompt method and perform a detailed experimental analysis. The experimental results demonstrate that the HIMAL intent refinement method significantly enhances system performance by incorporating human expertise as interpreters within the LLM ' s workflow. Furthermore, the HIMAL system effectively integrates human feedback with AI learning processes, thereby improving both the accuracy of AI outputs and contextual understanding capabilities. For future work, we plan to focus on optimizing performance with PEER [16] or DOE patterns, and integrating RAG functionalities and word slot system to broaden application scenarios.

## ACKNOWLEDGMENT

This work is funded by China Mobile Communications Group Co.,Ltd.

## REFERENCES

- [1] Zhang, P., Xu, W, Gao, H., et al. Toward wisdom-evolutionary and primitive-concise 6G: A new paradigm of semantic communication networks[J]. Engineering, 2022, 8: 60-73.
- [2] Wang, Zhenpo., Yuan, Changgui., Li, Xiaoyu. Analysis on technical challenges and development trends of power battery safety management for new energy vehicles[J]. Automotive Engineering, 2021, 42(12): 1606-1620.
- [3] Hou X, Ren Z, Yang K, et al. IIoT-MEC: A novel mobile edge computing framework for 5G-enabled IIoT[C]//2019 IEEE Wireless Communications and Networking Conference (WCNC). IEEE, 2019: 1-7.
- [4] Gajjar, V., Bhagat, S., Awasthi, A. Towards a Framework for Quality of Service and Experience in IoT[J]. IEEE Access, 2020, 8, 187583-187599.
- [5] Zhao, Y., Zhang, L. A Comprehensive Survey on Quality of Experience in Industrial IoT[J]. IEEE Internet of Things Journal, 2021, 8(1), 32-45.
- [6] Minovski, D. Quality of Experience in Industrial Internet of Things[D]. Luleå University of Technology, 2021.
- [7] Shao, J., Tong, J., Wu, Q., et al. WirelessLLM: Empowering Large Language Models Towards Wireless Intelligence[J]. arXiv preprint arXiv:2405.17053, 2024.
- [8] Kalita, A. Large Language Models (LLMs) for Semantic Communication in Edge-based IoT Networks[J]. arXiv preprint arXiv:2407.20970, 2024.
- [9] Jiang, F., Peng, Y., Dong, L., et al. Large language model enhanced multi-agent systems for 6G communications[J]. IEEE Wireless Communications, 2024.
- [10] Zhang, R., Du, H., Liu, Y., et al. Interactive AI with retrievalaugmented generation for next generation networking[J]. IEEE Network, 2024.
- [11] Zhao P, Zhang H, Yu Q, et al. Retrieval-augmented generation for ai-generated content: A survey[J]. arXiv preprint arXiv:2402.19473, 2024.
- [12] Wei J, Wang X, Schuurmans D, et al. Chain-of-thought prompting elicits reasoning in large language models[J]. Advances in neural information processing systems, 2022, 35: 24824-24837.
- [13] Wang X, Wei J, Schuurmans D, et al. Self-consistency improves chain of thought reasoning in language models[J]. arXiv preprint arXiv:2203.11171, 2022.
- [14] Yao S, Yu D, Zhao J, et al. Tree of thoughts: Deliberate problem solving with large language models[J]. Advances in neural information processing systems, 2023, 36: 11809-11822.
- [15] Cao Z, Gao W, Fu Y, et al. Wireless battery management systems: innovations, challenges, and future perspectives[J]. Energies, 2024, 17(13): 3277.
- [16] Wang Y, Li X, Wang B, et al. PEER: Expertizing DomainSpecific Tasks with a Multi-Agent Framework and Tuning Methods[J]. arXiv preprint arXiv:2407.06985, 2024.
