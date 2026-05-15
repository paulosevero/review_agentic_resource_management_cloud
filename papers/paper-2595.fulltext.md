---
paper_id: "paper-2595"
source_pdf_sha: "07db8b7fbec93cec816e57ceb076d020e1b964da4fd501e91b796a809d2307ac"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 5
  page_count: 8
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2595 — fulltext
## §unknown-1

IEEE Communications Magazine • April 2026
34
0163-6804/26/$25.00 © 2026 IEEE
AbstrAct
Large artificial intelligence models (LAMs) have 
introduced new opportunities to 6G networks, 
whereas their integration into vehicle-road-cloud 
collaborative systems remains challenging due to 
insufficient model coordination and difficulties in 
dynamic resource adaptation. To address these 
issues, this article proposes an agent-based net-
work architecture and a resource management 
method for vehicle-road-cloud collaboration. In 
this architecture, the cloud agent conducts large-
scale pre-training to characterize global resource 
allocation dynamics, while lightweight models 
are deployed at the road-side unit (RSU) agent 
and vehicle agent to enable real-time inference 
and decision-making. To balance model perfor-
mance and resource consumption, we introduce 
a lifecycle management strategy for the agent 
network. By analyzing the relationship between 
performance gain and the consumption of com-
munication and computation resources, we joint-
ly optimize training data sampling rates, model 
pruning ratio, and resource allocation strategies. 
This enables dynamic adjustment of the update 
frequency for cloud-based large models and 
the fine-tuning frequency for edge-side models, 
thereby ensuring continuous and high-efficiency 
model inference in resource-constrained dynam-
ic scenarios. Additionally, we design a decision 
LAM (D-LAM) for single-task scenarios, which 
employs sequence modeling and temporal 
embedding to achieve dynamic coordination of 
multi-dimensional resources. We further develop 
a decision multi-task LAM (DM-LAM) to address 
complex multi-task scenarios, which integrates 
a mixture-of-experts (MoE) mechanism with a 
gating network to support both personalized 
resource allocation for individual tasks and global 
optimization across heterogeneous tasks. Exper-
imental results demonstrate that the proposed 
method significantly improves resource utilization 
efficiency and achieves 10±$1.2% higher task 
completion rates compared to decision trans -
former model.

## § Introduction

Autonomous driving is an emerging technologi -
cal industry that deeply integrates next-generation 
information technologies and artificial intelligence 
(AI) with intelligent vehicles. It has become a crit -
ical direction for the development of smart trans-
portation and smart cities, which is a key strategic 
focus worldwide [1]. With the development of Vehi-
cle-to-Everything (V2X) technology, the integrated 
vehicle-road-cloud collaborative architecture, which 
enables seamless coordination among vehicles, 
roadside infrastructure, and cloud services through 
interconnected technologies, is opening up new 
possibilities for intelligent transportation. Moreover, 
it is widely recognized as a necessary pathway 
toward achieving fully autonomous driving [2].
With the advent of the 6G era, integrating AI 
into network ecosystems and constructing native-
ly intelligent agent-based networks has become 
a widely recognized goal in both academia and 
industry [3–5]. Within the vehicle-road-cloud col-
laborative architecture, significant heterogeneity 
exists in computing capabilities and data latency 
among vehicles, edge servers, and cloud platforms. 
This necessitates task-oriented and adaptive coor -
dination of multi-dimensional resources, including 
sensing, communication, computation, and AI 
models. Currently, research on agent-based sys -
tem architectures and resource management for 
vehicle-road-cloud collaboration remains in early 
stages. The authors in [6] proposed a resource 
cluster-based search and allocation scheme that 
enables inter-cluster resource discovery for multi-di-
mensional resource types, aiming to improve allo -
cation efficiency and adaptability in highly dynamic 
environments. In [7], a sense-and-utilize approach 
was adopted to model the distribution of compu-
tational resources, and a decentralized multi-agent 
deep reinforcement learning (DRL) algorithm was 
introduced to address collaborative task offloading 
in vehicular cloud computing. While these studies 
provide preliminary solutions to the resource allo-
cation challenges under vehicle-road-cloud archi-
tectures, their effectiveness heavily relies on strict 
assumptions about application scenarios. Once 
Xinxin He, Yang Yang, Zhiyong Yang, Yifei Gao, Changchuan Yin, and Shanzhi Chen
Xinxin He is with Beijing University of Posts and Telecommunications (BUPT) and the Beijing Key Laboratory of Network System Archi-
tecture and Convergence, China; Yang Yang, Zhiyong Yang, and Yifei Gao are with Beijing University of Posts and Telecommunications, 
China; Changchuan Yin is with the School of Information and Communication Engineering at BUPT, China; Shanzhi Chen is with China 
Information and Communication Technology Group Co., Ltd. (CICT), China.Digital Object Identifier: 10.1109/MCOM.001.2500421
Agent-Based Network Architecture 
and Resource Management for 
Vehicle-Road-Cloud Collaboration
LARGE AI MODEL FOR COMMUNICATIONS
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
35
the environmental state changes, the designed 
strategies often fail to generalize or transfer to new 
contexts. Furthermore, traditional reinforcement 
learning (RL), which relies on the Bellman equation 
for iterative value updates, is prone to instability 
under sparse reward conditions or noisy signals.
Against this backdrop, the emergence of power-
ful large artificial intelligence models (LAMs), such 
as ChatGPT, LLaMA, DeepSeek, and Gemini, has 
created transformative opportunities to enhance the 
performance and interactivity of 6G networks [8]. 
In native AI-driven wireless systems, LAMs possess 
cognitive capabilities such as perception, analogy, 
and reasoning, enabling them to rapidly emulate 
communication environments. This enables effi -
cient generalization and adaptation to unforeseen 
scenarios while supporting personalized services 
[9–11]. Recent academic efforts have explored 
the integration of LAMs into 6G networks, yield-
ing early-stage designs for communication-orient-
ed LAM architectures and novel wireless network 
frameworks. For instance, [12] proposes a LAM 
multi-agent communication framework to enhance 
intelligent decision-making and resource schedul-
ing among agents in 6G environments. In [13], the 
decision transformer (DT) model is introduced for 
wireless resource management, addressing challeng-
es such as long-term credit assignment and sequen-
tial decision modeling. Reference [14] presents a 
cloud-edge collaborative architecture. By jointly 
considering retraining frequency in the cloud and 
inference frame rates at the edge, it achieves gradi-
ent-based resource allocation to optimize inference 
accuracy. Despite the promising potential of LAMs 
in communication networks, significant challenges 
remain in developing LAM-enabled intelligent agent 
systems for wireless scenarios. At the system coor-
dination perspective, there is a lack of mechanism 
design for the collaboration between LAMs and 
lightweight communication models, including stan-
dard evaluation metrics for agent networks, adaptive 
update scheduling across cloud-edge-end hierar-
chies, and balancing trade-offs between model per-
formance and resource consumption in the cloud. 
Moreover, cloud-edge collaborative intelligent net-
works must support diverse vehicular communica-
tion patterns, including both vehicle-to-infrastructure 
(V2I) communication and vehicle-to-vehicle (V2V). 
At the model perspective, the deep integration of 
general-purpose large models with knowledge spe-
cific to layered communication network architec-
tures remains inadequate. It is necessary to further 
explore sequential decision-making models that 
align with the scheduling characteristics of commu-
nication and computing resources, as well as joint 
strategies for multi-task resource coordination in 
dynamic vehicular environments.
To address the above challenges, this article 
proposes a three-layer agent-based vehicle-road-
cloud collaborative architecture that integrates 
large and lightweight models, along with a corre-
sponding performance evaluation methodology. 
In addition, a dual-loop resource management 
framework is introduced. In the outer loop, a hier-
archical model lifecycle management strategy is 
designed for the networked system. In the inner 
loop, multi-dimensional resource management 
models for single-task and multi-task scenarios are 
designed respectively. The main contributions of 
this work are as follows:
•
 This article proposes an agent-based vehicle-
road-cloud collaborative network architecture, 
which enables efficient collaborative training
 
and real-time inference through pre-training 
cloud-based LAM and deploying lightweight, 
pruned models at the edge. 
•
 A
 model lifecycle management method for 
agent networks is introduced. By comprehen-
sively considering pre-training costs, fine-tuning 
costs, and inference performance, the method 
dynamically adjusts the update of cloud-based 
LAM, the fine-tuning of edge-base models, and 
the pruning strategy, ensuring continuous and 
efficient inference in V2X scenarios.
•
 Thi
