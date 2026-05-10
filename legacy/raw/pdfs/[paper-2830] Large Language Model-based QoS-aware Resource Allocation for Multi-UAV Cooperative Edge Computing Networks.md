---
title: Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks
authors:
  - Yaqing Wang
  - Lun Tang
  - Weili Wang
  - Xiaoqiang He
  - Qianbin Chen
abstract: |
  In 6G multiple unmanned aerial vehicles (UAVs) cooperative edge computing networks, strongly coupled system states and limited single-UAV observability lead to inefficient resource management and difficulty in guaranteeing Quality of Service (QoS). To address these issues, we propose a QoS-aware resource allocation method based on a large language model for multi-UAV cooperative edge computing networks.
keywords:
  - Multi-UAV cooperative edge computing
  - resource allocation
  - edge intelligence
  - large language model
  - deep reinforcement learning
extracted_date: "2026-05-09"
---

## Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks

Yaqing Wang, Lun Tang, Weili Wang, Xiaoqiang He, and Qianbin Chen Senior Member, IEEE

Abstract -In 6G multiple unmanned aerial vehicles (UAVs) cooperative edge computing networks, strongly coupled system states and limited single-UAV observability lead to inefficient resource management and difficulty in guaranteeing Quality of Service (QoS). To address these issues, we propose a QoS-aware resource allocation method based on a large language model (LLM) for Multi-UAV Cooperative Edge Computing Networks. First, we construct an LLM-based teacher-student resource allocation framework, operating with a global perspective, generates high-quality expert policies that are subsequently injected into distributed student agents via policy distillation, enabling efficient online decision-making in dynamic environments. Second, we design an LLM-based teacher model for accurate expert decision-making under dynamic network conditions. Specifically, we construct a time-varying network knowledge graph (NKG) to represent the complex spatiotemporal states of multi-UAV networks, employ a relation-aware graph attention network (R-GAT) to aggregate crucial neighborhood information and capture node importance, and further combine a fine-tuned LLM with a Tree-of-Thoughts (ToT) reasoning framework to produce high-quality expert resource allocation policies. Finally, we develop a multi-agent student model with policy distillation for efficient management of dynamic, multi-dimensional resources. We formulate a QoS objective that jointly considers delay and fairness, and jointly optimize user association, UAV trajectories, computing allocation, bandwidth allocation, and air-to-air (A2A) migration ratios. The student utilizes the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm and learns from the teacher efficiently via policy distillation, adapting adeptly to dynamic environments. Simulation results demonstrate that the proposed method achieves significantly faster convergence, lower steady-state delay, and higher fairness compared to baseline approaches, while also exhibiting robustness and scalability

This work was supported by National Natural Science Foundation of China (Grant No. 62401091), Chongqing Special Project for Technological Innovation and Application Development (CSTB2025TIAD-qykjggX0205), in part by National Natural Science Foundation of China (Grant No. 62541113), in part by Natural Science Foundation of Chongqing, China (No. CSTB2025NSCQ-GPX0796), in part by Scientific and Technological Research Project of Chongqing Municipal Education Commission (KJQN202503112, KJQN202503138), and in part by Teacher-Led Innovation Spark project by Chongqing Polytechnic University of Electronic Technology (25XJJSCX02).

Y. Wang, L. Tang, and Q. Chen are with the School of Communications and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing 400065, China, and also with the Chongqing Key Laboratory of Mobile Communications Technology, Chongqing, 400065, China. (email: 837887853@qq.com; tangluncq@163.com; lchenqb@cqupt.edu.cn;). Corresponding author:L. Tang(email:tangluncq@163.com).

W. Wang is with the School of Cyber Security and Information Law, Chongqing University of Posts and Telecommunications, Chongqing 400065, China, and also with the Chongqing Key Laboratory of Mobile Communications Technology, Chongqing 400065, China (e-mail: wangwl@cqupt.edu.cn).

X. He is with College of Communication Engineering, Chongqing Polytechnic University of Electronic Technology, Chongqing 401331, China. (e-mail: hexiaoq casey@foxmail.com)

across different network sizes and resource conditions.

Index Terms -Multi-UAV cooperative edge computing, resource allocation, edge intelligence, large language model, Deep reinforcement learning

## I. INTRODUCTION

W ITH the advent of 6G, Unmanned Aerial Vehicles (UAVs) are evolving from mere communication relays into integrated aerial edge computing and intelligence nodes, giving rise to multi-UAV cooperative mobile edge computing (MEC) networks [1]. Compared with conventional MEC, multi-UAV networks offer flexible deployment and superior line-of-sight (LoS) links, providing viable solutions for largescale, highly dynamic scenarios that demand guaranteed coverage and Quality of Service (QoS) [2]. This inherent flexibility enables deep cooperation among multiple UAVs, facilitating highly efficient joint resource allocation and forming a tightly coupled air-ground collaborative computing fabric. As a key enabler of advanced 6G systems, such cooperation holds broad potential [3].

Although a single UAV has powerful on-board sensing and computing capabilities, its overall performance is constrained by battery capacity and payload limits; its computing power is also difficult to schedule and provision a priori, making it hard to handle bursty and heterogeneous task arrivals on its own. Consequently, cooperative resource allocation among multiple UAVs becomes essential for sustaining high-quality service. However, in UAV-enabled edge intelligence (EI) systems, user distributions are non-stationary, task sets grow and shift, and network topology changes over time. Moreover, channel conditions between user devices (UDs) and UAVs, along with task demands, vary markedly with spatiotemporal conditions. Air-to-air (A2A) cooperation further introduces complex coupling across multiple resource dimensions (e.g., communication, computation, trajectory), rendering the joint optimization problem large-scale, non-convex, mixed-integer, and tightly coupled. These factors place stringent demands on system perception, coordination, and intelligent decisionmaking capabilities, motivating the need for more robust and sophisticated solutions [4].

To address this challenge, deep reinforcement learning (DRL) has been widely introduced for optimizing resource allocation objectives [5]. However, in multi-UAV cooperative edge networks, DRL's conventional 'from-scratch' exploration paradigm faces significant bottlenecks. As the numbers of UAVs and UDs grow, the joint action and state spaces expand exponentially, leading to sparse rewards, slow convergence, and policy instability [6]. Conventional DRL approaches are often slow and fragile, frequently getting trapped in low-return regions, which hinders the discovery of effective high-return policies [7] [8]. Recently, large language models (LLMs)-which acquire general knowledge and strong logical reasoning abilities from massive corpora [9]-have opened new avenues to overcome these limitations [10]. LLMs exhibit powerful decision-making and personalization capabilities [11]. Combining LLMs with DRL has thus become a promising research direction [12]: by leveraging the LLM's global planning and reasoning capacity alongside DRL's adaptive control prowess, LLMs can guide DRL exploration [13] [14], offering a feasible path to tackle the above challenges.

Despite progress, several key challenges persist in current multi-UAV edge intelligence networks: (1) Complexity of efficient resource cooperation in multi-UAV systems. The overall performance is often constrained by the computing capacity provisioned at edge servers. Since a single UAV has limited capability and cannot independently handle dense task requests, inter-UAV resource cooperation is essential for service quality. However, the states and performances of different UAVs become highly coupled: a UAV's load, resource availability, and location directly affect the performance and available resources of its neighbors, creating complex cascade effects. Achieving efficient, globally consistent resource coordination is therefore the first major challenge. (2) Joint optimization of multi-dimensional resources in highly dynamic environments. UAV networks operate under strong dynamics, reflected in real-time trajectory changes, stochastic task requests from ground devices, and sharp fluctuations in available bandwidth and computing resources. This time-varying nature turns resource allocation into a highdimensional, mixed-integer, strongly coupled joint optimization problem. The key challenge is how to realize precise, realtime allocation of multiple resources under such dynamics-so as to react promptly to environmental changes while meeting strict QoS constraints. (3) Limitations of conventional DRL. Standard DRL methods often converge slowly and are prone to suboptimal policies in complex action spaces, making them ill-suited to the joint optimization of multi-dimensional resources in dynamic multi-UAV networks and insufficient to meet the growing QoS demands of UDs. Overcoming DRL's exploration bottlenecks-by injecting high-quality priors to accelerate adaptation and learning-is thus a critical challenge.

To address the above challenges, we propose a QoS-aware resource allocation method for multi-UAV cooperative edge networks based on large language models (LLMs). By injecting global priors into DRL through a teacher-student distillation scheme, our approach handles multi-resource coupling in highly dynamic settings while jointly pursuing low delay and long-term fairness, significantly improving sample efficiency and online adaptability. Our main contributions are:

- 1. Teacher-student joint optimization framework for multi-UAV cooperative edge networks with LLMs: We design an LLM-assisted teacher model that produces high-quality expert policies. Through policy distillation,

2. this expert knowledge is effectively transferred to distributed student agents deployed on UAVs, accelerating their adaptation to dynamic scenarios and enhancing learning stability.

- 2. LLM-based teacher model tailored to dynamic networks for accurate, robust decision generation: To capture the highly coupled, heterogeneous states in multiUAV cooperation, we first construct a NKG that unifies topology and heterogeneous relations; then we use a RGAT to aggregate the importance of neighboring UAVs and encode structured knowledge for the LLM; finally, we apply LoRA fine-tuning together with Tree-of-Thoughts reasoning to generate high-quality expert decisions, providing reliable guidance for downstream optimization.
- 3. Student model with policy distillation for multiresource cooperative management in dynamic environments: We formulate a joint QoS objective that balances delay and fairness, and jointly optimize access control, UAV trajectory, computing allocation, bandwidth allocation, and A2A migration ratios. The student model is trained with MAPPO enhanced by policy distillation to achieve efficient multi-dimensional resource coordination. Experiments demonstrate that our method consistently outperforms baselines in both delay and fairness, and scales favorably with network size and resource variations.

The remainder of this article is organized as follows. Section II provides an overview of related works. Section III presents the system model. The problem formulation is proposed in Section IV. The novel algorithm based on the Teacher-Student framework is formulated in Section V. The simulation results are presented in Section VI, and this article is summarized in Section VII.

