---
title: "Large Language Model-Empowered Energy-Efficient Multi-UAV-Assisted MEC Heterogeneous Networks"
authors: "Ke Lv , Student Member, IEEE , Sai Huang , Senior Member, IEEE , Yuanyuan Yao , Member, IEEE , Weiwei Jiang , Senior Member, IEEE , and Zhiyong Feng , Senior Member, IEEE , Ke Lv (Student Member, IEEE) received the B.E. and M.S. degrees from Beijing Information Science and Technology University, Beijing, China, in 2021 and 2024, respectively. He is currently pursuing the Ph.D. degree with Beijing "
doi: "10.1109/TCCN.2025.3645407"
received: "6 May 2025"
accepted: "7 December 2025"
published: "17 December 2025"
keywords: "Artificial general intelligence, large language model, deep reinforcement learning, unmanned aerial vehicle, mobile edge computing"
---

## Large Language Model-Empowered Energy-Efficient Multi-UAV-Assisted MEC Heterogeneous Networks

Ke Lv , Student Member, IEEE , Sai Huang , Senior Member, IEEE , Yuanyuan Yao , Member, IEEE , Weiwei Jiang , Senior Member, IEEE , and Zhiyong Feng , Senior Member, IEEE

Abstract -The artificial general intelligence (AGI) based on large language models (LLMs) and deep reinforcement learning (DRL) possesses cross-domain empowerment capabilities, offering task scheduling and resource allocation in mobile edge computing (MEC), presenting significant potential. This paper proposes an LLM-driven DRL framework named L2D2, which autonomously generates reward functions for DRL through LLMs and enables dynamic model optimization through a self-refinement loop mechanism. The reward function within the L2D2 framework can adjust the strategy based on environmental feedback, eliminating the need for manual redesign in complex low-altitude scenarios and reducing debugging costs. To validate the performance of L2D2, the framework is utilized in a multi-unmanned aerial vehicle (UAV)-assisted MEC heterogeneous network operating in the low-altitude airspace to enhance system energy efficiency. A novel dueling double deep Q-network (D3QN) is utilized as the DRL method within L2D2, named the L2D2-D3QN algorithm. To evaluate its effectiveness in enhancing system energy efficiency, a comprehensive comparison is conducted across various LLMs, including Deepseek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-2.5. The simulation results demonstrate that the L2D2-D3QN algorithm achieves up to 56% higher energy efficiency compared to DRL with human-designed reward function. Furthermore, the influence of LLM tokenization strategies on the performance of LLM-driven DRL is also explored.

Index Terms -Artificial general intelligence, large language model, deep reinforcement learning, unmanned aerial vehicle, mobile edge computing.

## I. INTRODUCTION

T HE low-altitude economy, defined as an economic paradigm operating within 100 to 1000 meters above ground, has emerged as a strategic industry, attracting

Received 6 May 2025; revised 4 September 2025 and 30 October 2025; accepted 7 December 2025. Date of publication 17 December 2025; date of current version 28 January 2026. This work was supported in part by the National Natural Science Foundation of China under Grant (62422103, 62321001, 62171045, 62201090). The associate editor coordinating the review of this article and approving it for publication was J. Wang. (Corresponding author: Sai Huang.)

Ke Lv, Sai Huang, Weiwei Jiang, and Zhiyong Feng are with the Key Laboratory of Universal Wireless Communications, Ministry of Education, Beijing University of Posts and Telecommunications, Beijing 100876, China (e-mail: kelv@bupt.edu.cn; huangsai@bupt.edu.cn; jww@bupt.edu.cn; fengzy@bupt.edu.cn).

Yuanyuan Yao is with the Key Laboratory of Information and Communication Systems, Ministry of Information Industry, and the Key Laboratory of Modern Measurement and Control Technology, Ministry of Education, Beijing Information Science and Technology University, Beijing 100101, China (e-mail: yyyao@bistu.edu.cn).

Digital Object Identifier 10.1109/TCCN.2025.3645407

widespread global attention. With line-of-sight (Lo S) communication links and high mobility, the unmanned aerial vehicle (UAV) has emerged as a central enabling technology for the low-altitude economy [1], [2], [3]. By 2030, it is projected that the commercial UAV sector will reach a value of $260 billion, driving the rapid evolution of low-altitude airspace into a vital third dimension for digital infrastructure supporting logistics, agriculture, and public safety [4]. However, constructing and efficiently operating this new infrastructure fundamentally depends on reliable and scalable communication capabilities, which are essential for ensuring connectivity and facilitating data exchange among various systems and users.

To overcome the computing and transmission bottlenecks in low-altitude communication scenarios, UAV-assisted mobile edge computing (MEC) has emerged [5]. Unlike conventional cloud-centric architectures, UA V-assisted MEC deploys computational nodes directly on aircraft, alleviating the computational pressure on core network [6]. By enhancing task processing efficiency and optimizing network resource utilization, it has become a vital technical solution driving the development of this field. This innovative approach facilitates a variety of applications, including real-time video monitoring, delivery drones, and smart agricultural management, advancing the development of the low-altitude economy [7], [8], [9].

## A. Related Works

In the low-altitude UAV-assisted MEC systems, the limited flight endurance of UAVs critically constrain system operational duration, making energy consumption a crucial factor in determining overall performance sustainability. To achieve a balance between maximizing system throughput and minimizing overall energy consumption, energy efficiency has emerged as a fundamental metric. To maximize energy efficiency, Li et al. [10] employed the Dinkelbach algorithm and successive convex approximation (SCA) method to jointly optimize user transmit power, two-dimensional (2D) UAV trajectory, and computational load allocation. Qin et al. [11] introduced a reconfigurable intelligent surface (RIS) into UAV-assisted MEC systems and developed a double-loop iterative algorithm to maximize system energy efficiency. To maximize the energy efficiency of an RIS-assisted UAVenabled MEC system with non-orthogonal multiple access (NOMA) protocol, Qin et al. [12] employed block coordinate descent (BCD) method along with the Dinkelbach algorithm.

2332-7731 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.

Similarly, Liu et al. [13] explored the UAV-assisted NOMAMEC architecture, utilizing the SCA method and Dinkelbach algorithm to maximize energy efficiency. Qian et al. [14] assumed the presence of eavesdroppers in the environment and aimed to maximize system energy efficiency by optimizing the 2D UAV trajectory, UAV transmit power, local computation ratio, and terminal scheduling.