s article proposes a decision LAM (D-LAM)-
based resource management method in sin-
gle-task V2X scenarios. A sequence modeling 
framework with temporal embedding is devel-
oped to model multi-dimensional resource 
coordination as a sequential prediction task. For 
multi-task scenarios, a decision multi-task LAM 
(DM-LAM) with a mixture-of-experts (MoE) 
mechanism is proposed, which enables person-
alized and globally coordinated resource alloca-
tion across heterogeneous tasks through expert 
selection and gating, improving generalization 
and adaptability in dynamic environments.
The remainder of this article is organized as fol-
lows. We first introduces a collaborative frame-
work between large and lightweight models in 
vehicle-road-cloud systems, along with the model 
lifecycle management strategy. Then we presents a 
resource management method based on LAM for 
both single-task and multi-task scenarios, followed 
by simulation analysis and concluding remarks.
VehIcle -roAd -cloud  ArchItecture  WIth  lArge -
lIghtWeIght  AI Model  collAborAtIon
The proposed vehicle-road-cloud architecture with 
large-lightweight model collaboration is illustrated 
in Fig. 1. This framework supports various wireless 
communication applications in both V2V and V2I, 
such as vehicle cooperative perception, vehicle-in-
frastructure coordination, and autonomous driving. 
FIGURE 1. Vehicle-road-cloud architecture with large-lightweight AI model collaboration.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 2
frame rates at the edge, it achieves gradient-based resource
allocation to optimize inference accuracy. Despite the promis-
ing potential of LAMs in communication networks, signifi-
cant challenges remain in developing LAM-enabled intelligent
agent systems for wireless scenarios. At the system coordi-
nation perspective, there is a lack of mechanism design for
the collaboration between LAMs and lightweight communica-
tion models, including standard evaluation metrics for agent
networks, adaptive update scheduling across cloud–edge–end
hierarchies, and balancing trade-offs between model perfor-
mance and resource consumption in the cloud. Moreover,
cloud–edge collaborative intelligent networks must support
diverse vehicular communication patterns, including both
vehicle-to-infrastructure (V2I) communication and vehicle-to-
vehicle (V2V). At the model perspective, the deep integration
of general-purpose large models with knowledge specific to
layered communication network architectures remains inade-
quate. It is necessary to further explore sequential decision-
making models that align with the scheduling characteristics
of communication and computing resources, as well as joint
strategies for multi-task resource coordination in dynamic
vehicular environments.
To address the above challenges, this paper proposes a
three-layer agent-based vehicle–road–cloud collaborative ar-
chitecture that integrates large and lightweight models, along
with a corresponding performance evaluation methodology.
In addition, a dual-loop resource management framework is
introduced. In the outer loop, a hierarchical model lifecycle
management strategy is designed for the networked system.
In the inner loop, multi-dimensional resource management
models for single-task and multi-task scenarios are designed
respectively. The main contributions of this work are as
follows:
1) This paper proposes an agent-based vehicle-road-cloud
collaborative network architecture, which enables ef-
ficient collaborative training and real-time inference
through pre-training cloud-based LAM and deploying
lightweight, pruned models at the edge.
2) A model lifecycle management method for agent net-
works is introduced. By comprehensively considering
pre-training costs, fine-tuning costs, and inference per-
formance, the method dynamically adjusts the update of
cloud-based LAM, the fine-tuning of edge-base models,
and the pruning strategy, ensuring continuous and effi-
cient inference in V2X scenarios.
3) This paper proposes a decision LAM (D-LAM)-based
resource management method in single-task V2X sce-
narios. A sequence modeling framework with temporal
embedding is developed to model multi-dimensional
resource coordination as a sequential prediction task. For
multi-task scenarios, a decision multi-task LAM (DM-
LAM) with a mixture-of-experts (MoE) mechanism is
proposed, which enables personalized and globally co-
ordinated resource allocation across heterogeneous tasks
through expert selection and gating, improving general-
ization and adaptability in dynamic environments.
The remainder of this paper is organized as follows. We
Fig. 1. V ehicle-road-cloud architecture with large-lightweight AI model
collaboration
first introduces a collaborative framework between large and
lightweight models in vehicle–road–cloud systems, along with
the model lifecycle management strategy. Then we presents a
resource management method based on LAM for both single-
task and multi-task scenarios, followed by simulation analysis
and concluding remarks.
II. V
EHICLE -ROAD -C LOUD ARCHITECTURE WITH
LARGE -L IGHTWEIGHT AI M ODEL COLLABORA TION
The proposed vehicle-road-cloud architecture with large-
lightweight model collaboration is illustrated in Fig. 1. This
framework supports various wireless communication applica-
tions in both V2V and V2I, such as vehicle cooperative percep-
tion, vehicle-infrastructure coordination, and autonomous driv-
ing. To address diverse requirements across these applications,
such as minimizing task latency, maximizing energy efficiency,
the architecture performs multiple resource management oper-
ations including: V2V/V2I mode switch, power allocation, task
offloading, and heterogeneous computing resource matching.
Beyond multi-scenario resource management, the framework
also regulates system operation cycles to achieve coordinated
resource management and operational maintenance, including:
fine-tuning cycles for the road-side unit (RSU) agent models,
training update cycles for cloud models, and pruning control.
The multi-layer collaborative resource management architec-
ture based on LAM consists of the cloud agent layer, the
RSU agent layer and the vehicle agent layer, the workflow
of the architecture is as Fig. 2 shows. The vehicle agent
includes feature data uploading and resource management
decision feedback. The RSU agent layer primarily includes
dataset construction, model quantization, fine-tuning, model
inference, and performance monitoring. The cloud agent layer
mainly contains data aggregation, model pre-training, prun-
ing optimization, multi-scale resource manager, performance
monitoring system, and lifecycle management of collabora-
tive models. These layers forming a complete closed-loop
intelligent system framework from data collection to model
optimization.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
36
To address diverse requirements across these appli-
cations, such as minimizing task latency, maximizing 
energy efficiency, the architecture performs multiple 
resource management operations including: V2V/
V2I mode switch, power allocation, task offloading, 
and heterogeneous computing resource matching. 
Beyond multi-scenario resource management, the 
framework also regulates system operation cycles 
to achieve coordinated resource management and 
operational maintenance, including: fine-tuning 
cycles for the road-side unit (RSU) agent models, 
training update cycles for cloud models, and prun -
ing control. The multi-layer collaborative resource 
management architecture based on LAM consists of 
the cloud agent layer, the RSU agent layer and the 
vehicle agent layer, the workflow of the architecture 
is as Fig. 2 shows. The vehicle agent includes feature 
data uploading and resource management decision 
feedback. The RSU agent layer primarily includes 
dataset construction, model quantization, fine-tun-
ing, model inference, and performance monitoring. 
The cloud agent layer mainly contains data aggrega-
tion, model pre-training, pruning optimization, multi-
scale resource manager, performance monitoring 
system, and lifecycle management of collaborative 
models. These layers forming a complete closed-
loop intelligent system framework from data collec-
tion to model optimization.
MultI -scenArIo  d AtAset curAtIon  And  AggregAtIon
To accommodate diverse vehicular scenarios with 
distinct resource allocation patterns and objective 
functions, such as multi-agent vehicle platooning, 
intelligent traffic management, and emergency 
rescue operations, the proposed framework first 
constructs a large-scale training dataset to ensure 
generalization across different V2X communication 
scenarios and implement flexible switching between 
V2V and V2I modes. During continuous operation, 
resource management data is sampled periodically 
from multiple scenarios. For instance, in emergen-
cy rescue scenarios, raw data from vehicle sensors, 
onboard logs, and base station records are collected 
to extract: environmental features (e.g., channel state 
information (CSI), road topology), computational 
resources (e.g., GPU/CPU utilization), communica-
tion resources (e.g., available bandwidth, spectral 
efficiency), behavioral features (e.g., vehicle trajecto-
ries, task generation patterns), and resource alloca-
tion decisions (e.g., power allocation, task offloading 
strategies), along with system performance metrics 
(e.g., latency, spectrum utilization, server load). These 
samples are labeled according to the RL paradigm 
(state, action, reward) and stored on RSU agents. 
Each RSU agent periodically uploads newly collected 
samples to the cloud for data aggregation, including 
timestamp alignment, format standardization, redun-
dancy removal, and downsampling of high-frequen-
cy scenario data to maintain dataset balance.
In addition, considering the security of sensi-
tive data, we deploy part of the feature extraction 
modules of the cloud agent LAM on the edge 
side (vehicles and RSUs), and perform adaptive 
compression on the extracted features based on 
wireless channel capacity before uploading, effec-
tively protecting the privacy of local sensitive data.
Model  Pre -trAInIng  And  MultI -d IMensIonAl  AssessMent
During the model pre-training, the cloud designs 
differentiated prompt templates based on train-
ing samples and distinct communication scenario 
characteristics (e.g., low latency, high throughput), 
which forms a dynamic multi-scenario prompt 
library. The prompts are concatenated with training 
samples before being fed into the LAM to enhance 
learning capability. To adapt to dynamic environ-
ments, the pre-training process adopts incremen-
tal learning with timestamp features embedded in 
training samples. This allows the model to capture 
temporal evolution patterns in data distribution and 
a time-weighted loss function balances the learning 
weights between historical and new data.
FIGURE 2. Workflow of the AI model collaborative based resource management architecture.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 3
Fig. 2. Workflow of the AI model collaborative based resource management

## § Architecture

