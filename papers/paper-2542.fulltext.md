---
paper_id: "paper-2542"
source_pdf_sha: "f8aaf72f2b116ae7bb1e76b8c45443f8370ada68b2ae2a657e1b73b26bc5b3ec"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 1
  page_count: 13
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2542 — fulltext
## §unknown-1

IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 1
Generative AI-Enabled Transmission and
Computing Integration for Cloud-Edge
Collaborative IoT
Haoyu Ci, Yuxiang Leng, Ziming Li, Yiming Chen, Haijun Liao, Member, IEEE,
Zhenyu Zhou, Senior Member, IEEE, Wenqing Wu, and Xiaoyan Wang, Senior Member, IEEE
Abstract—Cloud–edge collaborative internet of things (IoT)
enables consumer energy management by exploring task offload-
ing and migration for low-latency processing. However, treat-
ing transmission and computing separately leads to inefficient
resource utilization. Furthermore, in queue backlogs with long-
tail distributions, traditional learning based approaches exhibit
deteriorated performance because rare but critical backlog sce-
narios remain undervalued. Therefore, we propose a generative
artificial intelligence (GAI)-enabled transmission and computing
integration framework to intelligently distribute workloads based
on channel conditions and cloud–edge capabilities. For transmis-
sion, GAI-assisted upper confidence bound (UCB) is proposed for
device-side offloading compression ratio optimization. It adjusts
exploration weight dynamically, ensuring robust transmission
reliability under varying channel conditions. For computing,
GAI-enhanced federated deep Q-network (FDQN) is developed
to jointly optimize task migration and computing resource allo-
cation. GAI synthesizes rare events and extreme experiences for
augmented training of global DQN, enabling adaptive learning
and robustness under extreme events. Simulation results demon-
strate that the proposed algorithm’s effectiveness in reducing
delay while ensuring long-term transmission reliability.
Index Terms —Cloud–edge collaboration, IoT, generative AI,
upper confidence bound, transmission–computing integration.
I. I NTRODUCTION
In consumer-side energy management, internet of things
(IoT) play a pivotal role in real-time monitoring and optimal
control. By embedding IoT nodes into distributed photo-
voltaics (PV), charging piles, and other electrical equipment,
they continuously collect high-frequency electrical parameters
[1], [2]. These data are uploaded to edge or cloud servers for
processing and analysis [3], [4]. Edge servers, geographically
close to consumers, can deliver millisecond-level respon-
siveness. However, their constrained computing and storage
This work was supported by Beijing Natural Science Foundation under
Grant Number 4254074, the Fundamental Research Funds for the Central
Universities under Grant Number 2025MS007, the Postdoctoral Fellowship
Program of CPSF under Grant Number GZB20250124, National Natural
Science Foundation of China (NSFC) under Grant Number 62501235, the
National Science and Technology Major Project of China under Grant Number
2025ZD0805901, and Grant-in-Aid for Scientific Research(C) (23K11080).
H. Ci, Y . Leng, Z. Li, Y . Chen, H. Liao, Z. Zhou, and W. Wu are with the
School of Electrical and Electronic Engineering, North China Electric Power
University, Beijing 102206, China (e-mail: {haoyu ci, 120231020409, zim-
ing li, yiming chen, haijun liao, zhenyu zhou, wenqing wu}@ncepu.edu.cn.
Corresponding author: Haijun Liao .
X. Wang is with Graduate School of Science and Engi-
neering, Ibaraki University, Ibaraki 316-8511, Japan (e-mail:
xiaoyan.wang.shawn@vc.ibaraki.ac.jp).
capacities cause large queue backlogs under peak loads or
traffic bursts [5]. Cloud servers, offer abundant computing re-
sources but suffer from long-distance network congestion and
transmission delay, exhibiting pronounced uncertainty [6], [7].
Therefore, it is imperative to construct a novel collaborative
data processing framework combining the complemented ad-
vantages of cloud and edge for IoT-empowered consumer-side
energy management. This new framework can dynamically
balance load distributions from a global perspective and ensure
low-latency high-reliability data processing.
Transmission and computing integration is the core for
achieving cloud–edge collaborative IoT [8]. For transmission,
by dynamically optimizing task-offloading compression ratio
of IoT devices, the volume of end-edge offloaded data is
substantially reduced [9]. For computing, fine-grained task
migrations allow computation intensive tasks on heavily-
loaded edge servers to be migrated in real time to lightly-
loaded edge or cloud servers, improving computing resource
utilization efficiency and global load balance [10]. Moreover,
computing resource allocation can be allocated on demand
according to real-time queue backlogs, further suppressing
queue oscillations [11]. However, transmission and computing
integrated optimization is extremely complex considering the
high dynamics of data arrivals, channel gains, and computing
resource distributions. Conventional model-based approaches
cannot be applied effectively due to the lack of global state
information.
Reinforcement learning leverages a closed-loop interac-
tion–feedback–update mechanism to perform distributed op-
timization without relying on exact mathematical models.
Within this framework, upper confidence bound (UCB) which
dynamically balances exploration and exploitation through
a confidence-driven approach has been widely utilized in
IoT and end-edge transmission optimization. In [12], Sun et
al. developed a data offloading method leveraging UCB to
cope with vehicular edge computing under dynamic mobility
conditions. In [13], Sun et al. proposed a task offloading
method applying classical UCB in vehicular cloud computing,
which achieved minimized average offloading delay without
real-time state exchange. In [14], Qiao et al. introduced
a trustworthy edge storage method based on UCB, which
leveraged server trust values and data popularity to guide
storage decisions. However, these methods generally focus on
the decentralized arm-selection problem and are not suitable
for high-dimensional optimization problems of transmission
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 2
and computing integration. Its confidence bounds struggle to
adapt to the dynamic interplay of large optimization dimen-
sions, while its static exploration-exploitation trade-off fails to
capture temporal correlations in edge environments.
To tackle these challenges, deep Q-network (DQN) emerges
as a promising alternative. It leverages deep reinforcement
learning to approximate value functions for high-dimensional
state-action spaces, enabling adaptive policy optimization [15].
In [16], Hu et al. proposed a DQN-based task-migration
method solving the dynamic offloading and resource alloca-
tion challenges under high-dimensional state-complex action
coupling. In [17], Cheng et al. presented a task offloading
and resource allocation method that combines double DQN
network update mechanism with dueling DQN dual-branch
structure. In [18], Zhou et al. proposed a method that applied
the double DQN algorithm to joint computation offloading and
resource allocation. Nevertheless, these approaches suffer from
issues such as poor adaptations for extreme scenarios because
of DQN’s reliance on extensive real-world interactions for
training [19]. They also make insufficient utilization of global
observations due to the lack of collaborative model training
and knowledge sharing.
Generative adversarial networks (GAN) as an important
subset of generative artificial intelligence (GAI) leverage an
adversarial training mechanism to accurately fit and extrapo-
late the probability distribution of real data in the feature space,
thereby providing deep reinforcement learning with high-
quality synthetic samples such as scarce channel trajectories
and computing load distributions [20], [21]. This significantly
expands the experience replay buffer and enhances the robust-
ness of the policy network against extreme events. In [22],
Zhao et al. used a self-attention GAN to synthesize distributed-
generator outputs and line-damage data under extreme events
and trained a double DQN on these samples. In [23], Zhu
et al. used Wasserstein GAN adversarial training mechanism
to generate worst-case scenarios and iteratively injected them
into DQN training, solving the issue of insufficient robust-
ness. In [24], Guo et al. introduced a GAN-powered routing
scheme that generated network state samples in real time and
integrated them into DQN for routing decisions.
Despite recent research progresses, many critical issues
remain open. First, although recent literature actively ad-
dresses joint communication and data compression in IoT edge
networks, existing studies generally treat these transmission
strategies and computing resource allocation as completely
independent problems. This lack of an integrated frame-
work inevitably leads to heterogeneous resource mismatch
and suboptimal optimization performances. Second, traditional
UCB-based approaches cannot dynamically adjust exploration
weights based on channel conditions. This results in insuf-
ficient exploration during good channel states or excessive
packet loss during poor channel conditions, violating the long-
term transmission reliability constraint. Last but not least,
rare events such as severe traffic bursts and drastic channel
deteriorations induce long-tail distributions in system states
[25]. Consequently, the joint optimization of edge-side task
migration and computing resource allocation suffers from
sample scarcity. This causes severe performance degradation
under extreme events despite GAN-assisted DQN training.
These shortcomings stem from the lack of conditional control
over the generation process, making it challenging to gen-
erate specific or targeted data samples required in complex
transmission-computing integration scenarios.
To address the above challenges, we propose a GAI-
enabled transmission and computing integration algorithm
for cloud–edge collaborative IoT. First, we formulate a low-
latency task data processing problem for consumer energy
management applications. The objective is to minimize the
long-term average end-to-end cloud–edge collaborative pro-
cessing delay. Second, leveraging Lyapunov optimization, the
long-term latency minimization and reliability constraints are
decoupled into per-slot deterministic optimization subprob-
lems, i.e., task offloading compression ratio decisions sub-
problem, and task migration and edge computing resource
allocation subproblem. For transmission optimization, the pro-
posed algorithm leverages GAN-assisted UCB to solve the
first subproblem. For computing optimization, the proposed
algorithm leverages GAI-enhanced FDQN to solve the second
subproblem. The main contributions of this paper are summa-
rized as follows:
1) GAI-enabled transmission and computing integra-
tion framework for cloud–edge collaborative IoT: By
unifying data transmission and computing optimization,
this novel framework intelligently distributes workloads
based on real-time channel conditions and cloud–edge
capabilities. It facilitates adaptive resource sharing, par-
allel processing, and GAI-assisted learning enhancement
to improve load balancing and minimize data processing
delay.
2) GAI-assisted UCB for device-side offloading com-
pression ratio optimization: It leverages GAN to ex-
trapolate channel gain distributions for dynamic explo-
ration weight adjustment. Exploration is prioritized to
discover optimal strategies during high-quality channel
states, while exploitation of known reliable configu-
rations is emphasized under poor channel conditions.
This intelligent adaptation to channel gain fluctuations
ensures robust transmission reliability.
3) GAI-enhanced FDQN for joint edge task migration
and computing-resource optimization: It leverages
conditional GAN (CGAN) to synthesize rare events and
extreme experiences for augmented training of global
DQN. The enhanced global model is distributed to edge
servers through a performance-aware weighted federated
aggregation mechanism. This approach effectively miti-
gates challenges posed by scarce long-tail samples and
unobservable global states. It ensures adaptive learning
across heterogeneous environments and significantly en-
hancing policy’s robustness to extreme events.
II. S YSTEM MODEL
The proposed framework of transmission and computing
integration for cloud–edge collaborative IoT is shown in Fig.
1. It consists of device layer, edge layer, cloud layer, and
application layer.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 3
Fig. 1. The proposed integrated framework for cloud–edge collaborative IoT transmission and computing.
TABLE I
NOMENCLATURE
Notation Description Notation Description
J Set of edge servers, indexed by j P k,j (t) Transmission power of device dj,k
J Total number of edge servers hk,j (t) Channel gain between dj,k and server j
Kj Set of IoT devices served by edge server j W k,j (t) Successful data reception probability
dj,k The k-th IoT device with edge server j L k,j (t) V olume of lost data during transmission
T Set of time slots, indexed by t x k,j,j′ (t) Binary task migration decision variable
τ Duration of a single time slot Qk,j (t) Computation queue backlog at edge server j
Qk(t) Data backlog in device dj,k’s local queue Yk,j (t) Amount of task data processed by server j
Ak(t) Newly collected data by device dj,k fk,j (t) CPU frequency allocated to dj,k’s task
yk(t) Data compression ratio for device dj,k f max
j (t) Max CPU frequency of edge server j
U tx
k,j (t) Compressed data offloaded to edge λk Computation intensity (cycles/bit)
Rk,j (t) Transmission rate from dj,k to server j τ tot
k,j (t) Total end-to-end processing delay
Bk,j Communication bandwidth Zk,j (t) Virtual queue for reliability constraint
V Lyapunov control parameter Lmax Max tolerable long-term packet loss
• Application Layer : Based on the data processed by
edge and cloud layers, this layer supports consumer
energy management applications, including distributed
PV regulation, consumer electric vehicle (EV) charge and
discharge management, consumer home energy manage-
ment, and consumer demand response.
• Cloud Layer: The cloud layer contains high-performance
cloud server with powerful storage and computing capa-
bilities. Through cloud–edge collaboration, cloud servers
process data migrated from edge servers. FDQN archi-
tecture is adopted to train the global model via federated
aggregation. In addition, two GANs are deployed to
generate channel state samples for IoT devices and queue
backlog distribution samples for edge servers, guiding
integrated optimization of transmission and computation.
• Edge Layer : Multiple edge servers are deployed to pro-
cess data for IoT devices within their coverage areas.
An edge server with heavy queue backlog can migrate
its tasks to lightly loaded edge servers or the cloud,
improving load balancing and reducing queuing delay.
Each edge server independently trains its integrated opti-
mization model based on the global model distributed by
the cloud, enabling joint optimization of task migration
and edge computing resource allocation.
• Device Layer : The device layer includes numerous IoT
devices deployed on various power grid facilities, such
as distributed PVs, electric vehicles, charging piles, con-
sumer loads, and energy storage batteries. These devices
collect real-time operating data and key state parameters.
IoT devices compress the collected data and offload them
to edge servers for processing.
Edge servers are constrained by limited resources and wire-
less channel fluctuations. Cloud–edge data migration experi-
ences high variability and uncertainty due to routing, conges-
tion, and long-distance communication, which have become
a critical bottleneck. Therefore, cloud–edge collaboration has
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 4
become essential. By processing delay-sensitive tasks at edge
and migrating overloaded tasks to the cloud, a balance between
computing efficiency and response delay is achieved.
A slotted model with slot length τ is considered, and the
slot set is defined as T = {1, . . . , t, . . . , T}. For transmission,
IoT devices optimize the compression ratio for task offloading.
For computing, edge servers optimize task migration decisions
and computing resource allocation. The goal is to minimize the
end-to-end cloud–edge collaborative processing delay, subject
to transmission reliability and resource allocation constraints.
To provide a quick reference, the principal notations used in
this paper are summarized in Table I.
A. Device-to-Edge Task Offloading Model
The cloud–edge system includes J edge servers and one
central cloud server, where the set is defined as J =
{1, . . . , j, . . . , J+ 1}. For j = 1, . . . , J, the index j denotes
edge server, and j = J + 1 denotes cloud server. Each edge
server j ∈ J provides services for Kj IoT devices, where dj,k
represents the k-th device associated with edge server j.
Each device dj,k stores the data to be offloaded in a local
queue. The backlog Qk(t) of dj,k at slot t is updated as
Qk(t + 1) = Qk(t) + Ak(t) −
U tx
k,j(t)
yk(t) , (1)
where Ak(t) denotes the amount of newly collected data.
U tx
k,j(t) denotes the amount of compressed data offloaded to
edge server j. yk(t) ∈ (0, 1] denotes the task offloading
compression ratio.
To reduce transmission overhead, devices apply data com-
pression. The offloaded data U tx
k,j(t) depends on both the
channel capacity and the compressed backlog, given by
U tx
k,j(t) = min (τ Rk,j(t), yk(t)Qk(t)) , (2)
where the transmission rate Rk,j(t) from device dj,k to edge
server j is given by
Rk,j(t) = Bk,j log2

