---
title: "LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks"
authors:
  - name: "Ziqiang Ye"
    affiliation: "National Key Laboratory of Wireless Communications, University of Electronic Science and Technology of China"
  - name: "Yulan Gao"
    affiliation: "KTH Royal Institute of Technology"
  - name: "Yue Xiao"
    affiliation: "National Key Laboratory of Wireless Communications, University of Electronic Science and Technology of China"
  - name: "Xianfu Lei"
    affiliation: "Southwest Jiaotong University"
  - name: "Pingzhi Fan"
    affiliation: "Southwest Jiaotong University"
  - name: "George K. Karagiannidis"
    affiliation: "Aristotle University of Thessaloniki"
abstract: "Secure communications in low-altitude economy networks (LAENets) are critical because the broadcast nature of air-ground links, the strong line-of-sight (LoS) propagation, and the high mobility of intelligent aerial agents (IAAs) inherently expose transmissions to agile, coordinated jamming and eavesdropping. This paper proposes a synergistic framework combining a lightweight retrieval-augmented generation (RAG)-enhanced large language model (LLM) with a soft actor-critic (SAC)-based reinforcement learning agent for joint optimization of frequency-hopping selection, trajectory control, and power allocation. The LLM predicts adversarial intent distributions across frequency bands and jammer trajectories, while the SAC agent enables anticipatory and context-aware secure communication. Simulation results demonstrate approximately 53.84% secrecy-rate improvement compared to baseline deep learning and reinforcement learning approaches."
keywords:
  - LAENet
  - LLM
  - Intelligent Aerial Agents
  - Security Communication
  - Trajectory Prediction
  - Frequency Hopping
  - Reinforcement Learning
doi: "10.1109/TNSE.2025.3647682"
publication_date: "2025-12-24"
year: 2025
journal: "IEEE Transactions on Network Science and Engineering"
---

Ziqiang Ye , Yulan Gao , Member, IEEE , Yue Xiao , Member, IEEE , Xianfu Lei , Member, IEEE , Pingzhi Fan , Life Fellow, IEEE , and George K. Karagiannidis , Fellow, IEEE

Abstract -Secure communications in low-altitude economy networks (LAENets) are critical because the broadcast nature of air-ground links, the strong line-of-sight (LoS) propagation, and the high mobility of intelligent aerial agents (IAAs) inherently exposetransmissions to agile, coordinated jamming and eavesdropping. In this paper, we consider a dynamic adversarial scenario where a legitimate IAA simultaneously provides service to multiple terrestrial receivers, while being threatened by collaborative adversarial entities comprising an intelligent UA V-based jammer and a ground-level eavesdropper. The adversaries cooperatively optimize their spatial trajectories and spectrum allocation strategies through real-time adaptive coordination. To counter such coordinated threats, we propose a synergistic framework where a lightweight retrieval-augmented generation (RAG)-enhanced large language model (LLM) predicts, from sequential wireless observations, the probabilistic jamming/eavesdropping intent distributions across frequency bands and the jammer's next-step trajectory. These predictions are then exploited by a soft actor-critic (SAC)based reinforcement learning agent at the IAA to jointly optimize frequency-hopping selection, trajectory control, and power allocation, thereby enabling anticipatory and context-aware secure communication. Simulation results demonstrate that, compared to baseline models from deep learning (DL) and reinforcement learning (RL) approaches, our framework achieves an average secrecy-rate improvement of approximately 53.84%, while also delivering faster convergence and greater robustness against adaptive, coordinated attacks. The experiments are conducted under comparable training budgets, and our approach outperforms typical DL models (e.g., convolutional neural network (CNN), long

Received 31 August 2025; revised 11 November 2025; accepted 9 December 2025. Date of publication 24 December 2025; date of current version 13 January 2026. This work was supported in part by the National Key R&amp;D Program of China under Grant 2025YFE0100900, in part by the National Natural Science Foundation of China under Grant 62271420 and Grant U23A20273, and in part by the Swedish Innovation Agency (VINNOVA) under Project Multi-RO6GIoT-GAI. Recommended for acceptance by Prof. Geng Sun. (Corresponding authors: Yulan Gao; Yue Xiao.)

Ziqiang Ye and Yue Xiao are with the National Key Laboratory of Wireless Communications, University of Electronic Science and Technology of China, Chengdu 611731, China (e-mail: yysxiaoyu@hotmail.com; xiaoyue@uestc. edu.cn).

Yulan Gao is with the Division of Information Science and Engineering, KTH Royal Institute of Technology, 100 44 Stockholm, Sweden (e-mail: yulang@ kth.se).

Xianfu Lei and Pingzhi Fan are with the School of Information Science and Technology, Institute of Mobile Communications, Southwest Jiaotong University, Chengdu 610031, China (e-mail: xflei@home.swjtu.edu.cn; p.fan@ ieee.org).

George K. Karagiannidis is with the Department of Electrical and Computer Engineering, Aristotle University of Thessaloniki, 54124 Thessaloniki, Greece (e-mail: geokarag@auth.gr).

Digital Object Identifier 10.1109/TNSE.2025.3647682

short-term memory (LSTM), Transformer) and optimization baselines (e.g., proximal policy optimization (PPO), simulated annealing) across secrecy rate, convergence speed, and robustness. This establishes the proposed framework as a practical solution for securing next-generation LAENets under coordinated jamming and eavesdropping.

Index Terms -LAENet, LLM, IAA, security communication, trajectory prediction, hop-frequency planning.

## I. INTRODUCTION

T HE rapid expansion of low-altitude economy networks (LAENets) [1], [2], [3], [4] has fundamentally transformed data collection and connectivity across applications such as environmental monitoring [5], [6], precision agriculture [7], [8], [9], and smart infrastructure management [10], [11], [12]. In these networks, a large number of distributed, low-power wireless devices communicate via intelligent aerial agents (IAAs) that act as mobile base stations under 1000 meters [13], [14]. However, the inherent broadcast nature and strong line-of-sight (LoS) propagation of IAA-ground links expose communications to a wide range of sophisticated attacks, including malicious jamming and pervasive eavesdropping [15], [16], [17]. Furthermore, the high density of ground terminals and the mobility of adversaries further exacerbate these security vulnerabilities. While essential, conventional cryptographic techniques are often inadequate against adaptive and coordinated attackers [18]; consequently, physical-layer security (PLS) has become an essential paradigm, exploiting wireless channel randomness and intelligent resource allocation to safeguard data confidentiality [19], [20].

Despite substantial progress in IAA-enabled physical-layer security, many prior works exhibit critical limitations when operating in the dynamic, dense, and highly adversarial environments characteristic of LAENets [21]. Classical deep-learning methods (e.g., convolutional nerual networks (CNNs)) often assume static or over-simplified models for eavesdroppers and jammers, neglecting their potential mobility, cooperation, and strategic adaptation [15], [22], [23]. Such assumptions frequently yield models effective only under idealized conditions, failing to capture the unpredictability and complexity of real-world attacks. Moreover, traditional solutions typically treat trajectory planning, frequency selection, and power control as sequential or decoupled subproblems, which leads to pronounced suboptimality and scalability issues. As network density grows or adversarial

2327-4697 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

strategies become more coordinated, these methods either incur prohibitive computational costs or cannot respond in real time to rapidly changing threats [24], [25]. In addition, many existing studies overlook propulsion-communication co-design and fall short of addressing the geometric and operational constraints imposed by practical LAENets deployments.

The recent wave of breakthroughs in generative artificial intelligence (GenAI) [26], [27], including diffusion models [28], transformers [29], [30], [31], and multi-modal foundation models [32], [33], are reshaping intelligent wireless communications and security. GenAI empowers agents not only to learn from massive, complex datasets but also to generate predictive scenarios and synthesize diverse behaviors in highly dynamic environments. These generative approaches excel at capturing intricate spatio-temporal dependencies, reasoning about intent, and modeling the strategic interaction between multiple agents. In particular, transformers and diffusion models have been explored for sequential prediction tasks, such as trajectory forecasting and learned policy generation, to support anticipatory resource management and preemptive strategy adjustment. Moreover, large language model (LLM)-driven retrieval-augmented generation (RAG) frameworks facilitate the extraction and abstraction of latent adversarial patterns from historical data, thereby improving situational awareness and decision-making. Building on this progress, LLMs have demonstrated strong capabilities in temporal reasoning, intent recognition, and context-aware prediction [34], [35], offering a new paradigm for proactive and adaptive wireless security via structured prompts and RAG (e.g., Telco-RAG) [36] that abstract latent adversarial strategies from sequential wireless observations.

Nevertheless, secure LAENets still faces three critical challenges: adversary modeling, coupled decision-making, and prediction-control integration. First, conventional deep learning (DL) methods typically assume static or overly simplified adversaries, neglecting the mobility, cooperation, and strategic adaptation of intelligent jammers and eavesdroppers [15], [22], [23]. These assumptions yield solutions that may perform well under idealized settings but fail to capture the unpredictability of real-world attacks. Second, trajectory planning, frequency selection, and power control are often optimized in isolated or sequential stages. This decoupling exacerbates the inherent non-convex coupling among decisions, weakens real-time responsiveness, and leads to suboptimal and poorly scalable solutions [24], [25], [37]. Third, predictive intelligence is insufficiently integrated with online control: intent forecasting is usually treated as an offline or point-estimate task, offering no uncertainty-aware guidance to the controller. This limitation becomes particularly critical under coordinated jamming and eavesdropping scenarios [17], [38].