A. Multi-scenario Dataset Curation and Aggregation
To accommodate diverse vehicular scenarios with distinct
resource allocation patterns and objective functions, such as
multi-agent vehicle platooning, intelligent traffic management,
and emergency rescue operations, the proposed framework
first constructs a large-scale training dataset to ensure gener-
alization across different V2X communication scenarios and
implement flexible switching between V2V and V2I modes.
During continuous operation, resource management data is
sampled periodically from multiple scenarios. For instance,
in emergency rescue scenarios, raw data from vehicle sensors,
onboard logs, and base station records are collected to extract:
environmental features (e.g., channel state information (CSI),
road topology), computational resources (e.g., GPU/CPU uti-
lization), communication resources (e.g., available bandwidth,
spectral efficiency), behavioral features (e.g., vehicle tra-
jectories, task generation patterns), and resource allocation
decisions (e.g., power allocation, task offloading strategies),
along with system performance metrics (e.g., latency, spectrum
utilization, server load). These samples are labeled according
to the RL paradigm (state, action, reward) and stored on RSU
agents. Each RSU agent periodically uploads newly collected
samples to the cloud for data aggregation, including timestamp
alignment, format standardization, redundancy removal, and
downsampling of high-frequency scenario data to maintain
dataset balance.
In addition, considering the security of sensitive data, we
deploy part of the feature extraction modules of the cloud
agent LAM on the edge side (vehicles and RSUs), and perform
adaptive compression on the extracted features based on wire-
less channel capacity before uploading, effectively protecting
the privacy of local sensitive data.
B. Model Pre-training and Multi-dimensional Assessment
During the model pre-training, the cloud designs differenti-
ated prompt templates based on training samples and distinct
communication scenario characteristics (e.g., low latency, high
throughput), which forms a dynamic multi-scenario prompt
library. The prompts are concatenated with training samples
before being fed into the LAM to enhance learning capability.
To adapt to dynamic environments, the pre-training process
adopts incremental learning with timestamp features embed-
ded in training samples. This allows the model to capture
temporal evolution patterns in data distribution and a time-
weighted loss function balances the learning weights between
historical and new data.
For post-trained models, a multi-dimensional assessment
framework is established beyond basic accuracy metrics.
Functional evaluation focuses on inference accuracy in RSU-
vehicle scenarios, multi-step task completion rates, and real-
time decision-making capability. Performance evaluation mea-
sures critical metrics including throughput, response latency,
and resource utilization rates. Adaptability evaluation involves
domain shift testing and adversarial sample detection to verify
model robustness. Unqualified models are retrained, while
qualified ones are compressed via attention-weighted struc-
tured channel pruning to reduce deployment overhead without
compromising key features.
C. Edge-adaptive Fine-tuning and Deployment
In vehicle-road-cloud collaborative architectures, con-
strained by the computing capacity and bandwidth of edge
nodes (RSUs and vehicles), direct deployment of LAM and on-
device training are both highly inefficient. Additionally, pre-
trained models suffer from environmental adaptability issues.
To address these challenges, quantization is applied to the
received pre-trained models to reduce computational and mem-
ory overhead. For optimal resource management, the quantized
models undergo fine-tuning using scenario-specific prompts
and small dataset before deployment for resource management
tasks. This paper introduces low-rank adaptation (LoRA) as an
efficient fine-tuning solution for LAM deployment on RSUs,
achieving lightweight and modular parameter updates. After
fine-tuning, only the low-rank adaptation modules need to be
distributed to vehicle agents. This significantly reduces band-
width consumption and deployment overhead while demon-
strating rapid scenario adaptation capability.
D. Model Evaluation and Lifecycle Management
To address dynamic environment, the proposed architecture
dynamically adjusts roadside model fine-tuning frequency and
cloud-side LAM update intervals for efficient resource man-
agement. Edge devices continuously collect incremental sam-
ples, storing them in local datasets following the training data
construction pipeline. Each device implements real-time model
state monitoring, tracking inference metrics and performance
indicators. These metrics jointly determine optimal fine-tuning
frequency through model cost-performance analysis.
However, the adaptation capacity of model fine-tuning is
inherently limited. When environmental changes exceed a
certain threshold, even fine-tuned models fail to maintain
satisfactory performance. To address this limitation, the system
activates cloud-based incremental learning that RSU uploads
incrementally collected samples to the cloud for data aggrega-
tion, followed by incremental updates to the LAM using the
aggregated dataset. The updated model undergoes comprehen-
sive evaluation and targeted pruning before being redistributed
to base stations for deployment.
To accommodate diverse 
vehicular scenarios with 
distinct resource allocation 
patterns and objective func -
tions, such as multi-agent 
vehicle platooning, intelli-
gent traffic management, 
and emergency rescue 
operations, the proposed 
framework first constructs 
a large-scale training 
dataset to ensure general -
ization across different V2X 
communication scenarios 
and implement flexible 
switching between V2V and 
V2I modes.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
37
For post-trained models, a multi-dimensional 
assessment framework is established beyond basic 
accuracy metrics. Functional evaluation focuses 
on inference accuracy in RSU-vehicle scenarios, 
multi-step task completion rates, and real-time deci-
sion-making capability. Performance evaluation mea-
sures critical metrics including throughput, response 
latency, and resource utilization rates. Adaptability 
evaluation involves domain shift testing and adver-
sarial sample detection to verify model robustness. 
Unqualified models are retrained, while qualified 
ones are compressed via attention-weighted struc-
tured channel pruning to reduce deployment over-
head without compromising key features.
edge -Ad APtIVe FIne -tun Ing  And  d ePloy Ment
In vehicle-road-cloud collaborative architectures, 
constrained by the computing capacity and band-
width of edge nodes (RSUs and vehicles), direct 
deployment of LAM and on-device training are 
both highly inefficient. Additionally, pre-trained 
models suffer from environmental adaptability 
issues. To address these challenges, quantization 
is applied to the received pre-trained models to 
reduce computational and memory overhead. 
For optimal resource management, the quantized 
models undergo fine-tuning using scenario-specific 
prompts and small dataset before deployment for 
resource management tasks. This article introduces 
low-rank adaptation (LoRA) as an efficient fine-tun-
ing solution for LAM deployment on RSUs, achiev-
ing lightweight and modular parameter updates. 
After fine-tuning, only the low-rank adaptation 
modules need to be distributed to vehicle agents. 
This significantly reduces bandwidth consumption 
and deployment overhead while demonstrating 
rapid scenario adaptation capability.
Model  eVAluAtIon  And  lIFecycle  MAnAgeMent
To address dynamic environment, the proposed 
architecture dynamically adjusts roadside model 
fine-tuning frequency and cloud-side LAM update 
intervals for efficient resource management. Edge 
devices continuously collect incremental samples, 
storing them in local datasets following the training 
data construction pipeline. Each device implements 
real-time model state monitoring, tracking infer-
ence metrics and performance indicators. These 
metrics jointly determine optimal fine-tuning fre-
quency through model cost-performance analysis.
However, the adaptation capacity of model 
fine-tuning is inherently limited. When environ -
mental changes exceed a certain threshold, even 
fine-tuned models fail to maintain satisfactory per-
formance. To address this limitation, the system 
activates cloud-based incremental learning that 
RSU uploads incrementally collected samples to 
the cloud for data aggregation, followed by incre-
mental updates to the LAM using the aggregated 
dataset. The updated model undergoes compre-
hensive evaluation and targeted pruning before 
being redistributed to base stations for deployment.
Based on the aforementioned model fine-tun-
ing and cloud-based incremental learning frame-
work, a multi-scale resource management is 
established at the cloud center to orchestrate 
the model production and adaptation pipeline. 
This controller dynamically coordinates edge-side 
fine-tuning cycles, cloud model update intervals, 
and pruning ratio by holistically evaluating multi-
ple cost-performance dimensions
The cloud-based control center employs a 
multi-scale resource management controller to reg-
ulate both the model fine-tuning and incremental 
learning updates throughout model lifecycle. The 
proposed model lifecycle management framework 
is illustrated as Fig. 3. We mainly account multi-di-
mensional cost factors include: computational and 
memory resources for fine-tuning, inference laten-
cy and performance, cloud computational and 
memory overhead for model updates, bandwidth 
consumption for both incremental data upload and 
model distribution, the impact of pruning ratio on 
model accuracy as well as sampling rates of incre-
mental training datasets. Through an actor-critic 
architecture, the framework dynamically optimizes 
the fine-tuning cycles, pruning ratio and the cloud 
update frequency, achieving maximal model per-
formance under predefined resource constraints.
Specifically, to account for the dynamic nature 
of V2X network topologies, we configure the 
model fine-tuning d
fine  = p t to be performed 
every p transmission slots. Considering the limit-
ed effectiveness of model fine-tuning, we estab-
lish a model update window l  that triggers a 
cloud-based LAM update after every k  fine-tuning 
rounds. During this window, the model is retrained 
and updated to ensure the accuracy of locally 
deployed models. Let d
train  = l  + k d fine denote 
the model update period. The model update win-
dow consists of sample data transmission delay, 
model pre-training delay, and model distribution 
delay. The relationship between training batch 
size b, model pruning rate s , and convergence 
rate g, which is characterized by an upper bound 
on the average L2-norm of gradients [15]:
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 4
Fig. 3. Collaborative model lifecycle management framework
Based on the aforementioned model fine-tuning and cloud-
based incremental learning framework, a multi-scale resource
management is established at the cloud center to orchestrate
the model production and adaptation pipeline. This controller
dynamically coordinates edge-side fine-tuning cycles, cloud
model update intervals, and pruning ratio by holistically eval-
uating multiple cost-performance dimensions
The cloud-based control center employs a multi-scale re-
source management controller to regulate both the model fine-
tuning and incremental learning updates throughout model
lifecycle. The proposed model lifecycle management frame-
work is illustrated as Fig. 3. We mainly account multi-
dimensional cost factors include: computational and memory
resources for fine-tuning, inference latency and performance,
cloud computational and memory overhead for model updates,
bandwidth consumption for both incremental data upload and
model distribution, the impact of pruning ratio on model
accuracy as well as sampling rates of incremental training
datasets. Through an actor-critic architecture, the framework
dynamically optimizes the fine-tuning cycles, pruning ratio
and the cloud update frequency, achieving maximal model
performance under predefined resource constraints.
Specifically, to account for the dynamic nature of V2X
network topologies, we configure the model fine-tuning δ
fine =
pτ to be performed every p transmission slots. Considering
the limited effectiveness of model fine-tuning, we establish
a model update window λ that triggers a cloud-based LAM
update after every k fine-tuning rounds. During this window,
the model is retrained and updated to ensure the accuracy of
locally deployed models. Let δ
train = λ + kδfine denote the
model update period. The model update window consists of
sample data transmission delay, model pre-training delay, and
model distribution delay. The relationship between training
batch size b, model pruning rate σ, and convergence rate γ,
which is characterized by an upper bound on the average L2-
norm of gradients [15]:
1
γ = φ
bS + ψσ, (1)
where E∥∇F (w )∥2 ≤ 1
γ . The first term characterizes the
baseline constraint intensity of training error through gradient
smoothness features φ, establishing an inverse regulatory
relationship with b and training rounds S . The second term
accounts for the model’s sensitivity to σ, where ψ relates to
the changes in weight norms.
The analysis demonstrates that larger training batch sizes
and lower pruning rates lead to slower convergence rates,
reduced parameter update magnitudes, and accelerated con-
vergence attainment. Consequently, by acquiring the pruning
rate and convergence rate, we can calculate both the total
training delay and the final parameter count before model
distribution The model distribution delay can be calculated
based on allocated cloud bandwidth.
The length of the model fine-tuning cycle is jointly deter-
mined by the fine-tuning cost C
fine and model performance
P . An exponential function P0e−βδ fine is used to represent
the performance decay degree after the fine-tuning cycle
δ
fine. Considering the specified performance lower bound prec,
the fine-tuning cost consumption involved in a single local
model with parameter quantity M includes: (1) parameter
cost, governed by M , fine-tuning parameter ratio and unit
parameter cost; (2) computation cost, determined by M ,
training duration, hardware cost, and batch size; (3) memory
cost, influenced by the parameter storage coefficient, M and
unit storage cost.
For different fine-tuning strategies, the model performance
improvements vary. We introduce a fine-tuning efficacy factor
to quantify the fine-tuned model performance. The perfor-
mance gain ∆P after fine-tuning consists of distribution sim-
ilarity between incremental data and historical data, learning
efficiency coefficient, and fine-tuning efficacy factor. The fine-
tuning efficiency function can be expressed as:
η
fine(δfine)= C fine
δfine
+
∫ δfine
0
(P0e−βt − P rec)dt− ∆P (2)
After multiple rounds of model fine-tuning, the marginal
benefits of fine-tuning operations diminish. When the fine-
tuning gain falls below a threshold, a cloud-based LAM update
and subsequent local redeployment are required. The setting of
the model update cycle primarily considers multi-dimensional
factors including retraining cost and update performance gain.
The cost consumed by a single model update consists of: (1)
parameter cost, governed by initial training parameter quan-
tity and unit parameter cost; (2) computation cost, determined
by M , training duration, hardware cost and batch size; (3)
memory cost, influenced by pruning rate, parameter storage
coefficient, M and unit storage cost.
Combined with the model update window length, the update
efficiency function can be expressed as:
η
train(δtrain,σ)= C train + λ
δtrain
− ∆F (σ, b) (3)
where ∆F (·) is the performance gain function influenced by
the model pruning rate σ and training batch size b. By applying
DRL to optimize both the fine-tuning efficiency function and
update efficiency function, we achieve collaborative model
lifecycle management efficiency through adaptive control of
fine-tuning cycles and update cycles.
 (1)