1 + Pk,j(t)hk,j(t)
Ik,j(t) + N0

. (3)
Here, Bk,j is the bandwidth, Pk,j(t) is the transmission power,
hk,j(t) is the channel gain, Ik,j(t) is the interference power,
and N0 is the noise power.
The successful reception probability of compressed data
depends on yk(t). Compression reduces transmission amount,
but excessive compression also lowers decompression success.
Following [26], the success probability is modeled as
Wk,j(t) = β1eβ2yk(t) + β3eβ4yk(t), (4)
where β1, β2, β3, and β4 are model parameters learned by the
Levenberg–Marquardt method.
Thus, the amount of successfully received and decom-
pressed data at edge server j in slot t is given by
U rx
k,j(t) =



U tx
k,j (t)
yk(t) , with probability Wk,j(t);
0, with probability 1 − Wk,j(t).
(5)
Correspondingly, the lost data volume is given by
Lk,j(t) =
U tx
k,j(t)
yk(t)
 
1 − Wk,j(t)

. (6)
B. Cloud–Edge Collaborative Task Migration Model
The task migration variable is defined as xk,j,j ′(t) ∈ {0, 1}.
When xk,j,j ′(t) = 1 and j′ = j, the task is processed locally at
edge server j. When xk,j,j ′(t) = 1 and j′ ̸= j with j′ ̸= J +1,
the task is migrated from edge server j to another edge server
j′. When xk,j,j ′(t) = 1 and j′ = J + 1, the task is migrated
from the edge server to the cloud.
Each edge server j maintains a separate computation queue
Qk,j(t) for each device dj,k. The backlog evolves as
Qk,j(t + 1) =Qk,j(t) + U rx
k,j(t) +
X
j′∈J
U rx
k,j ′(t) · xk,j ′,j(t)
− Yk,j(t) · xk,j,j(t) − U rx
k,j(t) · xk,j,J +1(t)
−
X
j′∈J ,j̸=j′
U rx
k,j(t) · xk,j,j ′(t),
(7)
where the third term is the incoming data migrated from other
edge servers, the fourth term is the processed task volume,
and the last two terms are the tasks migrated to other edge
servers or to the cloud.
The processed task amount Yk,j(t) is defined as
Yk,j(t) = min

