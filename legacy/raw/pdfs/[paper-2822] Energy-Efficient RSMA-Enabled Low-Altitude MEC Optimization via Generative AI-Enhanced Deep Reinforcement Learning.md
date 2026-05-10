---
title: "Energy-Efficient RSMA-Enabled Low-Altitude MEC Optimization via Generative AI-Enhanced Deep Reinforcement Learning"
authors: "Wang, X., Du, H., Feng, L., Huang, K."
venue: "Conference/Journal (6G Communications)"
year: 2024
abstract: "UAV-based MEC system with RSMA for uplink task offloading optimization using generative AI-enhanced deep reinforcement learning"
keywords:
  - Rate-Splitting Multiple Access
  - RSMA
  - Mobile Edge Computing
  - MEC
  - UAV
  - Deep Reinforcement Learning
  - Generative AI
  - Diffusion Models
  - Energy Efficiency
  - Trajectory Optimization
  - 6G
tags:
  - edge-computing
  - reinforcement-learning
  - optimization
  - multi-agent
  - uav
  - generative-ai
status: converted
source: pdf-to-markdown
---

## Energy-Efficient RSMA-Enabled Low-Altitude MEC Optimization via Generative AI-Enhanced Deep Reinforcement Learning

Xudong Wang , Hongyang Du , Member, IEEE , Lei Feng , Member, IEEE , and Kaibin Huang , Fellow, IEEE

Abstract -The growing demand for low-latency computing in 6G is driving the use of UAV-based low-altitude mobile edge computing (MEC) systems. However, limited spectrum often leads to severe uplink interference among ground terminals (GTs). In this paper, we investigate a rate-splitting multiple access (RSMA)-enabled low-altitude MEC system, where a UAV-based edge server assists multiple GTs in concurrently offloading their tasks over a shared uplink. We formulate a joint optimization problem involving the UAV 3D trajectory, RSMA decoding order, task offloading decisions, and resource allocation, aiming to mitigate multi-user interference and maximize energy efficiency. Given the high dimensionality, non-convex nature, and dynamic characteristics of this optimization problem, we propose a generative AI-enhanced deep reinforcement learning (DRL) framework to solve it efficiently. Specifically, we embed a diffusion model into the actor network to generate high-quality action samples, improving exploration in hybrid action spaces and avoiding local optima. In addition, a priority-based RSMA decoding strategy is designed to facilitate efficient successive interference cancellation with low complexity. Simulation results demonstrate that the proposed method for low-altitude MEC systems outperforms baseline methods, and that integrating GDM with RSMA can achieve significantly improved energy efficiency performance.

Index Terms -Rate-splitting multiple access, mobile edge computing (MEC), resource allocation, deep reinforcement learning.

## I. INTRODUCTION

I N THE sixth generation (6G) era, the proliferation of Internet of Things (IoT) devices and new immersive applications, such as augmented/virtual reality and holographic telepresence, is driving an unprecedented demand for computational resources at the network edge [1]. These latency-sensitive and computation-intensive services exceed the capabilities of onboard processors in battery-powered ground terminals (GTs), resulting in performance degradation

Received 29 June 2025; revised 5 October 2025; accepted 1 November 2025. Date of publication 10 November 2025; date of current version 31 December 2025. This work is supported in part by the National Natural Science Foundation of China under Grant 62571057, in part by the Beijing Natural Science Foundation of China under Grant L254013, and in part by the BUPT Excellent Ph.D. Students Foundation under Grant CX20253001. The associate editor coordinating the review of this article and approving it for publication was W. Yuan. (Corresponding author: Lei Feng.)

Xudong Wang and Lei Feng are with the State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, Beijing 100876, China (e-mail: xdwang@bupt.edu.cn; fenglei@bupt.edu.cn).

Hongyang Du and Kaibin Huang are with the Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong, SAR, China (e-mail: duhy@eee.hku.hk; huangkb@hku.hk).

Digital Object Identifier 10.1109/TCCN.2025.3631051

when tasks are executed locally [2]. Mobile edge computing (MEC) offers a viable solution by offloading tasks to proximate edge servers, reducing latency and improving efficiency [2]. However, terrestrial BS-centric MEC is constrained by coverage and capacity, especially in remote or infrastructure-limited environments [3], or when BSs become overloaded or fail to support edge users. These limitations motivate the exploration of airborne MEC, wherein aerial platforms augment the edge computing infrastructure beyond what ground-based MEC can provide.

In recent years, the low-altitude economy (LAE) has expanded swiftly, with uncrewed aerial vehicles (UAVs) emerging as key components in the evolution of mobile communication networks [4], [5]. Dynamically deployed UAVs can form LAE networks that augment terrestrial infrastructure with additional communication and computing capabilities. When equipped with computing units, UAVs serve as airborne MEC servers, enabling low-altitude MEC systems that bring computation offloading closer to users [6]. Such UAV-assisted MEC networks improve coverage and service reliability while significantly reducing end-to-end latency and GT energy consumption, as users no longer need to transmit to distant base stations. Nevertheless, supporting multiple offloading users via a shared UAV radio link introduces substantial multiuser interference. When many users simultaneously offload tasks over limited spectrum resources, interference among their uplink transmissions becomes severe and can drastically bottleneck the system performance, especially under strict bandwidth constraints.

Rate-splitting multiple access (RSMA) has emerged as a promising strategy to manage interference and improve spectral efficiency in multi-user networks [7]. RSMA separates a user's transmission into private and common components, allowing for a combination of interference decoding and noise handling strategies [8]. Unlike uplink Non-Orthogonal Multiple Access (NOMA) with fixed user grouping and power allocation, RSMA offers greater flexibility through adjustable message splits and decoding orders, enhancing spectral efficiency. This makes RSMA well-suited for low-altitude UAV MEC, where multiple GTs can offload concurrently over the shared spectrum without orthogonalization [9]. While existing RSMA studies focus on downlink, extending it to uplink UAV-assisted MEC systems offers new potential for interference mitigation. However, this introduces complex design challenges, requiring joint optimization of UAV trajectory,

2332-7731 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.

See https://www.ieee.org/publications/rights/index.html for more information.

offloading decisions, RSMA decoding order, and power allocation. Addressing these tightly coupled variables remains a significant challenge.

Conventional optimization techniques, such as convex optimization and heuristic algorithms, are widely used for joint resource and trajectory design but often suffer from high complexity and local optima [10]. Deep reinforcement learning (DRL) offers an online alternative, capable of learning near-optimal policies for joint scheduling and control in high-dimensional environments [11]. However, DRL faces challenges in continuous action spaces, including poor sample efficiency and convergence instability [12]. To address these drawbacks, some studies incorporate generative diffusion models (GDMs), which is a class of generative AI (GenAI) techniques adept at modeling complex distributions through iterative sampling [13], [14], [15], [16]. By iteratively refining random samples to match an intended distribution, diffusion models excel at generating high-quality solutions even in large search spaces [15]. This motivates our proposed RSMAassisted low-altitude MEC framework, combining generative AI-enhanced DRL for improved energy efficiency.

## A. Related Works

Low-altitude MEC systems are characterized by dynamic node locations, limited computational resources, and a strong dependence on communication link quality, making UAV trajectory planning and computation offloading particularly challenging. As a result, recent studies have investigated the joint optimization of UAV trajectories and resource allocation in low-altitude MEC systems [17], [18], [19], [20]. For example, the authors in [17] designed a joint task offloading and trajectory control scheme for UAV-assisted energy-harvesting MEC systems to minimize propulsion energy while maintaining queue stability. The authors in [18] and [19] proposed joint optimization of communication resources and UAV trajectories to improve offloading throughput or reduce energy consumption under quality of service (QoS) and energy constraints. In [20], a bi-objective ant colony algorithm addressed delay and control cost minimization problem. These studies provide valuable insights into low-altitude edge resource management. However, transmission frameworks based on orthogonal multiple access (OMA) struggle to accommodate the explosive growth in network density, particularly in spectrum-constrained low-altitude networks, often leading to degraded performance in interference management and task completion rates.

Leveraging its capability to mitigate multi-user interference and enhance spectral efficiency, RSMA has been incorporated into low-altitude networks to improve communication performance under interference-limited conditions [21], [22], [27], [28], [29]. In [27], an alternating optimization strategy for RSMA-enabled low-altitude networks was proposed to maximize system throughput while ensuring user rate requirements. The work in [28] demonstrated that RSMA significantly improves physical-layer security in a dual-UAV downlink scenario. Additionally, RSMA has been introduced into low-altitude MEC systems to further improve offloading performance. Specifically, the authors in [21] designed a UAV relay architecture and propose a data-stream splitting scheme that minimizes UAV energy consumption under task latency constraints. In [29], a joint passive reflecting units and dynamic rate-splitting optimization framework was proposed for uplink RSMA-enabled UAV-MEC systems to minimize total UAV power consumption. The authors in [22] applied RSMA to a UAV-MEC system assisted by a reconfigurable intelligent surface (RIS) with wireless power transfer and observed that the RSMA-based scheme achieves more reliable and efficient task offloading in the presence of strong co-channel interference. Dynamic low-altitude MEC systems must adapt to time-varying channels and fluctuating interference levels, but traditional iterative optimization methods face scalability challenges when dealing with highly coupled decision variables in such dynamic environments.

