---
title: Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration
authors:
  - name: Xinxin He
    affiliation: Beijing University of Posts and Telecommunications (BUPT), Beijing Key Laboratory of Network System Architecture and Convergence, China
  - name: Yang Yang
    affiliation: Beijing University of Posts and Telecommunications, China
  - name: Zhiyong Yang
    affiliation: Beijing University of Posts and Telecommunications, China
  - name: Yifei Gao
    affiliation: Beijing University of Posts and Telecommunications, China
  - name: Changchuan Yin
    affiliation: School of Information and Communication Engineering, Beijing University of Posts and Telecommunications, China
  - name: Shanzhi Chen
    affiliation: China Information and Communication Technology Group Co., Ltd. (CICT), China
doi: 10.1109/MCOM.001.2500421
year: 2024
abstract: |
  Large artificial intelligence models (LAMs) have introduced new opportunities to 6G networks, whereas their integration into vehicle-road-cloud collaborative systems remains challenging due to insufficient model coordination and difficulties in dynamic resource adaptation. To address these issues, this article proposes an agent-based network architecture and a resource management method for vehicle-road-cloud collaboration.
keywords:
  - Agent-based networks
  - Vehicle-road-cloud architecture
  - Large language models
  - Resource management
  - 6G networks
  - V2X communication
publication_type: magazine
venue: IEEE Communications Magazine
---

## Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration Xinxin He, Yang Yang, Zhiyong Yang, Yifei Gao, Changchuan Yin, and Shanzhi Chen

## Abstract Large artificial intelligence models (LAMs) have introduced new opportunities to 6G networks, whereas their integration into vehicle-road-cloud collaborative systems remains challenging due to insufficient model coordination and difficulties in dynamic resource adaptation. To address these issues, this article proposes an agent-based network architecture and a resource management method for vehicle-road-cloud collaboration. In this architecture, the cloud agent conducts largescale pre-training to characterize global resource allocation dynamics, while lightweight models are deployed at the road-side unit (RSU) agent and vehicle agent to enable real-time inference and decision-making. To balance model performance and resource consumption, we introduce a lifecycle management strategy for the agent network. By analyzing the relationship between performance gain and the consumption of communication and computation resources, we jointly optimize training data sampling rates, model pruning ratio, and resource allocation strategies. This enables dynamic adjustment of the update frequency for cloud-based large models and the fine-tuning frequency for edge-side models, thereby ensuring continuous and high-efficiency model inference in resource-constrained dynamic scenarios. Additionally, we design a decision LAM (D-LAM) for single-task scenarios, which employs sequence modeling and temporal embedding to achieve dynamic coordination of multi-dimensional resources. We further develop a decision multi-task LAM (DM-LAM) to address complex multi-task scenarios, which integrates a mixture-of-experts (MoE) mechanism with a gating network to support both personalized resource allocation for individual tasks and global optimization across heterogeneous tasks. Experimental results demonstrate that the proposed method significantly improves resource utilization efficiency and achieves 10±$1.2% higher task completion rates compared to decision transformer model.

## Introduction Autonomous driving is an emerging technological industry that deeply integrates next-generation information technologies and artificial intelligence (AI) with intelligent vehicles. It has become a critical direction for the development of smart transportation and smart cities, which is a key strategic focus worldwide [1]. With the development of Vehicle-to-Everything (V2X) technology, the integrated vehicle-road-cloud collaborative architecture, which enables seamless coordination among vehicles, roadside infrastructure, and cloud services through interconnected technologies, is opening up new possibilities for intelligent transportation. Moreover, it is widely recognized as a necessary pathway toward achieving fully autonomous driving [2].

With the advent of the 6G era, integrating AI into network ecosystems and constructing natively intelligent agent-based networks has become a widely recognized goal in both academia and industry [3-5]. Within the vehicle-road-cloud collaborative architecture, significant heterogeneity exists in computing capabilities and data latency among vehicles, edge servers, and cloud platforms. This necessitates task-oriented and adaptive coordination of multi-dimensional resources, including sensing, communication, computation, and AI models. Currently, research on agent-based system architectures and resource management for vehicle-road-cloud collaboration remains in early stages. The authors in [6] proposed a resource cluster-based search and allocation scheme that enables inter-cluster resource discovery for multi-dimensional resource types, aiming to improve allocation efficiency and adaptability in highly dynamic environments. In [7], a sense-and-utilize approach was adopted to model the distribution of computational resources, and a decentralized multi-agent deep reinforcement learning (DRL) algorithm was introduced to address collaborative task offloading in vehicular cloud computing. While these studies provide preliminary solutions to the resource allocation challenges under vehicle-road-cloud architectures, their effectiveness heavily relies on strict assumptions about application scenarios. Once Xinxin He is with Beijing University of Posts and Telecommunications (BUPT) and the Beijing Key Laboratory of Network System Architecture and Convergence, China; Yang Yang, Zhiyong Yang, and Yifei Gao are with Beijing University of Posts and Telecommunications, China; Changchuan Yin is with the School of Information and Communication Engineering at BUPT, China; Shanzhi Chen is with China Information and Communication Technology Group Co., Ltd. (CICT), China.

Digital Object Identifier: 10.1109/MCOM.001.2500421

Magazine - lArge AI

Models For Communications

the environmental state changes, the designed strategies often fail to generalize or transfer to new contexts. Furthermore, traditional reinforcement learning (RL), which relies on the Bellman equation for iterative value updates, is prone to instability under sparse reward conditions or noisy signals. es at the edge, it achieves gradient-based resource n to optimize inference accuracy. despite the promistial of LAMs in communication networks, signi lenges remain in developing lAM-enabled intelligent

2

FIGURE 1. Vehicle-road-cloud architecture with large-lightweight AI model collaboration.

<!-- image -->

Vehicle-road-cloud architecture with large-lightweight AI

model

- This article proposes an agent-based vehicleroad-cloud collaborative network architecture, which enables efficient collaborative training and real-time inference through pre-training cloud-based LAM and deploying lightweight, pruned models at the edge. dynamic collaboration first introduces a collaborative framework between large and lightweight models in vehicle-road-cloud systems, along with the model lifecycle management strategy. Then we presents a
- This article proposes a decision LAM (D-LAM)based resource management method in single-task V2X scenarios. A sequence modeling framework with temporal embedding is developed to model multi-dimensional resource coordination as a sequential prediction task. For multi-task scenarios, a decision multi-task LAM (DM-LAM) with a mixture-of-experts (MoE) mechanism is proposed, which enables personalized and globally coordinated resource allocation across heterogeneous tasks through expert selection and gating, improving generalization and adaptability in dynamic environments. are as efinference The proposed vehicle-road-cloud architecture with largelightweight model collaboration is illustrated in Fig. 1. This framework supports various wireless communication applications in both V2V and V2I, such as vehicle cooperative perception, vehicle-infrastructure coordination, and autonomous driving. To address diverse requirements across these applications, such as minimizing task latency, maximizing energy efficiency, the architecture performs multiple resource management operations including: V2V/V2I mode switch, power allocation, task
- A model lifecycle management method for agent networks is introduced. By comprehensively considering pre-training costs, fine-tuning costs, and inference performance, the method dynamically adjusts the update of cloud-based LAM, the fine-tuning of edge-base models, and the pruning strategy, ensuring continuous and efficient inference in V2X scenarios. a resource management method based on LAM for both singletask and multi-task scenarios, followed by simulation analysis and concluding remarks. II. V EHICLE -R OAD-CLOUD ARCHITECTURE WITH L ARGE -L IGHTWEIGHT AI MODEL COLLABORATION

The remainder of this article is organized as follows. We first introduces a collaborative framework between large and lightweight models in vehicle-road-cloud systems, along with the model lifecycle management strategy. Then we presents a resource management method based on LAM for both single-task and multi-task scenarios, followed by simulation analysis and concluding remarks. offfioading, and heterogeneous computing resource matching. Beyond multi-scenario resource management, the framework also regulates system operation cycles to achieve coordinated resource management and operational maintenance, including: fine-tuning cycles for the road-side unit (RSU) agent models, training update cycles for cloud models, and pruning control.