## II. RELATED WORKS

A. Resource Allocation for Cooperative Multi-UAV Networks

In cooperative UAV networks, [15] considers a multi-UAV collaborative offloading scenario and formulates an optimization problem that minimizes latency. It proposes a Lyapunovand perturbation-based algorithm and achieves a near-optimal offloading strategy. In [16], a multi-UAV edge-computing network assisted by reconfigurable intelligent surfaces is created; by jointly optimizing task association, transmit power, task splitting, and computing (CPU) frequency allocation with trajectory design, the long-term average delay is minimized. Lyapunov optimization and SAC are then used for online decision-making. In [17], they focus on cooperative sensing in a UAV network and propose a sensing-aware resourceallocation scheme that jointly maximizes QoE while minimizing transmission delay. The approach couples semantic communication with trajectory planning and adopts a mixedcooperative DRL method for online decision-making. In [18], they jointly optimize task offloading, server selection, and power allocation in a multi-UAV MEC scenario. It also plans UAV flight paths and CPU frequency to minimize energy consumption and processing delay under a total cost budget. In [19], they study MEC for UAV swarms and use the Age of Task (AoT) as the optimization objective while jointly optimizing trajectory and power via a BCD (block coordinate descent) + SCA solver to improve the timeliness metric. In [20], a multi-UAV edge-computing network with federated sensing is built, jointly optimizing data-sensing access, end-side power, UAV trajectory, and resource allocation, the long-term average sensing-throughput is maximized using a Lyapunov-based online method, while energy consumption and delay constraints are satisfied.

While the aforementioned studies address various resource allocation issues in multi-UAV scenarios, most focus predominantly on ground device-to-UAV or UAV-to-UD optimization. Relatively less consideration has been given to inter-UAV cooperation, including cross-UAV task migration and collaborative computing mechanisms among UAVs, which is a key focus of our work. Beyond UAV-centric MEC optimization, recent studies also emphasize traffic-aware slicing and adaptability under time-varying demands. In particular, Mohajer et al. propose FlexSlice [21], which jointly considers traffic-aware network slicing and an adaptive TD3-based offloading strategy. This line of work is complementary to ours: while FlexSlice focuses on traffic-aware slicing and adaptive control in MEC, our work targets multi-UAV cooperative edge computing with mobility-coupled decisions and explicit inter-UAV workload migration over A2A links.

## B. Applications of Large Language Models in Multi-UAV Systems

In recent years, LLMs are characterized by their strong content-generation and reasoning capabilities derived from vast pre-training corpora, have attracted wide attention in edge intelligence scenarios. A key research trend is how to build LLM-based cooperative mechanisms among resourceconstrained edge devices [22]-now a highly active topic [23][26]. For UAV networks in particular, computing, energy, and communications constraints are more pronounced, work coupling LLMs with UAV systems is still at an early stage [27]. In [28], they investigate joint optimization under an air-ground-cloud architecture, exploring LLMs as decision nodes on edge UAVs, together with data quantization and distributed inference, to enhance on-board intelligence for complex tasks. [29] combines LLMs with knowledge graphs to strengthen semantic representation, thereby improving UAVs' cross-domain knowledge understanding and their perception-and-reasoning ability for ground devices. [30] studies LLM-oriented optimization for integrated sensing-andcommunication tasks, demonstrating the potential of LLMs for jointly modeling perception and communication performance. In [31], they introduce an inverse-reinforcementlearning (IRL)-based 'intelligence' enhancement method that helps agents adapt to environment bias, thus improving crossscenario generalization.

## III. SYSTEM MODEL

## A. System Architecture

As depicted in Fig. 1, we consider a multi-UAV cooperative edge computing network operating within a hierarchical framework that integrates the cloud, UAV, and device layers.

- Device Layer: This layer comprises a set of K UDs, denoted by K = { 1 , 2 , . . . , K } , Each UD k ∈ K generates heterogeneous computation tasks, such as realtime video surveillance and traffic flow prediction.
- UAV Layer: This layer consists of a set of N UAVs, denoted by N = { 1 , 2 , ..., N } . Each UAV acts as an aerial edge server, equipped with on-board computing capabilities. This layer facilitates both ground-to-air (G2A) data uploads and air-to-air (A2A) task migration for cooperative processing among UAVs. The distributed Student Models are deployed on each UAV for real-time, online decision-making.
- Cloud Layer: The cloud layer, typically hosted in a ground station, possesses substantial computational resources. It is responsible for executing the global Teacher Model. The Teacher Model leverages its comprehensive network view to generate expert policies, which are then transmitted to the UAV layer via policy distillation to guide the Student Models.

The system operates over a time horizon partitioned into T discrete time slots, indexed by t ∈ { 1 , 2 , ..., T } , each with a duration of τ . The task generated by UD k ∈ K in slot t is denoted as M k ( t ) = { D k ( t ) , W k ( t ) , T max } , where D k ( t ) denotes the input data size, W k ( t ) the required number of CPU cycles, and T max the maximum tolerable delay. Due to the limited local processing capacity of UDs, tasks must be offloaded via G2A links to the UAVs for execution [16]. When a UAV serves a large number of UDs and its communication or computing resources approach saturation, it can migrate a portion of its tasks to neighboring UAVs via A2A links for cooperative processing. Therefore, this paper models both G2A and A2A transmissions.

## B. Communication Model

1. G2A Communication Model: Assume that all UAVs move at a fixed altitude H . Let the position of UAV n at slot t be d n ( t ) = ( x n ( t ) , y n ( t ) , z n ( t ) ) , and let the position of user device (UD) k be d k ( t ) = ( x k ( t ) , y k ( t ) , 0 ) . The 3D distance (in meters) between UD k and UAV n is d k,n ( t ) = ∥ ∥ d n ( t ) -d k ( t ) ∥ ∥

We adopt a probabilistic the line-of-sight (LoS) and nonline-of-sight (NLoS) path-loss model to capture blockage in realistic environments. Following [32], [33], the LoS probability between UD k and UAV n is

<!-- formula-not-decoded -->

where a and b are environment-dependent constants. Hence, the NLoS probability is P NLoS k,n ( t ) = 1 -P LoS k,n ( t ) . The freespace path loss (in dB) from UD k to UAV n is

<!-- formula-not-decoded -->

where f c is the carrier frequency and c is the speed of light. The total path loss (in dB) for the G2A link is then

<!-- formula-not-decoded -->

Fig. 1. System framework of the proposed Teacher-Student for multi-UAV cooperative architecture.

<!-- image -->

where η LoS and η NLoS denote the additional path loss for LoS and NLoS links, respectively.

The transmission rate from UD k to UAV n at slot t is

<!-- formula-not-decoded -->

where p k ( t ) denotes the transmit power of UD k , g k,n ( t ) is the channel gain, given by g k,n ( t ) = 10 -PL k,n ( t ) / 10 , ∑ k ′ ∈K\{ k } p k ′ ( t ) g k ′ ,n ( t ) represents the co-channel interference from other UDs within the coverage of UAV n , and σ 2 is the noise power. The term B k,n ( t ) denotes the bandwidth allocated by UAV n to UD k . Since the total bandwidth assigned by UAV n cannot exceed its available resource B n , the following constraint must hold:

<!-- formula-not-decoded -->

Define a binary variable δ k,n ( t ) ∈ { 0 , 1 } to indicate the association between UD k and UAV n at slot t . We set δ k,n ( t ) = 1 if UD k is associated with UAV n , and δ k,n ( t ) = 0 otherwise. In each slot, every UD can connect to at most one UAV, while a UAV may serve multiple UDs simultaneously. Hence, the access-control constraint is

<!-- formula-not-decoded -->

2. A2A Communication Model: Since A2A links among UAVs are typically LoS-dominant due to limited blockage in the air, we model the large-scale A2A channel gain using freespace path loss. The system operates in discrete time slots of duration τ , At the decision time scale, we assume the largescale channel is quasi-static within each slot, i.e., it is deter- mined by the UAV positions in slot t . Let the distance between UAV n and UAV n ′ at slot t be d n,n ′ ( t ) = ∥ ∥ d n ( t ) -d n ′ ( t ) ∥ ∥ .

To avoid collisions and keep the flight speed within a safe range, the trajectories must satisfy the minimum-separation constraint

̸

<!-- formula-not-decoded -->

where d min denotes the smallest allowable inter-UAV distance.

To ensure kinematic feasibility and prevent unrealistic interslot jumps, we impose the maximum-speed constraint

<!-- formula-not-decoded -->

The free-space path loss (in dB) of the A2A link is

<!-- formula-not-decoded -->

The data rate from UAV n to UAV n ′ is

<!-- formula-not-decoded -->

where B n,n ′ ( t ) is the bandwidth allocated to the A2A link, p n ( t ) is the transmit power of UAV n , g n,n ′ ( t ) = 10 -PL n,n ′ ( t ) / 10 is the channel gain of the A2A link, and σ 2 n ′ is the noise power at receiver n ′ .

Due to the limited on-board computing resources, a UAV may allocate a portion of its tasks to neighboring UAVs for cooperative processing. Let γ n,n ′ ( t ) ∈ [0, 1] denote the fraction of the task that UAV n migrates to a neighboring UAV n ′ at slot t . Due to the limited A2A radio range, we define the dynamic neighbor set of UAV n at

<!-- formula-not-decoded -->

R A 2 A denotes the maximum A2A distance to guarantee a reliable link. Task migration is only permitted to UAVs in N n ( t ) , i.e., γ n,n ′ ( t ) = 0 , ∀ n ′ / ∈ N n ( t ) . The migrated data size is D n,n ′ ( t ) = γ n,n ′ ( t ) D k ( t ) . Accordingly, the fraction processed on the original UAV n is 1 -∑ n ′ ∈N γ n,n ′ ( t ) , and the retained data size at UAV n is D n ( t ) = ( 1 -∑ n ′ ∈N γ n,n ′ ( t ) ) D k ( t ) . We consider divisible workloads, where the task can be partitioned into independently executable subtasks

## C. QoS-aware Problem

