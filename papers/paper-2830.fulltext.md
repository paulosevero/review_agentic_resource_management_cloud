---
paper_id: "paper-2830"
source_pdf_sha: "66d063034475f6fc624d7f3d37038aa6c63349b32e280061c6cc499a6271618e"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 4
  page_count: 18
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2830 — fulltext
## §unknown-1

JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 1
Large Language Model-based QoS-aware Resource
Allocation for Multi-UA V Cooperative Edge
Computing Networks
Yaqing Wang, Lun Tang, Weili Wang, Xiaoqiang He, and Qianbin ChenSenior Member, IEEE
Abstract—In 6G multiple unmanned aerial vehicles (UA Vs)
cooperative edge computing networks, strongly coupled system
states and limited single-UA V observability lead to inefficient
resource management and difficulty in guaranteeing Quality of
Service (QoS). To address these issues, we propose a QoS-aware
resource allocation method based on a large language model
(LLM) for Multi-UA V Cooperative Edge Computing Networks.
First, we construct an LLM-based teacher–student resource allo-
cation framework, operating with a global perspective, generates
high-quality expert policies that are subsequently injected into
distributed student agents via policy distillation, enabling effi-
cient online decision-making in dynamic environments. Second,
we design an LLM-based teacher model for accurate expert
decision-making under dynamic network conditions. Specifically,
we construct a time-varying network knowledge graph (NKG)
to represent the complex spatiotemporal states of multi-UA V
networks, employ a relation-aware graph attention network
(R-GAT) to aggregate crucial neighborhood information and
capture node importance, and further combine a fine-tuned
LLM with a Tree-of-Thoughts (ToT) reasoning framework to
produce high-quality expert resource allocation policies. Finally,
we develop a multi-agent student model with policy distillation for
efficient management of dynamic, multi-dimensional resources.
We formulate a QoS objective that jointly considers delay and
fairness, and jointly optimize user association, UA V trajectories,
computing allocation, bandwidth allocation, and air-to-air (A2A)
migration ratios. The student utilizes the Multi-Agent Proximal
Policy Optimization (MAPPO) algorithm and learns from the
teacher efficiently via policy distillation, adapting adeptly to
dynamic environments. Simulation results demonstrate that the
proposed method achieves significantly faster convergence, lower
steady-state delay, and higher fairness compared to baseline
approaches, while also exhibiting robustness and scalability
This work was supported by National Natural Science Foundation of
China (Grant No. 62401091), Chongqing Special Project for Technological
Innovation and Application Development (CSTB2025TIAD-qykjggX0205),
in part by National Natural Science Foundation of China (Grant No.
62541113), in part by Natural Science Foundation of Chongqing, China
(No. CSTB2025NSCQ-GPX0796), in part by Scientific and Technolog-
ical Research Project of Chongqing Municipal Education Commission
(KJQN202503112, KJQN202503138), and in part by Teacher-Led Innovation
Spark project by Chongqing Polytechnic University of Electronic Technology
(25XJJSCX02).
Y . Wang, L. Tang, and Q. Chen are with the School of Communications
and Information Engineering, Chongqing University of Posts and Telecommu-
nications, Chongqing 400065, China, and also with the Chongqing Key Lab-
oratory of Mobile Communications Technology, Chongqing, 400065, China.
(email: 837887853@qq.com; tangluncq@163.com; lchenqb@cqupt.edu.cn;).
Corresponding author:L. Tang(email:tangluncq@163.com).
W. Wang is with the School of Cyber Security and Information Law,
Chongqing University of Posts and Telecommunications, Chongqing 400065,
China, and also with the Chongqing Key Laboratory of Mobile Communica-
tions Technology, Chongqing 400065, China (e-mail: wangwl@cqupt.edu.cn).
X. He is with College of Communication Engineering, Chongqing Polytech-
nic University of Electronic Technology, Chongqing 401331, China. (e-mail:
hexiaoq casey@foxmail.com)
across different network sizes and resource conditions.
Index Terms—Multi-UA V cooperative edge computing, re-
source allocation, edge intelligence, large language model, Deep
reinforcement learning

## § Introduction

W
ITH the advent of 6G, Unmanned Aerial Vehicles
(UA Vs) are evolving from mere communication relays
into integrated aerial edge computing and intelligence nodes,
giving rise to multi-UA V cooperative mobile edge computing
(MEC) networks [1]. Compared with conventional MEC,
multi-UA V networks offer flexible deployment and superior
line-of-sight (LoS) links, providing viable solutions for large-
scale, highly dynamic scenarios that demand guaranteed cover-
age and Quality of Service (QoS) [2]. This inherent flexibility
enables deep cooperation among multiple UA Vs, facilitating
highly efficient joint resource allocation and forming a tightly
coupled air-ground collaborative computing fabric. As a key
enabler of advanced 6G systems, such cooperation holds broad
potential [3].
Although a single UA V has powerful on-board sensing and
computing capabilities, its overall performance is constrained
by battery capacity and payload limits; its computing power
is also difficult to schedule and provision a priori, making
it hard to handle bursty and heterogeneous task arrivals on
its own. Consequently, cooperative resource allocation among
multiple UA Vs becomes essential for sustaining high-quality
service. However, in UA V-enabled edge intelligence (EI) sys-
tems, user distributions are non-stationary, task sets grow and
shift, and network topology changes over time. Moreover,
channel conditions between user devices (UDs) and UA Vs,
along with task demands, vary markedly with spatiotemporal
conditions. Air-to-air (A2A) cooperation further introduces
complex coupling across multiple resource dimensions (e.g.,
communication, computation, trajectory), rendering the joint
optimization problem large-scale, non-convex, mixed-integer,
and tightly coupled. These factors place stringent demands
on system perception, coordination, and intelligent decision-
making capabilities, motivating the need for more robust and
sophisticated solutions [4].
To address this challenge, deep reinforcement learning
(DRL) has been widely introduced for optimizing resource
allocation objectives [5]. However, in multi-UA V cooperative
edge networks, DRL’s conventional “from-scratch” exploration
paradigm faces significant bottlenecks. As the numbers of
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 2
UA Vs and UDs grow, the joint action and state spaces expand
exponentially, leading to sparse rewards, slow convergence,
and policy instability [6]. Conventional DRL approaches
are often slow and fragile, frequently getting trapped in
low-return regions, which hinders the discovery of effective
high-return policies [7] [8]. Recently, large language models
(LLMs)—which acquire general knowledge and strong logical
reasoning abilities from massive corpora [9]—have opened
new avenues to overcome these limitations [10]. LLMs ex-
hibit powerful decision-making and personalization capabil-
ities [11]. Combining LLMs with DRL has thus become a
promising research direction [12]: by leveraging the LLM’s
global planning and reasoning capacity alongside DRL’s adap-
tive control prowess, LLMs can guide DRL exploration [13]
[14], offering a feasible path to tackle the above challenges.
Despite progress, several key challenges persist in current
multi-UA V edge intelligence networks: (1) Complexity of
efficient resource cooperation in multi-UA V systems. The
overall performance is often constrained by the computing
capacity provisioned at edge servers. Since a single UA V
has limited capability and cannot independently handle dense
task requests, inter-UA V resource cooperation is essential
for service quality. However, the states and performances of
different UA Vs become highly coupled: a UA V’s load, re-
source availability, and location directly affect the performance
and available resources of its neighbors, creating complex
cascade effects. Achieving efficient, globally consistent re-
source coordination is therefore the first major challenge. (2)
Joint optimization of multi-dimensional resources in highly
dynamic environments. UA V networks operate under strong
dynamics, reflected in real-time trajectory changes, stochas-
tic task requests from ground devices, and sharp fluctua-
tions in available bandwidth and computing resources. This
time-varying nature turns resource allocation into a high-
dimensional, mixed-integer, strongly coupled joint optimiza-
tion problem. The key challenge is how to realize precise, real-
time allocation of multiple resources under such dynamics—so
as to react promptly to environmental changes while meeting
strict QoS constraints. (3) Limitations of conventional DRL.
Standard DRL methods often converge slowly and are prone
to suboptimal policies in complex action spaces, making
them ill-suited to the joint optimization of multi-dimensional
resources in dynamic multi-UA V networks and insufficient to
meet the growing QoS demands of UDs. Overcoming DRL’s
exploration bottlenecks—by injecting high-quality priors to
accelerate adaptation and learning—is thus a critical challenge.
To address the above challenges, we propose a QoS-aware
resource allocation method for multi-UA V cooperative edge
networks based on large language models (LLMs). By inject-
ing global priors into DRL through a teacher–student distilla-
tion scheme, our approach handles multi-resource coupling in
highly dynamic settings while jointly pursuing low delay and
long-term fairness, significantly improving sample efficiency
and online adaptability. Our main contributions are:
1)Teacher–student joint optimization framework for
multi-UA V cooperative edge networks with LLMs:
We design an LLM-assisted teacher model that produces
high-quality expert policies. Through policy distillation,
this expert knowledge is effectively transferred to dis-
tributed student agents deployed on UA Vs, accelerating
their adaptation to dynamic scenarios and enhancing
learning stability.
2)LLM-based teacher model tailored to dynamic net-
works for accurate, robust decision generation:To
capture the highly coupled, heterogeneous states in multi-
UA V cooperation, we first construct a NKG that unifies
topology and heterogeneous relations; then we use a R-
GAT to aggregate the importance of neighboring UA Vs
and encode structured knowledge for the LLM; finally, we
apply LoRA fine-tuning together with Tree-of-Thoughts
reasoning to generate high-quality expert decisions, pro-
viding reliable guidance for downstream optimization.
3)Student model with policy distillation for multi-
resource cooperative management in dynamic en-
vironments:We formulate a joint QoS objective that
balances delay and fairness, and jointly optimize access
control, UA V trajectory, computing allocation, bandwidth
allocation, and A2A migration ratios. The student model
is trained with MAPPO enhanced by policy distillation
to achieve efficient multi-dimensional resource coordina-
tion. Experiments demonstrate that our method consis-
tently outperforms baselines in both delay and fairness,
and scales favorably with network size and resource
variations.
The remainder of this article is organized as follows. Sec-
tion II provides an overview of related works. Section III
presents the system model. The problem formulation is pro-
posed in Section IV. The novel algorithm based on the
Teacher-Student framework is formulated in Section V. The
simulation results are presented in Section VI, and this article
is summarized in Section VII.
II. RELATEDWORKS
A. Resource Allocation for Cooperative Multi-UAV Networks
In cooperative UA V networks, [15] considers a multi-UA V
collaborative offloading scenario and formulates an optimiza-
tion problem that minimizes latency. It proposes a Lyapunov-
and perturbation-based algorithm and achieves a near-optimal
offloading strategy. In [16], a multi-UA V edge-computing net-
work assisted by reconfigurable intelligent surfaces is created;
by jointly optimizing task association, transmit power, task
splitting, and computing (CPU) frequency allocation with
trajectory design, the long-term average delay is minimized.
Lyapunov optimization and SAC are then used for online
decision-making. In [17], they focus on cooperative sensing
in a UA V network and propose a sensing-aware resource-
allocation scheme that jointly maximizes QoE while mini-
mizing transmission delay. The approach couples semantic
communication with trajectory planning and adopts a mixed-
cooperative DRL method for online decision-making. In [18],
they jointly optimize task offloading, server selection, and
power allocation in a multi-UA V MEC scenario. It also plans
UA V flight paths and CPU frequency to minimize energy
consumption and processing delay under a total cost budget.
In [19], they study MEC for UA V swarms and use the Age
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 3
of Task (AoT) as the optimization objective while jointly
optimizing trajectory and power via a BCD (block coordinate
descent) + SCA solver to improve the timeliness metric.
In [20], a multi-UA V edge-computing network with feder-
ated sensing is built, jointly optimizing data-sensing access,
end-side power, UA V trajectory, and resource allocation, the
long-term average sensing-throughput is maximized using a
Lyapunov-based online method, while energy consumption
and delay constraints are satisfied.
While the aforementioned studies address various resource
allocation issues in multi-UA V scenarios, most focus predom-
inantly on ground device-to-UA V or UA V-to-UD optimization.
Relatively less consideration has been given to inter-UA V
cooperation, including cross-UA V task migration and collab-
orative computing mechanisms among UA Vs, which is a key
focus of our work. Beyond UA V-centric MEC optimization, re-
cent studies also emphasize traffic-aware slicing and adaptabil-
ity under time-varying demands. In particular, Mohajer et al.
propose FlexSlice [21], which jointly considers traffic-aware
network slicing and an adaptive TD3-based offloading strategy.
This line of work is complementary to ours: while FlexSlice
focuses on traffic-aware slicing and adaptive control in MEC,
our work targets multi-UA V cooperative edge computing with
mobility-coupled decisions and explicit inter-UA V workload
migration over A2A links.
B. Applications of Large Language Models in Multi-UAV
Systems
In recent years, LLMs are characterized by their strong
content-generation and reasoning capabilities derived from
vast pre-training corpora, have attracted wide attention in
edge intelligence scenarios. A key research trend is how to
build LLM-based cooperative mechanisms among resource-
constrained edge devices [22]—now a highly active topic
[23]- [26]. For UA V networks in particular, computing, en-
ergy, and communications constraints are more pronounced,
work coupling LLMs with UA V systems is still at an early
stage [27]. In [28], they investigate joint optimization under
an air–ground–cloud architecture, exploring LLMs as deci-
sion nodes on edge UA Vs, together with data quantization
and distributed inference, to enhance on-board intelligence
for complex tasks. [29] combines LLMs with knowledge
graphs to strengthen semantic representation, thereby im-
proving UA Vs’ cross-domain knowledge understanding and
their perception-and-reasoning ability for ground devices. [30]
studies LLM-oriented optimization for integrated sensing-and-
communication tasks, demonstrating the potential of LLMs
for jointly modeling perception and communication perfor-
mance. In [31], they introduce an inverse-reinforcement-
learning (IRL)–based “intelligence” enhancement method that
helps agents adapt to environment bias, thus improving cross-
scenario generalization.
III. SYSTEMMODEL
A. System Architecture
As depicted in Fig. 1, we consider a multi-UA V coopera-
tive edge computing network operating within a hierarchical
framework that integrates the cloud, UA V , and device layers.
•Device Layer: This layer comprises a set ofKUDs,
denoted byK={1,2, . . . , K}, Each UDk∈ K
generates heterogeneous computation tasks, such as real-
time video surveillance and traffic flow prediction.
•UA V Layer: This layer consists of a set ofNUA Vs,
denoted byN={1,2, ..., N}. Each UA V acts as an aerial
edge server, equipped with on-board computing capabil-
ities. This layer facilitates both ground-to-air (G2A) data
uploads and air-to-air (A2A) task migration for cooper-
ative processing among UA Vs. The distributed Student
Models are deployed on each UA V for real-time, online
decision-making.
•Cloud Layer: The cloud layer, typically hosted in a
ground station, possesses substantial computational re-
sources. It is responsible for executing the global Teacher
Model. The Teacher Model leverages its comprehensive
network view to generate expert policies, which are then
transmitted to the UA V layer via policy distillation to
guide the Student Models.
The system operates over a time horizon partitioned into
Tdiscrete time slots, indexed byt∈ {1,2, ..., T}, each with
a duration ofτ. The task generated by UDk∈ Kin slott
is denoted asM k(t) =