As the complexity of system models increases, the analytical solution of objective functions faces significant challenges. Conventional optimization algorithms exhibit notable limitations in terms of computational efficiency, convergence, and solution quality. Fortunately, the emerging deep reinforcement learning (DRL) provides an innovative solution to this problem. DRL combines deep learning (DL) with reinforcement learning (RL) to enable agents to learn optimal strategies in complex environments through trial-and-error mechanisms and reward feedback [15], [16], [17]. With this capability, DRL can be effectively employed to optimize resource allocation in MEC. Li et al. [18] utilized Q-learning from RL to achieve dynamic coordination among heterogeneous UAVs, providing better services for internet of things (Io T) devices with different tasks. Compared to existing RL algorithms, Zhang et al. [19] employed deep Q-learning network (DQN) from DRL to jointly optimize multi-UAV trajectories, power allocation, and video-level selection, achieving maximum energy efficiency. Furthermore, Wu et al. [20] optimized resource allocation in MEC, joint control of UAVs, and passive beamforming through double deep Q-learning network (DDQN) to maximize the system energy efficiency. Considering three-dimensional (3D) multi-UAV trajectories, Liu et al. [21] employed DDQN and convex optimization techniques to develop near-optimal multi-UAV trajectories and task offloading strategies, resulting in improved energy efficiency.

## B. Contributions

The core elements of the aforementioned works are summarized in Table I. Related works [10], [11], [12], [13], [14], [18], [19], and [20] restrict UA V to 2D space, failing to explore the full potential of UA V in 3D environments. Additionally, related works [10], [11], [12], [13], [19], [20], and [21] focus solely on single UAV scenarios, neglecting the collaborative capabilities of multi-UAV. The traditional optimization methods employed in [10], [11], [12], [13], and [14] have significant limitations, making it challenging to address more complex problems. Although works [19], [20], [21] utilize DQN and DDQN, challenges such as overestimation and unstable convergence persist. In fact, the quality of the reward function design is crucial to the training effectiveness of DRL. An unreasonable reward value design can negatively impact the learning efficiency of the agent. The increasing complexity of network structures presents significant challenges in designing reward functions.

The anticipated emergence of artificial general intelligence (AGI) is expected to achieve significant breakthroughs in addressing the above problems in the future. The breakthrough in language comprehension and generation capabilities represents a critical milestone in achieving AGI, which is exactly the value of large language models (LLMs) [22], [23]. As one of the foundational technologies supporting AGI development, LLMs not only master the complex grammatical structure of human language through deep training of massive text data, but also establish a knowledge network architecture comprising trillions of parameters [24], [25], [26]. This probabilistic reasoning based network enables machines to capture semantic associations, deconstruct logical relationships, and even demonstrate elementary common sense reasoning capabilities. Therefore, this capability of LLMs is well-suited for addressing the design of reward functions in complex MEC networks. To the best of our knowledge, there is less works on leveraging DRL with LLM-designed rewards to achieve resource allocation in MEC. The progress of models such as GPT-4, Llama, and Deep Seek marks a critical moment in which artificial intelligence (AI) systems have reached near-human levels in language interaction, laying a significant foundation for the development of AGI with general cognitive capabilities. To explore AGI, we propose an LLM-driven DRL framework and implement it within the low-altitude economy to verify its performance. The future mobile communication and computing environments are inherently heterogeneous, with user equipment having different energy states and quality of service (Qo S) requirements [27]. Therefore, this work considers a multi-UAV-assisted MEC heterogeneous network that includes human-type users as well as constrained application protocol (Co AP)-based Io T devices. The focus is on optimizing the 3D trajectories of multi-UAVs and user association factors to maximize system energy efficiency. The main contributions of this paper are summarized as follows:

- A novel LLM-driven DRL framework, termed L2D2, is proposed that autonomously generates dynamic reward functions through semantic understanding of network states. To the best of our knowledge, this work establishes the first LLM-based reward designing into wireless resource allocation for MEC, effectively addressing the limitations of manual reward engineering in complex low-altitude environments. A closed-loop self-refinement mechanism is designed that leverages the synergy between real-time performance evaluation and parameter correction, facilitating the continuous evolution of the algorithm.
- This work experimentally investigates the tokenization mechanism of LLMs for prompts and their effects on decision-making performance in DRL. Focusing on the mainstream LLM architectures, including Deep Seek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen2.5, the tokenizers are evaluated based on the number of tokens segmented from prompts. The impact of reward functions generated by various LLMs on DRL training is further analyzed.
- The L2D2 framework innovatively integrates dueling double deep Q-network (D3QN) with LLM, termed the L2D2-D3QN algorithm, effectively overcoming the inherent overestimation and unstable convergence associated with traditional DQN and DDQN. Moreover, comprehensive experiments are designed to explore the capabilities

TABLE I RELATED WORK ON UAV-ASSISTED MEC

of LLM-driven DRL. Compared to the DRL based on human-designed reward function, the LLM-driven DRL can provide up to a 56% improvement in system energy efficiency.

The rest of this paper is organized as follows. Section II describes the system model for multi-UAV-assisted MEC heterogeneous network. Building upon this foundation, Section III formulates the energy efficiency optimization problem with multiple constraints. Section IV further describes the proposed L2D2 framework and L2D2D3QN algorithm. Simulation results and analysis are presented in Section V, followed by the conclusions in Section VI.

## II. SYSTEM MODEL

The system model of multi-UAV-assisted MEC heterogeneous network is depicted in Fig. 1, where U cognitive UAVs assist M human-type users as well as N Io T devices based on Co AP for MEC. For human-type users, the UAV can directly compute the tasks, while for Io T devices, the UAV requires AMC before computation. In addition, these devices have different computing demands, which are represented by D m and D n respectively. v h u,t and v v u,t are defined as the horizontal and vertical flight speeds of the UA V u at time slot t , respectively. The 3D spatial coordinate positions of Io T device n , human-type user m , and UAV u at time slot t are defined by Q n,t ∆ = ( x n,t , y n,t , 0) , Q m,t ∆ = ( x m,t , y m,t , 0) , and Q UAV u,t ∆ = ( x UAV u,t , y UAV u,t , H UAV u,t ) , where n ∈ N = { 1 , 2 , 3 . . . N } , m ∈ M = { 1 , 2 , 3 . . . M } , t ∈ T = { 1 , 2 , 3 . . . T } , and H UAV u,t denotes the altitude of UAV u at time slot t , u ∈ U = { 1 , 2 , 3 . . . U } . The mission can be terminated once UAVs fulfill the computing demands of all Io T devices and humantype users.

## A. Signal Transmission Model

Considering the existence of ground obstacles, the likelihood of the Lo S link between the Io T device n and the UAV

Fig. 1. Multi-UAV-assisted MEC heterogeneous network.

<!-- image -->

u remains unblocked at the time slot t is modeled below [28]:

<!-- formula-not-decoded -->

where d u,n,t represents the Euclidean distance between the Io T device n and the UAV u at time slot t . The parameters a and b , which are environment-specific, are derived from [28]. Likewise, the likelihood of the Lo S link between the human-type user m and the UAV u being unblocked at the time slot t is

<!-- formula-not-decoded -->

where d u,m,t denotes the Euclidean distance between the human-type user m and the UAV u at time slot t . The channel gain from the Io T device n to the UAV u at time slot t is denoted by h u,n,t , and h u,m,t represents the channel gain from the human-type user m to the UAV u at time slot t [29]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where α 1 corresponds to the received power at a 1-meter reference distance for a 1 W transmit power. Consequently, the uplink data rate between the Io T device n to the UAV u at time slot t can be expressed as