Qk,j(t), τ fk,j(t)
λk

, (8)
where fk,j(t) is the CPU frequency allocated for dj,k, and λk
is the task computation intensity of dj,k.
C. Delay Model
1) Device-to-Edge Offloading Queuing Delay: The queuing
delay of device dj,k is denoted by τ D
k (t), which includes both
local waiting and transmission delay. According to Little’s
Law, it is expressed as
τ D
k (t) = Qk(t)
˜Ak(t)
, (9)
where ˜Ak(t) is the average data arrival rate, given by
˜Ak(t) = 1
t
t−1X
i=0
Ak(i). (10)
2) Edge Processing Delay: Similarly, the queuing delay for
processing the tasks device dj,k at edge server j is denoted
by τ E
k,j(t). It includes both edge-to-edge migration delay and
computing delay, expressed as
τ E
k,j(t) = Qk,j(t)
˜Ak,j(t)
, (11)
where the average arrival rate at edge server j is
˜Ak,j(t) = 1
t
t−1X
i=0

U rx
k,j(i) +
X
j′∈J
U rx
k,j ′(i)xk,j ′,j(i)

 . (12)
The first term denotes the received tasks from dj,k, and
the second term denotes the tasks migrated from other edge
servers.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 5
3) Cloud Processing Delay: Unlike edge servers, the cloud
has abundant computing resources [27]. Therefore, it is as-
sumed that no backlog exists at the cloud. The delay only
includes the migration delay τ ec
k,j(t) and the computing delay
τ c
k,j(t). τ ec
k,j(t) is expressed as
τ ec
k,j(t) =
U rx
k,j(t)xk,j,j ′(t)
Rj,J+1(t) , j ′ = J + 1, (13)
where Rj,J+1(t) is the transmission rate from edge server j
to the cloud, and τ c
k,j(t) is given by
τ c
k,j(t) =
U rx
k,j(t)xk,j,j ′(t)
f c
k,j(t) , j ′ = J + 1, (14)
where f c
k,j(t) is the CPU frequency allocated for dj,k by the
cloud.
4) End-to-End Cloud–Edge Collaborative Processing De-
lay: The total end-to-end processing delay for device dj,k,
denoted by τ tot
k (t), consists of several components. These
components are the offloading queuing delay τ D
k (t) at the
device, the processing queuing delay τ E
k,j(t) at the local edge
server j, the processing queuing delay τ E
k,j ′(t) if migrated to
another edge server j′, and the sum of transmission delay
τ ec
k,j(t) and computing delay τ c
k,j(t) if migrated to the cloud.
The total delay is expressed as
τ tot
k (t) =τ D
k (t) + τ E
k,j(t) +
X
j′∈J ,j̸=j′
τ E
k,j ′(t)
+ xk,j,J +1(t)
 
τ ec
k,j(t) + τ c
k,j(t)

.
(15)
III. P ROBLEM FORMULATION AND TRANSFORMATION
This paper aims to address the low-latency task data pro-
cessing problem for consumer energy management applica-
tions. The goal is to minimize the long-term average end-to-
end cloud–edge collaborative processing delay through inte-
grated transmission and computation. Specifically, for trans-
mission, devices optimize task offloading compression ratio
decisions. For computing, edge servers jointly optimize task
migration and edge computing resource allocation based on
the global model distributed by the cloud. The problem is
formulated as
P1: min
y,x,f
1
T
X
t∈T
X
j∈J
X
k∈Kj
τ tot
k (t),
s.t. C1:
X
j∈J
xk,j,j ′(t) = 1, ∀k ∈ K, ∀t ∈ T,
C2:
X
k∈Kj
fk,j(t) ≤ f max
j (t), ∀j ∈ J , ∀t ∈ T,
C3: lim
T →∞
1
T
X
t∈T
Lk,j(t) ≤ Lmax
k,j , ∀k ∈ K, ∀j ∈ J .
(16)
Here, y = {yk(t)} denotes the set of task offloading
compression ratio strategy, x = {xk,j,j ′(t)} denotes the set
of task migration decisions, and f = {fj(t)} denotes the
set of computing resource allocation policies. C1 ensures
that each task is processed by one edge server or the cloud
server. C2 represents the edge server’s available computation
resource constraint, where f max
j (t) is the maximum available
computation resource for edge server j. C3 represents the
long-term transmission reliability constraint, where Lmax
k,j is
the pre-set threshold for the average packet loss over time.
Specifically, this long-term constraint ensures the statistical
completeness of data, providing critical support for real-
time monitoring and optimal control in consumer-side energy
management. Furthermore, this statistical guarantee acts as a
soft constraint that strategically tolerates short-term reliability
violations, thereby significantly improving resource utilization
efficiency.
The optimization problem P1 is a stochastic optimization
problem and cannot be solved directly. Specifically, due to the
lack of future information such as data arrival rates, channel
gains, and noise, the strategy that minimizes the objective
function at each time slot may not guarantee long-term con-
straints. In this paper, we adopt a Lyapunov optimization
framework [28] to transform P1 into a series of deterministic
optimization problems for each time slot. Specifically, a virtual
queue Zk,j(t) is introduced to handle C3, and its evolution is
defined as
Zk,j(t + 1) = max{Zk,j(t) + Lk,j(t) − Lmax
k , 0}. (17)
According to [28], if the constructed virtual queue Zk,j(t) is
proven to be mean-rate stable, the original long-term reliability
constraint C3 will be satisfied. Thus, P1 can be equivalently
transformed into
P2: min
y,x,f
1
T
X
t∈T
X
j∈J
X
k∈Kj
τ tot
k (t),
s.t. C1 − C2,
C4: (17) is mean-rate stable .
(18)
This formulation controls both the data queue backlog and
the long-term constraint violations represented by the virtual
deficit. Let Θ(t) = [ Qk(t), Qk,j(t), Zk,j(t)] represent the
system state, and define the Lyapunov function as
L(Θ(t)) =1
2
 X