Dk(t), W k(t), T max
	
,whereD k(t)
denotes the input data size,W k(t)the required number of
CPU cycles, andT max the maximum tolerable delay. Due to
the limited local processing capacity of UDs, tasks must be
offloaded via G2A links to the UA Vs for execution [16]. When
a UA V serves a large number of UDs and its communication
or computing resources approach saturation, it can migrate
a portion of its tasks to neighboring UA Vs via A2A links
for cooperative processing. Therefore, this paper models both
G2A and A2A transmissions.
B. Communication Model
1) G2A Communication Model:Assume that all UA Vs
move at a fixed altitudeH. Let the position of UA Vnat
slottbed n(t) =
 
xn(t), y n(t), z n(t)

, and let the posi-
tion of user device (UD)kbed k(t) =
 
xk(t), y k(t),0

.
The 3D distance (in meters) between UDkand UA Vnis
dk,n(t) =


dn(t)−d k(t)


We adopt a probabilistic the line-of-sight (LoS) and non-
line-of-sight (NLoS) path-loss model to capture blockage in
realistic environments. Following [32], [33], the LoS proba-
bility between UDkand UA Vnis
P LoS
k,n (t) = 1
1 +aexp

−b

arcsin
  H
dk,n(t)

−a
 ,(1)
whereaandbare environment-dependent constants. Hence,
the NLoS probability isP NLoS
k,n (t) = 1−P LoS
k,n (t).The free-
space path loss (in dB) from UDkto UA Vnis
P LFS
k,n(t) = 20 log10
 
dk,n(t)

+20 log10
 
fc

+20 log10

4π
c

,
(2)
wheref c is the carrier frequency andcis the speed of light.
The total path loss (in dB) for the G2A link is then
P Lk,n(t) =P L FS
k,n(t)+P LoS
k,n (t)η LoS+P NLoS
k,n (t)η NLoS,(3)
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 4
Fig. 1. System framework of the proposed Teacher–Student for multi-UA V
cooperative architecture.
whereη LoS andη NLoS denote the additional path loss for LoS
and NLoS links, respectively.
The transmission rate from UDkto UA Vnat slottis
Rk,n(t) =B k,n(t) log 2

1 + pk(t)g k,n(t)X
k′∈K\{k}
pk′(t)g k′,n(t) +σ 2

 ,
(4)
wherep k(t)denotes the transmit power of UDk,g k,n(t)
is the channel gain, given byg k,n(t) = 10 −P Lk,n(t)/10,P
k′∈K\{k} pk′(t)g k′,n(t)represents the co-channel interfer-
ence from other UDs within the coverage of UA Vn, andσ 2
is the noise power. The termB k,n(t)denotes the bandwidth
allocated by UA Vnto UDk. Since the total bandwidth
assigned by UA Vncannot exceed its available resourceB n,
the following constraint must hold:
X
k∈K
Bk,n(t)≤B n,∀n∈ N.(5)
Define a binary variableδ k,n(t)∈ {0,1}to indicate the
association between UDkand UA Vnat slott. We set
δk,n(t) = 1if UDkis associated with UA Vn, andδ k,n(t) = 0
otherwise. In each slot, every UD can connect to at most one
UA V , while a UA V may serve multiple UDs simultaneously.
Hence, the access-control constraint is
X
n∈N
δk,n(t)≤1,∀k∈ K.(6)
2) A2A Communication Model:Since A2A links among
UA Vs are typically LoS-dominant due to limited blockage in
the air, we model the large-scale A2A channel gain using free-
space path loss. The system operates in discrete time slots of
durationτ, At the decision time scale, we assume the large-
scale channel is quasi-static within each slot, i.e., it is deter-
mined by the UA V positions in slott. Let the distance between
UA Vnand UA Vn ′ at slottbed n,n′(t) =


dn(t)−d n′(t)


.
To avoid collisions and keep the flight speed within a safe
range, the trajectories must satisfy the minimum-separation
constraint


dn(t)−d n′(t)


 ≥d min,∀n, n ′ ∈ N, n̸=n ′,(7)
whered min denotes the smallest allowable inter-UA V distance.
To ensure kinematic feasibility and prevent unrealistic inter-
slot jumps, we impose the maximum-speed constraint
∥dn(t+ 1)−d n(t)∥ ≤v maxτ,∀n∈ N(8)
The free-space path loss (in dB) of the A2A link is
P Ln,n′(t) = 20 log10
 
dn,n′(t)

+20 log10
 
fc

+20 log10

4π
c

.
(9)
The data rate from UA Vnto UA Vn ′ is
Rn,n′(t) =B n,n′(t) log 2

1 + pn(t)g n,n′(t)X
m∈N \{n}
pm(t)g m,n′(t) +σ 2
n′

 ,
(10)
whereB n,n′(t)is the bandwidth allocated to the A2A
link,p n(t)is the transmit power of UA Vn,g n,n′(t) =
10−P Ln,n′ (t)/10 is the channel gain of the A2A link, andσ 2
n′
is the noise power at receivern ′.
Due to the limited on-board computing resources, a UA V
may allocate a portion of its tasks to neighboring UA Vs
for cooperative processing. Letγ n,n′(t)∈[0,1]denote the
fraction of the task that UA Vnmigrates to a neighboring
UA Vn′ at slott. Due to the limited A2A radio range, we
define the dynamic neighbor set of UA V n at
Nn(t) =

n′ ∈ N \ {n}


 ∥dn(t)−d n′(t)∥ ≤R A2A
	
(11)
RA2A denotes the maximum A2A distance to guarantee a
reliable link. Task migration is only permitted to UA Vs in
Nn(t), i.e.,γ n,n′(t) = 0,∀n ′ /∈ Nn(t).The migrated data
size isD n,n′(t) =γ n,n′(t)D k(t).Accordingly, the fraction
processed on the original UA Vnis1− P
n′∈N γn,n′(t),
and the retained data size at UA VnisD n(t) =

1−
P
n′∈N γn,n′(t)