Motivated by these challenges, we investigate a secure LAENet scenario where a legitimate IAA, a UAV-based jammer, and multiple cooperative mobile ground eavesdroppers in dynamic low-altitude airspace. We propose a unified framework that combines a lightweight Telco-RAG-enhanced LLM for intent and trajectory prediction with a soft actor-critic (SAC)based scheme for joint trajectory and resource optimization. The LLM generates probabilistic jamming and eavesdropping distributions across frequency bands, along with the jammer's predicted next-step position from sequential observations. These uncertainty-aware predictions are injected into the SAC agent as exogenous state features and are further used to construct a risk-aware secrecy reward that balances user rate performance against mobility and power costs. By bridging intent-driven prediction with deep DL, the proposed approach advances the state-of-the-art, and its superiority over conventional baselines is validated through extensive simulations. Accordingly, the main contributions of this paper are as follows:

- /a114 We propose a novel intent prediction module based on a lightweight LLM, which leverages structured prompts and historical wireless environment data to predict the probabilistic frequency selection, trajectory strategies of coordinated jammers and eavesdroppers in low altitude economy networks.
- /a114 We seamlessly incorporate the LLM-predicted intent distributions into a RL framework based on SAC, enabling the IAA base station to proactively optimize its trajectory, transmit power, and frequency allocation for realtime adaptation to sophisticated and dynamic adversarial threats, significantly improving the secrecy performance.
- /a114 Extensive simulations demonstrate that the proposed framework consistently outperforms existing DL and RLbased baselines in terms of trajectory and intent prediction accuracy, secrecy rate, and convergence speed. These results highlight the practical effectiveness and robustness of our approach for secure communications in low-altitude networks under coordinated jamming and wiretapping attacks.

Different from the existing works, our proposed framework explicitly accounts for cooperative interactions between jammers and eavesdroppers in both the frequency and spatial domains, thereby capturing more realistic and challenging threat scenarios. Moreover, while conventional approaches often decouple trajectory planning, spectrum selection, and power control into separate optimization problems, our design integrates these decisions by embedding a LLM-driven probabilistic intent prediction module directly into the RL loop. This integration enables proactive, context-aware strategy adaption based on predicted adversarial behaviors, allowing the system to responds swiftly to complex and dynamic attacks. As a result, by jointly optimizing trajectory, frequency allocation, and transmit power within a unified learning framework, the proposed approach overcomes the suboptimality and slow responsiveness of sequential optimization methods and achieves superior secrecyrate performance together with enhanced robustness in adversarial wireless environments.

Theremainder of this paper is structured as follows: Section II provides an overview of related research. Section III and IV detail the system model and secrecy rate analysis. Section V formulates the framework. Section VI presents simulation results, and Section VII concludes the work.

## II. RELATED WORK

The proliferation of LAENets and IAAs-assisted communication systems has fundamentally reshaped the landscape of wireless communications security. As these networks continue to expand in scale, complexity, and operational flexibility, they face a rapidly evolving array of security threats and system-level challenges. This section provides a comprehensive overview of existing research on jamming and eavesdropping threats in LAENets, on state-of-the-art anti-jamming and secure transmission strategies, and on the recent adoption of machine learning, particularly RL and LLMs for enhancing security and resilience. By systematically reviewing these key areas, we highlight the major limitations of current approaches and motivate the unified, intent-driven framework proposed in this work.

## A. Jamming and Eavesdropping Threats in LAENets

The security of LAENets has attracted growing attention due to the increasing deployment of IAAs-assisted communication systems. The broadcast nature of air-ground wireless transmissions, combined with the high mobility and density of devices in LAENets, renders such networks particularly vulnerable to sophisticated jamming and eavesdropping attacks [39], [40], [41], [42], [43], [44]. Adversaries employ diverse attack strategies, including power control, trajectory adaptation, and machinelearning-based policy optimization, with the goal of maximizing disruption and intercepting confidential information. For example, alternating optimization and successive convex approximation have been used to optimize transmit/jamming power and trajectories and thereby improve secrecy-rate performance [39], [41], [42], [45], [46], [47], while deep reinforcement learning and transfer learning have enabled more adaptive jamming in cellular systems [40], [48], [49], [50]. detection and adversarial intent inference are increasingly reliant on data-driven models, such as support vector machines (SVMs) and clustering algorithms [44]. While these attack strategies present significant security risks, they have in turn spurred the development of a diverse set of countermeasures at both the physical and higher layers, aimed at enhancing the resilience of LAENets communications in the face of sophisticated adversarial behaviors.

## B. Anti-Jamming and Secure Communication Strategies

In response to these adversarial threats, a wide range of anti-jamming and secure communication strategies have been extensively studied. At the physical layer, techniques such as artificial-noise (AN) injection, cooperative jamming, and adaptive beamforming have proved effective in mitigating interference and enhancing secrecy-rate performance [17], [38], [51], [52], [53], [54]. Furthermore, dynamic trajectory optimization and power control allow legitimate IAAs to avoid high-risk interference zones and to reduce the risk of eavesdropping [55], [56], [57]. Notably, segment-by-segment flight-path planning and joint resource allocation have been shown to improve secrecy-rate performance in time-varying environments [53], [55], [57], [58]. However, most existing works still assume static or independent adversaries and often rely on iterative optimization or hand-crafted feature design [17], [38], [59], [60], [61], which limits real-time responsiveness and scalability in large-scale LAENets. These limitations exacerbated by fast-evolving adversarial strategies and the increasing scale and heterogeneity of LAENets motivate more flexible, data-driven security frameworks that can counter coordinated, intelligent attackers. As a result, there has been growing interest in leveraging advanced machine learning and artificial intelligence approaches, notably RL and LLMs to endow UAV-assisted networks with adaptive and proactive defense capabilities.

Fig. 1. System model of IAAs-assisted secure communication under jamming and eavesdropping.

<!-- image -->

## C. AI-Driven Security Approaches

To address these challenges, machine learning, particularly reinforcement learning, has been increasingly adopted for adaptive and secure resource management in wireless networks. Supervised and deep learning methods have been used for spectrum management [62], [63], [64], [65], [66], [67], jamming detection [68], [69], [70], [71], and user modeling [72], [73], facilitating more data-driven network control [74], [75], [76]. However, these methods often require labeled data and fixed model structures, which constrains their utility for online, real-time optimization under uncertainty [77]. RL-based solutions empower UAVs and network agents to interact with their environments and autonomously learn optimal strategies for anti-jamming [78], secure spectrum access [79], and trajectory control [80]. More recently, intent-guided and generative RL models have emerged, such as diffusion-model-based trajectory generation [81], [82], [83] and transformer-enhanced soft actor-critic algorithms for complex resource optimization [84], [85]. Despite these advances, most RL frameworks still depend on local observations or simplified adversarial models, limiting their resilience to coordinated, adaptive attacks.

The advent of large language models (LLMs) has opened new frontiers for intent and sequence prediction in multi-agent systems [86]. LLMs demonstrate remarkable reasoning and pattern-extraction capabilities for temporal data, as evidenced by their success in human intent prediction [87], unsupervised intent discovery [85], [88], [89], and time-series forecasting [34],

[35], [90]. In particular, prompt-based and RAG LLMs can abstract latent adversarial strategies from sequential wireless observations, offering powerful tools for proactive and adaptive defense.

According to the above classification, similar to the works in [39], [41], this paper considers proactive defense adversarial jamming and eavesdropping in LAENets. Unlike recent LLM-RL hybrid approaches that primarily focus on sequential decision-making in isolated domains [91], our framework introduces a domain-specific integration where the Telco-RAGenhanced LLM generates probabilistic intent predictions that directly inform risk-aware reward shaping in the SAC controller, specifically designed to counter coordinated multi-domain adversarial strategies in dynamic low-altitude networks. However, unlike prior works that rely on static adversary models or decoupled optimization of trajectory, frequency, and power, we integrated an LLM-driven probabilistic intent prediction module with a DRL framework. This design enables realistic modeling of coordinated adversaries and supports real-time, uncertaintyaware joint optimization in dynamic low-altitude environments.

## III. SYSTEM MODEL

## A. System Overview

As illustrated in Fig. 1, we consider a secure communication scenario within a LAENets, involving a legitimate IAA base station, multiple legitimate ground receivers, multiple eavesdroppers, and an IAA-based jammer. Unlike traditional static models, this system adopts a dynamic game-theoretic framework where both legitimate and adversarial parties adapt their strategies over time. Notably, the legitimate IAA base station employs a LLM to predict per-band jamming/eavesdropping intent distributions q J [ n ] , q E [ n ] and the jammer's next-step position ˆ w J n from sequential wireless observations. This predictive intelligence enables the legitimate IAA to make informed decisions regarding its trajectory, transmit power, and frequency selection. To address privacy concerns, the framework processes wireless observations in an aggregated and anonymized form, focusing on channel characteristics rather than user-specific data, with future extensions planned to incorporate differential privacy mechanisms for enhanced user protection.

The IAA base station is denoted as B , the legitimate receivers as s ∈ S ≜ { 1 , 2 , . . . , S } , the eavesdropper as e ∈ E ≜ { 1 , 2 , . . . , E } , and the jammer as J . All entities operate within a three-dimensional Cartesian coordinate system [92]. The coordinates of the IAA base station at time slot n are represented as ( x B [ n ] , y B [ n ] , H ) , where H is the fixed flight altitude of the IAA base station due to policy constraints [93]. The receivers are deployed on the ground and their coordinates are denoted by ( x S s , y S s , 0) for s ∈ S . The eavesdropper and jammer are positioned at coordinates ( x E e , y E e , 0) for e ∈ E and ( x J , y J , H ) , respectively.