In a multi-UAV cooperative edge computing network, UDs face two core QoS requirements:

- Delay sensitivity. Tasks such as traffic prediction and emergency assessment demand that both transmission and computation be completed within a stringent time window. If the end-to-end delay exceeds the predefined deadline, the task may become obsolete, rendering the result useless. Therefore, delay is a critical QoS metric.
- Resource allocation fairness. Due to significant variations in distance, channel conditions, and task loads

among UDs served by different UAVs (and even among UDs attached to the same UAV), users with favorable conditions may receive a disproportionately large share of resources. Conversely, remote or disadvantaged users might experience long-term under-service or even resource starvation, which degrades the overall user experience.

Optimizing either of these goals in isolation can be detrimental to the other. For instance, exclusively pursuing minimal delay may lead to severe bias against UDs located far from a UAV, whereas strictly enforcing fairness could increase local congestion and overall latency. Consequently, we formulate a joint optimization problem that aims to minimize the delay while upholding a high standard of fairness.

Moreover, UAVs are battery-powered. Uncontrolled energy consumption can interrupt tasks and jeopardize flight safety. To ensure safe and sustained service, we impose an energy constraint on each UAV, requiring that its total energy consumption not exceed E max , thereby guaranteeing safe and continuous flight.

## D. Delay Model

We consider both the transmission delay from UD to UAV and between UAVs, as well as the computation delay on UAVs.

1. UD-UAV transmission delay: At slot t , the uplink transmission delay for the task generated by UD k and associated with UAV n is

<!-- formula-not-decoded -->

where δ k,n ( t ) ∈ { 0 , 1 } is the association indicator, D k ( t ) is the input data size, and R k,n ( t ) is the G2A rate.

2. Computation delay on UAV n : Let f n,k ( t ) the effective CPU service rate (cycles/s) allocated by UAV n to the computation workload associated with UD k in slot t under CPU sharing, To explicitly capture the practical multi-task CPU sharing mechanism and the induced load coupling, the perslot CPU allocations at UAV n satisfy ∑ k ∈K δ k,n ( t ) f n,k ( t ) ≤ f max n , ∀ n ∈ N . where f max n is the maximum computing capability of UAV n . Then the computation delay on UAV n is

<!-- formula-not-decoded -->

where W k ( t ) is the required number of CPU cycles and γ n,n ′ ( t ) ∈ [0, 1] is the fraction of the task migrated from UAV n to a neighboring UAV n ′ .

3. UAV-UAV transmission delay: If a fraction γ n,n ′ ( t ) of the task is allocated from UAV n to UAV n ′ , the A2A transmission delay is

<!-- formula-not-decoded -->

where R n,n ′ ( t ) is the achievable A2A rate from n to n ′ .

4. Computation delay on the neighboring UAV n ′ : Let f n ′ ,n ( t ) denote the effective CPU service rate (cycles/s) allocated by the neighboring UAV n ′ to process the migrated portion received from UAV n in slot t under CPU sharing, To explicitly capture the multi-task CPU sharing at UAV n ′ , the per-slot CPU allocations at UAV n ′ satisfy ∑ n ∈N\{ n ′ } f n ′ ,n ( t ) ≤ f max n ′ , ∀ n ′ ∈ N . where f max n ′ is the maximum computing capability of UAV n ′ Then the corresponding computation delay is

<!-- formula-not-decoded -->

Combining the above, we consider divisible workloads where the portion retained at UAV n and the migrated portion processed at neighboring UAVs can be executed in parallel; thus, the end-to-end completion time is modeled as the max of the parallel branches the total delay for a task from UD k served by UAV n is

<!-- formula-not-decoded -->

The completion delay of UD k in slot t is

<!-- formula-not-decoded -->

which must satisfy the QoS deadline constraint T k ( t ) ≤ T max .

## E. Fairness Model

To avoid long-term under-service caused by path loss or load concentration, we adopt Jain's index [34] to measure the fairness of the service received by all UDs, ensuring a uniform quality of service as much as possible. First, let the instantaneous throughput of UD k at slot t be

<!-- formula-not-decoded -->

where R k,n ( t ) is the UD-UAV rate and δ k,n ( t ) ∈ { 0 , 1 } indicates the association.

The long-term average throughput of UD k up to slot t is defined by the running average:

<!-- formula-not-decoded -->

Accordingly, the fairness among UDs at time t is quantified by Jain's index:

<!-- formula-not-decoded -->

where J ( t ) ∈ [ 1 K , 1 ] . A value of J ( t ) closer to 1 indicates more equitable resource allocation. When J ( t ) = 1 K , a single UD monopolizes all resources, which corresponds to the most unfair case.

To make the fairness term comparable with the normalized delay term in the objective, we further define the normalized Jain's index as

<!-- formula-not-decoded -->

where ˜ J ( t ) ∈ [0, 1] .

## F. Energy Model

We consider the computation energy on UAVs and the transmission energy over A2A links in our model.

1. Local computation energy on UAV n : After UAV n receives the task of UD k , the energy consumed for local computation at slot t is modeled as:

<!-- formula-not-decoded -->

where κ is the effective switching capacitance coefficient, and denotes a fixed hardware-related parameter reflecting the processor's dynamic power characteristics in the adopted DVFS-based energy model. f n,k ( t ) is the CPU frequency allocated by UAV n to UD k , and γ n,n ′ ( t ) ∈ [0, 1] is the task fraction migrated to a neighboring UAV n ′ .

- 2. A2A transmission energy of UAV n : When UAV n migrates a fraction γ n,n ′ ( t ) of the task to a neighbor n ′ , the energy consumed by transmitting over the A2A link is

<!-- formula-not-decoded -->

where p n ( t ) is the transmit power of UAV n and T tra n,n ′ ( t ) is the A2A transmission delay from n to n ′ .

Combining the above, the total energy consumed by UAV n at slot t is the sum of its total local computation energy and its total A2A transmission energy, aggregated over all served UDs and all migration links:

<!-- formula-not-decoded -->

## IV. OPTIMIZATION FORMULATION

We aim to jointly optimize UD-UAV association, UAV trajectories, computation and bandwidth allocation, and the task migration fractions delegated to neighboring UAVs. Let the decision variables at slot t be ∆ ( t ) = { δ k,n ( t ) } , D ( t ) = { d n ( t ) } , F ( t ) = { f n,k ( t ) , f n ′ ,n ( t ) } , B ( t ) = { B k,n ( t ) } , Γ ( t ) = { γ n,n ′ ( t ) } for all k ∈ K and n, n ′ ∈ N . To comprehensively enhance system QoS, which encompasses both task completion delay and resource allocation fairness, we formulate the optimization problem based on a weighted delay-fairness (WDF) objective. Specifically, our goal is to minimize the following objective function:

̸

<!-- formula-not-decoded -->

The weighting parameters α and β reflect the relative QoS priorities between delay minimization and fairness enhancement, with α + β = 1 . A larger α makes the objective more delay-oriented and tends to favor lower latency, whereas a larger β makes the objective more fairness-oriented and tends to promote more balanced service among users. Therefore, the proposed framework can be adapted to different QoS preferences by adjusting the delay-fairness weighting. Constraint C1 ensures that each UD associates with at most one UAV in a slot. C2 guarantees collision avoidance via a minimum inter-UAV separation. C3 limits the movement of each UAV between consecutive time slots by enforcing a maximum flight speed v max . C4 limits the total bandwidth allocated by each UAV. C5 and C6 bound the local and cooperative CPU frequencies by the maximum computing capability of the serving UAV. C7 constrains the accumulated energy consumption of each UAV within the battery budget. Since the system runs over T slots of duration τ , C7 enforces the onboard energy budget E max over the episode window Tτ . C8 imposes the QoS deadline for task completion. C9 specifies the nonnegative weights for delay and fairness and normalizes them to sum to one.

## V. PROBLEM SOLUTION BASED ON TEACHER-STUDENT MODEL

The formulated optimization problem involves both discrete and continuous variables, resulting in a complex, non-linear, and non-convex multi-parameter problem. It falls into the class of mixed-integer nonlinear programming (MINLP) and is NPhard, making it intractable to solve exactly. Conventional DRL methods often struggle with inefficient exploration in such large action spaces; when an agent learns from scratch, it tends to suffer from low sample efficiency, slow convergence, and may get trapped in suboptimal policies. To address these challenges, we introduce a teacher-student policy distillation paradigm. We leverage an LLM-generated expert policy as the teacher for resource allocation decisions and devise a policydistillation mechanism to warm-start the student's learning process. This approach enables the student policy network to benefit from the teacher's prior knowledge, thereby improving initial performance, accelerating sample efficiency, and fostering more robust and accurate resource-allocation strategies in dynamic multi-UAV scenarios.

## A. LLM-Based Teacher Model for Multi-UAV Cooperative Resource Allocation

In multi-dimensional and highly-coupled UAV network resource allocation scenarios, relying solely on DRL with random priors often leads to low sample efficiency and slow convergence. To address this, we design a teacher model comprising three modules: a network knowledge graph (NKG) construction module, a GAT-based representation extraction module, and an LLM-based decision-making module. This architecture leverages the advanced reasoning and generative capabilities of LLMs to produce expert-level optimization policies. Specifically, we first construct a NKG to uniformly model the topology and resource dependencies of the dynamic airground cooperative environment. Next, we employ a relationaware graph attention network (R-GAT) to extract salient features from the NKG that capture each UAV's local state and its neighborhood context. Finally, we integrate a fine-tuned LoRA-based LLM with a Tree-of-Thoughts (ToT) reasoning framework to generate high-quality expert policies, which subsequently supervise the MAPPO training of the student model.

Under the proposed teacher-student architecture, the Teacher Model is deployed in the cloud to construct an aggregated global view from periodically collected state summaries, while the Student Models are deployed on UAVs for distributed real-time decision-making based on local observations. Accordingly, the Teacher provides expert guidance based on aggregated network information, whereas the Students continuously adapt their actions based on local observations. Therefore, the proposed framework does not require continuous full-state broadcasting among UAVs, and its signaling overhead mainly consists of periodic state reporting and occasional delivery of distilled guidance.