Dk(t).We consider divisible workloads,
where the task can be partitioned into independently exe-
cutable subtasks
C. QoS-aware Problem
In a multi-UA V cooperative edge computing network, UDs
face two core QoS requirements:
•Delay sensitivity.Tasks such as traffic prediction and
emergency assessment demand that both transmission
and computation be completed within a stringent time
window. If the end-to-end delay exceeds the predefined
deadline, the task may become obsolete, rendering the
result useless. Therefore, delay is a critical QoS metric.
•Resource allocation fairness.Due to significant vari-
ations in distance, channel conditions, and task loads
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 5
among UDs served by different UA Vs (and even among
UDs attached to the same UA V), users with favorable
conditions may receive a disproportionately large share
of resources. Conversely, remote or disadvantaged users
might experience long-term under-service or even re-
source starvation, which degrades the overall user expe-
rience.
Optimizing either of these goals in isolation can be detri-
mental to the other. For instance, exclusively pursuing minimal
delay may lead to severe bias against UDs located far from a
UA V , whereas strictly enforcing fairness could increase local
congestion and overall latency. Consequently, we formulate a
joint optimization problem that aims to minimize the delay
while upholding a high standard of fairness.
Moreover, UA Vs are battery-powered. Uncontrolled energy
consumption can interrupt tasks and jeopardize flight safety.
To ensure safe and sustained service, we impose an energy
constraint on each UA V , requiring that its total energy con-
sumption not exceedE max, thereby guaranteeing safe and
continuous flight.
D. Delay Model
We consider both the transmission delay from UD to UA V
and between UA Vs, as well as the computation delay on UA Vs.
1) UD–UAV transmission delay:At slott, the uplink trans-
mission delay for the task generated by UDkand associated
with UA Vnis
T tra
k,n(t) = δk,n(t)D k(t)
Rk,n(t) ,(12)
whereδ k,n(t)∈ {0,1}is the association indicator,D k(t)is
the input data size, andR k,n(t)is the G2A rate.
2) Computation delay on UAVn:Letf n,k(t)the effective
CPU service rate (cycles/s) allocated by UA Vnto the com-
putation workload associated with UDkin slottunder CPU
sharing, To explicitly capture the practical multi-task CPU
sharing mechanism and the induced load coupling, the per-
slot CPU allocations at UA Vnsatisfy P
k∈K δk,n(t)fn,k(t)≤
f max
n ,∀n∈ N. wheref max
n is the maximum computing
capability of UA Vn. Then the computation delay on UA V
nis
T com
n,k (t) = Dn(t)Wk(t)
fn,k(t) ,(13)
whereW k(t)is the required number of CPU cycles and
γn,n′(t)∈[0,1]is the fraction of the task migrated from UA V
nto a neighboring UA Vn ′.
3) UAV–UAV transmission delay:If a fractionγ n,n′(t)of
the task is allocated from UA Vnto UA Vn ′, the A2A
transmission delay is
T tra
k,n,n′(t) = Dn,n′(t)
Rn,n′(t) ,(14)
whereR n,n′(t)is the achievable A2A rate fromnton ′.
4) Computation delay on the neighboring UAVn ′:Let
fn′,n(t)denote the effective CPU service rate (cycles/s)
allocated by the neighboring UA Vn ′ to process the mi-
grated portion received from UA Vnin slottunder CPU
sharing, To explicitly capture the multi-task CPU sharing
at UA Vn ′, the per-slot CPU allocations at UA Vn ′ satisfyP
n∈N \{n′} fn′,n(t)≤f max
n′ ,∀n ′ ∈ N. wheref max
n′ is
the maximum computing capability of UA Vn ′ Then the
corresponding computation delay is
T com
k,n′ (t) = Dn,n′(t)Wk(t)
fn′,n(t) .(15)
Combining the above, we consider divisible workloads
where the portion retained at UA V n and the migrated portion
processed at neighboring UA Vs can be executed in parallel;
thus, the end-to-end completion time is modeled as the max
of the parallel branches the total delay for a task from UDk
served by UA Vnis
Tk,n(t) =T tra
k,n(t) + max
n
T com
n,k (t), T tra
k,n,n′(t) +T com
k,n′ (t)
o
.
(16)
The completion delay of UDkin slottis
Tk(t) =
X
n∈N
δk,n(t)T k,n(t),(17)
which must satisfy the QoS deadline constraintT k(t)≤T max.
E. Fairness Model
To avoid long-term under-service caused by path loss or
load concentration, we adopt Jain’s index [34] to measure
the fairness of the service received by all UDs, ensuring a
uniform quality of service as much as possible. First, let the
instantaneous throughput of UDkat slottbe
Rk(t) =
X
n∈N
δk,n(t)R k,n(t),(18)
whereR k,n(t)is the UD–UA V rate andδ k,n(t)∈ {0,1}
indicates the association.
The long-term average throughput of UDkup to slottis
defined by the running average:
¯Rk(t) = 1
t
tX
τ=1
Rk(τ)(19)
Accordingly, the fairness among UDs at timetis quantified
by Jain’s index:
J(t) =
X
k∈K
¯Rk(t)
2
K
X
k∈K
¯R2
k(t)
.(20)
whereJ(t)∈
 1
K ,1

. A value ofJ(t)closer to1indicates
more equitable resource allocation. WhenJ(t) = 1
K , a single
UD monopolizes all resources, which corresponds to the most
unfair case.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 6
To make the fairness term comparable with the normalized
delay term in the objective, we further define the normalized
Jain’s index as
˜J(t) = J(t)− 1
K
1− 1
K
(21)
where ˜J(t)∈[0,1].
F . Energy Model
We consider the computation energy on UA Vs and the
transmission energy over A2A links in our model.
1) Local computation energy on UAVn:After UA Vn
receives the task of UDk, the energy consumed for local
computation at slottis modeled as:
Ecom
n,k (t) =δ k,n(t)κ f 2
n,k(t)Dn(t)Wk(t),(22)
whereκis the effective switching capacitance coefficient,
and denotes a fixed hardware-related parameter reflecting
the processor’s dynamic power characteristics in the adopted
DVFS-based energy model.f n,k(t)is the CPU frequency
allocated by UA Vnto UDk, andγ n,n′(t)∈[0,1]is the
task fraction migrated to a neighboring UA Vn ′.
2) A2A transmission energy of UAVn:When UA Vn
migrates a fractionγ n,n′(t)of the task to a neighborn ′, the
energy consumed by transmitting over the A2A link is
Etra
n,k,n′(t) =δ k,n(t)p n(t)T tra
n,n′(t),(23)
wherep n(t)is the transmit power of UA VnandT tra
n,n′(t)is
the A2A transmission delay fromnton ′.
Combining the above, the total energy consumed by UA V
nat slottis the sum of its total local computation energy and
its total A2A transmission energy, aggregated over all served
UDs and all migration links:
En(t) =
X
k∈K
Ecom
n,k (t) +
X
k∈K
X
n′∈N \{n}
Etra
n,k,n′(t).(24)
IV. OPTIMIZATIONFORMULATION
We aim to jointly optimize UD–UA V association, UA V
trajectories, computation and bandwidth allocation, and the
task migration fractions delegated to neighboring UA Vs. Let
the decision variables at slottbe∆(t) ={δ k,n(t)},D(t) =
{dn(t)},F(t) ={f n,k(t), f n′,n(t)},B(t) ={B k,n(t)},
Γ(t) ={γ n,n′(t)}for allk∈ Kandn, n ′ ∈ N. To
comprehensively enhance system QoS, which encompasses
both task completion delay and resource allocation fairness,
we formulate the optimization problem based on a weighted
delay-fairness (WDF) objective. Specifically, our goal is to
minimize the following objective function:
P1:min
∆(t),D(t),F(t),B(t),Γ(t)
α· 1
K
X
k∈K
Tk(t)
Tmax
+β·
 
1− ˜J(t)

s.t. C1:
X
n∈N
δk,n(t)≤1∀k∈ K
C2:


dn(t)−d n′(t)


 ≥d min ∀n, n ′ ∈ N, n̸=n ′
C3:∥d n(t+ 1)−d n(t)∥ ≤v maxτ∀n∈ N
C4:
X
k∈K
Bk,n(t)≤B n ∀n∈ N
C5:
X
k∈K
δk,n(t)f n,k(t)≤f max
n ∀n∈ N
C6:
X
n∈N \{n′}
fn′,n(t)≤f max
n′ ∀n ′ ∈ N
C7:
X
t∈T
En(t)≤E max ∀n∈ N
C8:T k(t)≤T max ∀k∈ K
C9:α, β≥0, α+β= 1.
(25)
The weighting parametersαandβreflect the relative QoS
priorities between delay minimization and fairness enhance-
ment, withα+β= 1. A largerαmakes the objective
more delay-oriented and tends to favor lower latency, whereas
a largerβmakes the objective more fairness-oriented and
tends to promote more balanced service among users. There-
fore, the proposed framework can be adapted to different
QoS preferences by adjusting the delay-fairness weighting.
Constraint C1 ensures that each UD associates with at most
one UA V in a slot. C2 guarantees collision avoidance via
a minimum inter-UA V separation. C3 limits the movement
of each UA V between consecutive time slots by enforcing a
maximum flight speedv max. C4 limits the total bandwidth
allocated by each UA V . C5 and C6 bound the local and
cooperative CPU frequencies by the maximum computing
capability of the serving UA V . C7 constrains the accumulated
energy consumption of each UA V within the battery budget.
Since the system runs overTslots of durationτ, C7 enforces
the onboard energy budgetE max over the episode window
T τ. C8 imposes the QoS deadline for task completion. C9
specifies the nonnegative weights for delay and fairness and
normalizes them to sum to one.
V. PROBLEMSOLUTIONBASED ONTEACHER-STUDENT
MODEL
The formulated optimization problem involves both discrete
and continuous variables, resulting in a complex, non-linear,
and non-convex multi-parameter problem. It falls into the class
of mixed-integer nonlinear programming (MINLP) and is NP-
hard, making it intractable to solve exactly. Conventional DRL
methods often struggle with inefficient exploration in such
large action spaces; when an agent learns from scratch, it
tends to suffer from low sample efficiency, slow convergence,
and may get trapped in suboptimal policies. To address these
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 7
challenges, we introduce a teacher-student policy distillation
paradigm. We leverage an LLM-generated expert policy as the
teacher for resource allocation decisions and devise a policy-
distillation mechanism to warm-start the student’s learning
process. This approach enables the student policy network to
benefit from the teacher’s prior knowledge, thereby improving
initial performance, accelerating sample efficiency, and foster-
ing more robust and accurate resource-allocation strategies in
dynamic multi-UA V scenarios.
A. LLM-Based Teacher Model for Multi-UAV Cooperative
Resource Allocation
In multi-dimensional and highly-coupled UA V network
resource allocation scenarios, relying solely on DRL with
random priors often leads to low sample efficiency and slow
convergence. To address this, we design a teacher model
comprising three modules: a network knowledge graph (NKG)
construction module, a GAT-based representation extraction
module, and an LLM-based decision-making module. This
architecture leverages the advanced reasoning and generative
capabilities of LLMs to produce expert-level optimization poli-
cies. Specifically, we first construct a NKG to uniformly model
the topology and resource dependencies of the dynamic air-
ground cooperative environment. Next, we employ a relation-
aware graph attention network (R-GAT) to extract salient
features from the NKG that capture each UA V’s local state
and its neighborhood context. Finally, we integrate a fine-tuned
LoRA-based LLM with a Tree-of-Thoughts (ToT) reasoning
framework to generate high-quality expert policies, which
subsequently supervise the MAPPO training of the student
model.
Under the proposed teacher–student architecture, the
Teacher Model is deployed in the cloud to construct an
aggregated global view from periodically collected state sum-
maries, while the Student Models are deployed on UA Vs for
distributed real-time decision-making based on local observa-
tions. Accordingly, the Teacher provides expert guidance based
on aggregated network information, whereas the Students
continuously adapt their actions based on local observations.
Therefore, the proposed framework does not require contin-
uous full-state broadcasting among UA Vs, and its signaling
overhead mainly consists of periodic state reporting and occa-
sional delivery of distilled guidance.
1) Network Knowledge Graph Construction in multi-UAV
cooperative network:To capture the intricate topology and
resource interactions in a dynamic multi-UA V cooperative
environment, we construct a NKG. In a unified schema,
physical entities (UDs, UA Vs, base stations, and cloud servers)
are represented as nodes, while dependencies such as commu-
nication, computation, and task migration are encoded as typed
edges.
We define the time-varying knowledge graph in multi-UA V
cooperative network as
G(t) =
 
V(t),R,E(t),X(t)