k∈Kj
(Qk(t))2 +
X
k∈Kj
X
j∈J
(Qk,j(t))2
+
X
k∈Kj
X
j∈J
(Zk,j(t))2
!
.
(19)
The single-slot Lyapunov drift, ∆(Θ(t)) is expressed as
∆(Θ(t)) = E[L(Θ(t + 1)) − L(Θ(t)) | Θ(t)]. (20)
∆(Θ(t)) reflects the instantaneous change in the total net-
work backlog. A negative drift indicates that the backlog is
expected to decrease, stabilizing the network, while a positive
drift suggests that the backlog is worsening. To optimize
the objective function while maintaining queue stability con-
straints, drift-plus-penalty is employed to minimize delay,
expressed as
∆V L(Θ(t)) = ∆L(Θ(t)) − V E[Ψ(t) | Θ(t)], (21)
where V > 0 is a control parameter that trades off queue
stability and delay performance. Ψ(t) represents the total end-
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 6
to-end cloud–edge collaborative processing delay across all
devices in time slot t, expressed as
Ψ(t) =
X
j∈J
X
k∈Kj
τ tot
k (t). (22)
For all possible Θ(t) and V > 0, the upper bound of the
drift penalty is given by
∆V L(Θ(t)) ≤ B + E
" X
k∈Kj
(Ak(t) − U tx
k,j(t))
+
X
j∈J
X
k∈Kj
Qk,j(t)(U rx
k,j(t)
+
X
j′∈J
U rx
k,j ′(t)xk,j ′,j(t) − Yk,j(t)xk,j,j(t)
−
X
j′∈J ,j̸=j′
U rx
k,j(t)xk,j,j ′(t)
− U rx
k,j(t)xk,j,J +1(t))
+
X
j∈J
X
k∈Kj
Zk,j(t)
 
Lk,j(t) − Lmax
k,j






Θ(t)
#
− V E[Ψ(t) | Θ(t)].
(23)
Here, B is a constant that does not affect the Lyapunov
optimization.
For ease of problem decomposition, the upper bound of
expression (23) is slightly relaxed and simplified as
∆V L(Θ(t)) ≤ B′ + E
"
−
X
k∈Kj
Qk(t)U tx
k,j(t)
+
X
j∈J
X
k∈Kj
Qk,j(t)(U rx
k,j(t)
+
X
j′∈J
U rx
k,j ′(t)xk,j ′,j(t) − Yk,j(t)xk,j,j(t)
−
X
j′∈J ,j̸=j′
U rx
k,j(t)xk,j,j ′(t)
− U rx
k,j(t)xk,j,J +1(t))
+
X
j∈J
X
k∈Kj
Zk,j(t)Lk,j(t)