1. Network Knowledge Graph Construction in multi-UAV cooperative network: To capture the intricate topology and resource interactions in a dynamic multi-UAV cooperative environment, we construct a NKG. In a unified schema, physical entities (UDs, UAVs, base stations, and cloud servers) are represented as nodes, while dependencies such as communication, computation, and task migration are encoded as typed edges.

We define the time-varying knowledge graph in multi-UAV cooperative network as

<!-- formula-not-decoded -->

## where

- V ( t ) : the set of nodes at slot t , including UDs, UAVs, base stations, cloud/edge servers;
- R : the set of relation types; According to the scenario, includes three primary relations:
- (1) Communication link : if a feasible G2A path exists between a UD and a UAV, create a 'wireless access' relation.
- (2) Computing service : when a UAV can process a UD's task, create a 'compute service' relation.
- (3) Task migration : when two UAVs cooperate via an A2A link to process tasks, create a 'task migration' relation; the edge attribute stores the current migration ratio.
- E ( t ) ⊆ V ( t ) ×V ( t ) ×R : the set of typed relation triples;
- X ( t ) : is the collection of time-varying attributes attached to nodes and edges, describing the real-time state. These include:
- (1) Node attributes : position, battery level, CPU frequency, task data size, etc.
- (2) Edge attributes : inter-node distance, LoS probability, channel gain, allocated bandwidth, migration ratio, etc.

Fig. 2. LLM-Based Teacher Model for Multi-UAV Cooperative Resource Allocation

<!-- image -->

Because the NKG evolves with the system, we define three types of update rules:

- Node update : when a new UD joins or a UAV fails or recovers, add or remove the node in V ( t ) and synchronously create or delete its incident edges.
- Edge update : based on new association decisions, add or remove UD-UAV communication edges; if the bandwidth on a link drops to zero, delete that edge; when a migration policy is issued, create or update the corresponding 'task migration' edge and its ratio.
- Attribute update : for existing nodes or edges, update only their attributes in X ( t ) .

Compared to a static graph model, the proposed NKG naturally represents heterogeneous entities and multi-UAV interactions within a single schema, while its time-varying at- tributes provide structured background knowledge to the LLM. Coupled with GAT-based feature extraction, this yields rich relational representations that capture both network structure and physical state, enabling more accurate and generalizable decision-making.

- 2. RGAT-based Knowledge Feature Extraction: Given the highly dynamic nature of the multi-UAV environment, both the network topology and the relationships between entities evolve over time. Relying on simple neighborhood aggregation is insufficient to capture these dynamics. We therefore adopt a Relation-aware Graph Attention Network to extract salient features from the NKG. R-GAT allocates attention weights to neighbors conditioned on node and edge attributes for each distinct relation type. It then performs intra-relation aggregation followed by cross-relation fusion, thereby dynamically modeling the complex and time-varying inter-node dependencies. This mechanism enables node embeddings to encode topological and relational semantics, so that key neighbors and links (e.g., migration or bandwidth) are emphasized and the subsequent inference is more accurate and stable.

Let h ( 0 ) i denote the initial feature of each node i in the NKG, which is a vector formed by concatenating its text embedding and the type encoding of the node. Let x ( e ) ij be the edge attribute, and for each GAT layer l and relation r ∈ R , the unnormalized attention score from i to its neighbor j is

<!-- formula-not-decoded -->

where N r ( i ) is the set of neighbors of i under relation r , and j ∈ N r ( i ) . W ( l ) r , U ( l ) r are trainable linear transformations, a ( l ) r is the trainable attention vector, and ∥ denotes vector concatenation.

The normalized attention weight is obtained by a softmax over the relation-specific neighborhood:

<!-- formula-not-decoded -->

We then perform intra-relation aggregation to update the node features:

<!-- formula-not-decoded -->

To capture the heterogeneous impact of different relations on node i , we aggregate the features for each relation separately and then fuse them; We also employ a multi-head attention mechanism ( M heads) to improve stability and expressive power:

<!-- formula-not-decoded -->

where σ ( · ) is an activation function and ∥ denotes head-wise concatenation.

After propagating for L layers, each entity node in G obtains the final representation h ( L ) i , which integrates rich contextual information from its key neighbors across multiple relation types. This mechanism enables the model to learn deep feature

,

representations that fuse network structure with entity states, thereby enhancing the accuracy and robustness of subsequent decision-making.

- 3. LLM Decision Module Based on Tree-of-Thoughts: Foundation models are trained for broad, general-purpose scenarios. We therefore first perform lightweight domain adaptation via LoRA to align the LLM with our specific context. Since directly prompting an LLM for end-to-end solutions struggles with multi-objective, multi-constraint optimization, we then adopt the Tree-of-Thoughts framework [35] to guide the fine-tuned model in generating decisions that are diverse, accurate, and consistent with domain knowledge.
- a) Fine-tuning with LoRA: Although a pre-trained LLM possesses strong general reasoning abilities, a knowledge gap remains for specialized multi-UAV cooperative edge scenarios. To align the LLM's decisions with our specific setting, we employ a LoRA-based fine-tuning approach. Full-parameter finetuning is computationally prohibitive, requiring substantial resources to update the entire model. Consequently, parameterefficient fine-tuning (PEFT) methods are widely adopted. LoRA, a prominent PEFT method, freezes most weights in the pre-trained Transformer and injects low-rank, trainable layers into the attention blocks, thereby greatly reducing the number of trainable parameters and the associated training overhead.

3. Let W 0 denote a weight matrix in the pretrained model. LoRA injects two low-rank matrices B ∈ R s × r and A ∈ R r × d to construct a matched update ∆ W = BA . The fine-tuned LLM is then written as

<!-- formula-not-decoded -->

where r ≪ min( s, d ) . During training, W 0 is kept frozen and only the low-rank matrices B and A are updated, significantly reducing both the number of trainable parameters and the memory footprint.

- b) Multi-step Decision Making via Tree-of-Thoughts: Resource allocation in a multi-UAV network is a highdimensional combinatorial problem that must jointly consider UD association, UAV trajectory, computation and bandwidth allocation, and inter-UAV task migration under multiple constraints. Relying on an LLM to generate a one-shot solution often yields only a 'surface-level' plan. To exploit deeper reasoning, we adopt the Tree-of-Thoughts framework: a complex optimization problem is decomposed into a sequence of interdependent subproblems that are explored on a reasoning tree, while the LLM performs search over thought chains.

ToT generalizes chain-of-thought (CoT) [36] into a tree structure,where each root-to-leaf path corresponds to a complete CoT. Each node stores an intermediate thought, and edges link successive reasoning steps. This structure allows the model to explore diverse reasoning branches in parallel, backtrack, and compare different paths, thus mimicking human-like multi-step deliberation: generate, evaluate, and select among different lines of thought.

Let A = ( V , E ) denote the search tree, where the root encodes the initial global state, and each node v ∈ V keeps the current partial decision, its evaluation, and the corresponding local state. During generation, the LLM expands the tree, scores branches, and finally selects the root-to-leaf path with the lowest loss as the expert chain. Concretely, the procedure consists of four stages:

- 1. Problem Decomposition. Given the initial positions, resource states of all UAVs and UDs, residual energy, and task requests with their deadlines, the problem is decomposed into stepwise reasoning prompts. Following our system model, we split resource allocation into three sub-tasks:
- Task 1: UD association. This sub-task determines the association variables δ k,n ( t ) , matching to the most suitable UAV.
- Task 2: UAV trajectory planning. Given the user distribution and access requests, plan the next-step position d n ( t ) of each UAV by optimizing link quality while satisfying collision-avoidance constraints.
- Task 3: Resource and migration allocation: For already associated UDs, this sub-task determines the bandwidth { B k,n ( t ) } , compute resources { f n,k ( t ) , f n ′ ,k ( t ) } , and the migration ratio to a neighboring UAV γ n,n ′ ( t ) if needed.

Candidate Generation. At each node of the reasoning tree-i.e., at every decision step-the LLM receives the subtask prompt along with the current network snapshot and global features, and proposes multiple feasible solutions. Specifically, the sub-task prompt is constructed in a structured manner and includes the current sub-task description, the current-slot system state s t , the graph feature H ( L ) the retained partial decisions from previous reasoning steps, and the corresponding feasibility constraints. In this way, each ToT step uses a bounded structured context rather than a long conversational history. For a given sub-task Taski , we call the LLM with parameters θ to obtain K candidate actions together with their thought chains:

<!-- formula-not-decoded -->

where s t is the system state, H ( L ) = { h L i } i ∈V ( t ) is the final NKG features.

Quantitative Self-Evaluation. Each retained candidate branch is quantitatively evaluated according to the weighted delay-fairness objective. For the i -th retained candidate at slot t , its evaluation loss is written as

<!-- formula-not-decoded -->

where T ( i ) k ( t ) and ˜ J ( i ) ( t ) denote the delay and Jain's fairness index under the i -th candidate action, respectively. Lower loss indicates a better candidate branch.

Beam Search and Pruning. To efficiently navigate the large candidate space and approximate the best reasoning chain, we adopt a beam-search strategy with two tunable hyperparameters:

- Depth L : the tree expands from Task 1 to Task 3, A complete reasoning chain is obtained at depth 3, so we set the maximum search depth to L = 3 .
- Beam width B : at each layer, we retain the B chains with the lowest loss and prune the others. Each node expands at most K cand candidates.

After beam search reaches the final reasoning depth, we retain the topB complete candidate branches in the final beam. Let A T ( s t ) = { a (1) t , ..., a ( B ) t } denote the retained candidate action set. Their losses are normalized into confidence weights by

<!-- formula-not-decoded -->

where τ T is the temperature parameter. The Teacher policy distribution is defined as

<!-- formula-not-decoded -->

For expert action generation, the candidate with the highest probability is selected, while for policy distillation the full normalized distribution over the retained candidate set is used as the Teacher-side supervisory signal.

