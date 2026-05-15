---
paper_id: "paper-2592"
source_pdf_sha: "12b1ce71d584c19f4a15d47a746c719f64778c65c0734843832a7885769b4d27"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 4
  page_count: 14
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2592 — fulltext
## §unknown-1

1
Foundation Model Enhanced Joint Multi-Hop Task
Offloading in Dynamic R2X/V2X-based Edge
Computing Networks
Mingqi Han, Xinghua Sun,Member,IEEE, Xijun Wang,Member,IEEE,
Wen Zhan,Member,IEEE, Xiang Chen,Member,IEEE, and Tony Q. S. Quek,Fellow,IEEE
Abstract—Recent popularization of the Internet of Vehicles
(IoVs) and vehicles-to-everything (V2X) enables the emergence
of real-time vehicular applications, posing challenges to resource-
limited vehicles. Toward this end, vehicle edge computing (VEC)
has been proposed to alleviate the computational burden on
vehicles by leveraging resources from roadside units (RSUs)
and VEC servers. While existing works mainly focus on the
task requirement for either vehicles or RSUs, the joint task
offloading for both V2X and RSUs-to-everything (R2X) has not
been fully studied. In this paper, we aim at optimizing the task
offloading strategies for both vehicles and RSUs, and adopt
a multi-hop task offloading manner to fully utilize the VEC
network resources. This problem introduces a severe state-action
space shift issue with varying dimensions and representation,
which poses challenges for conventional DRL approaches. To
address it, we propose a Bidirectional Encoder Representations
from Transformers (Bert)-based matching Q-network (BMQN)
algorithm. First, we design the BMQN model to efficiently
capture correlations among all vehicles and RSUs through bi-
directional attention. Then, we propose type-embedded grouped
attention and available action embedding to mitigate the over-
fitting sequence length issue, thereby enhancing generalization
capacity. Moreover, we propose to address the state-action space
shift issue through a matching-based manner, which can sig-
nificantly enhance the task offloading ability by matching the
states among devices. Simulation results demonstrate that: 1)
the BMQN can achieve much better performance than other
approaches in scenarios comprising various numbers of vehicles
and RSUs as well as diverse road lengths; 2) the BMQN
has sufficient generalization capacity to adapt to inexperienced
scenarios through matching-based architecture and available
action embedding.
Index Terms—Vehicle Edge Computing, Multi-hop Transmis-
sion, Joint Task Offloading, Intelligent Transportation Systems,
Reinforcement Learning, Foundation Model

## § Introduction

O
WINGto growing popularization of intelligent vehi-
cles, the Internet of Vehicles (IoVs) and vehicles-to-
everything (V2X) have emerged to support communication
M. Han, X. Sun and W. Zhan are with the School of Electron-
ics and Communication Engineering, Sun Yat-Sen University, China
(Email:hanmq@mail2.sysu.edu.cn, sunxinghua@mail.sysu.edu.cn, zhanw6
@mail.sysu.edu.cn).
X. Wang and X. Chen are with the School of Electronics and In-
formation Technology, Sun Yat-Sen University, China (Email: wangxi-
jun@mail.sysu.edu.cn, chenxiang@mail.sysu.edu.cn)
Tony Q. S. Quek is with Information System Technology and Design Pillar,
Singapore University of Technology and Design, Singapore 487372 (e-mail:
tonyquek@sutd.edu.sg).
for intelligent transportation services, e.g., autonomous driv-
ing, video streaming and location mapping [1], [2]. In IoV ,
dedicated short-range communication technology and cellular
network technology are widely applied to enhance vehicle-to-
infrastructure (V2I) and vehicle-to-vehicle (V2V) communi-
cation [3], [4].
In IoV , many real-time applications, such as artificial intelli-
gence, image-aided navigation and intelligent vehicle control,
rely on both communication and computational resources.
However, IoV frameworks focus mainly on optimizing com-
munication capabilities, resulting in a bottleneck for the adop-
tion of computationally intensive vehicular applications. To
address the increasing demand for computational resources,
vehicular edge computing (VEC) has been proposed by in-
tegrating with mobile-edge computing (MEC) [5], [6]. In
VEC networks, roadside units (RSUs) are strategically de-
ployed along the road near vehicles, thereby providing low-
latency computational support. In particular, considering the
inevitable communication and computation overhead, VEC
targets computationally intensive and delay constrained tasks.
By offloading tasks to these RSUs, vehicles can leverage
distributed computational resources, significantly enhancing
system performance. Within this paradigm, intelligent task
offloading becomes critical. For example, executing all tasks
locally results in the waste of computational resources in
the VEC network, while indiscriminate offloading to RSUs
may introduce communication overhead and queuing delays,
especially in dense device environments. These challenges
have driven extensive research into optimizing task offload-
ing strategies for VEC networks [7]–[20]. Studies show that
selectively offloading tasks to RSUs or nearby vehicles can
substantially reduce both execution costs and latency, striking
a balance between resource utilization and efficiency.
Aforementioned VEC studies [5]–[20] primarily focus on
optimizing task offloading strategies from the vehicle-centric
perspective. In addition to the vehicle perspective, emerging
RSU-generated applications like road traffic management and
autonomous navigation [21] are also computationally intensive
and delay constrained, which require task offloading strategies
from the RSU perspective. To address this, RSU-to-vehicle
(R2V) communication has been introduced, enabling RSUs to
leverage vehicle computational resources for task execution
[22]–[25]. Furthermore, traditional single-hop offloading re-
stricts viable offloading targets due to vehicle mobility and
RSU coverage limitations, resulting in underutilized VEC
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
2
network resources. This limitation has spurred interest in
multi-hop task offloading [12], [25]–[27], where nearby ve-
hicles act as relays to extend offloading reach. By treating
nearby vehicles as relay nodes, tasks from RSUs can be
further routed to out-of-coverage vehicles, thereby maximizing
resource utilization across the VEC network.
With the rapid advancement of VEC, computational de-
mands are increasing not only for vehicles but also for RSUs.
While existing studies address task offloading from either
the vehicle or the RSU perspective, they overlook scenarios
where both entities have concurrent computational demands.
In this paper, we aim at jointly optimizing the task offload-
ing strategies for both V2X and RSUs-to-everything (R2X).
Specifically, tasks generated by vehicles and RSUs can be
offloaded to all other nodes, i.e., vehicles, RSUs and the cloud
center via multi-hop transmissions. However, given that both
the network topology and the offloading positions space are
related to the number of vehicles and RSUs, this joint task
offloading problem for both vehicles and RSUs in dynamic
VEC networks poses significant challenges for current task
offloading schemes.
A. Literature Review
Current task offloading strategies can be broadly classified
into two main categories, conventional optimization-based
schemes [7]–[14] and Deep Reinforcement Learning (DRL)-
based schemes [15]–[20]. Conventional schemes, e.g., greedy
and game theory-based approaches, can effectively obtain the
near-optimal solutions based on special architectures and con-
figurations of the problem. In [7], a greedy heuristic algorithm
was proposed to optimize the V2X service placement by as-
signing services to the nearest computing node with sufficient
capacity, leading to low algorithmic complexity. Similarly, [8]
compared the task offload algorithms based on game theory
and based on approximate load balancing in VEC networks,
highlighting the importance of load balancing between edge
servers. In [12], the multi-hop offloading problem is approxi-
mated as a generalized allocation model, and the greedy and
bat algorithms were adopted to address it by constraining the
maximum hop counts. Despite the domain-specific advantages,
conventional methods face inherent limitations. First, they
exhibit a trade-off between computational complexity and
solution quality [28]. Second, these strategies are typically
tailored to specific problem configurations, e.g., fixed network
topologies, which may encounter severe performance degra-
dation in dynamic VEC scenarios.
Recently, Deep Reinforcement Learning (DRL) has
achieved great success in sequential decision problems. By
training the model offline and deploying the converged model
online, the DRL approach achieves excellent decision making
capability with low computational complexity. Motivated by
it, the DRL-based task offloading strategies become popular
in the VEC network [15]–[17], [19]. In [15], a twin delayed
deep deterministic policy gradient-based approach is proposed
to minimize task execution time and energy cost by jointly
optimizing the task offloading and resources allocation for
V2V and vehicles-to-RSUs (V2R). In [16], considering het-
erogeneous resources among vehicles, RSUs and the VEC
server, the asynchronous advantage actor-critic is introduced
for task offloading and multi-resource management. By regard-
ing vehicles as multiple agents, a multi-agent reinforcement
learning (MARL)-based scheme is proposed to address the
task offloading problem in dynamic VEC networks [19].
B. Motivation
The joint task offloading problem for both V2X and R2X
addressed in this paper, where tasks from vehicles and RSUs
can be offloaded to any device in the VEC network via multi-
hop transmission, comprises three primary challenges.
First, the multi-hop transmission and R2X/V2X task of-
floading features lead to an excessive action space, particularly
in large-scale scenarios. With increasing vehicles and RSUs,
the action space increases exponentially. For instance, in a
small-scale VEC scenario with5vehicles,2RSUs, and1
VEC server, the action space size is7 8 = 2097152, which
requires substantial computational resources for conventional
DRL models using multi-layer perception (MLP) and recurrent
neural network (RNN). Moreover, such DRL models cannot
efficiently capture the correlation across vehicles and RSUs,
resulting in inferior performance.
Second, due to vehicle mobility, both the number and posi-
tion of vehicles are varying in dynamic VEC networks. This
dynamic feature introduces nonalignment between scenarios
during training and testing, which requires generalization
capacity in inexperienced scenarios. Since existing DRL-based
task offloading strategies mainly focus on experienced scenar-
ios [15]–[17], [19], [25], these schemes using conventional
models may encounter severe performance degradation in
inexperienced scenarios due to implicit partial observability
[29]. In particular, when the number of vehicles and RSUs
changes, the dimension of the input state and the output offload
action also changes, which poses challenges to conventional
MLP/RNN-based DRL models.
Moreover, since tasks can be offloaded to all devices in
the VEC network through a multi-hop manner, the varying
number of vehicles and RSUs further introduces a severe
state-action space shift issue. For example, denote action
ai = 5as offloading of tasks from deviceito the5-th
device, corresponding to RSU 1 in a VEC scenario with4
vehicles and2RSUs (assuming vehicles are indexed before
RSUs). However, in scenarios with more than5vehicles, a
same actiona i = 5would instead represents offloading task to
the5-th vehicle. Furthermore, when the numbers of vehicles
and RSUs are reduced, e.g.,3vehicles and1RSU, certain
actionsa i = 5is no longer be valid. Since DRL focus on the
fixed state-action space with determined representations, such
action space shift issue significantly degrade the performance,
especially in inexperienced scenarios [30].
C. Contributions and Main Results
In this paper, considering multi-hop task offloading problem
in dynamic VEC networks for both vehicles and RSUs, we
propose Bidirectional Encoder Representations from Trans-
formers (Bert)-based matching Q-network (BMQN) approach
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
3
to minimize the task execution time by optimizing the joint
tasks offloading decision for both V2X and R2X.
For the first issue, we design a Bert-enhanced BMQN
model that dynamically adapts to the scale of VEC networks
while maintaining parameter efficiency. Unlike conventional
MLP and RNN-based DRL architectures applied in scenarios
with fixed input-output mapping dimensions, BMQN leverages
a foundation model-based Bert with bidirectional attention
mechanisms to adaptively scale to the number of vehicles
and RSUs without parameter overhead. Moreover, through
the bi-directional attention, the BMQN model can contex-
tually capture correlations among vehicles and RSUs [31].
In the BMQN model, the embeddings for heterogeneous
nodes, including vehicles, RSUs and the cloud server, can
be dynamically weighted through cross-device attention to
capture real-time resource availability and spatial relationships.
This bidirectional attention mechanism allows the Bert module
to distill intrinsic correlations between entities, significantly
enhancing offloading performance.
For the second issue, we propose type-embedded grouped
attention and available action embedding in the BMQN model
to enhance the generalization capacity. Considering the total
number of vehicles and RSUs as the sequence length, LLMs
encounter severe performance degradation in inexperienced
scenarios due to the over-fitting sequence length issue for
foundation models [32]. Specifically, positional embedding
serves as important relationship information in transformer-
based foundation models. When the number of devices is
different from that during training, inexperienced position
information leads to inappropriate attention weight, resulting
in performance degradation [33], [34]. In the BMQN, instead
of conventional positional indices, we propose to leverage
the device types, i.e., vehicle, RSU and cloud center, as the
grouped attention to provide device information for vehicles
and RSUs. In particular, we further propose an available action
embedding in the BMQN model to provide information on
the current task offloading space, which further enhances the
generalization capacity.
For the third issue, we propose to address this joint task
offloading problem with the state-action space shift issue
through a novel matching-based manner. Conventional DRL
schemes aim to estimate Q-values for a fixed action space,
which is insufficient for this dynamic scenario. Instead of
directly calculating Q-values, we propose a pairwise state
matching scheme in the BMQN model to adaptively compute
Q-values for each offloading decision across vehicles and
RSUs, which can adapt to the shifted state-action space.
Specifically, we deploy two independent Bert modules in the
BMQN to extract the hidden state for each vehicle and RSU
when serving as offloading initiator and receiver, respectively.
Then, these hidden states can be jointly matched to obtain the
Q-values, which can be then used to determine the joint task
offloading strategy. This matching-based architecture ensures
that the output vector size dynamically adjusts to the current
shifted action space without requiring modifications to the
model parameters. By emphasizing the learning of relation-
ships among agent states instead of relying on a fixed state-
action space, the BMQN model can enhance task offloading
performance in both experienced and inexperienced scenarios.
The main contributions of our work are summarized as
follows:
•We design a foundation model-based BMQN to adapt to
the dynamic scale of VEC networks while efficiently cap-
turing the correlation among vehicles and RSUs, thereby
addressing the issue of varying number of vehicles and
RSUs in dynamic VEC networks. Then, we propose type-
embedded grouped attention to mitigate the over-fitting
sequence length issue of the foundation model, in which
the device type embedding serves as group attention
instead of conventional position indices. Moreover, we
propose an available action embedding to identify the
current action space, which further enhances the general-
ization capacity in inexperienced scenarios.
•We propose a novel matching-based architecture within
the BMQN model to effectively address the challenging
state-action space shift issue. In the BMQN, we utilize
two independent Bert modules to extract hidden states
for each vehicle and RSU when they act as offloading
initiators and receivers, respectively. These hidden states
are then jointly matched to determine the optimal task
offloading actions. By focusing on learning the corre-
lations among devices rather than relying on Q-values
within a fixed state-action space, the BMQN significantly
enhances task offloading performance.
•We evaluate the performance of proposed BMQN in
both experienced and inexperienced dynamic VEC sce-
narios with varying number of vehicles, RSUs and di-
verse road length. Simulation results demonstrate that
the BMQN can achieve significantly better performance
and generalization capacity in all scenarios compared
with conventional greedy scheme and other popular DRL
algorithm as well as other foundation model-based actor-
critic approaches.
D. Outline
The remainder of the paper is organized as follows: Section
II formulates the background of foundation models. Section
A. elaborates the system model and problem of interest in
VEC networks. Section IV illustrates the proposed BMQN
algorithm. Section V demonstrated the simulation results, and
the conclusion are provided in section VI.