,(26)
where
•V(t): the set of nodes at slott, including UDs, UA Vs,
base stations, cloud/edge servers;
Fig. 2. LLM-Based Teacher Model for Multi-UA V Cooperative Resource
Allocation
•R: the set of relation types; According to the scenario,
includes three primary relations:
(1)Communication link: if a feasible G2A path exists
between a UD and a UA V , create a “wireless access”
relation.
(2)Computing service: when a UA V can process a UD’s
task, create a “compute service” relation.
(3)Task migration: when two UA Vs cooperate via an
A2A link to process tasks, create a “task migration”
relation; the edge attribute stores the current migra-
tion ratio.
•E(t)⊆ V(t)× V(t)× R: the set of typed relation triples;
•X(t): is the collection of time-varying attributes attached
to nodes and edges, describing the real-time state. These
include:
(1)Node attributes: position, battery level, CPU fre-
quency, task data size, etc.
(2)Edge attributes: inter–node distance, LoS probabil-
ity, channel gain, allocated bandwidth, migration
ratio, etc.
Because the NKG evolves with the system, we define three
types of update rules:
•Node update: when a new UD joins or a UA V fails
or recovers, add or remove the node inV(t)and syn-
chronously create or delete its incident edges.
•Edge update: based on new association decisions, add or
remove UD–UA V communication edges; if the bandwidth
on a link drops to zero, delete that edge; when a migration
policy is issued, create or update the corresponding “task
migration” edge and its ratio.
•Attribute update: for existing nodes or edges, update only
their attributes inX(t).
Compared to a static graph model, the proposed NKG
naturally represents heterogeneous entities and multi-UA V
interactions within a single schema, while its time-varying at-
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 8
tributes provide structured background knowledge to the LLM.
Coupled with GAT-based feature extraction, this yields rich
relational representations that capture both network structure
and physical state, enabling more accurate and generalizable
decision-making.
2) RGAT-based Knowledge Feature Extraction:Given the
highly dynamic nature of the multi-UA V environment, both
the network topology and the relationships between entities
evolve over time. Relying on simple neighborhood aggregation
is insufficient to capture these dynamics. We therefore adopt
a Relation-aware Graph Attention Network to extract salient
features from the NKG. R-GAT allocates attention weights to
neighbors conditioned on node and edge attributes for each
distinct relation type. It then performs intra-relation aggrega-
tion followed by cross-relation fusion, thereby dynamically
modeling the complex and time-varying inter-node dependen-
cies. This mechanism enables node embeddings to encode
topological and relational semantics, so that key neighbors and
links (e.g., migration or bandwidth) are emphasized and the
subsequent inference is more accurate and stable.
Leth (0)
i denote the initial feature of each nodeiin the
NKG, which is a vector formed by concatenating its text
embedding and the type encoding of the node. Letx (e)
ij be the
edge attribute, and for each GAT layerland relationr∈ R,
the unnormalized attention score fromito its neighborjis
c(l,r)
ij = LeakyReLU

a(l)
r
⊤
W(l)
r h(l)
i


 W(l)
r h(l)
j


 U(l)
r x(e)
ij

,
(27)
whereN r(i)is the set of neighbors ofiunder relationr, and
j∈ N r(i).W (l)
r ,U (l)
r are trainable linear transformations,
a(l)
r is the trainable attention vector, and∥denotes vector
concatenation.
The normalized attention weight is obtained by a softmax
over the relation-specific neighborhood:
α(l,r)
ij =
exp
 
c(l,r)
ij

P
k∈Nr(i)
exp
 
c(l,r)
ik
 ,
X
j∈Nr(i)
α(l,r)
ij = 1.(28)
We then perform intra-relation aggregation to update the
node features:
˜h(l+1)
i,r =
X
j∈Nr(i)
α(l,r)
ij W (l)
r h(l)
j .(29)
To capture the heterogeneous impact of different relations
on nodei, we aggregate the features for each relation sep-
arately and then fuse them; We also employ a multi-head
attention mechanism (Mheads) to improve stability and
expressive power:
h(l+1)
i =σ
 


M
m=1
X
r∈R
˜h(l+1,m)
i,r
!
,(30)
whereσ(·)is an activation function and∥denotes head-wise
concatenation.
After propagating forLlayers, each entity node inGobtains
the final representationh (L)
i , which integrates rich contextual
information from its key neighbors across multiple relation
types. This mechanism enables the model to learn deep feature
representations that fuse network structure with entity states,
thereby enhancing the accuracy and robustness of subsequent
decision-making.
3) LLM Decision Module Based on Tree-of-Thoughts:
Foundation models are trained for broad, general-purpose
scenarios. We therefore first perform lightweight domain adap-
tation via LoRA to align the LLM with our specific context.
Since directly prompting an LLM for end-to-end solutions
struggles with multi-objective, multi-constraint optimization,
we then adopt the Tree-of-Thoughts framework [35] to guide
the fine-tuned model in generating decisions that are diverse,
accurate, and consistent with domain knowledge.
a) Fine-tuning with LoRA:Although a pre-trained LLM
possesses strong general reasoning abilities, a knowledge gap
remains for specialized multi-UA V cooperative edge scenarios.
To align the LLM’s decisions with our specific setting, we em-
ploy a LoRA-based fine-tuning approach. Full-parameter fine-
tuning is computationally prohibitive, requiring substantial
resources to update the entire model. Consequently, parameter-
efficient fine-tuning (PEFT) methods are widely adopted.
LoRA, a prominent PEFT method, freezes most weights in the
pre-trained Transformer and injects low-rank, trainable layers
into the attention blocks, thereby greatly reducing the number
of trainable parameters and the associated training overhead.
LetW 0 denote a weight matrix in the pretrained model.
LoRA injects two low-rank matricesB∈R s×r andA∈R r×d
to construct a matched update∆W=BA. The fine-tuned
LLM is then written as
W=W 0 + ∆W=W 0 +BA,(31)
wherer≪min(s, d). During training,W 0 is kept frozen and
only the low-rank matricesBandAare updated, significantly
reducing both the number of trainable parameters and the
memory footprint.
b) Multi-step Decision Making via Tree-of-Thoughts:
Resource allocation in a multi-UA V network is a high-
dimensional combinatorial problem that must jointly consider
UD association, UA V trajectory, computation and bandwidth
allocation, and inter-UA V task migration under multiple con-
straints. Relying on an LLM to generate a one-shot solution
often yields only a ”surface-level” plan. To exploit deeper
reasoning, we adopt the Tree-of-Thoughts framework: a com-
plex optimization problem is decomposed into a sequence of
interdependent subproblems that are explored on a reasoning
tree, while the LLM performs search over thought chains.
ToT generalizes chain-of-thought (CoT) [36] into a tree
structure,where each root-to-leaf path corresponds to a com-
plete CoT. Each node stores an intermediate thought, and
edges link successive reasoning steps. This structure allows the
model to explore diverse reasoning branches in parallel, back-
track, and compare different paths, thus mimicking human-like
multi-step deliberation: generate, evaluate, and select among
different lines of thought.
LetA= (V,E)denote the search tree, where the root
encodes the initial global state, and each nodev∈ Vkeeps the
current partial decision, its evaluation, and the corresponding
local state. During generation, the LLM expands the tree,
scores branches, and finally selects the root–to–leaf path with
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 9
the lowest loss as the expert chain. Concretely, the procedure
consists of four stages:
1) Problem Decomposition.Given the initial positions,
resource states of all UA Vs and UDs, residual energy, and
task requests with their deadlines, the problem is decomposed
into stepwise reasoning prompts. Following our system model,
we split resource allocation into three sub-tasks:
•Task 1: UD association. This sub-task determines the as-
sociation variablesδ k,n(t), matching to the most suitable
UA V .
•Task 2: UA V trajectory planning. Given the user distribu-
tion and access requests, plan the next-step positiond n(t)
of each UA V by optimizing link quality while satisfying
collision-avoidance constraints.
•Task 3: Resource and migration allocation: For already
associated UDs, this sub-task determines the bandwidth
{Bk,n(t)}, compute resources{f n,k(t), fn′,k(t)}, and the
migration ratio to a neighboring UA Vγ n,n′(t)if needed.
Candidate Generation.At each node of the reasoning
tree—i.e., at every decision step—the LLM receives the sub-
task prompt along with the current network snapshot and
global features, and proposes multiple feasible solutions.
Specifically, the sub-task prompt is constructed in a struc-
tured manner and includes the current sub-task description,
the current-slot system states t, the graph featureH (L) the
retained partial decisions from previous reasoning steps, and
the corresponding feasibility constraints. In this way, each ToT
step uses a bounded structured context rather than a long
conversational history. For a given sub-task Task-i, we call
the LLM with parametersθto obtainKcandidate actions
together with their thought chains:

(ai,CoT i)
	Kcand
i=1 = LLM θ

st, H (L), T ask−i

(32)
wheres t is the system state,H (L) ={h L
i }i∈V(t) is the final
NKG features.
Quantitative Self-Evaluation.Each retained candidate
branch is quantitatively evaluated according to the weighted
delay-fairness objective. For thei-th retained candidate at slot
t, its evaluation loss is written as
L(i)
t =α· 1
K
X
k∈K
T (i)
k (t)
Tmax
+β·
 
1− ˜J (i)(t)

,(33)
whereT (i)
k (t)and ˜J (i)(t)denote the delay and Jain’s fairness
index under thei-th candidate action, respectively. Lower loss
indicates a better candidate branch.
Beam Search and Pruning.To efficiently navigate the
large candidate space and approximate the best reasoning
chain, we adopt a beam-search strategy with two tunable
hyperparameters:
•DepthL: the tree expands from Task 1 to Task 3, A
complete reasoning chain is obtained at depth 3, so we
set the maximum search depth toL= 3.
•Beam widthB: at each layer, we retain theBchains with
the lowest loss and prune the others. Each node expands
at mostK cand candidates.
After beam search reaches the final reasoning depth, we re-
tain the top-Bcomplete candidate branches in the final beam.
LetA T (st) ={a (1)
t , ..., a(B)
t }denote the retained candidate
action set. Their losses are normalized into confidence weights
by
ω(i)
t =
exp

−L(i)
t /τT

PB
j=1 exp

−L(j)
t /τT
 , i= 1, . . . , B.
whereτ T is the temperature parameter. The Teacher policy
distribution is defined as
πT

a(i)
t |s t

=ω (i)
t , i= 1, . . . , B.
For expert action generation, the candidate with the highest
probability is selected, while for policy distillation the full
normalized distribution over the retained candidate set is used
as the Teacher-side supervisory signal.
The time complexity of beam search isO
 
B ×K cand × L