## B. Mobility Model

We consider a flight period of duration T seconds, divided into N equal-length time slots with δ t = T N such that each aerial agent's position is approximately constant within a slot. The trajectory of agent m ∈ { B,J } over T is represented by the N -point sequences w m [ n ] = ( x m [ n ] , y m [ n ] , H ) , n ∈ N ≜ { 1 , . . . , N } .

Let V max denote the maximum speed of agent, then the maximum displacement per slot is L max = V max δ t . Both aerial agents follow a periodic trajectory and return to their initial points by the end of the period. Accordingly, their mobility constraints are

<!-- formula-not-decoded -->

and

<!-- formula-not-decoded -->

To avoid collision between the IAA base station and the jammer, we impose a minimum separation distance:

<!-- formula-not-decoded -->

where d min denotes the required minimum distance.

For receiver S s , the 3D distance to agent m ∈ { B,J } at slot n and the corresponding elevation angle are

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Similarly, for eavesdropper E e ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## C. Cooperated Jamming and Wiretapping Model

In contrast to conventional scenarios where jammers and eavesdroppers operate independently, this paper explicitly assumes a cooperative relationship between the jammer and the eavesdroppers. In particular, the jammer jointly optimizes its trajectory and jamming frequency selection to assist eavesdropping activities, strategically interfering in specific frequency bands to push the legitimate IAA base station towards alternative frequencies monitored by the eavesdroppers. Additionally, by deliberately maintaining a controlled spatial distance from the legitimate IAA, the jammer reduces interference at the eavesdroppers, thereby improving their signal reception quality and maximizing their eavesdropping rates. This coordinated adversarial behavior significantly complicates the legitimate IAA's optimization problem and highlights the importance of predictive intelligence in developing effective defense strategies.

To formalize the cooperative adversarial game structure, we model the jammer and eavesdroppers as players in a cooperative game where they share complete information and jointly optimize a common objective function. Specifically, at each time slot n , the jammer observes the legitimate IAA's transmission strategy and shares this information with the eavesdroppers through a low-latency control channel. The eavesdroppers then communicate their channel state information and monitor capabilities back to the jammer. Based on this shared information, the adversaries collaboratively solve a joint optimization problem to determine the optimal joint strategy.

Fig. 2. Time-frequency grid illustrating cooperative jamming and eavesdropping. The jammer blocks selected channels to influence legitimate transmissions, while eavesdroppers monitor less-interfered channels.

<!-- image -->

To explicitly characterize the cooperative frequency strategies, we define the frequency set F = { f 1 , . . . , f K } and the probability vectors as follows. At each slot n , the IAA base station, the jammer, and the eavesdropper select frequency bands according to

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Here, each element q k B [ n ] ∈ [0, 1] , q k J [ n ] ∈ [0, 1] and q k E [ n ] ∈ [0, 1] indicates the probability that the IAA base station transmits, the jammer interferes, and eavesdroppers monitor frequency band f k at time slot n , respectively.

When the jammer deliberately interferes with frequency f k , its goal is to push the legitimate IAA to switch to other communication bands, thereby reshaping q B [ n ] . Simultaneously, the eavesdroppers adapt q E [ n ] to maximize eavesdropping efficiency, typically favoring bands that are less jammed yet likely used by the IAA. This probabilistic modeling explicitly captures cooperative adversarial strategies and substantially complicates the legitimate IAA's joint resource-allocation and frequencyselection problem.

## D. Signal Model

As illustrated in Fig. 2, the frequency-hopping transmission from the IAA base station to a receiver is performed over one of K non-overlapping (orthogonal) channels F = { f 1 , f 2 , . . . , f K } in slotted time. Upon detecting a change in the jamming pattern, the controller recomputes the resource allocation and decides whether to remain on the current band or switch to another.

Inspired by [17], we consider a probabilistic LoS modelthat accounts for both LoS and non-line-of-sight (NLoS) conditions. The LoS probabilities at slot n are [94]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where a LoS and b LoS are model parameters. The complementary NLoS probabilities are:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The large-scale path loss between receiver S s and the agent m ∈ { B,J } in dB at slot n is given for LoS and NLoS cases by [95]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where n LoS and n NLoS are path loss exponents, X NLoS ∼ N (0 , σ 2 NLoS ) represents a normally distributed random variable modeling shadow fading, and σ NLoS denotes the standard deviation. PL k d 0 is the reference path loss and can be computed by:

<!-- formula-not-decoded -->

with λ k = c/f k the wavelength of band f k , f k the carrier frequency, and c the speed of light.

Let P S s ,B [ n ] denote the transmit power allocated by IAA base stations to receiver S s at slot n , and P S s ,J [ n ] denote the jammer's transmit power at slot n . They satisfy:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

On band f k , the received power at S s from m ∈ { B,J } is

<!-- formula-not-decoded -->

Likewise, for eavesdropper E e , the LoS and NLoS components of eavesdropper E e are obtained from (21) and (22), respectively

<!-- formula-not-decoded -->

and the received power is

<!-- formula-not-decoded -->

## E. Performance Model

We first define the achievable rates conditioned on selecting frequency f k . The achievable rate of legitimate receiver S s on frequency f k in non-jammed and jammed condition can be denoted by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and the achievable rate on frequency f k of eavesdropper E e is given by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then, incorporating frequency-selection probabilities, the expected achievable rates at receiver S s and eavesdropper E e during time slot n can be derived. The achievable rate of the receiver S s in bps/Hz is given by

<!-- formula-not-decoded -->

where q k B [ n ] is the probability that the IAA base station transmits on frequency f k . And the achievable rate of the eavesdropper E e in bps/Hz is given by

<!-- formula-not-decoded -->

where q k E [ n ] represents the eavesdropper's probability of monitoring frequency f k .

Hence, the average secrecy rate for receiver S s in bps/Hz over T time slots can be expressed as

<!-- formula-not-decoded -->

where [ · ] ≜ max( · , 0) .

## IV. PROBLEM FORMULATION

For the IAA base station, the objective is to maximize the minimumaverage secrecy rate among all receivers by jointly designing the trajectory, transmit-power allocation, and frequencyselection policy, subject to mobility and power constraints. The problem is

<!-- formula-not-decoded -->

where 1 N is omitted in (31). In addition, we omit the operation [ · ] + in (31), because if the summation term in time slot n in the objective function is less than 0, we can set P B [ n ] = 0 . We observe that both the numerator and the dominator of the fractions in R S s [ n ] and R E e [ n ] have trajectory and transmit power optimization variables, while optimization variables in [96] or [38] exist only in the numerator or denominator of the fraction in the logarithmic function, which makes our problem (31) more difficult to tackle. Moreover, we consider multiple receivers and multiple eavesdroppers, while [38], [96] only consider one receiver and one eavesdropper, which are essentially special cases of our proposed general optimization framework.

Conversely, the adversarial jammer and the cooperative eavesdroppers seek to maximize their advantage, defined as the difference between the eavesdropping and legitimate rates, by jointly selecting the jammer's trajectory, the jamming-band distribution, and the monitoring-band distributions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where the adversarial side optimization variables include the jammer trajectory w J , interference frequency selection probability vector q J , and eavesdropping frequency selection probability vector q E .

Problem (P2) explicitly highlights the cooperative strategy adopted by the jammer and eavesdroppers to maximize their advantage against the legitimate IAA, thus forming a clear adversarial counterpart to the legitimate optimization problem (P1).

Fig. 3. Lightweight Telco-RAG LLM-assisted prediction framework for cooperative jamming-eavesdropping. Environmental and historical data are encoded via graph-structured topology and physics-aware kinematic/propagation embeddings, while retrieval-augmented, structured prompts about jammer and eavesdropper behaviors are processed by an LLM. The predicted adversarial actions guide the IAA base station's control and communication strategies through an SAC paradigm.

<!-- image -->

## V. PROPOSED ALGORITHM

In this section, we propose a Telco-RAG-assisted large language model (LLM) coupled with a soft actor-critic (SAC) controller for secure communications under coordinated jamming and eavesdropping.

As shown in Fig. 3, a lightweight LLM is integrated into the IAA controller to enable intelligent prediction and realtime adaptation. The wireless environment is abstracted into graph-structured and physics-aware embeddings, and historical observations of the jammer and eavesdroppers are combined with user requirements through retrieval-augmented, structured prompts. Leveraging the LLM's reasoning over temporal sequences, the system produces per-slot predictions of adversarial intent and motion, including the jammer's next-step position ˆ w J n +1 , per-band jamming probabilities ˆ q J [ n ] , and eavesdroppers' monitoring distributions q E [ n ] . These predictions are then used as priors for state augmentation and reward shaping within an SAC framework, which outputs proactive trajectory, power, and frequency decisions for the IAA base station to maximize secrecy performance while countering cooperative adversarial strategies in LAENets.

## A. Cooperative Jamming and Eavesdropping Strategy Optimization

We propose a cooperative jamming-eavesdropping strategy in which the aerial jammer and ground eavesdroppers coordinate their actions in real time. Unlike conventional independent adversaries, the jammer and eavesdroppers dynamically share information to jointly select jamming and monitoring bands and adjust the jammer's trajectory so as to maximize the overall eavesdropping-rate advantage. For instance, the jammer may avoid certain bands to leave clean channels for eavesdroppers, or reposition to create spatial conditions that amplify the eavesdropping rate-posing new challenges for secure communication in LAENets.