The time complexity of beam search is O ( B× K cand ×L ) . By searching the tree and pruning suboptimal branches, the model explores diverse alternatives. Candidates that severely violate constraints or deviate from the objective are discarded early, allowing computational resources to be focused on higher-quality solutions. Through this iterative 'analyze - generate - evaluate - search' cycle, the ToT framework ultimately returns a high-quality expert resource-allocation policy for the multi-UAV cooperative network.

Algorithm 1 LLM-based Teacher Policy Generation for Multi-UAV Cooperative Resource Allocation

Input: Global system state s t , previous knowledge graph G ( t -1) ; ToT depth L , beam width B , per-step candidates K cand ; RGAT layers L and heads M .

Output: Teacher policy distribution π T ( a t | s t ) .

- 1: Stage 1: NKG construction
- 2: for each slot t ∈ T do
- 3: Update node set V ( t ) (insert/remove nodes).
- 4: Update edge set E ( t ) (G2A link, computing service, task migration).
- 5: Update dynamic attributes X ( t ) (positions, battery, LoS probability, bandwidth, migration ratio).
- 6: Stage 2: R-GAT feature extraction
- 19: Stage 3: LLM decision module with ToT

- 7: Initialize node embeddings h (0) v .

- 8: for layer ℓ = 1 , 2 , . . . , L do

- 9: for node i ∈ V ( t ) do 10: for relation r ∈ R do 11: by

Compute unnormalized attention score c ( ℓ,r ) ij (27) for j ∈ N r ( i ) .

- 12: by (28).

Normalize to attention weight α ( ℓ,r ) ij

13:

Intra-relation aggregation to obtain ˜ h ( ℓ +1) i,r by (29).

- 14: end for

- 15: Multi-relation and multi-head fusion to obtain h ( ℓ +1) i by (30).

- 16: end for

- 17: end for

- 18: Let H ( L ) = { h L i } i ∈V ( t ) be the final NKG features.

Fig. 3. Student Model Based on MAPPO with Policy Distillation

<!-- image -->

- 20: Initialize the ToT root with ( s t , H ( L ) ) .
- 21: Decompose the decision into three sub-tasks: user association, UAV trajectory, and resource allocation.
- 22: for task i = 1 , 2 , 3 do
- 23: Candidate generation : use the LoRA-tuned LLM to generate K cand candidates for task i conditioned on ( s t , H ( L ) ) .
- 24: Candidate evaluation : score each candidate using the objective in (33).
- 25: Beam search &amp; pruning : keep the top B branches at the current ToT depth; expand until the maximum depth L is reached.
- 26: Update the ToT state with retained branches.
- 27: end for
- 28: Construct the Teacher policy distribution by softmaxnormalizing the negative evaluation losses of the topB complete candidates in the final ToT beam.
- 29: end for
- 30: return π T ( a t | s t )

## B. Student Model Based on MAPPO with Policy Distillation

The teacher leverages global context to infer a high-quality expert policy distribution and then transfers it to the student, providing guidance for decision making. The student follows an actor-critic paradigm and interacts with the environment through local sensing and partial observations to produce fast responses. However, in high-dimensional mixed action spaces, conventional deep RL can suffer from low sample efficiency, slow convergence, and suboptimal local minima. To inherit the teacher's prior knowledge while improving learning efficiency, we augment the student's MAPPO training with a loss term for policy distillation, which regularizes the deviation from the teacher distribution. In this way, the student can both acquire the teacher's expertise and maintain fast decision adaptation on the edge.

- 1. POMDP Formulation: As student agents (UAVs) operate with only local observations during execution and lack real-time access to the complete global state, we model the decentralized resource allocation problem as a Partially Observable Markov Decision Process (POMDP), defined by the tuple ⟨S ( t ) , A ( t ) , P , O ( t ) , R ( t ) , γ ⟩ .
- Agents: Each UAV n ∈ N acts as an individual agent.
- State Space S : At slot t , the global state includes the positions of all UDs and UAVs d k ( t ) , d n ( t ) , the bandwidth allocations between each UD and UAV B k,n ( t ) , the total bandwidth of each UAV B n ( t ) , and the computing CPU frequency of each UAV f n ( t ) . We write S ( t ) = { s 1 ( t ) , s 2 ( t ) , . . . , s N ( t ) } .
- Action Space A : At slot t , agent n takes action

<!-- formula-not-decoded -->

.

which contains the next-step UAV position, UD-UAV association, bandwidth allocated to each associated UD, and the task fraction migrated from UAV n to its neighbor n ′ . The joint action is A ( t ) = { a 1 ( t ) , a 2 ( t ) , . . . , a N ( t ) } .

- State transition: The kernel P is defined by the probability of transitioning from the current state s t to the next state s t +1 after taking action a t , i.e., P ( s t +1 | s t , a t ) .
- Observation: At slot t , UAV n observes its local state o n ( t ) , including its position, the task data size D k ( t ) , the required CPU cycles W k ( t ) , etc. The observation space of UAV n is O ( t ) = { o 1 ( t ) , o 2 ( t ) , . . . , o N ( t ) } .
- Reward: We further refine the reward by introducing penalties. The instantaneous reward of agent n at slot t is

<!-- formula-not-decoded -->

Here, 'feasible' means all constraints C1-C7 are satisfied; where ξ 1 penalizes collisions : when the distance between any two UAVs is less than the minimum safe separation d min , both agents are penalized; ξ 2 penalizes energy overflow : if a UAV's cumulative energy consumption exceeds its energy budget, a penalty is issued; ξ 3 penalizes no service : if a UD is not covered or is not associated with any UAV, the UD incurs a penalty. These penalties prevent service interruption and encourage broader coverage. The discount factor γ balances immediate and future rewards.

2. MAPPO with Policy Distillation: MAPPO follows an actor-critic architecture. The actor generates an action from the observed state, while the critic estimates the state-value or action-value to evaluate the current policy and improve it through interaction with the environment. Because samples collected by interacting with the environment can be highly correlated, and because mixed continuous-discrete action spaces are large, we adopt experience replay: trajectories are stored in a buffer and mini-batches are drawn at training time to improve sample reuse.

At the beginning, each agent's policy network is randomly initialized; let θ denote the parameters of the actor network for agent n , and ω the parameters of the critic network . At each slot t , given state s t , the UAV samples an action a n ( t ) from the policy and then executes it; Here, the Student policy is implemented as a hybrid discrete-continuous actor. Specifically, the association decision is modeled as a categorical action parameterized by softmax logits. The UAV trajectory action is represented as a bounded normalized displacement mapped by a tanh operator, while the bandwidth allocation, CPU allocation, and migration ratios are represented as nonnegative normalized fractions generated by softmax operators and then scaled by the corresponding resource budgets. In this way, the sampled action remains bounded and physically feasible during MAPPO training and execution. These transformations can be interpreted as an implicit projection step that maps candidate actions into the feasible action space, thereby ensuring that all resource constraints are satisfied. The environment transitions to the next state s t +1 and returns reward r ( t ) . To stabilize training and mitigate policy drift caused by long rollout horizons, we adopt the trust region idea in PPO: in each update, we optimize within a clipped ratio range using the 'new' actor (outputting the current action) and the 'old' actor (a frozen copy that produced the buffer trajectories). The MAPPO objective is

<!-- formula-not-decoded -->

where q t ( θ ) = π θ ( a t | o t ) π θ old ( a t | o t ) is the importance ratio, and the clipping function is

<!-- formula-not-decoded -->

which constrains the update to [ 1 -ε, 1 + ε ] so that policy changes remain small. Here θ old is the parameter of the behav- ior policy that generated the buffer data, ε is a hyperparameter, and ˆ A t is the advantage.

To obtain more stable training and reduce variance, we adopt a V-critic and generalized advantage estimation (GAE). The advantage is

<!-- formula-not-decoded -->

with temporal-difference error

<!-- formula-not-decoded -->

and the value loss

<!-- formula-not-decoded -->

where V ψ is the critic and ˆ V t = r t + γ V ψ ( s t +1 ) ,

We use Jensen-Shannon (JS) divergence as the distillation term. Compared with the KL divergence, JS is symmetric and avoids the mismatch direction issue. Let π T be the teacher policy and π S the student policy. Although the underlying action space includes both discrete and continuous components, the distillation process is not performed over the entire hybrid action space. Instead, the Teacher policy is defined as a discrete distribution over the finite candidate action set A T ( s t ) generated by the ToT module. The JS divergence between their action distributions at state s t is

<!-- formula-not-decoded -->

where the mixture policy is

<!-- formula-not-decoded -->

and the KL divergence is

<!-- formula-not-decoded -->

Hence,

<!-- formula-not-decoded -->

where the summation is taken over the finite candidate action set A T ( s t ) induced by the ToT-based teacher, rather than over the entire hybrid action space. We add the distillation regularizer to the PPO objective so that the student learns from the teacher while still improving via environment interaction:

<!-- formula-not-decoded -->

where λ V &gt; 0 and λ JS &gt; 0 are weighting hyperparameters. A larger λ JS enforces stronger imitation of the teacher, whereas a smaller value relies more on environment-driven learning. Complexity Analysis: The main computational overhead of the proposed framework is concentrated at the cloud-side Teacher, including NKG construction/update, R-GAT feature extraction, and LLM-based ToT reasoning, while the Student

## Algorithm 2 Multi-Agent Resource Allocation with Policy Distillation based on MAPPO

- Input: Number of episodes M , episode length T , number of agents N ; teacher policy π T ( · | s ) ; update epochs K upd; Replay buffer R ; actor parameters θ and critic parameters ψ .

Output: Student policy parameters θ ⋆ .