Data-driven optimization methods, particularly DRL, have emerged as powerful solutions for complex optimization problems in low-altitude MEC systems due to their dynamic adaptability and global exploration capabilities. For example, the authors in [23] employed DRL to jointly adjust UAV flight paths and offloading decisions, effectively reducing the system's energy consumption and task latency compared to heuristic baselines. To further improve solution quality and avoid local optima, GDMs have been introduced to augment DRL in wireless network optimization [30], [31]. By leveraging the diffusion-based generative process, agents can enhance their exploration of complex state spaces and refine reward evaluation during training [32], [33], [34], [35]. For instance, the authors in [32] introduced a diffusion-assisted DRL framework that generates diverse state samples and more informative reward signals, achieving faster convergence and lower computational overhead compared to standard DRL in a dynamic resource allocation task. Similarly, in [35], a diffusion-enhanced DRL framework was applied to a wireless sensing-guided edge network to derive optimal pricing strategies, thereby maximizing user utility. Therefore, given the generative capability, integrating diffusion models with DRL to address joint trajectory and resource allocation in RSMA-enabled low-altitude MEC systems presents a promising research direction.

In fact, recent studies have emphasized the role of GenAI in enabling intelligent optimization for low-altitude networks. In UAV-enabled IoT systems, diffusion-modelenhanced multi-objective optimization frameworks have been developed to jointly minimize delay, motion energy, and computational resource consumption, thereby improving forest monitoring efficiency under stringent UAV energy constraints [24]. At the networking layer, GenAI has also been leveraged in game-theoretic frameworks, where large language model (LLM)-enabled models assist in constructing and solving complex UAV-assisted mobile networking games, providing automated strategies for resource trading and secure communication [25]. Complementarily, in the low-altitude airspace edge inference domain, generative diffusion models have been embedded into actor networks to design online batching and beamforming policies, achieving near-optimal task completion under dynamic and uncertain arrivals [26].

TABLE I COMPARE OUR WORK WITH EXITING STUDIES

In order to highlight the contribution and novelty of our work, we have summarized and compared several most relevant studies in Table I.

## B. Motivations and Contributions

This paper presents a joint optimization framework for uplink RSMA-enabled low-altitude MEC systems to maximize energy efficiency. Due to the high-dimensional and hybrid action space of UAV trajectory, user offloading, RSMA decoding order, and power allocation, the conventional DRL methods often struggle with inefficient exploration, poor convergence, and vulnerability to local optima. To overcome these challenges, we proposed a GenAI-enhanced DRL algorithm, in which a GDM generator is embedded into the actor network to guide the exploration process. By leveraging the capability of GDM to generate structured and high-quality candidate actions, the proposed algorithm effectively navigates complex solution spaces and mitigates local optima issues common in traditional approaches. The main contributions are summarized as follows :

- We develop a uplink RSMA-assisted low-altitude MEC system, where a UAV equipped with an mobile edge server provides computing services to multiple GTs, and the task data of each GT is split into multiple sub-messages that are concurrently transmitted with different powers. Then we formulate a novel non-convex optimization problem that maximizes energy efficiency by jointly optimizing the UAV's flight trajectory, user offloading decisions, and RSMA communication parameters.
- We propose a generative AI-enhanced deep reinforcement learning framework, termed GDRS, to efficiently solve the high-dimensional, non-convex optimization problem in RSMA-enabled UAV-MEC systems. The problem is decomposed into a decoding-order sub-problem and a continuous control problem. To reduce the decoding complexity, we derive a lightweight priority-based RSMA strategy that dynamically orders sub-messages based on channel quality and user QoS demands for uplink multiuser low-altitude MEC networks, enabling interference cancellation with low overhead.
- To overcome the challenges of poor exploration and local optima, we embed a generative diffusion model into the policy network. This integration allows the agent to generate structured candidate actions, including UAV trajectories and resource allocation decisions, leading to more stable convergence and higher policy quality across dynamic and coupled state-action spaces.
- We carried out a comprehensive set of simulations to validate the proposed GDRS and to assess the scalability of the RSMA framework. The results show that our RSMA-enabled framework achieves higher throughput and energy efficiency compared to NOMA-based schemes. Moreover, the GenAI-enhanced DRL method outperforms conventional DRL approaches in terms of reward, highlighting the superior exploration capability of the diffusion model.

The rest of this paper is organized as follows. Section II introduces the system model and formally defines the optimization problem. In Section III, we elaborate on the algorithmic framework developed to address the problem. Section IV showcases simulation results and provides an in-depth discussion of the numerical findings. Section V highlights the key contributions and draws the final conclusions of the paper.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

As illustrated in Fig. 1, we investigate an RSMA-assisted low-altitude MEC systems, where the UAV is despatched to serve K ≜ { 1 , 2 , . . . , K } GTs. Given the stringent limitations on size, payload capacity, and onboard energy in lightweight rotary-wing UAVs for airborne MEC applications, we consider a single-antenna UAV to circumvent the extra hardware burden and energy expenditure associated with multi-antenna implementations, and leave the multiple UAVs for future work.

## A. Network Model

We consider a uniformly gridded task area, where the UAV dynamically determines its 3D trajectory through discrete waypoints to serve the GTs. The horizontal coordinate of the center of the i -th cell is represented by D ℓ i = [ x i , y i ] T ∈

Fig. 1. RSMA-enabled multi-user low-altitude MEC networks.

<!-- image -->

R 2 × 1 , where L ≜ { 1 , 2 , . . . , L } denotes the set of all cell indices. The spacing between the centers of neighboring cells along the x -axis and y -axis are denoted by x s and y s , respectively. The UAV's horizontal position is represented by D u n ∈ L , where n ∈ N ≜ { 1 , 2 , . . . , N } and N represents the total number of discrete time slots. Each time slot is associated with a UAV flight duration level t u n ∈ T ≜ { 1 , 2 , . . . , T } , where the actual duration is bounded by t min ≤ t u n × ∆ t ≤ t max . Here, t min and t max define the minimum and maximum allowable flight durations, and ∆ t = ⌊ t max /T ⌋ denotes the time resolution per level. The initial and final UA V positions are fixed and denoted as D u 0 and D u e , respectively. Accordingly, the horizontal UAV path can be approximated as the sequence { D u 0 , D u 1 , . . . , D u n , . . . , D u N , D u e } . To capture the UAV's vertical mobility, the altitude at time slot n is represented by h u n ∈ H ≜ { 1 , 2 , . . . , H } . The actual height must satisfy h min ≤ h u n × ∆ h ≤ h max , where h min and h max denote the minimum and maximum permissible heights, respectively, and ∆ h = ⌊ h max /H ⌋ denotes the step size between discrete altitude levels. Consequently, the complete UAV trajectory consists of N discrete 3D waypoints [ D u n , h u n ] and the associated time durations t u n , ∀ n ∈ N .

## B. Mobility Model

The ground terminals are assumed to be either stationary or with low mobility, which aligns with practical IoT-type users such as sensors or handheld devices. Their horizontal positions are fixed at the beginning of the mission, denoted by u k = [ x k , y k ] T ∈ R 2 × 1 , k ∈ K , and are uniformly distributed across the task area. The horizontal velocity of UAV is expressed as

<!-- formula-not-decoded -->

where V h max represents the maximum horizontal velocity. Besides, the vertical flying velocity is expressed as

<!-- formula-not-decoded -->

where V v max denotes the UAV's maximum vertical velocity. When v h n = 0 , the UAV is either hovering or performing steady straight-and-level flight during time slot n .

Based on [36], the propulsion energy consumption of the UAV is given by

<!-- formula-not-decoded -->

where W 0 and W 1 represent the constant blade profile power and the induced power under hovering conditions, while W 2 denotes the constant power required during ascent or descent. The parameters F 0 and g represent the fuselage drag ratio and the rotor solidity. In addition, ρ refers to the air density, and M stands for the area of the rotor disc. The parameter U t denotes the tip velocity of the rotor blade, and ¯ v signifies the tip velocity of the rotor blade, and ¯ v refers to the average induced airflow velocity in hovering flight.

## C. Communication Model

Based on the air-to-ground propagation model for urban scenarios [37], the probability of establishing the LoS connection between the UAV and GT k can be expressed as

<!-- formula-not-decoded -->

where α and β are environment-dependent constants, l k,n = √ ( x i -x k ) 2 +( y i -y k )) 2 . Based on this, the corresponding pathloss can be expressed as

<!-- formula-not-decoded -->

where A 1 = ζ LoS -ζ NLoS , A 2 = 20log( 4 πf c c ) + ζ NLoS , f c denotes the carrier frequency; c represents the speed of light, ζ LoS and ζ NLoS are the environment-dependent path loss factors for LoS and NLoS conditions, respectively. We define a k,n ∈ { 0 , 1 } as the offloading indicator of GT k at time slot n , with a k,n = 1 representing task offloading to the UAV and a k,n = 0 indicating local computation. To support concurrent offloading, RSMA is applied. Specifically, the message of each GT w k,n is split into |I| sub-messages w k,n,i , each allocated a transmit power p k,n,i to achieve rate splitting, such that ∑ i ∈I p k,n,i ≤ P max , ∀ k, n , where P max is the maximum uplink transmit power of each GT. The composite message is w k,n = ∑ i ∈I √ p k,n,i w k,n,i , ∀ k, n. Thus, the received signal of UAV at time slot n is obtained as