To tackle this adversarial optimization, we formulate the cooperative jamming and eavesdropping problem as P2 in (32), where the objective is to maximize the illegal (eavesdropping) rate advantage. The intelligent agents jointly optimize their frequency selection probabilities and the jammer's trajectory, considering both the physical layer and resource constraints. Specifically, we employ an SAC reinforcement learning framework, where the adversarial agents interact with the environment to learn optimal joint strategies under uncertainty. Through continuous interaction and policy updates, the SAC-based method enables the adversaries to adaptively refine their jamming and wiretapping strategies, thus providing a strong baseline for evaluating the robustness and effectiveness of our proposed defense algorithm. The details of the SAC framework will be introduced later.

## B. LLM-Based Intent Prediction and Trajectory Prediction

To proactively defend against jamming and wiretapping, our framework integrates the Telco-RAG [36] for sequential intent prediction and adversarial trajectory prediction. This module is designed to forecast, in each upcoming time slot, the most likely jamming frequencies, wiretapping frequencies, and the jammer's position, based on observed historical data [97]. In our system model, we assume the legitimate IAA base station has knowledge of eavesdropper locations, which is achievable through passive localization techniques such as signal strength analysis and direction-of-arrival estimation that are well-established in wireless security applications [15].

The prediction task can be formulated as follows. At each time slot n , given a sequence of historical observations

<!-- formula-not-decoded -->

serves as the input context for intent prediction. Each X [ t ] encodes the system state at time t , including the jammer's position, and the frequencies occupied for communication, jamming, and wiretapping, respectively. The core prediction task is to infer, for the next time slot, the probability that each available frequency band will be targeted for jamming or eavesdropping, alongside the next position of the jammer.

Formally, the model outputs two probability distributions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where ˆ q k J [ n ] and ˆ q k E [ n ] denotes the predicted probability that the jammer and the eavesdropper select frequency band f k for jamming and wiretapping at time n . In addition, the LLM predicts the expected spatial location ˆ w J [ n ] of the jammer for the next slot. The overall intent prediction process can thus be expressed as

<!-- formula-not-decoded -->

To facilitate effective reasoning by the LLM, the historical state sequence is embedded into a structured prompt that describes the evolution of agent positions and spectral activities. The prompt is constructed as Fig. 3.

This prompt format can be adapted for both few-shot and chain-of-thought (CoT) prompting to further enhance LLM reasoning, following best practices in intent and mobility prediction.

Therefore, at each decision epoch, the LLM-based intent predictor provides the predicted jamming probability vector ˆ q J [ n ] , wiretapping probability vector ˆ q E [ n ] , and the anticipated position ˆ w J [ n ] of the jammer. By leveraging the LLM's sequential modeling and commonsense reasoning capabilities, the model is able to generate not only point estimates but also probability distributions over all possible adversarial actions.

## C. Implementation Details of SAC

The soft actor-critic algorithm [98] is a state-of-the-art deep reinforcement learning framework designed for continuous control tasks, featuring an off-policy, entropy-regularized actorcritic architecture. SAC aims to learn a stochastic policy that maximizes both the expected cumulative reward and the policy entropy, thereby encouraging exploration and robustness in highly dynamic environments. Let π θ ( a | s ) denote the policy network parameterized by θ , and let Q φ ( s, a ) and V ψ denote the soft Q-function and value function parameterized by φ and ψ , respectively. The SAC objective augments the standard expected reward with an entropy term as follows:

<!-- formula-not-decoded -->

where r [ n ] is the reward at time step n , α &gt; 0 is the temperature parameter controlling the trade-off between reward maximization and entropy, and H ( π ( ·| s [ n ])) denotes the entropy of the policy at state s [ n ] .

The soft Q-function is learned by minimizing the Bellman residual:

<!-- formula-not-decoded -->

where Q ¯ φ is the target network and γ ∈ (0 , 1) is the discount factor.

The The value function is updated to minimize

<!-- formula-not-decoded -->

The policy network is trained by maximizing the expected soft Q-value and entropy:

<!-- formula-not-decoded -->

SAC iteratively samples transitions from the replay buffer, updates the networks using stochastic gradient descent, and periodically soft-updates the target Q-network.

## D. SAC-Based Robust Policy Optimization

Building upon the LLM-based intent and adversarial trajectory prediction, we formulate secure trajectory and resource control as sequential decision making. By incorporating TelcoRAG priors, including predicted jamming and eavesdropping band distributions and the anticipated jammer position, the IAA base station proactively adapts its trajectory, power, and band selection to maximize long-term secrecy under dynamic, adversarial conditions.

Toachieve this, we adopt the SAC algorithm, a state-of-the-art deep reinforcement learning framework well-suited for continuous, high-dimensional control tasks. In our design, the SAC agent receives as input not only the real-time system state, but also the LLM-generated adversarial intent predictions, enabling morerobustandanticipatorydecision-making. This problem can be formulated as a Markov decision process (MDP) described by a four-tuple big &lt; S , A , R big &gt; . S , A , and R represent the state space, action space, and reward function.

State: The state at time slot n is denoted as s [ n ] , should comprehensively describe both the system status and the adversarial predictions. Specifically, at each time slot n , the environment state s [ n ] is defined as a joint representation comprising the current position of the legitimate IAA, the last observed or predicted position of the jammer, the fixed locations of legitimate receivers and eavesdroppers, as well as the probabilistic intent predictions ˆ q J [ n ] and ˆ q E [ n ] andtheanticipated jammer position ˆ w J [ n ] . Formally, the state can be written as

<!-- formula-not-decoded -->

where each element provides the agent with comprehensive situational awareness, including both its own previous actions and the anticipated adversarial strategies.

Action: Within this environment, the action a [ n ] at time slot n is composed of the legitimate IAA's control decisions, specifically the next-step trajectory, the transmit power allocation, and the frequency band selection. This is formally denoted as

<!-- formula-not-decoded -->

where w B [ n +1] represents the IAA's next position subject to kinematic constraint, and q B [ n +1] denotes the probability over all available frequency bands.

Reward function: The reward function is designed to directly reflect the secrecy performance of the system in the presence of adversarial interference and wiretapping. At each time step, the immediate reward r [ n ] is defined as the minimum secrecy rate among all legitimate receivers, calculated as the difference between the achievable rates at the legitimate receivers and the maximal eavesdropping rates, both evaluated using the probabilistic outputs from the LLM-based intent prediction. Specifically, the reward is expressed as

<!-- formula-not-decoded -->

In summary, the complete algorithm is detailed in Algorithm 1.

## VI. NUMERICAL RESULTS

In this section, we present comprehensive simulation results to evaluate the effectiveness of the proposed LLM-guided secure trajectory and resource optimization framework. We first introduce the simulation setup, including the network topology, channel parameters, and learning algorithm configurations. Then, we systematically compare our approach with several benchmark schemes under various adversarial scenarios, focusing on average secrecy rate, robustness to coordinated attacks, and convergence behavior. The experiments are conducted on a server equipped with a single NVIDIA RTX 4090 GPU and an Intel Core i7-13900KF processor. The system runs Linux (Debian, kernel 6.1.140) and utilizes PyTorch.

## A. Experiment Settings

We simulate a LAENets using the key parameters listed in Table I. The area is a 100 m × 100 m square; both the jammer andtheIAAbasestationflyatafixedaltitudeof500 m.Thereare 4 legitimate receivers and 4 eavesdroppers, randomly deployed on the ground plane. The initial horizontal positions of the IAA base station and the jammer are also sampled uniformly within the area. Time is slotted, and each UAV obeys a maximumper-slot displacement of 4 m (i.e., L max = 4 m, consistent with L max = V max δ t ). The propagation environment follows the 3GPP TR 38.901 urban model [99].

## B. Performance Analysis of Telco-RAG-Based Intent and Trajectory Prediction

To evaluate the proposed Telco-RAG-based intent recognition and trajectory prediction method, we compare against representative baselines, including a long short-term memory (LSTM) model, a Transformer-style attention model, a CNN, and ChatGPT-3.5. All methods use the same historical trajectory and spectrum-usage inputs with an identical sliding window, sampling interval, and feature normalization; for ChatGPT3.5, the numerical sequences are serialized into structured

## Algorithm 1: LLM-guided SAC for Secure IAA Trajectory and Policy Optimization.

prompts using the same Telco-RAG context. Prediction quality is assessed primarily by mean square error (MSE) on intent probabilities.

Trajectory accuracy is critical for downstream resource allocation and path planning. Fig. 4 illustrates that the CNN model presents larger trajectory prediction errors than LSTM

Fig. 4. Comparison of predicted and true IAA trajectories using different prediction models.

TABLE I EXPERIMENTAL SETTINGS

<!-- image -->

and attention-based models, with the most pronounced discrepancies occurring during abrupt changes in the jammer's direction or velocity. Such errors can cause the IAA to misanticipate high-interference regions, leading to mistimed band selection and suboptimal power/trajectory decisions, thereby degrading secrecy performance.

In contrast, the Telco-RAG approach yields more accurate intent and trajectory forecasts, enabling proactive avoidance of predicted high-risk regions and more precise allocation of power and spectrum in anticipation of likely jamming and eavesdropping activities. This anticipatory capability is particularly beneficial in dynamic adversarial environments, where small prediction errors accumulate and can substantially reduce secrecy rate and robustness.

