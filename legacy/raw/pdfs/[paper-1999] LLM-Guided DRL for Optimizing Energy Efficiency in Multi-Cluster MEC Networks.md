---
title: "LLM-Guided DRL for Optimizing Energy Efficiency in Multi-Cluster MEC Networks"
authors:
  - "Huiying Niu"
  - "Jinglun Cai"
  - "Ke Lv"
  - "Fei Shi"
  - "Sai Huang"
affiliations:
  - "The 54th Research Institute of CETC, Shijiazhuang, China"
  - "Key Laboratory of Universal Wireless Communications, Ministry of Education, Beijing University of Posts and Telecommunications, China"
abstract: "Enabled by unmanned aerial vehicles (UAVs), multi-cluster mobile edge computing (MEC) networks can provide highly flexible communication services for massive user connectivity. However, multiple clusters significantly increase network complexity, obstructing the optimization of system energy efficiency. This paper innovatively proposes a closed-loop large language models (LLMs)-guided deep reinforcement learning (DRL) framework named LGD, in which the LLM can iteratively design rewards for DRL. By combining the LGD framework with the powerful dueling double deep Q-network (D3QN) in DRL, the LGD-D3QN algorithm is proposed and applied to multi-cluster MEC networks to improve energy efficiency. Compared to other LLM and DRL algorithms, LGD-D3QN can achieve a significant improvement in energy efficiency."
keywords:
  - "Large language model"
  - "Deep reinforcement learning"
  - "Unmanned aerial vehicle"
  - "Mobile edge computing"
---

## LLM-Guided DRL for Optimizing Energy Efficiency in Multi-Cluster MEC Networks

Huiying Niu The 54th Research Institute of CETC Shijiazhuang, China

hui7884@163.com

## Jinglun Cai

The 54th Research Institute of CETC Shijiazhuang, China cetc54sjz@163.com

Abstract -Enabled by unmanned aerial vehicles (UAVs), multicluster mobile edge computing (MEC) networks can provide highly flexible communication services for massive user connectivity. However, multiple clusters significantly increase network complexity, obstructing the optimization of system energy efficiency. This paper innovatively proposes a closed-loop large language models (LLMs)-guided deep reinforcement learning (DRL) framework named LGD, in which the LLM can iteratively design rewards for DRL. By combining the LGD framework with the powerful dueling double deep Q-network (D3QN) in DRL, the LGD-D3QN algorithm is proposed and applied to multi-cluster MEC networks to improve energy efficiency. Compared to other LLM and DRL algorithms, LGD-D3QN can achieve a significant improvement in energy efficiency.

Index Terms -Large language model, Deep reinforcement learning, Unmanned aerial vehicle, Mobile edge computing

## I. INTRODUCTION

By offloading computation to the network edge, mobile edge computing (MEC) effectively boosts service capabilities at the network edge, addressing the shortcomings of traditional centralized cloud computing regarding real-time performance and coverage quality [1]. Nevertheless, the coverage of fixed terrestrial base stations remains geographically constrained. To further realize ubiquitous computing, unmanned aerial vehicles (UAVs), with their unique mobility and flexible deployment capabilities, have become ideal aerial platforms for MEC [2]. UAVs equipped with MEC servers can be deployed as aerial base stations, which are capable of establishing robust lineof-sight (LoS) links with users to offer low-latency and highbandwidth services. Network coverage is extended by UAVs, particularly in emergency communications, temporary hotspot areas, and remote regions [3].

UAV-assisted MEC provides a new scheme for communication and computation services to ground users and has gained

This work was supported in part by the National Natural Science Foundation of China under Grant (62422103, 62321001, 62171045, 62201090).

## Ke Lv

Key Laboratory of Universal Wireless Communications, Ministry of Education Beijing University of Posts and Telecommunications Beijing, China kelv@bupt.edu.cn Fei Shi\*

The 54th Research Institute of CETC Shijiazhuang, China dragonsf@163.com

## Sai Huang

Key Laboratory of Universal Wireless Communications, Ministry of Education Beijing University of Posts and Telecommunications

Beijing, China

huangsai@bupt.edu.cn