<!-- formula-not-decoded -->

where g k,n denotes the channel gain between k -th GT and UAV, given by g k,n = 10 -d k,n / 10 , where n 0 represents the additive white Gaussian noise (AWGN). In this paper, we assume that perfect CSI can be obtained [38], [39].

To decode multiple sub-messages, the UAV employs successive interference cancellation (SIC). Let π k,n,i , i ∈ I indicate the SIC decoding order of sub-message w k,n,i , and let π = { π k,n,i , ∀ k, n, i } denote a decoding permutation, which contains all valid SIC decoding sequences for the |I| K submessages. Under this decoding strategy, the achievable uplink rate for sub-message w k,n,i is obtained as [29]

<!-- formula-not-decoded -->

where B denotes the system bandwidth, N 0 represents the noise power spectral density. The set W k,n,i = { ( k ′ , i ′ ) | a k ′ ,n = a k,n , π k ′ ,n,i ′ &gt; π k,n,i , ∀ k ′ , i ′ } contains the sub-messages that are decoded after w k,n,i based on the SIC decoding order at the UAV.

## D. Computing Model

In the considered RSMA-enabled low-altitude MEC systems, each GT has an estimated computational task G k = { C k , D k } , where C k represents the total required CPU cycles, D k denotes the overall data size to be calculated. As discussed in [40], when GT k chooses to offload its task to the UAV during time slot n , the expected amount of data successfully transmitted in that slot is obtained as

<!-- formula-not-decoded -->

where κ n ∈ [0, 1] represents the portion of time slot n that is assigned to data transmission. To ensure that the transmitted data m k,n can be processed by the UAV's onboard CPU with a processed rate of f u , κ n must be properly chosen. This requirement imposes the following constraint :

<!-- formula-not-decoded -->

To further enhance the total amount of processed data, α n is further constrained as

<!-- formula-not-decoded -->

Given the offloading decision a k,n at time slot n and (10), the amount of task data G k processed during slot n is represented as

<!-- formula-not-decoded -->

where f g denotes the processed speed of the GT's CPU. In (11), the delay due to downlink transmission from UAV to GT is neglected, assuming that the corresponding data size is negligible. Accordingly, the overall system energy efficiency can be defined as η = ∑ K k =1 ∑ N n =1 ϖ k,n /E uav .

## E. Problem Formulation

We aim to maximize the system energy efficiency η while maintaining reliable MEC performance by jointly optimizing the UAV trajectory, task offloading decisions, uplink power allocation, and SIC decoding order. Let A = { a k,n , ∀ k ∈ K , ∀ n ∈ N} , P = { p k,n,i , ∀ k ∈ K , ∀ n ∈ N , ∀ i } , D = { D u n , ∀ n ∈ N} , h = { h u n , ∀ n ∈ N} , and t = { t u n , ∀ n ∈ N} , the optimization problem can then be formulated as

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

<!-- formula-not-decoded -->

where µ k,n,i denotes a predefined non-negative coefficient that allocates a proportion of the rate R k,n to the i -th sub-message of GT k in time slot n , satisfying R k,n,i = µ k,n,i R k,n , ∀ i and ∑ i ∈I µ k,n,i = 1 , ∀ k, n . The minimum rate requirement for each GT is denoted by R min . Constraints in P 0 are interpreted as follows: C1 models offloading as a binary decision problem; C2 ensures tasks are completed within the UAV's mission time; C3 limits the total transmit power of each GT; C4 ∼ C7 describe UAV mobility constraints; C8 enforces non-negative transmission powers; C9 guarantees feasible SIC decoding; C10 enforces the rate requirement; and C11 ensures valid rate splitting among sub-messages.

The optimization problem P 0 is a non-convex mixed-integer program due to the discrete offloading variable a , the nonconvex objective, and constraint C2, making it difficult to solve optimally. Moreover, the UAV's complex energy model further complicates trajectory and flight time design for energy efficiency maximization. Prior work has shown that solving P 0 via successive convex approximation (SCA) incurs high computational cost, rendering it impractical [36]. To overcome these challenges, we derive the optimal decoding order policy, and then develop a GenAI-based optimization framework, detailed in the following section.

## III. THE PROPOSED GDRS ALGORITHM

To efficiently address problem P 0 , we decompose it into two sub-problems: 1) the decoding order sub-problem P 1 , and 2) the joint UAV 3D trajectory, power allocation, and task offloading sub-problem P 2 . For P 1 , the optimal decoding policy π is determined based on channel gains. Subsequently, P 2 is reformulated as a Markov decision process (MDP), and a generative AI-enhanced DRL framework is developed to optimize { A , P , D , h } .

## A. Decoding Order Policy

The optimal decoding order plays a critical role in mitigating inter-submessage interference and enhancing overall energy efficiency, and thus must be carefully considered. Given a fixed UAV trajectory D , altitude profile h , offloading decisions A , power allocation P , and UAV flight time t , P 0 is rewritten as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Solving the decoding order optimization problem P 1 is challenging due to its non-convex objective function and the intricate interdependence of discrete variables, rendering it a mixed-integer nonlinear programming (MINLP) problem that is typically hard to solve. While exhaustive search methods [41] can yield the optimal solution, their computational cost scales exponentially with the number of sub-messages, making them impractical for multi-user systems. Existing works [42], [43], [44] often adopt channel gain-based heuristics for decoding order. To better balance computational efficiency and system performance, we propose a decoding strategy that jointly considers both the channel gains and the rate-splitting proportions of each GT's sub-messages.

Lemma 1: The decoding order of sub-messages is determined by sorting υ k,n,i ≜ | g k,n | 2 ( 1 + 1 ρ min k,n,i ) =

| g k,n | 2 ( 1 + 1 2 ( µ k,n,i R min ) -1 ) in descending order, where ρ min k,n,i represents the minimum signal-to-interference-plusnoise ratio (SINR) required for GT k to decode the i -th sub-message at time slot n .

Proof: Since the decoding order policy π influences the achievable data rate but does not impact the energy consumption of UAV, the optimization problem P 1 is equivalently reformulated as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As indicated in (11), for given UAV trajectory D , altitude profile h , offloading decisions A , power allocation P , and flight time t , the data processed ϖ k,n depends solely on the sum rate ∑ i ∈I R k,n,i . Hence, maximizing ϖ k,n reduces to maximizing the aggregate rate. To this end, we aim to design a decoding order policy that maximizes the sum rate at each time slot. Let w a and w b be two consecutive sub-messages in the decoding sequence, associated with respective channel gains g a and g b , and corresponding power levels p a and p b . If the cumulative interference from previously decoded sub-messages is upper bounded by a constant ϵ , we have

<!-- formula-not-decoded -->

where ξ represents the interference from sub-messages decoded after both w a and w b . Two decoding scenarios are possible: a) w a is decoded before w b , and b) w b is decoded before w a . We analyze the achievable signal strength under both cases. Case a): when w a decoded first: In Case a), where w a is decoded first, the feasible power allocation for w a and w b must satisfy

<!-- formula-not-decoded -->

where 0 ≤ p a , p b ≤ P max . Based on this feasible region, the corresponding lower bound of the achievable signal strength can be expressed as

<!-- formula-not-decoded -->

and the associated upper limit for power control is given by

<!-- formula-not-decoded -->

The maximum achievable signal strength from sub-messages w a and w b , denoted by χ ≜ | g a | 2 p a + | g b | 2 p b , can thus be written as

<!-- formula-not-decoded -->

Case b): when w b is decoded first, the maximum combined signal strength from w a and w b can similarly be expressed as

<!-- formula-not-decoded -->

By comparing expressions (19) and (20), we observe that in Case a), if | g a | 2 ( 1 + 1 ρ min a ) ≥ | g b | 2 ( 1 + 1 ρ min b ) , then χ a ≥ χ b , i.e., decoding of w a , indicating that decoding w a first yields higher signal strength. Conversely, in Case b), if | g a | 2 ( 1 + 1 ρ min a ) ≤ | g b | 2 ( 1 + 1 ρ min b ) , then χ a ≤ χ b , and decoding w b first becomes the better choice.

This confirms that the optimal decoding strategy is to prioritize decoding the sub-message w k,n,i corresponding to the larger value of | g k,n | 2 ( 1 + 1 ρ min k,n,i ) . Accordingly, a nearoptimal decoding order is obtained by sorting all sub-messages in descending order of υ k,n,i ≜ | g k,n | 2 ( 1 + 1 ρ min k,n,i ) =

<!-- formula-not-decoded -->

Lemma 1 reveals that the optimal decoding order in RSMAenabled UAV-MEC systems can be determined by a unified metric that jointly accounts for both channel quality and QoS-driven SINR thresholds of the sub-messages. This implies that a sub-message with either a stronger channel condition or a stricter decoding requirement should be given higher decoding priority. Such an ordering rule not only balances interference suppression and fairness across users but also converts the otherwise factorial-complexity decoding-order optimization into a simple sorting operation, thereby significantly reducing computational burden.

## B. MDP Construction

With the decoding order strategy π determined, problem P 0 is reformulated as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

To obtain the optimal joint trajectory, task offloading, and power allocation, we propose generative AI-enhanced DRL method.

