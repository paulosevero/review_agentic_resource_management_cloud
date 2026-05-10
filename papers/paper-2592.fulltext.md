---
title: "Foundation Model Enhanced Joint Multi-Hop Task Offloading in Dynamic R2X/V2X-based Edge Computing Networks"
authors:
  - "Mingqi Han"
  - "Xinghua Sun"
  - "Xijun Wang"
  - "Wen Zhan"
  - "Xiang Chen"
  - "Tony Q. S. Quek"
affiliations:
  - "School of Electronics and Communication Engineering, Sun Yat-sen University, China"
  - "School of Electronics and Information Technology, Sun Yat-sen University, China"
  - "Information System Technology and Design Pillar, Singapore University of Technology and Design, Singapore"
keywords:
  - "Vehicle Edge Computing"
  - "Multi-hop Transmission"
  - "Joint Task Offloading"
  - "Intelligent Transportation Systems"
  - "Reinforcement Learning"
  - "Foundation Model"
date: 2024
abstract: "Recent popularization of the Internet of Vehicles (IoVs) and vehicles-to-everything (V2X) enables the emergence of real-time vehicular applications, posing challenges to resource-limited vehicles. Toward this end, vehicle edge computing (VEC) has been proposed to alleviate the computational burden on vehicles by leveraging resources from roadside units (RSUs) and VEC servers. While existing works mainly focus on the task requirement for either vehicles or RSUs, the joint task offloading for both V2X and RSUs-to-everything (R2X) has not been fully studied. In this paper, we aim at optimizing the task offloading strategies for both vehicles and RSUs, and adopt a multi-hop task offloading manner to fully utilize the VEC network resources. This problem introduces a severe state-action space shift issue with varying dimensions and representation, which poses challenges for conventional DRL approaches. To address it, we propose a Bidirectional Encoder Representations from Transformers (Bert)-based matching Q-network (BMQN) algorithm. First, we design the BMQN model to efficiently capture correlations among all vehicles and RSUs through bidirectional attention. Then, we propose type-embedded grouped attention and available action embedding to mitigate the overfitting sequence length issue, thereby enhancing generalization capacity. Moreover, we propose to address the state-action space shift issue through a matching-based manner, which can significantly enhance the task offloading ability by matching the states among devices. Simulation results demonstrate that: 1) the BMQN can achieve much better performance than other approaches in scenarios comprising various numbers of vehicles and RSUs as well as diverse road lengths; 2) the BMQN has sufficient generalization capacity to adapt to inexperienced scenarios through matching-based architecture and available action embedding."
---

## Foundation Model Enhanced Joint Multi-Hop Task Offloading in Dynamic R2X/V2X-based Edge Computing Networks

Mingqi Han, Xinghua Sun, Member , IEEE , Xijun Wang, Member , IEEE , Wen Zhan, Member , IEEE , Xiang Chen, Member , IEEE , and Tony Q. S. Quek, Fellow , IEEE

Abstract -Recent popularization of the Internet of Vehicles (IoVs) and vehicles-to-everything (V2X) enables the emergence of real-time vehicular applications, posing challenges to resourcelimited vehicles. Toward this end, vehicle edge computing (VEC) has been proposed to alleviate the computational burden on vehicles by leveraging resources from roadside units (RSUs) and VEC servers. While existing works mainly focus on the task requirement for either vehicles or RSUs, the joint task offloading for both V2X and RSUs-to-everything (R2X) has not been fully studied. In this paper, we aim at optimizing the task offloading strategies for both vehicles and RSUs, and adopt a multi-hop task offloading manner to fully utilize the VEC network resources. This problem introduces a severe state-action space shift issue with varying dimensions and representation, which poses challenges for conventional DRL approaches. To address it, we propose a Bidirectional Encoder Representations from Transformers (Bert)-based matching Q-network (BMQN) algorithm. First, we design the BMQN model to efficiently capture correlations among all vehicles and RSUs through bidirectional attention. Then, we propose type-embedded grouped attention and available action embedding to mitigate the overfitting sequence length issue, thereby enhancing generalization capacity. Moreover, we propose to address the state-action space shift issue through a matching-based manner, which can significantly enhance the task offloading ability by matching the states among devices. Simulation results demonstrate that: 1) the BMQN can achieve much better performance than other approaches in scenarios comprising various numbers of vehicles and RSUs as well as diverse road lengths; 2) the BMQN has sufficient generalization capacity to adapt to inexperienced scenarios through matching-based architecture and available action embedding.