Table II summarizes the quantitative results. Our method attains the lowest errors for both trajectory prediction (Trajectory MSE: 0.018 ) and intent prediction (Intent MSE: 0.002 ), outperforming conventional deep learning baselines. While ChatGPT3.5 is competitive, our approach achieves lower MSE. The CNN baseline shows the largest errors, suggesting difficulty in capturing the long-range temporal dependencies of jammer behavior.

Overall, these results confirm the advantage of integrating Telco-RAG's structured prompt and retrieval-augmented prediction mechanism for intent inference in wireless adversarial scenarios. Our measurements show that the inference time for the Telco-RAG prediction module is 0.49 s per prediction which is slightly longer than ChatGPT-3.5 (0.36 s) but remains well within the acceptable range for dynamic aerial communication scenarios. The proposed approach offers a favorable balance between prediction accuracy and computational efficiency, making it suitable for real-time secure IAA communication systems.

Fig. 5. Comparison of optimization performance using different optimization methods.

<!-- image -->

## C. Convergence and Performance Evaluation of SAC-Based Optimization

We evaluate the convergence and overall performance of the proposed SAC-based trajectory and resource optimizer against two baselines: simulated annealing (SA) and proximal policy optimization (PPO).

Each network uses two hidden layers with 512 units; the replay mini-batch size is 1024. The discount factor is γ = 0 . 99 ; target networks are softly updated with τ = 0 . 005 . The learning rate is 3 × 10 -4 . The temperature α is adapted via automatic entropy tuning toward a target entropy H ∗ . Unless otherwise stated, we employ Adam and a standard replay buffer. To ensure fairness in comparison, all models were trained under identical computational budgets, with training epochs, batch sizes, and evaluation criteria matched across the DL and RL baselines.

As shown in Fig. 5, SAC exhibits rapid improvement in average reward during early training, followed by stable convergence after approximately 1 . 5 × 10 4 training iterations. PPO also converges but to a consistently lower asymptote under the considered adversarial environment. SA performs worst among the three methods, reflecting the difficulty of exploring and optimizing in a continuous, high-dimensional action space with stringent constraints.

These results highlight SAC's advantage in sample efficiency and robustness, which we attribute to off-policy learning with entropy regularization and to the effective ingestion of LLMderived priors in the state representation.

Fig. 6. Average reward over time slots for different intent prediction and optimization algorithms. The proposed method is compared with Attentionand ChatGPT-based intent models under SAC, PPO, and simulated annealing optimization frameworks.

TABLE II PREDICTION ACCURACY (MSE) AND COMPUTATIONAL TIME COMPARISON AMONG DIFFERENT MODELS

<!-- image -->

## D. Overall Performance Evaluation and Trajectory Visualization

Fig. 6 presents the average reward as a function of time slot under various combinations of intent prediction models and optimization algorithms. It is evident that the proposed method consistently achieves the highest reward across all time slots, significantly outperforming both Attention-based and ChatGPT-based variants regardless of the downstream optimizer (SAC, PPO, or simulated annealing). Specifically, our approach, which integrates Telco-RAG for intent prediction with SAC for resource optimization, demonstrates a substantial advantage in terms of both average reward and reward stability. Methods utilizing SAC generally outperform their PPO and simulated annealing counterparts, highlighting the effectiveness of entropyregularized deep RL in this complex adversarial environment. Furthermore, both Attention- and ChatGPT-based approaches lag behind our method, suggesting the critical importance of precise and context-aware intent prediction for proactive secure communication.

The total decision latency of our framework, including TelcoRAGLLMinference (0.49 s) and SAC forward pass (517.3 ms), is 0.54 s, ensuring real-time operation capability for dynamic threat response in LAENets.

Fig. 7 visualizes the optimized trajectories of both the IAA base station and the jammer in a representative scenario, together with the fixed ground positions of legitimate receivers and eavesdroppers. The IAA base station's trajectory dynamically adapts to both the network layout and the predicted actions of the adversary, strategically maintaining spatial diversity from the jammer while positioning itself to optimize connectivity to the receivers and minimize eavesdropping risk. The jammer, in turn, pursues a correlated yet distinct path aimed at disrupting communication links while facilitating wiretapping. This spatial interplay illustrates the real-time game-theoretic nature of the optimization and confirms the effectiveness of our approach in maintaining physical-layer security under adversarial cooperation.

Fig. 7. Optimized trajectories of the IAA base station and the jammer, along with the positions of legitimate receivers and eavesdroppers, under the proposed method.

<!-- image -->

Fig. 8 presents two side-by-side heatmaps illustrating the predicted probability distributions for jamming and eavesdropping across all 8 frequency channels and 10 time slots. Each cell displays the exact numerical probability, with color intensity providing visual representation. Green check marks indicate correct high-probability predictions, while red crosses denote prediction errors. Our analysis reveals three key insights. First, the model effectively identifies coordinated frequency-hopping tactics where jamming and eavesdropping alternate between adjacent frequency bands, evident in the diagonal patterns across the time-frequency grid. This capability stems from the RAGenhanced architecture, which recognizes subtle correlations in historical adversarial behavior that traditional methods miss. Second, prediction accuracy varies with strategy complexity. The model achieves near-perfect alignment when adversaries follow predictable patterns but shows slight adaptation delays during rapid tactical shifts. This suggests our approach excels at recognizing established patterns but requires several time slots to fully adapt novel attack sequences. Most importantly, these probabilistic predictions enable tiered defense strategies. Channels with moderate probabilities often represent 'decoy' frequencies that adversaries monitor briefly. This allows the IAA to implement nuanced responses, fully avoiding high-probability channels while only reducing power on moderate-probability channels. Unlike binary prediction methods, our approach enables the SAC controller to make continuous, risk-aware adjustments to frequency hopping and power allocation, directly contributing to the 53.84% secrecy rate improvement over traditional methods.

Fig. 8. Predicted probability distributions for jamming and eavesdropping across all channels and time slots. For each time slot, the heatmap displays the predicted probability that each frequency channel will be targeted by the jammer or eavesdropper, with icons marking the actual ground-truth jamming and eavesdropping events.

<!-- image -->

## VII. CONCLUSION

In this paper, we proposed a novel framework for secure low altitude economy networks communications in adversarial environments, where jammers and eavesdroppers cooperate and adapt their strategies over time. Leveraging a lightweight large language model, our approach enables probabilistic intent and trajectory prediction for both jamming and wiretapping agents. These predictions are seamlessly integrated into an SAC reinforcement learning paradigm, allowing the IAA base station to proactively optimize its trajectory, transmission power, and frequency selection in real time. Extensive numerical results demonstrate that the proposed LLM-guided framework not only achieves superior prediction accuracy and secrecy performance compared to conventional deep learning and RL baselines, but also exhibits faster convergence and stronger robustness against coordinated and adaptive attacks. This work highlights the potential of combining advanced intent prediction with reinforcement learning for next-generation secure wireless networks. Future research directions include the extension to multi-IAA scenarios, consideration of imperfect or delayed observations, and the integration of real-world field trials to further validate the practical effectiveness of the proposed approach. Additionally, future research should investigate the integration of localization capabilities for concealed eavesdroppers, dynamic altitude control, the development of specialized lightweight LLM architectures for resource-constrained platforms, and the framework's resilience against attacks targeting the prediction module itself, to further enhance the practical deployment potential of this approach in real-world LAENets.

## REFERENCES

- [1] Y. Jiang et al., '6G non-terrestrial networks enabled low-altitude economy: Opportunities and challenges,' 2023, arXiv:2311.09047 .
- [2] C. Zhao et al., 'Temporal spectrum cartography in low-altitude economy networks: A generative AI framework with multi-agent learning,' 2025, arXiv:2505.15571 .
- [3] Y. Xiao et al., 'Space-air-ground integrated wireless networks for 6G: Basics, key technologies and future trends,' IEEEJ. Sel. Areas Commun. , vol. 42, no. 12, pp. 3327-3354, Dec. 2024.
- [4] W.Yuanetal.,'Fromgroundtosky:Architectures,applications,andchallenges shaping low-altitude wireless networks,' 2025, arXiv:2506.12308 .
- [5] S. Asadzadeh, W. J. de Oliveira, and C. R. de Souza Filho, 'UAV-based remote sensing for the petroleum industry and environmental monitoring: State-of-the-art and perspectives,' J. Petroleum Sci. Eng. , vol. 208, 2022, Art. no. 109633.
- [6] A. Fascista, 'Toward integrated large-scale environmental monitoring usingWSN/UAV/crowdsensing:Areviewofapplications,signalprocessing, and future perspectives,' Sensors , vol. 22, no. 5, 2022, Art. no. 1824.
- [7] DJI, 'Revolutionizing agave farming: Using agras T40 drones to spray agave,' 2024. [Online]. Available: https://ag.dji.com/case-studies/agrast40-t50-agave
- [8] DJI, 'DJI agriculture, a global leader in facilitating agricultural innovation through drone technology, unveils its agriculture drone industry insight report (2023/2024),' 2024. [Online]. Available: https://ag.dji. com/newsroom/ag-news-en-white-paper-2023
- [9] D. C. Tsouros, S. Bibi, and P. G. Sarigiannidis, 'A review on UA V-based applications for precision agriculture,' Information , vol. 10, no. 11, 2019, Art. no. 349.
- [10] DJI, 'Powerline inspection - electricity - inspection,' 2024. [Online]. Available: https://enterprise.dji.com/inspection/powerline-inspection
- [11] M. C. Lucic, O. Bouhamed, H. Ghazzai, A. Khanfor, and Y. Massoud, 'Leveraging UAVs to enable dynamic and smart aerial infrastructure for its and smart cities: An overview,' Drones , vol. 7, no. 2, 2023, Art. no. 79.