## § Preliminaries

A. F oundation Model
Recently, Large Language Models (LLMs) have emerged as
one of the most popular artificial intelligence (AI) techniques,
which has widely revolutionized the natural language process
(NLP) domain, e.g., GPT [35], [36]. LLMs have revolutionized
various domains through its awesome comprehending and
inferring ability in human-text data [37]. LLMs are trained
on vast amounts of diverse text data and are designed to
understand and generate human language, which is widely
applied in NLP tasks, e.g., question-answering, text generation
and text summarization. Through the transformer architecture
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
4
Fig. 1. The Bert model utilizes bi-directional attention to capture the
relationship across input tokens, in which both the former and latter tokens
and corresponding hidden states are passed to the module for current token.
“Trm” represents the transformer architecture.
Fig. 2. The GPT-based model using uni-directional attention to capture
the relationship between input tokens, in which only the former tokens and
corresponding hidden states are passed to the module for current token.
and massive model parameters, LLMs can process high-
dimensional data and generate large-scale text, making them
efficient for a variety of NLP tasks. However, LLMs focus
on NLP tasks with human-text data, which obstacles its
application in tasks of other domains. To address downstream
tasks that involve domain-specific data, the foundation model
and the fine-tuning technique are introduced. The foundation
model is a type of LLM that serves as the starting point
for constructing more specialized models aiming at the task-
specific domain. Similarly, the foundation model is pre-trained
with diverse human-generated text data as that of LLMs to
establish comprehending ability on large-scale input vectors.
Due to the great inferring and comprehending ability of
foundation model, there is a growing interest in integrating
it into wireless scenarios [38]–[41].
Foundation models can be roughly divided into two types,
e.g., the Bert-based models using bi-directional attention and
the GPT-based models using uni-directional attention. As Fig.
1 illustrates, by sharing the tokens and hidden states among
multiple transformer modules using bi-directional attention,
Bert-based models can aggregate information among input
tokens and capture the contextual feature [31]. Therefore,
the Bert-based model illustrates better performance in feature
extraction tasks. For GPT-based models, as Fig. 2 illustrates,
the uni-directional attention is applied, in which only the
Fig. 3. The considered VEC network with single VEC server,multiple RSUs
and vehicles. The vehicles moves with different speeds and directions along
the x-axis. The task of each vehicle and RSU can be offloaded to each available
device including vehicle, RSU or VEC server.
former tokens and corresponding hidden states are passed to
modules for the current token [35]. Through uni-directional
attention, GPT-based models can reduce half of the compu-
tational complexity, and achieve better performance in long-
text generation tasks. In this paper, aiming at extracting the
intrinsic relationship among vehicles and RSUs, we adopt the
Bert in the BMQN model to achieve better decision ability.
B. Fine-tune Technique
After pre-training, the foundation model should be further
fine-tuned for downstream tasks. The domain-specific data is
utilized as fine-tuning data. Due to the over-parameterized fea-
ture of foundation models, directly fine-tuning all parameters
in the foundational model results in excessive computational
cost, leading to the emergence of fine-tuning approaches [36].
Recently, the Low-Rank Adaptation (LoRA) has emerged
as one of the most popular fine-tune approaches [42]. By
injecting the trainable low-rank decomposition matrices into
selected linear layers in the transformer while freezing the
original model parameters, the convergence rate can be en-
hanced and the required training cost can be significantly
reduced. Denoting the low-rank decomposition matrices as
A∈ R d×n, B∈ R n×d and weight matrix of original layer
asW∈ R d×d, the procedure of LoRA is given by
h=x∗(W+A∗B),(1)
in whichhandxdenote the output and input of original
linear layer, respectively. In particular, the over-parameterized
model actually resides on a low intrinsic dimension, which
enables efficient fine-tuning of the foundational model us-
ing a reduced parameter space [43]. Therefore, fine-tuning
foundation models using low-rank decomposition matrices in
LoRA can achieve a performance level to that training from
scratch, but with significantly lower training costs and a higher
convergence rate.
III. SYSTEMMODEL ANDPROBLEM OFINTEREST
In this paper, for simplicity, we consider a single road
scenario in the VEC network. As Fig. 3 illustrates, we con-
sider a three-level VEC network comprising a VEC server,
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
5
Fig. 4. Illustration of the task model and queuing model in the VEC network.
multiple RSUs and vehicles. The set of RSUs is denoted as
M={1,2, . . . , M}, and the set of vehicles is denoted asN=
{1,2, . . . , N}. The time within this VEC network is divided
into multiple time slots, denoted as{1,2, . . . , t, t+ 1, . . .}.
As Fig. 4 illustrates, each RSU and vehicle generate an
independent computation task at the beginning of each time
slott. The taskrof deviceiat time slottis characterized
by
 