DRL operates on two core components: the agent and the environment. Their interaction is typically modeled as a MDP, characterized by ⟨S , A , R , ω, P⟩ , where S denotes the state space, and A the action space available to the agent. The reward function R quantifies the immediate feedback received after taking a specific action in a particular state, whereas the discount factor ω controls the trade-off between short-term and long-term rewards. The transition probability function P governs the dynamics of state evolution following each action. The key components S , A , and R are detailed as follows:

1. State Spaces: At time slot n , the state of GT k is defined by its fixed location, i.e., s k ( n ) = u kn ≜ u k , ∀ n ∈ N . The state of UAV s u ( n ) can be represented by its 3D position and time allocation, i.e., s u ( n ) = ( D u n , h u n , t u n ) . Hence, the overall system state at slot n is obtained as s ( n ) = {{ s k ( n ) } k ∈K , s u ( n ) , n } ∈ S .

2. Action Spaces: Following the mobility model in [45], the UAV is allowed to move only to one of the adjacent horizontal cells within a single time slot. As a result, its horizontal position D u ( n ) is updated in the next slot as :

<!-- formula-not-decoded -->

where d ( n ) denotes the UAV's selected horizontal flight action at time slot n , with E , S , W , and N , indicating movement in the directions of east, south, west, and north, respectively. The symbol O signifies the UA V remains stationary. In the vertical dimension, the UAV is similarly constrained to move only to an adjacent altitude level in each time slot. Accordingly, the UAV's altitude h u n will be updated in the next slot as :

<!-- formula-not-decoded -->

where h ( n ) denotes the UAV's chosen altitude action at time slot n ; U and D represent ascending and descending, respectively. If the selected horizontal action d ( n ) leads the UAV outside the area of interest at time slot n +1 , it is reset to O to keep the UAV stationary. Similarly, if h ( n ) causes the UAV's altitude to exceed the allowable range [ h min , h max ] , it is set to O to retain the current altitude level. Accordingly, the system action at time slot n can be expressed as a ( n ) = ( d ( n ) , h ( n ) , t u n , { a k,n } k ∈K , { p k,n,i } k ∈K , i ∈ { 1 , 2 } ) ∈ A , where the action space A comprises the UAV's movement and time allocation actions, as well as the GTs' task offloading and power control decisions.

3. Rewards: The reward associated with a state-action pair ( s ( n ) , a ( n )) at time slot n is given by :

<!-- formula-not-decoded -->

After performing action a ( n ) , the reward r ( s ( n ) , a ( n )) is defined as the energy efficiency, measured by the ratio between the amount of data processed by each GT in the next time slot, i.e., ϖ k,n +1 , and the UAV's propulsion energy consumption E uav n +1 . To influence the convergence behavior, two scaling factors λ 1 and λ 2 are introduced. Additionally, PV denotes a penalty function, which is defined as

<!-- formula-not-decoded -->

where c 0 is a positive constant that controls the penalty magnitude. Through this design, the DRL framework aims to learn energy-efficient solutions for RSMA-enabled lowaltitude MEC systems.

## C. The Proposed Generative AI-Enhanced DRL Method

Jointly optimizing UAV trajectory, task offloading, and power allocation presents significant challenges for conventional DRL algorithms, primarily due to the high-dimensional and discrete nature of the action space. The structured coupling of UAV mobility, interference management through RSMA, and computation offloading decisions leads to an optimization landscape where the search space is vast, highly non-convex, and prone to local optima. Standard DRL agents often exhibit poor sample efficiency and limited exploration capability under such conditions, resulting in unstable convergence and suboptimal policies [46]. Motivated by these limitations, we adopt a diffusion model-based DRL framework that leverages the generative modeling ability of diffusion processes to iteratively refine noisy samples into structured candidate actions consistent with system constraints. This generative mechanism promotes more effective exploration, enhances the agent's ability to escape local minima, and ensures that synthesized actions, such as UAV trajectories and resource allocation patterns, are both diverse and high-quality.

The Denoising Diffusion Probabilistic Model (DDPM) progressively perturbs data into Gaussian noise through a forward diffusion process and then learns to recover the original data via a reverse denoising process [47]. Leveraging this generative mechanism and its ability to incorporate conditional information, we design a diffusion-based optimizer for enhancing solution quality and synergizing effectively with DRL to address dynamic and complex optimization in RSMA-enabled low altitude MEC systems. Compared with other generative models, such as generative adversarial networks (GANs) and variational autoencoders (VAEs), diffusion models avoid mode collapse and oversmoothing issues, enabling more stable and diverse sample generation, which is particularly critical for the non-convex, mixed-integer optimization tasks considered in this work.

In the diffusion framework, an optimal decision under the current environment is progressively perturbed with noise until it becomes Gaussian, a process referred to as forward probability noising [13]. In the reverse phase, the decision generation network π θ ( · ) serves as a denoiser that reconstructs the original solution z 0 from Gaussian noise, conditioned on the system state s . The following presents the formal mathematical formulation of this diffusion-based decision process.

1. Forward Process: The decision output z 0 = π ϑ ( s ) represents the probability distribution over discrete decisions under the observed environment state s . In the forward diffusion process, this initial distribution is gradually perturbed by Gaussian noise, resulting in a sequence of intermediate representations z 1 , z 2 , . . . , z T , each sharing the same dimensionality as z 0 . At each step t , the transition from z t -1 to z t follows a Gaussian distribution with mean √ 1 -φ t z t -1 and variance φ t I , as described in [48].

<!-- formula-not-decoded -->

where t = 1 , . . . , T , φ t = 1 -e -φ min T -2 t -1 2 T 2 ( φ max -φ min ) denotes the time-dependent variance in the forward process [48].

Since each z t depends only on its immediate predecessor z t -1 , the forward process constitutes a Markov chain. Consequently, the distribution of z T conditioned on z 0 can be expressed as the product of transition probabilities across denoising steps [48], which is shown as

<!-- formula-not-decoded -->

Although the forward process is not explicitly executed, it defines a closed-form relationship between z 0 and any intermediate state z t , given by

<!-- formula-not-decoded -->

where ν t = 1 -φ t , ¯ ν t = ∏ t k =1 ν k denotes the cumulative product up to step t . The forward process relates z t and z 0 as a noisy transformation, where ε ∼ N ( 0 , I ) is standard Gaussian noise. As t increases, z T converges to pure noise distributed as N ( 0 , I ) . However, since wireless network optimization problems typically lack ground-truth datasets of optimal decisions z 0 , the forward process is not executed in the proposed framework.

2. Reverse Process: The goal of the reverse process is to reconstruct the desired target z 0 starting from a noise sample z T ∼ N ( 0 , I ) by iteratively denoising it. Within our framework, this procedure corresponds to synthesizing the optimal decision policy from an initially Gaussian-distributed sample. The transition between z t and z t -1 is modeled as p ( z t -1 | z t ) , which is intractable in closed form but can be approximated by a Gaussian distribution, expressed as

<!-- formula-not-decoded -->

where the mean µ ϑ is learned via a deep neural network, and the variance is obtained as [48].

<!-- formula-not-decoded -->

By applying Bayes' theorem, the reverse process can be reformulated in terms of the forward process and expressed as a Gaussian probability density function. Accordingly, the mean is derived as

<!-- formula-not-decoded -->

where t = 1 , . . . , T . Based on the forward process in (28), the reconstructed sample z 0 can be directly estimated by

<!-- formula-not-decoded -->

where σ ϑ ( z t , t, s ) denotes a deep neural network parameterized by ϑ that predicts the denoising noise conditioned on the observed state s . To prevent excessive noise in the reconstructed decision z 0 , which may obscure the true action probabilities, the output is scaled using a hyperbolic tangent activation to ensure bounded noise levels.

During the reverse denoising process, each step t introduces a new noise component σ ϑ , which remains independent of the forward-process noise σ . As a result, z 0 cannot be directly recovered using (32). Instead, we substitute (32) into the reverse transition expression in (31) to estimate the mean, shown as

<!-- formula-not-decoded -->

We then sample z t -1 from the reverse transition distribution p ( z t ) p ϑ ( z t -1 | z t ) and iterate this process over t = T, T -1 , . . . , 1 . By recursively applying these steps, the final generation distribution p ϑ ( z 0 ) is given by

<!-- formula-not-decoded -->

where p ( z T ) denotes a standard Gaussian distribution. After the reverse process yields the generative distribution p ϑ ( z 0 ) , a sample of the final output z 0 can be drawn accordingly.

A common challenge in training generative models lies in the inability to backpropagate gradients through stochastic sampling operations. To overcome this, we adopt a reparameterization technique that separates the source of randomness from the distribution parameters. Specifically, the sampling is reformulated using the following update rule :

<!-- formula-not-decoded -->

where σ ∼ N (0 , I ) . By recursively adopting the reverse update rule in (35), all intermediate states z t (0 ≤ t ≤ T ) , including the final output z 0 , can be generated from an initial Gaussian noise sample.

Finally, the softmax function is applied to z 0 to convert it into a valid probability distribution, given by

<!-- formula-not-decoded -->

Each element in π ϑ ( s ) represents the probability of selecting a specific action under state s .