<!-- formula-not-decoded -->

where α u,n,t represents the association factor between the Io T device n and the UAV u at time slot t , taking values in { 0 , 1 } . P CC u,n,t indicates the probability that the signal modulation of the Io T device n can be correctly recognized by the UAV u at time slot t , P n denotes the transmit power of the Io T device n , σ 2 denotes the power density of additive white Gaussian noise, and W represents the bandwidth. The adoption of connectionless user datagram protocol (UDP) effectively reduces communication overhead, enhancing the applicability of Co AP-based Io T devices [30]. This enables Io T devices to transmit signals utilizing various modulation techniques. The Rep CCNet has demonstrated impressive performance in AMC [31]. Thus the Rep CCNet is integrated into UAVs to enhance their cognitive capabilities. For human-type users with uniform signal modulation, AMC is not required to be implemented by UAVs. Consequently, the data transmission rate between the user m and the UAV u at time slot t can be expressed as

<!-- formula-not-decoded -->

where α u,m,t takes values in { 0 , 1 } to indicate the association factor between the human-type user m and the UAV u at time slot t . Additionally, P m denotes the transmit power of the human-type user m .

## B. Energy Consumption Model

In time slot t , the amount of tasks that the UA V u is required to handle can be expressed as

<!-- formula-not-decoded -->

where τ denotes the duration of each time slot. Additionally, D R m,t and D R n,t indicate the remaining computing demands for the human-type user m and the Io T device n , respectively. Furthermore, the energy consumption of the central processing unit (CPU) for the UAV u at time slot t is defined as

<!-- formula-not-decoded -->

where f CPU u denotes the CPU frequency, C CPU u refers to the number of CPU cycles needed to process a single bit of data, and κ is a factor that depends on the effective switched capacitance of the CPU architecture. For the UAV u , the flight energy consumption at time slot t is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where P d / a denotes the constant power for ascending or descending. P bla and P ind represent the constant blade profile power and the induced power during hovering, respectively. U tip is the tip speed of rotor blade, and v 0 indicates the average induced velocity of the rotor during hovering. The parameters G and ρ denote the rotor disc area and the air density, respectively. Additionally, s and d 0 represent the rotor solidity and fuselage drag ratio, respectively [32]. Therefore, the total system energy consumption at time slot t is formulated as

<!-- formula-not-decoded -->

where P m and P n respectively characterize the transmit power of human-type users and Io T devices.

## III. PROBLEM FORMULATION

Based on the analysis above, the system energy efficiency for each time slot t can be derived as

<!-- formula-not-decoded -->

Since the objective is to maximize the average energy efficiency of the system, the optimization problem P 1 is formulated as:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where constraints (12a) and (12b) limit the flight speed of each UAV in the horizontal and vertical directions, constraints (12c) to (12e) limit the 3D coordinates of each UAV, constraints (12f) and (12g) represent the allocation factors, constraint (12h) restricts each UA V to communicate with only one object within a time slot. Constraints (12i) and (12j) indicate that the system needs to satisfy the computing demands of all Io T devices and human-type users during total time slots.

## IV. PROPOSED L2D2 FRAMEWORK AND L2D2-D3QN ALGORITHM

To advance the exploration of AGI, we integrate LLM with DRL and propose an LLM-driven DRL framework termed L2D2. The fundamental component of the L2D2 is selfrefinement loop, as depicted in Fig. 2. The flow of the L2D2 is outlined as follows:

- I) Initial input: The initial prompt serves as the input for LLM, containing a description of the environment in which the agents operate as well as the tasks.

2. II) Initial reward function: The LLM generates the initial reward function based on the initial prompt. At this stage, the reward function includes system resource variables ( x 1 , x 2 ) as well as weights ( α , β ).
3. III) Parameter prompt: To obtain the initial values of the weights for the reward function, the parameter prompt is input into the LLM. This prompt contains specific values for the environmental variables, providing reliable references for the LLM to calculate the weights of the reward function.
4. IV) Reward function: The LLM provides the weights for the reward function based on the parameter prompt ( α = 0 . 2 , β = 1 . 5 ). At this point, the reward function no longer includes variables unrelated to the environment in which the agents operate.

- V) Training: The DRL is trained utilizing the reward function provided by the LLM.

6. VI) Result: The results of the DRL are assessed by human experts or the LLM. If the results meet the criteria for satisfaction, they are considered the final output; otherwise, the results are documented in the feedback prompt.
7. VII) Feedback prompt: The feedback prompt outlines the results of the DRL and is utilized to provide feedback to the LLM, facilitating the fine-tuning of the weights in the reward function.
8. VIII) Reward function fine-tuning: After receiving the feedback prompt, the LLM adjusts the weights within the reward function, thereby generating an updated reward function.
9. IX) Final output: The final output includes the ultimate reward function, the system resource allocation strategy, and the results.

Based on the L2D2 framework, we designed the L2D2D3QN algorithm, which utilizes D3QN as the DRL in L2D2. The following subsections will introduce D3QN, the reward design process utilizing LLM, and the algorithmic flow of L2D2-D3QN.

## A. D3QN

To effectively present the D3QN framework, we start by providing a concise overview of DRL fundamentals. As a foundational RL methodology, Q-learning tackles the challenge of identifying optimal policies within Markov decision processes (MDPs) frameworks. This algorithm operates by iteratively estimating the state-action value function Q ( s t , a t ) , which enables agents to determine optimal action selections through direct experience interactions. Crucially, the approach eliminates the need for explicit environmental dynamics knowledge, including transition probabilities or reward mechanisms. The formula of Q ( s t , a t ) is expanded to

<!-- formula-not-decoded -->

where r t is the immediate reward at time slot t , and γ ∈ [0, 1] is a decay factor used to balance the importance of current rewards and future rewards. The objective of Q-learning is to identify a strategy π that maximizes the cumulative discounted reward after the agent takes action a t in any given state s t , with the optimal state-action value function Q ∗ ( s t , a t ) is denoted as

<!-- formula-not-decoded -->

Moreover, it satisfies the Bellman optimality equation :

<!-- formula-not-decoded -->

Q-learning iteratively updates the value of Q ( s t , a t ) through the temporal difference method, gradually approaching state-action value function Q ∗ ( s t , a t ) :

<!-- formula-not-decoded -->

where ¯ α is the learning rate. However, when the state and action spaces are large, storing and updating the Q-table becomes inefficient, as the memory and computation requirements grow exponentially with the dimensionality of the problem. This limitation, known as the curse of dimensionality, makes traditional Q-learning incapable of handling complex tasks. To overcome these challenges, DQN were developed, combining Q-learning with deep neural networks (DNNs) to approximate the Q-function. By leveraging the representational power of neural networks, DQN can efficiently handle high-dimensional state spaces and learn directly from raw input data, enabling breakthroughs in complex tasks. The DQN has the capability of experience replay, allowing it to store historical experiences ( s t , a t , r t , s t +1 ) in a replay buffer. During training, DQN randomly samples from this buffer, breaking data correlation. The DQN consists of two networks: an estimation network with weights Θ and a target network with weights Θ -. The estimation network computes Q ( s t , a t | Θ) , which is employed to approximate Q ( s t , a t ) . Throughout training, only Θ are updated by minimizing the loss function :