Index Terms -Vehicle Edge Computing, Multi-hop Transmission, Joint Task Offloading, Intelligent Transportation Systems, Reinforcement Learning, Foundation Model

## I. INTRODUCTION

O WING to growing popularization of intelligent vehicles, the Internet of Vehicles (IoVs) and vehicles-toeverything (V2X) have emerged to support communication

M. Han, X. Sun and W. Zhan are with the School of Electronics and Communication Engineering, Sun Yat-Sen University, China (Email:hanmq@mail2.sysu.edu.cn, sunxinghua@mail.sysu.edu.cn, zhanw6 @mail.sysu.edu.cn).

X. Wang and X. Chen are with the School of Electronics and Information Technology, Sun Yat-Sen University, China (Email: wangxijun@mail.sysu.edu.cn, chenxiang@mail.sysu.edu.cn)

Tony Q. S. Quek is with Information System Technology and Design Pillar, Singapore University of Technology and Design, Singapore 487372 (e-mail: tonyquek@sutd.edu.sg).

for intelligent transportation services, e.g., autonomous driving, video streaming and location mapping [1], [2]. In IoV, dedicated short-range communication technology and cellular network technology are widely applied to enhance vehicle-toinfrastructure (V2I) and vehicle-to-vehicle (V2V) communication [3], [4].

In IoV, many real-time applications, such as artificial intelligence, image-aided navigation and intelligent vehicle control, rely on both communication and computational resources. However, IoV frameworks focus mainly on optimizing communication capabilities, resulting in a bottleneck for the adoption of computationally intensive vehicular applications. To address the increasing demand for computational resources, vehicular edge computing (VEC) has been proposed by integrating with mobile-edge computing (MEC) [5], [6]. In VEC networks, roadside units (RSUs) are strategically deployed along the road near vehicles, thereby providing lowlatency computational support. In particular, considering the inevitable communication and computation overhead, VEC targets computationally intensive and delay constrained tasks. By offloading tasks to these RSUs, vehicles can leverage distributed computational resources, significantly enhancing system performance. Within this paradigm, intelligent task offloading becomes critical. For example, executing all tasks locally results in the waste of computational resources in the VEC network, while indiscriminate offloading to RSUs may introduce communication overhead and queuing delays, especially in dense device environments. These challenges have driven extensive research into optimizing task offloading strategies for VEC networks [7]-[20]. Studies show that selectively offloading tasks to RSUs or nearby vehicles can substantially reduce both execution costs and latency, striking a balance between resource utilization and efficiency.

Aforementioned VEC studies [5]-[20] primarily focus on optimizing task offloading strategies from the vehicle-centric perspective. In addition to the vehicle perspective, emerging RSU-generated applications like road traffic management and autonomous navigation [21] are also computationally intensive and delay constrained, which require task offloading strategies from the RSU perspective. To address this, RSU-to-vehicle (R2V) communication has been introduced, enabling RSUs to leverage vehicle computational resources for task execution [22]-[25]. Furthermore, traditional single-hop offloading restricts viable offloading targets due to vehicle mobility and RSU coverage limitations, resulting in underutilized VEC

network resources. This limitation has spurred interest in multi-hop task offloading [12], [25]-[27], where nearby vehicles act as relays to extend offloading reach. By treating nearby vehicles as relay nodes, tasks from RSUs can be further routed to out-of-coverage vehicles, thereby maximizing resource utilization across the VEC network.