Sr
i,t, Cr
i,t, dr
i,t

[15], [16], whereS r
i,t denotes the size of
task data,C r
i,t denotes the required CPU cycle per bit of task
data andd r
i,t denotes the execution delay constraint of the
task. For both vehicles and RSUs, tasks are executed through
a first come first serve (FCFS) manner, in which the second
task can be computed only when the computation of the first
task is completed. In particular, the task calculated halfway at
the last time slottwill continue executing in the next time
slott+ 1.
A. Connectivity Model
In this paper, we characterize the connectivity among vehi-
cles and RSUs through connection time, i.e., the duration time
that two devices can establish communication successfully. In
the VEC network, the connection time among vehicles and
RSUs relates to both the communication range of devices and
the mobility of vehicles. For the mobility, we assume that each
vehiclei∈ Nhas its own velocityv i, driving directionθ i ∈
{−1,1}and initial positions
 
xi
0, yi
. In particular, though we
consider that all vehicles drive along the x-axis of the road,
we introduce they-axis for better simulating the positions
of vehicles in practical roads with multiple lanes. For RSU
i∈ M, the velocity is given byv i = 0. Subsequently, the x-
axis position of deviceiat timetis given byx i
t =x i
0+v i·θi·t.
Then, we assume that all vehicles have the same communi-
cation rangeR v, and all RSUs have the same communication
rangeR r. Given the transmission timeτ, the transmission
between transmitteriand receiverjsuccesses only when their
distanceD i,j
t (τ)is always under the communication range
Di,j
t (τ)≤R i, Ri ∈ {R v, Rr},(2)
andD i,j
t (τ)denotes the distance between deviceiandjfrom
timettot+τ
Di,j
t (τ) =
q
(yi −y j)2 +
 
xi
t −x j
t
2
.(3)
Subsequently, we can derive the connection timel i,j
t between
the transmitteriand the receiverj
li,j
t = arg max
τ
Di,j
t (τ),s.t.D i,j
t (τ)≤R i.(4)
B. Communication Model
In this VEC network, we consider that the transmissions
for V2X are conducted through a wireless manner [3]. The
bandwidth for vehicles and RSUs is given byB v andB r,
respectively, and the transmission power for vehicles and
RSUs is given byP v andP r, respectively. In particular,
the direct wireless transmission is successful only when the
receiver is always within the coverage area of the transmitter
during the whole transmission as illustrated in (2). The set of
vehicles within the coverage area of vehiclenand RSUmat
current timetis denoted asN n andN m, respectively. Utilizing
the multi-hop transmission, the vehiclesiandjthat are unable
to communicate directly can establish connection via a middle
vehiclev, when both vehicles are in the coverage area of
middle vehiclei, j∈ N v. Similarly, vehicles can also establish
connection with the out-of-coverage RSUs through the multi-
hop transmission. Then, we consider the transmissions for R2R
and RSUs-to-VEC server are conducted via the optical fiber
cable, which can always ensure a successful transmission. In
particular, the task offloaded from vehicleito the VEC server
should be first transmitted to the nearest RSU, denoted asM i,
and then transmitted to the VEC server.
B.1 Single-hop Transmission
First, we derive the single-hop transmission rate in this
VEC network. For the communication for V2V and V2R, the
wireless transmission rate between transmitteriand receiver
jat timetis given by
wi,j
t (τ) =B i log2

1 + P i
ω·P L i,j(τ)