Against this backdrop, the emergence of powerful large artificial intelligence models (LAMs), such as ChatGPT, LLaMA, DeepSeek, and Gemini, has created transformative opportunities to enhance the performance and interactivity of 6G networks [8]. In native AI-driven wireless systems, LAMs possess cognitive capabilities such as perception, analogy, and reasoning, enabling them to rapidly emulate communication environments. This enables efficient generalization and adaptation to unforeseen scenarios while supporting personalized services [9-11]. Recent academic efforts have explored the integration of LAMs into 6G networks, yielding early-stage designs for communication-oriented LAM architectures and novel wireless network frameworks. For instance, [12] proposes a LAM multi-agent communication framework to enhance intelligent decision-making and resource scheduling among agents in 6G environments. In [13], the decision transformer (DT) model is introduced for wireless resource management, addressing challenges such as long-term credit assignment and sequential decision modeling. Reference [14] presents a cloud-edge collaborative architecture. By jointly considering retraining frequency in the cloud and inference frame rates at the edge, it achieves gradient-based resource allocation to optimize inference accuracy. Despite the promising potential of LAMs in communication networks, significant challenges remain in developing LAM-enabled intelligent agent systems for wireless scenarios. At the system coordination perspective, there is a lack of mechanism design for the collaboration between LAMs and lightweight communication models, including standard evaluation metrics for agent networks, adaptive update scheduling across cloud-edge-end hierarchies, and balancing trade-offs between model performance and resource consumption in the cloud. Moreover, cloud-edge collaborative intelligent networks must support diverse vehicular communication patterns, including both vehicle-to-infrastructure (V2I) communication and vehicle-to-vehicle (V2V). At the model perspective, the deep integration of general-purpose large models with knowledge specific to layered communication network architectures remains inadequate. It is necessary to further explore sequential decision-making models that align with the scheduling characteristics of communication and computing resources, as well as joint strategies for multi-task resource coordination in dynamic vehicular environments. tems for wireless scenarios. At the system coordirspective, there is a lack of mechanism design for boration between LAMs and lightweight communicals, including standard evaluation metrics for agent adaptive update scheduling across cloud-edge-end es, and balancing trade-offs between model perforresource consumption in the cloud. Moreover, e collaborative intelligent networks must support ehicular communication patterns, including both o-infrastructure (V2I) communication and vehicle-to). At the model perspective, the deep integration l-purpose large models with knowledge speci c to ommunication network architectures remains inades necessary to further explore sequential decisiondels that align with the scheduling characteristics ication and computing resources, as well as joint multi-task resource coordination in environments. the above challenges, this paper proposes er agent-based vehicle-road-cloud collaborative are that integrates large and lightweight models, along rresponding performance evaluation methodology. n, a dual-loop resource management framework is d. In the outer loop, a hierarchical model lifecycle t strategy is designed for the networked system. loop, multi-dimensional resource management r single-task and multi-task scenarios are designed the main contributions of this work aper proposes an agent-based vehicle-road-cloud aborative network architecture, which enables collaborative training and real-time ugh pre-training cloud-based lAM and deploying tweight, pruned models at the edge. l lifecycle management method for agent netintroduced. by comprehensively considering raining costs, ne-tuning costs, and inference perFig. 1.

## VehIcle-roAd-cloud ArchItecture WIth lArgelIghtWeIght AI Model collAborAtIon The multi-layer collaborative resource management architecture based on LAM consists of the cloud agent layer, the

workffiow

vehicle agent

management

includes

fine-tuning, model The proposed vehicle-road-cloud architecture with large-lightweight model collaboration is illustrated in Fig. 1. This framework supports various wireless communication applications in both V2V and V2I, such as vehicle cooperative perception, vehicle-infrastructure coordination, and autonomous driving. RSU agent layer and the vehicle agent layer, the of the architecture is as Fig. 2 shows. The includes feature data uploading and resource decision feedback. The RSU agent layer primarily dataset construction, model quantization,

s

for

ess

ner

ely.

nt

s

is