where E||∇F(w)
||2  1/g . The first term charac-
terizes the baseline constraint intensity of train-
ing error through gradient smoothness features 
, establishing an inverse regulatory relationship 
FIGURE 3. Collaborative model lifecycle management framework.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 4
Fig. 3. Collaborative model lifecycle management framework
Based on the aforementioned model fine-tuning and cloud-
based incremental learning framework, a multi-scale resource
management is established at the cloud center to orchestrate
the model production and adaptation pipeline. This controller
dynamically coordinates edge-side fine-tuning cycles, cloud
model update intervals, and pruning ratio by holistically eval-
uating multiple cost-performance dimensions
The cloud-based control center employs a multi-scale re-
source management controller to regulate both the model fine-
tuning and incremental learning updates throughout model
lifecycle. The proposed model lifecycle management frame-
work is illustrated as Fig. 3. We mainly account multi-
dimensional cost factors include: computational and memory
resources for fine-tuning, inference latency and performance,
cloud computational and memory overhead for model updates,
bandwidth consumption for both incremental data upload and
model distribution, the impact of pruning ratio on model
accuracy as well as sampling rates of incremental training
datasets. Through an actor-critic architecture, the framework
dynamically optimizes the fine-tuning cycles, pruning ratio
and the cloud update frequency, achieving maximal model
performance under predefined resource constraints.
Specifically, to account for the dynamic nature of V2X
network topologies, we configure the model fine-tuning δ
fine =
pτ to be performed every p transmission slots. Considering
the limited effectiveness of model fine-tuning, we establish
a model update window λ that triggers a cloud-based LAM
update after every k fine-tuning rounds. During this window,
the model is retrained and updated to ensure the accuracy of
locally deployed models. Let δ
train = λ + kδfine denote the
model update period. The model update window consists of
sample data transmission delay, model pre-training delay, and
model distribution delay. The relationship between training
batch size b, model pruning rate σ, and convergence rate γ,
which is characterized by an upper bound on the average L2-
norm of gradients [15]:
1
γ = φ
bS + ψσ, (1)
where E∥∇F (w )∥
2 ≤ 1
γ . The first term characterizes the
baseline constraint intensity of training error through gradient
smoothness features φ, establishing an inverse regulatory
relationship with b and training rounds S . The second term
accounts for the model’s sensitivity to σ, where ψ relates to
the changes in weight norms.
The analysis demonstrates that larger training batch sizes
and lower pruning rates lead to slower convergence rates,
reduced parameter update magnitudes, and accelerated con-
vergence attainment. Consequently, by acquiring the pruning
rate and convergence rate, we can calculate both the total
training delay and the final parameter count before model
distribution The model distribution delay can be calculated
based on allocated cloud bandwidth.
The length of the model fine-tuning cycle is jointly deter-
mined by the fine-tuning cost C
fine and model performance
P . An exponential function P0e−βδ fine is used to represent
the performance decay degree after the fine-tuning cycle
δ
fine. Considering the specified performance lower bound prec,
the fine-tuning cost consumption involved in a single local
model with parameter quantity M includes: (1) parameter
cost, governed by M , fine-tuning parameter ratio and unit
parameter cost; (2) computation cost, determined by M ,
training duration, hardware cost, and batch size; (3) memory
cost, influenced by the parameter storage coefficient, M and
unit storage cost.
For different fine-tuning strategies, the model performance
improvements vary. We introduce a fine-tuning efficacy factor
to quantify the fine-tuned model performance. The perfor-
mance gain ∆P after fine-tuning consists of distribution sim-
ilarity between incremental data and historical data, learning
efficiency coefficient, and fine-tuning efficacy factor. The fine-
tuning efficiency function can be expressed as:
η
fine(δfine)= C fine
δfine
+
∫ δfine
0
(P0e−βt − P rec)dt− ∆P (2)
After multiple rounds of model fine-tuning, the marginal
benefits of fine-tuning operations diminish. When the fine-
tuning gain falls below a threshold, a cloud-based LAM update
and subsequent local redeployment are required. The setting of
the model update cycle primarily considers multi-dimensional
factors including retraining cost and update performance gain.
The cost consumed by a single model update consists of: (1)
parameter cost, governed by initial training parameter quan-
tity and unit parameter cost; (2) computation cost, determined
by M , training duration, hardware cost and batch size; (3)
memory cost, influenced by pruning rate, parameter storage
coefficient, M and unit storage cost.
Combined with the model update window length, the update
efficiency function can be expressed as:
η
train(δtrain,σ)= C train + λ
δtrain
− ∆F (σ, b) (3)
where ∆F (·) is the performance gain function influenced by
the model pruning rate σ and training batch size b. By applying
DRL to optimize both the fine-tuning efficiency function and
update efficiency function, we achieve collaborative model
lifecycle management efficiency through adaptive control of
fine-tuning cycles and update cycles.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
38
with b and training rounds S . The second term 
accounts for the model’s sensitivity to s , where ψ 
relates to the changes in weight norms.
The analysis demonstrates that larger training 
batch sizes and lower pruning rates lead to slower 
convergence rates, reduced parameter update 
magnitudes, and accelerated convergence attain-
ment. Consequently, by acquiring the pruning 
rate and convergence rate, we can calculate both 
the total training delay and the final parameter 
count before model distribution The model distri-
bution delay can be calculated based on allocat-
ed cloud bandwidth.
The length of the model fine-tuning cycle is 
jointly determined by the fine-tuning cost C
fine 
and model performance P . An exponential func-
tion P0 e–bd fine  is used to represent the perfor -
mance decay degree after the fine-tuning cycle 
d
fine . Considering the specified performance 
lower bound p rec, the fine-tuning cost consump-
tion involved in a single local model with parame-
ter quantity M includes: 
1. Parameter cost, governed by M , fine-tuning 
parameter ratio and unit parameter cost;
2. Computation cost, determined by M , training 
duration, hardware cost, and batch size;
3. Memory cost, influenced by the parameter 
storage coefficient, M and unit storage cost. 
For different fine-tuning strategies, the model 
performance improvements vary. We introduce 
a fine-tuning efficacy factor to quantify the fine-
tuned model performance. The performance gain 
DP after fine-tuning consists of distribution similar-
ity between incremental data and historical data, 
learning efficiency coefficient, and fine-tuning effi-
cacy factor. The fine-tuning efficiency function 
can be expressed as:
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 4
Fig. 3. Collaborative model lifecycle management framework
Based on the aforementioned model fine-tuning and cloud-
based incremental learning framework, a multi-scale resource
management is established at the cloud center to orchestrate
the model production and adaptation pipeline. This controller
dynamically coordinates edge-side fine-tuning cycles, cloud
model update intervals, and pruning ratio by holistically eval-
uating multiple cost-performance dimensions
The cloud-based control center employs a multi-scale re-
source management controller to regulate both the model fine-
tuning and incremental learning updates throughout model
lifecycle. The proposed model lifecycle management frame-
work is illustrated as Fig. 3. We mainly account multi-
dimensional cost factors include: computational and memory
resources for fine-tuning, inference latency and performance,
cloud computational and memory overhead for model updates,
bandwidth consumption for both incremental data upload and
model distribution, the impact of pruning ratio on model
accuracy as well as sampling rates of incremental training
datasets. Through an actor-critic architecture, the framework
dynamically optimizes the fine-tuning cycles, pruning ratio
and the cloud update frequency, achieving maximal model
performance under predefined resource constraints.
Specifically, to account for the dynamic nature of V2X
network topologies, we configure the model fine-tuning δ
fine =
pτ to be performed every p transmission slots. Considering
the limited effectiveness of model fine-tuning, we establish
a model update window λ that triggers a cloud-based LAM
update after every k fine-tuning rounds. During this window,
the model is retrained and updated to ensure the accuracy of
locally deployed models. Let δ
train = λ + kδfine denote the
model update period. The model update window consists of
sample data transmission delay, model pre-training delay, and
model distribution delay. The relationship between training
batch size b, model pruning rate σ, and convergence rate γ,
which is characterized by an upper bound on the average L2-
norm of gradients [15]:
1
γ = φ
bS + ψσ, (1)
where E∥∇F (w )∥
2 ≤ 1
γ . The first term characterizes the
baseline constraint intensity of training error through gradient
smoothness features φ, establishing an inverse regulatory
relationship with b and training rounds S . The second term
accounts for the model’s sensitivity to σ, where ψ relates to
the changes in weight norms.
The analysis demonstrates that larger training batch sizes
and lower pruning rates lead to slower convergence rates,
reduced parameter update magnitudes, and accelerated con-
vergence attainment. Consequently, by acquiring the pruning
rate and convergence rate, we can calculate both the total
training delay and the final parameter count before model
distribution The model distribution delay can be calculated
based on allocated cloud bandwidth.
The length of the model fine-tuning cycle is jointly deter-
mined by the fine-tuning cost C
fine and model performance
P . An exponential function P0e−βδ fine is used to represent
the performance decay degree after the fine-tuning cycle
δ
fine. Considering the specified performance lower bound prec,
the fine-tuning cost consumption involved in a single local
model with parameter quantity M includes: (1) parameter
cost, governed by M , fine-tuning parameter ratio and unit
parameter cost; (2) computation cost, determined by M ,
training duration, hardware cost, and batch size; (3) memory
cost, influenced by the parameter storage coefficient, M and
unit storage cost.
For different fine-tuning strategies, the model performance
improvements vary. We introduce a fine-tuning efficacy factor
to quantify the fine-tuned model performance. The perfor-
mance gain ∆P after fine-tuning consists of distribution sim-
ilarity between incremental data and historical data, learning
efficiency coefficient, and fine-tuning efficacy factor. The fine-
tuning efficiency function can be expressed as:
ηfine(δfine)= C fine
δfine
+
∫ δfine
0
(P0e−βt − P rec)dt− ∆P (2)
After multiple rounds of model fine-tuning, the marginal
benefits of fine-tuning operations diminish. When the fine-
tuning gain falls below a threshold, a cloud-based LAM update
and subsequent local redeployment are required. The setting of
the model update cycle primarily considers multi-dimensional
factors including retraining cost and update performance gain.
The cost consumed by a single model update consists of: (1)
parameter cost, governed by initial training parameter quan-
tity and unit parameter cost; (2) computation cost, determined
by M , training duration, hardware cost and batch size; (3)
memory cost, influenced by pruning rate, parameter storage
coefficient, M and unit storage cost.
Combined with the model update window length, the update
efficiency function can be expressed as:
η
train(δtrain,σ)= C train + λ
δtrain
− ∆F (σ, b) (3)
where ∆F (·) is the performance gain function influenced by
the model pruning rate σ and training batch size b. By applying
DRL to optimize both the fine-tuning efficiency function and
update efficiency function, we achieve collaborative model
lifecycle management efficiency through adaptive control of
fine-tuning cycles and update cycles.
 (2)