<!-- formula-not-decoded -->

Fig. 2. The flowchart of the L2D2 framework.

<!-- image -->

<!-- formula-not-decoded -->

where y DQN t represents the target value, and Θ is copied to Θ -every O steps. However, the max operator employed by the DQN to compute the target Q-value, leading to a overestimation of Q-values. This in turn affects the performance and stability of the policy. To tackle this issue, DDQN was proposed, which decouples action selection from Q-value estimation, significantly reducing the overestimation bias and thereby improving the robustness and convergence efficiency of the algorithm. The target action in DDQN is chosen by the estimation network, whereas the target Q-value is evaluated by the target network. The loss function L (Θ) is defined as :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By decoupling action selection from Q-value estimation, DDQN alleviates the overestimation issue in DQN. Nevertheless, estimating Q ( s t , a t ) for all actions in state s t employing DQN or DDQN can still result in unstable convergence. D3QN is an enhanced variant of DDQN, built upon the dueling network architecture to separate the state value and action advantage functions. Additionally, it incorporates double Q-learning to mitigate the overestimation of Q-values.

The architecture of D3QN is illustrated in Fig. 2. Initially, the input parameters are extracted from the replay buffer of size F and fed into the input layer. After passing through a hidden layer composed of DNNs, relevant features are processed into two distinct streams. One stream corresponds to the state value, which is independent of the action chosen by the agent and solely dependent on the current state s t . The output of this stream indicates the value of the current environment, referred to as the state value function V ( s t ) , which is utilized to evaluate the performance of the agent within that environment. The other stream signifies the advantage of selecting action a t in state s t , known as the action advantage function A ( s t , a t ) . This function evaluates the relative advantage of the agent when selecting an action from A and assesses the significance of action a t in state s t . These streams are represented as V ( s t ∣ ∣ ∣ Θ , ˜ β ) and A ( s t , a t | Θ , ˜ α ) , where Θ , ˜ α , and ˜ β , represent the parameters for the hidden layer (DNNs), the state value function network, and the action advantage function network, respectively.

In contrast to the DQN and the DDQN, the D3QN learns the value and advantage components independently before combining them for the final output. This output Q ( s t , a t ) is expressed as Q ( s t , a t ∣ ∣ ∣ Θ , ˜ α, ˜ β ) , and calculated by the following formula :

<!-- formula-not-decoded -->

where |A| represents the dimension of the action space A . Subtracting the mean of A ( s t , a t | Θ , ˜ α ) ensures the identifiability of the action advantage function, avoiding redundancy between V ( s t ∣ ∣ ∣ Θ , ˜ β ) and A ( s t , a t | Θ , ˜ α ) . Moreover, this separation mitigates the risk of overestimation biases that can occur when combining the two functions. By ensuring that A ( s t , a t | Θ , ˜ α ) is identifiable, D3QN can more accurately evaluate the potential advantages of actions without conflating them with the overall state value. The loss function for D3QN

is defined as follows :

<!-- formula-not-decoded -->

where Θ -, ˜ α -, and ˜ β -, are the parameters of the target network used to estimate the updates for the periodic replications of Θ , ˜ α , and ˜ β within the network.

In the multi-UAV-assisted MEC heterogeneous network, each UAV u is regarded as an agent. The state s u,t , action a u,t , and reward function r t are defined as follows.

- State s u,t : At time slot t , the system state s u,t ∈ S encompasses multiple observations that describe the environment. These observations include the 3D coordinates of the UAV u , the horizontal and vertical flight speeds of the UAV u , the association factor between the UAV u and the human-type user m , the association factor between the UAV u and the Io T device n , the blocking probability of the Lo S link between the UAV u and the human-type user m , the blocking probability of the Lo S link between the UAV u and the Io T device n , and the probability that the UAV u can correctly recognize the signal modulation of the Io T device n . Consequently, the state space for the agent u at time slot t is defined as

<!-- formula-not-decoded -->

- Action a u,t : The UAV u selects action a u,t based on state s u,t , which comprises six components:

1. The adjustment of horizontal flight speed for the UAV u , denoted as ∆ v h u,t ∈ { v b , -v b , 0 } , where v b represents the speed variation per time slot.
2. The adjustment of vertical flight speed for the UA V u , denoted as ∆ v v u,t ∈ { v b , -v b , 0 } .
3. The horizontal movement action of the UAV u , denoted as ∆ L u,t ∈ {( v h u,t t, 0 ) , ( -v h u,t t, 0 ) , ( 0 , v h u,t t ) , ( 0 , -v h u,t t ) , (0 , 0) } . 4. The vertical movement action of the UAV u , denoted as ∆ H u,t ∈ { v v u,t t, -v v u,t t, 0 } .
4. Selection of association factor between the UA V u and the human-type user m , denoted as α u,m,t ∈ { 0 , 1 } .
5. Selection of association factor between the UA V u and the Io T device n , denoted as α u,n,t ∈ { 0 , 1 } .

- Reward r t : The reward for UAVs at time slot t is determined by the LLM, which will be elaborated upon in the subsequent section.

## B. LLM-Empowered Reward Design

When employing LLM for reward function designing, a critical initial step involves enabling the LLM to comprehend the environment and tasks associated with the agents. To achieve this fundamental understanding, the initial prompt provided to the LLM incorporates comprehensive descriptions of both the environmental variables and mission objectives, as visually outlined in Fig. 3. This initial prompt ensures that the LLM establishes appropriate contextual awareness before commencing reward function development. After obtaining the initial reward function, it is essential to further refine the weight values. Taking Deepseek-R1 as an example, after receiving the initial prompt word, it generates the following reward function:

Fig. 3. Initial prompt.

<!-- image -->

<!-- formula-not-decoded -->

Fig. 4. Parameter prompt and feedback prompt.

<!-- formula-not-decoded -->

where P speed indicates the penalty for UAVs violating speed limits, P bounds indicates the penalty for UAVs violating 3D space constraints, and P task represents a penalty for unsatisfied computational requirements. These penalties can be calculated from environmental parameters. Therefore, only the weights λ 1 , λ 2 , and λ 3 remain unknown in the reward function. To further determine the initial values of the reward weights, the parameter prompt containing the environmental parameters is provided to the LLM, as shown in Fig. 4. After obtaining the initial weights of the reward function ( λ 1 = 0 . 1 , λ 2 = 0 . 5 , and λ 3 = 0 . 05 ), the reward function is provided to the D3QN for training. Once the training is complete, the results will serve as feedback prompt to promote the LLM in further fine-tuning the reward function, as shown in Fig. 4. The final reward function is obtained after several iterations. The algorithmic flow of the L2D2-D3QN is presented in Algorithm 1. The computational complexity of the L2D2-D3QN algorithm is O ( |S 1 | · |A 1 | · k ) , where |S 1 | and |A 1 | are the number of states and actions of the L2D2-D3QN algorithm, respectively.