,(5)
in whichB i, P i denotes the bandwidth and transmission
power for transmitteri, respectively.ωdenotes the noise
power. In particular, according to the V2X channel model in
urban case [3],P L i,j denotes the channel fading from device
ito devicej, which is given by
P Li,j(τ) = 38.77+16.7 log 10(Di,j
t (τ))+18.2 log 10(fc),(6)
in whichD i,j
t (τ)is the distance between devicesiandjfrom
timetto timet+τ, andf c denotes the carrier frequency.
Due to the mobility of vehicles, the average transmission rate
during the connection timel i,j
t is given by
wi,j
t = 1
li,j
t
Z li,j
t
0
wi,j
t (τ)dτ.(7)
Then, the wireless transmission time between vehicleiand
other devicesjcan be derived as
T i,j
w,t =S 1
i,t/wi,j
t ,(8)
in whichS 1
i,t is the task data size of the head-of-line (HOL)
task of vehicleiat timet. To ensure reliable communication,
a successful transmission is contingent upon the connection
duration, requiringT i,j
w,t ≤l i,j
t . In particular, when the trans-
mission time between devicesiandjexceeds the slot duration
T i,j
w,t ≥1sat the current timet, the task generated at the next
slott+ 1will be buffered in a transmission queue of vehicle
iand processed sequentially once the previous transmission is
complete.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
6
For the RSU-to-RSUs, similar to [25], we assume that the
transmission timeT i,j
w,t betweenRSUiandjthrough the op-
tical fiber cable is proportional to the number of transmission
hops
T i,j
w,t =
(
0,ifi=j
|i−j|β,ifi̸=j ,(9)
in whichβrepresents the fixed wired transmission time
between two adjacent RSUs. For RSUs-to-Cloud, we consider
that each RSU can communicate with the VEC server directly,
and the transmission rate is fixed asr R2C. Subsequently, the
transmission timeT i,j
w,t between RSUiand the VEC server is
given byT i,j
w,t =
S1
i,t
rR2C .
Finally, we can summarize the transmission time between
each deviceiandjas
T i,j
w,t =



0,ifi=j
S0,j
i,t /wi,j
t ,elifiorj∈ N
|i−j|β,elifi, j∈ M
S1
i,t
rR2C ,otherwise
,(10)
in which “iorj∈ N” represents the communication between
vehicle and other devices, andi, j∈ Mrepresents the
communication for RSU-to-RSU.
B.2 Multi-hop transmission
Moving forward, we derive the multi-hop transmission
time. Given the task offloading position of deviceiat
timetbya i
t, we denote all possible transmission paths as
{Li
1,t, . . . , Li
n,t, . . .}, in which each path comprises a series
of devices from the beginningito the destinationa i
t,L i
n,t =
{i, n1, . . . , nH , ai
t}. In particular, each candidate devicen k
in the pathL i
n,t is under the coverage area of both its
former devicen k−1 and latter devicen k+1. The connection
time of the multi-hop transmission pathL i
n,t is the minimum
connection time among the connection times of its single-hop
transmission,
li
t = min{l i,n1
t , ln1,n2
t , . . . , lnH ,ai
t
t },(11)
in whichl n1,n2
t is the single-hop link connection time from
devicen 1 ton 2. Aiming at successful task offloading, we
adopt a modified Dijkstra algorithm to find the path with
maximum connection timeL i,∗
t = arg max
Li
t
li
t. Such a problem
is a classical widest path problem, in which Dijkstra’s priority-
based expansion inherently filters suboptimal candidates by
taking the connection time as value of each pathL(P) =
min
ln∈P
{ln}. This approach eliminates the need for manual
screening boundaries and ensures that the optimal path is
identified with minimal computational overhead. Once the
optimal path is determined, the total multi-hop transmission
latency is calculated as the summation of the individual
transmission delays across each hop along that path,
T i
w,t =
H−1X
h=1
T nh,nh+1
w,t +T i,n1
w,t +T nH ,ai
t
w,t
s.t.T i
w,t ≤l i,∗
t , T i
w,t ≤d r
i,t
,(12)
in whichT i
w,t ≤l i,∗
t , andT i
w,t ≤d r
i,t is the connection time
requirement and task delay requirement, respectively.
C. Computation Model
In this paper, we consider a multi-tier VEC network, in
which tasks can be offloaded from all vehicles and RSUs
to all vehicles, RSUs and the the VEC server. The compu-
tation frequency of deviceiis denoted asf i. For vehicles,
we consider that each vehicle has independent computation
capacity from a distribution of vehicle computation frequency
fi ∼f v,∀i∈ N. For RSUs, similarly, we consider that each
RSU has its own computation capacity from the distribution
of RSU computation frequencyf i ∼f r,∀i∈ M. In par-
ticular, considering massive computational resource for the
VEC server, we assume the task computation time for tasks
offloaded to the VEC server can be ignored.
Since we consider an FCFS computation manner as illus-
trated in Fig. 4, the computation time of the current task should
take the remaining tasks in the queue into consideration.
Denoting the task offloading position of deviceiasa i
t and
the remaining task of devicea i
t asm, the total computation
time for deviceiat timetcan be obtained as
T i
c,t =
m+1X
j=1
(Sj
ai
t,t ·C j
ai
t,t)/fai
t
,(13)
in whichS j
ai
t,t andC j
ai
t,t denote the data size and required
computation cycles per bit of taskj.
D. Optimization Model
In this paper, we aim to minimize the average task execution
time for all vehicles and RSUs under the constraints of
connection time and task delay requirement. Denoting the joint
tasks offloading actions asa t, the optimization problem can
be formulated as
min
at
1
(N+M)T
TX
t=1
X
i∈N ∪M
T i
w,t +T i
c,t
s.t.C1 :a i
t ∈ {1, . . . , N, . . . , N+M, N+M+ 1},
C2 :T i
w,t +T i
c,t ≤min(l i,∗
t , dr
i,t),
C3 :wi,j
t ≥w min
(14)
Here, constraint C1 represents that the task can be offloaded to
any vehicle, RSU or the VEC server. Constraint C2 represents
that the task must be completed within the connection time as
well as the delay requirement. Constraint C3 is the minimum
transmission rate requirement to ensure a successful transmis-
sion. To address such a challenging 0-1 integer programming
problem, we propose the BMQN algorithm to optimizea t. In
the next section, we will briefly illustrate the DRL model of
the BMQN.
IV. BMQN ALGORITHM
In this paper, since the task execution time depends on both
the offloading decisions and previous task offloading status,
we formulate this problem as a Markov Decision Process
(MDP). Combining the powerful foundation model with the
popular actor-critic architecture in DRL domain, we propose
the BMQN algorithm to address this challenging problem
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
7
for jointly deciding task offloading positions for both V2X
and R2X. In the following, we will demonstrate the MDP
formulation of the BMQN, followed by the illustrations of the
model architecture and a detailed algorithm procedure.
A. DRL Model F ormulation
In the MDP, the BMQN agent first observes the environmen-
tal state, makes an efficient offloading decision accordingly,
and then receives a reward.
A.1 State
To characterize the joint state of all vehicles and RSUs, we
first establish the local state of each vehicle and RSUiat time
slottass i
t, comprising positions, task buffer status and device
status, which is given by
si
t =

qi
t, t, Ri, P i, vi, f i, S1
i,t, C1
i,t, d1
i,t
	
∈R 9,(15)
in whichq i
t denotes the total required computational resources
(in CPU cycles) for processing all tasks in the queue of
deviceiat time slott.R i, P i, vi, f i comprising the coverage
range, transmission power, velocity and computation capacity
of deviceiserves as the status of devicei.S 1
i,t, C1
i,t, d1
i,t
represents the HOL task of task queue of devicei.
Then, we stack the states of all devices as a joint state
st =

s1
t , . . . , sN
t , sN+1
t , . . . , sN+M
t
	
∈R (N+M)×9 ,(16)
in whichN, Mdenote the number of vehicles and RSUs,
respectively, ands N+m
t denotes the state of RSUm. In
particular, through the stacked two-dimensional states t, the
BMQN model can ensure the offloading decision with same
dimensional ofs t, which adapt to dynamic VEC environments
with varying number of vehicles and RSUs. Moreover, by
integrating multiple transformer modules in the BMQN model,
the BMQN model can efficiently capture the relationship
among all vehicles and RSUs, enhancing the offloading ability.
A.2 Action
As aforementioned, tasks of both vehicles and RSUs can be
offloaded to any devices in the VEC network, i.e., vehicles,
RSUs and the VEC server. Therefore, we define the local
offloading action of deviceiat time slottas
ai
t ∈ {1, . . . , N, N+ 1, . . . , N+M, N+M+ 1} ∈R N+M+1 ,
(17)
in whicha i
t ∈ {1, . . . , N}represents offloading to a vehicle,
ai
t ∈ {N+ 1, . . . , N+M}represents offloading to a RSU
anda i
t =N+M+ 1represents offloading to the cloud server.
Then, the stacked local action of all vehicles and RSUs also
serves as the joint action
at =

a1
t , . . . , aN
t , aN+1
t , . . . , aN+M
t
	
∈R (N+M)×(N+M+1) ,
(18)
in whicha N+m
t denotes the offloading action of RSUm. Such
joint offloading action introduces two challenges. First, since
we aim at enhancing the generalization of BMQN model in
inexperienced scenarios with more devices than that during
training, the BMQN model should always keep the shape of
output action as(N+M)×(N+M+1)regardless the change
of the number of vehiclesNand RSUsM. Second, since
a same action valuea i
t may represents different offloading
decision when the number of vehiclesNand RSUsMvaries,
it further introduces severe action space shift issue. To address
these issues, we propose a matching-based architecture in the
BMQN model, which will be illustrated in next section.
A.3 Reward
As our goal is to minimize the average task execution time
while ensuring delay and connectivity requirements for the
successful task completion rate, we take the negative value
of task execution time as the reward for each device, and
introduce additional punishment when the task is not offloaded
successfully or executed within the required execution delay
di,t, which is given by
ri
t =
(
−(T i
w,t +T i
c,t),if the task executes successfully
α,else ,
(19)
Here,αis a fixed punishment value for unsuccessful offloading
and out-of-time execution due to connection time and task
delay constraints, which can encourage the BMQN model to
learn a better offloading strategy to ensure the requirement for
the successful task completion rate. Then, we also stack the
local reward of each device as a joint reward vector
rt =

r1
t , . . . , rN
t , rN+1
t , . . . , rN+M
t
	
∈R N+M ,(20)
which can better matches the shape of joint states t, and
provide more state-action-reward pairs to accelerate the con-
vergence of model.
B. Model Architecture
In this section, we first demonstrate the model architecture,
and then the input-output mapping of the proposed BMQN
model. Due to the challenging issue of varying shape of action
space(N+M)×(N+M+ 1), we propose a matching-based
architecture in the BMQN model to address it. The BMQN
model is illustrated in Fig. 5. First, we feed forward the x-
axis positionsX t =

x1
t , . . . , xN
t , . . . xN+M
t
	
and the joints t
of both vehicles and RSUs through different embedding layers,
respectively, which are then summed up into a single vector.
In particular, we introduce the x-axis positionsX t instead of
conventional index position embedding to capture the actual
geographical position relationship among devices.
Then, we introduce the available actionA t to mitigate the
over-fitting issue of transformer in the sequence length [13],
i.e., the number of vehicles and RSUs given by
At = (
N
z }| {
1,· · ·,1,
N ∗−N
z }| {
0,· · ·,0,
M
z }| {
1,· · ·,1,
M ∗−M
z }| {
0,· · ·,0,1),(21)
which represents whether the offloading positionsa i
t is suitable
in the current VEC network. Then, the available actiona t is
also feed forward through an embedding layer, concatenated
with aforementioned state, and then passed into the Bert-based
module comprising multiple encoder-only transformers. In par-
ticular, we introduce the type of devices, i.e., vehicle or RSU,
in the transformer-based Bert module as a grouped attention
approach to further mitigate the performance degradation of
BMQN in inexperienced scenarios [33], [34]. Since the work
of LLMs highly lies on the accurate position information of
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
8
Fig. 5. The novel architecture of the proposed BMQN model, in which two different Bert modules are introduced to obtain two different features of input joint
states t. Then, these two features are matched through a mat multiply module to obtain the Q-values of all state-action pairs. In particular, “Trm” represents
the encoder-only transformer as presented in Fig. 1.
input vectors, we replace the original positional embedding
with types of devices in input vectors to avoid the issue of
unlearned positions in inexperienced scenarios.
For the Bert-based module illustrated in Fig. 5, the bidi-
rectional attention mechanism is adopted in the encoder-only
transformer to capture the information of both the previ-
ous devices and the latter devices [31]. Though the GPT-
based decoder-only transformer can achieve better perfor-
mance in long-text generation using left-to-right attention,
the bidirectional encoder-only transformer can better extract
the context information. Since the joint offloading positions
decision mainly relies on the extraction of state features and
relationship among all devices, the encoder-only transformer
in the proposed BMQN model can achieve better performance
than the popular decoder-only transformer. As aforementioned,
we deploy two independent Bert modules to address the joint
multi-hop task offloading problem through a matching-based
manner. In this architecture, the BMQN first extracts two
different hidden featuresh l, hr, respectively, which serve as
image feature and text feature. In particular, we introduce
the LoRA to efficiently fine-tune the over-parameterized Bert
module as illustrated in (1), in which the LoRA layers are
deployed in the query and value layers within all transformer
modules presented in Fig. 5.
After the extraction ofh l andh r, the right hidden feature
hr is then passed to a cloud embedding layer to obtain the
hidden feature of VEC serverh c. In this VEC network,
since the queue state and computation and communication
resources of the VEC server is consistent, we propose a
learnable vectorh c ∈R 1×h with the same length ash l and
hr. Then, in the matching-based architecture, the concate-
nated vector(h r, hc)is multiplied withh l to obtain the Q-
valuesQ t ∈R (N+M)×(N+M+1) . Through this architecture,
the hidden state across vehicles, RSUs and the cloud center
are matched to calculate the offloading actiona t, effectively
capturing their correlations while ensuring that the shape ofa t
dynamically adapts toNandM. By focusing on learning the
correlations among devices rather than relying on Q-values
within a fixed state-action space, the BMQN significantly
enhances task offloading performance.
C. Loss Function
Due to the over-parameterized feature of LLMs, introducing
additional aforementioned BMQN model as the actor may
introduce excessive training cost and worse convergence per-
formance. In the proposed BMQN algorithm, we apply the
BMQN model through a value-based DRL manner. The critic
model is trained to evaluate the Q-value of each state-action
pairQ(s t,a t). The loss function of the BMQN is given by
LBMQN(θ) =E (st,at)∼E

Qθ (st,a t)− ˆQ(s t,a t)
2
=E (st,at)∼Et
"N+MX
i

Qθ

si
t, ai
t

− ˆQ

si
t, ai
t
2
#1
16
(22)
and the target Q -value ˆQ(s t,a t)is given by
ˆQ(s t,a t) =r t +γE
h
max
a
Q(s t+1,a)
i
(23)
Here,Eis the sampled batch from the experience memory and
θdenotes the model parameters of critic.Q θ (st,a t)denotes
the Q-value given states t and actiona t. Through (22), the
BMQN can evaluate the Q-values for each joint offloading
actionagiven specifics, which is then utilized to obtain the
offloading actiona.
D. Algorithm Overview
The overall procedure of the proposed BMQN algorithm is
illustrated in Fig. 6. During execution, each vehicle and RSU
first observes the local states i
t and uploads it to the VEC
server at the beginning of each roundt. Utilizing the BMQN
model, the joint actiona t is calculated and broadcast to all
devices to decide the offloading positions. In particular, the
actiona t is randomly sampled during training to fully explore
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
9
Fig. 6. The overall procedure of the training and execution stage of the
proposed BMQN algorithm.
the action space [44], and is deterministic during execution to
enhance exploitation,
(
at ∼Q(s t,a) +N(0, σ t),during training
at = arg max
a
Q(s t,a),during execution (24)
in whichN(0, σ t)denotes the noise with powerσ t introduced
for exploration. Then, each device receives a local rewardr i
t
and moves to the next states i
t+1. At the end of roundt, the
experienceE t ={s t,a t,r t}is cached in the VEC server. At
the end of each episode, the BMQN model starts training using
the sampled experienceE. During training, the BMQN model
randomly sample a batch of experienceE, obtain their Q -
valueQ(s t,a t), and calculate the loss function presented in
(22) for parameters update. The detailed pseudo-code of the
proposed BMQN is summarized in Algorithm 1.
Algorithm 1BMQN Algorithm
Require:Initialize: BMQN parametersϕ,θ, episodesK, steps per
episodeT, training epochsHand noise powerσ 0
1:Training Phase:
2:Load the pre-trained Bert model parameters to the BMQN model
and initialize embedding, LoRA and classifier layers.
3:forepisodek∈ {1,2, . . . , K}do
4:forstept∈ {1,2, . . . , T}do
5:Obtain joint states t, current device positionsX t and
current available actionA t to calculateQ(s t,a)
6:Randomly sample offloading actiona t from the distribu-
tionQ(s t,a) +N(0, σ t)
7:Receive rewardr t and store experienceE t into memory
8:fortraining epochsh∈ {1,2, . . . , H}do
9:Sample a batch of experience
n
{st,a t,r t}N
i=1
o
t∈E
10:Feed the batch of experience dataEthrough the BMQN
model to calculate and backward the BMQN lossL F Q N
11:Update the parameters of each embedding, LoRA and clas-
sifier layer in the BMQN model according to the total loss, then
decay the noise powerσ t+1 =σ t ·λ.
12:Merge the trained LoRA layers into the original layers of the
Bert-based modules in the BMQN model
V. SIMULATIONRESULTS
In this section, we evaluate our proposed BMQN algorithm
by providing simulation results under different scenarios,
including both experienced and inexperienced scenarios. In the
following, we first illustrate the simulation setting, and then
the detailed performance evaluations will be presented under
different scenarios.
A. Simulation Setting
As aforementioned, we considerNvehicles andMRSUs
and a single VEC server. AllNvehicles are randomly gener-
ated in the beginning of the episode, including both velocity
vi, initial positionsx i
1 and initial tasks(S i,1, Ci,1, di,1). For
RSUs, they are deployed at 400 m intervals along the road,
i.e., there are 3 RSUs in a road with 1100 m length. The trans-
mission power, communication bandwidth and computation
capacity are fixed among episodes. The VEC networks com-
prising different numbers of vehicles or RSUs and different
road lengths are served as different scenarios. The evaluation
of the BMQN in each scenario is averaged by 5 episodes.
In particular, to better evaluate the generalization capacity of
proposed BMQN in inexperienced VEC scenarios with both
small-number and large-number of vehicles, we consider the
number of vehiclesNranging only from 5 to 9 instead 1 to
9 during training. The detailed parameters in evaluation are
summarized in Table I, and the hyper-parameters of BMQN
and baseline approaches are illustrated in Table II.
TABLE I
VEC NETWORKPARAMETERS
Parameters Value
Task delay requirementd i di ∈[3,8]s
Number of vehicles during trainingN N∈ {5,6,7,8,9,10}
Communication range of vehicle and RSUR v, Rr 200m,400m
Bandwidth for vehicle and RSUB v, Br 10,20MHz
Length of road during trainingL [0.7,1.2]km
Minimum transmission ratew min 0.02Mbps
Vehicle transmission powerP v 10dbm
RSU transmission powerP r 50dbm
Vehicle computation capabilityf v [15,20]Gcycles/s
RSU computation capabilityf v [35,40]Gcycles/s
Noise powerω 63dbm
Fixed lossK 20 dB
multi-hop transmission time between RSUsβ 3 s
R2C transmission rater R2C 2Mb/s
TABLE II
HYPER-PARAMETERS OFBMQN
Parameters Value Parameters Value
LoRA rank 8 LoRA Alpha 16
Batch sizeB 300 Optimizer AdamW
B. Baseline Approaches
To present a comprehensive comparison, the following
approaches are introduced to evaluate the performance of the
proposed BMQN algorithm.
•Greedy:First, we introduce the greedy optimization ap-
proach as a baseline, which is widely applied in chal-
lenging integer programming problems for both the VEC
and MEC networks [12], [45]. During simulations, the
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
10
Fig. 7. The model architecture of the baseline BACA approach, in which a
shared Bert module is utilized for obtaining the action of actor and Q-values
of critic.
task of each vehicle and RSU is offloaded to the device
with minimum total task computation time through a
sequential manner
•Soft Actor-Critic (SAC):Then, we introduce the popular
SAC in the DRL domain as a baseline. In the SAC,
stochastic policy is deployed to balance the exploration
and exploitation, thereby enhancing the convergence [46].
In the SAC model, the conventional MLP/RNN-based
actor and critic modules are introduced, which are utilized
to obtain action distribution and Q-values, respectively.
In particular, due to the exponentially increasing size of
action space with respect to the number of devices and
corresponding massive training cost, we only introduce
the SAC in small-scale scenarios.
•Proximal Policy Optimization (PPO):Moreover, we also
introduce the PPO algorithm as a baseline, which is one
of the most popular approaches in DRL domain [47].
Similar to the SAC, we deploy a MLP/RNN-based actor-
critic to obtain action distribution and state-values. Then,
we also introduce the PPO in small-scale scenarios due
to the exponentially increasing action space.
In particular, to comprehensively evaluate the proposed
BMQN, we deploy three approaches for ablation study.
•Bert-based actor-critic with available action embedding
(BACA):For evaluation of the novel matching archi-
tecture of the proposed BMQN model, we propose a
BACA approach as a baseline. The BACA model is
illustrated in Fig. 7, which also takes stateS t, positions
Xt and available actionA t as input. The only difference
between BACA and the BMQN lies in that the BACA
adopts a more popular actor-critic architecture instead
of the matching-based architecture to directly obtain the
joint offloading actiona t from an over-size fixed action
space to achieve generalization capacity for inexperienced
scenarios.
•Bert-based actor-critic (BAC):For evaluation of the
available action embeddingA t, we introduce the BAC
approach. The BAC model has similar architecture similar
to that presented in Fig. 7. The only difference between
BAC and BACA lies on that BAC does not introduceA t
as input information.
•Uni-directional-based actor-critic (UAC):For evaluation
of the bi-directional attention, we introduce the UAC
approach. The UAC model utilizes a decoder-based foun-
dation model with uni-directional attention to capture the
relationship among vehicles and RSUs.
C. Performance Metrics
The following metrics are used to evaluate the performance
of the proposed BMQN algorithm.
•Average task execution time:We demonstrate the average
task execution time of all vehicles and RSUs in each
episode to evaluate the task offloading performance of
the proposed BMQN approach.
•Task completion ratio:Due to the task delay requirement
and device connection time constraint, we demonstrate
the task completion ratio to evaluate the task offloading
ability, which is the number of successful tasks propor-
tioned by the number of all generated tasks.
•Average reward: We demonstrate the average obtained
reward for all vehicles and RSUs to evaluate the overall
performance of the DRL-based BMQN approach, which
is given by 1
(N+M)
P
i∈N,M
ri
t.
D. Exploitation Performance
D.1 Small-scale Static Scenario
In this section, we first evaluate the proposed BMQN
approach in a simple small-scale static scenario with a fixed
road length600mand fixed numbers of vehicles4and RSUs
2. Note that this scenario is already experienced during the
training. The performance comparison on average task execu-
tion time, the task completion ratio and the average reward
are illustrated in Fig. 8a, Fig. 8b and Fig. 8c, respectively.
Obviously, the proposed BMQN approach can significantly
outperform all other approaches on both the task execution
time, task completion ratio and average reward. Compared
with conventional greedy offloading approach, the BMQN can
achieve21%higher reward. Compared with popular DRL-
based SAC approach, the BMQN can achieve25%higher
reward. Such results demonstrate that the BMQN can signifi-
cantly enhance the overall VEC performance. In particular, the
conventional MLP/RNN-based SAC and PPO model illustrate
poor performance due to the massive action space. Specifically,
even in such a small-scale scenario, agents cannot fully
explore the action space with exponentially increasing size,
i.e.,(6 + 1) 6 = 117649, results in convergence to unexpected
local optimums.
Then, we evaluate the key mechanism proposed in the
BMQN model. As aforementioned, in the BMQN, we pro-
pose matching-based architecture to address the action space
shift issue, and introduce the group attention and available
action embedding to address the over-fitting issue for LLMs.
Compared with BACA, the BMQN can achieve11%higher
reward, which illustrate that capture relationship of local states
among different vehicles and RSUs through matching-based
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
11
Fixed Ranges and Number of Vehicles
0.5
1
1.5
2
2.5
3
3.5Average task delay/s
Task Delay Comparison
BAC
BACA
BMQN
SAC
PPO
UAC
Greedy
(a) Average task execution time.
Fixed Ranges and Number of Vehicles
0.8
0.85
0.9
0.95
1
Successful probability
Successful Probability Comparison
BAC
BACA
BMQN
SAC
PPO
UAC
Greedy (b) Task completion ratio.
Fixed Ranges and Number of Vehicles
-3.5
-3
-2.5
-2
-1.5
-1
Average reward
Reward Comparison
BAC
BACA
BMQN
SAC
PPO
UAC
Greedy (c) Average reward.
Fig. 8. Performance comparison between the proposed BMQN and other approaches in a static scenario with fixed road length 600 m and fixed number of
vehiclesN= 4and RSUsM= 1, which is experienced during training.
700m 800m 900m 1000m 1100m
Different Ranges and Number of Vehicles
0
1
2
3
4
5
6Average task delay/s
Task Delay Comparison
BAC
BACA
BMQN
UAC
Greedy
(a) Average task execution time.
700m 800m 900m 1000m 1100m
Different Ranges and Number of Vehicles
0.4
0.5
0.6
0.7
0.8
0.9
1
Successful probability
Successful Probability Comparison
BAC
BACA
BMQN
GAC
Greedy (b) Task completion ratio.
700m 800m 900m 1000m 1100m
Different Ranges and Number of Vehicles
-7
-6
-5
-4
-3
-2
-1
0
Average reward
Reward Comparison
BAC
BACA
BMQN
UAC
Greedy (c) Average reward.
Fig. 9. Performance comparison between the proposed BMQN and other approaches in dynamic scenario with diverse road length and number of vehicles
and RSUs, which are experienced during training.
architecture can enhance the decision performance even in
scenarios without action space shift issue. Subsequently, the
BACA achieves better performance than that of the BAC, high-
lighting that introducing available action embedding enhances
decision-making even in experienced scenarios. Moreover, the
BAC illustrates better performance than the UAC, demon-
strating that bi-directional attention can capture more intrinsic
relationships among vehicles and RSUs.
D.2 Large-scale Dynamic Scenario
Moving forward, we evaluate the proposed BMQN in large-
scale dynamic scenarios with the length of the roadLranging
from700mto1200mand the number of vehicles ranging from
5to10, in which the configurations for testing matches to
that during training. The performance comparison on average
task execution time, the task completion ratio and average
reward of objective function across different scenarios with
varying numbers of vehicles and diverse lengths of road are
illustrated in Fig. 9a, Fig. 9b and Fig. 9c, respectively. In
this large-scale scenario, the proposed BMQN illustrates much
better performance than other approaches in dynamic VEC
networks no matter how the scenario changes. Compared
with the conventional greedy approach, the BMQN achieves
60%higher average reward among each scenario, in which
this improvement is significantly higher than that in previous
small-scale static scenarios. Specifically, such a result may
relate to the exponentially increasing action space. Since the
greedy approach mainly focuses on a few parts of the whole
action space, it encounters severe performance degradation
in large-scale scenarios. Compared with BACA, the BMQN
can achieve12%higher average reward, which is similar to
that within small-scale scenarios. Similarly, the BACA also
demonstrates better performance than the BAC without avail-
able action embedding. In particular, for small-scale scenarios,
i.e.,L= 700m, the BAC has a similar performance as the
UAC. However, with the increasing scale of scenarios, the
BAC illustrates significantly better than the UAC using only
uni-directional attention. Since longer roads can contain more
vehicles and RSUs, such a result emphasizes the importance of
bi-directional attention in joint decision problems, especially
with the increasing number of vehicles and RSUs.
E. Generalization Performance
Moreover, we evaluate the generalization capacity of the
proposed BMQN in several inexperienced scenarios. The
scenario settings are the combination of the length of road
rangesLand the number of vehiclesNgiven by(L, N)∈
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
12
1st Scene 2nd Scene 3rd Scene 4th Scene
Different Ranges and Number of Vehicles
0
1
2
3
4
5
6
7
8
9Average task delay/s
Task Delay Comparison
BAC
BACA
BMQN
UAC
(a) Average task execution time.
1st Scene 2nd Scene 3rd Scene 4th Scene
Different Ranges and Number of Vehicles
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Successful probability
Successful Probability Comparison
BAC
BACA
BMQN
UAC (b) Task completion ratio.
1st Scene 2nd Scene 3rd Scene 4th Scene
Different Ranges and Number of Vehicles
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
Average reward
Reward Comparison
BAC
BACA
BMQN
UAC (c) Average reward.
Fig. 10. Generalization capacity comparison between the proposed BMQN and other approaches in4different scenario with400mor1600mroad length,
3or11vehicles and1or4RSUs, which are all inexperienced during training.
0 50 100 150 200 250
Training episode
-650
-600
-550
-500
-450
-400
-350
-300
-250Average Reward
Convergence Comparison
BACA
BMQN
GAC
Fig. 11. The convergence comparison between the proposed BMQN approach
and the BACA and UAC approaches.
{(300,3),(300,11),(1600,3),(1600,11)}. The performance
comparison in these scenarios is illustrated in Fig. 10. The pro-
posed BMQN also achieves the best performance and gener-
alization capacity, which can ensure considerable performance
in both small-scale and large-scale scenarios. Compared with
BACA, the BMQN has27%higher average reward among
scenarios, in which such improvement is significantly higher
than that in previously experienced scenarios. Such results
further demonstrate that the matching-based architecture can
indeed enhance the decision performance and generalization
capacity. Similarly, the BACA also achieves much better
performance than BAC and UAC, especially in large-scale
scenarios with more vehicles and RSUs, emphasizing the
importance of the available action embedding in enhancing
generalization capacity for the foundation model.
F . Convergence Comparison
Finally, we present the convergence of the proposed BMQN
approach. The achieved reward-versus-episodes of the BMQN,
BACA and UAC approaches of Fig. 9 are illustrated in Fig.
11, in which the scenario of each episode is varying. At
the beginning of training, each model struggles to explore
the state-action space, which has bad performance. With the
convergence, both the proposed BMQN and BACA approaches
can quickly learn efficient joint task offloading strategies and
obtain considerable average rewards. On the contrary, without
the available action embedding and the bi-directional attention,
the UAC approach encounters difficulties in capturing the
intrinsic relationship among agents, leading to worse conver-
gence in dynamic training scenarios with varying number of
vehicles and RSUs.

## § Conclusion

In this paper, considering the challenging joint multi-hop
task offloading problem in dynamic VEC networks, we pro-
pose the BMQN algorithm to optimize the joint task offloading
decision for both V2X and R2X. To address the issue of
varying numbers of vehicles and RSUs, we introduce bi-
directional Bert to capture correlation across vehicles and
RSUs while ensuring the dimension of task offloading actions
aligned with the number of vehicles and RSUs. In particular,
we propose type-embedded grouped attention and available
action embedding to mitigate the over-fitting sequence length
issue, resulting in better generalization capacity. Moreover,
we propose a novel matching-based architecture in BMQN to
address the issue of varying action space through a matching-
based manner. In this architecture, two independent Bert
modules extract hidden states for vehicles and RSUs when
serving as offloading initiators and receivers, respectively.
These hidden states are then jointly matched to determine
the optimal task offloading actions. By emphasizing on learn-
ing correlations between devices rather than relying on Q-
values within a fixed state-action space, the BMQN achieves
significantly better task offloading performance. Simulation
results demonstrate that the proposed BMQN can achieve great
performance in both dynamic VEC networks with varying
numbers of vehicles and RSUs. In particular, the BMQN
demonstrates great generalization capacity when adapting to
inexperienced scenarios.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
13

## § References

[1] N. Lu, N. Cheng, N. Zhang, X. Shen, and J. W. Mark, “Connected
Vehicles: Solutions and Challenges,”IEEE Internet of Things Journal,
vol. 1, no. 4, pp. 289–299, 2014.
[2] Z. MacHardy, A. Khan, K. Obana, and S. Iwashina, “V2X Access
Technologies: Regulation, Research, and Remaining Challenges,”IEEE
Communications Surveys & Tutorials, vol. 20, no. 3, pp. 1858–1877,
2018.
[3] 3GPP, “Study on Evaluation Methodology of New Vehicle-to-Everything
(V2X) Use Cases for LTE and NR (v15.3.0, Release 15),”document TR
37.885, 2024.
[4] K. Abboud, H. A. Omar, and W. Zhuang, “Interworking of DSRC and
Cellular Network Technologies for V2X Communications: A Survey,”
IEEE Transactions on V ehicular Technology, vol. 65, no. 12, pp. 9457–
9470, 2016.
[5] M. Ahmed, S. Raza, M. A. Mirza, A. Aziz, M. A. Khan, W. U. Khan,
J. Li, and Z. Han, “A survey on vehicular task offloading: Classification,
issues, and challenges,”Journal of King Saud University - Computer and
Information Sciences, vol. 34, no. 7, pp. 4135–4162, 2022.
[6] A. Waheed, M. A. Shah, S. M. Mohsin, A. Khan, C. Maple,
S. Aslam, and S. Shamshirband, “A Comprehensive Review of Comput-
ing Paradigms, Enabling Computation Offloading and Task Execution in
Vehicular Networks,”IEEE Access, vol. 10, pp. 3580–3600, 2022.
[7] A. Moubayed, A. Shami, P. Heidari, A. Larabi, and R. Brunner, “Edge-
Enabled V2X Service Placement for Intelligent Transportation Systems,”
IEEE Transactions on Mobile Computing, vol. 20, no. 4, pp. 1380–1392,
2021.
[8] J. Zhang, H. Guo, J. Liu, and Y . Zhang, “Task Offloading in Vehicular
Edge Computing Networks: A Load-Balancing Solution,”IEEE Trans-
actions on V ehicular Technology, vol. 69, no. 2, pp. 2092–2104, 2020.
[9] Y . Wu, L. P. Qian, H. Mao, X. Yang, H. Zhou, X. Tan, and D. H. K.
Tsang, “Secrecy-Driven Resource Management for Vehicular Computa-
tion Offloading Networks,”IEEE Network, vol. 32, no. 3, pp. 84–91,
2018.
[10] S.-Y . Lin, C.-M. Huang, and T.-Y . Wu, “Multi-Access Edge Computing-
Based Vehicle-Vehicle-RSU Data Offloading Over the Multi-RSU-
Overlapped Environment,”IEEE Open Journal of Intelligent Transporta-
tion Systems, vol. 3, pp. 7–32, 2022.
[11] V . Nguyen, T. T. Khanh, N. H. Tran, E.-N. Huh, and C. S. Hong, “Joint
Offloading and IEEE 802.11p-Based Contention Control in Vehicular
Edge Computing,”IEEE Wireless Communications Letters, vol. 9, no. 7,
pp. 1014–1018, 2020.
[12] C. Chen, Y . Zeng, H. Li, Y . Liu, and S. Wan, “A Multihop Task
Offloading Decision Model in MEC-Enabled Internet of Vehicles,”IEEE
Internet of Things Journal, vol. 10, no. 4, pp. 3215–3230, 2023.
[13] W. Feng, S. Lin, N. Zhang, G. Wang, B. Ai, and L. Cai, “Joint C-V2X
Based Offloading and Resource Allocation in Multi-Tier Vehicular Edge
Computing System,”IEEE Journal on Selected Areas in Communica-
tions, vol. 41, no. 2, pp. 432–445, 2023.
[14] Z. Zhang and F. Zeng, “Efficient Task Allocation for Computation
Offloading in Vehicular Edge Computing,”IEEE Internet of Things
Journal, vol. 10, no. 6, pp. 5595–5606, 2023.
[15] W. Fan, Y . Zhang, G. Zhou, and Y . Liu, “Deep Reinforcement Learning-
Based Task Offloading for Vehicular Edge Computing With Flexible
RSU-RSU Cooperation,”IEEE Transactions on Intelligent Transporta-
tion Systems, vol. 25, no. 7, pp. 7712–7725, 2024.
[16] L. Liu, J. Feng, X. Mu, Q. Pei, D. Lan, and M. Xiao, “Asynchronous
Deep Reinforcement Learning for Collaborative Task Computing and
On-Demand Resource Allocation in Vehicular Edge Computing,”IEEE
Transactions on Intelligent Transportation Systems, vol. 24, no. 12, pp.
15 513–15 526, 2023.
[17] X. Dai, Z. Xiao, H. Jiang, and J. C. S. Lui, “UA V-Assisted Task
Offloading in Vehicular Edge Computing Networks,”IEEE Transactions
on Mobile Computing, vol. 23, no. 4, pp. 2520–2534, 2024.
[18] M. Han, X. Sun, X. Wang, W. Zhan, and X. Chen, “Joint Caching,
Communication, Computation Resource Management in Mobile-Edge
Computing Networks,” in2024 IEEE Wireless Communications and
Networking Conference (WCNC), 2024, pp. 1–6.
[19] B. Wang, D. Tu, and J. Wang, “Actor-Critic Deep RL for Vehicular Edge
Computing Optimization,” in2024 International Wireless Communica-
tions and Mobile Computing (IWCMC), 2024, pp. 291–295.
[20] M. Han, X. Sun, X. Wang, W. Zhan, and X. Chen, “Transformer-Based
Distributed Task Offloading and Resource Management in Cloud-Edge
Computing Networks,”IEEE Journal on Selected Areas in Communica-
tions, vol. 43, no. 9, pp. 2938–2953, 2025.
[21] J. Zhang and K. B. Letaief, “Mobile Edge Intelligence and Computing
for the Internet of Vehicles,”Proceedings of the IEEE, vol. 108, no. 2,
pp. 246–261, 2020.
[22] M. Khabbaz, “Deadline-constrained rsu-to-vehicle task offloading
scheme for vehicular fog networks,”IEEE Transactions on V ehicular
Technology, vol. 72, no. 11, pp. 14 955–14 961, 2023.
[23] K. Shi, W. Zhao, C. Wu, R. Zhong, X. Wu, Y . Yang, and X. Zheng,
“Rsu-assisted proactive perception and edge computing for autonomous
driving,” in2023 IEEE International Conference on Metaverse Comput-
ing, Networking and Applications (MetaCom), 2023, pp. 71–77.
[24] M. Li, J. Gao, L. Zhao, and X. Shen, “Deep Reinforcement Learning for
Collaborative Edge Computing in Vehicular Networks,”IEEE Transac-
tions on Cognitive Communications and Networking, vol. 6, no. 4, pp.
1122–1135, 2020.
[25] W. Zhao, Y . Cheng, Z. Liu, X. Wu, and N. Kato, “Asynchronous DRL
Based Multi-Hop Task Offloading in RSU-Assisted IoV Networks,”
IEEE Transactions on Cognitive Communications and Networking, pp.
1–1, 2024.
[26] L. Liu, M. Zhao, M. Yu, M. A. Jan, D. Lan, and A. Taherkordi,
“Mobility-Aware Multi-Hop Task Offloading for Autonomous Driving
in Vehicular Edge Computing and Networks,”IEEE Transactions on
Intelligent Transportation Systems, vol. 24, no. 2, pp. 2169–2182, 2023.
[27] J. S ´anchez-Garc´ıa, J. M. Garc´ıa-Campos, M. Arzamendia, D. G. Reina,
S. Toral, and D. Gregor, “A survey on unmanned aerial and aquatic
vehicle multi-hop networks: Wireless communications, evaluation tools
and applications,”Computer Communications, vol. 119, pp. 43–65,
2018.
[28] C. H. Papadimitriou, “On the complexity of integer programming,”
Journal of the ACM (JACM), vol. 28, no. 4, pp. 765–768, 1981.
[29] D. Ghosh, J. Rahme, A. Kumar, A. Zhang, R. P. Adams, and S. Levine,
“Why Generalization in RL is Difficult: Epistemic POMDPs and Implicit
Partial Observability,” inAdvances in Neural Information Processing
Systems, vol. 34. Curran Associates, Inc., 2021, pp. 25 502–25 515.
[30] W. Li, X. Wang, B. Jin, D. Luo, and H. Zha, “Structured cooperative
reinforcement learning with time-varying composite action space,”IEEE
Transactions on Pattern Analysis and Machine Intelligence, vol. 44,
no. 11, pp. 8618–8634, 2022.
[31] J. Devlin, “Bert: Pre-training of deep bidirectional transformers for
language understanding,”arXiv preprint arXiv:1810.04805, 2018.
[32] D. Vari ˇs and O. Bojar, “Sequence length is a domain: Length-based
overfitting in transformer models,”arXiv preprint arXiv:2109.07276,
2021.
[33] H. Jin, X. Han, J. Yang, Z. Jiang, Z. Liu, C.-Y . Chang, H. Chen, and
X. Hu, “Llm maybe longlm: Self-extend llm context window without
tuning,”document TR 37.885, Jun. 2019.
[34] M. Du, F. He, N. Zou, D. Tao, and X. Hu, “Shortcut learning of large
language models in natural language understanding,”Communications
of the ACM, vol. 67, no. 1, pp. 110–120, 2023.
[35] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman,
D. Almeida, J. Altenschmidt, S. Altman, S. Anadkatet al., “Gpt-4
technical report,”arXiv preprint arXiv:2303.08774, 2023.
[36] Y . Chang, X. Wang, J. Wang, Y . Wu, K. Zhu, H. Chen, L. Yang, X. Yi,
C. Wang, Y . Wanget al., “A survey on evaluation of large language
models,”arXiv preprint arXiv:2307.03109, 2023.
[37] J. Kaddour, J. Harris, M. Mozes, H. Bradley, R. Raileanu, and
R. McHardy, “Challenges and applications of large language models,”
arXiv preprint arXiv:2307.10169, 2023.
[38] M. Kotaru, “Adapting foundation models for information syn-
thesis of wireless communication specifications,”arXiv preprint
arXiv:2308.04033, 2023.
[39] X. Chen, Z. Guo, X. Wang, H. H. Yang, C. Feng, J. Su, S. Zheng,
and T. Q. Quek, “Foundation Model Based Native AI Framework in 6G
with Cloud-Edge-End Collaboration,”arXiv preprint arXiv:2310.17471,
2023.
[40] M. Akrout, A. Mezghani, E. Hossain, F. Bellili, and R. W. Heath, “From
Multilayer Perceptron to GPT: A Reflection on Deep Learning Research
for Wireless Physical Layer,”IEEE Communications Magazine, vol. 62,
no. 7, pp. 34–41, 2024.
[41] L. Dong, F. Jiang, Y . Peng, K. Wang, K. Yang, C. Pan, and R. Schober,
“LAMBO: Large AI Model Empowered Edge Intelligence,”IEEE Com-
munications Magazine, pp. 1–7, 2024.
[42] E. J. Hu, Y . Shen, P. Wallis, Z. Allen-Zhu, Y . Li, S. Wang, L. Wang,
and W. Chen, “Lora: Low-rank adaptation of large language models,”
arXiv preprint arXiv:2106.09685, 2021.
[43] A. Aghajanyan, L. Zettlemoyer, and S. Gupta, “Intrinsic dimensionality
explains the effectiveness of language model fine-tuning,”arXiv preprint
arXiv:2012.13255, 2020.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply. 
14
[44] K. Asadi and M. L. Littman, “An Alternative Softmax Operator for
Reinforcement Learning,” inProceedings of the 34th International
Conference on Machine Learning, ser. Proceedings of Machine Learning
Research, vol. 70. PMLR, 06–11 Aug 2017, pp. 243–252.
[45] A. Naouri, H. Wu, N. A. Nouri, S. Dhelim, and H. Ning, “A novel
framework for mobile-edge computing by optimizing task offloading,”
IEEE Internet of Things Journal, vol. 8, no. 16, pp. 13 065–13 076, 2021.
[46] T. Haarnoja, A. Zhou, K. Hartikainen, G. Tucker, S. Ha, J. Tan, V . Ku-
mar, H. Zhu, A. Gupta, P. Abbeelet al., “Soft actor-critic algorithms
and applications,”arXiv preprint arXiv:1812.05905, 2018.
[47] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Prox-
imal policy optimization algorithms,”arXiv preprint arXiv:1707.06347,
2017.
Mingqi Hanreceived the B.Eng. degree in Commu-
nication Engineering from School of Electronics and
Communication Engineering, Shenzhen Campus of
Sun Yat-sen University, Shenzhen, China in 2022.
He is currently pursing for the M.E. degree in
Information and Communication Engineering with
School of Electronics and Communication Engineer-
ing, Shenzhen Campus of Sun Yat-sen University,
Shenzhen, China. His research interests include ma-
chine learning, reinforcement learning and multiple
access.
Xinghua Sun(M’13) received the B.S. degree from
Nanjing University of Posts and Telecommunica-
tions (NJUPT), China, in 2008 and the Ph.D. degree
from City University of Hong Kong (CityU), China,
in 2013. In 2010, he was a visiting student with
National Institute for Research in Digital Science
and Technology (INRIA), France. In 2013, he was
a postdoctoral fellow at CityU. From 2015 to 2016,
he was a postdoctoral fellow at University of British
Columbia, Canada. From July to Aug. 2019, he
was a visiting scholar at Singapore University of
Technology and Design, Singapore. From 2014 to 2018, he was an associate
professor with NJUPT. Since 2018, he has been an associate professor with
Sun Yat-sen University, Guangdong, China. His research interests are in the
area of stochastic modeling of wireless networks and machine learning for
next generation wireless communications and networks. He was a co-recipient
of the Best Paper Award from the EAI IoTaaS in 2023 and the IEEE FCN in
2024.
Xijun Wang(Member, IEEE) received the B.S.
degree (Hons.) in communications engineering from
Xidian University, Xi’an, Shaanxi, China, in 2005,
and the Ph.D. degree in electronic engineering from
Tsinghua University, Beijing, China, in January
2012. He was an Assistant Professor from 2012 to
2015 and an Associate Professor from 2015 to 2018
with the School of Telecommunications Engineer-
ing, Xidian University. From 2015 to 2016, he was
a Research Fellow with the Information Systems
Technology and Design Pillar, Singapore University
of Technology and Design. He is currently an Associate Professor with Sun
Yat-sen University. He has published several IEEE journals and conference
proceedings in the areas of wireless networks and patents related to heteroge-
neous networks. His current research interests include UA V communications,
edge computing, and age of information. He served as the technical program
committee member for numerous IEEE conferences. He was a recipient of
the Best Paper Award from the IEEE ICCC 2013. He also served as the
Publicity Chair for IEEE ICCC 2013 and the Technical Program Co-Chair
for the Wireless Communications Systems Symposium and IEEE ICCC 2016.
He is currently a reviewer for several IEEE journals. He was recognized
as an Exemplary Reviewer of the IEEE WIRELESS COMMUNICATIONS
LETTERS in 2014. He is currently an Associate Editor of IEEE ACCESS.
Wen Zhan(Member, IEEE) received the B.S. and
M.S. degrees from the University of Electronic Sci-
ence and Technology of China, China, in 2012 and
2015, respectively, and the Ph.D. degree from the
City University of Hong Kong, China, in 2019. He
was a Research Assistant and a Postdoctoral Fel-
low with the City University of Hong Kong. Since
2020, He has been with the School of Electronics
and Communication Engineering, Sun Yat-sen Uni-
versity, China, where he is currently an Assistant
Professor. His research interests include Internet of
Things, modeling, and performance optimization of next-generation mobile
communication systems.
Xiang Chen(Member, IEEE) received the B.E.
and Ph.D. degrees from the Department of Elec-
tronic Engineering, Tsinghua University, Beijing,
China, in 2002 and 2008, respectively. From July
2008 to December 2014, he was with the Wireless
and Mobile Communication Technology Research
and Development Center (Wireless Center) and the
Aerospace Center, Tsinghua University. In July 2005
and from September 2006 to April 2007, he visited
NTT DoCoMo Research and Development (YRP),
and Wireless Communications and Signal Process-
ing (WCSP) Laboratory, National Tsing Hua University. Since January 2015,
he has been with the School of Electronics and Information Technology,
Sun Yat-sen University, where he is currently a Full Professor. His research
interests mainly focus on 5G/6G wireless and mobile communication net
works, and the Internet of Things (IoT).
Tony Q. S. QuekTony Q. S. Quek (S’98-M’08-
SM’12-F’18) received the B.E. and M.E. degrees
in electrical and electronics engineering from the
Tokyo Institute of Technology in 1998 and 2000,
respectively, and the Ph.D. degree in electrical
engineering and computer science from the Mas-
sachusetts Institute of Technology in 2008. Cur-
rently, he is the Cheng Tsang Man Chair Profes-
sor with Singapore University of Technology and
Design (SUTD) and ST Engineering Distinguished
Professor. He also serves as the Director of the
Future Communications RD Programme, the Head of ISTD Pillar, and the
Deputy Director of the SUTD-ZJU IDEA. His current research topics include
wireless communications and networking, network intelligence, non-terrestrial
networks, open radio access network, and 6G.
Dr. Quek has been actively involved in organizing and chairing sessions,
and has served as a member of the Technical Program Committee as well as
symposium chairs in a number of international conferences. He is currently
serving as an Area Editor for the IEEE TRANSACTIONS ON WIRELESS
COMMUNICATIONS.
Dr. Quek was honored with the 2008 Philip Yeo Prize for Outstandin-
gAchievement in Research, the 2012 IEEE William R. Bennett Prize, the
2015SUTD Outstanding Education Awards– Excellence in Research, the 2016
IEEE Signal Processing Society Young Author Best Paper Award, the 2017
CTTC Early Achievement Award, the 2017 IEEE ComSoc AP Outstanding
Paper Award, the 2020 IEEE Communications Society Young Author Best
Paper Award, the 2020 IEEE Stephen O. Rice Prize, the 2020 Nokia Visiting
Professor, and the 2022 IEEE Signal Processing Society Best Paper Award. He
is a Fellow of IEEE and a Fellow of the Academy of Engineering Singapore.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3665406
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:02:52 UTC from IEEE Xplore.  Restrictions apply.