A
fter multiple rounds of model fine-tuning, 
the marginal benefits of fine-tuning operations 
diminish. When the fine-tuning gain falls below 
a threshold, a cloud-based LAM update and sub-
sequent local redeployment are required. The 
setting of the model update cycle primarily con-
siders multi-dimensional factors including retrain-
ing cost and update performance gain. The cost 
consumed by a single model update consists of:
1. Parameter cost , governed by initial training 
parameter quantity and unit parameter cost;
2. Computation cost, determined by M , training 
duration, hardware cost and batch size;
3. Memory cost , influenced by pruning rate, 
parameter storage coefficient, M  and unit 
storage cost. 
Combined with the model update window 
length, the update efficiency function can be 
expressed as:
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 4
Fig. 3. Collaborative model lifecycle management framework
Based on the aforementioned model fine-tuning and cloud-
based incremental learning framework, a multi-scale resource
management is established at the cloud center to orchestrate
the model production and adaptation pipeline. This controller
dynamically coordinates edge-side fine-tuning cycles, cloud
model update intervals, and pruning ratio by holistically eval-
uating multiple cost-performance dimensions
The cloud-based control center employs a multi-scale re-
source management controller to regulate both the model fine-
tuning and incremental learning updates throughout model
lifecycle. The proposed model lifecycle management frame-
work is illustrated as Fig. 3. We mainly account multi-
dimensional cost factors include: computational and memory
resources for fine-tuning, inference latency and performance,
cloud computational and memory overhead for model updates,
bandwidth consumption for both incremental data upload and
model distribution, the impact of pruning ratio on model
accuracy as well as sampling rates of incremental training
datasets. Through an actor-critic architecture, the framework
dynamically optimizes the fine-tuning cycles, pruning ratio
and the cloud update frequency, achieving maximal model
performance under predefined resource constraints.
Specifically, to account for the dynamic nature of V2X
network topologies, we configure the model fine-tuning δ
fine =
pτ to be performed every p transmission slots. Considering
the limited effectiveness of model fine-tuning, we establish
a model update window λ that triggers a cloud-based LAM
update after every k fine-tuning rounds. During this window,
the model is retrained and updated to ensure the accuracy of
locally deployed models. Let δ
train = λ + kδfine denote the
model update period. The model update window consists of
sample data transmission delay, model pre-training delay, and
model distribution delay. The relationship between training
batch size b, model pruning rate σ, and convergence rate γ,
which is characterized by an upper bound on the average L2-
norm of gradients [15]:
1
γ = φ
bS + ψσ, (1)
where E∥∇F (w )∥
2 ≤ 1
γ . The first term characterizes the
baseline constraint intensity of training error through gradient
smoothness features φ, establishing an inverse regulatory
relationship with b and training rounds S . The second term
accounts for the model’s sensitivity to σ, where ψ relates to
the changes in weight norms.
The analysis demonstrates that larger training batch sizes
and lower pruning rates lead to slower convergence rates,
reduced parameter update magnitudes, and accelerated con-
vergence attainment. Consequently, by acquiring the pruning
rate and convergence rate, we can calculate both the total
training delay and the final parameter count before model
distribution The model distribution delay can be calculated
based on allocated cloud bandwidth.
The length of the model fine-tuning cycle is jointly deter-
mined by the fine-tuning cost C
fine and model performance
P . An exponential function P0e−βδ fine is used to represent
the performance decay degree after the fine-tuning cycle
δ
fine. Considering the specified performance lower bound prec,
the fine-tuning cost consumption involved in a single local
model with parameter quantity M includes: (1) parameter
cost, governed by M , fine-tuning parameter ratio and unit
parameter cost; (2) computation cost, determined by M ,
training duration, hardware cost, and batch size; (3) memory
cost, influenced by the parameter storage coefficient, M and
unit storage cost.
For different fine-tuning strategies, the model performance
improvements vary. We introduce a fine-tuning efficacy factor
to quantify the fine-tuned model performance. The perfor-
mance gain ∆P after fine-tuning consists of distribution sim-
ilarity between incremental data and historical data, learning
efficiency coefficient, and fine-tuning efficacy factor. The fine-
tuning efficiency function can be expressed as:
η
fine(δfine)= C fine
δfine
+
∫ δfine
0
(P0e−βt − P rec)dt− ∆P (2)
After multiple rounds of model fine-tuning, the marginal
benefits of fine-tuning operations diminish. When the fine-
tuning gain falls below a threshold, a cloud-based LAM update
and subsequent local redeployment are required. The setting of
the model update cycle primarily considers multi-dimensional
factors including retraining cost and update performance gain.
The cost consumed by a single model update consists of: (1)
parameter cost, governed by initial training parameter quan-
tity and unit parameter cost; (2) computation cost, determined
by M , training duration, hardware cost and batch size; (3)
memory cost, influenced by pruning rate, parameter storage
coefficient, M and unit storage cost.
Combined with the model update window length, the update
efficiency function can be expressed as:
ηtrain(δtrain,σ)= C train + λ
δtrain
− ∆F (σ, b) (3)
where ∆F (·) is the performance gain function influenced by
the model pruning rate σ and training batch size b. By applying
DRL to optimize both the fine-tuning efficiency function and
update efficiency function, we achieve collaborative model
lifecycle management efficiency through adaptive control of
fine-tuning cycles and update cycles.
 (3)
where D
F() is the performance gain function influ-
enced by the model pruning rate s  and training 
batch size b . By applying DRL to optimize both 
the fine-tuning efficiency function and update effi-
ciency function, we achieve collaborative model 
lifecycle management efficiency through adaptive 
control of fine-tuning cycles and update cycles.
collAborAtIVe  resource  MAnAgeMent  Model  
In  VehIcle -roAd -cloud  systeMs
sIngle -tAsk  scenArIos
As illustrated in Fig. 4, this study proposes a 
collaborative training architecture tailored for 
vehicle-road-cloud systems within a computing 
power network-enabled environment. At the 
vehicle layer, environmental and state informa-
tion can be collected either by individual agents 
operating independently or through the collab-
oration of multiple agents. Regardless of the 
operational mode, the raw data collected is first 
transmitted to edge nodes deployed at RSUs. 
These edge nodes are responsible for fusing 
and preliminarily processing the received multi-
source heterogeneous data, performing tasks 
such as redundancy elimination and consisten-
cy verification to ensure data integrity and reli-
ability. Subsequently, the integrated system state 
information is uploaded in real-time to the cloud 
platform. Upon receiving the data, the cloud 
system conducts systematic pre-processing for 
the training of the LAM, including critical proce-
dures such as data cleansing, compression, and 
segmentation. For each task category, a corre-
sponding prompt vector is designed and embed-
ded along with the environmental state as input 
sequences for the D-LAM.
During the cloud-layer model training, the sys-
tem first constructs a global view of the comput -
ing power network by aggregating localized state 
information uploaded by vehicle clusters via edge 
nodes. This aggregated information is then syn -
thesized into a unified global environment vector, 
serving as the foundational input for model train-
ing. The D-LAM is trained based on pre-sampled 
sequences in the form of state-action-reward-return 
tuples. The state space captures the environmental 
context of the computing network at each time 
step, incorporating various factors such as com-
putational resource metrics of vehicular terminals 
and edge nodes, vehicle-RSU positional relation-
ships, and task demand intensity. The action space 
encompasses all feasible scheduling operations, 
including task offloading destination selection, allo-
cation of computational and bandwidth resources, 
interference mitigation, and beam-forming con -
trol. The immediate reward quantifies the impact 
of each scheduling action on overall system per-
formance indicators such as latency, energy effi-
ciency, and through put. Meanwhile, the expected 
return reflects the cumulative benefit of scheduling 
over multiple time slots in a dynamic environment. 
To enhance the model’s capability in handling 
multi-modal input data, independent linear embed-
ding layers are applied to each data modality. In 
addition, to improve the model’s responsiveness for 
delay-sensitive tasks, a fixed length input sequence 
window is introduced. This constraint limits the 
temporal context, encouraging the model to focus 
on recent history and striking a balance between 
context modeling capacity and inference latency 
— thereby improving its realtime applicability and 
 These edge nodes are 