## V. SIMULATION RESULT

To ensure a fair comparison, both the estimation network and target network of the DRL algorithms presented in this paper consist of 2 layers, each containing 20 neurons, maintaining consistent hyperparameters as outlined in Table II. The activity space for UAVs is defined as (0 m to 1000 m, 0 m to 1000 m, 100 m to 150 m), with Io T devices and human-type users distributed randomly. The simulation parameters are detailed in Table III.

To explore the reward functions generated by different LLMs, the Deepseek-R1 1 , GPT-4o 2 , Llama-3.1-70B 3 , Claude-

1 https://deepseek-r1.com/

2 https://openai.com/index/hello-gpt-4o/

3 https://www.llama.com/llama3\_1/

## Algorithm 1 L2D2-D3QN Algorithm

Initialization: Initial prompt, environment parameters, the Θ u and Θ -u of the evaluation network Q u ( · ) and target network Q -( · ) , experience replay buffer F .

u Provide initial prompt to LLM; Provide parameter prompt to LLM; The reward function obtained from LLM is recorded as R 1 ; for k = 1, . . . , K for episode = 1, . . . , E Initialize the system state s 0 ; while t = 1, . . . , T Each agent u randomly selects a u,t with probability ε , otherwise selects a u,t by the training network; Utilize Rep CCNet to obtain P CC u,m,t ; Each agent u calculates the reward based on R k ; Update s u,t to s u,t +1 based on a u,t ; Store sample ( s u,t , a u,t , r u,t , s u,t +1 ) in the experience replay buffer; for u = 1, . . . , U Agent u selects a mini-batch of random samples from the experience replay buffer; Update Θ u by gradient descent step on Eq. (22); Update the target networks every O steps: Θ -u = Θ u ; u = u +1 ; end for if the result meet the criteria for satisfaction break; end if end while end for k = k +1 ; Provide the feedback prompt to LLM and record the reward function obtained as R k ;

end for

TABLE II HYPERPARAMETERS OF THE DRL ALGORITHMS

3.7-Sonnet 4 , and Qwen-2.5 5 are deployed as LLMs in the L2D2 framework. These LLMs are popular for their wide range of applications and robust performance, with excellent generation and comprehension capabilities. The final reward function generated by Deepseek-R1 is as follows:

4 https://www.anthropic.com/claude/sonnet

5 https://chat.qwen.ai/

TABLE III SIMULATION SETTINGS

<!-- formula-not-decoded -->

where P speed indicates the penalty for UAVs violating speed limits, P bounds indicates the penalty for UAVs violating 3D space constraints, and P task represents a penalty for unsatisfied computing demands. The values of λ 1 , λ 2 , and λ 3 are 0.25, 0.4, and 0.01, respectively.

The final reward function generated by GPT-4o is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where P GPT speed indicates the penalty for UAVs violating speed limits, P GPT bounds indicates the penalty for UAVs violating 3D space constraints, and P GPT task represents a penalty for unsatisfied computational requirements. The values of λ 1 , λ 2 , and λ 3 are 0.1, 0.5, and 1, respectively. It is evident that Deepseek R1 and GPT-4o have similar idea in constructing the reward function. However, their differing perceptions of the feedback results ultimately lead to different fine-tuned reward weights.

In contrast to Deepseek-R1 and GPT-4o, the Llama-3.170B introduces a distinct approach when generating the reward function. It separates the penalties for UA Vs that exceed speed limits from those that violate 3D space constraints. Additionally, Llama-3.1-70B removes the penalty of unsatisfied computing demands and instead employs completed tasks as a positive reward to motivate the agent. The final reward function generated by Llama-3.1-70B is shown below:

<!-- formula-not-decoded -->

where P Llama hspeed , P Llama vspeed , P Llama xbound , P Llama ybound , and P Llama zbound represent the penalties incurred by UA Vs for violating the horizontal speed constraint, vertical speed constraint, x-axis boundary constraint, y-axis boundary constraint, and z-axis boundary constraint, respectively. The values of λ 1 , λ 2 , λ 3 , λ 4 , λ 5 , λ 6 , and λ 7 are 0.05, 0.5, 0.5, 0.5, 0, 0, and 0.1, respectively.

Compared to the LLMs described previously, the final reward function generated by Claude-3.7-Sonnet is more complex:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where C Claude demand is denoted as the reward progress toward meeting computing demands, and C Claude con penalizes constraint violations. The structure of C Claude demand is unique, as the sum of the first two components indicates the proportion of the currently fulfilled computing demand relative to the total demand, serving as a positive incentive. The third component reflects the proportion of the current time relative to the total time, representing the percentage of time consumed. By adopting percentage-based metrics, unit dependency issues are eliminated, enabling standardized evaluation across tasks of varying scales and timeframes. Therefore, C Claude demand essentially measures the efficiency of task completion. When it is positive, it means that the task is completed faster than the time consumed. In contrast, when it is negative, it means that the task is completed behind the time schedule. The values of λ 1 , λ 2 , λ 3 , P 1 , and P 2 are 1.8, 1.2, 6, 1.5, and 1, respectively.

The Qwen-2.5 further decomposes the penalty for unsatisfied computational requirements:

<!-- formula-not-decoded -->

<!-- image -->

Fig. 5. Flight trajectories of UA Vs (LLM = Deepseek-R1).

Fig. 6. Flight trajectories of UA Vs (LLM = GPT-4o).

<!-- image -->

Fig. 7. Flight trajectories of UA Vs (LLM = Llama-3.1-70B).

<!-- image -->

<!-- formula-not-decoded -->

where P Qwen demand represents demand satisfaction penalty, and P Qwen con represents constraint violation penalty. The values of λ m , λ n , γ h , γ v , γ x , γ y and γ z are 4, 4, 4.06, 5.64, 0, 0, and 0.44, respectively. When LLMs in the L2D2 algorithm are Deepseek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-2.5, the corresponding UAVs trajectories are shown in Fig. 5, Fig. 6, Fig. 7, Fig. 8, and Fig. 9.

## A. Comparison With Different LLMs

Different LLM designs feature distinct reward function constructions and varying weights, resulting in different reward values upon convergence of the L2D2-D3QN algorithm. Therefore, it is unfair to compare the reward values of L2D2D3QN driven by different LLMs. Although the designs of the reward functions differ, the energy efficiency indicators that the LLMs ultimately optimize adhere to a unified standard.

<!-- image -->

Fig. 8. Flight trajectories of UA Vs (LLM = Claude-3.7-Sonnet).

Fig. 9. Flight trajectories of UA Vs (LLM = Qwen-2.5).

<!-- image -->

Fig. 10. Average energy efficiency curves of L2D2-D3QN with different LLMs.

<!-- image -->