.
By searching the tree and pruning suboptimal branches, the
model explores diverse alternatives. Candidates that severely
violate constraints or deviate from the objective are discarded
early, allowing computational resources to be focused on
higher-quality solutions. Through this iterative ”analyze - gen-
erate - evaluate - search” cycle, the ToT framework ultimately
returns a high-quality expert resource-allocation policy for the
multi-UA V cooperative network.
Algorithm 1LLM-based Teacher Policy Generation for
Multi-UA V Cooperative Resource Allocation
Input:Global system states t, previous knowledge graph
G(t−1); ToT depthL, beam widthB, per-step candidates
Kcand; RGAT layersLand headsM.
Output:Teacher policy distributionπ T (at |s t).
1:Stage 1: NKG construction
2:foreach slott∈ Tdo
3:Update node setV(t)(insert/remove nodes).
4:Update edge setE(t)(G2A link, computing service,
task migration).
5:Update dynamic attributesX(t)(positions, battery, LoS
probability, bandwidth, migration ratio).
6:Stage 2: R-GAT feature extraction
7:Initialize node embeddingsh (0)
v .
8:forlayerℓ= 1,2, . . . , Ldo
9:fornodei∈ V(t)do
10:forrelationr∈ Rdo
11:Compute unnormalized attention scorec (ℓ,r)
ij by
(27) forj∈ N r(i).
12:Normalize to attention weightα (ℓ,r)
ij by (28).
13:Intra-relation aggregation to obtain ˜h(ℓ+1)
i,r by
(29).
14:end for
15:Multi-relation and multi-head fusion to obtain
h(ℓ+1)
i by (30).
16:end for
17:end for
18:LetH (L) ={h L
i }i∈V(t) be the final NKG features.
19:Stage 3: LLM decision module with ToT
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 10
Fig. 3. Student Model Based on MAPPO with Policy Distillation
20:Initialize the ToT root with(s t, H(L)).
21:Decompose the decision into three sub-tasks: user as-
sociation, UA V trajectory, and resource allocation.
22:fortaski= 1,2,3do
23:Candidate generation: use the LoRA-tuned LLM to
generateK cand candidates for taskiconditioned on
(st, H(L)).
24:Candidate evaluation: score each candidate using the
objective in (33).
25:Beam search & pruning: keep the topBbranches
at the current ToT depth; expand until the maximum
depthLis reached.
26:Update the ToT state with retained branches.
27:end for
28:Construct the Teacher policy distribution by softmax-
normalizing the negative evaluation losses of the top-B
complete candidates in the final ToT beam.
29:end for
30:returnπ T (at |s t)
B. Student Model Based on MAPPO with Policy Distillation
The teacher leverages global context to infer a high-quality
expert policy distribution and then transfers it to the student,
providing guidance for decision making. The student follows
an actor–critic paradigm and interacts with the environment
through local sensing and partial observations to produce fast
responses. However, in high-dimensional mixed action spaces,
conventional deep RL can suffer from low sample efficiency,
slow convergence, and suboptimal local minima. To inherit the
teacher’s prior knowledge while improving learning efficiency,
we augment the student’s MAPPO training with a loss term
for policy distillation, which regularizes the deviation from the
teacher distribution. In this way, the student can both acquire
the teacher’s expertise and maintain fast decision adaptation
on the edge.
1) POMDP Formulation:As student agents (UA Vs) oper-
ate with only local observations during execution and lack
real-time access to the complete global state, we model
the decentralized resource allocation problem as a Partially
Observable Markov Decision Process (POMDP), defined by
the tuple⟨S(t),A(t),P,O(t),R(t), γ⟩.
•Agents: Each UA Vn∈ Nacts as an individual agent.
•State SpaceS: At slott, the global state includes the
positions of all UDs and UA Vsd k(t),d n(t), the band-
width allocations between each UD and UA VB k,n(t),
the total bandwidth of each UA VB n(t), and the com-
puting CPU frequency of each UA Vf n(t). We write
S(t) ={s 1(t), s2(t), . . . , sN(t)}.
•Action SpaceA: At slott, agentntakes action
an(t) ={δ k,n(t), d n(t), f n,k(t), f n,n′(t),
Bk,n(t), γ n,n′(t)} k∈K,n,n′∈N , .
which contains the next-step UA V position, UD–UA V
association, bandwidth allocated to each associated UD,
and the task fraction migrated from UA Vnto its neighbor
n′. The joint action isA(t) ={a 1(t), a2(t), . . . , aN(t)}.
•State transition: The kernelPis defined by the probability
of transitioning from the current states t to the next state
st+1 after taking actiona t, i.e.,P(s t+1 |s t, at).
•Observation: At slott, UA Vnobserves its local state
on(t), including its position, the task data sizeD k(t), the
required CPU cyclesW k(t), etc. The observation space
of UA VnisO(t) ={o 1(t), o2(t), . . . , oN(t)}.
•Reward: We further refine the reward by introducing
penalties. The instantaneous reward of agentnat slot
tis
rn(t) =



−

α· 1
K
P
k∈K
Tk(t)
Tmax
+β
 
1− J(t)

,feasible,
−ξ1Ncol −ξ 2Eover −ξ 3Nns,infeasible.
(34)
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 11
Here, “feasible” means all constraints C1–C7 are satis-
fied; whereξ 1 penalizescollisions: when the distance
between any two UA Vs is less than the minimum safe
separationd min, both agents are penalized;ξ 2 penalizes
energy overflow: if a UA V’s cumulative energy con-
sumption exceeds its energy budget, a penalty is issued;
ξ3 penalizesno service: if a UD is not covered or is
not associated with any UA V , the UD incurs a penalty.
These penalties prevent service interruption and encour-
age broader coverage. The discount factorγbalances
immediate and future rewards.
2) MAPPO with Policy Distillation:MAPPO follows an
actor–critic architecture. The actor generates an action from
the observed state, while the critic estimates the state–value
or action–value to evaluate the current policy and improve
it through interaction with the environment. Because sam-
ples collected by interacting with the environment can be
highly correlated, and because mixed continuous–discrete ac-
tion spaces are large, we adopt experience replay: trajectories
are stored in a buffer and mini–batches are drawn at training
time to improve sample reuse.
At the beginning, each agent’s policy network is randomly
initialized; letθdenote the parameters of the actor network for
agentn, andωthe parameters of the critic network . At each
slott, given states t, the UA V samples an actiona n(t)from
the policy and then executes it; Here, the Student policy is im-
plemented as a hybrid discrete-continuous actor. Specifically,
the association decision is modeled as a categorical action
parameterized by softmax logits. The UA V trajectory action is
represented as a bounded normalized displacement mapped
by a tanh operator, while the bandwidth allocation, CPU
allocation, and migration ratios are represented as nonnegative
normalized fractions generated by softmax operators and then
scaled by the corresponding resource budgets. In this way,
the sampled action remains bounded and physically feasible
during MAPPO training and execution. These transformations
can be interpreted as an implicit projection step that maps
candidate actions into the feasible action space, thereby ensur-
ing that all resource constraints are satisfied. The environment
transitions to the next states t+1 and returns rewardr(t). To
stabilize training and mitigate policy drift caused by long
rollout horizons, we adopt the trust region idea in PPO: in
each update, we optimize within a clipped ratio range using
the “new” actor (outputting the current action) and the “old”
actor (a frozen copy that produced the buffer trajectories). The
MAPPO objective is
Jclip =E
" TX
t=0
min

qt(θ) ˆAt,clip
 
qt(θ),1−ε,1 +ε
 ˆAt
#
,
(35)
whereq t(θ) = πθ(at |o t)
πθold(at |o t) is the importance ratio, and the
clipping function is
clip
 
r,1−ε,1 +ε

= max

min
 
r,1 +ε

,1−ε

,(36)
which constrains the update to[ 1−ε,1 +ε]so that policy
changes remain small. Hereθ old is the parameter of the behav-
ior policy that generated the buffer data,εis a hyperparameter,
and ˆAt is the advantage.
To obtain more stable training and reduce variance, we
adopt a V–critic and generalized advantage estimation (GAE).
The advantage is
ˆAt =δ t + (γλ)δ t+1 +· · ·+ (γλ) T−t−1 δT−1 ,(37)
with temporal–difference error
δt =r t +γ V ψ(st+1)−V ψ(st),(38)
and the value loss
LV = 1
2 E
h 
Vψ(st)− ˆVt
2i
,(39)
whereV ψ is the critic and ˆVt =r t +γ V ψ(st+1),
We use Jensen–Shannon (JS) divergence as the distillation
term. Compared with the KL divergence, JS is symmetric and
avoids the mismatch direction issue. Letπ T be the teacher
policy andπ S the student policy. Although the underlying
action space includes both discrete and continuous compo-
nents, the distillation process is not performed over the entire
hybrid action space. Instead, the Teacher policy is defined as a
discrete distribution over the finite candidate action setA T (st)
generated by the ToT module. The JS divergence between their
action distributions at states t is
DJS
 
πT (· |s t)


 πS(· |o t)

= 1

## §2 DKL

 
πT (· |s t)


 ¯π(· |st)

+ 1

## §2 DKL

 
πS(· |o t)


 ¯π(· |st)

,
(40)
where the mixture policy is
¯π(at |s t) = 1
2
 
πT (at |s t) +π S(at |o t)

,(41)
and the KL divergence is
DKL
 
πT (· |s t)


 ¯π(· |st)

=
X
a∈AT (st)
πT (at |s t) log πT (at |s t)
¯π(at |s t) .
(42)
Hence,
DJS
 
πT (· |s t)


 πS(· |o t)

= 1
2
X
a∈AT (st)
πT (at |s t) log πT (at |s t)
¯π(at |s t)
+ 1
2
X
a∈AT (st)
πS(at |o t) log πS(at |o t)
¯π(at |s t) .
(43)
where the summation is taken over the finite candidate
action setA T (st)induced by the ToT-based teacher, rather
than over the entire hybrid action space. We add the distillation
regularizer to the PPO objective so that the student learns from
the teacher while still improving via environment interaction:
F(πθ) =J clip(πθ)+λ V LV +λ JS DJS
 
πT (· |s t)


 πθ(· |o t)

,
(44)
whereλ V >0andλ JS >0are weighting hyperparameters. A
largerλ JS enforces stronger imitation of the teacher, whereas
a smaller value relies more on environment-driven learning.
Complexity Analysis:The main computational overhead of
the proposed framework is concentrated at the cloud-side
Teacher, including NKG construction/update, R-GAT feature
extraction, and LLM-based ToT reasoning, while the Student
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 12
Algorithm 2Multi-Agent Resource Allocation with Policy
Distillation based on MAPPO
Input:Number of episodesM, episode lengthT, number of
agentsN; teacher policyπ T (· |s); update epochsK upd;
Replay bufferR; actor parametersθand critic parameters
ψ.
Output:Student policy parametersθ ⋆.
1:forepisode= 1,2, . . . , Mdo
2:Reset the environment; obtain initial global states t and
local observationso t.
3:forslott= 1,2, . . . , Tdo
4:foreach UA Vn= 1,2, . . . , Ndo
5:Sample actiona t from the actorπ θ(· |o t).
6:end for
7:Execute the joint actiona(t); obtain rewardr t, next
global states t+1, and next observationso t+1.
8:Store
 
st, ot, at, rt, st+1, ot+1