extensive attention from researchers. Maximizing both the endurance of the UAV and system throughput makes energy efficiency a crucial evaluation criterion. Traditional optimization methods are widely utilized to maximize energy efficiency. Li et al. [4] addressed the problem by jointly optimizing three factors: the two-dimensional (2D) UAV trajectory, the user transmit power, and the computation load allocation. For the solution, the Dinkelbach algorithm and the successive convex approximation (SCA) method were employed. However, with the increasing complexity of system models, finding an analytical solution to the objective function becomes challenging, and conventional optimization algorithms face considerable limitations regarding convergence, computational efficiency, and solution quality. This challenge benefits from the innovative approach of deep reinforcement learning (DRL). In the field of DRL, Zhang et al. [5] utilized the deep Qlearning network (DQN) to jointly optimize video layer selection, power allocation, and multi-UAV trajectories to improve energy efficiency. Additionally, Liu et al. [6] tackled the threedimensional (3D) multi-UAV trajectory planning problem. By integrating the double deep Q-learning network (DDQN), the system energy efficiency is greatly improved.

However, the above-mentioned studies focused solely on simple MEC scenarios, without addressing complex multicluster MEC scenarios. Furthermore, as the complexity of the system model further increases, the design of the reward significantly affects the results of DRL. Therefore, it is necessary to design appropriate rewards to improve the training effectiveness of DRL in complex scenarios. By training on massive human language and knowledge, large language models (LLMs) gain deep semantic understanding and logical reasoning power [7]. Consequently, LLMs can be leveraged to interpret complex task objectives and environmental information, and formulate them as effective reward functions, thus enabling DRL agents to learn efficiently in complex environments [8], [9]. Compared with [8] and [9], we have added a pre-generation mechanism in the process of LLM guiding DRL to design rewards. Before generating the actual reward function, an initial reward function with random weights is first generated utilizing the environment and task description. Then, through the first training iteration of the DRL, the values of these weights are gradually adjusted, rather than generating a new reward function structure each time, or having the reward value directly provided by the LLM. The contributions of this paper are summarized as follows:

- A multi-cluster MEC network is considered, where each cluster is composed of heterogeneous MEC nodes, including human users and internet of things (IoT) devices. At least one UAV equipped with MEC server is contained within each cluster. Furthermore, each MEC node has different computing demands.
- A closed-loop LLM-guided DRL framework is designed, named LGD. The output of the DRL is encapsulated into a prompt and then fed back to the LLM, which refines the reward function to better guide the next training of the DRL. Furthermore, a novel dueling double deep Qnetwork (D3QN) is employed as the DRL within the LGD framework, leading to the proposal of the LGD-D3QN algorithm. To our knowledge, this is the first time that LLM-guided DRL design rewards has been applied to multi-cluster MEC.
- The performances of five popular LLMs: DeepSeek-R1, GPT-4o, Claude-3.7-Sonnet, Llama-3.1-70B, and Qwen2.5, are compared within the LGD framework, and the impact of the tokenization mechanism on system performance is analyzed.

This paper is structured as follows: Section II outlines the system model; Section III discusses the problem formulation; Section IV introduces the LGD framework and the LGDD3QN algorithm; Section V provides the simulation results, while Section VI offers the conclusion.

## II. SYSTEM MODEL

Fig. 1. Multi-UAV-assisted multi-cluster MEC network.

<!-- image -->

The system model of multi-UAV-assisted multi-cluster MEC network is illustrated in Fig. 1, where U UAVs equipped with MEC servers assist M human users as well as N IoT devices. Each cluster contains at least one UAV. These devices have different computing demands, denoted as D m and D n respectively. v h u,t and v v u,t represent the horizontal and vertical flight speeds of the UAV u at time slot t , respectively. The 3D coordinate of IoT device n , human user m , and UAV u at time slot t are Q n,t ∆ = ( x n,t , y n,t , 0) , Q m,t ∆ = ( x m,t , y m,t , 0) , and Q UAV u,t ∆ = ( x UAV u,t , y UAV u,t , H UAV u,t ) , where n ∈ N = { 1 , 2 , 3 . . . N } , m ∈ M = { 1 , 2 , 3 . . . M } , t ∈ T = { 1 , 2 , 3 . . . T } , and H UAV u,t denotes the altitude of UAV u at time slot t , u ∈ U = { 1 , 2 , 3 . . . U } . Once the UAV fulfills all computing requirements of IoT devices and human users, the task can be terminated. The probability that the LoS link between the IoT device n and the UAV u remains unobstructed at the time slot t is

<!-- formula-not-decoded -->