Consequently, it is practical significance to compare different LLM schemes based on system energy efficiency. Fig. 10 presents the convergence curves of average energy efficiency for L2D2-D3QN across different LLMs and human-designed reward functions.

The reward function designed by human-1 is identical to the reward functions presented in [19] and [21], as shown below :

<!-- formula-not-decoded -->

This design does not consider the punishment of constraints on the agent. In addition, the reward function designed by human-2 is the same as in [20]:

<!-- formula-not-decoded -->

Fig. 11. CDF of average energy efficiency for L2D2-D3QN with different LLMs.

<!-- image -->

where δ t = 1 indicates that the agents satisfy all constraints, while δ t = 0 signifies that the agents do not meet all the constraints. The discount factor ω = 0 . 5 signifies that the reward decreases when the agent fails to comply with the constraint. Compared to other LLMs, the curve of Deep Seek-R1 is the most stable and offers the highest improvement in energy efficiency. In addition, compared with the human-designed reward functions, the reward functions designed by LLMs can provide more significant improvements in system energy efficiency.

Fig. 11 presents the cumulative distribution function (CDF) of average energy efficiency, where the reward functions in L2D2-D3QN is designed by Deepseek-R1, GPT-4o, Llama3.1-70B, Claude-3.7-Sonnet, Qwen-2.5, and humans. The corresponding value where CDF = 1 represents the maximum energy efficiency achievable by L2D2-D3QN. As shown in the figure, compared to GPT-4o, Llama-3.1-70B, Claude3.7-Sonnet, Qwen-2.5, human-1, and human-2, L2D2-D3QN driven by Deepseek-R1 can achieve energy efficiency improvements of 7%, 9%, 16%, 17%, 30%, and 56%, respectively, highlighting the advantages of Deepseek-R1 in reward function design. As a result, if no penalties are considered for the agents, as seen in the case of human-1, the learning performance of agents will be poor. On the contrary, if the considerations are overly complex, as seen in the case of Qwen-2.5, it becomes challenging to achieve excellent reward parameters through fine-tuning.

Additionally, the effect of different LLM token mechanisms on energy efficiency improvement is also explored. Fig. 12 illustrates the number of tokens for different LLMs, categorized by initial prompt, parameter prompt, and feedback prompt, with token counts determined by Tiktokenizer 6 and Token Counter 7 . For different LLMs, the word count of the initial prompt provided to them is identical. It can be seen that Deep Seek-R1 divides the initial prompt into the lowest number of tokens. Since different LLM designs employ varying reward functions, the word counts for parameter prompt and feedback prompt differ slightly. Qwen-2.5 generates the highest number of token divisions for prompts due to its subword-level tokenization, which features fine-grained segmentation. The differences in the number of tokens generated by tokenizers of different LLMs for the same text can impact the ability of model to handle context. For instance, a higher token count may fragment information, making it difficult for the model to capture long-range dependencies or process prompts efficiently, ultimately affecting the quality of the generated reward function. Compared with other LLMs, Qwen-2.5 has the highest number of token divisions for prompts, and its generated reward function is also the most complex. An overly complex reward function makes it challenging to fine-tune the reward weights of Qwen-2.5, ultimately resulting in low system energy efficiency. In contrast, Deep Seek-R1 primarily utilizes a word-based segmentation strategy, which involves dividing the input text into complete words while minimizing the total number of tokens. This approach preferentially utilizes whole words or combinations of high-frequency phrases to divide the input text, which results in a reduced number of token divisions. In some scenarios, fewer tokens can lead to more efficient information encoding, allowing the model to better capture key information and generate a more reasonable reward function structure. Therefore, if an LLM can dynamically adapt its tokenization strategies to suit different tasks, it has the potential to achieve significant performance improvements. This is expected to become a key focus of future research.

6 https://tiktokenizer.vercel.app/

7 https://tokencounter.org/

Fig. 12. The number of tokens for prompt segmentation in different LLMs.

<!-- image -->

## B. Comparison With Different DRL Methods

To investigate the impact of different DRLs on maximizing system energy efficiency, Fig. 13 presents the convergence curves of energy efficiency when the LLM in L2D2 is enabled by Deepseek-R1, with DRLs including DQN, DDQN, and D3QN. These are referred to as L2D2-DQN, L2D2DDQN, and L2D2-D3QN, respectively. Compared with DQN and DDQN, D3QN clearly delivers greater improvements in energy efficiency and achieves more stable convergence. Furthermore, Fig. 14 shows the CDF of energy efficiency for L2D2-DQN, L2D2-DDQN, and L2D2-D3QN. Compared to DQN and DDQN, D3QN can achieve energy efficiency improvements of 40% and 34%, respectively.

Fig. 13. Average energy efficiency curves of L2D2 with different DRLs.

<!-- image -->

Fig. 14. CDF of average energy efficiency for L2D2 with different DRLs.

<!-- image -->

## C. Comparison With Different Trajectories

To investigate the impact of UAV flight trajectories on energy efficiency, the trajectory generated by L2D2-D3QN (Deepseek-R1) is compared with both the straight trajectory [34] and the circular trajectory [35]. In all cases, the initial location of UAVs is set at (0 m, 0 m, 100 m). From a horizontal perspective, circle 1 represents the UAVs flying clockwise from (0 m, 0 m) to (1000 m, 0 m), while circle 2 denotes the UAVs flying counterclockwise from (0 m, 0 m) to (0 m, 1000 m). The straight trajectory involves the UAVs flying directly from (0 m, 0 m) to (1000 m, 1000 m). For a fair comparison, the baseline trajectories maintain a fixed horizontal path for UAVs, while the remaining variables are optimized employing L2D2-D3QN (Deepseek-R1). Furthermore, to avoid collisions, UA Vs are assigned different altitudes when following the same baseline trajectory. As demonstrated in Fig. 15, the trajectory generated by L2D2-D3QN exhibits a significant improvement in energy efficiency, highlighting its superiority in trajectory optimization.

## D. Comparison With Different Numbers of UAVs and MEC Nodes

Moreover, the impact of the number of UAVs and MEC nodes on system energy efficiency has been explored, as illus- trated in Fig. 16. For a single UA V, L2D2-D3QN significantly improves energy efficiency when MEC nodes are few. However, as MEC nodes increase, the UAV struggles to meet computational demands under constraints, resulting in a gradual decline in energy efficiency. With two UAVs, energy efficiency rises alongside the number of MEC nodes. Nevertheless, the rate of improvement decreases once the number exceeds 16, suggesting that the capacity of the two UAVs is approaching its limits. In scenarios with three or four UAVs, the increase in the number of UAVs raises the flight energy consumption, resulting in low system energy efficiency when the number of MEC nodes is relatively few. As a result, it is crucial to select the appropriate number of UAVs based on the number of MEC nodes to optimize energy efficiency in practical applications.

Fig. 15. The CDF of the average energy efficiency for different trajectories.

<!-- image -->

Fig. 16. The impact of the number of UAVs and MEC nodes on system energy efficiency, where u denotes the number of UAVs.