- 1: for episode = 1 , 2 , . . . , M do
- 2: Reset the environment; obtain initial global state s t and local observations o t .
- 3: for slot t = 1 , 2 , . . . , T do
- 4: for each UAV n = 1 , 2 , . . . , N do
- 5: Sample action a t from the actor π θ ( · | o t ) .
- 6: end for
- 7: Execute the joint action a ( t ) ; obtain reward r t , next global state s t +1 , and next observations o t +1 .
- 8: Store ( s t , o t , a t , r t , s t +1 , o t +1 ) into R .
- 9: end for
- 10: Use the centralized critic V ψ ( s t ) to compute bootstrapped returns.
- 11: Compute TD error as in Eq. (38) and GAE as in Eq. (37).
- 12: for k = 1 , 2 , . . . , K upd do
- 13: Sample a mini-batch M⊂R of size B .
- 14: for each UAV n = 1 , 2 , . . . , N do
- 15: Compute the actor loss with PPO clipping as in Eq. (35).
- 16: Compute the critic loss as in Eq. (39).
- 17: Compute the JS divergence between student and teacher policies as in Eq. (43).
- 18: Form the total loss as in Eq. (44).
- 19: end for
- 20: Update the actor parameters θ and the critic parameters ψ .
- 21: end for
- 22: end for
- 23: return θ ⋆ .

Models deployed on UAVs only perform lightweight online decision-making.

For NKG maintenance, the update cost under incremental graph updates can be approximately characterized by O ( | ∆ V ( t ) | + | ∆ E ( t ) | + | ∆ X ( t ) | ) . For R-GAT feature extraction, ignoring fixed feature dimensions, the approximate per-slot complexity is O ( L GAT · M · ∑ r ∈R | E r ( t ) | ) . For ToT reasoning, using beam search with depth L , beam width B , and at most K cand candidates per node, the search complexity can be approximated as O ( B × K cand × L ) .

## VI. SIMULATION RESULTS AND ANALYSIS

We conduct simulations using Python and PyTorch to validate the performance of our proposed algorithm. The simulation environment comprises a multi-UAV network with four UAVs operating at a fixed altitude of 100 m, maintaining a minimum safety separation of 10 m. Each UAV is equipped with a computing capability ranging from 10 to 20 GHz. The channel bandwidths are 20 MHz for G2A links and 40 MHz for A2A links, and the noise power is -100 dBm [37]. For propagation, we use a LoS path-loss exponent of 3 and add an additional 23 dB attenuation for NLoS links [38]. For UD tasks, the input data size is uniformly chosen from 1 to 3 MB, and the required CPU cycles are 300-500 M cycles.

As the teacher model, we adopt GPT-4o as the pretrained backbone and apply parameter-efficient fine-tuning via LoRA with rank r = 8 . The fine-tuned LLM performs ToT search on the teacher side to generate and evaluate candidate actions; the ToT hyperparameters are depth L = 3 , beam B = 6 , and candidates K cand = 5 . The teacher then outputs an expert policy distribution, which is used to perform policy distillation and supervise the student MAPPO training. In the reward design, the penalty coefficients are set to ξ 1 = 4 , ξ 2 = 2 , ξ 3 = 2 , corresponding to the collision penalty, the energybudget violation penalty, and the penalty for unserved users, respectively.

TABLE I SIMULATION PARAMETER SETTINGS

| Parameters                             | Value               |
| -------------------------------------- | ------------------- |
| Number of UAVs N                       | 4                   |
| Number of UDs K                        | [10, 60]            |
| Height of UAVs H                       | 100m                |
| Minimum distance of UAVs d min         | 10m                 |
| Data size of tasks D k ( t )           | [1, 3] MB           |
| Computing workload of tasks W k ( t )  | [300, 500] M cycles |
| Allowed delay threshold T max          | [250, 300] ms       |
| Channel bandwidth of G2A B k,n ( t )   | 20MHz               |
| Channel bandwidth of A2A B n,n ′       | 40MHz               |
| Noise power σ 2                        | -100dBm             |
| Path loss η Los , η NLos               | 3,23 dB             |
| Computation resource of UAVs f n ( t ) | [10, 20] GHz        |
| Transmit power of UAVs p n ( t )       | 20dBm               |
| Transmit power of UDs p k ( t )        | 10dBm               |
| The Rank of LoRA r                     | 8                   |
| ToT hyperparameters ( L,B,K cand ) L   | 3, 6, 5             |

Accordingly, the experimental evaluation mainly focuses on delay, fairness, and WDF performance, while the UAV energy budget is enforced through Constraint C6 and the energyoverflow penalty. To demonstrate the efficacy of our proposed algorithm, we compare it against four baseline methods:

- (1)Nearest: In a multi-UAV setting, each UD always offloads its task to the UAV with the smallest Euclidean distance.
- (2) PPO-Only: This variant uses PPO alone for optimization, with no teacher model, no Tree-of-Thought reasoning, and no knowledge distillation, all other settings match those of our student model.
- (3) 3D-MADDPG [39]: A fairness-aware scheme for multiUAV MEC scenarios. It employs MADDPG to jointly optimize UAV selection and 3D trajectories under system constraints, training with the objective of minimizing energy consumption based on fairness among UAVs.

(4)EEFC-TDBA [40]: This algorithm considers a singleUAV scenario without inter-UAV collaboration and uses DDPG to optimize the UAV's trajectory and resource allocation.

Fig. 4. Comparison of reward of different algorithms

<!-- image -->

Figure 4 presents the convergence performance of the algorithms during training. As observed, the reward curves for all methods increase steadily with the number of episodes and eventually stabilize, indicating that the agents gradually learn effective resource-allocation policies through interaction with the environment. From the figure, the proposed method rises more quickly and then levels off, demonstrating superior sample efficiency and final performance. This advantage is primarily due to the heuristic guidance provided by the teacher model combined with ToT reasoning, which yields higherquality candidates and more stable exploration. Although 3DMADDPG enables multi-agent cooperation, it lacks teacher guidance and a generate-score mechanism aligned with the global objective, resulting in slower convergence and inferior performance compared with our approach. PPO-Only, which does not employ a teacher or knowledge distillation, learns less efficiently; and EEFC-TDBA, lacking inter-UAV collaboration, performs the worst. Overall, the simulation results strongly validate the significant advantages of our method in convergence speed, final reward, and stability.

Figure 5 shows how the delay evolves with training episodes across all methods. Overall, except for Nearest, the curves drop rapidly and stabilize after approximately 300-400 episodes, indicating that the agents progressively learn more efficient access and resource allocation policies that shorten task completion time. The Proposed method decreases the fastest and attains the lowest delay, suggesting that teacher guidance from the LoRA-tuned LLM together with distillation regularization based on JS divergence enables more prompt hotspot load balancing across multiple UAVs and more effective intraUAV resource reallocation; it also exploits A2A task migration and bandwidth coordination more fully. 3D-MADDPG ranks second; although it enables cooperation, it lacks teacher-driven global-objective awareness and feasibility priors. PPO-Only, which has neither teacher signals nor distillation, relies on exploration and consequently converges more slowly, so both methods underperform the Proposed approach. EEFC-TDBA, which lacks inter-UAV collaboration, exhibits markedly higher delay. Nearest, whose distance-based association hardly improves with training, remains at a high delay throughout. Taken together, these results show that the Proposed method delivers significantly better convergence speed, final delay, and stability than the baselines.

Fig. 5. Comparison of delay for different algorithms

<!-- image -->

Figure 6 shows how delay varies with the number of devices. As the number of devices increases, competition for access and computing resources intensifies and link interference rises, leading to a higher system load; consequently, all methods exhibit an overall increase in delay. The Proposed method consistently achieves the lowest delay and shows the smallest increase with scale, demonstrating superior scalability. This advantage stems from teacher guidance and knowledge distillation, which provide high-quality candidate actions and constraint awareness, enabling the policy to proactively load-balance hotspots across multiple UAVs and coordinate resource allocation via A2A task migration. 3D-MADDPG and PPO-Only perform next best. EEFC-TDBA, which lacks interUAV collaboration, is heavily affected by congestion. Nearest performs substantially worse because it associates solely by distance without load balancing, causing delay to increase almost linearly as the number of devices grows. These results indicate that the Proposed method maintains lower delay and stronger scalability across a range of system sizes.

Figure 7 illustrates the relationship between UAV computing capability and delay. As the capacity increases from low to high, the delay of all methods decreases. The Proposed method maintains the lowest delay across the entire range. This advantage arises because teacher guidance and distillation provide high-quality priors, enabling the policy to proactively balance load and avoid congestion across multiple UAVs, while coordinating multi-dimensional resources-bandwidth and computing-via A2A task migration. Consequently, queuing and congestion overheads are effectively reduced. By comparison, although 3D-MADDPG and PPO-Only also benefit from increased computing capacity, they remain inferior to the Proposed method due to the absence of teacher priors or limitations in multi-dimensional coordination. EEFC-TDBA, which operates with a single UAV and lacks cooperative computing, shows a weaker response to increased capacity. Nearest relies solely on proximity-based association and scarcely considers cross-UAV cooperation, making it the least sensitive to capacity improvements; its curve is higher and reaches a plateau earlier. Overall, the results indicate that the Proposed method consistently achieves lower delay under diverse computing-resource settings.

Fig. 6. Delay of different algorithms under different number of devices

<!-- image -->

Figure 8 tracks the Jain's fairness index during training. In the early stages, when the policy has not yet matured, bandwidth and computing resources tend to be skewed toward a few users, leading to low fairness. With repeated interaction with the environment and the influence of the fairness term in the loss function, the agents gradually learn to allocate resources more evenly; distillation from the teacher policy distribution provides additional stable guidance, so fairness increases overall and eventually stabilizes. In comparison, the Proposed method rises the fastest and attains the highest level, indicating that candidate generation and evaluation via the LoRA-tuned LLM with ToT effectively suppress long-term bias. Although 3D-MADDPG supports multi-agent cooperation, it lacks teacher-guided global-objective awareness and thus still exhibits mild imbalance. PPO-Only, which introduces neither teacher signals nor knowledge distillation and relies on exploration, converges more slowly; hence both methods underperform the Proposed approach. EEFC-TDBA, which lacks inter-UAV collaboration, performs worse. Nearest is a simple non-learning strategy that associates purely by distance without load balancing, so its fairness does not improve with training. Overall, these results demonstrate that the Proposed method improves fairness more efficiently and more robustly.