Θ(t)
#
− V E[Ψ(t) | Θ(t)].
(24)
Problem P2 can be solved by minimizing the drift-plus-
penalty upper bound in each slot. To facilitate the solution, P2
is further decomposed into two subproblems: device-side task
offloading compression ratio optimization subproblem SP1
and edge-side task migration and edge computing resource
allocation joint optimization subproblem SP2.
1) Device-side Task Offloading Compression Ratio Opti-
mization: In SP1, device dk,j decides the task offloading
compression ratio to offload data to edge server j. SP1 is
formulated as
SP1: max
{yk(t)}
ΦD(t) =Qk(t)U tx
k,j(t) − Zk,j(t)Lk,j(t)
− V τ tot
k (t).
(25)
2) Edge-side Task Migration and Edge Computing Re-
source Allocation Joint Optimization: In SP2, edge servers
decide task migration and edge computing resource allocation.
SP2 is formulated as
SP2: max
{xk,j,j′ (t)},{fk,j (t)}
ΦE(t) =
X
k∈Kj
Qk,j(t)(Yk,j(t)xk,j,j(t)
+
X
j̸=j′
U rx
k,j(t)xk,j,j ′(t) + U rx
k,j(t)xk,j,J +1(t) − U rx
k,j(t)
−
X
j′∈J ,j̸=j′
U rx
k,j ′(t)xk,j,j ′(t)) − V τ tot
k (t).
(26)
IV. GAI-E NABLED TRANSMISSION AND COMPUTING
INTEGRATION ALGORITHM FOR CLOUD –E DGE
COLLABORATIVE IOT
In this section, we present the proposed GAI-enabled trans-
mission and computing integration algorithm for cloud–edge
collaborative IoT. The framework of the algorithm is illustrated
in Fig. 2. First, it employs GAI-assisted UCB algorithm to
solve SP1. Second, it employs GAI-enhanced FDQN algo-
rithm to solve SP2.
A. GAI-assisted UCB for Device-side Offloading Compression
Ratio Optimization
Traditional UCB lacks adaptability to external dynamics. In
scenarios with channel quality fluctuations, UCB relying only
on historical statistics fails to achieve optimal responsiveness.
To address this issue, we propose a GAI-assisted UCB algo-
rithm for optimizing device-side task offloading compression
ratio strategies. By integrating GAN-based channel state gen-
eration, the proposed algorithm enhances decision foresight.
The proposed GAN structure consists of a generator and a
discriminator. The generator generates channel states based
on historical channel gains and noise/interference informa-
tion. The discriminator distinguishes between real channel
states and the generator’s generated states. During training,
the generator optimizes to deceive the discriminator, while
the discriminator improves its recognition capability. Through
adversarial training, both networks are iteratively improved
until the generator outputs channel states close to the real one.
The GAN generator takes the historical channel state se-
quence ˜Hk,j as input and produces a predicted future channel
sequence Hk,j = {hk,j(1), hk,j(2), . . . , hk,j(T )}. The adver-
sarial training objective is defined as
min
G
max
D
V (G, D)=E[log D( ˜Hk,j)]+E[log(1−D(G( ˜Hk,j)))].
(27)
Here, G denotes the generator and D denotes the discrim-
inator. During training, D learns to distinguish real chan-
nel states from generated ones, while G is improved under
the feedback from D to approximate the true distribution.
This iterative optimization enables the model to capture both
statistical and temporal features of the channel, improving
generation accuracy. The operation processes are as follow.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 7
Fig. 2. The principle of GAI-enabled transmission and computing integration algorithm for cloud–edge collaborative IoT.
1) Initialization: The compression ratio is discretized into
A actions, denoted by yk = { 1
A , . . . , a
A , . . . ,1}, where a =
1, . . . , A. For device dk,j, the historical average reward of
action a up to slot t is ¯ΦD
k,a(t), and the number of times
that action a has been selected is nk,a(t). Both are initialized
as zero. The trained GAN generator produces Hk,j based on
historical channel gains, noise, and interference.
2) GAI-assisted Decision Making: At each slot t, device
dk,j estimates signal-to-interference-plus-noise ratio (SINR)
based on generated channel states as
SINRpred
k,j (t) = Pk,j(t)hk,j(t)
Ik,j(t) + N0
. (28)
It compares SINRpred
k,j (t) with a threshold SINR th to determine
the dynamic exploration weight ck(t) as
ck(t) =
(
chigh, if SINR pred
k,j (t) ≥ SINRth,
clow, if SINR pred
k,j (t) < SINRth, (29)
where chigh > c low ≥ 0 are exploration weight coefficients.
Each action is assigned a preference index as
Ik,a(t) = ¯ΦD
k,a(t) + ck(t)
q
ln t
nk,a(t) . (30)
The first term prioritizes actions with higher historical rewards.
The second term ensures exploration via the confidence inter-
val. The device selects the action a∗ with the largest index and
performs the action. Dynamic weight encourages aggressive
exploration under good channel conditions and conservative
reliance on exploiting under poor channels, thereby balancing
optimality and robustness.
3) Learning: At the end of slot t, device dk,j records the
total end-to-end processing delay τ tot
k (t), calculates the reward
ΦD(t), and updates the statistics as
nk,a∗(t + 1) = nk,a∗(t) + 1, (31)
¯ΦD
k,a∗(t + 1) =
nk,a∗(t)¯ΦD
k,a∗(t) + ΦD(t)
nk,a∗(t + 1) . (32)
B. GAI-enhanced FDQN for Cloud–Edge Collaborative Task
Migration and Edge Computing Resource Allocation Joint
Optimization
Subproblem SP2 is modeled as a Markov decision process
(MDP). The state space, action space, and reward function are
defined as follows.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 8
1) State Space: The state space is defined as Sj(t) =
{Qj(t), Qj′(t), Zj(t), Urx
j (t)}, which includes the backlog
vector of edge server j, i.e., Qj(t) = {Qk,j(t) | k ∈ K j},
the backlog vector of other edge servers Qj′(t) = {Qk,j ′(t) |
k ∈ K j′, j′ ∈ J , j′ ̸= j, j′ ̸= J + 1}, the virtual queue vector
Zj(t) = {Zk,j(t) | k ∈ K j}, and the received data vector
Urx
j (t) = {U rx
k,j(t) | k ∈ K j}.
2) Action Space: The action space consists of task mi-
gration and edge computing resource allocation variables.
The discretized resource allocation is defined as ˜fk,j(t) =
o
O f max
j (t), where O is the number of discrete levels and o
is the index. The action space is represented as Aj(t) =
{xk,j,j ′(t) ⊗ ˜fk,j(t) | k ∈ K j, j′ ∈ { 1, . . . , J + 1}, j′ ̸= j},
where ⊗ denotes the Cartesian product.
3) Reward Function: The reward function is defined as the
optimization objective of SP2, i.e., ΦE(t).
The proposed GAI-enhanced FDQN framework is illus-
trated in Fig. 2. It performs joint training through cloud–edge
federated aggregation, which improves convergence efficiency
and global generalization. A dual-mode adaptive mechanism
controls model uploading, balancing global performance im-
provement and communication overhead. The cloud deploys a
CGAN to address data scarcity in extreme cases for federated
learning. The conditional variable c describes macro network
conditions, with smaller values indicating worse scenarios.
CGAN generates extreme experiences online, which are used
to strengthen the aggregated global model before it is dis-
tributed to edge servers. Each edge server deploys a DQN
agent with a main network θmain
j (t) and a target network
θtarget
j (t) of the same structure. The main network estimates
Q-values for real-time decisions, while the target network
provides stable targets for training. Historical experiences
are replayed to reduce data correlation and improve learning
optimality. Within this integrated architecture, the local agent
observes its current state and selects an action, which includes
task migration and edge computing resource allocation, while
the cloud aggregates uploaded models by federated averaging
with performance weights. The execution process is shown in
Algorithm 1. The details are as follows:
1) Edge Server Initialization: Each edge server initializes
all real physical queues and virtual queues with backlog and
indicator variables set to zero.
2) Model Downloading: At the beginning of each time slot,
if (t − 1) mod D = 0 or a performance alert is triggered in
the previous slot, the edge server downloads the global model
and sets θmain
j (t) = θmain
G,en(t) and θtarget
j (t) = θtarget
G,en (t).
3) Action Selection and Execution at Edge Server: Each
edge server observes its current state Sj(t). Then, based on
the main network θmain
j (t), it computes the Q-value for each
action Q(Sj(t), Aj(t), θmain
j (t)). Using the ϵ-greedy strategy,
it selects an action Aj(t), which includes task migration and
edge computing resource allocation as
Aj(t) =
(
random selection, with probability ϵ,
A∗
j(t), with probability 1 − ϵ, (33)
where A∗
j(t) denotes the action corresponding to the maxi-
mum Q-value. The selected action is then executed.
4) Learning at Edge Server: Each edge server updates
queues Qj(t + 1), Qj′(t + 1), and Zj(t + 1) based on (7) and
(18). It computes ΦE(t) according to (27), transitions to the
next state Sj(t + 1), and stores the experience tuple V(t) =
(Sj(t), Aj(t), ΦE(t), Sj(t + 1)) in the replay buffer Dj(t).
During training, I samples are drawn from the buffer to form
a mini-batch ˜Rj(t) with I < E , where E is the buffer size.
The DQN loss is given by
L(t) =1
I
X
v∈ ˜Rj (t)
h
ΦE(t)
+ ρQ(Sv
j (t + 1), Av
j (t + 1), θtarget
j (t))
− Q(Sv
j (t), Av
j (t), θmain
j (t))
i2
,
(34)
where ρ is the discount factor. The main network is updated
by gradient descent as
θmain
j (t + 1) = θmain
j (t) − ψ∇θmain(t)L(t), (35)
where ψ is the learning rate. The target network is updated
every T0 slots as θtarget
j (t + 1) = θmain
j (t + 1); otherwise, it
remains unchanged.
5) Dual-mode Adaptive Edge Server Model Uploading:
Edge servers upload their DQN parameters to the cloud fol-
lowing a dual-mode adaptive triggering mechanism. All edge
servers upload every D slots, or whenever one packet-loss
queue deficit exceeds a threshold and triggers a performance
alert.
6) Federated Model Aggregation at the Cloud: At the
end of each slot, the cloud computes the performance weight
ρj(t) for each edge server as
ρj(t) = numE
max(t) −PK
k=1 I [Lk,j(t) > L max
k ]
numEmax(t) − numE
min(t) , (36)
where numE
max(t) and numE
min(t) denote the maximum and
minimum numbers of violated packet-loss constraints among
all edge servers in slot t. The cloud aggregates uploaded
models by federated averaging with performance weights. The
global main and target networks are updated as
θmain
G (t + 1) = αθmain
G,en(t) + (1 − α)
P
j∈J ρj(t)θmain
j (t + 1)P
j∈J ρj(t) ,
(37)
θtarget
G (t + 1) = αθtarget
G,en (t) + (1 − α)
P
j∈J ρj(t)θtarget
j (t + 1)P
j∈J ρj(t) .
(38)
7) GAI Based Extreme Scenario Data Generation: The
cloud deploys a CGAN similar to the GAN introduced ear-
lier, but with conditional variables describing the generation
state. The generator learns to model queue distributions under
different conditions c, while the discriminator learns to distin-
guish real from generated queue distributions under the same
condition. The training objective is defined as
min
G
max
D
V (G, D) =E[log D(V(t)|c)]
+ E
h
log(1 − D(G(V(t)|c)|c))
i
.
(39)
The trained CGAN generates queue distributions for extreme
scenarios. Each generated distribution is assembled into an
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 9
Algorithm 1 GAI-enhanced FDQN for Cloud–Edge Col-
laborative Task Migration and Edge Computing Resource
Allocation Joint Optimization
1: Input: Sj(t), ϵ.
2: Output: {xk,j,j ′}, {fk,j(t)}.
3: Phase 1: Edge server initialization
4: Set Qk,j(0) = 0, Zk,j(0) = 0, xk,j,j ′ = 0.
5: for t = 1, · · · , T do
6: Phase 2: Model downloading
7: if (t − 1) mod D = 0 or a performance alert is
triggered in the previous slot then
8: Set θmain
j (t) = θmain
G,en(t), θtarget
j (t) = θtarget
G,en (t).
9: end if
10: Phase 3: Action selection and execution at edge
server
11: Observe the current state Sj(t).
12: Randomly generate a constant β ∈ [0, 1].
13: if β ≤ ϵ then
14: Choose an action Aj(t) randomly.
15: else
16: Choose A∗
j(t).
17: end if
18: Phase 4: Learning at edge server
19: Update all queue backlogs as (7), (17).
20: Calculate ΦE(t) based on (26).
21: Transfer to the next state Sj(t + 1).
22: Update Dj(t) with V(t).
23: Choose ˜R(t) in V(t).
24: Calculate L(t) as (34) and update θmain
j (t) as (35).
25: if t mod T0 = 0 then
26: Update the target network as θtarget
j (t) = θmain
j (t).
27: end if
28: Phase 5: Dual-mode adaptive edge server model
uploading
29: if (t mod D = 0) or receive performance alert then
30: Upload θtarget
j (t) and θmain
j (t) to the cloud server.
31: end if
32: Phase 6: Federated model aggregation at the cloud
33: Calculate ρj(t) as (36).
34: Update θmain
G (t) and θtarget
G (t) by federated averaging as
(37), (38).
35: Phase 7: CGAN based extreme scenario data gen-
eration
36: CGAN generator outputs an extreme scenario mini-
batch Vsynth(t).
37: Phase 8: GAI-enhanced global model training
38: Calculate Laug(t) as (40).
39: Update θmain
G,en(t + 1) and θtarget
G,en (t + 1) as (41), (42).
40: t = t + 1.
41: end for
experience, and multiple experiences are collected to form an
extreme scenario mini-batch Vsynth(t) for enhanced training.
8) GAI-enhanced Global Model Training: Using the mini-
batch Vsynth(t), the cloud performs augmented training of the
global model. The augmented loss function is defined as
Laug(t) = 1
|Vsynth(t)|
X
v∈Vsynth(t)