where d u,n,t denotes the distance between the IoT device n and the UAV u at time slot t . a and b , which are specific to the environment, are obtained from [10]. Similarly, the probability that the LoS link between the human user m and the UAV u being unobstructed at the time slot t is

<!-- formula-not-decoded -->

where d u,m,t is the distance between the human user m and the UAV u at time slot t . The channel gain from the IoT device n to the UAV u at time slot t is denoted by h u,n,t , and h u,m,t represents the channel gain from the human user m to the UAV u at time slot t [2]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where α 1 represents the received power at a reference distance of 1 meter for a transmission power of 1 W. As a result, the uplink data rate from the IoT device n to the UAV u at time slot t can be represented as

<!-- formula-not-decoded -->

where B is the bandwidth, α u,n,t is the association factor between the IoT device n and the UAV u at time slot t , taking values in { 0 , 1 } . P n is the transmit power of the IoT device n , and σ 2 denotes the power density of additive white Gaussian noise. Similarly, the data transmission rate between the human user m and the UAV u at time slot t is

<!-- formula-not-decoded -->

where P m is the transmit power of the human user m , α u,m,t takes values in { 0 , 1 } representing the association factor between the UAV u and the human user m . The amount of tasks that the UAV u is tasked with handling in time slot t is D u,t . In time slot t , the energy consumption of the central processing unit (CPU) for the UAV u is defined as

<!-- formula-not-decoded -->

where τ denotes the duration of each time slot, f C u denotes the CPU frequency, κ is a factor that is influenced by the effective switched capacitance of the CPU architecture, and C C u is the number of CPU cycles required to process a single bit of data. In time slot t , the flight energy consumption of the UAV u is

<!-- formula-not-decoded -->

where P d / a , P bla , P ind , U tip , v 0 , G , ρ , s , and d 0 are all dynamic parameters involved in UAV flight energy consumption [3]. Consequently, the total system energy consumption at time slot t can be expressed as

<!-- formula-not-decoded -->

where E I t and E H t represent the transmit power of IoT devices and human users, respectively.

## III. PROBLEM FORMULATION

Building on the analysis above, the system energy efficiency for each time slot t can be expressed as

<!-- formula-not-decoded -->

To maximize the average energy efficiency of the system, the optimization problem P 1 is formulated as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where constrains (12) and (13) limit the flight speed of each UAV in the horizontal and vertical directions, while (14) to (16) restrict their 3D coordinates. Constraints (17) and (18) define the allocation factors, and (19) ensures that each UAV communicates with only one MEC node within a time slot. Finally, (20) and (21) indicate that the system must satisfy the computing demands of all MEC nodes across time slots.

## IV. PROPOSED LGD FRAMEWORK AND LGD-D3QN ALGORITHM

Fig. 2. Flowchart of the LGD framework algorithm.

<!-- image -->

The LGD framework is shown in Fig. 2, and the specific process is as follows:

- 1. Initial input: Firstly, the description of the environment and the task is input into the LLM as the initial prompt.
- 2. Initial reward function: Utilizing prompt engineering enables LLMs to comprehend the task description outlined in the initial prompt, including the objectives and constraints of the task. Subsequently, the LLM formulates an initial reward function based on this prompt. Taking DeepSeek-R1 as an example, the following reward function is designed:

<!-- formula-not-decoded -->

U

∑

(

max

u

=1

+max

(

0

0

, v

, v

h

u,t

h

min

-

-

v

v

h

max

h

+max

)

u,t

+max

(

0

(

0

, v

, v

v

u,t

v

min

-

-

v

v

v

max

v

u,t

) )

)

,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where λ 1 , λ 2 , and λ 3 are the weights of speed penalty P speed , boundary penalty P bounds , and task penalty P task , respectively.

(

)

P

speed

=

- 3. Parameter prompt: Encapsulating the environment parameters and the initial reward function as a parameter prompt for input into the LLM.
- 4. Reward function: The LLM further evaluates the weight settings in the reward function based on the parameter prompt, and generates a new reward function.
- 5. Training: Guiding DRL training with reward function generated by the LLM.
- 6. Result: DRL outputs results based on the new reward function.
- 7. Feedback prompt: The output of the DRL is encapsulated into feedback prompt.
- 8. Reward function fine-tuning: The feedback prompt is input into the LLM to refine the reward function.
- 9. Final output: The iteration stops when the output of DRL is deemed sufficiently good (as judged by the LLM) or when the preset maximum number of iterations is reached. The best performance across all iterations is then returned as the final output.