Figure 9 compares the Jain's Fairness index across the number of devices. As device count increases, competition for access and computing resources intensifies and hotspots and load imbalance become more likely, resulting in an overall downward trend in fairness. The Proposed method experiences the smallest decline and maintains the highest index across the entire range, indicating that teacher guidance and distillation regularization provide constraint awareness and high-quality priors that enable the policy to proactively diffuse hotspots across multiple UAVs and to achieve more balanced intra-UAV bandwidth reallocation. 3D-MADDPG and PPO-Only exhibit some load awareness and decline more gradually as scale grows, but without teacher-guided global-objective awareness or distillation regularization, their redistribution capability lags behind the Proposed method, and hotspot UAVs gradually become overloaded. EEFC-TDBA, which lacks inter-UAV cooperation, achieves markedly lower fairness than the preceding three methods. Nearest declines the most because its greedy, distance-based association ignores instantaneous load, often causing local overload and idle resources, thereby depressing the Jain index. As the number of devices increases further, the system approaches saturation and load proportions stabilize, so the curves fluctuate mildly around a lower plateau toward the end. Overall, the Proposed method maintains higher and more stable fairness across different device counts.

Figure 10 compares the algorithms under two fairness measures. To justify the choice of the Jain index for fairness, we report both the Jain index and the Min-Max ratio as fairness utility functions, where the Min-Max ratio is defined as M = min 1 ≤ k ≤ K R k ( t ) max 1 ≤ k ≤ K R k ( t ) . Under both metrics, the five methods follow the same ranking: Proposed ranks first, 3DMADDPG second, PPO-Only third, EEFC-TDBA fourth, and Nearest last. This is consistent with the earlier conclusions on delay, utility, and fairness. The Proposed method leads on both metrics, indicating that, with teacher guidance from the LoRA-LLM and ToT together with distillation, the policy proactively diffuses hotspots across multiple UAVs and, within each UAV, achieves more balanced resource allocation, thereby markedly reducing the phenomenon of persistent neglect of a small subset of users.

In addition, the Jain index values are overall higher than those of the Min-Max ratio, reflecting that the latter is more sensitive to extremes (best and worst users) and therefore yields more conservative scores under the same policy. Nevertheless, both metrics produce the same relative ordering, which confirms the robustness advantage of the proposed approach and supports using the Jain index as a reasonable and more discriminative fairness measure.

Figure 11 illustrates how the WDF evolves over training episodes, where lower curves indicate smaller WDF values. Except for Nearest, all methods drop rapidly with episodes and then gradually stabilize, showing that the policies learn a better trade-off between delay and fairness. The Proposed method remains the lowest throughout and exhibits the smallest variance, indicating that teacher guidance from the LoRA-tuned LLM together with ToT and policy distillation enables the agent to reduce task delay and improve resource allocation fairness simultaneously, with better stability. 3D-MADDPG ranks second: although it supports cooperation, it lacks teacher-guided awareness of the global objective and feasibility priors, thus yielding higher values than the Proposed method. PPO-Only, which does not use a teacher or distillation and relies mainly on exploration, converges more slowly and attains a higher objective value. EEFC-TDBA, lacking collaboration among UAVs, is strongly affected by congestion. Nearest, which greedily associates by distance, shows almost no improvement. This ranking is consistent with the earlier results on delay and fairness, further confirming that the proposed algorithm improves overall QoS.

Fig. 7. Delay with different UAV computing capability

<!-- image -->

Fig. 8. Comparison of Jain's fairness index for different algorithms

<!-- image -->

Figure 12 shows the relationship between the WDF and the UAV computing capacity. As computing capacity increases, the WDF exhibits an overall decline. Higher CPU frequencies markedly shorten both local and cooperative computation time while also improving fairness, thereby benefiting both delay and fairness simultaneously. The Proposed method attains the lowest overall cost across the entire range because the LLMbased teacher model supplies high-quality expert policies that enable joint optimization of access, trajectory, and resource allocation. 3D-MADDPG and PPO-Only also benefit from increased capacity; however, lacking teacher priors and with limited multi-dimensional coordination, they remain inferior to the Proposed method. EEFC-TDBA adopts a single-UAV perspective without cooperative computing and therefore re- sponds more weakly to capacity improvements. Nearest relies solely on nearest association without cross-UAV coordination, resulting in the highest overall cost.

Fig. 9. Jain's fairness index of different algorithms under different number of devices

<!-- image -->

Fig. 10. Comparison of the different algorithms under two fairness measures

<!-- image -->

Figure 13 plots the WDF versus bandwidth. As bandwidth increases from 30 MHz to 70 MHz, the WDF of all methods decreases overall, indicating that greater available bandwidth effectively mitigates link congestion and queuing delays and thus reduces the objective value. The Proposed method attains the lowest values at all bandwidth points, reflecting stronger coordinated resource allocation under teacher guidance and distillation; moreover, its decline is more pronounced as bandwidth grows, showing that the policy effectively converts added bandwidth into improvements in both delay and fairness. 3D-MADDPG and PPO-Only rank next: although they benefit to some extent from additional bandwidth, the lack of teacher-driven global scoring and feasibility priors leaves residual resource bias. EEFC-TDBA, which lacks interUAV cooperation, gains only limited benefit from bandwidth expansion. Nearest associates solely by distance without load balancing, yielding the highest objective value and the smallest improvement. These results align with the episode-wise convergence trends, indicating that larger bandwidth generally lowers system cost, while cooperation and hierarchical decision-making remain advantageous across all bandwidth settings.

Fig. 11. Comparison of WDF for different algorithms

<!-- image -->

TABLE II ABLATION STUDY OF THE PROPOSED FRAMEWORK.

| Method                       | Components | Components | Components | Components | Metrics | Metrics  | Metrics |
| ---------------------------- | ---------- | ---------- | ---------- | ---------- | ------- | -------- | ------- |
|                              | NKG        | R-GAT      | ToT        | Distill.   | Delay   | Fairness | WDF     |
| Ours w/o ToT w/o w/o NKG w/o | ✓          | ✓ ✓ ×      | ✓          | ✓          | 244     | 0.918    | 0.448   |
|                              | ✓          |            | ×          | ✓          | 252     | 0.903    | 0.486   |
| R-GAT                        | ✓          |            | ✓          | ✓          | 259     | 0.891    | 0.522   |
|                              | ×          | ✓          | ✓          | ✓          | 266     | 0.879    | 0.558   |
| Distill.                     | ✓          | ✓          | ✓          | ×          | 273     | 0.862    | 0.594   |

To further validate the contribution of each key component, we conduct an ablation study by removing the NKG module, the R-GAT module, the ToT-based teacher reasoning module, and the Teacher-to-Student distillation module, respectively. As shown in Table II, the full model achieves the best overall performance in terms of delay, fairness, and WDF. Removing any one of these modules leads to a consistent performance degradation. In particular, removing the distillation module causes the largest drop, indicating that the Teacher-guided policy transfer plays a critical role in improving the final Student policy. Removing ToT also leads to a clear degradation, which confirms the importance of structured multi-branch candidate exploration in the Teacher module. In addition, the performance drops of w/o NKG and w/o R-GAT verify the effectiveness of structured knowledge modeling and relationaware feature extraction for multi-UAV cooperative resource allocation.

## VII. CONCLUSION

In this paper, we propose an LLM-based teacher-student joint optimization framework for 6G multi-UAV edge cooperative networks. The teacher model, operating with a global view, produces high-quality expert resource-allocation policies that serve as priors for the student. The student model adopts MAPPO augmented with a policy distillation; under a joint objective balancing latency and fairness, it makes coordinated decisions on access control, UAV trajectory planning, computation and bandwidth allocation, and A2A task migration ratio. Simulations demonstrate that, relative to strong baselines, our approach achieves faster convergence, lower steady-state latency, and improved fairness, while maintaining robustness and scalability as the network size and the available computing and bandwidth resources vary.

Fig. 12. WDF with different UAV computing capability

<!-- image -->

Fig. 13. WDF with different Bandwidth

<!-- image -->

## REFERENCES

- [1] L. Wang et al. , 'Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks,' IEEE Trans. Services Comput. , vol. 18, no. 4, pp. 2143-2157, Jul./Aug. 2025.
- [2] H. Guo, Y. Wang, J. Liu and C. Liu, 'Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond,' IEEE Trans. Wireless Commun. , vol. 23, no. 1, pp. 347-359, Jan. 2024.