responsible for fusing and 
preliminarily processing 
the received multi-source 
heterogeneous data, 
performing tasks such as 
redundancy elimination and 
consistency verification to 
ensure data integrity and 
reliability. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
39
deployment efficiency. Subsequently, a policy gen-
eration head maps the attention outputs into a con-
crete resource scheduling policy vector, specifying 
the current computing path and resource alloca-
tion decisions. To achieve short-term system utility 
maximization under multi-dimensional communi-
cation resource constraints, this study incorporates 
both task inference accuracy and delay penalty into 
the reward function design. As illustrated in Fig. 4, 
the short-term utility function is modeled as the log-
arithm of the ratio between inference accuracy and 
task completion time at each communication time 
slot t, weighted by a trade-off parameter reflecting 
system gain versus cost.
The entire training process is conducted in 
an auto-regressive manner, where the output at 
each time step is fed into the subsequent time 
step as part of the input. Upon completion of 
the training phase, the model undergoes light-
weight compression techniques such as pruning 
and knowledge distillation to reduce its compu-
tational footprint. Furthermore, few-shot fine-tun-
ing is performed in local environments using a 
small set of task-specific samples, thereby pro-
ducing task-adaptive local scheduling models. 
These models support low-latency and high-effi-
ciency resource scheduling under the collabora-
tive vehicle-road-cloud architecture.
Compared to traditional RL approaches 
(e.g., value function approximation), D-LAM 
demonstrates significant advantages in handling 
large-scale historical trajectories and high-dimen-
sional state spaces. Leveraging its auto-regressive 
sequence modeling capability, D-LAM captures 
temporal dependencies more effectively, gener-
ating more robust and generalizable scheduling 
policies, thereby enabling better adaptation to 
complex V2X scenarios and enhancing overall 
service quality and resource utilization efficiency.
MultI -tAsk  scenArIos
In the vehicle-road-cloud collaborative comput-
ing network environment, vehicles often need 
to execute multiple tasks in parallel, such as real-
time perception, behavior prediction, path plan-
ning, local map construction, and model updates. 
These tasks significantly differ in terms of time sen-
sitivity, computational complexity, and collabora-
tion requirements. Thus, there is an urgent need 
to develop a multi-task management architecture 
that integrates task recognition, dynamic schedul-
ing, and collaboration capabilities.
To address these needs, this article proposes a 
DM-LAM to achieve multi-task resource manage-
ment based on LAMs. By leveraging the powerful 
learning capabilities of LAM, the method optimizes 
task scheduling and resource allocation, enabling 
efficient decision-making in concurrent multi-task-
ing scenarios. The DM-LAM frames the resource 
scheduling process as a sequential decision-making 
task with long-term dependencies. Different tasks 
exhibit distinct resource utilization patterns, such as 
computation, communication, and caching, during 
execution. As a result, the method introduces a 
specialized expert network within the LAM archi-
tecture and implements dynamic expert scheduling 
through a task feature-driven gating mechanism. 
This approach offers differentiated resource opti-
mization paths for various task types. For tasks with 
high computational loads, the DM-LAM uses an 
expert selection mechanism to prioritize nodes 
with computational advantages. It dynamically 
determines whether to perform local processing, 
collaborate at the edge, or offload to the cloud, 
considering the task’s data scale and communi-
cation overhead. For communication-sensitive 
tasks, the model prioritizes expert strategies with 
low-latency transmission capabilities and adjusts 
communication paths based on real-time channel 
FIGURE 4. Collaborative training architecture between large and lightweight models in vehicle-road-cloud systems.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 5
Fig. 4. Collaborative training architecture between large and lightweight models in vehicle–road–cloud systems
III. C OLLABORA TIVE RESOURCE MANAGEMENT MODEL
IN VEHICLE –ROAD –CLOUD SYSTEMS
A. Single-Task Scenarios
As illustrated in Fig. 4, this study proposes a collaborative
training architecture tailored for vehicle–road–cloud systems
within a computing power network-enabled environment. At
the vehicle layer, environmental and state information can be
collected either by individual agents operating independently
or through the collaboration of multiple agents. Regardless
of the operational mode, the raw data collected is first trans-
mitted to edge nodes deployed at RSUs. These edge nodes
are responsible for fusing and preliminarily processing the
received multi-source heterogeneous data, performing tasks
such as redundancy elimination and consistency verification
to ensure data integrity and reliability. Subsequently, the
integrated system state information is uploaded in real-time
to the cloud platform. Upon receiving the data, the cloud
system conducts systematic pre-processing for the training of
the LAM, including critical procedures such as data cleansing,
compression, and segmentation. For each task category, a
corresponding prompt vector is designed and embedded along
with the environmental state as input sequences for the D-
LAM.
During the cloud-layer model training, the system first
constructs a global view of the computing power network by
aggregating localized state information uploaded by vehicle
clusters via edge nodes. This aggregated information is then
synthesized into a unified global environment vector, serving
as the foundational input for model training. The D-LAM
is trained based on pre-sampled sequences in the form of
state–action–reward–return tuples. The state space captures the
environmental context of the computing network at each time
step, incorporating various factors such as computational re-
source metrics of vehicular terminals and edge nodes, vehicle-
RSU positional relationships, and task demand intensity. The
action space encompasses all feasible scheduling operations,
including task offloading destination selection, allocation of
computational and bandwidth resources, interference mitiga-
tion, and beam-forming control. The immediate reward quan-
tifies the impact of each scheduling action on overall system
performance indicators such as latency, energy efficiency,
and through put. Meanwhile, the expected return reflects the
cumulative benefit of scheduling over multiple time slots in
a dynamic environment. To enhance the model’s capability in
handling multi-modal input data, independent linear embed-
ding layers are applied to each data modality. In addition, to
improve the model’s responsiveness for delay-sensitive tasks,
a fixed length input sequence window is introduced. This
constraint limits the temporal context, encouraging the model
to focus on recent history and striking a balance between
context modeling capacity and inference latency—thereby
improving its realtime applicability and deployment efficiency.
Subsequently, a policy generation head maps the attention
outputs into a concrete resource scheduling policy vector,
specifying the current computing path and resource allocation
decisions. To achieve short-term system utility maximization
under multi-dimensional communication resource constraints,
this study incorporates both task inference accuracy and delay
penalty into the reward function design. As illustrated in Fig.
4, the short-term utility function is modeled as the logarithm
of the ratio between inference accuracy and task completion
time at each communication time slot t, weighted by a trade-
off parameter reflecting system gain versus cost.
The entire training process is conducted in an auto-
regressive manner, where the output at each time step is fed
into the subsequent time step as part of the input. Upon com-
pletion of the training phase, the model undergoes lightweight
compression techniques such as pruning and knowledge dis-
tillation to reduce its computational footprint. Furthermore,
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
40
conditions, ensuring optimal task selection across 
multiple paths, such as V2V and V2I. For tasks 
involving large-scale data caching and forwarding, 
DM-LAM utilizes an expert routing mechanism to 
flexibly match nodes with caching advantages or 
data pre-fetching capabilities, enabling coordinated 
scheduling of computation and caching. Addition-
ally, the DM-LAM takes full advantage of resource 
disparities among heterogeneous nodes in the 
computing network. In scenarios where multiple 
tasks arrive simultaneously, it dynamically balanc-
es global resource scheduling with local task opti-
mization. In resource-constrained environments, 
the model actively selects real-time responses for 
high-priority tasks based on task priority, delay sen-
sitivity, and resource consumption characteristics.
The DM-LAM can dynamically optimize 
resource scheduling strategies in complex vehi-
cle-road-cloud collaborative environments, tailor-
ing solutions to the varying demands of multiple 
tasks. It effectively coordinates resource conflicts 
between tasks, providing an efficient and stable 
multi-task resource management solution.
n uMerIcAl  results  And  AnAlysIs
Based on the proposed architecture, the devel-
oped method enables reliable interaction in 
dynamic vehicle-road-cloud scenarios through a 
model lifecycle management scheme. The simu-
lation focuses on a V2X scenario with single RSU 
assisted multi-vehicle cooperative perception: 
vehicles are randomly distributed within a 150 
meters radius of a fixed RSU, with speeds rang-
ing from 20 to 60 km/h. Both the vehicles and 
the RSU are equipped with 32GB of memory, 
and the bandwidth between them is set to 50-100 
Mbps. A resource allocation strategy dataset is 
constructed using the proximal policy optimiza-
tion (PPO) algorithm.
Specifically, the state space incorporates the 
varying number of vehicles, their positions and 
speeds relative to the RSU, vehicle-to-RSU CSI, 
and available RSU computing resources. The 
action space consists of data upload bandwidth 
and inference compute resource allocation strat-
egies. The reward function comprehensively con-
siders communication and computation resource 
utilization alongside task latency. The dataset is 
divided into pre-training (60%), fine-tuning (30%), 
and evaluation (10%) subsets based on vehicle 
count variations. Experiments are conducted on 
NVIDIA A6000 GPU. The LAM is built upon 
Qwen2.5-14b, integrated with task-specific fea-
ture extraction modules and prompt engineering. 
Both pre-training and fine-tuning (with LoRA rank 
= 16, a  = 64) phases employ the AdamW opti-
mizer, using a batch size of 64. The pre-training 
learning rate is set to 510
-5, while the fine-tuning 
learning rate is reduced to 110 -5.
We compare the proposed method with DT, 
PPO, and random selection baselines by simulating 
time-varying scenario dynamics in the dataset to 
evaluate the resource utilization changes achieved 
by different resource allocation schemes. As shown 
in Fig. 5, the proposed model demonstrates supe-
rior performance compared to DT, PPO, and ran -
dom selection. Moreover, the results indicate that 
our method effectively recalibrates model perfor-
mance in response to dynamic scenario changes, 
ensuring reliable inference. This is attributed to the 
adaptive fine-tuning cycles and update cycles in 
our framework, which promptly stabilize inference 
performance through model adjustments when 
significant scenario shifts occur.
To validate the model’s generalization capacity, 
we conducted the experiment under diverse sce -
narios with varying vehicle numbers. As illustrated 
in Fig. 6, while DT and PPO exhibited significant 
degradation of task completion rates with increas-
ing vehicle numbers, our model demonstrated con-
sistent stability and maintained higher performance 
through lifecycle management scheme. The exper-
imental results show that our approach achieves 
approximately 10±1.2% higher task completion 
rates compared to DT, which substantiates the gen-
eralization capability of the proposed method in 
complex dynamic environments. This improvement 
is primarily attributed to the adaptive fine-tuning 
cycles that enable real-time model adaptation.