With the rapid advancement of VEC, computational demands are increasing not only for vehicles but also for RSUs. While existing studies address task offloading from either the vehicle or the RSU perspective, they overlook scenarios where both entities have concurrent computational demands. In this paper, we aim at jointly optimizing the task offloading strategies for both V2X and RSUs-to-everything (R2X). Specifically, tasks generated by vehicles and RSUs can be offloaded to all other nodes, i.e., vehicles, RSUs and the cloud center via multi-hop transmissions. However, given that both the network topology and the offloading positions space are related to the number of vehicles and RSUs, this joint task offloading problem for both vehicles and RSUs in dynamic VEC networks poses significant challenges for current task offloading schemes.

## A. Literature Review

Current task offloading strategies can be broadly classified into two main categories, conventional optimization-based schemes [7]-[14] and Deep Reinforcement Learning (DRL)based schemes [15]-[20]. Conventional schemes, e.g., greedy and game theory-based approaches, can effectively obtain the near-optimal solutions based on special architectures and configurations of the problem. In [7], a greedy heuristic algorithm was proposed to optimize the V2X service placement by assigning services to the nearest computing node with sufficient capacity, leading to low algorithmic complexity. Similarly, [8] compared the task offload algorithms based on game theory and based on approximate load balancing in VEC networks, highlighting the importance of load balancing between edge servers. In [12], the multi-hop offloading problem is approximated as a generalized allocation model, and the greedy and bat algorithms were adopted to address it by constraining the maximum hop counts. Despite the domain-specific advantages, conventional methods face inherent limitations. First, they exhibit a trade-off between computational complexity and solution quality [28]. Second, these strategies are typically tailored to specific problem configurations, e.g., fixed network topologies, which may encounter severe performance degradation in dynamic VEC scenarios.

Recently, Deep Reinforcement Learning (DRL) has achieved great success in sequential decision problems. By training the model offline and deploying the converged model online, the DRL approach achieves excellent decision making capability with low computational complexity. Motivated by it, the DRL-based task offloading strategies become popular in the VEC network [15]-[17], [19]. In [15], a twin delayed deep deterministic policy gradient-based approach is proposed to minimize task execution time and energy cost by jointly optimizing the task offloading and resources allocation for V2V and vehicles-to-RSUs (V2R). In [16], considering heterogeneous resources among vehicles, RSUs and the VEC

server, the asynchronous advantage actor-critic is introduced for task offloading and multi-resource management. By regarding vehicles as multiple agents, a multi-agent reinforcement learning (MARL)-based scheme is proposed to address the task offloading problem in dynamic VEC networks [19].

## B. Motivation

The joint task offloading problem for both V2X and R2X addressed in this paper, where tasks from vehicles and RSUs can be offloaded to any device in the VEC network via multihop transmission, comprises three primary challenges.

First, the multi-hop transmission and R2X/V2X task offloading features lead to an excessive action space, particularly in large-scale scenarios. With increasing vehicles and RSUs, the action space increases exponentially. For instance, in a small-scale VEC scenario with 5 vehicles, 2 RSUs, and 1 VEC server, the action space size is 7 8 = 2097152 , which requires substantial computational resources for conventional DRL models using multi-layer perception (MLP) and recurrent neural network (RNN). Moreover, such DRL models cannot efficiently capture the correlation across vehicles and RSUs, resulting in inferior performance.

Second, due to vehicle mobility, both the number and position of vehicles are varying in dynamic VEC networks. This dynamic feature introduces nonalignment between scenarios during training and testing, which requires generalization capacity in inexperienced scenarios. Since existing DRL-based task offloading strategies mainly focus on experienced scenarios [15]-[17], [19], [25], these schemes using conventional models may encounter severe performance degradation in inexperienced scenarios due to implicit partial observability [29]. In particular, when the number of vehicles and RSUs changes, the dimension of the input state and the output offload action also changes, which poses challenges to conventional MLP/RNN-based DRL models.