- [3] P. Cao et al. , 'Computational Intelligence Algorithms for UAV Swarm Networking and Collaboration: A Comprehensive Survey and Future Directions,' IEEE Commun. Surv. Tutor. , vol. 26, no. 4, pp. 2684-2728, fourthquarter 2024.
- [4] S. Javaid, H. Fahim, B. He and N. Saeed, 'Large Language Models for UAVs: Current State and Pathways to the Future,' IEEE Open J. Veh. Technol. , vol. 5, pp. 1166-1192, 2024.
- [5] J. Zhang et al. , 'Decision Transformers for Wireless Communications: A New Paradigm of Resource Management,' IEEE Wireless Commun. , vol. 32, no. 2, pp. 180-186, Apr. 2025.
- [6] W. Zhao et al. , 'A Survey on DRL-Based UAV Communications and Networking: DRL Fundamentals, Applications and Implementations,' IEEE Commun. Surv. Tutor. , early access, Jun. 23, 2025, doi: 10.1109/COMST.2025.3581912.
- [7] S. Long et al. , 'A Survey on Intelligent Network Operations and Performance Optimization Based on Large Language Models,' IEEE Commun. Surv. Tutor. , early access, Jan. 07, 2025, doi: 10.1109/COMST.2025.3526606.
- [8] H. Kurunathan, H. Huang, K. Li, W. Ni and E. Hossain, 'Machine Learning-Aided Operations and Communications of Unmanned Aerial Vehicles: A Contemporary Survey,' IEEE Commun. Surv. Tutor. , vol. 26, no. 1, pp. 496-533, firstquarter 2024.
- [9] G. Qu, Q. Chen, W. Wei, Z. Lin, X. Chen and K. Huang, 'Mobile Edge Intelligence for Large Language Models: A Contemporary Survey,' IEEE Commun. Surv. Tutor. , early access, Jan. 09, 2025, doi: 10.1109/COMST.2025.3527641.
- [10] L. Cai, R. Zhang, C. Zhao, et al. , 'Large Language Model-Enhanced Reinforcement Learning for Low-Altitude Economy Networking,' arXiv preprint arXiv:2505.21045, 2025.
- [11] X. Li, H. Li, C. Sun, Q. Fan, Z. Han and V. C. M. Leung, 'EdgeEnhanced Intelligence: A Comprehensive Survey of Large Language Models and Edge-Cloud Computing Synergy,' IEEE Commun. Surv. Tutor. , early access, 2025, doi: 10.1109/COMST.2025.3587225.
- [12] P. F. Moshiri, M. A. Onsu, P. Lohan, et al. , 'Integrating Language Models for Enhanced Network State Monitoring in DRL-Based SFC Provisioning,' arXiv preprint arXiv:2502.11298, 2025.
- [13] H. Pang, Z. Wang and G. Li, 'Large Language Model Guided Deep Reinforcement Learning for Decision Making in Autonomous Driving,' arXiv preprint arXiv:2412.18511, 2024.
- [14] Z. Zhou, B. Hu, C. Zhao, et al. , 'Large Language Model as a Policy Teacher for Training Reinforcement Learning Agents,' arXiv preprint arXiv:2311.13373, 2023.
- [15] Z. Bai, Y. Lin, Y. Cao and W. Wang, 'Delay-Aware Cooperative Task Offloading for Multi-UAV Enabled Edge-Cloud Computing,' IEEE Trans. Mobile Comput. , vol. 23, no. 2, pp. 1034-1049, Feb. 2024.
- [16] C. Wang et al. , 'Computing Power in the Sky: Digital Twin-Assisted Collaborative Computing With Multi-UAV Networks,' IEEE Trans. Veh. Technol. , vol. 74, no. 9, pp. 14466-14482, Sept. 2025.
- [17] H. Hu, X. Zhu, F. Zhou, W. Wu, R. Q. Hu and H. Zhu, 'Resource Allocation for Multi-Modal Semantic Communication in UAV Collaborative Networks,' IEEE Trans. Commun. , vol. 73, no. 9, pp. 7599-7616, Sept. 2025.
- [18] F. Pervez, A. Sultana, C. Yang and L. Zhao, 'Energy and Latency Efficient Joint Communication and Computation Optimization in a MultiUAV-Assisted MEC Network,' IEEE Trans. Wireless Commun. , vol. 23, no. 3, pp. 1728-1741, Mar. 2024.
- [19] Y. Gao, J. Tao, Y. Xu, Z. Wang, Y. Gao and M. Wang, 'Improving User QoE via Joint Trajectory and Resource Optimization in Multi-UAV Assisted MEC,' IEEE Trans. Services Comput. , vol. 18, no. 3, pp. 14721486, May/Jun. 2025.
- [20] P. Qin, M. Fu, Y. Fu and J. Wang, 'Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network,' IEEE Trans. Wireless Commun. , early access, 2025, doi: 10.1109/TWC.2025.3582151.
- [21] A. Mohajer, J. Hajipour and V. C. M. Leung, 'Dynamic Offloading in Mobile Edge Computing With Traffic-Aware Network Slicing and Adaptive TD3 Strategy,' IEEE Commun. Lett. , vol. 29, no. 1, pp. 9599, Jan. 2025.
- [22] G. Liu, N. Van Huynh, H. Du, et al. , 'Generative AI for Unmanned Vehicle Swarms: Challenges, Applications and Opportunities,' arXiv preprint arXiv:2402.18062, 2024.
- [23] D. Ye et al. , 'Optimizing AIGC Services by Prompt Engineering and Edge Computing: A Generative Diffusion Model-Based Contract Theory Approach,' IEEE Trans. Veh. Technol. , vol. 74, no. 1, pp. 571-586, Jan. 2025.
- [24] X. Zhang et al. , 'Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks,' IEEE Trans. Wireless Commun. , vol. 24, no. 1, pp. 643-658, Jan. 2025.
- [25] Y. Hu, D. Ye, J. Kang, M. Wu and R. Yu, 'A Cloud-Edge Collaborative Architecture for Multimodal LLM-Based Advanced Driver Assistance Systems in IoT Networks,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13208-13221, 15 May 2025.
- [26] M. Zhang, X. Shen, J. Cao, Z. Cui and S. Jiang, 'EdgeShard: Efficient LLM Inference via Collaborative Edge Computing,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13119-13131, 15 May 2025.
- [27] Y. Tian, F. Lin, Y. Li, et al. , 'UAVs Meet LLMs: Overviews and Perspectives Towards Agentic Low-Altitude Mobility,' Inf. Fusion , vol. 122, Art. no. 103158, 2025.
- [28] S. Zhang et al. , 'Large Models for Aerial Edges: An Edge-Cloud Model Evolution and Communication Paradigm,' IEEE J. Sel. Areas Commun. , vol. 43, no. 1, pp. 21-35, Jan. 2025.
- [29] G. Sun et al. , 'Large Language Model (LLM)-Enabled Graphs in Dynamic Networking,' IEEE Network , vol. 39, no. 4, pp. 290-301, Jul. 2025.
- [30] H. Li, M. Xiao, K. Wang, D. I. Kim and M. Debbah, 'Large Language Model Based Multi-Objective Optimization for Integrated Sensing and Communications in UAV Networks,' IEEE Wireless Commun. Lett. , vol. 14, no. 4, pp. 979-983, Apr. 2025.
- [31] Y. Ren, H. Zhang, F. R. Yu, W. Li, P. Zhao and Y. He, 'Industrial Internet of Things With Large Language Models (LLMs): An Intelligence-Based Reinforcement Learning Approach,' IEEE Trans. Mobile Comput. , vol. 24, no. 5, pp. 4136-4152, May 2025.
- [32] X. Xu, G. Feng, S. Qin, Y. Liu and Y. Sun, 'Joint UAV Deployment and Resource Allocation: A Personalized Federated Deep Reinforcement Learning Approach,' IEEE Trans. Veh. Technol. , vol. 73, no. 3, pp. 40054018, Mar. 2024.
- [33] J. Yin et al. , 'QoS-Aware Energy-Efficient Multi-UAV Offloading Ratio and Trajectory Control Algorithm in Mobile-Edge Computing,' IEEE Internet Things J. , vol. 11, no. 24, pp. 40588-40602, 15 Dec. 2024.
- [34] R. K. Jain et al. , 'A Quantitative Measure of Fairness and Discrimination,' Eastern Res. Lab., Digit. Equip. Corporation, Hudson, MA, Rep. vol. 21, pp. 1-38, 1984.
- [35] S. Yao, D. Yu, J. Zhao, et al. , 'Tree of Thoughts: Deliberate Problem Solving With Large Language Models,' Adv. Neural Inf. Process. Syst. , vol. 36, pp. 11809-11822, 2023.
- [36] J. Wei, X. Wang, D. Schuurmans, et al. , 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models,' Adv. Neural Inf. Process. Syst. , vol. 35, pp. 24824-24837, 2022.
- [37] H. Hao, C. Xu, W. Zhang, S. Yang and G.-M. Muntean, 'Joint Task Offloading, Resource Allocation, and Trajectory Design for Multi-UAV Cooperative Edge Computing With Task Priority,' IEEE Trans. Mobile Comput. , vol. 23, no. 9, pp. 8649-8663, Sept. 2024.
- [38] 'Study on Enhanced LTE Support for Aerial Vehicles (Release 15),' 3GPP Std. 36.777, Dec. 2017.
- [39] Y. He, Y. Gan, H. Cui and M. Guizani, 'Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System,' IEEE Internet Things J. , vol. 10, no. 13, pp. 11383-11395, 1 Jul. 2023.
- [40] R. Ding, F. Gao and X. S. Shen, '3D UAV Trajectory Design and Frequency Band Allocation for Energy-Efficient and Fair Communication: A Deep Reinforcement Learning Approach,' IEEE Trans. Wireless Commun. , vol. 19, no. 12, pp. 7796-7809, Dec. 2020.

<!-- image -->

Yaqing Wang received the M.S. degree from Guangxi Normal University, Guilin, Guangxi, China, in 2021. She is currently pursuing the Ph.D. degree in communication and information systems with Chongqing University of Posts and Telecommunications, Chongqing, China. Her current research interests include edge intelligence computing, digital twin, and intelligent network management.

<!-- image -->

<!-- image -->

Lun Tang received the Ph.D. degree in communication and information system from Chongqing University, Chongqing, China, in 2010. He is currently a professor with the School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications. His current research interests include digital twin networks, 5G/6G, Industrial Internet of Things, and the Internet of Vehicles.

Weili Wang received the M.E. and Ph.D. degrees in information and communication engineering from Chongqing University of Posts and Telecommunications, Chongqing, China, in 2018 and 2023, respectively. She was a Visiting Researcher with Carleton University, Ottawa, ON, Canada, from December 2021 to January 2023. She is currently a Postdoctoral Researcher with Cyber Security and Information Law Research Center, Chongqing. Her current research interests include intelligent network management and self-healing techniques in 6G.

<!-- image -->

Xiaoqiang He received the Ph.D degree in Chongqing University of Posts and Telecommunications, Chongqing, China, in 2023. He is currently a lecturer with College of Communication Engineering, Chongqing Polytechnic University of Electronic Technology. From May 2019 to October 2020, he was a Visiting Graduate Student (Ph.D. student) with the Department of Electrical, Computer, and Biomedical Engineering, Ryerson University, Canada. His current research interests include mobile edge computing, edge intelligence computing,

intrusion detection system, and digital twin.

<!-- image -->

Qianbin Chen (M'03-SM'14) received the Ph.D. degree in communication and information system from the University of Electronic Science and Technology of China, Chengdu, China, in 2002. He is currently a Professor with the School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications, and the Director of the Chongqing Key Laboratory of Mobile Communication Technology. He has authored or co-authored over 100 papers in journals and peer-reviewed conference proceedings, and has co-

authored seven books. He holds 47 granted national patents.