ΦE(t)
+ ρQ(Sv(t + 1), Av(t + 1), θtarget
G (t + 1))
− Q(Sv(t), Av(t), θmain
G (t + 1))
2
.
(40)
The global model is updated by gradient descent as
θmain
G,en(t + 1) = θmain
G (t + 1) − µ∇θG
main(t+1)Laug(t), (41)
θtarget
G,en (t + 1) = θtarget
G (t + 1) − µ∇θG
target(t+1)Laug(t), (42)
where µ is the learning rate at the cloud.
V. S IMULATION
We evaluate the efficacy of the proposed algorithm in
MATLAB. The simulated scenario encompasses a 2 km ×
3 km area subdivided into six sub-regions, each hosting one
edge server for 50 IoT devices. Two services are considered:
(i) distribution automation, which imposes stringent delay
constraints but tolerates moderate packet loss. (ii) electricity
information collection, which prioritizes ultra-reliable delivery
with relaxed delay demands. Devices access to their respective
edge servers via 5G links configured with 0.2 MHz bandwidth
and 50 mW transmit power. The interference is characterized
by an alpha-stable distribution [29]. Detailed simulation pa-
rameters are provided in Table II [30]–[32]. These parameter
settings are rigorously configured according to established
5G standards and commercial edge hardware specifications to
realistically reflect the physical constraints of consumer energy
management networks, thereby guaranteeing the validity and
reproducibility of the simulated results.
We utilize two comparison algorithms. Baseline 1 is a
UCB and distributed DQN enabled cloud-edge collaborative
algorithm. Each device applies UCB for compression ratio
selection, while each edge server uses DQN for migration
and resource allocation [33]. Baseline 2 is a federated DQN
based cloud–edge collaborative optimization algorithm. Each
edge server runs a DQN agent for joint optimization of
compression, migration, and resource allocation, with local
models periodically aggregated in the cloud [34]. Both base-
lines reformulate the long-term reliability constraint via a
penalty term and minimize the weighted sum of end-to-end
delay and reliability penalty. They are explicitly selected to
highlight the deficiencies relative to the proposed algorithm.
Baseline 1 lacks the integrated coordination of transmission
and computing. Baseline 2 lacks GAI enhancement, rendering
it vulnerable to extreme scenarios with long-tail distributions.
Figure 3 shows the end-to-end delay and average packet
loss among different algorithms. Compared with Baseline 1,
the proposed algorithm reduces end-to-end delay by 29.65%,
while the average packet loss also decreases by 0.68%.
Baseline 2 achieves better delay performance at the cost of
failing to satisfy the packet loss constraint. In contrast, the
proposed algorithm can stably achieve a balanced trade-off
between end-to-end delay and packet loss. This improvement
comes from the GAI-assisted UCB, which generates channel
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 10
TABLE II
SIMULATION PARAMETERS
Parameter Value Parameter Value
T 200 τ 100 ms
K 300 J 6
Bk,j 0.2 MHz Pk,j (t) 500 mW
λk 1000 cycles/bit hk,j (t) [-80,-60] dB
N0 -174 dBm γ 0.99
ψ 0.001 f max
j 20 GHz
Fig. 3. End-to-end delay and average packet loss among different algorithms.
states through GAN to enhance exploration efficiency, thereby
improving convergence speed and optimality. In addition, the
GAI-enhanced FDQN adopts a dual-mode model uploading
strategy, while the cloud aggregates models based on packet
loss performance, suppressing abnormal updates and amplify-
ing high-quality models. Moreover, CGAN generates extreme
scenario data to enhance global model robustness.
Figure 4 shows the end-to-end delay and compression ratio
selection in channel degradation scenarios. When the channel
condition is normal, the proposed algorithm reduces the end-
to-end delay of Service 2 by 54.91% and that of Service 1 by
17.47% compared with UCB. This is because the proposed
algorithm can flexibly select compression ratios according to
service requirements: for delay-sensitive Service 1, it prefers
lower compression ratios to reduce delay, while for packet-
loss-sensitive Service 2, it selects higher compression ratios
to reduce packet loss. In contrast, traditional UCB fails to
differentiate between services. After the channel deteriorates
at the 100-th slot, the proposed algorithm quickly adapts by
adjusting exploration weights with GAI assistance, achieving
a rapid decrease in delay to a new optimum while maintaining
service differentiation. Traditional UCB, however, relies solely
on historical experience, leading to a surge in delay and severe
performance degradation.
Figure 5 shows average end-to-end delay with respect to the
number of devices. As the number of devices per edge server
increases, the network experiences heavier load, increasing
end-to-end delays. When the number of devices reaches 360,
the proposed algorithm achieves 45.56% lower delay than
baseline1, respectively. GAI-enhanced FDQN dynamically ad-
justs task migration to minimize end-to-end delay. Meanwhile,
(a) Proposed algorithm.
(b) Traditional UCB.
(c) Compression ratio selection.
Fig. 4. Convergence performance and compression ratio selection of different
UCB algorithms in channel degradation scenarios.
GAI-assisted UCB effectively identifies channel congestion
and adaptively adjusts compression ratios, ensuring low delay
under heavy-load conditions.
Figure 6 illustrates the training process of the proposed
algorithm and Baseline 2 under federated DQN. The pro-
posed algorithm achieves stable convergence and reduces
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 11
Fig. 5. Average end-to-end delay versus number of devices.
Fig. 6. Training process of different federated DQN algorithms.
the normalized loss function by 49.33% at the 200-th slot
compared with Baseline 2. This is attributed to federated
averaging, allocating model weights based on performance to
suppress poor updates and enhance global stability. Moreover,
by prioritizing high-quality experiences during early training,
the algorithm reduces ineffective exploration and further ac-
celerates convergence.
Figure 7 shows the evolution of virtual queue backlogs
under traffic surge. At the 100-th slot, the backlog of edge
server 2 suddenly doubles. After the anomaly, the proposed
algorithm quickly stabilizes server backlogs and maintains bal-
anced load. Compared with Baseline 1, the convergence time
is reduced by 11.48%, and the total virtual queue backlog is
reduced by 20.88%, respectively. This is because the proposed
GAI-enhanced FDQN framework leverages GAN-generated
extreme scenarios to improve robustness, while the packet
loss performance-aware federated aggregation mechanism ef-
fectively suppresses the negative impact of edge anomalies on
the global system.
VI. C ONCLUSION
This article proposed a GAI-enabled transmission and com-
puting integration algorithm for cloud–edge collaborative IoT
(a) Proposed algorithm.
(b) Baseline 1.
(c) Baseline 2.
Fig. 7. Virtual queue backlogs under traffic surge scenarios.
in consumer energy management. The algorithm employed
GAI-assisted UCB to optimize compression, where GAI gen-
erated channel states to dynamically adjust the exploration
coefficient. For computing, it employed GAI-enhanced FDQN
with cloud-side CGAN to jointly optimize task migration,
resource allocation, and federated global model training. This
joint design ensures efficient heterogeneous resource utiliza-
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 12
tion, addressing both latency reduction and reliability assur-
ance. Simulation results show that the proposed algorithm
achieves significant performance gains, reducing average delay
by 7.85% and 4.06%, decreasing average packet loss by
43.64% and 14.55%, and improving average convergence
speed by 39.72% and 26.18% compared with two base-
lines. Beyond consumer energy management, the proposed
framework holds significant potential for broader consumer
electronics domains, such as adapting to rapid channel fluctu-
ations in connected vehicles and managing massive IoT traffic
bursts in smart home ecosystems. Future work will investigate
large language models for adaptive optimization and quantum
communication for secure low-latency cloud–edge IoT.