intoR.
9:end for
10:Use the centralized criticV ψ(st)to compute boot-
strapped returns.
11:Compute TD error as in Eq. (38) and GAE as in
Eq. (37).
12:fork= 1,2, . . . , K upd do
13:Sample a mini-batchM ⊂ Rof sizeB.
14:foreach UA Vn= 1,2, . . . , Ndo
15:Compute the actor loss with PPO clipping as in
Eq. (35).
16:Compute the critic loss as in Eq. (39).
17:Compute the JS divergence between student and
teacher policies as in Eq. (43).
18:Form the total loss as in Eq. (44).
19:end for
20:Update the actor parametersθand the critic param-
etersψ.
21:end for
22:end for
23:returnθ ⋆.
Models deployed on UA Vs only perform lightweight online
decision-making.
For NKG maintenance, the update cost under incremen-
tal graph updates can be approximately characterized by
O(|∆V(t)|+|∆E(t)|+|∆X(t)|). For R-GAT feature ex-
traction, ignoring fixed feature dimensions, the approximate
per-slot complexity isO(L GAT ·M· P
r∈R |Er(t)|). For ToT
reasoning, using beam search with depthL, beam widthB,
and at mostK cand candidates per node, the search complexity
can be approximated asO(B×K cand ×L).
VI. SIMULATION RESULTS AND ANALYSIS
We conduct simulations using Python and PyTorch to
validate the performance of our proposed algorithm. The
simulation environment comprises a multi-UA V network with
four UA Vs operating at a fixed altitude of 100 m, maintaining
a minimum safety separation of 10 m. Each UA V is equipped
with a computing capability ranging from 10 to 20 GHz. The
channel bandwidths are 20 MHz for G2A links and 40 MHz
for A2A links, and the noise power is−100dBm [37]. For
propagation, we use a LoS path-loss exponent of 3 and add
an additional 23 dB attenuation for NLoS links [38]. For UD
tasks, the input data size is uniformly chosen from 1 to 3 MB,
and the required CPU cycles are 300–500 M cycles.
As the teacher model, we adopt GPT-4o as the pretrained
backbone and apply parameter-efficient fine-tuning via LoRA
with rankr= 8. The fine-tuned LLM performs ToT search
on the teacher side to generate and evaluate candidate actions;
the ToT hyperparameters are depthL= 3, beamB= 6,
and candidatesK cand = 5. The teacher then outputs an expert
policy distribution, which is used to perform policy distillation
and supervise the student MAPPO training. In the reward
design, the penalty coefficients are set toξ 1 = 4, ξ 2 =
2, ξ3 = 2, corresponding to the collision penalty, the energy-
budget violation penalty, and the penalty for unserved users,
respectively.
TABLE I
SIMULATION PARAMETER SETTINGS
Parameters Value
Number of UA VsN 4
Number of UDsK [10,60]
Height of UA VsH 100m
Minimum distance of UA Vsd min 10m
Data size of tasksD k(t) [1,3]MB
Computing workload of tasksW k(t) [300,500]M cycles
Allowed delay thresholdT max [250,300]ms
Channel bandwidth of G2AB k,n(t) 20MHz
Channel bandwidth of A2AB n,n′ 40MHz
Noise powerσ 2 -100dBm
Path lossη Los, ηN Los 3,23 dB
Computation resource of UA Vsf n(t) [10,20]GHz
Transmit power of UA Vsp n(t) 20dBm
Transmit power of UDsp k(t) 10dBm
The Rank of LoRAr 8
ToT hyperparameters(L, B, K cand)L 3, 6, 5
Accordingly, the experimental evaluation mainly focuses on
delay, fairness, and WDF performance, while the UA V energy
budget is enforced through Constraint C6 and the energy-
overflow penalty. To demonstrate the efficacy of our proposed
algorithm, we compare it against four baseline methods:
(1)Nearest: In a multi-UA V setting, each UD always offloads
its task to the UA V with the smallest Euclidean distance.
(2) PPO-Only: This variant uses PPO alone for optimization,
with no teacher model, no Tree-of-Thought reasoning, and no
knowledge distillation, all other settings match those of our
student model.
(3) 3D-MADDPG [39]: A fairness-aware scheme for multi-
UA V MEC scenarios. It employs MADDPG to jointly optimize
UA V selection and 3D trajectories under system constraints,
training with the objective of minimizing energy consumption
based on fairness among UA Vs.
(4)EEFC-TDBA [40]: This algorithm considers a single-
UA V scenario without inter-UA V collaboration and uses
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 13
/s48 /s50/s48/s48 /s52/s48/s48 /s54/s48/s48 /s56/s48/s48 /s49/s48/s48/s48
/s45/s57
/s45/s56
/s45/s55
/s45/s54
/s45/s53
/s45/s52
/s45/s51
/s45/s50
/s82/s101/s119/s97/s114/s100
/s69/s112/s105/s115/s111/s100/s101/s115
/s32/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45/s77/s65/s68/s68/s80/s71
/s32/s80/s80/s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70/s67/s45/s84/s68/s66/s65
Fig. 4. Comparison of reward of different algorithms
DDPG to optimize the UA V’s trajectory and resource allo-
cation.
Figure 4 presents the convergence performance of the
algorithms during training. As observed, the reward curves
for all methods increase steadily with the number of episodes
and eventually stabilize, indicating that the agents gradually
learn effective resource-allocation policies through interaction
with the environment. From the figure, the proposed method
rises more quickly and then levels off, demonstrating superior
sample efficiency and final performance. This advantage is
primarily due to the heuristic guidance provided by the teacher
model combined with ToT reasoning, which yields higher-
quality candidates and more stable exploration. Although 3D-
MADDPG enables multi-agent cooperation, it lacks teacher
guidance and a generate–score mechanism aligned with the
global objective, resulting in slower convergence and inferior
performance compared with our approach. PPO–Only, which
does not employ a teacher or knowledge distillation, learns
less efficiently; and EEFC–TDBA, lacking inter-UA V collab-
oration, performs the worst. Overall, the simulation results
strongly validate the significant advantages of our method in
convergence speed, final reward, and stability.
Figure 5 shows how the delay evolves with training episodes
across all methods. Overall, except for Nearest, the curves drop
rapidly and stabilize after approximately 300–400 episodes,
indicating that the agents progressively learn more efficient
access and resource allocation policies that shorten task com-
pletion time. The Proposed method decreases the fastest and
attains the lowest delay, suggesting that teacher guidance from
the LoRA-tuned LLM together with distillation regularization
based on JS divergence enables more prompt hotspot load
balancing across multiple UA Vs and more effective intra-
UA V resource reallocation; it also exploits A2A task migration
and bandwidth coordination more fully. 3D-MADDPG ranks
second; although it enables cooperation, it lacks teacher-driven
global-objective awareness and feasibility priors. PPO-Only,
which has neither teacher signals nor distillation, relies on
exploration and consequently converges more slowly, so both
/s48 /s50/s48/s48 /s52/s48/s48 /s54/s48/s48 /s56/s48/s48 /s49/s48/s48/s48
/s49/s56/s48
/s50/s48/s48
/s50/s50/s48
/s50/s52/s48
/s50/s54/s48
/s50/s56/s48
/s51/s48/s48
/s51/s50/s48
/s51/s52/s48
/s68/s101/s108/s97/s121/s40/s109/s115/s41
/s69/s112/s105/s115/s111/s100/s101/s115
/s32/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45/s77/s65/s68/s68/s80/s71
/s32/s80/s80/s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45/s84/s68/s66/s65
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 5. Comparison of delay for different algorithms
methods underperform the Proposed approach. EEFC-TDBA,
which lacks inter-UA V collaboration, exhibits markedly higher
delay. Nearest, whose distance-based association hardly im-
proves with training, remains at a high delay throughout. Taken
together, these results show that the Proposed method delivers
significantly better convergence speed, final delay, and stability
than the baselines.
Figure 6 shows how delay varies with the number of
devices. As the number of devices increases, competition for
access and computing resources intensifies and link interfer-
ence rises, leading to a higher system load; consequently, all
methods exhibit an overall increase in delay. The Proposed
method consistently achieves the lowest delay and shows the
smallest increase with scale, demonstrating superior scalabil-
ity. This advantage stems from teacher guidance and knowl-
edge distillation, which provide high-quality candidate actions
and constraint awareness, enabling the policy to proactively
load-balance hotspots across multiple UA Vs and coordinate
resource allocation via A2A task migration. 3D-MADDPG and
PPO-Only perform next best. EEFC-TDBA, which lacks inter-
UA V collaboration, is heavily affected by congestion. Nearest
performs substantially worse because it associates solely by
distance without load balancing, causing delay to increase
almost linearly as the number of devices grows. These results
indicate that the Proposed method maintains lower delay and
stronger scalability across a range of system sizes.
Figure 7 illustrates the relationship between UA V computing
capability and delay. As the capacity increases from low
to high, the delay of all methods decreases. The Proposed
method maintains the lowest delay across the entire range.
This advantage arises because teacher guidance and distillation
provide high-quality priors, enabling the policy to proactively
balance load and avoid congestion across multiple UA Vs,
while coordinating multi-dimensional resources—bandwidth
and computing—via A2A task migration. Consequently, queu-
ing and congestion overheads are effectively reduced. By com-
parison, although 3D-MADDPG and PPO-Only also benefit
from increased computing capacity, they remain inferior to
the Proposed method due to the absence of teacher priors or
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 14
/s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48 /s54/s48
/s49/s56/s48
/s50/s48/s48
/s50/s50/s48
/s50/s52/s48
/s50/s54/s48
/s50/s56/s48
/s51/s48/s48
/s51/s50/s48
/s68/s101/s108/s97/s121/s40/s109/s115/s41
/s78/s117/s109/s98/s101/s114/s32/s111/s102/s32/s68/s101/s118/s105/s99/s101/s115
/s32/s80/s114/s111/s112/s111/s115/s101 /s100
/s32/s51/s68/s45/s77/s65 /s68/s68/s80/s71 
/s32/s80/s80/s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45/s84 /s68/s66/s65 
/s32/s78/s101 /s97/s114/s101 /s115/s116
Fig. 6. Delay of different algorithms under different number of devices
limitations in multi-dimensional coordination. EEFC-TDBA,
which operates with a single UA V and lacks cooperative
computing, shows a weaker response to increased capac-
ity. Nearest relies solely on proximity-based association and
scarcely considers cross-UA V cooperation, making it the least
sensitive to capacity improvements; its curve is higher and
reaches a plateau earlier. Overall, the results indicate that
the Proposed method consistently achieves lower delay under
diverse computing-resource settings.
Figure 8 tracks the Jain’s fairness index during training.
In the early stages, when the policy has not yet matured,
bandwidth and computing resources tend to be skewed toward
a few users, leading to low fairness. With repeated interaction
with the environment and the influence of the fairness term
in the loss function, the agents gradually learn to allocate
resources more evenly; distillation from the teacher policy
distribution provides additional stable guidance, so fairness
increases overall and eventually stabilizes. In comparison, the
Proposed method rises the fastest and attains the highest level,
indicating that candidate generation and evaluation via the
LoRA-tuned LLM with ToT effectively suppress long-term
bias. Although 3D-MADDPG supports multi-agent coopera-
tion, it lacks teacher-guided global-objective awareness and
thus still exhibits mild imbalance. PPO-Only, which introduces
neither teacher signals nor knowledge distillation and relies
on exploration, converges more slowly; hence both methods
underperform the Proposed approach. EEFC-TDBA, which
lacks inter-UA V collaboration, performs worse. Nearest is a
simple non-learning strategy that associates purely by distance
without load balancing, so its fairness does not improve with
training. Overall, these results demonstrate that the Proposed
method improves fairness more efficiently and more robustly.
Figure 9 compares the Jain’s Fairness index across the
number of devices. As device count increases, competition
for access and computing resources intensifies and hotspots
and load imbalance become more likely, resulting in an overall
downward trend in fairness. The Proposed method experiences
the smallest decline and maintains the highest index across the
entire range, indicating that teacher guidance and distillation
regularization provide constraint awareness and high-quality
priors that enable the policy to proactively diffuse hotspots
across multiple UA Vs and to achieve more balanced intra-UA V
bandwidth reallocation. 3D-MADDPG and PPO-Only exhibit
some load awareness and decline more gradually as scale
grows, but without teacher-guided global-objective awareness
or distillation regularization, their redistribution capability lags
behind the Proposed method, and hotspot UA Vs gradually
become overloaded. EEFC-TDBA, which lacks inter-UA V co-
operation, achieves markedly lower fairness than the preceding
three methods. Nearest declines the most because its greedy,
distance-based association ignores instantaneous load, often
causing local overload and idle resources, thereby depressing
the Jain index. As the number of devices increases further, the
system approaches saturation and load proportions stabilize, so
the curves fluctuate mildly around a lower plateau toward the
end. Overall, the Proposed method maintains higher and more
stable fairness across different device counts.
Figure 10 compares the algorithms under two fairness
measures. To justify the choice of the Jain index for fairness,
we report both the Jain index and the Min–Max ratio as
fairness utility functions, where the Min–Max ratio is defined
asM= min1≤k≤K Rk(t)
max1≤k≤K Rk(t). Under both metrics, the five
methods follow the same ranking: Proposed ranks first, 3D-
MADDPG second, PPO-Only third, EEFC-TDBA fourth, and
Nearest last. This is consistent with the earlier conclusions
on delay, utility, and fairness. The Proposed method leads
on both metrics, indicating that, with teacher guidance from
the LoRA-LLM and ToT together with distillation, the policy
proactively diffuses hotspots across multiple UA Vs and, within
each UA V , achieves more balanced resource allocation, thereby
markedly reducing the phenomenon of persistent neglect of a
small subset of users.
In addition, the Jain index values are overall higher than
those of the Min–Max ratio, reflecting that the latter is more
sensitive to extremes (best and worst users) and therefore
yields more conservative scores under the same policy. Never-
theless, both metrics produce the same relative ordering, which
confirms the robustness advantage of the proposed approach
and supports using the Jain index as a reasonable and more
discriminative fairness measure.
Figure 11 illustrates how the WDF evolves over training
episodes, where lower curves indicate smaller WDF values.
Except for Nearest, all methods drop rapidly with episodes and
then gradually stabilize, showing that the policies learn a better
trade-off between delay and fairness. The Proposed method re-
mains the lowest throughout and exhibits the smallest variance,
indicating that teacher guidance from the LoRA-tuned LLM
together with ToT and policy distillation enables the agent
to reduce task delay and improve resource allocation fairness
simultaneously, with better stability. 3D-MADDPG ranks sec-
ond: although it supports cooperation, it lacks teacher-guided
awareness of the global objective and feasibility priors, thus
yielding higher values than the Proposed method. PPO-Only,
which does not use a teacher or distillation and relies mainly
on exploration, converges more slowly and attains a higher
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 15
/s49/s48 /s49/s50 /s49/s52 /s49/s54 /s49/s56 /s50/s48
/s50/s48/s48
/s50/s50/s48
/s50/s52/s48
/s50/s54/s48
/s50/s56/s48
/s51/s48/s48
/s51/s50/s48
/s51/s52/s48
/s68/s101/s108/s97/s121/s40/s109/s115/s41
/s85/s65/s86/s32/s67/s111/s109/s112/s117/s116/s97/s116/s105/s111/s110/s32/s67/s97/s112/s97/s98/s105/s108/s105/s116/s121 /s40/s71/s72/s122/s41
/s32/s80 /s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45 /s77/s65/s68/s68/s80 /s71
/s32/s80 /s80 /s79/s45 /s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45 /s84/s68/s66/s65
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 7. Delay with different UA V computing capability
/s50/s48/s48 /s52/s48/s48 /s54/s48/s48 /s56/s48/s48 /s49/s48/s48/s48
/s48/s46/s55/s48
/s48/s46/s55/s53
/s48/s46/s56/s48
/s48/s46/s56/s53
/s48/s46/s57/s48
/s48/s46/s57/s53
/s74/s97/s105/s110 /s115/s32/s70/s97/s105/s114/s110/s101/s115/s115/s32/s73/s110/s100/s101/s120
/s69/s112/s105/s115/s111/s100/s101/s115
/s32/s80 /s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45/s77/s65 /s68/s68/s80 /s71 
/s32/s80 /s80 /s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70/s67/s45/s84 /s68/s66/s65 
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 8. Comparison of Jain’s fairness index for different algorithms
objective value. EEFC-TDBA, lacking collaboration among
UA Vs, is strongly affected by congestion. Nearest, which
greedily associates by distance, shows almost no improvement.
This ranking is consistent with the earlier results on delay
and fairness, further confirming that the proposed algorithm
improves overall QoS.
Figure 12 shows the relationship between the WDF and the
UA V computing capacity. As computing capacity increases,
the WDF exhibits an overall decline. Higher CPU frequencies
markedly shorten both local and cooperative computation time
while also improving fairness, thereby benefiting both delay
and fairness simultaneously. The Proposed method attains the
lowest overall cost across the entire range because the LLM-
based teacher model supplies high-quality expert policies that
enable joint optimization of access, trajectory, and resource
allocation. 3D-MADDPG and PPO-Only also benefit from
increased capacity; however, lacking teacher priors and with
limited multi-dimensional coordination, they remain inferior
to the Proposed method. EEFC-TDBA adopts a single-UA V
perspective without cooperative computing and therefore re-
/s48 /s49/s48 /s50/s48 /s51/s48 /s52/s48 /s53/s48 /s54/s48
/s48/s46/s55/s53
/s48/s46/s56/s48
/s48/s46/s56/s53
/s48/s46/s57/s48
/s48/s46/s57/s53
/s74/s97/s105/s110/s39/s115/s32/s70/s97/s105/s114/s110/s101/s115/s115/s32/s73/s110/s100/s101/s120
/s78/s117/s109/s98/s101/s114/s32/s111/s102/s32/s68/s101/s118/s105/s99/s101/s115
/s32/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45/s77/s65/s68/s68/s80/s71
/s32/s80/s80/s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45/s84/s68/s66/s65
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 9. Jain’s fairness index of different algorithms under different number
of devices
/s80/s114/s111/s112/s111/s115/s101/s100
/s51/s68/s45/s77/s65/s68/s68/s80/s71
/s80/s80/s79/s45/s79/s110/s108/s121
/s69/s69/s70/s67/s45/s84/s68/s66/s65
/s78/s101/s97/s114/s101/s115/s116
/s48/s46/s48
/s48/s46/s50
/s48/s46/s52
/s48/s46/s54
/s48/s46/s56
/s49/s46/s48
/s70/s97/s105/s114/s110/s101/s115/s115
/s65/s108/s103/s111/s114/s105/s116/s104/s109
/s32/s74/s97/s105/s110/s39/s115/s32/s105/s110/s100/s101/s120
/s32/s77 /s105/s110 /s77 /s97/s120/s32/s82/s97/s116/s105/s111
Fig. 10. Comparison of the different algorithms under two fairness measures
sponds more weakly to capacity improvements. Nearest relies
solely on nearest association without cross-UA V coordination,
resulting in the highest overall cost.
Figure 13 plots the WDF versus bandwidth. As bandwidth
increases from 30 MHz to 70 MHz, the WDF of all methods
decreases overall, indicating that greater available bandwidth
effectively mitigates link congestion and queuing delays and
thus reduces the objective value. The Proposed method attains
the lowest values at all bandwidth points, reflecting stronger
coordinated resource allocation under teacher guidance and
distillation; moreover, its decline is more pronounced as
bandwidth grows, showing that the policy effectively con-
verts added bandwidth into improvements in both delay and
fairness. 3D-MADDPG and PPO-Only rank next: although
they benefit to some extent from additional bandwidth, the
lack of teacher-driven global scoring and feasibility priors
leaves residual resource bias. EEFC-TDBA, which lacks inter-
UA V cooperation, gains only limited benefit from bandwidth
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 16
/s48 /s50/s48/s48 /s52/s48/s48 /s54/s48/s48 /s56/s48/s48 /s49/s48/s48/s48
/s48/s46/s52/s48
/s48/s46/s52/s53
/s48/s46/s53/s48
/s48/s46/s53/s53
/s48/s46/s54/s48
/s48/s46/s54/s53
/s48/s46/s55/s48
/s48/s46/s55/s53
/s48/s46/s56/s48
/s48/s46/s56/s53
/s87/s68/s70
/s69/s112/s105/s115/s111/s100/s101/s115
/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45/s77/s65/s68/s68/s80/s71
/s32/s80/s80/s79/s45/s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45/s84 /s68/s66/s65
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 11. Comparison of WDF for different algorithms
TABLE II
ABLATION STUDY OF THE PROPOSED FRAMEWORK.
Method Components Metrics
NKG R-GAT ToT Distill. Delay Fairness WDF
Ours✓ ✓ ✓ ✓244 0.918 0.448
w/o ToT✓ ✓×✓252 0.903 0.486
w/o R-GAT✓×✓ ✓259 0.891 0.522
w/o NKG×✓ ✓ ✓266 0.879 0.558
w/o Distill.✓ ✓ ✓×273 0.862 0.594
expansion. Nearest associates solely by distance without load
balancing, yielding the highest objective value and the small-
est improvement. These results align with the episode-wise
convergence trends, indicating that larger bandwidth gener-
ally lowers system cost, while cooperation and hierarchical
decision-making remain advantageous across all bandwidth
settings.
To further validate the contribution of each key component,
we conduct an ablation study by removing the NKG module,
the R-GAT module, the ToT-based teacher reasoning module,
and the Teacher-to-Student distillation module, respectively.
As shown in Table II, the full model achieves the best overall
performance in terms of delay, fairness, and WDF. Removing
any one of these modules leads to a consistent performance
degradation. In particular, removing the distillation module
causes the largest drop, indicating that the Teacher-guided
policy transfer plays a critical role in improving the final
Student policy. Removing ToT also leads to a clear degrada-
tion, which confirms the importance of structured multi-branch
candidate exploration in the Teacher module. In addition, the
performance drops of w/o NKG and w/o R-GAT verify the
effectiveness of structured knowledge modeling and relation-
aware feature extraction for multi-UA V cooperative resource
allocation.
VII.CONCLUSION
In this paper, we propose an LLM-based teacher–student
joint optimization framework for 6G multi-UA V edge coop-
erative networks. The teacher model, operating with a global
/s49/s48 /s49/s50 /s49/s52 /s49/s54 /s49/s56 /s50/s48
/s48/s46/s52/s48
/s48/s46/s52/s53
/s48/s46/s53/s48
/s48/s46/s53/s53
/s48/s46/s54/s48
/s48/s46/s54/s53
/s48/s46/s55/s48
/s48/s46/s55/s53
/s48/s46/s56/s48
/s87/s68/s70
/s85/s65/s86/s32/s67/s111/s109/s112/s117/s116/s97/s116/s105/s111/s110/s32/s67/s97/s112/s97/s98/s105/s108/s105/s116/s121 /s40/s71/s72/s122/s41
/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45 /s77/s65/s68/s68/s80/s71
/s32/s80/s80/s79/s45 /s79/s110/s108/s121 
/s32/s69/s69/s70/s67/s45 /s84/s68/s66/s65
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 12. WDF with different UA V computing capability
/s51/s48 /s52/s48 /s53/s48 /s54/s48 /s55/s48
/s48/s46/s48
/s48/s46/s49
/s48/s46/s50
/s48/s46/s51
/s48/s46/s52
/s48/s46/s53
/s48/s46/s54
/s48/s46/s55
/s48/s46/s56
/s48/s46/s57
/s87/s68/s70
/s66/s97/s110/s100/s119/s105/s100/s116/s104/s40/s77/s72/s122/s41
/s32/s80/s114/s111/s112/s111/s115/s101/s100
/s32/s51/s68/s45 /s77/s65 /s68/s68/s80/s71 
/s32/s80/s80/s79/s45 /s79/s110/s108/s121 
/s32/s69/s69/s70 /s67/s45 /s84 /s68/s66/s65 
/s32/s78/s101/s97/s114/s101/s115/s116
Fig. 13. WDF with different Bandwidth
view, produces high-quality expert resource-allocation policies
that serve as priors for the student. The student model adopts
MAPPO augmented with a policy distillation; under a joint
objective balancing latency and fairness, it makes coordinated
decisions on access control, UA V trajectory planning, compu-
tation and bandwidth allocation, and A2A task migration ratio.
Simulations demonstrate that, relative to strong baselines,
our approach achieves faster convergence, lower steady-state
latency, and improved fairness, while maintaining robustness
and scalability as the network size and the available computing
and bandwidth resources vary.