By applying the D3QN as a DRL method, the LGDD3QN algorithm is obtained. D3QN can effectively reduce the estimation bias of Q-values by decoupling the action advantage from the state value, thereby improving the stability and efficiency of learning. The specific implementation of the D3QN will not be elaborated upon here and can be referenced in our previous work [11]. In the LGD-D3QN algorithm, each UAV is considered as an agent. The state of each agent includes the 3D coordinates of the UAV, the flight speed, and the association factor between the UAV and the MEC node. The action space of the agent consists of the following parts:

1. Adjustment of the horizontal flight speed, represented as ∆ v h u,t ∈ { v 1 , -v 1 , 0 } , where v 1 is the speed variation per time slot.
2. Adjustment of the vertical flight speed, represented as ∆ v v u,t ∈ { v 1 , -v 1 , 0 } .
3. Horizontal movement action, represented as ∆ L u,t ∈ {( v h u,t t, 0 ) , ( -v h u,t t, 0 ) , ( 0 , v h u,t t ) , ( 0 , -v h u,t t ) , (0 , 0) } .
4. Vertical movement action, represented as ∆ H u,t { v v u,t t, -v v u,t t, 0 } .
5. ∈
6. Selection of association factor with the human user m , represented as α u,m,t ∈ { 0 , 1 } .
7. Selection of association factor with the IoT device n , represented as α u,n,t ∈ { 0 , 1 } .

Every agent shares the same global reward. Only when the entire group performs well can each agent obtain a high return. This encourages them to explore behaviors that are beneficial to the group, even if these behaviors may be suboptimal for individuals in the short term.

## V. SIMULATION RESULT

For a fair comparison, all DRL hyperparameters and the initial prompts fed into the LLM are kept consistent. The operating range of UAVs is (0 m ∼ 1000 m, 0 m ∼ 1000 m, 100 m ∼ 150 m), v 1 = 1 m/s. According to [2], D m = 1 ∼ 10 Mbits, D n = 1 ∼ 10 Mbits, α 0 = -50 dBm, κ = 10 -28 , C C u =

200, and f C u = 3 GHz. According to [3], a = 9.61, b = 0.16, P bla = 79.86 W, ρ = 1.225 kg/m, s = 0.05, G = 0.503 m 2 , P d / a = 11.46 W, U tip = 120 m/s, v 0 = 4.3 m/s, d 0 = 0.6, and σ 2 = -169 dBm/Hz.

Fig. 3. Energy efficiency curves of the LGD-D3QN with different LLMs.

<!-- image -->

Fig. 4. CDF of energy efficiency for the LGD-D3QN with different LLMs.

<!-- image -->

Fig. 3 and Fig. 4 compare the impact of reward functions generated by different LLMs on the D3QN training results in the LGD-D3QN algorithm. Evidently, the utilization of DeepSeek-R1 in the LLM provides the most significant boost in system energy efficiency. To demonstrate the superiority of LLM in reward function generation, a comparison is made with rewards designed by two human experts, where human 1 directly used energy efficiency as the reward function. Human 2 adds a weight less than one on the basis of human 1. If the agent does not satisfy all the constraints, the reward is calculated by multiplying the energy efficiency by this weight, resulting in a penalty. As shown in Fig. 4, LGD-D3QN can achieve an energy efficiency improvement of up to 43.5% compared to human expert-driven DRL.

Fig. 5. Energy efficiency curves of the LGD framework with different DRLs.

<!-- image -->

Fig. 5 compares the energy efficiency improvements of the LGD framework when utilizing different DRL methods. To ensure a fair comparison, LGD-D3QN, LGD-DDQN, and LGD-DQN all adopt DeepSeek-R1 as the LLM. The difference is that the DRL methods of these algorithms are D3QN, DDQN, and DQN. Compared with DDQN and DQN, D3QN addresses the issues of overestimation and unstable convergence. It is evident that the LGD-D3QN yields the largest energy efficiency improvement, which can be attributed to the superiority of the D3QN algorithm.

Fig. 6. The number of tokens for prompt segmentation in different LLMs.

<!-- image -->