## § References

[1] K. Singh et al., “Joint active and passive beamforming design for RIS-
aided IBFD IoT communications: QoS and power efficiency consider-
ations,” IEEE Trans. Consum. Electron. , vol. 69, no. 2, pp. 170–182,
May 2023.
[2] H. Liao et al. , “Ultra-low AoI digital twin-assisted resource allocation
for multi-mode power IoT in distribution grid energy management,”
IEEE J. Sel. Areas Commun., vol. 41, no. 10, pp. 3122–3132, Oct. 2023.
[3] L. Chettri and R. Bera, “A comprehensive survey on internet of things
(IoT) toward 5G wireless systems,” IEEE Internet Things J. , vol. 7,
no. 1, pp. 16–32, Jan. 2020.
[4] M. Chen et al. , “Secure MLLM semantic communication enabled air-
space-ground-maritime networks,” IEEE Commun. Mag., vol. 63, no. 7,
pp. 26–33, Jul. 2025.
[5] R. Ma et al., “cFedDT: cross-domain federated learning in digital twins
for metaverse consumer electronic products,” IEEE Trans. Consum.
Electron., vol. 70, no. 1, pp. 3167–3182, Feb. 2024.
[6] S. Zhang et al., “Blockchain and federated deep reinforcement learning
based secure cloud-edge-end collaboration in power IoT,” IEEE Wireless
Commun., vol. 29, no. 2, pp. 84–91, Apr. 2022.
[7] Z. Hu, C. Fang, Z. Wang, S. Tseng, and M. Dong, “Many-objective
optimization-based content popularity prediction for cache-assisted
cloud–edge–end collaborative IoT networks,” IEEE Internet Things J. ,
vol. 11, no. 1, pp. 1190–1200, Jan. 2024.
[8] W. Yu, A. Najafi, Y . Huang, and A. Garcia-Ortiz, “Combination of task
allocation and approximate computing for fog-architecture-based IoT,”
IEEE Internet Things J. , vol. 8, no. 9, pp. 7638–7648, May 2021.
[9] R. Yao et al. , “Joint task offloading and power control optimization
for IoT-enabled smart cities: an energy-efficient coordination via deep
reinforcement learning,” IEEE Trans. Consum. Electron., vol. 71, no. 2,
pp. 2517–2529, May 2025.
[10] Y . Rong, Y . Mao, H. Cui, X. He, and M. Chen, “Edge computing enabled
large-scale traffic flow prediction with GPT in intelligent autonomous
transport system for 6G network,” IEEE Trans. Intell. Transp. Syst. ,
vol. 26, no. 10, pp. 17 321–17 338, Oct. 2025.
[11] W. Yu, Y . Huang, and A. Garcia-Ortiz, “Distributed optimal on-line
task allocation algorithm for wireless sensor networks,” IEEE Sens. J. ,
vol. 18, no. 1, pp. 446–458, Jan. 2018.
[12] Y . Sun et al. , “Adaptive learning-based task offloading for vehicular
edge computing systems,” IEEE Trans. Veh. Technol., vol. 68, no. 4, pp.
3061–3074, Apr. 2019.
[13] Y . Sun et al. , “Learning-based task offloading for vehicular cloud
computing systems,” in Proc. 2018 IEEE Int. Conf. Commun. (ICC),
Kansas City, USA, May 2018, pp. 1–7.
[14] F. Qiao et al. , “Trustworthy edge storage orchestration in intelligent
transportation systems using reinforcement learning,” IEEE Trans. Intell.
Transp. Syst., vol. 22, no. 7, pp. 4443–4456, Jul. 2021.
[15] Z. Wang et al., “Edge-end cooperative network resource allocation with
time synchronization awareness for federated learning-based distributed
energy regulation,” IEEE Trans. Smart Grid , vol. 16, no. 3, pp. 2671–
2682, May 2025.
[16] J. Hu et al. , “Deep reinforcement learning for task offloading in edge
computing assisted power IoT,” IEEE Access, vol. 9, no. 9, pp. 93 892–
93 901, Sep. 2021.
[17] W. Cheng, X. Liu, X. Wang, and G. Nie, “Task offloading and resource
allocation for industrial internet of things: a double-dueling deep Q-
network approach,” IEEE Access, vol. 10, no. 10, pp. 103 111–103 120,
Oct. 2022.
[18] H. Zhou, K. Jiang, X. Liu, X. Li, and V . C. M. Leung, “Deep
reinforcement learning for energy-efficient computation offloading in
mobile-edge computing,” IEEE Internet Things J. , vol. 9, no. 2, pp.
1517–1530, Jan. 2022.
[19] M. Chen et al. , “Embodied artificial intelligence-enabled internet of
vehicles: challenges and solutions,” IEEE Veh. Technol. Mag. , vol. 20,
no. 2, pp. 63–70, Jun. 2025.
[20] Z. Kaleem et al., “Emerging trends in UA Vs: from placement, semantic
communications to generative AI for mission-critical networks,” IEEE
Trans. Consum. Electron., vol. 71, no. 3, pp. 7412–7438, Aug. 2025.
[21] M. Rahimi et al. , “GAI-driven semantic CSI quantization for aerial
BD-RIS-assisted NOMA in future consumer networks,” IEEE Trans.
Consum. Electron., vol. pp, no. 99, pp. 1–14, Feb. 2026.
[22] J. Zhao, F. Li, H. Sun, Q. Zhang, and H. Shuai, “Self-attention generative
adversarial network enhanced learning method for resilient defense of
networked microgrids against sequential events,” IEEE Trans. Power
Syst., vol. 38, no. 5, pp. 4369–4380, Sep. 2023.
[23] R. Zhu, H. Liu, M. Kang, W. Yu, and J. Zhao, “Adversarial scenario
generation integrated distributionally robust deep reinforcement learning
for survival of critical loads,” IEEE Trans. Smart Grid , vol. 16, no. 5,
pp. 3533–3547, Sep. 2025.
[24] Q. Guo, F. Tang, and N. Kato, “Routing for space-air-ground integrated
network with GAN-powered deep reinforcement learning,” IEEE Trans.
Cogn. Commun. Netw., vol. 11, no. 2, pp. 914–922, Apr. 2025.
[25] F. Hu, X. Fu, and H. Huang, “Safe reinforcement learning for event-
triggered control of automated vehicles with uncertainty,” IEEE Trans.
Intell. Transp. Syst. , vol. 26, no. 9, pp. 14 039–14 052, Sep. 2025.
[26] H. Liao et al., “Electric semantic compression-based 6G wireless sens-
ing and communication integrated resource allocation,” IEEE Internet
Things J., vol. 11, no. 24, pp. 39 333–39 345, Dec. 2024.
[27] Z. Wang, M. Goudarzi, and R. Buyya, “TF-DDRL: a transformer-
enhanced distributed DRL technique for scheduling IoT applications in
edge and cloud computing environments,” IEEE Trans. Serv. Comput. ,
vol. 18, no. 2, pp. 1039–1053, Apr. 2025.
[28] T. Shuminoski and T. Janevski, “Lyapunov optimization framework for
5G mobile nodes with multi-homing,” IEEE Commun. Lett. , vol. 20,
no. 5, pp. 1026–1029, May 2016.
[29] R. Li, G. Li, P. Zhang, and F. Gong, “Bit error rate performance of DFT-
S-OFDM systems under alpha-stable noise,” IEEE Communications
Letters, vol. 29, no. 3, pp. 645–649, Mar. 2025.
[30] H. Yuan and M. Zhou, “Profit-maximized collaborative computation of-
floading and resource allocation in distributed cloud and edge computing
systems,” IEEE Trans. Autom. Sci. Eng. , vol. 18, no. 3, pp. 1277–1287,
Jul. 2021.
[31] M. Ding et al., “Ultra-dense networks: a holistic analysis of multi-piece
path loss, antenna heights, finite users and BS idle modes,” IEEE Trans.
Mob. Comput., vol. 20, no. 4, pp. 1702–1713, Apr. 2021.
[32] A. T. Z. Kasgari, W. Saad, M. Mozaffari, and H. V . Poor, “Experi-
enced deep reinforcement learning with generative adversarial networks
(GANs) for model-free ultra reliable low latency communication,” IEEE
Trans. Commun., vol. 69, no. 2, pp. 884–899, Feb. 2021.
[33] S. Chu et al. , “Resource efficient asynchronous federated learning for
digital twin empowered IoT network,” IEEE Trans. Green Commun.
Netw., vol. pp, no. 99, pp. 1–18, May 2025.
[34] S. Yu, X. Chen, Z. Zhou, X. Gong, and D. Wu, “When deep rein-
forcement learning meets federated learning: intelligent multitimescale
resource management for multiaccess edge computing in 5G ultradense
network,” IEEE Internet Things J. , vol. 8, no. 4, pp. 2238–2251, Feb.
2021.
Haoyu Ci is currently pursuing the Ph.D. degree
with the School of Electrical and Electronic En-
gineering, North China Electric Power University,
Beijing, China. His research interests include ar-
tificial intelligence applications in power systems,
cloud-edge collaborative computing, and smart grid
communication.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON CONSUMER ELECTRONICS 13
Yuxiang Leng is currently pursuing the B.E. degree
with the School of Electrical and Electronic Engi-
neering, North China Electric Power University. His
research interests include power IoT, cloud-edge-end
collaboration, and resource allocation.
Ziming Li is currently pursuing the M.E. degree
with the School of Electrical and Electronic En-
gineering, North China Electric Power University,
Beijing, China. His research interests include electric
vehicle demand response and smart grid communi-
cation.
Yiming Chen is currently pursuing the M.E. de-
gree with the School of Electrical and Electronic
Engineering, North China Electric Power University,
Beijing, China. His research interests include power
IoT and smart grid communication.
Haijun Liao (Member, IEEE) received the B.Eng.
degree in smart grid information engineering and the
Ph.D. degree in electrical engineering from North
China Electric Power University, Beijing, China, in
2019 and 2024, respectively. She is currently an
Assistant Professor with the School of Electrical and
Electronic Engineering, North China Electric Power
University. Her research interest includes power in-
ternet of things, cyber-physical systems, cloud-edge-
end collaboration, sensing-transmission-computing-
control integration. Dr. Liao was the recipient of the
IEEE IWCMC 2019 Best Paper Award, IEEE VTC-2020 Spring Best Student
Paper Award, IEEE CAMAD 2021 Best Paper Award, and IEEE IWCMC
2025 Best Paper Award.
Zhenyu Zhou (Senior Member, IEEE) received the
M.E. and Ph.D. degrees in international information
and communication studies from Waseda Univer-
sity, Tokyo, Japan, in 2008 and 2011, respectively.
From September 2012 to April 2019, he was an
Associate Professor with the School of Electrical
and Electronic Engineering, North China Electric
Power University, Beijing, China, where he has
been a Full Professor/PhD supervisor in information
and communication engineering as well as electrical
engineering since April 2019. His research interests
include energy informatics, cyber-physical systems, smart grid energy man-
agement, industrial internet of things, and sensing-transmission-computing-
control integration. He has undertaken a number of major projects for power
grid companies and made significant contributions to the engineering practice
of energy informatics applications in smart grids. He was the recipient of
the IET Premium Award in 2017, IEEE Globecom 2018 Best Paper Award,
and IEEE Communications Society Asia Pacific Board Outstanding Young
Researcher. He was an Associate Editor for IEEE Internet of Things Journal,
IET Quantum Communication, and Transactions on Emerging Telecommuni-
cations Technologies, and the Guest Editor of IEEE Communications Maga-
zine and IEEE Transactions on Industrial Informatics. He is an IET Fellow and
a Senior Member of the Chinese Society for Electrical Engineering, Chinese
Institute of Electronics, and the China Institute of Communications.
Wenqing Wu is currently pursuing the M.E. de-
gree with the School of Electrical and Electronic
Engineering, North China Electric Power University,
Beijing, China. Her research interests include cloud-
edge-end collaboration and smart grid communica-
tion.
Xiaoyan Wang (Senior Member, IEEE) received the
B.E. degree in electrical engineering from Beihang
University, Beijing, China, in 2004, and the M.E.
and Ph.D. degrees in computer science from the
University of Tsukuba, Tsukuba, Japan, in 2010 and
2013, respectively.
He is currently a Professor with the Graduate
School of Science and Engineering at Ibaraki Uni-
versity, Hitachi, Japan. From 2013 to 2016, he
worked as an Assistant Professor (by special ap-
pointment) at the National Institute of Informatics
(NII), Tokyo, Japan. His research interests include intelligent networking,
wireless communications and sensing, cloud computing, big data systems,
and security and privacy.
This article has been accepted for publication in IEEE Transactions on Consumer Electronics. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCE.2026.3680801
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:01:14 UTC from IEEE Xplore.  Restrictions apply.