## § References

[1] L. Wanget al., “Joint Task Offloading and Migration Optimization in
UA V-Enabled Dynamic MEC Networks,”IEEE Trans. Services Comput.,
vol. 18, no. 4, pp. 2143–2157, Jul./Aug. 2025.
[2] H. Guo, Y . Wang, J. Liu and C. Liu, “Multi-UA V Cooperative Task
Offloading and Resource Allocation in 5G Advanced and Beyond,”IEEE
Trans. Wireless Commun., vol. 23, no. 1, pp. 347–359, Jan. 2024.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 17
[3] P. Caoet al., “Computational Intelligence Algorithms for UA V Swarm
Networking and Collaboration: A Comprehensive Survey and Future
Directions,”IEEE Commun. Surv. Tutor., vol. 26, no. 4, pp. 2684–2728,
fourthquarter 2024.
[4] S. Javaid, H. Fahim, B. He and N. Saeed, “Large Language Models for
UA Vs: Current State and Pathways to the Future,”IEEE Open J. Veh.
Technol., vol. 5, pp. 1166–1192, 2024.
[5] J. Zhanget al., “Decision Transformers for Wireless Communications: A
New Paradigm of Resource Management,”IEEE Wireless Commun., vol.
32, no. 2, pp. 180–186, Apr. 2025.
[6] W. Zhaoet al., “A Survey on DRL-Based UA V Communications
and Networking: DRL Fundamentals, Applications and Implementa-
tions,”IEEE Commun. Surv. Tutor., early access, Jun. 23, 2025, doi:
10.1109/COMST.2025.3581912.
[7] S. Longet al., “A Survey on Intelligent Network Operations
and Performance Optimization Based on Large Language Mod-
els,”IEEE Commun. Surv. Tutor., early access, Jan. 07, 2025, doi:
10.1109/COMST.2025.3526606.
[8] H. Kurunathan, H. Huang, K. Li, W. Ni and E. Hossain, “Machine
Learning-Aided Operations and Communications of Unmanned Aerial
Vehicles: A Contemporary Survey,”IEEE Commun. Surv. Tutor., vol. 26,
no. 1, pp. 496–533, firstquarter 2024.
[9] G. Qu, Q. Chen, W. Wei, Z. Lin, X. Chen and K. Huang, “Mobile
Edge Intelligence for Large Language Models: A Contemporary Sur-
vey,”IEEE Commun. Surv. Tutor., early access, Jan. 09, 2025, doi:
10.1109/COMST.2025.3527641.
[10] L. Cai, R. Zhang, C. Zhao,et al., “Large Language Model-Enhanced
Reinforcement Learning for Low-Altitude Economy Networking,”arXiv
preprintarXiv:2505.21045, 2025.
[11] X. Li, H. Li, C. Sun, Q. Fan, Z. Han and V . C. M. Leung, “Edge-
Enhanced Intelligence: A Comprehensive Survey of Large Language
Models and Edge–Cloud Computing Synergy,”IEEE Commun. Surv.
Tutor., early access, 2025, doi: 10.1109/COMST.2025.3587225.
[12] P. F. Moshiri, M. A. Onsu, P. Lohan,et al., “Integrating Language
Models for Enhanced Network State Monitoring in DRL-Based SFC
Provisioning,”arXiv preprintarXiv:2502.11298, 2025.
[13] H. Pang, Z. Wang and G. Li, “Large Language Model Guided Deep
Reinforcement Learning for Decision Making in Autonomous Driving,”
arXiv preprintarXiv:2412.18511, 2024.
[14] Z. Zhou, B. Hu, C. Zhao,et al., “Large Language Model as a Policy
Teacher for Training Reinforcement Learning Agents,”arXiv preprint
arXiv:2311.13373, 2023.
[15] Z. Bai, Y . Lin, Y . Cao and W. Wang, “Delay-Aware Cooperative
Task Offloading for Multi-UA V Enabled Edge–Cloud Computing,”IEEE
Trans. Mobile Comput., vol. 23, no. 2, pp. 1034–1049, Feb. 2024.
[16] C. Wanget al., “Computing Power in the Sky: Digital Twin-Assisted
Collaborative Computing With Multi-UA V Networks,”IEEE Trans. Veh.
Technol., vol. 74, no. 9, pp. 14466–14482, Sept. 2025.
[17] H. Hu, X. Zhu, F. Zhou, W. Wu, R. Q. Hu and H. Zhu, “Resource Allo-
cation for Multi-Modal Semantic Communication in UA V Collaborative
Networks,”IEEE Trans. Commun., vol. 73, no. 9, pp. 7599–7616, Sept.
2025.
[18] F. Pervez, A. Sultana, C. Yang and L. Zhao, “Energy and Latency
Efficient Joint Communication and Computation Optimization in a Multi-
UA V-Assisted MEC Network,”IEEE Trans. Wireless Commun., vol. 23,
no. 3, pp. 1728–1741, Mar. 2024.
[19] Y . Gao, J. Tao, Y . Xu, Z. Wang, Y . Gao and M. Wang, “Improving
User QoE via Joint Trajectory and Resource Optimization in Multi-UA V
Assisted MEC,”IEEE Trans. Services Comput., vol. 18, no. 3, pp. 1472–
1486, May/Jun. 2025.
[20] P. Qin, M. Fu, Y . Fu and J. Wang, “Cooperative UA V Trajectory
Design and Resource Allocation in Blockchain-Enabled Secure Aerial
Edge Computing Network,”IEEE Trans. Wireless Commun., early access,
2025, doi: 10.1109/TWC.2025.3582151.
[21] A. Mohajer, J. Hajipour and V . C. M. Leung, ”Dynamic Offloading
in Mobile Edge Computing With Traffic-Aware Network Slicing and
Adaptive TD3 Strategy,”IEEE Commun. Lett., vol. 29, no. 1, pp. 95-
99, Jan. 2025.
[22] G. Liu, N. Van Huynh, H. Du,et al., “Generative AI for Unmanned
Vehicle Swarms: Challenges, Applications and Opportunities,”arXiv
preprintarXiv:2402.18062, 2024.
[23] D. Yeet al., “Optimizing AIGC Services by Prompt Engineering and
Edge Computing: A Generative Diffusion Model-Based Contract Theory
Approach,”IEEE Trans. Veh. Technol., vol. 74, no. 1, pp. 571–586, Jan.
2025.
[24] X. Zhanget al., “Beyond the Cloud: Edge Inference for Generative
Large Language Models in Wireless Networks,”IEEE Trans. Wireless
Commun., vol. 24, no. 1, pp. 643–658, Jan. 2025.
[25] Y . Hu, D. Ye, J. Kang, M. Wu and R. Yu, “A Cloud–Edge Collaborative
Architecture for Multimodal LLM-Based Advanced Driver Assistance
Systems in IoT Networks,”IEEE Internet Things J., vol. 12, no. 10,
pp. 13208–13221, 15 May 2025.
[26] M. Zhang, X. Shen, J. Cao, Z. Cui and S. Jiang, “EdgeShard: Efficient
LLM Inference via Collaborative Edge Computing,”IEEE Internet Things
J., vol. 12, no. 10, pp. 13119–13131, 15 May 2025.
[27] Y . Tian, F. Lin, Y . Li,et al., “UA Vs Meet LLMs: Overviews and
Perspectives Towards Agentic Low-Altitude Mobility,”Inf. Fusion, vol.
122, Art. no. 103158, 2025.
[28] S. Zhanget al., “Large Models for Aerial Edges: An Edge–Cloud Model
Evolution and Communication Paradigm,”IEEE J. Sel. Areas Commun.,
vol. 43, no. 1, pp. 21–35, Jan. 2025.
[29] G. Sunet al., “Large Language Model (LLM)-Enabled Graphs in
Dynamic Networking,”IEEE Network, vol. 39, no. 4, pp. 290–301, Jul.
2025.
[30] H. Li, M. Xiao, K. Wang, D. I. Kim and M. Debbah, “Large Language
Model Based Multi-Objective Optimization for Integrated Sensing and
Communications in UA V Networks,”IEEE Wireless Commun. Lett., vol.
14, no. 4, pp. 979–983, Apr. 2025.
[31] Y . Ren, H. Zhang, F. R. Yu, W. Li, P. Zhao and Y . He, “Industrial Internet
of Things With Large Language Models (LLMs): An Intelligence-Based
Reinforcement Learning Approach,”IEEE Trans. Mobile Comput., vol.
24, no. 5, pp. 4136–4152, May 2025.
[32] X. Xu, G. Feng, S. Qin, Y . Liu and Y . Sun, “Joint UA V Deployment
and Resource Allocation: A Personalized Federated Deep Reinforcement
Learning Approach,”IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 4005–
4018, Mar. 2024.
[33] J. Yinet al., “QoS-Aware Energy-Efficient Multi-UA V Offloading Ratio
and Trajectory Control Algorithm in Mobile-Edge Computing,”IEEE
Internet Things J., vol. 11, no. 24, pp. 40588–40602, 15 Dec. 2024.
[34] R. K. Jainet al., “A Quantitative Measure of Fairness and Discrimina-
tion,” Eastern Res. Lab., Digit. Equip. Corporation, Hudson, MA, Rep.
vol. 21, pp. 1–38, 1984.
[35] S. Yao, D. Yu, J. Zhao,et al., “Tree of Thoughts: Deliberate Problem
Solving With Large Language Models,”Adv. Neural Inf. Process. Syst.,
vol. 36, pp. 11809–11822, 2023.
[36] J. Wei, X. Wang, D. Schuurmans,et al., “Chain-of-Thought Prompting
Elicits Reasoning in Large Language Models,”Adv. Neural Inf. Process.
Syst., vol. 35, pp. 24824–24837, 2022.
[37] H. Hao, C. Xu, W. Zhang, S. Yang and G.-M. Muntean, “Joint Task
Offloading, Resource Allocation, and Trajectory Design for Multi-UA V
Cooperative Edge Computing With Task Priority,”IEEE Trans. Mobile
Comput., vol. 23, no. 9, pp. 8649–8663, Sept. 2024.
[38] “Study on Enhanced LTE Support for Aerial Vehicles (Release 15),”
3GPP Std. 36.777, Dec. 2017.
[39] Y . He, Y . Gan, H. Cui and M. Guizani, “Fairness-Based 3-D Multi-UA V
Trajectory Optimization in Multi-UA V-Assisted MEC System,”IEEE
Internet Things J., vol. 10, no. 13, pp. 11383–11395, 1 Jul. 2023.
[40] R. Ding, F. Gao and X. S. Shen, “3D UA V Trajectory Design and
Frequency Band Allocation for Energy-Efficient and Fair Communica-
tion: A Deep Reinforcement Learning Approach,”IEEE Trans. Wireless
Commun., vol. 19, no. 12, pp. 7796–7809, Dec. 2020.
Yaqing Wangreceived the M.S. degree from
Guangxi Normal University, Guilin, Guangxi, China,
in 2021. She is currently pursuing the Ph.D. degree
in communication and information systems with
Chongqing University of Posts and Telecommuni-
cations, Chongqing, China. Her current research
interests include edge intelligence computing, digital
twin, and intelligent network management.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply. 
JOURNAL OF LATEX CLASS FILES, VOL. 18, NO. 9, SEPTEMBER 2020 18
Lun Tangreceived the Ph.D. degree in communica-
tion and information system from Chongqing Uni-
versity, Chongqing, China, in 2010. He is currently
a professor with the School of Communication and
Information Engineering, Chongqing University of
Posts and Telecommunications. His current research
interests include digital twin networks, 5G/6G, In-
dustrial Internet of Things, and the Internet of Ve-
hicles.
Weili Wangreceived the M.E. and Ph.D. degrees
in information and communication engineering from
Chongqing University of Posts and Telecommu-
nications, Chongqing, China, in 2018 and 2023,
respectively. She was a Visiting Researcher with
Carleton University, Ottawa, ON, Canada, from De-
cember 2021 to January 2023. She is currently a
Postdoctoral Researcher with Cyber Security and
Information Law Research Center, Chongqing. Her
current research interests include intelligent network
management and self-healing techniques in 6G.
Xiaoqiang Hereceived the Ph.D degree in
Chongqing University of Posts and Telecommuni-
cations, Chongqing, China, in 2023. He is cur-
rently a lecturer with College of Communication
Engineering, Chongqing Polytechnic University of
Electronic Technology. From May 2019 to October
2020, he was a Visiting Graduate Student (Ph.D. stu-
dent) with the Department of Electrical, Computer,
and Biomedical Engineering, Ryerson University,
Canada. His current research interests include mo-
bile edge computing, edge intelligence computing,
intrusion detection system, and digital twin.
Qianbin Chen(M’03-SM’14) received the Ph.D.
degree in communication and information system
from the University of Electronic Science and Tech-
nology of China, Chengdu, China, in 2002. He is
currently a Professor with the School of Commu-
nication and Information Engineering, Chongqing
University of Posts and Telecommunications, and the
Director of the Chongqing Key Laboratory of Mo-
bile Communication Technology. He has authored
or co-authored over 100 papers in journals and
peer-reviewed conference proceedings, and has co-
authored seven books. He holds 47 granted national patents.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3683128
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:54:26 UTC from IEEE Xplore.  Restrictions apply.