<!-- image -->

## VI. CONCLUSION

An LLM-driven DRL framework (L2D2) and an algorithm (L2D2-D3QN) are proposed in this paper to maximize the system energy efficiency in multi-UAV-assisted MEC heterogeneous networks, exploring the potential of the low-altitude airspace. Through comprehensive experiments, the effects of various LLMs (Deepseek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-2.5) and DRLs (DQN, DDQN, and D3QN) on system energy efficiency improvement are systematically evaluated. In addition, the impact of tokenization strategies of LLMs on system performance has been explored. The reward function under the L2D2 framework can adjust the strategy according to environmental feedback without manual redesign, effectively enhancing the potential of UAVs in lowaltitude space. In the future, we will explore the integration of sensing and communication technologies [36], [37], [38] along with visual language models [39] to provide promising steps for AGI.

## REFERENCES

- [1] R. Huang et al., 'Dynamic task offloading for multi-UAVs in vehicular edge computing with delay guarantees: A consensus admmbased optimization,' IEEE Trans. Mobile Comput. , vol. 23, no. 12, pp. 13696-13712, Aug. 2024.
- [2] G. Cheng, X. Song, Z. Lyu, and J. Xu, 'Networked ISAC for low-altitude economy: Transmit beamforming and UAV trajectory design,' in Proc. IEEE/CIC Int. Conf. Commun. China (ICCC) , Aug. 2024, pp. 78-83.
- [3] Y. Li, Q. Zeng, C. Shao, P. Zhuo, B. Li, and K. Sun, 'UAV localization method with keypoints on the edges of semantic objects for low-altitude economy,' Drones , vol. 9, no. 1, p. 14, Dec. 2024.
- [4] W. Yuan et al., 'From ground to sky: Architectures, applications, and challenges shaping low-altitude wireless networks,' 2025, ar Xiv:2506.12308 .
- [5] Y. Luo, W. Ding, and B. Zhang, 'Optimization of task scheduling and dynamic service strategy for multi-UAV-enabled mobile-edge computing system,' IEEE Trans. Cognit. Commun. Netw. , vol. 7, no. 3, pp. 970-984, Sep. 2021.
- [6] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and L. Hanzo, 'Multi-agent deep reinforcement learning-based trajectory planning for multi-UAV assisted mobile edge computing,' IEEE Trans. Cognit. Commun. Netw. , vol. 7, no. 1, pp. 73-84, Mar. 2021.
- [7] J. Miao, S. Bai, S. Mumtaz, Q. Zhang, and J. Mu, 'Utility-oriented optimization for video streaming in UAV-aided MEC network: A DRL approach,' IEEE Trans. Green Commun. Netw. , vol. 8, no. 2, pp. 878-889, Jun. 2024.
- [8] J. Xu, X. Liu, A. G. Neiat, L. Chu, X. Li, and Y. Yang, 'A holistic and hybrid service selection strategy for MEC-based UAV last-mile delivery systems,' IEEE Trans. Services Comput. , vol. 17, no. 6, pp. 3022-3036, Aug. 2024.
- [9] M. Akbari, A. Syed, W. S. Kennedy, and M. Erol-Kantarci, 'Constrained federated learning for Ao I-limited SFC in UAV-aided MEC for smart agriculture,' IEEE Trans. Mach. Learn. Commun. Netw. , vol. 1, pp. 277-295, 2023.
- [10] M. Li, N. Cheng, J. Gao, Y. Wang, L. Zhao, and X. Shen, 'Energyefficient UAV-assisted mobile edge computing: Resource allocation and trajectory optimization,' IEEE Trans. Veh. Technol. , vol. 69, no. 3, pp. 3424-3438, Mar. 2020.
- [11] X. Qin, W. Yu, Z. Song, T. Hou, Y. Hao, and X. Sun, 'Energy efficiency optimization for RIS-assisted UAV-enabled MEC systems,' in Proc. IEEE Globecom Workshops (GC Wkshps) , Dec. 2022, pp. 1164-1169.
- [12] X. Qin, Z. Song, T. Hou, W. Yu, J. Wang, and X. Sun, 'Joint optimization of resource allocation, phase shift, and UAV trajectory for energyefficient RIS-assisted UAV-enabled MEC systems,' IEEE Trans. Green Commun. Netw. , vol. 7, no. 4, pp. 1778-1792, Dec. 2023.
- [13] Z. Liu, J. Qi, Y. Shen, K. Ma, and X. Guan, 'Maximizing energy efficiency in UAV-assisted NOMA-MEC networks,' IEEE Internet Things J. , vol. 10, no. 24, pp. 22208-22222, Dec. 2023.
- [14] X. Xing, Y. Huo, Q. Gao, H. Li, X. Gao, and J. Qian, 'An enhanced energy efficiency scheme for secure computing in UAV-MEC networks,' Int. J. Sensor Netw. , vol. 44, no. 1, pp. 23-35, 2024.
- [15] V. Saxena, J. Jaldén, and H. Klessig, 'Optimal UAV base station trajectories using flow-level models for reinforcement learning,' IEEE Trans. Cognit. Commun. Netw. , vol. 5, no. 4, pp. 1101-1112, Dec. 2019.
- [16] H. Zhang, H. Wang, Y. Li, K. Long, and A. Nallanathan, 'DRL-driven dynamic resource allocation for task-oriented semantic communication,' IEEE Trans. Commun. , vol. 71, no. 7, pp. 3992-4004, Jul. 2023.