## § Conclusion

This article addresses the challenges of coordi-
nation and dynamic resource adaptation faced 
by the integration of LAMs in vehicle-road-cloud 
collaborative systems. It proposes an agent-based 
network architecture and resource management 
method. Through large-scale pre-training in the 
cloud and lightweight model deployment at the 
edge, real-time inference and decision-making are 
achieved. Additionally, the lifecycle management 
method proposed in this article jointly optimizes 
the sampling rate, model pruning, and resource 
allocation, effectively balancing model perfor -
mance with resource consumption. The use of 
multi-dimensional resource management models 
effectively supports resource coordination and 
personalized scheduling in both single-task and 
multi-task scenarios. Experimental results validate 
the feasibility of the proposed method.
FIGURE 5. Performance comparison in dynamic V2X scenario.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 6
few-shot fine-tuning is performed in local environments using
a small set of task-specific samples, thereby producing task-
adaptive local scheduling models. These models support low-
latency and high-efficiency resource scheduling under the
collaborative vehicle–road–cloud architecture.
Compared to traditional RL approaches (e.g., value func-
tion approximation), D-LAM demonstrates significant advan-
tages in handling large-scale historical trajectories and high-
dimensional state spaces. Leveraging its auto-regressive se-
quence modeling capability, D-LAM captures temporal depen-
dencies more effectively, generating more robust and general-
izable scheduling policies, thereby enabling better adaptation
to complex V2X scenarios and enhancing overall service
quality and resource utilization efficiency.
B. Multi-Task Scenarios
In the vehicle-road-cloud collaborative computing network
environment, vehicles often need to execute multiple tasks in
parallel, such as real-time perception, behavior prediction, path
planning, local map construction, and model updates. These
tasks significantly differ in terms of time sensitivity, computa-
tional complexity, and collaboration requirements. Thus, there
is an urgent need to develop a multi-task management archi-
tecture that integrates task recognition, dynamic scheduling,
and collaboration capabilities.
To address these needs, this paper proposes a DM-LAM
to achieve multi-task resource management based on LAMs.
By leveraging the powerful learning capabilities of LAM,
the method optimizes task scheduling and resource alloca-
tion, enabling efficient decision-making in concurrent multi-
tasking scenarios. The DM-LAM frames the resource schedul-
ing process as a sequential decision-making task with long-
term dependencies. Different tasks exhibit distinct resource
utilization patterns, such as computation, communication, and
caching, during execution. As a result, the method introduces
a specialized expert network within the LAM architecture and
implements dynamic expert scheduling through a task feature-
driven gating mechanism. This approach offers differentiated
resource optimization paths for various task types. For tasks
with high computational loads, the DM-LAM uses an expert
selection mechanism to prioritize nodes with computational
advantages. It dynamically determines whether to perform lo-
cal processing, collaborate at the edge, or offload to the cloud,
considering the task’s data scale and communication overhead.
For communication-sensitive tasks, the model prioritizes ex-
pert strategies with low-latency transmission capabilities and
adjusts communication paths based on real-time channel con-
ditions, ensuring optimal task selection across multiple paths,
such as V2V and V2I. For tasks involving large-scale data
caching and forwarding, DM-LAM utilizes an expert routing
mechanism to flexibly match nodes with caching advantages or
data pre-fetching capabilities, enabling coordinated scheduling
of computation and caching. Additionally, the DM-LAM takes
full advantage of resource disparities among heterogeneous
nodes in the computing network. In scenarios where multiple
tasks arrive simultaneously, it dynamically balances global
resource scheduling with local task optimization. In resource-
constrained environments, the model actively selects real-time
Fig. 5. Performance comparison in dynamic V2X scenario
responses for high-priority tasks based on task priority, delay
sensitivity, and resource consumption characteristics.
The DM-LAM can dynamically optimize resource schedul-
ing strategies in complex vehicle-road-cloud collaborative
environments, tailoring solutions to the varying demands of
multiple tasks. It effectively coordinates resource conflicts
between tasks, providing an efficient and stable multi-task
resource management solution.
I V. N
UMERICAL RESULTS AND ANAL YSIS
Based on the proposed architecture, the developed method
enables reliable interaction in dynamic vehicle-road-cloud
scenarios through a model lifecycle management scheme.
The simulation focuses on a V2X scenario with single RSU
assisted multi-vehicle cooperative perception: vehicles are
randomly distributed within a 150 meters radius of a fixed
RSU, with speeds ranging from 20 to 60 km/h. Both the
vehicles and the RSU are equipped with 32GB of memory,
and the bandwidth between them is set to 50-100 Mbps. A
resource allocation strategy dataset is constructed using the
proximal policy optimization (PPO) algorithm.
Specifically, the state space incorporates the varying number
of vehicles, their positions and speeds relative to the RSU,
vehicle-to-RSU CSI, and available RSU computing resources.
The action space consists of data upload bandwidth and
inference compute resource allocation strategies. The reward
function comprehensively considers communication and com-
putation resource utilization alongside task latency. The dataset
is divided into pre-training (60%), fine-tuning (30%), and
evaluation (10%) subsets based on vehicle count variations.
Experiments are conducted on NVIDIA A6000 GPU. The
LAM is built upon Qwen2.5-14b, integrated with task-specific
feature extraction modules and prompt engineering. Both
pre-training and fine-tuning (with LoRA rank=16, alpha=64)
phases employ the AdamW optimizer, using a batch size of
64. The pre-training learning rate is set to 5× 10
−5, while the
fine-tuning learning rate is reduced to 1 × 10−5.
We compare the proposed method with DT, PPO, and ran-
dom selection baselines by simulating time-varying scenario
dynamics in the dataset to evaluate the resource utilization
changes achieved by different resource allocation schemes. As
shown in Fig. 5, the proposed model demonstrates superior
FIGURE 6. Performance comparison in various scenario.
IEEE COMMUNICA TIONS MAGAZINE – LARGE AI MODELS FOR COMMUNICA TIONS 7
Fig. 6. Performance comparison in various scenario
performance compared to DT, PPO, and random selection.
Moreover, the results indicate that our method effectively
recalibrates model performance in response to dynamic sce-
nario changes, ensuring reliable inference. This is attributed
to the adaptive fine-tuning cycles and update cycles in our
framework, which promptly stabilize inference performance
through model adjustments when significant scenario shifts
occur.
To validate the model’s generalization capacity, we con-
ducted the experiment under diverse scenarios with varying
vehicle numbers. As illustrated in Fig. 6, while DT and PPO
exhibited significant degradation of task completion rates with
increasing vehicle numbers, our model demonstrated con-
sistent stability and maintained higher performance through
lifecycle management scheme. The experimental results show
that our approach achieves approximately 10± 1.2% higher
task completion rates compared to DT, which substantiates
the generalization capability of the proposed method in com-
plex dynamic environments. This improvement is primarily
attributed to the adaptive fine-tuning cycles that enable real-
time model adaptation.
V. C
ONCLUSION
This paper addresses the challenges of coordination and
dynamic resource adaptation faced by the integration of LAMs
in vehicle-road-cloud collaborative systems. It proposes an
agent-based network architecture and resource management
method. Through large-scale pre-training in the cloud and
lightweight model deployment at the edge, real-time inference
and decision-making are achieved. Additionally, the lifecycle
management method proposed in this paper jointly optimizes
the sampling rate, model pruning, and resource allocation,
effectively balancing model performance with resource con-
sumption. The use of multi-dimensional resource management
models effectively supports resource coordination and person-
alized scheduling in both single-task and multi-task scenarios.
Experimental results validate the feasibility of the proposed
method.
VI. A
CKNOWLEDGMENT
This work was supported by the National Key Re-
search and Development Program of China under Grant
2024YFE0200300, the National Natural Science Foundation of
China under Grant 61931005, and the Fundamental Research
Funds for the Central Universities under Grant 2025TSQY05.
R
EFERENCES
[1] J. Zhao, W. Zhao, B. Deng, Z. Wang, F. Zhang, W. Zheng, W. Cao, J. Nan,
Y . Lian, and A. F. Burke, “Autonomous driving system: A comprehensive
survey,” Expert Systems with Applications, vol. 242, p. 122836, 2024.
[2] F. Qu, F. Du, and L. Zong, “Design and construction of cloud data
platform for intelligent connected vehicles,” in Proc. 2024 Int. Conf.
Smart City and Information System (ICSCIS), New Y ork, NY , USA:
ACM, 2024, pp. 397–401.
[3] Q. Cui, X. Y ou, N. Wei, et al., “Overview of AI and communication for
6G network: fundamentals, challenges, and future research opportunities,”
Sci. China Inf. Sci., vol. 68, art. 171301, 2025.
[4] W. Wu, C. Zhou, M. Li, H. Wu, H. Zhou, N. Zhang, X. S. Shen, and W.
Zhuang, “AI-Native Network Slicing for 6G Networks,” in IEEE Wireless
Communications, vol. 29, no. 1, pp. 96–103, Feb. 2022.
[5] Z. Chen, Q. Sun, N. Li, X. Li, Y . Wang and C. -L. I, “Enabling Mobile AI
Agent in 6G Era: Architecture and Key Technologies,” in IEEE Network,
vol. 38, no. 5, pp. 66-75, Sept. 2024.
[6] H. Choi, Y . Lee, G. Kim, E. Lee, and Y . Nam, “Resource cluster-based
resource search and allocation scheme for vehicular clouds in vehicular
ad hoc networks,” Sensors, vol. 24, no. 1, 2024.
[7] S. Xu and C. Guo, “Computation offloading in a cognitive vehicular
network with vehicular cloud computing and remote cloud computing,”
Sensors, vol. 20, no. 23, p. 6820, Nov. 2020.
[8] M. Xu, D. Niyato, J. Kang, Z. Xiong, S. Mao, Z. Han, D. I. Kim,
and K. B. Letaief, “When Large Language Model Agents Meet 6G
Networks: Perception, Grounding, and Alignment,” in IEEE Wireless
Communications, vol. 31, no. 6, pp. 63–71, Dec. 2024.
[9] J. Du, T. Lin, C. Jiang et al., “Distributed Foundation Models for
Multi-Modal Learning in 6G Wireless Networks,” IEEE Wireless Com-
munications, vol. 31, no. 3, pp. 20–30, Jun. 2024.
[10] Z. Chen, H. H. Y ang, Y . Tay et al., “The Role of Federated Learning in
a Wireless World with Foundation Models,” IEEE Wireless Communica-
tions, vol. 31, no. 3, pp. 42–49, Jun. 2024.
[11] R. Zhang, K. Xiong, H. Du, D. Niyato, J. Kang, X. S. Shen, and
H. V . Poor, “Generative AI-enabled vehicular networks: Fundamentals,
framework, and case study,” IEEE Network, vol. 38, no. 4, pp. 259–267,
Jul. 2024.
[12] F. Jiang, Y . Liu, L. Dong, C. Pan, and X. Y ou, “Large language model
enhanced multi-agent systems for 6G communications,” in IEEE Wireless
Communications, vol. 31, no. 6, pp. 48–55, Dec. 2024.
[13] J. Zhang, J. Li, Z. Wang, L. Shi, S. Jin, W. Chen, and H. V . Poor,
“Decision transformers for wireless communications: A new paradigm of
resource management,” IEEE Wireless Communications, vol. 32, no. 2,
pp. 180–186, Apr. 2025.
[14] Y . Nan, S. Jiang, and M. Li, “Large-scale video analytics with
cloud–edge collaborative continuous learning,” ACM Transactions on
Sensor Networks, vol. 20, no. 1, pp. 1–23, Oct. 2023.
[15] S. Liu, G. Y u, R. Yin, J. Y uan and F. Qu, ”Adaptive Batchsize Selection
and Gradient Compression for Wireless Federated Learning,” GLOBE-
COM 2020 - 2020 IEEE Global Communications Conference, Taipei,
Taiwan, 2020, pp. 1-6, doi: 10.1109/GLOBECOM42002.2020.9322122.
Xinxin He (hxx 9000@bupt.edu.cn) is currently an Associate Professor with
Beijing University of Posts and Telecommunications (BUPT) and the Beijing
Key Laboratory of Network System Architecture and Convergence, China.
She is a Member of IEEE.
Yang Yang (sherry yangyang@bupt.edu.cn) is currently pursuing the M.S.
degree at Beijing University of Posts and Telecommunications, China.
Zhiyong Yang (yangzhiyong@bupt.edu.cn) is currently pursuing the M.E.
degree at Beijing University of Posts and Telecommunications, China.
Yifei Gao (yifeigao@bupt.edu.cn) is currently pursuing the M.S. degree at
Beijing University of Posts and Telecommunications, China.
Changchuan Yin (ccyin@bupt.edu.cn) is currently a Professor with the
School of Information and Communication Engineering at BUPT. He was the
co-recipient of the IEEE Marconi Prize Paper Award in 2023 and the IEEE
International Conference on Wireless Communications and Signal Processing
Best Paper Award in 2009. He is a Senior Member of IEEE.
Shanzhi Chen (chensz@cict.com) is currently the CTO and EVP of R&D at
China Information and Communication Technology Group Co., Ltd. (CICT),
the Director of the State Key Laboratory of Wireless Mobile Communications,
and a Board Director of SMIC. He is a Fellow of IEEE.
This article addresses the 
challenges of coordination 
and dynamic resource 
adaptation faced by the 
integration of LAMs in vehi -
cle-road-cloud collaborative 
systems.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Communications Magazine • April 2026
41