Moreover, since tasks can be offloaded to all devices in the VEC network through a multi-hop manner, the varying number of vehicles and RSUs further introduces a severe state-action space shift issue. For example, denote action a i = 5 as offloading of tasks from device i to the 5 -th device, corresponding to RSU 1 in a VEC scenario with 4 vehicles and 2 RSUs (assuming vehicles are indexed before RSUs). However, in scenarios with more than 5 vehicles, a same action a i = 5 would instead represents offloading task to the 5 -th vehicle. Furthermore, when the numbers of vehicles and RSUs are reduced, e.g., 3 vehicles and 1 RSU, certain actions a i = 5 is no longer be valid. Since DRL focus on the fixed state-action space with determined representations, such action space shift issue significantly degrade the performance, especially in inexperienced scenarios [30].

## C. Contributions and Main Results

In this paper, considering multi-hop task offloading problem in dynamic VEC networks for both vehicles and RSUs, we propose Bidirectional Encoder Representations from Transformers (Bert)-based matching Q-network (BMQN) approach to minimize the task execution time by optimizing the joint tasks offloading decision for both V2X and R2X.

For the first issue, we design a Bert-enhanced BMQN model that dynamically adapts to the scale of VEC networks while maintaining parameter efficiency. Unlike conventional MLP and RNN-based DRL architectures applied in scenarios with fixed input-output mapping dimensions, BMQN leverages a foundation model-based Bert with bidirectional attention mechanisms to adaptively scale to the number of vehicles and RSUs without parameter overhead. Moreover, through the bi-directional attention, the BMQN model can contextually capture correlations among vehicles and RSUs [31]. In the BMQN model, the embeddings for heterogeneous nodes, including vehicles, RSUs and the cloud server, can be dynamically weighted through cross-device attention to capture real-time resource availability and spatial relationships. This bidirectional attention mechanism allows the Bert module to distill intrinsic correlations between entities, significantly enhancing offloading performance.

For the second issue, we propose type-embedded grouped attention and available action embedding in the BMQN model to enhance the generalization capacity. Considering the total number of vehicles and RSUs as the sequence length, LLMs encounter severe performance degradation in inexperienced scenarios due to the over-fitting sequence length issue for foundation models [32]. Specifically, positional embedding serves as important relationship information in transformerbased foundation models. When the number of devices is different from that during training, inexperienced position information leads to inappropriate attention weight, resulting in performance degradation [33], [34]. In the BMQN, instead of conventional positional indices, we propose to leverage the device types, i.e., vehicle, RSU and cloud center, as the grouped attention to provide device information for vehicles and RSUs. In particular, we further propose an available action embedding in the BMQN model to provide information on the current task offloading space, which further enhances the generalization capacity.

For the third issue, we propose to address this joint task offloading problem with the state-action space shift issue through a novel matching-based manner. Conventional DRL schemes aim to estimate Q-values for a fixed action space, which is insufficient for this dynamic scenario. Instead of directly calculating Q-values, we propose a pairwise state matching scheme in the BMQN model to adaptively compute Q-values for each offloading decision across vehicles and RSUs, which can adapt to the shifted state-action space. Specifically, we deploy two independent Bert modules in the BMQN to extract the hidden state for each vehicle and RSU when serving as offloading initiator and receiver, respectively. Then, these hidden states can be jointly matched to obtain the Q-values, which can be then used to determine the joint task offloading strategy. This matching-based architecture ensures that the output vector size dynamically adjusts to the current shifted action space without requiring modifications to the model parameters. By emphasizing the learning of relationships among agent states instead of relying on a fixed stateaction space, the BMQN model can enhance task offloading performance in both experienced and inexperienced scenarios.

The main contributions of our work are summarized as follows:

- We design a foundation model-based BMQN to adapt to the dynamic scale of VEC networks while efficiently capturing the correlation among vehicles and RSUs, thereby addressing the issue of varying number of vehicles and RSUs in dynamic VEC networks. Then, we propose typeembedded grouped attention to mitigate the over-fitting sequence length issue of the foundation model, in which the device type embedding serves as group attention instead of conventional position indices. Moreover, we propose an available action embedding to identify the current action space, which further enhances the generalization capacity in inexperienced scenarios.
- We propose a novel matching-based architecture within the BMQN model to effectively address the challenging state-action space shift issue. In the BMQN, we utilize two independent Bert modules to extract hidden states for each vehicle and RSU when they act as offloading initiators and receivers, respectively. These hidden states are then jointly matched to determine the optimal task offloading actions. By focusing on learning the correlations among devices rather than relying on Q-values within a fixed state-action space, the BMQN significantly enhances task offloading performance.
- We evaluate the performance of proposed BMQN in both experienced and inexperienced dynamic VEC scenarios with varying number of vehicles, RSUs and diverse road length. Simulation results demonstrate that the BMQN can achieve significantly better performance and generalization capacity in all scenarios compared with conventional greedy scheme and other popular DRL algorithm as well as other foundation model-based actorcritic approaches.

## D. Outline

The remainder of the paper is organized as follows: Section II formulates the background of foundation models. Section A. elaborates the system model and problem of interest in VEC networks. Section IV illustrates the proposed BMQN algorithm. Section V demonstrated the simulation results, and the conclusion are provided in section VI.

## II. PRELIMINARIES

## A. Foundation Model

Recently, Large Language Models (LLMs) have emerged as one of the most popular artificial intelligence (AI) techniques, which has widely revolutionized the natural language process (NLP) domain, e.g., GPT [35], [36]. LLMs have revolutionized various domains through its awesome comprehending and inferring ability in human-text data [37]. LLMs are trained on vast amounts of diverse text data and are designed to understand and generate human language, which is widely applied in NLP tasks, e.g., question-answering, text generation and text summarization. Through the transformer architecture and massive model parameters, LLMs can process highdimensional data and generate large-scale text, making them efficient for a variety of NLP tasks. However, LLMs focus on NLP tasks with human-text data, which obstacles its application in tasks of other domains. To address downstream tasks that involve domain-specific data, the foundation model and the fine-tuning technique are introduced. The foundation model is a type of LLM that serves as the starting point for constructing more specialized models aiming at the taskspecific domain. Similarly, the foundation model is pre-trained with diverse human-generated text data as that of LLMs to establish comprehending ability on large-scale input vectors. Due to the great inferring and comprehending ability of foundation model, there is a growing interest in integrating it into wireless scenarios [38]-[41].

Fig. 1. The Bert model utilizes bi-directional attention to capture the relationship across input tokens, in which both the former and latter tokens and corresponding hidden states are passed to the module for current token. 'Trm' represents the transformer architecture.

<!-- image -->

Fig. 2. The GPT-based model using uni-directional attention to capture the relationship between input tokens, in which only the former tokens and corresponding hidden states are passed to the module for current token.

<!-- image -->

Foundation models can be roughly divided into two types, e.g., the Bert-based models using bi-directional attention and the GPT-based models using uni-directional attention. As Fig. 1 illustrates, by sharing the tokens and hidden states among multiple transformer modules using bi-directional attention, Bert-based models can aggregate information among input tokens and capture the contextual feature [31]. Therefore, the Bert-based model illustrates better performance in feature extraction tasks. For GPT-based models, as Fig. 2 illustrates, the uni-directional attention is applied, in which only the former tokens and corresponding hidden states are passed to modules for the current token [35]. Through uni-directional attention, GPT-based models can reduce half of the computational complexity, and achieve better performance in longtext generation tasks. In this paper, aiming at extracting the intrinsic relationship among vehicles and RSUs, we adopt the Bert in the BMQN model to achieve better decision ability.

Fig. 3. The considered VEC network with single VEC server,multiple RSUs and vehicles. The vehicles moves with different speeds and directions along the x-axis. The task of each vehicle and RSU can be offloaded to each available device including vehicle, RSU or VEC server.

<!-- image -->

## B. Fine-tune Technique