- [12] R. H. Jacobsen et al., 'Design of an autonomous cooperative drone swarm for inspections of safety critical infrastructure,' Appl. Sci. , vol. 13, no. 3, 2023, Art. no. 1256.
- [13] S.-Y. Chang, K. Park, J. Kim, and J. Kim, 'Securing UAV flying base station for mobile networking: A review,' Future Internet , vol. 15, no. 5, 2023, Art. no. 176.
- [14] B. Dai, J. Niu, T. Ren, Z. Hu, and M. Atiquzzaman, 'Towards energyefficient scheduling of UA V and base station hybrid enabled mobile edge computing,' IEEE Trans. Veh. Technol. , vol. 71, no. 1, pp. 915-930, Jan. 2022.
- [15] J. Tang, G. Chen, and J. P. Coon, 'Secrecy performance analysis of wireless communications in the presence of UAV jammer and randomly located UAV eavesdroppers,' IEEE Trans. Inf. Forensics Secur. , vol. 14, no. 11, pp. 3026-3041, Nov. 2019.
- [16] Y. Zhou et al., 'Improving physical layer security via a UAV friendly jammer for unknown eavesdropper location,' IEEE Trans. Veh. Technol. , vol. 67, no. 11, pp. 11280-11284, Nov. 2018.
- [17] Y. Li, R. Zhang, J. Zhang, S. Gao, and L. Yang, 'Cooperative jamming for secure UAV communications with partial eavesdropper information,' IEEE Access , vol. 7, pp. 94593-94603, 2019.
- [18] A. Raja, L. Njilla, and J. Yuan, 'Adversarial attacks and defenses toward AI-assisted UAV infrastructure inspection,' IEEE Internet Things J. , vol. 9, no. 23, pp. 23379-23389, Dec. 2022.
- [19] V. Hassija et al., 'Fast, reliable, and secure drone communication: A comprehensive survey,' IEEE Commun. Surv. Tut. , vol. 23, no. 4, pp. 2802-2832, 4th Quart. 2021.
- [20] M. Z. Hassan, G. Kaddoum, and O. Akhrif, 'Resource allocation for joint interference management and security enhancement in cellularconnected Internet-of-Drones networks,' IEEE Trans. Veh. Technol. , vol. 71, no. 12, pp. 12869-12884, Dec. 2022.
- [21] G. Li, W. Li, and Y. Peng, 'Exploring the new blue ocean of low-altitude economy:Anempiricalanalysisofindustrialstatus quo and technological innovation references,' J. Social Sci. Humanities Literature , vol. 8, no. 5, pp. 28-38, 2025.
- [22] Y. Zeng and R. Zhang, 'Energy-efficient UAV communication with trajectory optimization,' IEEE Trans. Wireless Commun. , vol. 16, no. 6, pp. 3747-3760, Jun. 2017.
- [23] H. Lei et al., 'Safeguarding UAV IoT communication systems against randomly located eavesdroppers,' IEEE Internet Things J. , vol. 7, no. 2, pp. 1230-1244, Feb. 2020.
- [24] P. Cao et al., 'Computational intelligence algorithms for UAV swarm networking and collaboration: A comprehensive survey and future directions,' IEEE Commun. Surv. Tut. , vol. 26, no. 4, pp. 2684-2728, 4th Quart. 2024.
- [25] Y. Zhang, R. Zhao, D. Mishra, and D. W. K. Ng, 'A comprehensive review of energy-efficient techniques for UA V-assisted industrial wireless networks,' Energies , vol. 17, no. 18, 2024, Art. no. 4737.
- [26] L. Bariah, Q. Zhao, H. Zou, Y. Tian, F. Bader, and M. Debbah, 'Large generative AI models for telecom: The next big thing?,' IEEE Commun. Mag. , vol. 62, no. 11, pp. 84-90, Nov. 2024.
- [27] S. Feuerriegel, J. Hartmann, C. Janiesch, and P. Zschech, 'Generative AI,' Bus. Inf. Syst. Eng. , vol. 66, no. 1, pp. 111-126, 2024.
- [28] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, 'High-resolution image synthesis with latent diffusion models,' in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. , 2022, pp. 10684-10695.
- [29] A. Vaswani et al., 'Attention is all you need,' in Proc. Adv. Neural Inf. Process. Syst. , 2017, vol. 30, pp. 6000-6010.
- [30] Y. Wang, Z. Gao, D. Zheng, S. Chen, D. Gündüz, and H. V. Poor, 'Transformer-empowered 6G intelligent networks: From massive MIMO processing to semantic communication,' IEEE Wireless Commun. , vol. 30, no. 6, pp. 127-135, Dec. 2023.
- [31] L. Jiao et al., 'Advanced deep learning models for 6G: Overview, opportunities, and challenges,' IEEE Access , vol. 12, pp. 133245-133314, 2024.
- [32] J. Du, T. Lin, C. Jiang, Q. Yang, C. F. Bader, and Z. Han, 'Distributed foundation models for multi-modal learning in 6G wireless networks,' IEEE Wireless Commun. , vol. 31, no. 3, pp. 20-30, Jun. 2024.
- [33] H. Wu, X. Chen, and K. Huang, 'Device-edge cooperative fine-tuning of foundation models as a 6G service,' IEEE Wireless Commun. , vol. 31, no. 3, pp. 60-67, Jun. 2024.
- [34] M. Jin et al., 'Time-LLM: Time series forecasting by reprogramming large language models,' 2023, arXiv:2310.01728 .
- [35] F. Jia, K. Wang, Y . Zheng, D. Cao, and Y . Liu, 'GPT4MTS: Prompt-based large language model for multimodal time-series forecasting,' in Proc. AAAI Conf. Artif. Intell. , 2024, vol. 38, no. 21, pp. 23343-23351.
- [36] A.-L. Bornea, F. Ayed, A. De Domenico, N. Piovesan, and A. Maatouk, 'Telco-rag: Navigating the challenges of retrieval augmented language modelsfor telecommunications,' in Proc. GLOBECOM2024-2024IEEE Glob. Commun. Conf ., 2024, pp. 2359-2364.
- [37] Y. Xiao, Q. Du, and G. K. Karagiannidis, 'Statistical age of information: A risk-aware metric and its applications in status updates,' IEEE Trans. Wireless Commun. , vol. 24, no. 3, pp. 2325-2340, Mar. 2025.
- [38] A. Li, Q. Wu, and R. Zhang, 'UAV-enabled cooperative jamming for improving secrecy of ground wiretap channel,' IEEE Wireless Commun. Lett. , vol. 8, no. 1, pp. 181-184, Feb. 2019.
- [39] C. Zhong, J. Yao, and J. Xu, 'Secure UAV communication with cooperative jamming and trajectory control,' IEEE Commun. Lett. , vol. 23, no. 2, pp. 286-289, Feb. 2019.
- [40] X. Lu, L. Xiao, C. Dai, and H. Dai, 'UAV-aided cellular communications with deep reinforcement learning against jamming,' IEEE Wireless Commun. , vol. 27, no. 4, pp. 48-53, Aug. 2020.
- [41] H. Wang, G. Ding, J. Chen, Y. Zou, and F. Gao, 'UAV anti-jamming communications with power and mobility control,' IEEE Trans. Wireless Commun. , vol. 22, no. 7, pp. 4729-4744, Jul. 2023.
- [42] X. Sun, D. W. K. Ng, Z. Ding, Y. Xu, and Z. Zhong, 'Physical layer security in UAV systems: Challenges and opportunities,' IEEE Wireless Commun. , vol. 26, no. 5, pp. 40-47, Oct. 2019.
- [43] H. Lu, H. Zhang, H. Dai, W. Wu, and B. Wang, 'Proactive eavesdropping in UAV-aided suspicious communication systems,' IEEE Trans. Veh. Technol. , vol. 68, no. 2, pp. 1993-1997, Feb. 2019.
- [44] T. M. Hoang, N. M. Nguyen, and T. Q. Duong, 'Detection of eavesdropping attack in UAV-aided wireless systems: Unsupervised learning with one-class SVM and K-means clustering,' IEEE Wireless Commun. Lett. , vol. 9, no. 2, pp. 139-142, Feb. 2020.
- [45] S. Jia et al., 'Secrecy performance analysis of UAV-assisted ambient backscatter communications with jamming,' IEEE Trans. Wireless Commun. , vol. 23, no. 12, pp. 18111-18125, Dec. 2024.
- [46] J. Wang, F. Fang, G. Han, N. Wang, and X. Wang, 'Joint secrecy rate achieving and authentication enhancement via tag-based encoding in chaotic UAV communication environment,' IEEE Internet Things J. , vol. 12, no. 8, pp. 9491-9507, Apr. 2025.
- [47] H. Yang, K. Lin, C. Wang, W. Xia, and C. Wang, 'Cooperative jamming and trajectory optimization for uav-enabled reliable and secure communications,' in Proc. IEEE 100th Veh. Technol. Conf. , 2024, pp. 1-5.
- [48] Z. Xing, Y. Qin, C. Du, W. Wang, and Z. Zhang, 'Deep reinforcement learning-driven jamming-enhanced secure unmanned aerial vehicle communications,' Sensors , vol. 24, no. 22, Art. no. 7328, 2024.
- [49] S. Wang, Y. Zhang, M. Chen, W. Zhang, and Z. He, 'Multi-agent global prioritized experience learning for UA V cooperative jamming in secure communication,' IEEE Trans. Signal Inf. Process. Netw. , vol. 11, pp. 916-927, 2025.
- [50] S. Cheepurupalli, D. K. Egu, P. K. Upadhyay, A. M. Salhab, J. M. Moualeu, and P. H. Nardelli, 'Deep learning-enabled secrecy performance analysis of UAV-aided reconfigurable intelligent surfaces with non-orthogonal multiple access,' IEEE Trans. Cogn. Commun. Netw. , vol. 11, no. 6, pp. 3797-3810, Dec. 2025.
- [51] M. T. Mamaghani and Y. Hong, 'Joint trajectory and power allocation design for secure artificial noise aided UAV communications,' IEEE Trans. Veh. Technol. , vol. 70, no. 3, pp. 2850-2855, Mar. 2021.
- [52] Y. Wen, G. Chen, S. Fang, M. Wen, S. Tomasin, and M. D. Renzo, 'RIS-assisted UAV secure communications with artificial noise-aware trajectory design against multiple colluding curious users,' IEEE Trans. Inf. Forensics Secur. , vol. 19, pp. 3064-3076, 2024.
- [53] H. Lee, S. Eom, J. Park, and I. Lee, 'UA V-aided secure communications with cooperative jamming,' IEEE Trans. Veh. Technol. , vol. 67, no. 10, pp. 9385-9392, Oct. 2018.
- [54] Y. Gao, Y. Xiao, M. Wu, M. Xiao, and J. Shao, 'Game theory-based anti-jamming strategies for frequency hopping wireless communications,' IEEE Trans. Wireless Commun. , vol. 17, no. 8, pp. 5314-5326, Aug. 2018.
- [55] C. Shen, T.-H. Chang, J. Gong, Y. Zeng, and R. Zhang, 'Multi-UAV interference coordination via joint trajectory and power control,' IEEE Trans. Signal Process. , vol. 68, pp. 843-858, 2020.
- [56] W.Mei, Q. Wu, and R. Zhang, 'Cellular-connected UAV: Uplink association, power control and interference coordination,' IEEE Trans. Wireless Commun. , vol. 18, no. 11, pp. 5380-5393, Nov. 2019.