- [17] W. Lei, Y. Ye, and M. Xiao, 'Deep reinforcement learning-based spectrum allocation in integrated access and backhaul networks,' IEEE Trans. Cognit. Commun. Netw. , vol. 6, no. 3, pp. 970-979, Sep. 2020.
- [18] J. Li et al., 'A reinforcement learning-based stochastic game for energy-efficient UAV swarm-assisted MEC with dynamic clustering and scheduling,' IEEE Trans. Green Commun. Netw. , vol. 9, no. 1, pp. 255-270, Mar. 2025.
- [19] Z. Zhang et al., 'Energy-efficient secure video streaming in UA V-enabled wireless networks: A safe-DQN approach,' IEEE Trans. Green Commun. Netw. , vol. 5, no. 4, pp. 1892-1905, Dec. 2021.
- [20] M. Wu et al., 'UAV-mounted RIS-aided mobile edge computing system: A DDQN-based optimization approach,' Drones , vol. 8, no. 5, p. 184, May 2024.
- [21] C. Liu, Y. Zhong, R. Wu, S. Ren, S. Du, and B. Guo, 'Deep reinforcement learning based 3D-trajectory design and task offloading in UAV-enabled MEC system,' IEEE Trans. Veh. Technol. , vol. 74, no. 2, pp. 3185-3195, Feb. 2025.
- [22] A. F. Mohammad, B. Clark, R. Agarwal, and S. Summers, 'LLM/GPT generative AI and artificial general intelligence (AGI): The next frontier,' in Proc. Congr. Comput. Sci., Comput. Eng., Appl. Comput. (CSCE) , Jul. 2023, pp. 413-417.
- [23] R. Zhang et al., 'Generative AI agents with large language model for satellite networks via a mixture of experts transmission,' IEEE J. Sel. Areas Commun. , vol. 42, no. 12, pp. 3581-3596, Dec. 2024.
- [24] A. T. Neumann, Y. Yin, S. Sowe, S. Decker, and M. Jarke, 'An LLM-driven chatbot in higher education for databases and information systems,' IEEE Trans. Educ. , vol. 68, no. 1, pp. 103-116, Feb. 2025.
- [25] Q. Lang, S. Tian, M. Wang, and J. Wang, 'Exploring the answering capability of large language models in addressing complex knowledge in entrepreneurship education,' IEEE Trans. Learn. Technol. , vol. 17, pp. 2053-2062, 2024.
- [26] J. Gong, L. G. Foo, Y. He, H. Rahmani, and J. Liu, 'LLMs are good sign language translators,' in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR) , Jun. 2024, pp. 18362-18372.
- [27] M. A. Hossain, A. R. Hossain, and N. Ansari, 'AI in 6G: Energy-efficient distributed machine learning for multilayer heterogeneous networks,' IEEE Netw. , vol. 36, no. 6, pp. 84-91, Nov. 2022.
- [28] A. Al-Hourani, S. Kandeepan, and S. Lardner, 'Optimal LAP altitude for maximum coverage,' IEEE Wireless Commun. Lett. , vol. 3, no. 6, pp. 569-572, Dec. 2014.
- [29] Z. Kuang, Y. Pan, F. Yang, and Y. Zhang, 'Joint task offloading scheduling and resource allocation in air-ground cooperation UAV-enabled mobile edge computing,' IEEE Trans. Veh. Technol. , vol. 73, no. 4, pp. 5796-5807, Apr. 2024.
- [30] S. Sinche et al., 'A survey of Io T management protocols and frameworks,' IEEE Commun. Surveys Tuts. , vol. 22, no. 2, pp. 1168-1190, 2nd Quart., 2020.
- [31] N. Tang, X. Wang, F. Zhou, S. Tang, and Y. Lyu, 'Reparameterization causal convolutional network for automatic modulation classification,' IEEE Trans. Veh. Technol. , vol. 73, no. 6, pp. 8576-8583, Jun. 2024.
- [32] H. Mei, K. Yang, Q. Liu, and K. Wang, '3D-trajectory and phase-shift design for RIS-assisted UAV systems using deep reinforcement learning,' IEEE Trans. Veh. Technol. , vol. 71, no. 3, pp. 3020-3029, Mar. 2022.
- [33] X. Zhang, M. Peng, and C. Liu, 'Sensing-assisted beamforming and trajectory design for UA V-enabled networks,' IEEE Trans. Veh. Technol. , vol. 73, no. 3, pp. 3804-3819, Mar. 2024.
- [34] Y. Guo, C. You, C. Yin, and R. Zhang, 'UAV trajectory and communication co-design: Flexible path discretization and path compression,' IEEE J. Sel. Areas Commun. , vol. 39, no. 11, pp. 3506-3523, Nov. 2021.
- [35] X. Diao, W. Yang, L. Yang, and Y. Cai, 'UAV-relaying-assisted multiaccess edge computing with multi-antenna base station: Offloading and scheduling optimization,' IEEE Trans. Veh. Technol. , vol. 70, no. 9, pp. 9495-9509, Sep. 2021.
- [36] J. Wang et al., 'Generative AI based secure wireless sensing for ISAC networks,' IEEE Trans. Inf. Forensics Security , vol. 20, pp. 5195-5210, 2025.
- [37] J. Wang et al., 'Generative AI enabled robust data augmentation for wireless sensing in ISAC networks,' IEEE J. Sel. Areas Commun. , early access, Sep. 24, 2025, doi: 10.1109/JSAC.2025.3613672.
- [38] J. Wang et al., 'Generative artificial intelligence assisted wireless sensing: Human flow detection in practical communication environments,' IEEE J. Sel. Areas Commun. , vol. 42, no. 10, pp. 2737-2753, Oct. 2024.
- [39] C. Xie et al., 'Disrupting vision-language model-driven navigation services via adversarial object fusion,' 2025, ar Xiv:2505.23266 .

<!-- image -->

<!-- image -->

Ke Lv (Student Member, IEEE) received the B.E. and M.S. degrees from Beijing Information Science and Technology University, Beijing, China, in 2021 and 2024, respectively. He is currently pursuing the Ph.D. degree with Beijing University of Posts and Telecommunications. His current research interests include wireless communication, unmanned aerial vehicle, mobile edge computing, and cognitive radio.

Sai Huang (Senior Member, IEEE) is currently a Full Professor with the Department of Information and Communication Engineering, Beijing University of Posts and Telecommunications (BUPT). He is an Academic Secretary with the Key Laboratory of Universal Wireless Communications, Ministry of Education, China. His research interests include machine learning assisted intelligent signal processing, statistical spectrum sensing and analysis, fast detection and depth recognition of universal wireless signals, millimeter wave signal processing, and cog-

nitive radio networks. He is a reviewer of international journals, such as IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE WIRELESS COMMUNICATIONS LETTERS, and IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, and international conferences, such as IEEE ICC and IEEE GLOBECOM.

<!-- image -->

Yuanyuan Yao (Member, IEEE) received the Ph.D. degree in information and communication engineering from Beijing University of Posts and Telecommunications, Beijing, China, in 2017. She is currently a Professor with the School of Information and Communication Engineering, Beijing Information Science and Technology University, Beijing. Her research interests include cooperative communication of UAV, RIS assisted communication, stochastic geometry and its applications in large-scale wireless networks, and intelligent radio resource allocation in 6G.

<!-- image -->

<!-- image -->

Weiwei Jiang (Senior Member, IEEE) received the B.Sc. and Ph.D. degrees from the Department of Electronic Engineering, Tsinghua University, Beijing, China, in 2013 and 2018, respectively. He is currently an Assistant Professor with the School of Information and Communication Engineering and the Key Laboratory of Universal Wireless Communications, Ministry of Education, Beijing University of Posts and Telecommunications. His current research interests include artificial intelligence for networking and communication, satellite communication, and smart grid communication.

Zhiyong Feng (Senior Member, IEEE) received the B.S., M.S., and Ph.D. degrees from BUPT, Beijing, China, in 1993, 1997, and 2009, respectively. She is currently a Full Professor with BUPT, where she is the Director of the Key Laboratory of Universal Wireless Communications, Ministry of Education. Her research interests include 5G mobile networks, ISAC system design, wireless network architecture design, cognitive wireless networks, universal signal detection and identification, and network information theory. She is a Technical Advisor of NGMN.

She is active in ITU-R WP5A/5C/5D, IEEE 1900, ETSI, and CCSA standards. She is an Editor of IET Communications and KSII Transactions on Internet and Information Systems and a reviewer of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, and IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS.