dding To address the above challenges, this article proposes a three-layer agent-based vehicle-roadcloud collaborative architecture that integrates large and lightweight models, along with a corresponding performance evaluation methodology. In addition, a dual-loop resource management framework is introduced. In the outer loop, a hierarchical model lifecycle management strategy is designed for the networked system. In the inner loop, multi-dimensional resource management models for single-task and multi-task scenarios are designed respectively. The main contributions of this work are as follows: ance, the method dynamically adjusts the update of d-based lAM, the ne-tuning of edge-base models, the pruning strategy, ensuring continuous and ef t inference in V2X scenarios. aper proposes a decision lAM (d-lAM)-based urce management method in single-task V2X sceos. A sequence modeling framework with temporal is developed to model multi-dimensional urce coordination as a sequential prediction task. For i-task scenarios, a decision multi-task lAM (dM-

ith a mixture-of-experts (Moe) mechanism is inference, and performance monitoring. The cloud agent layer mainly contains data aggregation, model pre-training, prun- ing optimization, multi-scale resource manager, performance Fig. 2.

FIGURE 2. Workflow of the AI model collaborative based resource management architecture.

<!-- image -->

<!-- image -->

Workfiow of the AI model collaborative based resource management To ado ded tem wei hist

F

fra Fun

vehi

time

sure

and

do

mo

qual

ture

co Ed In

strai

nod

devi

train To

rece

ory

mo

and

task To address diverse requirements across these applications, such as minimizing task latency, maximizing energy efficiency, the architecture performs multiple resource management operations including: V2V/ V2I mode switch, power allocation, task offloading, and heterogeneous computing resource matching. Beyond multi-scenario resource management, the framework also regulates system operation cycles to achieve coordinated resource management and operational maintenance, including: fine-tuning cycles for the road-side unit (RSU) agent models, training update cycles for cloud models, and pruning control. The multi-layer collaborative resource management architecture based on LAM consists of the cloud agent layer, the RSU agent layer and the vehicle agent layer, the workflow of the architecture is as Fig. 2 shows. The vehicle agent includes feature data uploading and resource management decision feedback. The RSU agent layer primarily includes dataset construction, model quantization, fine-tuning, model inference, and performance monitoring. The cloud agent layer mainly contains data aggregation, model pre-training, pruning optimization, multiscale resource manager, performance monitoring system, and lifecycle management of collaborative models. These layers forming a complete closedloop intelligent system framework from data collection to model optimization. cy rescue scenarios, raw data from vehicle sensors, onboard logs, and base station records are collected to extract: environmental features (e.g., channel state information (CSI), road topology), computational resources (e.g., GPU/CPU utilization), communication resources (e.g., available bandwidth, spectral efficiency), behavioral features (e.g., vehicle trajectories, task generation patterns), and resource allocation decisions (e.g., power allocation, task offloading strategies), along with system performance metrics (e.g., latency, spectrum utilization, server load). These samples are labeled according to the RL paradigm (state, action, reward) and stored on RSU agents. Each RSU agent periodically uploads newly collected samples to the cloud for data aggregation, including timestamp alignment, format standardization, redundancy removal, and downsampling of high-frequency scenario data to maintain dataset balance. In addition, considering the security of sensitive data, we deploy part of the feature extraction modules of the cloud agent LAM on the edge side (vehicles and RSUs), and perform adaptive compression on the extracted features based on wireless channel capacity before uploading, effectively protecting the privacy of local sensitive data. Model Pre-trAInIng And MultI-dIMensIonAl AssessMent architecture A. Multi-scenario Dataset Curation and Aggregation To accommodate diverse vehicular scenarios with distinct resource allocation patterns and objective functions, such as multi-agent vehicle platooning, intelligent trafffic management, and emergency rescue operations, the proposed framework ffirst constructs a large-scale training dataset to ensure generalization across different V2X communication scenarios and implement fiexible switching between V2V and V2I modes. During continuous operation, resource management data is sampled periodically from multiple scenarios. For instance, in emergency rescue scenarios, raw data from vehicle sensors, onboard logs, and base station records are collected to extract: environmental features (e.g., channel state information (CSI), C.

efffi

achi

ffine

distr

widt

strat MultI-scenArIo dAtAset curAtIon And AggregAtIon To accommodate diverse vehicular scenarios with distinct resource allocation patterns and objective functions, such as multi-agent vehicle platooning, intelligent traffic management, and emergency rescue operations, the proposed framework first constructs a large-scale training dataset to ensure generalization across different V2X communication scenarios and implement flexible switching between V2V and V2I modes. During continuous operation, resource management data is sampled periodically from multiple scenarios. For instance, in emergenDuring the model pre-training, the cloud designs differentiated prompt templates based on training samples and distinct communication scenario characteristics (e.g., low latency, high throughput), which forms a dynamic multi-scenario prompt library. The prompts are concatenated with training samples before being fed into the LAM to enhance learning capability. To adapt to dynamic environments, the pre-training process adopts incremental learning with timestamp features embedded in training samples. This allows the model to capture temporal evolution patterns in data distribution and a time-weighted loss function balances the learning weights between historical and new data. road topology), computational resources (e.g., GPU/CPU utilization), communication resources (e.g., available bandwidth, spectral effficiency), behavioral features (e.g., vehicle trajectories, task generation patterns), and resource allocation decisions (e.g., power allocation, task offioading strategies), along with system performance metrics (e.g., latency, spectrum utilization, server load). These samples are labeled according to the RL paradigm (state, action, reward) and stored on RSU

agents. Each RSU agent periodically uploads newly collected D.

Mo Ieee communications Magazine · April 2026 samples to the cloud for data aggregation, including timestamp

T

For post-trained models, a multi-dimensional assessment framework is established beyond basic accuracy metrics. Functional evaluation focuses on inference accuracy in RSU-vehicle scenarios, multi-step task completion rates, and real-time decision-making capability. Performance evaluation measures critical metrics including throughput, response latency, and resource utilization rates. Adaptability evaluation involves domain shift testing and adversarial sample detection to verify model robustness. Unqualified models are retrained, while qualified ones are compressed via attention-weighted structured channel pruning to reduce deployment overhead without compromising key features. IEEE COMMUNICATIONS MAGAZINE - LARGE AI MODELS FOR COMMUNICATIONS and

## edge-AdAPtIVe FIne-tunIng And dePloyMent Collaborative model lifecycle management framework An exponential performance an

P . the FIGURE 3. Collaborative model lifecycle management framework.

S

sm

rel

ac

th

inverse

an

. The se

σ

, where

ψ

re

ve

training b

converge

rat

and accele

tra

vergence attainment. Consequently, by acquiring t

calculate dis

count

delay can both bef ba be mi The length of the model fine-tuning cycle is joi

and model pe

e

- βδfi used is to

ne

function

decay after the

P

.

th

fine-tu

P

<!-- image -->

0

degree

ne. Considering the specified performance lower

δfi

n

throughout Cfi

ne

δfi

ne

δfi

ne account

where Collaborative model lifecycle management framework

ple cost-performance dimensions Based on the aforementioned model fine-tuning and cloud-

In vehicle-road-cloud collaborative architectures, constrained by the computing capacity and bandwidth of edge nodes (RSUs and vehicles), direct deployment of LAM and on-device training are both highly inefficient. Additionally, pre-trained models suffer from environmental adaptability issues. To address these challenges, quantization is applied to the received pre-trained models to reduce computational and memory overhead. For optimal resource management, the quantized models undergo fine-tuning using scenario-specific prompts and small dataset before deployment for resource management tasks. This article introduces low-rank adaptation (LoRA) as an efficient fine-tuning solution for LAM deployment on RSUs, achieving lightweight and modular parameter updates. After fine-tuning, only the low-rank adaptation modules need to be distributed to vehicle agents. This significantly reduces bandwidth consumption and deployment overhead while demonstrating rapid scenario adaptation capability. Fig. 3. dynamically The cloud-based control tuning and work is illustrated Fig. 3.

δfi Model eVAluAtIon And lIFecycle MAnAgeMent To address dynamic environment, the proposed architecture dynamically adjusts roadside model fine-tuning frequency and cloud-side LAM update intervals for efficient resource management. Edge devices continuously collect incremental samples, storing them in local datasets following the training data construction pipeline. Each device implements real-time model state monitoring, tracking inference metrics and performance indicators. These metrics jointly determine optimal fine-tuning frequency through model cost-performance analysis. However, the adaptation capacity of model fine-tuning is inherently limited. When environmental changes exceed a certain threshold, even fine-tuned models fail to maintain satisfactory performance. To address this limitation, the system activates cloud-based incremental learning that RSU uploads incrementally collected samples to the cloud for data aggregation, followed by incremental updates to the LAM using the aggregated dataset. The updated model undergoes comprehensive evaluation and targeted pruning before being redistributed to base stations for deployment. The cloud-based control center employs a multi-scale resource management controller to regulate both the model fine-tuning and incremental learning updates throughout model lifecycle. The proposed model lifecycle management framework is illustrated as Fig. 3. We mainly account multi-dimensional cost factors include: computational and memory resources for fine-tuning, inference latency and performance, cloud computational and memory overhead for model updates, bandwidth consumption for both incremental data upload and model distribution, the impact of pruning ratio on model accuracy as well as sampling rates of incremental training datasets. Through an actor-critic architecture, the framework dynamically optimizes the fine-tuning cycles, pruning ratio and the cloud update frequency, achieving maximal model performance under predefined resource constraints. Specifically, to account for the dynamic nature of V2X network topologies, we configure the model fine-tuning d fine = p t to be performed every p transmission slots. Considering the limited effectiveness of model fine-tuning, we establish a model update window l that triggers a cloud-based LAM update after every k fine-tuning rounds. During this window, the model is retrained and updated to ensure the accuracy of locally deployed models. Let d train = l + k d fine denote the model update period. The model update window consists of sample data transmission delay, model pre-training delay, and model distribution delay. The relationship between training batch size b , model pruning rate s , and convergence rate g , which is characterized by an upper bound on the average L2-norm of gradients [15]: based incremental learning framework, a multi-scale resource management is established at the cloud center to orchestrate the model production and adaptation pipeline. This controller coordinates edge-side fine-tuning cycles, cloud model update intervals, and pruning ratio by holistically evaluating multiple cost-performance dimensions center employs a multi-scale resource management controller to regulate both the model fineincremental learning updates throughout model lifecycle. The proposed model lifecycle management frameas Fig. 3. We mainly account multidimensional cost factors include: computational and memory resources for fine-tuning, inference latency and performance, cloud computational and memory overhead for model updates, bandwidth consumption for both incremental data upload and model distribution, the impact of pruning ratio on model accuracy as well as sampling rates of incremental training datasets. Through an actor-critic architecture, the framework dynamically optimizes the fine-tuning cycles, pruning ratio and the cloud update frequency, achieving maximal model performance under predefined resource constraints. Specifically, to account for the dynamic nature of V2X network topologies, we configure the model fine-tuning δfi ne = pτ to be performed every p transmission slots. Considering the limited effectiveness of model fine-tuning, we establish a model update window λ that triggers a cloud-based LAM update after every k fi ne-tuning rounds. During this window, the model is retrained and updated to ensure the accuracy of locally deployed models. Let δ train = λ + kδfi ne denote the model update period. The model update window consists of sample data transmission delay, model pre-training delay, and model distribution delay. The relationship between training batch size b , model pruning rate σ , and convergence rate γ , which is characterized by an upper bound on the average L2norm of gradients [15]: the fine-tuning cost consumption involved in a si model with parameter quantity M includes: (1) cost , governed by M , fine-tuning parameter ratio parameter cost; (2) computation cost , determin training duration, hardware cost, and batch size; (3 cost , influenced by the parameter storage coefficie unit storage cost. For different fine-tuning strategies, the model pe improvements vary. We introduce a fine-tuning effic to quantify the fine-tuned model performance. T mance gain ∆ P after fine-tuning consists of distrib ilarity between incremental data and historical dat efficiency coefficient, and fine-tuning efficacy factor tuning efficiency function can be expressed as: ηfi ne ( δfi After multiple rounds of model fine-tuning, benefits of fine-tuning operations diminish. When tuning gain falls below a threshold, a cloud-based L and subsequent local redeployment are required. The the model update cycle primarily considers multi-di factors including retraining cost and update perform The cost consumed by a single model update consi parameter cost , governed by initial training param tity and unit parameter cost; (2) computation cost , by M , training duration, hardware cost and batc memory cost , influenced by pruning rate, paramet coefficient, M and unit storage cost. Combined with the model update window length, efficiency function can be expressed as: η train ( δ train , σ ) = C train + λ δ train -∆ F ( σ, b ) Based on the aforementioned model fine-tuning and cloudbased incremental learning framework, a multi-scale resource management is established at the cloud center to orchestrate the model production and adaptation pipeline. This controller dynamically coordinates edge-side fine-tuning cycles, cloud model update intervals, and pruning ratio by holistically evaluating multiple cost-performance dimensions The cloud-based control center employs a multi-scale resource management controller to regulate both the model finetuning and incremental learning updates lifecycle. The proposed model lifecycle management framework is illustrated as Fig. 3. We mainly dimensional cost factors include: computational and memory resources for fine-tuning, inference latency and performance, cloud computational and memory overhead for model updates, bandwidth consumption for both incremental data upload and model distribution, the impact of pruning ratio on model accuracy as well as sampling rates of incremental training datasets. Through an actor-critic architecture, the framework dynamically optimizes the fine-tuning cycles, pruning ratio and the cloud update frequency, achieving maximal model performance under predefined resource constraints. Specifically, to account for the dynamic nature of V2X network topologies, we configure the model fine-tuning δfi ne = th m co pa tra co un im ef tu be tu an th fa Based on the aforementioned model fine-tuning and cloud-based incremental learning framework, a multi-scale resource management is established at the cloud center to orchestrate the model production and adaptation pipeline. This controller dynamically coordinates edge-side fine-tuning cycles, cloud model update intervals, and pruning ratio by holistically evaluating multiwhere E ‖∇ F (

model

e

- βt rec

multi-

- ∫

0

1 γ = ϕ bS + ψσ, (1) ‖ 2 ≤ 1 γ . The first term characterizes the baseline constraint intensity of training error through gradient fine-tuning cycles and update cycles. (1) where E | | ∇ F ( w )| | 2  1/ g . The first term characterizes the baseline constraint intensity of training error through gradient smoothness features  , establishing an inverse regulatory relationship pτ to be performed every p the limited effectiveness of a model update window λ update after every k fi ne-tuning rounds. During this window, the model is retrained and updated to ensure the accuracy of locally deployed models. Let δ train = λ + kδfi ne denote the

w

)

to

m

dt

ila

- the

is the performance gain function infl

F

)

(

∆

the model pruning rate

b

. B

Th

ne

) =

·

transmission slots. Considering

σ

and training batch size

DRL to optimize both the fine-tuning efficiency fu

update collaborat pa we establish

model fine-tuning,

that triggers a cloud-based LAM

model update period. The model update window consists of

sample data transmission delay, model pre-training delay, and

function,

efficiency we achieve

lifecycle management efficiency through adaptive

tit

by

m

co

ef

P

-

(

P

0

)

with b and training rounds S . The second term accounts for the model's sensitivity to s , where ψ relates to the changes in weight norms.

The analysis demonstrates that larger training batch sizes and lower pruning rates lead to slower convergence rates, reduced parameter update magnitudes, and accelerated convergence attainment. Consequently, by acquiring the pruning rate and convergence rate, we can calculate both the total training delay and the final parameter count before model distribution The model distribution delay can be calculated based on allocated cloud bandwidth. smoothness features ϕ , establishing an inverse regulatory relationship with b and training rounds S . The second term accounts for the model's sensitivity to σ , where ψ relates to the changes in weight norms. The analysis demonstrates that larger training batch and lower pruning rates lead to slower convergence reduced parameter update magnitudes, and accelerated vergence attainment. Consequently, by acquiring the pruning smoothness features ϕ , establishing an inverse regulatory relationship with b and training rounds S . The second term accounts for the model's sensitivity to σ , where ψ relates to the changes in weight norms. The analysis demonstrates that larger training batch lower pruning rates lead to slower convergence parameter update magnitudes, and accelerated vergence attainment. Consequently, by acquiring the pruning

NE - LARGE AI MODELS FOR COMMUNICATIONS AI MODELS FOR COMMUNICATIONS and reduced rate These edge nodes are responsible for fusing and preliminarily processing the received multi-source heterogeneous data, performing tasks such as redundancy elimination and consistency verification to ensure data integrity and reliability.

ycle management framework

oned model fine-tuning and cloud-

ent framework the

framework, a multi-scale resource

δfi

at the cloud center to orchestrate

l fine-tuning and cloud- the

daptation pipeline. This controller

, a multi-scale resource

dge-side fine-tuning cloud cycles,

pruning ratio by holistically eval-

ud center to orchestrate

pipeline. This controller

ne-tuning

ance dimensions

center employs a multi-scale cycles, cloud

atio by holistically eval-

ler to regulate both the model fine-

ensions throughout

updates

arning

ploys model

del lifecycle management frame-

.

3.

a

multi-scale re-

We mainly account multi-

late both the model fine-

clude: computational and memory

ates throughout model

nference latency and performance,

mory overhead for model updates,

cle management frame-

mainly multi- account

putational and memory

4 4 the fine-tuning efficiency function and update efficiency function, we achieve collaborative model lifecycle management efficiency through adaptive control of fine-tuning cycles and update cycles.

## collAborAtIVe resource MAnAgeMent Model In VehIcle-roAd-cloud systeMs

sizes

sizes

rates,

and

(2) (3) (3) model of perfor(2) marginal (3) (3) During the cloud-layer model training, the system first constructs a global view of the computing power network by aggregating localized state information uploaded by vehicle clusters via edge nodes. This aggregated information is then synthesized into a unified global environment vector, serving as the foundational input for model training. The D-LAM is trained based on pre-sampled sequences in the form of state-action-reward-return tuples. The state space captures the environmental context of the computing network at each time step, incorporating various factors such as computational resource metrics of vehicular terminals and edge nodes, vehicle-RSU positional relationships, and task demand intensity. The action space encompasses all feasible scheduling operations, including task offloading destination selection, allocation of computational and bandwidth resources, interference mitigation, and beam-forming control. The immediate reward quantifies the impact of each scheduling action on overall system performance indicators such as latency, energy efficiency, and through put. Meanwhile, the expected return reflects the cumulative benefit of scheduling over multiple time slots in a dynamic environment. To enhance the model's capability in handling multi-modal input data, independent linear embedding layers are applied to each data modality. In addition, to improve the model's responsiveness for delay-sensitive tasks, a fixed length input sequence window is introduced. This constraint limits the temporal context, encouraging the model to focus on recent history and striking a balance between context modeling capacity and inference latency - thereby improving its realtime applicability and

## sIngle-tAsk scenArIos The length of the model fine-tuning cycle is jointly determined by the fine-tuning cost C fine and model performance P . An exponential function P 0 e -bd fine is used to represent the performance decay degree after the fine-tuning cycle d fine . Considering the specified performance lower bound p rec , the fine-tuning cost consumption involved in a single local model with parameter quantity M includes: 1. Parameter cost , governed by M , fine-tuning parameter ratio and unit parameter cost; 2. Computation cost , determined by M , training duration, hardware cost, and batch size; 3. Memory cost , influenced by the parameter storage coefficient, M and unit storage cost. For different fine-tuning strategies, the model performance improvements vary. We introduce a fine-tuning efficacy factor to quantify the finetuned model performance. The performance gain D P after fine-tuning consists of distribution similarity between incremental data and historical data, learning efficiency coefficient, and fine-tuning efficacy factor. The fine-tuning efficiency function can be expressed as: reconrate and convergence rate, we can calculate both the total training delay and the final parameter count before model distribution The model distribution delay can be calculated based on allocated cloud bandwidth. The length of the model fine-tuning cycle is jointly determined by the fine-tuning cost Cfi ne and model performance P . An exponential function P 0 e -βδfi ne is used to represent the performance decay degree after the fine-tuning cycle δfi ne. Considering the specified performance lower bound p rec , the fine-tuning cost consumption involved in a single local model with parameter quantity M includes: (1) parameter cost , governed by M , fine-tuning parameter ratio and unit parameter cost; (2) computation cost , determined by M , training duration, hardware cost, and batch size; (3) memory cost , influenced by the parameter storage coefficient, M and unit storage cost. For different fine-tuning strategies, the model performance improvements vary. We introduce a fine-tuning efficacy factor to quantify the fine-tuned model performance. The performance gain ∆ P after fine-tuning consists of distribution similarity between incremental data and historical data, learning efficiency coefficient, and fine-tuning efficacy factor. The finetuning efficiency function can be expressed as: rates, conand convergence rate, we can calculate both the total training delay and the final parameter count before model distribution The model distribution delay can be calculated based on allocated cloud bandwidth. The length of the model fine-tuning cycle is jointly determined by the fine-tuning cost Cfi ne and model performance P . An exponential function P 0 e -βδfi ne is used to represent performance decay degree after the fine-tuning cycle ne. Considering the specified performance lower bound p rec , fine-tuning cost consumption involved in a single local model with parameter quantity M includes: (1) parameter cost , governed by M , fine-tuning parameter ratio unit parameter cost; (2) computation cost , determined by M , training duration, hardware cost, and batch size; (3) memory cost , influenced by the parameter storage coefficient, M and unit storage cost. For different fine-tuning strategies, the model performance improvements vary. We introduce a fine-tuning efficacy factor to quantify the fine-tuned model performance. The mance gain ∆ P after fine-tuning consists of distribution simAs illustrated in Fig. 4, this study proposes a collaborative training architecture tailored for vehicle-road-cloud systems within a computing power network-enabled environment. At the vehicle layer, environmental and state information can be collected either by individual agents operating independently or through the collaboration of multiple agents. Regardless of the operational mode, the raw data collected is first transmitted to edge nodes deployed at RSUs. These edge nodes are responsible for fusing and preliminarily processing the received multisource heterogeneous data, performing tasks such as redundancy elimination and consistency verification to ensure data integrity and reliability. Subsequently, the integrated system state information is uploaded in real-time to the cloud platform. Upon receiving the data, the cloud system conducts systematic pre-processing for the training of the LAM, including critical procedures such as data cleansing, compression, and segmentation. For each task category, a corresponding prompt vector is designed and embedded along with the environmental state as input sequences for the D-LAM.

both incremental data upload and

pact ratio pruning on of model

ling rates training of incremental

tency and performance,

rhead for model updates,

-critic architecture, the framework

<!-- formula-not-decoded -->

fine-tuning

emental data upload and

cycles, pruning

uency, ratio model

runing on maximal

achieving

ed resource constraints.

for dynamic nature of V2X

the

of training incremental

itecture, the framework

g

pruning ratio

cycles,

figure the model fine-tuning

p

δfi

ne

transmission

f

slots. Considering

model fine-tuning, we establish

model

maximal

hieving

e constraints.

that triggers a cloud-based LAM

ning rounds. During this window,

nature of V2X

ynamic

updated to ensure the accuracy of

ne

δfi

=

odel fine-tuning

et train kδfi ne

-

=

λ

δ

denote

model update window consists of

- the memory cost , influenced by pruning rate, parameter storage coefficient, M and unit storage cost. 1. Parameter cost , governed by initial training parameter quantity and unit parameter cost; factors including retraining cost and update performance gain. The cost consumed by a single model update consists of: (1)

ssion slots. Considering

ne-tuning, we establish

ers a cloud-based LAM

- Combined with the model update window length, the update efficiency function can be expressed as: 2. Computation cost , determined by M , training duration, hardware cost and batch size; parameter cost , governed by initial training parameter quantity and unit parameter cost; (2) computation cost , determined

elay, model pre-training delay, and

he between relationship

g rate training

σ

, and convergence rate

ds. During this window,

ensure the accuracy of

n upper bound on the average L2-

λ

-

kδfi

- γ , η train ( δ train , σ ) = C train + λ δ train -∆ F ( σ, b ) 3. Memory cost , influenced by pruning rate, parameter storage coefficient, M and unit storage cost. by M , training duration, hardware cost and batch size; memory cost , influenced by pruning rate, parameter storage

ne denote the

ate window consists of

ϕ

bS

ψσ,

-

l pre-training delay, and

nship training The the between first characterizes term

of training error through gradient

(1) where ∆ F ( · ) is the performance gain function influenced by the model pruning rate σ and training batch size b . By applying DRL to optimize both the fine-tuning efficiency function and Combined with the model update window length, the update efficiency function can be expressed as: coefficient, M and unit storage cost. Combined with the model update window length, the update efficiency function can be expressed as:

update function, we achieve collaborative efficiency

<!-- formula-not-decoded -->

and convergence rate

γ

,

und on the average L2-

,

(1)

term characterizes the

g error through gradient where ∆ F ( · ) is the performance gain function influenced by the model pruning rate σ and training batch size b . By applying DRL to optimize both the fine-tuning efficiency function and update efficiency function, we achieve collaborative model where D F (  ) is the performance gain function influenced by the model pruning rate s and training batch size b . By applying DRL to optimize both lifecycle management efficiency through adaptive control fine-tuning cycles and update cycles.

of

ratio

model

= benefits of fine-tuning operations diminish. When the finetuning gain falls below a threshold, a cloud-based LAM update and subsequent local redeployment are required. The setting of the model update cycle primarily considers multi-dimensional factors including retraining cost and update performance gain. The cost consumed by a single model update consists of: (1) parameter cost , governed by initial training parameter quantity and unit parameter cost; (2) computation cost , determined by M , training duration, hardware cost and batch size; After multiple rounds of model fine-tuning, the marginal benefits of fine-tuning operations diminish. When the fine-tuning gain falls below a threshold, a cloud-based LAM update and subsequent local redeployment are required. The setting of the model update cycle primarily considers multi-dimensional factors including retraining cost and update performance gain. The cost consumed by a single model update consists of: ηfi ne ( δfi ne ) = Cfi ne δfi ne + ∫ δfi ne 0 ( P 0 e -βt -P rec ) dt -∆ P After multiple rounds of model fine-tuning, the benefits of fine-tuning operations diminish. When the finetuning gain falls below a threshold, a cloud-based LAM update and subsequent local redeployment are required. The setting of the model update cycle primarily considers multi-dimensional Ieee Communications Magazine - lArge AI

Models For Communications

<!-- image -->

Fig. 4.

or The entire training process is conducted in an auto-regressive manner, where the output at each time step is fed into the subsequent time step as part of the input. Upon completion of the training phase, the model undergoes lightweight compression techniques such as pruning and knowledge distillation to reduce its computational footprint. Furthermore, few-shot fine-tuning is performed in local environments using a small set of task-specific samples, thereby producing task-adaptive local scheduling models. These models support low-latency and high-efficiency resource scheduling under the collaborative vehicle-road-cloud architecture. of the operational mode, the raw data collected is first transmitted to edge nodes deployed at RSUs. These edge nodes are responsible for fusing and preliminarily received multi-source heterogeneous data, such as redundancy elimination and consistency verification to ensure data integrity and reliability. integrated system state information is to the cloud platform. Upon receiving the data, system conducts systematic pre-processing for the training of the LAM, including critical procedures such as data cleansing, compression, and segmentation. For each task

FIGURE 4. Collaborative training architecture between large and lightweight models in vehicle-road-cloud systems. Collaborative training architecture between large and lightweight models in vehicle-road-cloud systems

deployment efficiency. Subsequently, a policy generation head maps the attention outputs into a concrete resource scheduling policy vector, specifying the current computing path and resource allocation decisions. To achieve short-term system utility maximization under multi-dimensional communication resource constraints, this study incorporates both task inference accuracy and delay penalty into the reward function design. As illustrated in Fig. 4, the short-term utility function is modeled as the logarithm of the ratio between inference accuracy and task completion time at each communication time slot t, weighted by a trade-off parameter reflecting system gain versus cost. III. C OLLABORATIVE RESOURCE MANAGEMENT MODEL IN VEHICLE -ROAD-CLOUD SYSTEMS A. Single-T ask Scenarios As illustrated in Fig. 4, this study proposes a collaborative training architecture tailored for vehicle-road-cloud systems within a computing power network-enabled environment. At the vehicle layer, environmental and state information can be collected either by individual agents operating independently through the collaboration of multiple agents.

Compared to traditional RL approaches (e.g., value function approximation), D-LAM demonstrates significant advantages in handling large-scale historical trajectories and high-dimensional state spaces. Leveraging its auto-regressive sequence modeling capability, D-LAM captures temporal dependencies more effectively, generating more robust and generalizable scheduling policies, thereby enabling better adaptation to complex V2X scenarios and enhancing overall service quality and resource utilization efficiency. corresponding prompt vector is designed and embedded along with the environmental state as input sequences for LAM. During the cloud-layer model training, the constructs a global view of the computing power network by aggregating localized state information uploaded by vehicle clusters via edge nodes. This aggregated information is then synthesized into a unified global environment vector, serving

as

is the foundational trained based input for

## MultI-tAsk scenArIos In the vehicle-road-cloud collaborative computing network environment, vehicles often need to execute multiple tasks in parallel, such as realtime perception, behavior prediction, path planning, local map construction, and model updates. These tasks significantly differ in terms of time sensitivity, computational complexity, and collaboration requirements. Thus, there is an urgent need to develop a multi-task management architecture that integrates task recognition, dynamic scheduling, and collaboration capabilities. action space encompasses all feasible scheduling operatio including task offfioading destination selection, allocation computational and bandwidth resources, interference miti tion, and beam-forming control. The immediate reward qua tifies the impact of each scheduling action on overall syste performance indicators such as latency, energy efficien and through put. Meanwhile, the expected return reffiects cumulative benefit of scheduling over multiple time slots i

RSU positional relationships, and task demand intensity. Th To address these needs, this article proposes a DM-LAM to achieve multi-task resource management based on LAMs. By leveraging the powerful learning capabilities of LAM, the method optimizes task scheduling and resource allocation, enabling efficient decision-making in concurrent multi-tasking scenarios. The DM-LAM frames the resource scheduling process as a sequential decision-making task with long-term dependencies. Different tasks exhibit distinct resource utilization patterns, such as computation, communication, and caching, during execution. As a result, the method introduces a specialized expert network within the LAM architecture and implements dynamic expert scheduling through a task feature-driven gating mechanism. This approach offers differentiated resource optimization paths for various task types. For tasks with high computational loads, the DM-LAM uses an expert selection mechanism to prioritize nodes with computational advantages. It dynamically determines whether to perform local processing, collaborate at the edge, or offload to the cloud, considering the task's data scale and communication overhead. For communication-sensitive tasks, the model prioritizes expert strategies with low-latency transmission capabilities and adjusts communication paths based on real-time channel Regardless processing the performing tasks Subsequently, the uploaded in real-time the cloud category, a the Dsystem first a dynamic environment. To enhance the model's capability handling multi-modal input data, independent linear embe ding layers are applied to each data modality. In addition, improve the model's responsiveness for delay-sensitive task a fixed length input sequence window is introduced. Th constraint limits the temporal context, encouraging the mo to focus on recent history and striking a balance betwe context modeling capacity and inference latency-there improving its realtime applicability and deployment efficienc Subsequently, a policy generation head maps the attenti outputs into a concrete resource scheduling policy vect specifying the current computing path and resource allocati decisions. To achieve short-term system utility maximizatio under multi-dimensional communication resource constrain this study incorporates both task inference accuracy and del penalty into the reward function design. As illustrated in Fig 4, the short-term utility function is modeled as the logarith of the ratio between inference accuracy and task complet time at each communication time slot t, weighted by a tra off parameter reffiecting system gain versus cost.

model training. The D-LAM

on pre-sampled sequences in the form of The entire training process is conducted in an aut regressive manner, where the output at each time step is f

state-action-reward-return tuples. The state space captures the

into the subsequent time step as part of the input. Upon co

5

AZINE - LARGE AI MODELS FOR COMMUNICATIONS

erformed in local environments using ific samples, thereby producing taskg models. These models support lowncy resource scheduling under the d-cloud architecture. al RL approaches (e.g., value funcAM demonstrates significant advanscale historical trajectories and highs. Leveraging its auto-regressive seity, D-LAM captures temporal depenThis article addresses the challenges of coordination and dynamic resource adaptation faced by the integration of LAMs in vehicle-road-cloud collaborative systems.

, generating more robust and general-

s, thereby enabling better adaptation

rios and overall enhancing service

ization efficiency.

oud collaborative computing network

ten need to execute multiple tasks in

e perception, behavior prediction, path

struction, and model updates. These

in terms of time sensitivity, computa-

llaboration requirements. Thus, there

elop a multi-task management archi-

sk recognition, dynamic scheduling,

lities.

ds, this paper proposes a DM-LAM

ource management based on LAMs.

erful learning capabilities

ask of LAM, scheduling alloca- resource and

ecision-making in concurrent multi-

M-LAM frames the resource schedul-

tial decision-making task with long-

erent resource exhibit distinct tasks

as computation, communication, and

n. As a result, the method introduces

ork within the LAM architecture and

ert scheduling through a task feature-

. This approach offers differentiated

ths for various task types. For tasks

loads, the DM-LAM uses an expert

prioritize nodes with computational

lly determines whether to perform lo-

te at the edge, or offload to the cloud,

ta scale and communication overhead.

itive the model prioritizes ex- tasks,

latency transmission capabilities and

aths based on real-time channel con-

l task selection across multiple paths,

For tasks data involving large-scale

DM-LAM utilizes an expert routing

atch nodes with caching advantages or

ities, enabling coordinated scheduling

ing. Additionally, the DM-LAM takes

rce disparities among heterogeneous

network. In scenarios where multiple

sly, it global dynamically balances

local task optimization. In resource-

s, the model actively selects real-time ing multiple between enables dynamic conflicts multi-task interaction vehicle-road-cloud in reliable scheme.

FIGURE 5. Performance comparison in dynamic V2X scenario. Fig. 5. Performance comparison in dynamic V2X scenario IEEE COMMUNICATIONS MAGAZINE - LARGE AI MODELS FOR COMMUNICATIONS

<!-- image -->

scenarios through a model lifecycle management FIGURE 6. Performance comparison in various scenario. Fig. 6. Performance comparison in various scenario

<!-- image -->

The simulation focuses on a V2X scenario with single RSU

performance perception:

PPO, and random selection.

vehicles

cooperative

DT,

to are

compared

multi-vehicle

assisted

conditions, ensuring optimal task selection across multiple paths, such as V2V and V2I. For tasks involving large-scale data caching and forwarding, DM-LAM utilizes an expert routing mechanism to flexibly match nodes with caching advantages or data pre-fetching capabilities, enabling coordinated scheduling of computation and caching. Additionally, the DM-LAM takes full advantage of resource disparities among heterogeneous nodes in the computing network. In scenarios where multiple tasks arrive simultaneously, it dynamically balances global resource scheduling with local task optimization. In resource-constrained environments, the model actively selects real-time responses for high-priority tasks based on task priority, delay sensitivity, and resource consumption characteristics. randomly distributed within a 150 meters radius of a fixed RSU, with speeds ranging from 20 to 60 km/h . Both the vehicles and the RSU are equipped with 32GB of memory, and the bandwidth between them is set to 50-100 Mbps. A resource allocation strategy dataset is constructed using the proximal policy optimization (PPO) algorithm. Specifically, the state space incorporates the varying number of vehicles, their positions and speeds relative to the RSU, vehicle-to-RSU CSI, and available RSU computing resources. The action space consists of data upload bandwidth and inference compute resource allocation strategies. The reward function comprehensively considers communication and computation resource utilization alongside task latency. The dataset is divided into pre-training ( 60% ), fine-tuning ( 30% ), and evaluation ( 10% ) subsets based on vehicle count variations. Experiments are conducted on NVIDIA A6000 GPU. The Moreover, the results indicate that our method effectively recalibrates model performance in response to dynamic scenario changes, ensuring reliable inference. This is attributed to the adaptive fine-tuning cycles and update cycles in our framework, which promptly stabilize inference performance through model adjustments when significant scenario shifts occur. To validate the model's generalization capacity, we conducted the experiment under diverse scenarios with varying vehicle numbers. As illustrated in Fig. 6, while DT and PPO exhibited significant degradation of task completion rates with increasing vehicle numbers, our model demonstrated consistent stability and maintained higher performance through lifecycle management scheme. The experimental results show that our approach achieves approximately 10 ± 1.2 % higher task completion rates compared to DT, which substantiates the generalization capability of the proposed method in com-

dom selection baselines by simulating time-varying scenario The DM-LAM can dynamically optimize resource scheduling strategies in complex vehicle-road-cloud collaborative environments, tailoring solutions to the varying demands of multiple tasks. It effectively coordinates resource conflicts between tasks, providing an efficient and stable multi-task resource management solution. LAM is built upon Qwen2.5-14b, integrated with task-specific feature extraction modules and prompt engineering. Both pre-training and fine-tuning (with LoRA rank=16, alpha=64) phases employ the AdamW optimizer, using a batch size of 64. The pre-training learning rate is set to 5 × 10 -5 , while the fine-tuning learning rate is reduced to 1 × 10 -5 . We compare the proposed method with DT, PPO, and ranplex dynamic environments. This improvement is primarily attributed to the adaptive fine-tuning cycles that enable realtime model adaptation. V. CONCLUSION This paper addresses the challenges of coordination and dynamic resource adaptation faced by the integration of LAMs

in proposes utilization an

dynamics Based on the proposed architecture, the developed method enables reliable interaction in dynamic vehicle-road-cloud scenarios through a model lifecycle management scheme. The simulation focuses on a V2X scenario with single RSU assisted multi-vehicle cooperative perception: vehicles are randomly distributed within a 150 meters radius of a fixed RSU, with speeds ranging from 20 to 60 km/h. Both the vehicles and the RSU are equipped with 32GB of memory, and the bandwidth between them is set to 50-100 Mbps. A resource allocation strategy dataset is constructed using the proximal policy optimization (PPO) algorithm. changes achieved by different resource allocation schemes. As shown in Fig. 5, the proposed model demonstrates superior agent-based network architecture and resource management method. Through large-scale pre-training in the cloud and lightweight model deployment at the edge, real-time inference and decision-making are achieved. Additionally, the lifecycle management method proposed in this paper jointly optimizes the sampling rate, model pruning, and resource allocation, effectively balancing model performance with resource consumption. The use of multi-dimensional resource management models effectively supports resource coordination and personalized scheduling in both single-task and multi-task scenarios. Experimental results validate the feasibility of the proposed method. VI. ACKNOWLEDGMENT This work was supported by the National Key Re-

## nuMerIcAl results And AnAlysIs in the dataset to evaluate the resource vehicle-road-cloud collaborative systems. It

search China of under Program Development Grant and

2024YFE0200300, the National Natural Science Foundation of

6

7

Specifically, the state space incorporates the varying number of vehicles, their positions and speeds relative to the RSU, vehicle-to-RSU CSI, and available RSU computing resources. The action space consists of data upload bandwidth and inference compute resource allocation strategies. The reward function comprehensively considers communication and computation resource utilization alongside task latency. The dataset is divided into pre-training (60%), fine-tuning (30%), and evaluation (10%) subsets based on vehicle count variations. Experiments are conducted on NVIDIA A6000 GPU. The LAM is built upon Qwen2.5-14b, integrated with task-specific feature extraction modules and prompt engineering. Both pre-training and fine-tuning (with LoRA rank = 16, a = 64) phases employ the AdamW optimizer, using a batch size of 64. The pre-training learning rate is set to 5  10 -5 , while the fine-tuning learning rate is reduced to 1  10 -5 . China under Grant 61931005, and the Fundamental Research Funds for the Central Universities under Grant 2025TSQY05. REFERENCES

,

To validate the model's generalization capacity, we conducted the experiment under diverse scenarios with varying vehicle numbers. As illustrated in Fig. 6, while DT and PPO exhibited significant degradation of task completion rates with increasing vehicle numbers, our model demonstrated consistent stability and maintained higher performance through lifecycle management scheme. The experimental results show that our approach achieves approximately 10±1.2% higher task completion rates compared to DT, which substantiates the generalization capability of the proposed method in complex dynamic environments. This improvement is primarily attributed to the adaptive fine-tuning cycles that enable real-time model adaptation. network with vehicular cloud computing and remote cloud computing,' Sensors , vol. 20, no. 23, p. 6820, Nov. 2020. [8] M. Xu, D. Niyato, J. Kang, Z. Xiong, S. Mao, Z. Han, D. I. Kim, and K. B. Letaief, 'When Large Language Model Agents Meet 6G Networks: Perception, Grounding, and Alignment,' in IEEE Wireless Communications , vol. 31, no. 6, pp. 63-71, Dec. 2024. [9] J. Du, T. Lin, C. Jiang et al ., 'Distributed Foundation Models for Multi-Modal Learning in 6G Wireless Networks,' IEEE Wireless Communications , vol. 31, no. 3, pp. 20-30, Jun. 2024. [10] Z. Chen, H. H. Yang, Y. Tay et al ., 'The Role of Federated Learning in a Wireless World with Foundation Models,' IEEE Wireless Communications , vol. 31, no. 3, pp. 42-49, Jun. 2024. [11] R. Zhang, K. Xiong, H. Du, D. Niyato, J. Kang, X. S. Shen, and H. V. Poor, 'Generative AI-enabled vehicular networks: Fundamentals, framework, and case study,' IEEE Network , vol. 38, no. 4, pp. 259-267, Jul. 2024. [12] F. Jiang, Y. Liu, L. Dong, C. Pan, and X. You, 'Large language model enhanced multi-agent systems for 6G communications,' in IEEE Wireless Communications , vol. 31, no. 6, pp. 48-55, Dec. 2024. [13] J. Zhang, J. Li, Z. Wang, L. Shi, S. Jin, W. Chen, and H. V. Poor, 'Decision transformers for wireless communications: A new paradigm of We compare the proposed method with DT, PPO, and random selection baselines by simulating time-varying scenario dynamics in the dataset to evaluate the resource utilization changes achieved by different resource allocation schemes. As shown in Fig. 5, the proposed model demonstrates superior performance compared to DT, PPO, and random selection. Moreover, the results indicate that our method effectively recalibrates model performance in response to dynamic scenario changes, ensuring reliable inference. This is attributed to the adaptive fine-tuning cycles and update cycles in our framework, which promptly stabilize inference performance through model adjustments when significant scenario shifts occur. [1] J. Zhao, W. Zhao, B. Deng, Z. Wang, F. Zhang, W. Zheng, W. Cao, J. Nan, Y. Lian, and A. F. Burke, 'Autonomous driving system: A comprehensive survey,' Expert Systems with Applications , vol. 242, p. 122836, 2024. [2] F. Qu, F. Du, and L. Zong, 'Design and construction of cloud data platform for intelligent connected vehicles,' in Proc. 2024 Int. Conf. Smart City and Information System (ICSCIS) , New York, NY, USA: ACM, 2024, pp. 397-401. [3] Q. Cui, X. You, N. Wei, et al., 'Overview of AI and communication for 6G network: fundamentals, challenges, and future research opportunities,' Sci. China Inf. Sci. , vol. 68, art. 171301, 2025. [4] W. Wu, C. Zhou, M. Li, H. Wu, H. Zhou, N. Zhang, X. S. Shen, and W. Zhuang, 'AI-Native Network Slicing for 6G Networks,' in IEEE Wireless Communications , vol. 29, no. 1, pp. 96-103, Feb. 2022. [5] Z. Chen, Q. Sun, N. Li, X. Li, Y. Wang and C. -L. I, 'Enabling Mobile AI Agent in 6G Era: Architecture and Key Technologies,' in IEEE Network vol. 38, no. 5, pp. 66-75, Sept. 2024. [6] H. Choi, Y. Lee, G. Kim, E. Lee, and Y. Nam, 'Resource cluster-based resource search and allocation scheme for vehicular clouds in vehicular ad hoc networks,' Sensors , vol. 24, no. 1, 2024. [7] S. Xu and C. Guo, 'Computation offloading in a cognitive vehicular

resource management,'

pp. 180-186, Apr. 2025.

This article addresses the challenges of coordination and dynamic resource adaptation faced by the integration of LAMs in vehicle-road-cloud collaborative systems. It proposes an agent-based network architecture and resource management method. Through large-scale pre-training in the cloud and lightweight model deployment at the edge, real-time inference and decision-making are achieved. Additionally, the lifecycle management method proposed in this article jointly optimizes the sampling rate, model pruning, and resource allocation, effectively balancing model performance with resource consumption. The use of multi-dimensional resource management models effectively supports resource coordination and personalized scheduling in both single-task and multi-task scenarios. Experimental results validate the feasibility of the proposed method. [14] Y. Nan, S. Jiang, and M. Li, 'Large-scale video analytics with cloud-edge collaborative continuous learning,' ACM Transactions on Sensor Networks , vol. 20, no. 1, pp. 1-23, Oct. 2023. [15] S. Liu, G. Yu, R. Yin, J. Yuan and F. Qu, 'Adaptive Batchsize Selection and Gradient Compression for Wireless Federated Learning,' GLOBECOM 2020 - 2020 IEEE Global Communications Conference, Taipei, Taiwan, 2020, pp. 1-6, doi: 10.1109/GLOBECOM42002.2020.9322122. Xinxin He (hxx 9000@bupt.edu.cn) is currently an Associate Professor with Beijing University of Posts and Telecommunications (BUPT) and the Beijing Key Laboratory of Network System Architecture and Convergence, China. She is a Member of IEEE. Yang Yang (sherry yangyang@bupt.edu.cn) is currently pursuing the M.S. degree at Beijing University of Posts and Telecommunications, China. Zhiyong Yang (yangzhiyong@bupt.edu.cn) is currently pursuing the M.E. degree at Beijing University of Posts and Telecommunications, China. Yifei Gao (yifeigao@bupt.edu.cn) is currently pursuing the M.S. degree at Beijing University of Posts and Telecommunications, China. Changchuan Yin (ccyin@bupt.edu.cn) is currently a Professor with School of Information and Communication Engineering at BUPT. He was the co-recipient of the IEEE Marconi Prize Paper Award in 2023 and the IEEE International Conference on Wireless Communications and Signal Processing Best Paper Award in 2009. He is a Senior Member of IEEE. Shanzhi Chen (chensz@cict.com) is currently the CTO and EVP of R&amp;D at

## conclusIon IEEE Wireless Communications

32, no. 2,

the China Information and Communication Technology Group Co., Ltd. (CICT),

the Director of the State Key Laboratory of Wireless Mobile Communications,

and a Board Director of SMIC. He is a Fellow of IEEE.

,

vol.

## AcknoWledgMent This work was supported by the National Key Research and Development Program of China under Grant 2024YFE0200300, the National Natural Science Foundation of China under Grant 61931005, and the Fundamental Research Funds for the Central Universities under Grant 2025TSQY05.

## reFerences

- [1] J. Zhao et al. , 'Autonomous Driving System: A Comprehensive Survey,' Expert Systems with Applications , vol. 242, 2024, p. 122836.
- [2] F. Qu, F. Du, and L. Zong, 'Design and Construction of Cloud Data Platform for Intelligent Connected Vehicles,' Proc. 2024 Int'l. Conf. Smart City and Information System (ICSCIS) , New York, NY, USA: ACM, 2024, pp. 397-401.
- [3] Q. Cui et al. , 'Overview of AI and Communication for 6G Network: Fundamentals, Challenges, and Future Research Opportunities,' Sci. China Inf. Sci. , vol. 68, art. 171301, 2025.
- [4] W. Wu et al. , 'AI-Native Network Slicing for 6G Networks,' IEEE Wireless Commun. , vol. 29, no. 1, Feb. 2022, pp. 96-103.
- [5] Z. Chen et al. , 'Enabling Mobile AI Agent in 6G Era: Architecture and Key Technologies,' IEEE Network , vol. 38, no. 5, Sept. 2024, pp. 66-75.
- [6] H. Choi et al. , 'Resource Cluster-Based Resource Search and Allocation Scheme for Vehicular Clouds in Vehicular Ad Hoc Networks,' Sensors , vol. 24, no. 1, 2024.
- [7] S. Xu and C. Guo, 'Computation Offloading in A Cognitive Vehicular Network with Vehicular Cloud Computing and Remote Cloud Computing,' Sensors , vol. 20, no. 23, p. 6820, Nov. 2020.
- [8] M. Xu et al. , 'When Large Language Model Agents Meet 6G Networks: Perception, Grounding, and Alignment,' IEEE Wireless Commun. , vol. 31, no. 6, Dec. 2024, pp. 63-71.
- [9] J. Du et al. , 'Distributed Foundation Models for Multi-Modal Learning in 6G Wireless Networks,' IEEE Wireless Commun. , vol. 31, no. 3, Jun. 2024, pp. 20-30.
- [10] Z. Chen et al. , 'The Role of Federated Learning in a Wireless World with Foundation Models,' IEEE Wireless Commun. , vol. 31, no. 3, June 2024, pp. 42-49.
- [11] R. Zhang et al. , 'Generative AI-Enabled Vehicular Networks: Fundamentals, Framework, and Case Study,' IEEE Network , vol. 38, no. 4, July 2024, pp. 259-67.
- [12] F. Jiang et al. , 'Large Language Model Enhanced MultiAgent Systems for 6G Communications,' IEEE Wireless Commun. , vol. 31, no. 6, Dec. 2024, pp. 48-55.
- [13] J. Zhang et al. , 'Decision Transformers for Wireless Communications: A New Paradigm of Resource Management,' IEEE Wireless Commun. , vol. 32, no. 2, Apr. 2025, pp. 180-86.
- [14] Y. Nan, S. Jiang, and M. Li, 'Large-Scale Video Analytics with Cloud-Edge Collaborative Continuous Learning,' ACM Trans. Sensor Networks , vol. 20, no. 1, Oct. 2023, pp. 1-23.
- [15] S. Liu et al. , 'Adaptive Batchsize Selection and Gradient Compression for Wireless Federated Learning,' GLOBECOM 2020 - 2020 IEEE Global Commun. Conf. , Taipei, Taiwan, 2020, pp. 1-6. DOI: 10.1109/GLOBECOM42002.2020.9322122.

## bIogrAPhIes XinXin He [M] (hxx\_9000@bupt.edu.cn) is currently an Associate Professor with Beijing University of Posts and Telecommunications (BUPT) and the Beijing Key Laboratory of Network System Architecture and Convergence, China.

Yang Yang (sherry\_yangyang@bupt.edu.cn) is currently pursuing the M.S. degree at Beijing University of Posts and Telecommunications, China.

ZHiYong Yang (yangzhiyong@bupt.edu.cn) is currently pursuing the M.E. degree at Beijing University of Posts and Telecommunications, China.

Yifei gao (yifeigao@bupt.edu.cn) is currently pursuing the M.S. degree at Beijing University of Posts and Telecommunications, China.

CHangCHuan Yin [SM] (ccyin@bupt.edu.cn) is currently a Professor with the School of Information and Communication Engineering at BUPT. He was the co-recipient of the IEEE Marconi Prize Paper Award in 2023 and the IEEE International Conference on Wireless Communications and Signal Processing Best Paper Award in 2009.

SHanZHi CHen [F] (chensz@cict.com) is currently the CTO and EVP of R&amp;D at China Information and Communication Technology Group Co., Ltd. (CICT), the Director of the State Key Laboratory of Wireless Mobile Communications, and a Board Director of SMIC.