After pre-training, the foundation model should be further fine-tuned for downstream tasks. The domain-specific data is utilized as fine-tuning data. Due to the over-parameterized feature of foundation models, directly fine-tuning all parameters in the foundational model results in excessive computational cost, leading to the emergence of fine-tuning approaches [36]. Recently, the Low-Rank Adaptation (LoRA) has emerged as one of the most popular fine-tune approaches [42]. By injecting the trainable low-rank decomposition matrices into selected linear layers in the transformer while freezing the original model parameters, the convergence rate can be enhanced and the required training cost can be significantly reduced. Denoting the low-rank decomposition matrices as A ∈ R d × n , B ∈ R n × d and weight matrix of original layer as W ∈ R d × d , the procedure of LoRA is given by

<!-- formula-not-decoded -->

in which h and x denote the output and input of original linear layer, respectively. In particular, the over-parameterized model actually resides on a low intrinsic dimension, which enables efficient fine-tuning of the foundational model using a reduced parameter space [43]. Therefore, fine-tuning foundation models using low-rank decomposition matrices in LoRA can achieve a performance level to that training from scratch, but with significantly lower training costs and a higher convergence rate.

## III. SYSTEM MODEL AND PROBLEM OF INTEREST

In this paper, for simplicity, we consider a single road scenario in the VEC network. As Fig. 3 illustrates, we consider a three-level VEC network comprising a VEC server, multiple RSUs and vehicles. The set of RSUs is denoted as M = { 1 , 2 , . . . , M } , and the set of vehicles is denoted as N = { 1 , 2 , . . . , N } . The time within this VEC network is divided into multiple time slots, denoted as { 1 , 2 , . . . , t, t + 1 , . . . } . As Fig. 4 illustrates, each RSU and vehicle generate an independent computation task at the beginning of each time slot t . The task r of device i at time slot t is characterized by ( S r i,t , C r i,t , d r i,t ) [15], [16], where S r i,t denotes the size of task data, C r i,t denotes the required CPU cycle per bit of task data and d r i,t denotes the execution delay constraint of the task. For both vehicles and RSUs, tasks are executed through a first come first serve (FCFS) manner, in which the second task can be computed only when the computation of the first task is completed. In particular, the task calculated halfway at the last time slot t will continue executing in the next time slot t +1 .

Fig. 4. Illustration of the task model and queuing model in the VEC network.

<!-- image -->

## Author Biographies

Mingqi Han received the B.Eng. degree in Communication Engineering from School of Electronics and Communication Engineering, Shenzhen Campus of Sun Yat-sen University, Shenzhen, China in 2022. He is currently pursing for the M.E. degree in Information and Communication Engineering with School of Electronics and Communication Engineering, Shenzhen Campus of Sun Yat-sen University, Shenzhen, China. His research interests include machine learning, reinforcement learning and multiple access.

<!-- image -->