- [57] S. Hosseinalipour, A. Rahmati, and H. Dai, 'Interference avoidance position planning in UAV-assisted wireless communication,' in Proc. - IEEE Int. Conf. Commun ., 2019, pp. 1-6.
- [58] Z. Zhao, Q. Du, and G. K. Karagiannidis, 'Improved grant-free access for URLLC via multi-tier-driven computing: Network-load learning, prediction, and resource allocation,' IEEEJ.Sel. Areas Commun. , vol. 41, no. 3, pp. 607-622, Mar. 2023.
- [59] Y. Liu et al., 'Secure rate maximization for ISAC-UAV assisted communication amidst multiple eavesdroppers,' IEEE Trans. Veh. Technol. , vol. 73, no. 10, pp. 15843-15847, Oct. 2024.
- [60] Y. Bian et al., 'Joint trajectory control, power control and collection schedule in UAV-assisted anti-jamming wireless data collection with imperfect CSI,' IEEE Commun. Lett. , vol. 28, no. 12, pp. 2839-2843, Dec. 2024.
- [61] M.D.Nguyen, W. Ajib, W.-P. Zhu, and G. K. Kurt, 'Integrated user association, computation offloading, resource allocation, and UA V trajectory control against jamming for UAV-based wireless networks,' IEEE Trans. Wireless Commun. , vol. 24, no. 7, pp. 5588-5604, Jul. 2025.
- [62] R. Gao, G. Yan, R. Niu, W. Chang, T. Yan, and C. Tang, 'A novel spectrum sensing method for multiple unknown signal sources using frequency domain energy detection and DBSCAN,' IEEEAccess , vol. 13, pp. 76811-76837, 2025.
- [63] P. Behmandpoor, M. Moonen, and P. Patrinos, 'Asynchronous messagepassing and zeroth-order optimization based distributed learning with a use-case in resource allocation in communication networks,' IEEETrans. Signal Inf. Process. Netw. , vol. 10, pp. 916-931, 2024.
- [64] K. M. Thilina, K. W. Choi, N. Saquib, and E. Hossain, 'Machine learning techniques for cooperative spectrum sensing in cognitive radio networks,' IEEE J. Sel. Areas Commun. , vol. 31, no. 11, pp. 2209-2221, Nov. 2013.
- [65] F. Azmat, Y. Chen, and N. Stocks, 'Analysis of spectrum occupancy using machine learning algorithms,' IEEE Trans. Veh. Technol. , vol. 65, no. 9, pp. 6853-6860, Sep. 2016.
- [66] P. Venkatraman, B. Hamdaoui, and M. Guizani, 'Opportunistic bandwidth sharing through reinforcement learning,' IEEE Trans. Veh. Technol. , vol. 59, no. 6, pp. 3148-3153, Jul. 2010.
- [67] L. Melián-Gutierrez, N. Modi, C. Moy, F. Bader, I. Perez-Álvarez, and S. Zazo, 'Hybrid UCB-HMM: A machine learning strategy for cognitive radio in HF band,' IEEE Trans. Cogn. Commun. Netw. , vol. 1, no. 3, pp. 347-358, Sep. 2015.
- [68] O. Puñal, I. Akta¸ s, C.-J. Schnelke, G. Abidin, K. Wehrle, and J. Gross, 'Machine learning-based jamming detection for IEEE 802.11: Design and experimental evaluation,' in Proc. IEEE Int. Symp. World Wireless, Mobile Multimedia Netw. , 2014, pp. 1-10.
- [69] S. K. Khan, N. Shiwakoti, P. Stasinopoulos, and Y. Chen, 'Cyber-attacks in the next-generation cars, mitigation techniques, anticipated readiness and future directions,' Accident Anal. Prevention , vol. 148, 2020, Art. no. 105837.
- [70] Y. Arjoune, F. Salahdine, M. S. Islam, E. Ghribi, and N. Kaabouch, 'A novel jamming attacks detection approach based on machine learning for wireless communication,' in Proc. Int. Conf. Inf. Netw. , 2020, pp. 459-464.
- [71] D. Karagiannis and A. Argyriou, 'Jamming attack detection in a pair of RF communicating vehicles using unsupervised machine learning,' Veh. Commun. , vol. 13, pp. 56-63, 2018.
- [72] C. Gilbert and M. A. Gilbert, 'Continuous user authentication on mobile devices,' Int. Res. J. Adv. Eng. Sci. , vol. 10, no. 1, pp. 158-173, 2025.
- [73] U. Mahbub and R. Chellappa, 'Path: Person authentication using trace histories,' in Proc. IEEE 7th Annu. Ubiquitous Comput., Electron. Mobile Commun. Conf. , 2016, pp. 1-8.
- [74] H. Song, L. Liu, J. Ashdown, and Y. Yi, 'A deep reinforcement learning frameworkforspectrummanagementindynamicspectrumaccess,' IEEE Internet Things J. , vol. 8, no. 14, pp. 11208-11218, Jul. 2021.
- [75] Y. Gao, Z. Ye, and H. Yu, 'Cost-efficient computation offloading in SAGIN: A deep reinforcement learning and perception-aided approach,' IEEE J. Sel. Areas Commun. , vol. 42, no. 12, pp. 3462-3476, Dec. 2024.
- [76] C. Zhang et al., 'Multi-objective aerial collaborative secure communication optimization via generative diffusion model-enabled deep reinforcement learning,' IEEE Trans. Mobile Comput. , vol. 24, no. 4, pp. 3041-3058, Apr. 2025.
- [77] Y. Zhang, D. Monder, and J. F. Forbes, 'Real-time optimization under parametric uncertainty: A probability constrained approach,' J. Process Control , vol. 12, no. 3, pp. 373-389, 2002.
- [78] X. Liu, Y. Xu, L. Jia, Q. Wu, and A. Anpalagan, 'Anti-jamming communications using spectrum waterfall: A deep reinforcement learning approach,' IEEECommun.Lett. , vol. 22, no. 5, pp. 998-1001, May 2018.
- [79] F. Li, B. Shen, J. Guo, K.-Y . Lam, G. Wei, and L. Wang, 'Dynamic spectrumaccess for Internet-of-Things based on federated deep reinforcement learning,' IEEE Trans. Veh. Technol. , vol. 71, no. 7, pp. 7952-7956, Jul. 2022.
- [80] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and A. Nallanathan, 'Deep reinforcement learning based dynamic trajectory control for UA Vassisted mobile edge computing,' IEEE Trans. Mobile Comput. , vol. 21, no. 10, pp. 3536-3550, Oct. 2022.
- [81] J. Wu, X. Fang, D. Niyato, J. Wang, and J. Wang, 'DRL optimization trajectory generation via wireless network intent-guided diffusion models for resource allocation,' IEEE Internet Things J. vol. 12, no. 19, pp. 40115-40129, Oct. 2025.
- [82] X. Zheng et al., 'UAV swarm-enabled collaborative post-disaster communications in low altitude economy via a two-stage optimization approach,' IEEE Trans. Mobile Comput. , vol. 24, no. 11, pp. 11833-11851, Nov. 2025.
- [83] H. Pan, Y. Liu, G. Sun, J. Fan, S. Liang, and C. Yuen, 'Joint power and 3D trajectory optimization for UAV-enabled wireless powered communication networks with obstacles,' IEEE Trans. Commun. , vol. 71, no. 4, pp. 2364-2380, Apr. 2023.
- [84] J. Huang et al., 'Low-altitude friendly-jamming for satellite-maritime communicationsviagenerativeAI-enableddeepreinforcementlearning,' 2025, arXiv:2501.15468 .
- [85] J. Wang et al., 'Generative AI based secure wireless sensing for ISAC networks,' IEEE Trans. Inf. Forensics Secur. , vol. 20, pp. 5195-5210, 2025.
- [86] Z. Sun, H. Liu, X. Qu, K. Feng, Y. Wang, and Y. S. Ong, 'Large language models for intent-driven session recommendations,' in Proc. 47th Int. ACM SIGIR Conf. Res. Develop. Inf. Retrieval , 2024, pp. 324-334.
- [87] Y. Liang and P. Zheng, 'Human-intention prediction with visual-language model,' in Proc. Int. Conf. Automat. Manuf., Transp. Logistics, 2024, pp. 1-4.
- [88] J. A. Rodriguez, N. Botzer, D. Vazquez, C. Pal, M. Pedersoli, and I. Laradji, 'IntentGPT: Few-shot intent discovery with large language models,' 2024, arXiv:2411.10670 .
- [89] G.Sunetal., 'Generative AI for advanced UAV networking,' IEEENetw. , vol. 39, no. 4, pp. 244-253, Jul. 2025.
- [90] K. Takeyama, Y. Liu, and M. Sra, 'TR-LLM: Integrating trajectory data for scene-aware LLM-based human action prediction,' 2024, arXiv:2410.03993 .
- [91] J. Chai, S. Li, Y. Fu, D. Zhao, and Y. Zhu, 'Empowering LLM agents with zero-shot optimal decision-making through Q-learning,' in Proc. 13th Int. Conf. Learn. Representations , 2024.
- [92] E. S. Grood, and W. J. Suntay, 'A joint coordinate system for the clinical description of three-dimensional motions: Application to the knee,' J. Biomech. Eng. , vol. 105, no. 2, pp. 136-144, 1983.
- [93] T. Wang, W. Du, C. Jiang, Y. Li, and H. Zhang, 'Safety constrained trajectory optimization for completion time minimization for UA V communications,' IEEE Internet Things J. , vol. 11, no. 21, pp. 34482-34491, Nov. 2024.
- [94] S. Sun, T. A. Thomas, T. S. Rappaport, H. Nguyen, I. Z. Kovacs, and I. Rodriguez, 'Path loss, shadow fading, and line-of-sight probability models for 5G urban macro-cellular scenarios,' in Proc. 2015 IEEE Globecom Workshops , 2015, pp. 1-7.
- [95] Q. Zhu, C.-X. Wang, B. Hua, K. Mao, S. Jiang, and M. Yao, '3GPP Tr 38.901 Channel Model,' in Wiley 5G Ref: The Essential 5G Reference Online . Hoboken, NJ, USA: Wiley Press, 2021, pp. 1-35.
- [96] G.Zhang,Q.Wu,M.Cui,andR.Zhang,'SecuringUAVcommunications via trajectory optimization,' in Proc. GLOBECOM 2017-2017 IEEE Glob. Commun. Conf ., 2017, pp. 1-6.
- [97] Z. Lan et al., 'TRAJ-LLM: A new exploration for empowering trajectory prediction with pre-trained large language models,' 2024, arXiv:2405.04909 .
- [98] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, 'Soft actorcritic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor,' in Proc. Int. Conf. Mach. Learn. , 2018, pp. 1861-1870.
- [99] N. Docomo et al., '5G channel model for bands up to 100 GHz,' Tech. Rep. 5GCM, Sep. 2016.
- [100] DJI, 'DJI matrice 400,' 2025. [Online]. Available: https://enterprise.dji. com/matrice-400/specs
- [101] Y. Jiang et al., 'Integrated sensing and communication for low altitude economy: Opportunities and challenges,' IEEE Commun. Mag. , vol. 63, no. 12, pp. 72-78, Dec. 2025.