The number of tokens divided by LLMs for different prompts is shown in Fig. 6. It is evident that Qwen-2.5 exhibits the highest number of prompt divisions, which stems from its subword-level tokenization rules that inherently possess finegrained segmentation properties. However, an excessive number of tokens may lead to information fragmentation, making it difficult for the model to capture long-range dependencies or process the prompt effectively, ultimately impacting the quality of the generated reward function. Compared to other LLMs, DeepSeek-R1 has the fewest tokens generated from the prompt division and achieves the best energy efficiency improvement. This is due to the fact that, in certain cases, fewer tokens can lead to more efficient information encoding, enabling the model to better capture key information and generate a more reasonable reward function structure. Therefore, investigating the impact of tokenization on LLM behavior is expected to be a key focus of future research.

## VI. CONCLUSION

A closed-loop LLM-guided DRL framework is proposed in this paper, and is applied within a multi-cluster MEC network to evaluate its effectiveness. Different LLMs and DRL methods are introduced into the LGD framework to comprehensively evaluate their effects on improving system energy efficiency. Compared with human experts, the LGD framework can significantly improve system energy efficiency. In the future, modeling of inter-cluster interactions, task migration, or communication overhead in multi-cluster UAVs will be taken into consideration.

## REFERENCES

- [1] P. Mach and Z. Becvar, 'Mobile Edge Computing: A Survey on Architecture and Computation Offloading,' IEEE Commun. Surveys Tuts., vol. 19, no. 3, pp. 1628-1656, thirdquarter 2017.
- [2] Z. Kuang, Y. Pan, F. Yang, and Y. Zhang, 'Joint Task Offloading Scheduling and Resource Allocation in AirCGround Cooperation UAVEnabled Mobile Edge Computing,' IEEE Trans. Veh. Technol., vol. 73, no. 4, pp. 5796-5807, April 2024.
- [3] H. Mei, K. Yang, Q. Liu, and K. Wang, '3D-Trajectory and PhaseShift Design for RIS-Assisted UAV Systems Using Deep Reinforcement Learning,' IEEE Trans. Veh. Technol., vol. 71, no. 3, pp. 3020-3029, March 2022.
- [4] M. Li, N. Cheng, J. Gao, Y. Wang, L. Zhao, and X. Shen, 'EnergyEfficient UAV-Assisted Mobile Edge Computing: Resource Allocation and Trajectory Optimization,' IEEE Trans. Veh. Technol., vol. 69, no. 3, pp. 3424-3438, March 2020.
- [5] Z. Zhang, Q. Zhang, J. Miao, F. R. Yu, F. Fu, J. Du, and T. Wu, 'EnergyEfficient Secure Video Streaming in UAV-Enabled Wireless Networks: A Safe-DQN Approach,' IEEE Trans. Green Commun.Netw., vol. 5, no. 4, pp. 1892-1905, Dec. 2021.
- [6] C. Liu, Y. Zhong, R. Wu, S. Ren, S. Du, and B. Guo, 'Deep Reinforcement Learning Based 3D-Trajectory Design and Task Offloading in UAV-Enabled MEC System,' IEEE Trans. Veh. Technol., vol. 74, no. 2, pp. 3185-3195, Feb. 2025.
- [7] A. T. Neumann, Y. Yin, S. Sowe, S. Decker, and M. Jarke, 'An LLMDriven Chatbot in Higher Education for Databases and Information Systems,' IEEE Trans. Educ., vol. 68, no. 1, pp. 103-116, Feb. 2025.
- [8] S. Sun, R. Liu, J. Lyu, J. Yang, L. Zhang, and X. Li, 'A large language model-driven reward design framework via dynamic feedback for reinforcement learning,' arXiv preprint arXiv:2410.14660, 2024.
- [9] T. Xie, S. Zhao, C. H. Wu, Y. Liu, Q. Luo, V. Zhong, Y. Yang, and T. Yu, 'Text2reward: Reward shaping with language models for reinforcement learning,' arXiv preprint arXiv:2309.11489, 2023.
- [10] A. Al-Hourani, S. Kandeepan, and S. Lardner, 'Optimal LAP Altitude for Maximum Coverage,' IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569-572, Dec. 2014.
- [11] Y. Yao, K. Lv, S. Huang and W. Xiang, '3D Deployment and Energy Efficiency Optimization Based on DRL for RIS-Assisted Air-to-Ground Communications Networks,' IEEE Trans. Veh. Technol., vol. 73, no. 10, pp. 14988-15003, Oct. 2024.