## § Acknowledgment

This work was supported by the National Key 
Research and Development Program of China 
under Grant 2024YFE0200300, the National Nat-
ural Science Foundation of China under Grant 
61931005, and the Fundamental Research Funds for 
the Central Universities under Grant 2025TSQY05.

## § References

[1] J. Zhao et al., “Autonomous Driving System: A Comprehen-
sive Survey,” Expert Systems with Applications, vol. 242, 
2024, p. 122836.
[2] F. Qu, F. Du, and L. Zong, “Design and Construction of 
Cloud Data Platform for Intelligent Connected Vehicles,” 
Proc. 2024 Int’l. Conf. Smart City and Information System 
(ICSCIS), New York, NY, USA: ACM, 2024, pp. 397–401.
[3] Q. Cui et al., “Overview of AI and Communication for 6G 
Network: Fundamentals, Challenges, and Future Research 
Opportunities,” Sci. China Inf. Sci., vol. 68, art. 171301, 2025.
[4] W. Wu et al., “AI-Native Network Slicing for 6G Networks,” 
IEEE Wireless Commun., vol. 29, no. 1, Feb. 2022, pp. 
96–103.
[5] Z. Chen et al., “Enabling Mobile AI Agent in 6G Era: Archi-
tecture and Key Technologies,” IEEE Network, vol. 38, no. 5, 
Sept. 2024, pp. 66–75.
[6] H. Choi et al., “Resource Cluster-Based Resource Search and 
Allocation Scheme for Vehicular Clouds in Vehicular Ad 
Hoc Networks,” Sensors, vol. 24, no. 1, 2024.
[7] S. Xu and C. Guo, “Computation Offloading in A Cogni-
tive Vehicular Network with Vehicular Cloud Computing 
and Remote Cloud Computing,” Sensors, vol. 20, no. 23, p. 
6820, Nov. 2020.
[8] M. Xu et al., “When Large Language Model Agents Meet 
6G Networks: Perception, Grounding, and Alignment,” IEEE 
Wireless Commun., vol. 31, no. 6, Dec. 2024, pp. 63–71.
[9] J. Du et al., “Distributed Foundation Models for Multi
-
Modal 
Learning in 6G Wireless Networks,” IEEE Wireless Commun., 
vol. 31, no. 3, Jun. 2024, pp. 20–30.
[10] Z. Chen et al., “The Role of Federated Learning in a Wire-
less World with Foundation Models,” IEEE Wireless Com-
mun., vol. 31, no. 3, June 2024, pp. 42–49.
[11] R. Zhang et al. , “Generative AI-Enabled Vehicular Net -
works: Fundamentals, Framework, and Case Study,” IEEE 
Network, vol. 38, no. 4, July 2024, pp. 259–67.
[12] F. Jiang et al., “Large Language Model Enhanced Multi-
Agent Systems for 6G Communications,” IEEE Wireless Com-
mun., vol. 31, no. 6, Dec. 2024, pp. 48–55.
[13] J. Zhang et al., “Decision Transformers for Wireless Commu-
nications: A New Paradigm of Resource Management,” IEEE 
Wireless Commun., vol. 32, no. 2, Apr. 2025, pp. 180–86.
[14] Y. Nan, S. Jiang, and M. Li, “Large
-
Scale Video Analytics 
with Cloud-Edge Collaborative Continuous Learning,” ACM 
Trans. Sensor Networks, vol. 20, no. 1, Oct. 2023, pp. 1–23.
[15] S. Liu et al., “Adaptive Batchsize Selection and Gra -
dient Compression for Wireless Federated Learning,” 
GLOBECOM 2020 — 2020 IEEE Global Commun. Conf. , 
Taipei, Taiwan, 2020, pp. 1–6. DOI: 10.1109/GLOBE -
COM42002.2020.9322122.
b IogrAPhIes
XinXin He [M] (hxx_9000@bupt.edu.cn) is currently an Associate 
Professor with Beijing University of Posts and Telecommunica-
tions (BUPT) and the Beijing Key Laboratory of Network System 
Architecture and Convergence, China. 
Yang  Yang  (sherry_yangyang@bupt.edu.cn) is currently pursu-
ing the M.S. degree at Beijing University of Posts and Telecom-
munications, China.
ZHiYong  Yang  (yangzhiyong@bupt.edu.cn) is currently pursuing 
the M.E. degree at Beijing University of Posts and Telecommu -
nications, China.
Yifei g ao  (yifeigao@bupt.edu.cn) is currently pursuing the M.S. 
degree at Beijing University of Posts and Telecommunications, 
China.
CHang CHuan  Yin [SM] (ccyin@bupt.edu.cn) is currently a Pro-
fessor with the School of Information and Communication Engi-
neering at BUPT. He was the co-recipient of the IEEE Marconi 
Prize Paper Award in 2023 and the IEEE International Confer-
ence on Wireless Communications and Signal Processing Best 
Paper Award in 2009. 
SHan ZHi CHen  [F] (chensz@cict.com) is currently the CTO and 
EVP of R&D at China Information and Communication Tech-
nology Group Co., Ltd. (CICT), the Director of the State Key 
Laboratory of Wireless Mobile Communications, and a Board 
Director of SMIC.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:53:14 UTC from IEEE Xplore.  Restrictions apply.