Xinghua Sun (M'13) received the B.S. degree from Nanjing University of Posts and Telecommunications (NJUPT), China, in 2008 and the Ph.D. degree from City University of Hong Kong (CityU), China, in 2013. In 2010, he was a visiting student with National Institute for Research in Digital Science and Technology (INRIA), France. In 2013, he was a postdoctoral fellow at CityU. From 2015 to 2016, he was a postdoctoral fellow at University of British Columbia, Canada. From July to Aug. 2019, he was a visiting scholar at Singapore University of

Technology and Design, Singapore. From 2014 to 2018, he was an associate professor with NJUPT. Since 2018, he has been an associate professor with Sun Yat-sen University, Guangdong, China. His research interests are in the area of stochastic modeling of wireless networks and machine learning for next generation wireless communications and networks. He was a co-recipient of the Best Paper Award from the EAI IoTaaS in 2023 and the IEEE FCN in 2024.

<!-- image -->

Xijun Wang (Member, IEEE) received the B.S. degree (Hons.) in communications engineering from Xidian University, Xi'an, Shaanxi, China, in 2005, and the Ph.D. degree in electronic engineering from Tsinghua University, Beijing, China, in January 2012. He was an Assistant Professor from 2012 to 2015 and an Associate Professor from 2015 to 2018 with the School of Telecommunications Engineering, Xidian University. From 2015 to 2016, he was a Research Fellow with the Information Systems Technology and Design Pillar, Singapore University

of Technology and Design. He is currently an Associate Professor with Sun Yat-sen University. He has published several IEEE journals and conference proceedings in the areas of wireless networks and patents related to heterogeneous networks. His current research interests include UAV communications, edge computing, and age of information. He served as the technical program committee member for numerous IEEE conferences. He was a recipient of the Best Paper Award from the IEEE ICCC 2013. He also served as the Publicity Chair for IEEE ICCC 2013 and the Technical Program Co-Chair for the Wireless Communications Systems Symposium and IEEE ICCC 2016. He is currently a reviewer for several IEEE journals. He was recognized as an Exemplary Reviewer of the IEEE WIRELESS COMMUNICATIONS LETTERS in 2014. He is currently an Associate Editor of IEEE ACCESS.

<!-- image -->

Wen Zhan (Member, IEEE) received the B.S. and M.S. degrees from the University of Electronic Science and Technology of China, China, in 2012 and 2015, respectively, and the Ph.D. degree from the City University of Hong Kong, China, in 2019. He was a Research Assistant and a Postdoctoral Fellow with the City University of Hong Kong. Since 2020, He has been with the School of Electronics and Communication Engineering, Sun Yat-sen University, China, where he is currently an Assistant Professor. His research interests include Internet of

Things, modeling, and performance optimization of next-generation mobile communication systems.

<!-- image -->

Xiang Chen (Member, IEEE) received the B.E. and Ph.D. degrees from the Department of Electronic Engineering, Tsinghua University, Beijing, China, in 2002 and 2008, respectively. From July 2008 to December 2014, he was with the Wireless and Mobile Communication Technology Research and Development Center (Wireless Center) and the Aerospace Center, Tsinghua University. In July 2005 and from September 2006 to April 2007, he visited NTT DoCoMo Research and Development (YRP), and Wireless Communications and Signal Process-

ing (WCSP) Laboratory, National Tsing Hua University. Since January 2015, he has been with the School of Electronics and Information Technology, Sun Yat-sen University, where he is currently a Full Professor. His research interests mainly focus on 5G/6G wireless and mobile communication net works, and the Internet of Things (IoT).

<!-- image -->

Tony Q. S. Quek Tony Q. S. Quek (S'98-M'08SM'12-F'18) received the B.E. and M.E. degrees in electrical and electronics engineering from the Tokyo Institute of Technology in 1998 and 2000, respectively, and the Ph.D. degree in electrical engineering and computer science from the Massachusetts Institute of Technology in 2008. Currently, he is the Cheng Tsang Man Chair Professor with Singapore University of Technology and Design (SUTD) and ST Engineering Distinguished Professor. He also serves as the Director of the

Future Communications RD Programme, the Head of ISTD Pillar, and the Deputy Director of the SUTD-ZJU IDEA. His current research topics include wireless communications and networking, network intelligence, non-terrestrial networks, open radio access network, and 6G.

Dr. Quek has been actively involved in organizing and chairing sessions, and has served as a member of the Technical Program Committee as well as symposium chairs in a number of international conferences. He is currently serving as an Area Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS.

Dr. Quek was honored with the 2008 Philip Yeo Prize for OutstandingAchievement in Research, the 2012 IEEE William R. Bennett Prize, the 2015SUTD Outstanding Education Awards- Excellence in Research, the 2016 IEEE Signal Processing Society Young Author Best Paper Award, the 2017 CTTC Early Achievement Award, the 2017 IEEE ComSoc AP Outstanding Paper Award, the 2020 IEEE Communications Society Young Author Best Paper Award, the 2020 IEEE Stephen O. Rice Prize, the 2020 Nokia Visiting Professor, and the 2022 IEEE Signal Processing Society Best Paper Award. He is a Fellow of IEEE and a Fellow of the Academy of Engineering Singapore.