- [102] M. Alzenad, A. El-Keyi, and H. Yanikomeroglu, '3-D placement of an unmanned aerial vehicle base station for maximum coverage of users with different QoS requirements,' IEEE Wireless Commun. Lett. , vol. 7, no. 1, pp. 38-41, Feb. 2018.

<!-- image -->

Ziqiang Ye received the B.S. degree in network engineering from Southwest Jiaotong University, Chengdu, China, in 2022, and the master's degree in cybersecurity with the University of Electronic Science and Technology of China (UESTC), Chengdu, where he is currently working toward the Ph.D. degree in communication and information systems. His research interests include machine learning, large AI models, and generative AI.

<!-- image -->

Yulan Gao (Member, IEEE) received the Ph.D. degree in communication and information systems from the National Key Laboratory of Wireless Communications, University of Electronic Science and Technology of China, Chengdu, China, in 2021. From 2022 to 2024, she was a Research Fellow with the School of Computer Science and Engineering, Nanyang Technological University, Singapore. She is currently a Postdoctoral Researcher with the Division of Information Science and Engineering, KTH Royal Institute of Technology, Stockholm, Sweden.

Her research focuses on optimization and AI in B5G/6G networks.

<!-- image -->

Yue Xiao (Member, IEEE) received the Ph.D. degree in communication and information systems from the University of Electronic Science and Technology of China (UESTC), Chengdu, China, in 2007. He is currently a Professor with the National Key Laboratory of Wireless Communications, UESTC. He has led more than 30 research projects in the field of 3G/4G/5G/6G wireless communication systems. He holds more than 50 patents related to wireless system design and has authored more than 200 papers in international journals and conferences. His research

interests include system design and signal processing for future wireless communication systems. He is a Senior Associate Editor for IEEE COMMUNICATIONS LETTERS, Area Editor of IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY, and Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS.

<!-- image -->

Xianfu Lei (Member, IEEE) received the Ph.D. degree from Southwest Jiaotong University, Chengdu, China, in 2012. From 2012 to 2014, he was a Research Fellow with the Department of Electrical and Computer Engineering, Utah State University. He has been an Associate Professor with the School of Information Science and Technology, Southwest Jiaotong University, since 2015. His research interests include 5G/6G networks, cooperative and energy harvesting networks, and physical-layer security. He has been the Area Editor of IEEE COMMUNICATIONS LETTERS

and Associate Editor for IEEE WIRELESS COMMUNICATIONS LETTERS and IEEE TRANSACTIONS ON COMMUNICATIONS. He was a Senior/Associate Editor for IEEE COMMUNICATIONS LETTERSfrom2014to2019.Hewastherecipientofthe Best Paper Award in IEEE/CIC ICCC 2020, Best Paper Award in WCSP 2018, WCSP 10-Year Anniversary Excellent Paper Award, IEEE Communications Letters Exemplary Editor 2019, and Natural Science Award of China Institute of Communications in 2019.

<!-- image -->

Pingzhi Fan (Life Fellow, IEEE) received the M.Sc. degree in computer science from Southwest Jiaotong University, Chengdu, China, in 1987, and the Ph.D. degree in electronic engineering from Hull University, Hull, U.K., in 1994. He is currently a Presidential Professor with Southwest Jiaotong University (SWJTU),HonoraryDeanoftheSWJTU-LeedsJoint School, and has been a Visiting Professor with Leeds University, U.K., since 1997. His research interests include high mobility wireless communications, massive randomaccess techniques, signal design and cod-

ing. He is an IEEE VTS Distinguished Speaker (2019-2025) and a Fellow of IET, CIE, and CIC. He was an EXCOM Member for the IEEE Region 10, IET (IEE) Council, and the IET Asia-Pacific Region. He was the recipient of U.K. ORS Award in 1992, National Science Fund for Distinguished Young Scholars (1998, NSFC), IEEE VT Society Jack Neubauer Memorial Award in 2018, IEEE SP Society SPL Best Paper Award in 2018, IEEE/CIC ICCC 2020 Best Paper Award, IEEE WCSP 2022 Best Paper Award, and IEEE ICC 2023 Best Paper Award. He was the Chief Scientist for the National 973 Plan Project (National Basic Research Program of China) between 2012 and 2016.

<!-- image -->

George K. Karagiannidis (Fellow, IEEE) is currently Professor with Electrical and Computer Engineering Department, Aristotle University of Thessaloniki, Thessaloniki, Greece, and Head of Wireless Communications &amp; Information Processing Group. His research interests include in the areas of wireless communications systems and networks, signal processing, optical wireless communications, wireless power transfer and applications and communications &amp; signal processing for biomedical engineering. Dr. Karagiannidis is the Editor-in Chief of IEEE TRANS-

ACTIONS ON COMMUNICATIONS and was the Editor-in Chief of IEEE COMMUNICATIONS LETTERS. He was the recipient of three prestigious awards: The 2021 IEEE ComSoc RCC Technical Recognition Award, 2018 IEEE ComSoc SPCE Technical Recognition Award, and the 2022 Humboldt Research Award from Alexander von Humboldt Foundation. He is one of the highly-cited authors across all areas of electrical engineering, recognized from Clarivate Analytics as Web-of-Science Highly-Cited Researcher in the ten consecutive years from 2015 to 2024.