To implement the proposed approach in practice, the first step involves calculating the mean µ ϑ of the reverse transition distribution p ϑ ( z t -1 | z t ) , as defined in (29) and (33), and then update z t -1 using the rule in (35). Subsequently, the optimal decision distribution z 0 is obtained via (36). To further enhance optimization, we integrate the diffusion model into the Soft Actor-Critic (SAC) framework. SAC is an off-policy DRL algorithm that augments the reward with an entropy term to jointly maximize expected returns and policy entropy, effectively balancing exploration and exploitation.

- 3. Experience Replay: The agent continuously interacts with the environment to collect trajectory data. At slot n , the actor observes the state s ( n ) and generates a discrete action distribution π ϑ ( s ( n )) . An action a ( n ) ∼ π ϑ ( s ( n )) is sampled and executed, after which the environment returns a reward r ( n ) = ( s ( n ) , a ( n )) and transitions to the next state s ( n +1) . The resulting transition tuple ( s ( n ) , a ( n ) , r ( n ) , s ( n + 1) is stored in the experience replay buffer B . This replay mechanism enables real-time interaction while allowing asynchronous sampling of past experiences, thereby enhancing training efficiency.

4. Double Critic Networks: In the proposed framework, the critic network is implemented as a soft Q-function Q ψ ( s ( n ) , a ( n )) , which evaluates the expected return augmented by the entropy of the policy ψ under ( s ( n ) , a ( n )) . The formulation is given by

<!-- formula-not-decoded -->

where ω denotes the reward discount factor, and s ( n +1) is the subsequent state sampled from the replay buffer B . The corresponding soft value function V π ( s ( n )) is expressed as :

<!-- formula-not-decoded -->

the term J ( π ϑ ( s ( n ))) represents the entropy of the policy at state s ( n ) , while γ ∈ [0, 1] is a tunable temperature coefficient that regulates the influence of the entropy in the objective. To reduce the overestimation bias often observed in Q-learning algorithms, GDRS incorporates a pair of critic networks, Q ψ 1 ( s ( n ) , a ( n )) and Q ψ 2 ( s ( n ) , a ( n )) . The actor is trained using the smaller of the two Q-values, ensuring a conservative and stable policy update.

- 5. Target Networks: Each critic network is associated with a corresponding target network, parameterized by ˆ ψ 1 and ˆ ψ 2 , respectively. These target networks mirror the architecture of their online counterparts and are introduced to enhance training stability by reducing fluctuations in target estimates.

Fig. 2. The proposed GDRS optimization framework for joint optimization of UAV trajectory, task offloading and power allocation in RSMA-enabled low-altitude MEC systems.

<!-- image -->

To ensure smooth updates, their parameters are adjusted incrementally using a soft update strategy, defined as :

<!-- formula-not-decoded -->

where ς ∈ (0 , 1] denotes the soft update rate, and i = 1 , 2 .

To train the critic networks, the agent draws a mini-batch of transition samples from the replay buffer B and optimizes the network parameters by minimizing the following loss function :

<!-- formula-not-decoded -->

where we define the Q-target ˆ y as

<!-- formula-not-decoded -->

Subsequently, the parameters of the two critic networks are updated using gradient descent, following the update rule :

<!-- formula-not-decoded -->

where τ c represents the learning rate of the critic network for updating critic network parameters.

For training the policy network, the actor aims to maximize the expected Q-value to enhance decision-making quality. The objective function for updating the actor is defined as :

<!-- formula-not-decoded -->

and we update the parameter ϑ , shown as

<!-- formula-not-decoded -->

where τ a indicates the learning rate of actor network.

## D. Algorithm Framework

Fig. 2 shows the framework of the proposed GDRS method, which extends the SAC algorithm. It comprises several core components for policy training, including an diffusion model-based actor network, double critic networks with corresponding target networks, an experience replay buffer, and the interaction environment [46]. In addition, the detailed progress of the proposed GDRS method is presented in Algorithm 1.

The computational complexity analysis of the proposed GDRS method is presented as follows. Notably, since the number of GTs K and the number of sub-messages | I | are much smaller than the model size and diffusion steps, the decoding-order cost can be safely neglected compared with the diffusion sampling and gradient updates. As for the action sampling, the computational complexity of action sampling is O ( EQT | ϑ | ) , where E , Q , and T are the total training episodes, sampling trajectory, and diffusion steps, respectively, | ϑ | is the number of actor parameters. As for the experience collection, the agent interacts with the environment, whose bookkeeping scales linearly with the state dimension D s . Thus, the complexity of experience collection is O ( EQD s ) . For learning updates, the model performs mini-batch backpropagation through the actor and the two critics followed by soft target updates, which contributes O ( EQ ( B| ϑ | ) + O ( B| ψ | ) + O ( | ϑ | + | ψ | )) , where B is the batch size and | ψ | is the total number of critic parameters. With the above, the overall training complexity is expressed as O ( EQ ( D s + T | ϑ | +( B +1)( | ϑ | + | ψ | ) )) .

## IV. SIMULATION RESULTS AND DISCUSSION

This section presents simulation studies designed to evaluate the effectiveness of the proposed GDRS approach. We begin by outlining the experimental configuration and baseline settings. Then, the simulation outcomes are discussed and examined thoroughly.

## A. Experimental Setup

1. Experimental Configuration: We consider a task area measuring 1000 × 1000 m , which includes one UAV equipped with an MEC server and certain number of GTs. The GTs are randomly located in the target area following a uniform distribution. We set the initial location of the UAV as [0, 0, 200] . The total time slots of the system is set to 100, and each time slot is of length 1 s . According to the settings about propulsion model of the rotary-wing UAV [36], we set U t = 120 m / s , ¯ v = 4 . 03 m / s , F 0 = 0 . 6 , g = 0 . 05 , ρ = 1 . 225 , M = 0 . 503 . Each GT divides its transmitted signal into two distinct sub-messages, 1 i.e., I = 2 . The rate-splitting ratio of the sub-messages is set to µ k,n,i = 0 . 5 , ∀ k, n, i . As for the training model, we set the learning rates of actor network and critic networks as τ c = τ a = 5 × 10 -4 , and set the update rate ς = 5 × 10 -3 for soft updating the target networks. All experiments were conducted in a Python 3.10 environment with PyTorch 2.1.0 on a server running Ubuntu, equipped with a 2.10 GHz Intel Xeon Gold 5218R processor (40 cores, 503 GB RAM) and an NVIDIA A100 GPU featuring 80 GB of memory. More parameters about the considered scenario and proposed method are shown in Table II.

# Setting the RSMA message split number to two represents a rational and efficient trade-off in the context of this study. It preserves the core advantages of RSMA, namely flexible interference management and rate allocation, while avoiding the exponential growth in training and implementation complexity that would result from excessive message splitting.

## Algorithm 1 GDRS: Generative Diffusion-Enhanced DRL for RSMA-Enabled Low-Altitude MEC

```
Input: Initialize replay buffer B ; actor parameters ϑ ; critic parameters ϕ 1 , ϕ 2 ; target parameters ˆ ψ 1 ← ψ 1 , ˆ ψ 2 ← ψ 2 ; training step index e ; diffusion step index t ; trajectory counter q . 1 while e < E do 2 while q < Q do 3 Determine the optimal decoding order π according to Lemma 1; 4 Observe current state s ( n ) ; sample initial noise z T ∼ N ( 0 , I ) ; 5 while t < T do 6 Apply denoising model σ ϑ ( z t , t, s ( n )) ; 7 Compute mean µ ϑ and variance ˜ φ t using (33) and (30); 8 Update z t using (35); 9 t ← t +1 ; 10 Sample discrete action a ( n ) to determine UAV trajectory, offloading, and power allocation; 11 Execute a ( n ) in the environment; record the resulting reward r ( n ) and the subsequent state s ′ ( n ) ; 12 Store the transition tuple ( s ( n ) , a ( n ) , r ( n ) , s ′ ( n )) in B ; 13 Randomly select a mini-batch of samples from B ; 14 Update critic parameters ψ 1 , ψ 2 using (40), (42); 15 Update actor parameters ϑ using (43) and (44); 16 Perform soft updates on ˆ ψ 1 , ˆ ψ 2 via (39); 17 q ← q +1 ; 18 e ← e +1 ; Output: Optimized actor policy ϑ ∗ .
```

- 2. Baseline Settings: To present fair comparison, we compare our proposed GDRS method with the following well-known DRL benchmark :
- PPORS: Proximal Policy Optimization for RSMAenabled low-altitude MEC, where the agent learns an optimal policy in a discrete action space to maximize the energy efficiency.
- DQNRS: Deep Q-Network for RSMA-enabled lowaltitude MEC, where the agent approximates the optimal action-value function in a discrete action space to maximize the energy efficiency.
- GDRS-Random: Generative diffusion-enhanced optimization for RSMA-enabled low-altitude MEC, where UAV adopts the random decoding order for uplink GTs instead of optimal policy proposed in Lemma 1.

Additionally, in order to validate the effectiveness of the RSMA framework in supporting low-altitude MEC systems, we also design generative diffusion-enhanced algorithms under different multiple access schemes as baseline approaches :

TABLE II SYSTEM PARAMETERS

- GDFD: Generative diffusion-enhanced optimization for Frequency Division Multiple Access (FDMA)-enabled low-altitude MEC, where the uplink bandwidth is equally divided among GTs, ensuring orthogonal transmissions without inter-user interference.
- GDNO: Generative diffusion-enhanced optimization for NOMA-enabled low-altitude MEC, where multiple GTs simultaneously share the same uplink resources via power-domain superposition coding and successive interference cancellation at the UAV.

## B. Experimental Results

Fig. 3 plots the average reward obtained by GDRS and the baseline algorithms over training episodes. First, GDRS converges substantially faster and attains a higher steady-state reward than all baselines. Specifically, the reward curve of GDRS rises sharply and stabilizes at a high value after about 110 training episodes. Furthermore, the proposed GDRS method outperforms PPORS and DQNRS. This is because PPORS and DQNRS rely on conventional policy updates that often become trapped in local optima, while GDRS leverages generative diffusion sampling to better explore feasible actions. In addition, compared to the method with random decoding order, GDRS exhibits less fluctuation in its training curve and achieves a higher average reward, demonstrating that the optimized decoding order enables more effective successive interference cancellation and higher reward accumulation.

Fig. 3. The reward curves of the proposed GDRS algorithm and other baselines for RSMA-enabled LAE MEC systems over training episodes.

<!-- image -->

Fig. 4. The reward curves of the proposed GDRS algorithm under different learning rate.

<!-- image -->

Fig. 4 examines the training reward curves of the proposed GDRS algorithm under different learning rates. When the learning rate is set to 5 × 10 -4 , the training curve achieves higher reward values compared to those with learning rates of 1 × 10 -4 and 1 × 10 -3 . This is because a large learning rate causes excessively large update steps, resulting in unstable training for the agent. Conversely, a small learning rate leads to a slow learning process and causes the training to converge prematurely or get trapped in a local optimum. A learning rate of 5 × 10 -4 strikes a better balance between learning stability and update efficiency. Therefore, all subsequent experiments adopt a learning rate of 5 × 10 -4 .

Fig. 5a investigates how the number of diffusion steps T affects the achieved average reward under different numbers of GTs K . First, we observe that the GDRS method with 20 denoising steps outperforms the version with 10 denoising steps, indicating that increasing the number of denoising steps helps the DRL agent learn more generalizable features, thereby enhancing training generalization. However, the GDRS method with 30 denoising steps yields a significantly lower average reward compared to the 20-step case. This is because an excessive number of denoising steps can remove valuable features from the data, reducing training efficiency. Furthermore, as the number of GTs increases, the average reward under all denoising configurations decreases noticeably. This is due to the increased UAV flight energy consumption caused by the larger number of GTs under a fixed computational capacity, leading to reduced energy efficiency. Moreover, Fig. 5b illustrates the inference latency of the proposed GDRS framework under different numbers of denoising steps. As the number of denoising steps increases, the inference latency correspondingly grows. Despite this growth, the inference time of the proposed GDRS remains within an acceptable sub-second range, which is still feasible for real-time decision-making in UAV-assisted MEC scenarios.

Fig. 5. (a) The impact of diffusion steps T on average reward under different number of GTs K . (b) Inference time evaluations of different methods.

<!-- image -->

Fig. 6. Energy efficiency of different methods versus the number of GTs.

<!-- image -->

Fig. 6 compares the energy efficiency of different methods versus the number of GTs. We find that all methods exhibit a downward trend as the number of GTs increases. This is because the addition of GTs introduces more stringent offloading and communication demands, leading to higher UAV propulsion energy consumption and reduced per-user resource availability. Moreover, we observe that the proposed GDRS method consistently achieves the highest energy efficiency across the entire range of GTs. In particular, the performance gap between GDRS and the baseline methods becomes more pronounced as the network density increases. This is attributed to the diffusion-guided exploration and adaptive RSMA decoding, which jointly enable efficient interference management and resource utilization in dense multiuser scenarios. Additionally, it can be seen that GDRS significantly outperforms GDFD. The main reason is that RSMA with optimized message splitting and decoding allows for concurrent transmissions over shared spectrum resources, whereas orthogonal allocation in FDMA-like schemes such as GDFD inevitably suffers from severe spectral inefficiency when the number of GTs grows.

Fig. 7. Energy efficiency of different methods versus the maximum of transmit power of each GT.

<!-- image -->

Fig. 8. Energy efficiency versus the total time slots of UA V under different multiple access methods.

<!-- image -->

Fig. 7 compares the energy efficiency of different methods versus the maximum transmit power of each GT. We find that all methods exhibit an upward trend as the maximum transmit power increases. This indicates that granting GTs higher transmit power generally enables more data bits to be offloaded and processed, and the growth in data bits outpaces the increase in UAV energy consumption. Moreover, we observe that the proposed GDRS method consistently achieves the highest energy efficiency across the entire power range, and the performance gap between GDRS and the baseline methods widens as the number of GTs increases. This is because its diffusion-guided exploration and optimized decoding order jointly convert increased transmit power into higher throughput while mitigating multiuser interference. Additionally, we can observe that GDRS outperforms GDFD in terms of energy efficiency. This is because RSMA with optimized decoding enables concurrent transmissions over shared bandwidth, whereas orthogonal allocation of FSMA limits spectral efficiency.

Fig. 9. Energy efficiency of different methods versus the data size of computation task of each GT.

<!-- image -->

Fig. 8 evaluates the energy efficiency versus the total number of time slots under different multiple access schemes. We compare the proposed RSMA-based system with representative NOMA-based scheme and FDMA-based scheme. First, all schemes exhibit an increase in energy efficiency as the time horizon expands. Intuitively, with more time slots, the UAV has greater flexibility to serve the offloading requests in a staggered manner and can fly in a more energy-conservative trajectory, thereby improving the overall energy efficiency. Besides, the RSMA-enabled system achieves the highest energy efficiency, significantly outperforming both the NOMA and OMA cases. As the number of time slots increases, the energy efficiency gap widens because RSMA can more fully exploit the extra time to optimize power allocation and decoding order among users. Since it still allows concurrent transmissions with SIC, the NOMA-based system is generally second-best here, but it suffers from higher interference and less flexible rate allocation than RSMA, resulting in lower efficiency. The OMA method performs the worst energy-wise due to its poor spectral utilization. By enabling part of the interference to be treated as useful information, RSMA strikes an advantageous balance that NOMA and OMA cannot, thus delivering better performance especially in high-load or extended-duration scenarios.

In Fig. 9, we analyze how the energy efficiency of the various methods varies with the size of computation task of GT. The plotted results indicate a general upward trend in energy efficiency as the task size grows. When tasks are very small, the overhead of coordination and UAV operation is relatively significant, leading to lower energy efficiency for all schemes. In this regime, GDRS still maintains a slight edge over other methods, but overall efficiency is limited by fixed costs, because its optimized decoding and resource allocation reduce interference even for small tasks, yet the coordination and UAV propulsion overhead dominate the energy budget. As the task size increases, all methods become more energy-efficient. This is because larger batches of data can be offloaded and processed in one go, amortizing the energy cost of UAV trajectory and link setup over more bits. Notably, the energy efficiency of GDRS method improves the most rapidly and to the highest values. And the margin between GDRS and the others widens with task size, indicating that GDRS scales especially well to heavy workloads. This is because GDRS method minimizes unnecessary UAV movement and efficiently multiplexes the uplink transmissions via RSMA.

Fig. 10. Energy efficiency of GDRS and PPORS methods versus the processed rate of UAV under different communication bandwidth.

<!-- image -->

Fig. 10 plots the energy efficiency of GDRS versus the baseline PPORS against the processed rate of UAV under different bandwidth conditions. First, we observe that increasing the UAV's processed rate leads to higher energy efficiency for both GDRS and PPORS. With a faster onboard CPU, the UAV can execute offloaded tasks more quickly, reducing the time GTs spend transmitting. With a faster onboard CPU, the UAV can execute offloaded tasks more quickly, reducing the time GTs spend on data transmission. Moreover, the energy efficiency of GDRS consistently surpasses that of the PPORS method, demonstrating the advantage of the generative diffusion model in adapting to the complexity of low-altitude MEC offloading involving mobile UAV. In addition, under a fixed UAV processed rate, energy efficiency increases with communication bandwidth. When more bandwidth is available, uplink transmissions require less time or lower power for the same data volume, thereby improving the energy efficiency. Notably, even under constrained bandwidth conditions, GDRS outperforms the baseline, because the diffusion model enables more effective exploration of the hybrid action space than PPO, avoiding premature convergence and yielding better joint optimization of power allocation and decoding order. Specifically, when the UAV processed rate is set to 500 cycles/s and the bandwidth to 0.1 MHz, GDRS improves energy efficiency by approximately 47 . 3% compared to PPORS, confirming that whether the bottleneck lies in computation or communication, GDRS achieves better energy utilization.

Fig. 11 illustrates the UAV 3D trajectories under different methods. We observe that the proposed GDRS method yields a more structured and energy-aware trajectory that dynamically adapts to the spatial distribution of GTs, enabling efficient task offloading while minimizing redundant UAV motion. In contrast, the trajectories under PPORS and DQNRS exhibit erratic and less adaptive patterns, reflecting the limited exploration and poor generalization capability of traditional DRL approaches in high-dimensional hybrid action spaces, because their action sampling is restricted to local policy distributions without structured guidance, which leads to premature convergence and prevents learning globally efficient UAV trajectories. Additionally, the GDRS-Random method, which employs a stochastic RSMA decoding order, results in a degraded trajectory with inefficient hovering and detours, further highlighting the necessity of the decoding policy derived in Lemma 1.

Fig. 11. UAV trajectories in 3D space for different methods.

<!-- image -->

## V. CONCLUSION

In this work, we developed an uplink RSMA-enabled low-altitude MEC framework aimed at enhancing energy efficiency in highly dynamic and interference-limited wireless environments. By formulating a joint optimization problem involving UAV three-dimensional trajectory design, user task offloading, transmit power allocation, and RSMA decoding order, we addressed the fundamental coupling between computation and communication in airborne edge networks. To solve this high-dimensional and non-convex problem, we introduced a GDM-enhanced DRL algorithm, where the integration of generative sampling within the actor network significantly improves exploration quality and policy convergence in hybrid action spaces. Moreover, a priority-based RSMA decoding policy was derived to enable lightweight and effective interference management through successive interference cancellation. The simulation results confirmed that RSMA can flexibly manage multi-user interference and that diffusion-enhanced exploration provides superior adaptability to dynamic task and channel variations, enabling UAVs to follow energy-aware trajectories while maintaining low computational and communication overhead. In future research, we will extend our framework toward robust optimization under imperfect or delayed CSI, consider heterogeneous mobility patterns of users, and investigate multi-antenna MEC networks.

## REFERENCES

- [1] E. Calvanese Strinati et al., '6G: The next frontier: From holographic messaging to artificial intelligence using subterahertz and visible light communication,' IEEE Veh. Technol. Mag. , vol. 14, no. 3, pp. 42-50, Sep. 2019.
- [2] P. Porambage, J. Okwuibe, M. Liyanage, M. Ylianttila, and T. Taleb, 'Survey on multi-access edge computing for Internet of Things realization,' IEEE Commun. Surveys Tuts. , vol. 20, no. 4, pp. 2961-2991, 4th Quart., 2018.
- [3] L. Nadeem et al., 'Integration of D2D, network slicing, and MEC in 5G cellular networks: Survey and challenges,' IEEE Access , vol. 9, pp. 37590-37612, 2021.
- [4] Y. Jiang et al., 'Integrated sensing and communication for low altitude economy: Opportunities and challenges,' IEEE Commun. Mag. , early access, Apr. 2025, doi: 10.1109/MCOM.001.2400685.
- [5] C. Zhao et al., 'Generative AI-enabled wireless communications for robust low-altitude economy networking,' 2025, arXiv:2502.18118 .
- [6] S. Jeong, O. Simeone, and J. Kang, 'Mobile edge computing via a UAV-mounted cloudlet: Optimization of bit allocation and path planning,' IEEE Trans. Veh. Technol. , vol. 67, no. 3, pp. 2049-2063, Mar. 2018.
- [7] Y. Mao, O. Dizdar, B. Clerckx, R. Schober, P. Popovski, and H. V. Poor, 'Rate-splitting multiple access: Fundamentals, survey, and future research trends,' IEEE Commun. Surveys Tuts. , vol. 24, no. 4, pp. 2073-2126, 2022.
- [8] X. Wang et al., 'Resource allocation and user pairing for rate splitting multiple access based wireless networked control systems,' IEEE Trans. Commun. , vol. 73, no. 7, pp. 4795-4810, Jul. 2025.
- [9] H. Bastami, H. Behroozi, M. Moradikia, A. Abdelhadi, D. W. K. Ng, and L. Hanzo, 'Large-scale rate-splitting multiple access in uplink UA V networks: Effective secrecy throughput maximization under limited feedback channel,' IEEE Trans. Veh. Technol. , vol. 72, no. 7, pp. 9267-9280, Jul. 2023.
- [10] C. Zhang et al., 'Multi-objective aerial collaborative secure communication optimization via generative diffusion model-enabled deep reinforcement learning,' IEEE Trans. Mobile Comput. , vol. 24, no. 4, pp. 3041-3058, Apr. 2025.
- [11] C. Fang et al., 'DRL-driven joint task offloading and resource allocation for energy-efficient content delivery in cloud-edge cooperation networks,' IEEE Trans. Veh. Technol. , vol. 72, no. 12, pp. 16195-16207, Dec. 2023.
- [12] F. You and H. Du, 'ReaCritic: Large reasoning transformerbased DRL critic-model scaling for heterogeneous networks,' 2025, arXiv:2505.10992 .
- [13] H. Du et al., 'Enhancing deep reinforcement learning: A tutorial on generative diffusion models in network optimization,' IEEE Commun. Surveys Tuts. , vol. 26, no. 4, pp. 2611-2646, 2024.
- [14] X. Wang et al., 'Generative AI enabled matching for 6G multiple access,' IEEE Wireless Commun. , early access, Oct. 2025, doi: 10.1109/MWC.2025.3615555.
- [15] X. Xu, X. Mu, Y. Liu, H. Xing, Y. Liu, and A. Nallanathan, 'Generative artificial intelligence for mobile communications: A diffusion model perspective,' IEEE Commun. Mag. , vol. 63, no. 7, pp. 98-105, Jul. 2025.
- [16] F. You, H. Du, X. Hou, Y. Ren, and K. Huang, 'DRESS: Diffusion reasoning-based reward shaping scheme for intelligent networks,' 2025, arXiv:2503.07433 .
- [17] Z. Yang, S. Bi, and Y.-J.-A. Zhang, 'Dynamic offloading and trajectory control for UAV-enabled mobile edge computing system with energy harvesting devices,' IEEE Trans. Wireless Commun. , vol. 21, no. 12, pp. 10515-10528, Dec. 2022.
- [18] Z. Hu, F. Zeng, Z. Xiao, B. Fu, H. Jiang, and H. Chen, 'Computation efficiency maximization and QoE-provisioning in UAV-enabled MEC communication systems,' IEEE Trans. Netw. Sci. Eng. , vol. 8, no. 2, pp. 1630-1645, Apr. 2021.
- [19] B. Liu, Y. Wan, F. Zhou, Q. Wu, and R. Q. Hu, 'Resource allocation and trajectory design for MISO UAV-assisted MEC networks,' IEEE Trans. Veh. Technol. , vol. 71, no. 5, pp. 4933-4948, May 2022.
- [20] Y. Wang, J. Zhu, H. Huang, and F. Xiao, 'Bi-objective ant colony optimization for trajectory planning and task offloading in UAVassisted MEC systems,' IEEE Trans. Mobile Comput. , vol. 23, no. 12, pp. 12360-12377, Dec. 2024.
- [21] R. Han, Y. Wen, L. Bai, J. Liu, and J. Choi, 'Rate splitting on mobile edge computing for UAV-aided IoT systems,' IEEE Trans. Cognit. Commun. Netw. , vol. 6, no. 4, pp. 1193-1203, Dec. 2020.
- [22] J. Kim, E. Hong, J. Jung, J. Kang, and S. Jeong, 'Energy minimization in reconfigurable intelligent surface-assisted unmanned aerial vehicleenabled wireless powered mobile edge computing systems with ratesplitting multiple access,' Drones , vol. 7, no. 12, p. 688, Nov. 2023.

- [23] J. Chen et al., 'Deep reinforcement learning based resource allocation in multi-UAV-aided MEC networks,' IEEE Trans. Commun. , vol. 71, no. 1, pp. 296-309, Jan. 2023.
- [24] H. Pan, B. Lin, Y. Liu, S. Liang, and C. Yuen, 'Diffusion-modelenhanced multiobjective optimization for improving forest monitoring efficiency in UAV-enabled Internet of Things,' IEEE Internet Things J. , vol. 12, no. 19, pp. 40980-40996, Oct. 2025.
- [25] L. He et al., 'Generative AI for game theory-based mobile networking,' IEEE Wireless Commun. , vol. 32, no. 1, pp. 122-130, Feb. 2025.
- [26] Y. Fu, P. Qin, Y. Wang, L. Chen, M. Li, and X. Zhao, 'Over-the-air edge inference for low-altitude airspace: Generative AI-aided multi-task batching and beamforming design,' IEEE Trans. Commun. , vol. 73, no. 10, pp. 9013-9027, Oct. 2025.
- [27] J. Feng, X. Liu, Z. Liu, and T. S. Durrani, 'Optimal trajectory and resource allocation for RSMA-UAV assisted IoT communications,' IEEE Trans. Veh. Technol. , vol. 73, no. 6, pp. 8693-8704, Jun. 2024.
- [28] H. Bastami, M. Letafati, M. Moradikia, A. Abdelhadi, H. Behroozi, and L. Hanzo, 'On the physical layer security of the cooperative ratesplitting-aided downlink in UAV networks,' IEEE Trans. Inf. Forensics Security , vol. 16, pp. 5018-5033, 2021.
- [29] Q. Zhou, Y. Liu, H. Feng, and L. Wang, 'PRU group allocation and dynamic rate-splitting design for power minimization in IRS-assisted UAV MEC systems with RSMA,' IEEE Trans. Green Commun. Netw. , vol. 9, no. 3, pp. 1398-1413, Sep. 2025.
- [30] J. Liu et al., 'Optimizing resource allocation for multi-modal semantic communication in mobile AIGC networks: A diffusion-based game approach,' IEEE Trans. Cognit. Commun. Netw. , vol. 11, no. 5, pp. 3346-3360, Oct. 2025.
- [31] C. Zhao et al., 'Temporal spectrum cartography in low-altitude economy networks: A generative AI framework with multi-agent learning,' 2025, arXiv:2505.15571 .
- [32] X. Zhang and J. Yu, 'Improve the training efficiency of DRL for wireless communication resource allocation: The role of generative diffusion models,' 2025, arXiv:2502.07211 .
- [33] X. Wang, H. Du, L. Feng, F. Zhou, and W. Li, 'Effective throughput maximization for NOMA-enabled URLLC transmission in industrial IoT systems: A generative AI-based approach,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13327-13339, May 2025.
- [34] J. Zhang, Z. Liu, X. Feng, H. Yang, and S. Liang, 'Enhanced secure beamforming for IRS-assisted IoT communication using a generative-diffusion-model-enabled optimization approach,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13398-13414, May 2025.
- [35] J. Wang et al., 'A unified framework for guiding generative AI with wireless perception in resource constrained mobile edge networks,' IEEE Trans. Mobile Comput. , vol. 23, no. 11, pp. 10344-10360, Nov. 2024.
- [36] H. Mei, K. Wang, D. Zhou, and K. Yang, 'Joint trajectorytask-cache optimization in UAV-enabled mobile edge networks for cyber-physical system,' IEEE Access , vol. 7, pp. 156476-156488, 2019.
- [37] A. Al-Hourani, S. Kandeepan, and S. Lardner, 'Optimal LAP altitude for maximum coverage,' IEEE Wireless Commun. Lett. , vol. 3, no. 6, pp. 569-572, Dec. 2014.
- [38] X. Pang, N. Zhao, J. Tang, C. Wu, D. Niyato, and K.-K. Wong, 'IRS-assisted secure UAV transmission via joint trajectory and beamforming design,' IEEE Trans. Commun. , vol. 70, no. 2, pp. 1140-1152, Feb. 2022.
- [39] S. Han, J. Wang, L. Xiao, and C. Li, 'Broadcast secrecy rate maximization in UAV-empowered IRS backscatter communications,' IEEE Trans. Wireless Commun. , vol. 22, no. 10, pp. 6445-6458, Oct. 2023.
- [40] Y. Du, K. Wang, K. Yang, and G. Zhang, 'Energy-efficient resource allocation in UAV based MEC system for IoT devices,' in Proc. IEEE Global Commun. Conf. (GLOBECOM) , Dec. 2018, pp. 1-6.
- [41] Z. Yang, M. Chen, W. Saad, W. Xu, and M. Shikh-Bahaei, 'Sum-rate maximization of uplink rate splitting multiple access (RSMA) communication,' IEEE Trans. Mobile Comput. , vol. 21, no. 7, pp. 2596-2609, Jul. 2022.
- [42] J. Zhu, Y. Huang, J. Wang, K. Navaie, and Z. Ding, 'Power efficient IRSassisted NOMA,' IEEE Trans. Commun. , vol. 69, no. 2, pp. 900-913, Feb. 2021.
- [43] M. Zeng, X. Li, G. Li, W. Hao, and O. A. Dobre, 'Sum rate maximization for IRS-assisted uplink NOMA,' IEEE Commun. Lett. , vol. 25, no. 1, pp. 234-238, Jan. 2021.
- [44] J. Zhang, L. Zhu, Z. Xiao, X. Cao, D. O. Wu, and X.-G. Xia, 'Optimal and sub-optimal uplink NOMA: Joint user grouping, decoding order, and power control,' IEEE Wireless Commun. Lett. , vol. 9, no. 2, pp. 254-257, Feb. 2020.
- [45] M. A. Abd-Elmagid, A. Ferdowsi, H. S. Dhillon, and W. Saad, 'Deep reinforcement learning for minimizing age-of-information in UAV-assisted networks,' in Proc. IEEE Global Commun. Conf. (GLOBECOM) , Dec. 2019, pp. 1-6.
- [46] H. Du et al., 'Diffusion-based reinforcement learning for edge-enabled AI-generated content services,' IEEE Trans. Mobile Comput. , vol. 23, no. 9, pp. 8902-8918, Sep. 2024.
- [47] A. Q. Nichol and P. Dhariwal, 'Improved denoising diffusion probabilistic models,' in Proc. 38th Int. Conf. Mach. Learn. , vol. 139, M. Meila and T. Zhang, Eds., Jul. 2021, pp. 8162-8171.
- [48] J. Ho, A. Jain, and P. Abbeel, 'Denoising diffusion probabilistic models,' in Proc. Adv. Neural Inf. Process. Syst. , vol. 33, 2020, pp. 6840-6851.
- [49] L. Zhao, Z. Fei, J. Huang, X. Wang, B. Li, and W. Yuan, 'Deployment design for multi-UAV-assisted IoT networks: A digital twin-driven deep reinforcement learning approach,' IEEE Trans. Wireless Commun. , early access, Aug. 2025, doi: 10.1109/TWC.2025.3596864.
- [50] Y. Zhao et al., 'Joint deployment and resource allocation for multi-AeBS networks: A two-timescale optimization framework using MADRL,' IEEE Trans. Commun. , vol. 73, no. 6, pp. 4272-4289, Jun. 2025.
- [51] C. Liu, Y. Zhong, R. Wu, S. Ren, S. Du, and B. Guo, 'Deep reinforcement learning based 3D-trajectory design and task offloading in UAV-enabled MEC system,' IEEE Trans. Veh. Technol. , vol. 74, no. 2, pp. 3185-3195, Feb. 2025.
- [52] T. Zhang, K. Zhu, S. Zheng, D. Niyato, and N. C. Luong, 'Trajectory design and power control for joint radar and communication enabled multi-UAV cooperative detection systems,' IEEE Trans. Commun. , vol. 71, no. 1, pp. 158-172, Jan. 2023.

<!-- image -->

Xudong Wang received the B.Eng. degree from the School of Electronic and Information Engineering, Beijing Jiaotong University, Beijing, China, in 2021. He is currently pursuing the Ph.D. degree with the State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, Beijing. His current research interests include low-altitude networks, wireless networked control, interference management in wireless networks, and generative AI.

<!-- image -->

Hongyang Du (Member, IEEE) received the B.Eng. degree from Beijing Jiaotong University, China, and the Ph.D. degree from Nanyang Technological University, Singapore. He is currently an Assistant Professor with the Department of Electrical and Electronic Engineering, The University of Hong Kong, where he directs the Network Intelligence and Computing Ecosystem (NICE) Laboratory. His research interests include edge intelligence, generative AI, and network management. He was a recipient of the IEEE ComSoc Young Professional

Award for Best Early Career Researcher in 2024, the IEEE Daniel E. Noble Fellowship Award from the IEEE Vehicular Technology Society in 2022, the IEEE Signal Processing Society Scholarship from the IEEE Signal Processing Society in 2023, and Singapore Data Science Consortium (SDSC) Dissertation Research Fellowship in 2023. He serves as the Editor-in-Chief Assistant (2022-2024) and an Editor (-2025) for IEEE COMMUNICATIONS SURVEYS AND TUTORIALS; an Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, and IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY; and the Guest Editor for IEEE Vehicular Technology Magazine .

<!-- image -->

Lei Feng (Member, IEEE) received the B.Eng. and Ph.D. degrees in communication and information systems from BUPT in 2009 and 2015, respectively. From 2015 to 2018, he was a Post-Doctoral Research Fellow of computer science with the State Key Laboratory of Networking and Switching Technology, BUPT. He is currently an Associate Professor with the School of Computer Science, BUPT. He has co-authored about 80 technical peer-reviewed papers published in academic journals and conferences, including IEEE Communications

Magazine , IEEE Wireless Communications Magazine , IEEE TRANSACTIONS ON BROADCASTING, IEEE TRANSACTIONS ON COMPUTERS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE Network , and IEEE WIRELESS COMMUNICATIONS. His research interests include resource management in wireless networks, signal processing, and integrated sensing and communication in smart grid. He was a recipient of the 2022 IEEE International Conference on Communications (IEEE ICC 2022) Best Paper Award.

<!-- image -->

Kaibin Huang (Fellow, IEEE) received the B.Eng. and M.Eng. degrees in electrical engineering from the National University of Singapore and the Ph.D. degree in electrical engineering from The University of Texas at Austin. He is currently a Philip K. H. Wong Wilson K. L. Wong Professor of electrical engineering and the Department Head of the Department of Electrical and Electronic Engineering, The University of Hong Kong (HKU), Hong Kong. He is a fellow of the U.S. National Academy of Inventors. He was an IEEE Distinguished Lecturer. His work

was recognized with seven best paper awards from the IEEE Communication Society. He is a member of the Engineering Panel of Hong Kong Research Grants Council (RGC) and a RGC Research Fellow (2021 Class). He has served on the editorial boards of five major journals in the area of wireless communications and co-edited ten journal special issues. He has been active in organizing international conferences, such as the 2014, 2017, and 2023 Editions of IEEE Globecom, a flagship conference in communication. He has been named as a Highly Cited Researcher by Clarivate from 2019 to 2024 and an AI 2000 Most Influential Scholar (Top 30 in the Internet of Things) from 2023 to 2024.
