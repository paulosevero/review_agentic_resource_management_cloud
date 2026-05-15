---
paper_id: "paper-2822"
source_pdf_sha: "2bd636b8a9b0d13799444098dc73108e63c56a660582dbffbf22b25772d0d549"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 4
  page_count: 16
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2822 — fulltext
## §unknown-1

IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026 3005
Energy-Efficient RSMA-Enabled Low-Altitude
MEC Optimization via Generative AI-Enhanced
Deep Reinforcement Learning
Xudong Wang
 , Hongyang Du
 , Member, IEEE, Lei Feng
 , Member, IEEE, and Kaibin Huang
 , Fellow, IEEE
Abstract— The growing demand for low-latency computing in
6G is driving the use of UA V-based low-altitude mobile edge
computing (MEC) systems. However, limited spectrum often leads
to severe uplink interference among ground terminals (GTs).
In this paper, we investigate a rate-splitting multiple access
(RSMA)-enabled low-altitude MEC system, where a UA V-based
edge server assists multiple GTs in concurrently offloading their
tasks over a shared uplink. We formulate a joint optimization
problem involving the UA V 3D trajectory, RSMA decoding order,
task offloading decisions, and resource allocation, aiming to
mitigate multi-user interference and maximize energy efficiency.
Given the high dimensionality, non-convex nature, and dynamic
characteristics of this optimization problem, we propose a genera-
tive AI-enhanced deep reinforcement learning (DRL) framework
to solve it efficiently. Specifically, we embed a diffusion model
into the actor network to generate high-quality action samples,
improving exploration in hybrid action spaces and avoiding local
optima. In addition, a priority-based RSMA decoding strategy is
designed to facilitate efficient successive interference cancellation
with low complexity. Simulation results demonstrate that the
proposed method for low-altitude MEC systems outperforms
baseline methods, and that integrating GDM with RSMA can
achieve significantly improved energy efficiency performance.
Index Terms— Rate-splitting multiple access, mobile edge com-
puting (MEC), resource allocation, deep reinforcement learning.
I. I NTRODUCTION
I
N
THE sixth generation (6G) era, the proliferation of
Internet of Things (IoT) devices and new immersive
applications, such as augmented/virtual reality and holo-
graphic telepresence, is driving an unprecedented demand
for computational resources at the network edge [1]. These
latency-sensitive and computation-intensive services exceed
the capabilities of onboard processors in battery-powered
ground terminals (GTs), resulting in performance degradation
Received 29 June 2025; revised 5 October 2025; accepted 1 November 2025.
Date of publication 10 November 2025; date of current version 31 December
2025. This work is supported in part by the National Natural Science
Foundation of China under Grant 62571057, in part by the Beijing Natural
Science Foundation of China under Grant L254013, and in part by the BUPT
Excellent Ph.D. Students Foundation under Grant CX20253001. The associate
editor coordinating the review of this article and approving it for publication
was W. Yuan. (Corresponding author: Lei Feng.)
Xudong Wang and Lei Feng are with the State Key Laboratory of
Networking and Switching Technology, Beijing University of Posts and
Telecommunications, Beijing 100876, China (e-mail: xdwang@bupt.edu.cn;
fenglei@bupt.edu.cn).
Hongyang Du and Kaibin Huang are with the Department of Electrical and
Electronic Engineering, The University of Hong Kong, Hong Kong, SAR,
China (e-mail: duhy@eee.hku.hk; huangkb@hku.hk).
Digital Object Identifier 10.1109/TCCN.2025.3631051
when tasks are executed locally [2]. Mobile edge com-
puting (MEC) offers a viable solution by offloading tasks
to proximate edge servers, reducing latency and improving
efficiency [2]. However, terrestrial BS-centric MEC is con-
strained by coverage and capacity, especially in remote or
infrastructure-limited environments [3], or when BSs become
overloaded or fail to support edge users. These limitations
motivate the exploration of airborne MEC, wherein aerial
platforms augment the edge computing infrastructure beyond
what ground-based MEC can provide.
In recent years, the low-altitude economy (LAE) has
expanded swiftly, with uncrewed aerial vehicles (UA Vs)
emerging as key components in the evolution of mobile com-
munication networks [4], [5]. Dynamically deployed UA Vs
can form LAE networks that augment terrestrial infrastructure
with additional communication and computing capabilities.
When equipped with computing units, UA Vs serve as airborne
MEC servers, enabling low-altitude MEC systems that bring
computation offloading closer to users [6]. Such UA V-assisted
MEC networks improve coverage and service reliability while
significantly reducing end-to-end latency and GT energy con-
sumption, as users no longer need to transmit to distant base
stations. Nevertheless, supporting multiple offloading users
via a shared UA V radio link introduces substantial multi-
user interference. When many users simultaneously offload
tasks over limited spectrum resources, interference among
their uplink transmissions becomes severe and can drastically
bottleneck the system performance, especially under strict
bandwidth constraints.
Rate-splitting multiple access (RSMA) has emerged as a
promising strategy to manage interference and improve spec-
tral efficiency in multi-user networks [7]. RSMA separates
a user’s transmission into private and common components,
allowing for a combination of interference decoding and
noise handling strategies [8]. Unlike uplink Non-Orthogonal
Multiple Access (NOMA) with fixed user grouping and power
allocation, RSMA offers greater flexibility through adjustable
message splits and decoding orders, enhancing spectral effi-
ciency. This makes RSMA well-suited for low-altitude UA V
MEC, where multiple GTs can offload concurrently over the
shared spectrum without orthogonalization [9]. While existing
RSMA studies focus on downlink, extending it to uplink
UA V-assisted MEC systems offers new potential for inter-
ference mitigation. However, this introduces complex design
challenges, requiring joint optimization of UA V trajectory,
2332-7731 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence
and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3006 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
offloading decisions, RSMA decoding order, and power allo-
cation. Addressing these tightly coupled variables remains a
significant challenge.
Conventional optimization techniques, such as convex opti-
mization and heuristic algorithms, are widely used for joint
resource and trajectory design but often suffer from high
complexity and local optima [10]. Deep reinforcement learn-
ing (DRL) offers an online alternative, capable of learning
near-optimal policies for joint scheduling and control in
high-dimensional environments [11]. However, DRL faces
challenges in continuous action spaces, including poor sam-
ple efficiency and convergence instability [12]. To address
these drawbacks, some studies incorporate generative diffusion
models (GDMs), which is a class of generative AI (GenAI)
techniques adept at modeling complex distributions through
iterative sampling [13], [14], [15], [16]. By iteratively refining
random samples to match an intended distribution, diffusion
models excel at generating high-quality solutions even in
large search spaces [15]. This motivates our proposed RSMA-
assisted low-altitude MEC framework, combining generative
AI-enhanced DRL for improved energy efficiency.
A. Related Works
Low-altitude MEC systems are characterized by dynamic
node locations, limited computational resources, and a strong
dependence on communication link quality, making UA V
trajectory planning and computation offloading particularly
challenging. As a result, recent studies have investigated the
joint optimization of UA V trajectories and resource allocation
in low-altitude MEC systems [17], [18], [19], [20]. For exam-
ple, the authors in [17] designed a joint task offloading and
trajectory control scheme for UA V-assisted energy-harvesting
MEC systems to minimize propulsion energy while maintain-
ing queue stability. The authors in [18] and [19] proposed
joint optimization of communication resources and UA V tra-
jectories to improve offloading throughput or reduce energy
consumption under quality of service (QoS) and energy con-
straints. In [20], a bi-objective ant colony algorithm addressed
delay and control cost minimization problem. These stud-
ies provide valuable insights into low-altitude edge resource
management. However, transmission frameworks based on
orthogonal multiple access (OMA) struggle to accommo-
date the explosive growth in network density, particularly in
spectrum-constrained low-altitude networks, often leading to
degraded performance in interference management and task
completion rates.
Leveraging its capability to mitigate multi-user interference
and enhance spectral efficiency, RSMA has been incorpo-
rated into low-altitude networks to improve communication
performance under interference-limited conditions [21], [22],
[27], [28], [29]. In [27], an alternating optimization strat-
egy for RSMA-enabled low-altitude networks was proposed
to maximize system throughput while ensuring user rate
requirements. The work in [28] demonstrated that RSMA
significantly improves physical-layer security in a dual-UA V
downlink scenario. Additionally, RSMA has been introduced
into low-altitude MEC systems to further improve offloading
performance. Specifically, the authors in [21] designed a UA V
relay architecture and propose a data-stream splitting scheme
that minimizes UA V energy consumption under task latency
constraints. In [29], a joint passive reflecting units and dynamic
rate-splitting optimization framework was proposed for uplink
RSMA-enabled UA V-MEC systems to minimize total UA V
power consumption. The authors in [22] applied RSMA to
a UA V-MEC system assisted by a reconfigurable intelligent
surface (RIS) with wireless power transfer and observed that
the RSMA-based scheme achieves more reliable and efficient
task offloading in the presence of strong co-channel inter-
ference. Dynamic low-altitude MEC systems must adapt to
time-varying channels and fluctuating interference levels, but
traditional iterative optimization methods face scalability chal-
lenges when dealing with highly coupled decision variables in
such dynamic environments.
Data-driven optimization methods, particularly DRL, have
emerged as powerful solutions for complex optimization prob-
lems in low-altitude MEC systems due to their dynamic
adaptability and global exploration capabilities. For example,
the authors in [23] employed DRL to jointly adjust UA V
flight paths and offloading decisions, effectively reducing
the system’s energy consumption and task latency compared
to heuristic baselines. To further improve solution quality
and avoid local optima, GDMs have been introduced to
augment DRL in wireless network optimization [30], [31].
By leveraging the diffusion-based generative process, agents
can enhance their exploration of complex state spaces and
refine reward evaluation during training [32], [33], [34], [35].
For instance, the authors in [32] introduced a diffusion-assisted
DRL framework that generates diverse state samples and more
informative reward signals, achieving faster convergence and
lower computational overhead compared to standard DRL
in a dynamic resource allocation task. Similarly, in [35],
a diffusion-enhanced DRL framework was applied to a wire-
less sensing-guided edge network to derive optimal pricing
strategies, thereby maximizing user utility. Therefore, given
the generative capability, integrating diffusion models with
DRL to address joint trajectory and resource allocation in
RSMA-enabled low-altitude MEC systems presents a promis-
ing research direction.
In fact, recent studies have emphasized the role of
GenAI in enabling intelligent optimization for low-altitude
networks. In UA V-enabled IoT systems, diffusion-model-
enhanced multi-objective optimization frameworks have been
developed to jointly minimize delay, motion energy, and
computational resource consumption, thereby improving forest
monitoring efficiency under stringent UA V energy con-
straints [24]. At the networking layer, GenAI has also been
leveraged in game-theoretic frameworks, where large lan-
guage model (LLM)-enabled models assist in constructing
and solving complex UA V-assisted mobile networking games,
providing automated strategies for resource trading and secure
communication [25]. Complementarily, in the low-altitude
airspace edge inference domain, generative diffusion models
have been embedded into actor networks to design online
batching and beamforming policies, achieving near-optimal
task completion under dynamic and uncertain arrivals [26].
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3007
TABLE I
COMPARE OUR WORK WITH EXITING STUDIES
In order to highlight the contribution and novelty of our work,
we have summarized and compared several most relevant
studies in Table I.
B. Motivations and Contributions
This paper presents a joint optimization framework for
uplink RSMA-enabled low-altitude MEC systems to max-
imize energy efficiency. Due to the high-dimensional and
hybrid action space of UA V trajectory, user offloading, RSMA
decoding order, and power allocation, the conventional DRL
methods often struggle with inefficient exploration, poor con-
vergence, and vulnerability to local optima. To overcome these
challenges, we proposed a GenAI-enhanced DRL algorithm,
in which a GDM generator is embedded into the actor network
to guide the exploration process. By leveraging the capability
of GDM to generate structured and high-quality candidate
actions, the proposed algorithm effectively navigates complex
solution spaces and mitigates local optima issues common in
traditional approaches. The main contributions are summarized
as follows:
• We develop a uplink RSMA-assisted low-altitude MEC
system, where a UA V equipped with an mobile edge
server provides computing services to multiple GTs,
and the task data of each GT is split into multiple
sub-messages that are concurrently transmitted with dif-
ferent powers. Then we formulate a novel non-convex
optimization problem that maximizes energy efficiency
by jointly optimizing the UA V’s flight trajectory,
user offloading decisions, and RSMA communication
parameters.
• We propose a generative AI-enhanced deep reinforcement
learning framework, termed GDRS, to efficiently solve
the high-dimensional, non-convex optimization problem
in RSMA-enabled UA V-MEC systems. The problem is
decomposed into a decoding-order sub-problem and a
continuous control problem. To reduce the decoding
complexity, we derive a lightweight priority-based RSMA
strategy that dynamically orders sub-messages based on
channel quality and user QoS demands for uplink multi-
user low-altitude MEC networks, enabling interference
cancellation with low overhead.
• To overcome the challenges of poor exploration and
local optima, we embed a generative diffusion model
into the policy network. This integration allows the agent
to generate structured candidate actions, including UA V
trajectories and resource allocation decisions, leading to
more stable convergence and higher policy quality across
dynamic and coupled state-action spaces.
• We carried out a comprehensive set of simulations to
validate the proposed GDRS and to assess the scala-
bility of the RSMA framework. The results show that
our RSMA-enabled framework achieves higher through-
put and energy efficiency compared to NOMA-based
schemes. Moreover, the GenAI-enhanced DRL method
outperforms conventional DRL approaches in terms of
reward, highlighting the superior exploration capability
of the diffusion model.
The rest of this paper is organized as follows. Section II
introduces the system model and formally defines the opti-
mization problem. In Section III, we elaborate on the
algorithmic framework developed to address the problem.
Section IV showcases simulation results and provides an
in-depth discussion of the numerical findings. Section V high-
lights the key contributions and draws the final conclusions of
the paper.
II. S YSTEM MODEL AND PROBLEM FORMULATION
As illustrated in Fig. 1, we investigate an RSMA-assisted
low-altitude MEC systems, where the UA V is despatched to
serve K ≜ {1, 2, . . . , K} GTs. Given the stringent limitations
on size, payload capacity, and onboard energy in lightweight
rotary-wing UA Vs for airborne MEC applications, we con-
sider a single-antenna UA V to circumvent the extra hardware
burden and energy expenditure associated with multi-antenna
implementations, and leave the multiple UA Vs for future work.
A. Network Model
We consider a uniformly gridded task area, where the
UA V dynamically determines its 3D trajectory through discrete
waypoints to serve the GTs. The horizontal coordinate of the
center of the i-th cell is represented by Dℓ
i = [ xi, yi]T ∈
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3008 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 1. RSMA-enabled multi-user low-altitude MEC networks.
R2×1, where L ≜ {1, 2, . . . , L} denotes the set of all cell
indices. The spacing between the centers of neighboring cells
along the x-axis and y-axis are denoted by xs and ys,
respectively. The UA V’s horizontal position is represented by
Du
n ∈ L, where n ∈ N ≜ {1, 2, . . . , N} and N represents
the total number of discrete time slots. Each time slot is
associated with a UA V flight duration level tu
n ∈ T ≜
{1, 2, . . . , T}, where the actual duration is bounded by tmin ≤
tu
n × ∆t ≤ tmax. Here, tmin and tmax define the minimum
and maximum allowable flight durations, and ∆t = ⌊tmax/T ⌋
denotes the time resolution per level. The initial and final UA V
positions are fixed and denoted as Du
0 and Du
e , respectively.
Accordingly, the horizontal UA V path can be approximated
as the sequence {Du
0 , Du
1 , . . . , Du
n, . . . , Du
N , Du
e }. To capture
the UA V’s vertical mobility, the altitude at time slot n is
represented by hu
n ∈ H ≜ {1, 2, . . . , H}. The actual height
must satisfy hmin ≤ hu
n × ∆h ≤ hmax, where hmin and
hmax denote the minimum and maximum permissible heights,
respectively, and ∆h = ⌊hmax/H⌋ denotes the step size
between discrete altitude levels. Consequently, the complete
UA V trajectory consists ofN discrete 3D waypoints [Du
n, hu
n]
and the associated time durations tu
n, ∀n ∈ N .
B. Mobility Model
The ground terminals are assumed to be either stationary or
with low mobility, which aligns with practical IoT-type users
such as sensors or handheld devices. Their horizontal positions
are fixed at the beginning of the mission, denoted by uk =
[xk, yk]T ∈ R2×1, k ∈ K, and are uniformly distributed across
the task area. The horizontal velocity of UA V is expressed as
vh
n = ∥Du
n+1 − Du
n∥
tun
≤ V h
max, ∀n ∈ N , (1)
where V h
max represents the maximum horizontal velocity.
Besides, the vertical flying velocity is expressed as
vv
n = ∥hu
n+1 − hu
n∥
tun
≤ V v
max, ∀n ∈ N , (2)
where V v
max denotes the UA V’s maximum vertical velocity.
When vh
n = 0, the UA V is either hovering or performing steady
straight-and-level flight during time slot n.
Based on [36], the propulsion energy consumption of the
UA V is given by
Euav =
NX
n=1
tu
n
 
W0

1 + 3(vh
n)2
U 2t

+ 1
2 F0ρgM (vh
n)3
+ W1
 r
1 + (vhn)4
4¯v4 − (vh
n)2
2¯v2
! 1
2
+ W2vv
n
!
, (3)
where W0 and W1 represent the constant blade profile power
and the induced power under hovering conditions, while
W2 denotes the constant power required during ascent or
descent. The parameters F0 and g represent the fuselage drag
ratio and the rotor solidity. In addition, ρ refers to the air
density, and M stands for the area of the rotor disc. The
parameter Ut denotes the tip velocity of the rotor blade, and
¯v signifies the tip velocity of the rotor blade, and ¯v refers to
the average induced airflow velocity in hovering flight.
C. Communication Model
Based on the air-to-ground propagation model for urban sce-
narios [37], the probability of establishing the LoS connection
between the UA V and GT k can be expressed as
ȷk,n = 1
1 + α exp

−β

arctan

hu
n
lk,n

− α
 , (4)
where α and β are environment-dependent constants, lk,n =p
(xi − xk)2 + (yi − yk))2. Based on this, the corresponding
pathloss can be expressed as
dk,n = 20log
q
(hun)2 + l2
k,n

+ A1 × ȷk,n + A2, (5)
where A1 = ζLoS − ζNLoS, A2 = 20log( 4πfc
c ) + ζNLoS,
fc denotes the carrier frequency; c represents the speed of
light, ζLoS and ζNLoS are the environment-dependent path loss
factors for LoS and NLoS conditions, respectively. We define
ak,n ∈ {0, 1} as the offloading indicator of GT k at time slot
n, with ak,n = 1 representing task offloading to the UA V and
ak,n = 0 indicating local computation. To support concurrent
offloading, RSMA is applied. Specifically, the message of each
GT wk,n is split into |I| sub-messages wk,n,i, each allocated
a transmit power pk,n,i to achieve rate splitting, such thatP
i∈I pk,n,i ≤ Pmax, ∀k, n, where Pmax is the maximum
uplink transmit power of each GT. The composite message is
wk,n =P
i∈I
√
pk,n,iwk,n,i, ∀k, n. Thus, the received signal
of UA V at time slot n is obtained as
yn =
X
k∈K
ak,n
√gk,nwk,n + n0
=
X
k∈K
ak,n
X
i∈I
√gk,npk,n,iwk,n,i + n0, (6)
where gk,n denotes the channel gain between k-th GT and
UA V , given by gk,n = 10 −dk,n/10, where n0 represents
the additive white Gaussian noise (AWGN). In this paper,
we assume that perfect CSI can be obtained [38], [39].
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3009
To decode multiple sub-messages, the UA V employs suc-
cessive interference cancellation (SIC). Let πk,n,i, i ∈ I
indicate the SIC decoding order of sub-message wk,n,i, and let
π = {πk,n,i, ∀k, n, i} denote a decoding permutation, which
contains all valid SIC decoding sequences for the |I| K sub-
messages. Under this decoding strategy, the achievable uplink
rate for sub-message wk,n,i is obtained as [29]
Rk,n,i = B log2
 
1 + gk,npk,n,i
BN0 +P
(k′,i′)∈Wk,n,i
gk′,npk′,n,i′
!
,
(7)
where B denotes the system bandwidth, N0 represents
the noise power spectral density. The set Wk,n,i =
{(k′, i′)|ak′,n = ak,n, πk′,n,i′ > π k,n,i, ∀k′, i′} contains the
sub-messages that are decoded after wk,n,i based on the SIC
decoding order at the UA V .
D. Computing Model
In the considered RSMA-enabled low-altitude MEC sys-
tems, each GT has an estimated computational task Gk =
{Ck, Dk}, where Ck represents the total required CPU cycles,
Dk denotes the overall data size to be calculated. As discussed
in [40], when GT k chooses to offload its task to the UA V
during time slot n, the expected amount of data successfully
transmitted in that slot is obtained as
mk,n =
X
i∈I
ak,nκntu
nRk,n,i, (8)
where κn ∈ [0, 1] represents the portion of time slot n that is
assigned to data transmission. To ensure that the transmitted
data mk,n can be processed by the UA V’s onboard CPU with
a processed rate of fu, κn must be properly chosen. This
requirement imposes the following constraint:
X
i∈I
κntu
nRk,n,i ≤ fu(1 − κn)tu
n
Dk
Ck
. (9)
To further enhance the total amount of processed data, αn is
further constrained as
κn = fuDkP
i∈I Rk,n,iCk + fuDk
. (10)
Given the offloading decision ak,n at time slot n and (10),
the amount of task data Gk processed during slot n is
represented as
ϖk,n = ak,n
fuDktu
n
P
i∈I Rk,n,iP
i∈I Rk,n,iCk + fuDk
+ (1 − ak,n)tu
nfg,
(11)
where fg denotes the processed speed of the GT’s CPU.
In (11), the delay due to downlink transmission from UA V
to GT is neglected, assuming that the corresponding data size
is negligible. Accordingly, the overall system energy efficiency
can be defined as η =PK
k=1
PN
n=1 ϖk,n/Euav.
E. Problem Formulation
We aim to maximize the system energy efficiency η while
maintaining reliable MEC performance by jointly optimizing
the UA V trajectory, task offloading decisions, uplink power
allocation, and SIC decoding order. Let A = {ak,n, ∀k ∈
K, ∀n ∈ N } , P = {pk,n,i, ∀k ∈ K , ∀n ∈ N , ∀i}, D =
{Du
n, ∀n ∈ N }, h = {hu
n, ∀n ∈ N }, and t = {tu
n, ∀n ∈ N },
the optimization problem can then be formulated as
P0 : max
A,P,D,h,t,π
η (12a)
s.t. C1 : ak,n = {0, 1}, ∀k ∈ K, ∀n ∈ N , (12b)
C2 :
X
n∈N
ϖk,n ≥ Dk, ∀k ∈ K, (12c)
C3 :
X
i∈I
pk,n,i ≤ Pmax, ∀k ∈ K, ∀n ∈ N , (12d)
C4 :


Du
n+1 − Du
n


tun
≤ V h
max, ∀n ∈ N , (12e)
C5 :


hu
n+1 − hu
n


tun
≤ V v
max, ∀n ∈ N , (12f)
C6 : hmin ≤ hu
n × ∆h ≤ hmax, ∀n ∈ N , (12g)
C7 : tmin ≤ tu
n × ∆t ≤ tmax, ∀n ∈ N , (12h)
C8 : pk,n,i ≥ 0, ∀k ∈ K, ∀n ∈ N , ∀i ∈ I , (12i)
C9 : π ∈ Π, (12j)
C10 :
X
i∈I
Rk,n,i ≥ Rmin, ∀k ∈ K, ∀n ∈ N
(12k)
C11 : Rk,n,1 : Rk,n,2 : . . . : Rk,n,I
= µk,n,1 : µk,n,2 : . . . : µk,n,I , ∀k ∈ K, ∀n ∈ N ,
(12l)
where µk,n,i denotes a predefined non-negative coefficient that
allocates a proportion of the rate Rk,n to the i-th sub-message
of GT k in time slot n, satisfying Rk,n,i = µk,n,iRk,n, ∀i andP
i∈I µk,n,i = 1, ∀k, n. The minimum rate requirement for
each GT is denoted by Rmin. Constraints in P0 are interpreted
as follows: C1 models offloading as a binary decision problem;
C2 ensures tasks are completed within the UA V’s mission
time; C3 limits the total transmit power of each GT; C4 ∼ C7
describe UA V mobility constraints; C8 enforces non-negative
transmission powers; C9 guarantees feasible SIC decoding;
C10 enforces the rate requirement; and C11 ensures valid rate
splitting among sub-messages.
The optimization problem P0 is a non-convex mixed-integer
program due to the discrete offloading variable a, the non-
convex objective, and constraint C2, making it difficult to
solve optimally. Moreover, the UA V’s complex energy model
further complicates trajectory and flight time design for energy
efficiency maximization. Prior work has shown that solving
P0 via successive convex approximation (SCA) incurs high
computational cost, rendering it impractical [36]. To overcome
these challenges, we derive the optimal decoding order policy,
and then develop a GenAI-based optimization framework,
detailed in the following section.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3010 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
III. T HE PROPOSED GDRS A LGORITHM
To efficiently address problem P0, we decompose it into
two sub-problems: 1) the decoding order sub-problem P1,
and 2) the joint UA V 3D trajectory, power allocation, and
task offloading sub-problem P2. For P1, the optimal decoding
policy π is determined based on channel gains. Subsequently,
P2 is reformulated as a Markov decision process (MDP), and
a generative AI-enhanced DRL framework is developed to
optimize {A, P, D, h}.
A. Decoding Order Policy
The optimal decoding order plays a critical role in mit-
igating inter-submessage interference and enhancing overall
energy efficiency, and thus must be carefully considered.
Given a fixed UA V trajectoryD, altitude profile h, offloading
decisions A, power allocation P, and UA V flight timet, P0 is
rewritten as
P1 : max
π
η (13a)
s.t. C9, C10, C11. (13b)
Solving the decoding order optimization problem P1 is chal-
lenging due to its non-convex objective function and the
intricate interdependence of discrete variables, rendering it a
mixed-integer nonlinear programming (MINLP) problem that
is typically hard to solve. While exhaustive search meth-
ods [41] can yield the optimal solution, their computational
cost scales exponentially with the number of sub-messages,
making them impractical for multi-user systems. Existing
works [42], [43], [44] often adopt channel gain-based heuris-
tics for decoding order. To better balance computational
efficiency and system performance, we propose a decoding
strategy that jointly considers both the channel gains and the
rate-splitting proportions of each GT’s sub-messages.
Lemma 1: The decoding order of sub-messages is deter-
mined by sorting υk,n,i ≜ |gk,n|2

1 + 1
ρmin
k,n,i

=
|gk,n|2

1 + 1
2(µk,n,i Rmin)−1

in descending order, where
ρmin
k,n,i represents the minimum signal-to-interference-plus-
noise ratio (SINR) required for GT k to decode the i-th
sub-message at time slot n.
Proof: Since the decoding order policy π influences
the achievable data rate but does not impact the energy con-
sumption of UA V , the optimization problemP1 is equivalently
reformulated as
P1.1 : max
πk,n,i
X
k∈K
ϖk,n (14a)
s.t. C9, C10, C11. (14b)
As indicated in (11), for given UA V trajectory D, altitude
profile h, offloading decisions A, power allocation P, and
flight time t, the data processed ϖk,n depends solely on the
sum rate P
i∈I Rk,n,i. Hence, maximizing ϖk,n reduces to
maximizing the aggregate rate. To this end, we aim to design
a decoding order policy that maximizes the sum rate at each
time slot. Let wa and wb be two consecutive sub-messages
in the decoding sequence, associated with respective channel
gains ga and gb, and corresponding power levels pa and
pb. If the cumulative interference from previously decoded
sub-messages is upper bounded by a constant ϵ, we have
|ga|2pa + |gb|2pb + ξ + N0 ≤ ϵ, (15)
where ξ represents the interference from sub-messages
decoded after both wa and wb. Two decoding scenarios are
possible: a) wa is decoded before wb, and b) wb is decoded
before wa. We analyze the achievable signal strength under
both cases. Case a): when wa decoded first: In Case a), where
wa is decoded first, the feasible power allocation for wa and
wb must satisfy
|ga|2pa
|gb|2pb + ξ + N0
≥ ρmin
a , |gb|2pb
ξ + N0
≥ ρmin
b , (16)
where 0 ≤ pa, pb ≤ Pmax. Based on this feasible region, the
corresponding lower bound of the achievable signal strength
can be expressed as
pa ≥ ρmin
a (ρmin
b + 1)(ξ + N0)
|ga|2 , p b ≥ ρmin
b (ξ + N0)
|gb|2 , (17)
and the associated upper limit for power control is given by
pa ≤ Pmax, p b ≤ min


Pmax,
|ga|2Pmax
ρmin
a
− ξ − N0
|gb|2


 ,
(18)
The maximum achievable signal strength from sub-messages
wa and wb, denoted by χ ≜ |ga|2pa + |gb|2pb, can thus be
written as
χ ≤ χa ≜ min
n
|ga|2Pmax

1 + 1
ρmin
b

,
 
|ga|2 + |gb|2
Pmax, ϵ − ξ − N0
o
. (19)
Case b): when wb is decoded first, the maximum combined
signal strength from wa and wb can similarly be expressed as
χ ≤ χb ≜ min
n
|gb|2Pmax

1 + 1
ρmin
b

,
 
|ga|2 + |gb|2
Pmax, ϵ − ξ − N0
o
. (20)
By comparing expressions (19) and (20), we observe that
in Case a), if |ga|2

1 + 1
ρmin
a

≥ | gb|2

1 + 1
ρmin
b

, then
χa ≥ χb, i.e., decoding of wa, indicating that decoding wa
first yields higher signal strength. Conversely, in Case b),
if |ga|2

1 + 1
ρmin
a

≤ |g b|2

1 + 1
ρmin
b

, then χa ≤ χb, and
decoding wb first becomes the better choice.
This confirms that the optimal decoding strategy is to
prioritize decoding the sub-message wk,n,i corresponding to
the larger value of |gk,n|2

1 + 1
ρmin
k,n,i

. Accordingly, a near-
optimal decoding order is obtained by sorting all sub-messages
in descending order of υk,n,i ≜ |gk,n|2

1 + 1
ρmin
k,n,i

=
|gk,n|2

1 + 1
2(µk,n,i Rmin)−1

. This concludes the proof. □
Lemma 1 reveals that the optimal decoding order in RSMA-
enabled UA V-MEC systems can be determined by a unified
metric that jointly accounts for both channel quality and
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3011
QoS-driven SINR thresholds of the sub-messages. This implies
that a sub-message with either a stronger channel condition
or a stricter decoding requirement should be given higher
decoding priority. Such an ordering rule not only balances
interference suppression and fairness across users but also
converts the otherwise factorial-complexity decoding-order
optimization into a simple sorting operation, thereby signif-
icantly reducing computational burden.
B. MDP Construction
With the decoding order strategy π determined, problem
P0 is reformulated as
P2 : max
A,P,D,h,t
η (21a)
s.t. C1 ∼ C8. (21b)
To obtain the optimal joint trajectory, task offloading, and
power allocation, we propose generative AI-enhanced DRL
method.
DRL operates on two core components: the agent and the
environment. Their interaction is typically modeled as a MDP,
characterized by ⟨S, A, R, ω, P⟩, where S denotes the state
space, and A the action space available to the agent. The
reward function R quantifies the immediate feedback received
after taking a specific action in a particular state, whereas the
discount factor ω controls the trade-off between short-term
and long-term rewards. The transition probability function P
governs the dynamics of state evolution following each action.
The key components S, A, and R are detailed as follows:
1) State Spaces: At time slot n, the state of GT k is
defined by its fixed location, i.e., sk(n) = ukn ≜ uk, ∀n ∈
N . The state of UA V su(n) can be represented by its 3D
position and time allocation, i.e., su(n) = ( Du
n, hu
n, tu
n).
Hence, the overall system state at slot n is obtained as s(n) =
{{sk(n)}k∈K, su(n), n} ∈ S .
2) Action Spaces: Following the mobility model in [45], the
UA V is allowed to move only to one of the adjacent horizontal
cells within a single time slot. As a result, its horizontal
position Du(n) is updated in the next slot as:
Du(n + 1) =










Du(n) + (0, ys), if d(n) = N
Du(n) − (0, ys), if d(n) = S
Du(n) + (xs, 0), if d(n) = E
Du(n) − (xs, 0), if d(n) = W
Du(n) + (0,0), if d(n) = O
(22)
where d(n) denotes the UA V’s selected horizontal flight action
at time slot n, with E, S, W , and N, indicating movement in
the directions of east, south, west, and north, respectively. The
symbol O signifies the UA V remains stationary. In the vertical
dimension, the UA V is similarly constrained to move only to
an adjacent altitude level in each time slot. Accordingly, the
UA V’s altitudehu
n will be updated in the next slot as:
hu
n+1 =



hu
n + 1, if h(n) = U
hu
n − 1, if h(n) = D
hu
n + 0, if h(n) = O
(23)
where h(n) denotes the UA V’s chosen altitude action at
time slot n; U and D represent ascending and descending,
respectively. If the selected horizontal action d(n) leads the
UA V outside the area of interest at time slot n + 1, it is reset
to O to keep the UA V stationary. Similarly, ifh(n) causes the
UA V’s altitude to exceed the allowable range [hmin, hmax],
it is set to O to retain the current altitude level. Accordingly,
the system action at time slot n can be expressed as a(n) =
(d(n), h(n), tu
n, {ak,n}k∈K, {pk,n,i}k∈K, i ∈ { 1, 2}) ∈ A ,
where the action space A comprises the UA V’s movement and
time allocation actions, as well as the GTs’ task offloading and
power control decisions.
3) Rewards: The reward associated with a state-action pair
(s(n), a(n)) at time slot n is given by:
r(s(n), a(n)) = λ1
X
k∈K
ϖk,n+1
Euav
n+1
− λ2 P V. (24)
After performing action a(n), the reward r(s(n), a(n)) is
defined as the energy efficiency, measured by the ratio between
the amount of data processed by each GT in the next time slot,
i.e., ϖk,n+1, and the UA V’s propulsion energy consumption
Euav
n+1. To influence the convergence behavior, two scaling
factors λ1 and λ2 are introduced. Additionally, P V denotes a
penalty function, which is defined as
P V =
(
c0, if C1 ∼ C8 are not satisfied,
0, Otherwise, (25)
where c0 is a positive constant that controls the penalty
magnitude. Through this design, the DRL framework aims
to learn energy-efficient solutions for RSMA-enabled low-
altitude MEC systems.
C. The Proposed Generative AI-Enhanced DRL Method
Jointly optimizing UA V trajectory, task offloading, and
power allocation presents significant challenges for conven-
tional DRL algorithms, primarily due to the high-dimensional
and discrete nature of the action space. The structured cou-
pling of UA V mobility, interference management through
RSMA, and computation offloading decisions leads to an
optimization landscape where the search space is vast, highly
non-convex, and prone to local optima. Standard DRL agents
often exhibit poor sample efficiency and limited exploration
capability under such conditions, resulting in unstable con-
vergence and suboptimal policies [46]. Motivated by these
limitations, we adopt a diffusion model-based DRL framework
that leverages the generative modeling ability of diffusion
processes to iteratively refine noisy samples into structured
candidate actions consistent with system constraints. This
generative mechanism promotes more effective exploration,
enhances the agent’s ability to escape local minima, and
ensures that synthesized actions, such as UA V trajectories and
resource allocation patterns, are both diverse and high-quality.
The Denoising Diffusion Probabilistic Model (DDPM) pro-
gressively perturbs data into Gaussian noise through a forward
diffusion process and then learns to recover the original
data via a reverse denoising process [47]. Leveraging this
generative mechanism and its ability to incorporate conditional
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3012 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
information, we design a diffusion-based optimizer for enhanc-
ing solution quality and synergizing effectively with DRL to
address dynamic and complex optimization in RSMA-enabled
low altitude MEC systems. Compared with other generative
models, such as generative adversarial networks (GANs) and
variational autoencoders (V AEs), diffusion models avoid mode
collapse and oversmoothing issues, enabling more stable and
diverse sample generation, which is particularly critical for
the non-convex, mixed-integer optimization tasks considered
in this work.
In the diffusion framework, an optimal decision under the
current environment is progressively perturbed with noise
until it becomes Gaussian, a process referred to as forward
probability noising [13]. In the reverse phase, the decision
generation network πθ(·) serves as a denoiser that reconstructs
the original solution z0 from Gaussian noise, conditioned on
the system state s. The following presents the formal mathe-
matical formulation of this diffusion-based decision process.
1) Forward Process: The decision output z0 = πϑ(s) repre-
sents the probability distribution over discrete decisions under
the observed environment state s. In the forward diffusion pro-
cess, this initial distribution is gradually perturbed by Gaussian
noise, resulting in a sequence of intermediate representations
z1, z2, . . . ,zT , each sharing the same dimensionality as z0.
At each step t, the transition from zt−1 to zt follows a
Gaussian distribution with mean √
1 − φtzt−1 and variance
φtI, as described in [48].
q (zt|zt−1) = N

zt;
p
1 − φtzt−1, φtI

, (26)
where t = 1, . . . , T , φt = 1 − e− φmin
T − 2t−1
2T 2 (φmax−φmin)
denotes the time-dependent variance in the forward
process [48].
Since each zt depends only on its immediate predeces-
sor zt−1, the forward process constitutes a Markov chain.
Consequently, the distribution of zT conditioned on z0 can
be expressed as the product of transition probabilities across
denoising steps [48], which is shown as
q(zT |z0) =
TY
t=1
q(zt|zt−1). (27)
Although the forward process is not explicitly executed,
it defines a closed-form relationship between z0 and any
intermediate state zt, given by
zt = √
¯νtz0 +
√
1 − ¯νtϵ, (28)
where νt = 1 − φt, ¯νt = Qt
k=1 νk denotes the cumulative
product up to step t. The forward process relates zt and
z0 as a noisy transformation, where ε ∼ N (0, I) is stan-
dard Gaussian noise. As t increases, zT converges to pure
noise distributed as N (0, I). However, since wireless network
optimization problems typically lack ground-truth datasets of
optimal decisions z0, the forward process is not executed in
the proposed framework.
2) Reverse Process: The goal of the reverse process is
to reconstruct the desired target z0 starting from a noise
sample zT ∼ N (0, I) by iteratively denoising it. Within
our framework, this procedure corresponds to synthesizing the
optimal decision policy from an initially Gaussian-distributed
sample. The transition between zt and zt−1 is modeled as
p(zt−1|zt), which is intractable in closed form but can be
approximated by a Gaussian distribution, expressed as
pϑ (zt−1|zt) = N (zt−1; µϑ (zt, t, s) , ˜φtI) , (29)
where the mean µϑ is learned via a deep neural network, and
the variance is obtained as [48].
˜φt = 1 − ¯νt−1
1 − ¯νt
φt. (30)
By applying Bayes’ theorem, the reverse process can be
reformulated in terms of the forward process and expressed
as a Gaussian probability density function. Accordingly, the
mean is derived as
µϑ (zt, t, s) =
√νt (1 − ¯νt−1)
1 − ¯νt
zt +
√¯νt−1φt
1 − ¯νt
z0, (31)
where t = 1, . . . , T. Based on the forward process in (28), the
reconstructed sample z0 can be directly estimated by
z0 = 1√¯νt
zt −
r
1
¯νt
− 1 · tanh (σϑ(zt, t, s)) , (32)
where σϑ(zt, t, s) denotes a deep neural network parame-
terized by ϑ that predicts the denoising noise conditioned
on the observed state s. To prevent excessive noise in the
reconstructed decision z0, which may obscure the true action
probabilities, the output is scaled using a hyperbolic tangent
activation to ensure bounded noise levels.
During the reverse denoising process, each step t introduces
a new noise component σϑ, which remains independent of the
forward-process noise σ. As a result, z0 cannot be directly
recovered using (32). Instead, we substitute (32) into the
reverse transition expression in (31) to estimate the mean,
shown as
µϑ (zt, t, s) = 1√νt

zt − φt tanh (σϑ(zt, t, s))√1 − ¯νt

. (33)
We then sample zt−1 from the reverse transition distri-
bution p(zt)pϑ(zt−1|zt) and iterate this process over t =
T, T − 1, . . . ,1. By recursively applying these steps, the final
generation distribution pϑ(z0) is given by
pθ (z0) = p (zT )
TY
t=1
pθ (zt−1|zt) , (34)
where p (zT ) denotes a standard Gaussian distribution. After
the reverse process yields the generative distribution pϑ(z0),
a sample of the final output z0 can be drawn accordingly.
A common challenge in training generative models lies
in the inability to backpropagate gradients through stochastic
sampling operations. To overcome this, we adopt a reparam-
eterization technique that separates the source of randomness
from the distribution parameters. Specifically, the sampling is
reformulated using the following update rule:
zt−1 = µϑ (zt, t, s) + ( ˜φt/2)2 ⊙ σ, (35)
where σ ∼ N (0, I). By recursively adopting the reverse update
rule in (35), all intermediate states zt (0 ≤ t ≤ T ), including
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3013
the final output z0, can be generated from an initial Gaussian
noise sample.
Finally, the softmax function is applied to z0 to convert it
into a valid probability distribution, given by
πϑ(s) =
(
ezj
0
PA
i=1 ezi
0
, ∀j ∈ A
)
(36)
Each element in πϑ(s) represents the probability of selecting
a specific action under state s.
To implement the proposed approach in practice, the first
step involves calculating the mean µϑ of the reverse transition
distribution pϑ(zt−1|zt), as defined in (29) and (33), and
then update zt−1 using the rule in (35). Subsequently, the
optimal decision distribution z0 is obtained via (36). To further
enhance optimization, we integrate the diffusion model into
the Soft Actor-Critic (SAC) framework. SAC is an off-policy
DRL algorithm that augments the reward with an entropy
term to jointly maximize expected returns and policy entropy,
effectively balancing exploration and exploitation.
3) Experience Replay: The agent continuously interacts
with the environment to collect trajectory data. At slot n,
the actor observes the state s(n) and generates a discrete
action distribution πϑ(s(n)). An action a(n) ∼ πϑ(s(n)) is
sampled and executed, after which the environment returns a
reward r(n) = (s(n), a (n)) and transitions to the next state
s(n+1). The resulting transition tuple (s(n), a(n), r(n), s(n+
1) is stored in the experience replay buffer B. This replay
mechanism enables real-time interaction while allowing asyn-
chronous sampling of past experiences, thereby enhancing
training efficiency.
4) Double Critic Networks: In the proposed framework,
the critic network is implemented as a soft Q-function
Qψ(s(n), a(n)), which evaluates the expected return aug-
mented by the entropy of the policy ψ under (s(n), a(n)).
The formulation is given by
Qψ(s(n), a(n))= Es(n+ 1)∼B[r(s(n), a(n))+ ωVπ(s(n+1)))],
(37)
where ω denotes the reward discount factor, and s(n + 1) is
the subsequent state sampled from the replay buffer B. The
corresponding soft value function Vπ(s(n)) is expressed as:
Vπ(s(n))= Ea(n)∼π[Qψ(s(n+1), a(n+1))+ γJ (πϑ(s(n)))],
s.t. J (πϑ(s(n)))= −πϑ(s(n)) logπϑ(s(n)), (38)
the term J(πϑ(s(n))) represents the entropy of the policy
at state s(n), while γ ∈ [0, 1] is a tunable temperature
coefficient that regulates the influence of the entropy in the
objective. To reduce the overestimation bias often observed
in Q-learning algorithms, GDRS incorporates a pair of critic
networks, Qψ1(s(n), a(n)) and Qψ2(s(n), a(n)). The actor
is trained using the smaller of the two Q-values, ensuring a
conservative and stable policy update.
5) Target Networks: Each critic network is associated with
a corresponding target network, parameterized by ˆψ1 and ˆψ2,
respectively. These target networks mirror the architecture
of their online counterparts and are introduced to enhance
training stability by reducing fluctuations in target estimates.
Fig. 2. The proposed GDRS optimization framework for joint optimization
of UA V trajectory, task offloading and power allocation in RSMA-enabled
low-altitude MEC systems.
To ensure smooth updates, their parameters are adjusted incre-
mentally using a soft update strategy, defined as:
ˆψi ← ςψ i + (1 − ς) ˆψi, (39)
where ς ∈ (0, 1] denotes the soft update rate, and i = 1, 2.
To train the critic networks, the agent draws a mini-batch of
transition samples from the replay buffer B and optimizes the
network parameters by minimizing the following loss function:
LQ(ψi) = E(s(n),a(n))∼B[1
2(Qψi(s(n), a(n)) − ˆq)2], (40)
where we define the Q-target ˆy as
ˆq = r(s(n), a(n)) + ωV ˆψ(s(n + 1)). (41)
Subsequently, the parameters of the two critic networks are
updated using gradient descent, following the update rule:
ψi ← ψi − τc∇ψi LQ(ψi), (42)
where τc represents the learning rate of the critic network for
updating critic network parameters.
For training the policy network, the actor aims to maximize
the expected Q-value to enhance decision-making quality. The
objective function for updating the actor is defined as:
Lπ(ϑ) = Es(n)∼B[γJ (πϑ(s(n))) − min
i=1,2
Qψi(s(n), a(n))],
(43)
and we update the parameter ϑ, shown as
ϑ ← ϑ − τa∇ϑLπ(ϑ), (44)
where τa indicates the learning rate of actor network.
D. Algorithm Framework
Fig. 2 shows the framework of the proposed GDRS method,
which extends the SAC algorithm. It comprises several
core components for policy training, including an diffusion
model-based actor network, double critic networks with corre-
sponding target networks, an experience replay buffer, and the
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3014 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
interaction environment [46]. In addition, the detailed progress
of the proposed GDRS method is presented in Algorithm 1.
The computational complexity analysis of the proposed
GDRS method is presented as follows. Notably, since the
number of GTs K and the number of sub-messages |I|
are much smaller than the model size and diffusion steps,
the decoding-order cost can be safely neglected compared
with the diffusion sampling and gradient updates. As for
the action sampling, the computational complexity of action
sampling is O(EQT |ϑ|), where E, Q, and T are the total
training episodes, sampling trajectory, and diffusion steps,
respectively, |ϑ| is the number of actor parameters. As for
the experience collection, the agent interacts with the envi-
ronment, whose bookkeeping scales linearly with the state
dimension Ds. Thus, the complexity of experience collec-
tion is O(EQDs). For learning updates, the model performs
mini-batch backpropagation through the actor and the two
critics followed by soft target updates, which contributes
O (EQ(B|ϑ|) + O(B|ψ|) + O(|ϑ| + |ψ|)), where B is the
batch size and |ψ| is the total number of critic parameters.
With the above, the overall training complexity is expressed
as O
 
E Q
 
Ds + T |ϑ| + (B + 1)(|ϑ| + |ψ|)

.
IV. S IMULATION RESULTS AND DISCUSSION
This section presents simulation studies designed to evaluate
the effectiveness of the proposed GDRS approach. We begin
by outlining the experimental configuration and baseline
settings. Then, the simulation outcomes are discussed and
examined thoroughly.
A. Experimental Setup
1) Experimental Configuration: We consider a task area
measuring 1000 ×1000 m, which includes one UA V equipped
with an MEC server and certain number of GTs. The GTs
are randomly located in the target area following a uni-
form distribution. We set the initial location of the UA V as
[0, 0, 200]. The total time slots of the system is set to 100,
and each time slot is of length 1 s. According to the settings
about propulsion model of the rotary-wing UA V [36], we set
Ut = 120 m/s, ¯v = 4.03 m/s, F0 = 0.6, g = 0.05, ρ = 1.225,
M = 0.503. Each GT divides its transmitted signal into two
distinct sub-messages, 1 i.e., I = 2. The rate-splitting ratio of
the sub-messages is set to µk,n,i = 0.5, ∀k, n, i. As for the
training model, we set the learning rates of actor network and
critic networks as τc = τa = 5 × 10−4, and set the update
rate ς = 5 × 10−3 for soft updating the target networks. All
experiments were conducted in a Python 3.10 environment
with PyTorch 2.1.0 on a server running Ubuntu, equipped with
a 2.10 GHz Intel Xeon Gold 5218R processor (40 cores, 503
GB RAM) and an NVIDIA A100 GPU featuring 80 GB of
memory. More parameters about the considered scenario and
proposed method are shown in Table II.
1Setting the RSMA message split number to two represents a rational and
efficient trade-off in the context of this study. It preserves the core advantages
of RSMA, namely flexible interference management and rate allocation, while
avoiding the exponential growth in training and implementation complexity
that would result from excessive message splitting.
Algorithm 1 GDRS: Generative Diffusion-Enhanced
DRL for RSMA-Enabled Low-Altitude MEC
Input: Initialize replay buffer B; actor parameters ϑ;
critic parameters ϕ1, ϕ2; target parameters
ˆψ1 ← ψ1, ˆψ2 ← ψ2; training step index e;
diffusion step index t; trajectory counter q.
1 while e < E do
2 while q < Q do

## §3 Determine the optimal decoding order π

according to Lemma 1;
4 Observe current state s(n); sample initial noise
zT ∼ N (0, I);
5 while t < T do
6 Apply denoising model σϑ(zt, t, s(n));
7 Compute mean µϑ and variance ˜φt
using (33) and (30);
8 Update zt using (35);
9 t ← t + 1;
10 Sample discrete action a(n) to determine UA V
trajectory, offloading, and power allocation;
11 Execute a(n) in the environment; record the
resulting reward r(n) and the subsequent state
s′(n);

## §12 Store the transition tuple

(s(n), a(n), r(n), s′(n)) in B;

## §13 Randomly select a mini-batch of samples from

B;
14 Update critic parameters ψ1, ψ2 using (40),
(42);
15 Update actor parameters ϑ using (43) and (44);
16 Perform soft updates on ˆψ1, ˆψ2 via (39);
17 q ← q + 1;
18 e ← e + 1;
Output: Optimized actor policy ϑ∗.
2) Baseline Settings: To present fair comparison, we com-
pare our proposed GDRS method with the following
well-known DRL benchmark:
• PPORS: Proximal Policy Optimization for RSMA-
enabled low-altitude MEC, where the agent learns an
optimal policy in a discrete action space to maximize
the energy efficiency.
• DQNRS: Deep Q-Network for RSMA-enabled low-
altitude MEC, where the agent approximates the optimal
action-value function in a discrete action space to maxi-
mize the energy efficiency.
• GDRS-Random: Generative diffusion-enhanced opti-
mization for RSMA-enabled low-altitude MEC, where
UA V adopts the random decoding order for uplink GTs
instead of optimal policy proposed in Lemma 1.
Additionally, in order to validate the effectiveness of the
RSMA framework in supporting low-altitude MEC systems,
we also design generative diffusion-enhanced algorithms under
different multiple access schemes as baseline approaches:
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3015
TABLE II
SYSTEM PARAMETERS
• GDFD: Generative diffusion-enhanced optimization for
Frequency Division Multiple Access (FDMA)-enabled
low-altitude MEC, where the uplink bandwidth is equally
divided among GTs, ensuring orthogonal transmissions
without inter-user interference.
• GDNO: Generative diffusion-enhanced optimization for
NOMA-enabled low-altitude MEC, where multiple GTs
simultaneously share the same uplink resources via
power-domain superposition coding and successive
interference cancellation at the UA V .
B. Experimental Results
Fig. 3 plots the average reward obtained by GDRS and
the baseline algorithms over training episodes. First, GDRS
converges substantially faster and attains a higher steady-state
reward than all baselines. Specifically, the reward curve of
GDRS rises sharply and stabilizes at a high value after
about 110 training episodes. Furthermore, the proposed GDRS
method outperforms PPORS and DQNRS. This is because
PPORS and DQNRS rely on conventional policy updates that
often become trapped in local optima, while GDRS lever-
ages generative diffusion sampling to better explore feasible
actions. In addition, compared to the method with random
decoding order, GDRS exhibits less fluctuation in its training
curve and achieves a higher average reward, demonstrating that
Fig. 3. The reward curves of the proposed GDRS algorithm and other
baselines for RSMA-enabled LAE MEC systems over training episodes.
Fig. 4. The reward curves of the proposed GDRS algorithm under different
learning rate.
the optimized decoding order enables more effective succes-
sive interference cancellation and higher reward accumulation.
Fig. 4 examines the training reward curves of the proposed
GDRS algorithm under different learning rates. When the
learning rate is set to 5 × 10−4, the training curve achieves
higher reward values compared to those with learning rates
of 1 × 10−4 and 1 × 10−3. This is because a large learning
rate causes excessively large update steps, resulting in unstable
training for the agent. Conversely, a small learning rate leads
to a slow learning process and causes the training to converge
prematurely or get trapped in a local optimum. A learning rate
of 5 × 10−4 strikes a better balance between learning stability
and update efficiency. Therefore, all subsequent experiments
adopt a learning rate of 5 × 10−4.
Fig. 5a investigates how the number of diffusion steps T
affects the achieved average reward under different numbers
of GTs K. First, we observe that the GDRS method with
20 denoising steps outperforms the version with 10 denoising
steps, indicating that increasing the number of denoising
steps helps the DRL agent learn more generalizable fea-
tures, thereby enhancing training generalization. However,
the GDRS method with 30 denoising steps yields a signif-
icantly lower average reward compared to the 20-step case.
This is because an excessive number of denoising steps can
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3016 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 5. (a) The impact of diffusion steps T on average reward under different
number of GTs K. (b) Inference time evaluations of different methods.
Fig. 6. Energy efficiency of different methods versus the number of GTs.
remove valuable features from the data, reducing training
efficiency. Furthermore, as the number of GTs increases, the
average reward under all denoising configurations decreases
noticeably. This is due to the increased UA V flight energy
consumption caused by the larger number of GTs under
a fixed computational capacity, leading to reduced energy
efficiency. Moreover, Fig. 5b illustrates the inference latency
of the proposed GDRS framework under different numbers of
denoising steps. As the number of denoising steps increases,
the inference latency correspondingly grows. Despite this
growth, the inference time of the proposed GDRS remains
within an acceptable sub-second range, which is still feasible
for real-time decision-making in UA V-assisted MEC scenarios.
Fig. 6 compares the energy efficiency of different methods
versus the number of GTs. We find that all methods exhibit
a downward trend as the number of GTs increases. This is
because the addition of GTs introduces more stringent offload-
ing and communication demands, leading to higher UA V
propulsion energy consumption and reduced per-user resource
availability. Moreover, we observe that the proposed GDRS
method consistently achieves the highest energy efficiency
across the entire range of GTs. In particular, the perfor-
mance gap between GDRS and the baseline methods becomes
more pronounced as the network density increases. This is
attributed to the diffusion-guided exploration and adaptive
RSMA decoding, which jointly enable efficient interference
management and resource utilization in dense multiuser sce-
narios. Additionally, it can be seen that GDRS significantly
outperforms GDFD. The main reason is that RSMA with
Fig. 7. Energy efficiency of different methods versus the maximum of
transmit power of each GT.
Fig. 8. Energy efficiency versus the total time slots of UA V under different
multiple access methods.
optimized message splitting and decoding allows for concur-
rent transmissions over shared spectrum resources, whereas
orthogonal allocation in FDMA-like schemes such as GDFD
inevitably suffers from severe spectral inefficiency when the
number of GTs grows.
Fig. 7 compares the energy efficiency of different methods
versus the maximum transmit power of each GT. We find
that all methods exhibit an upward trend as the maximum
transmit power increases. This indicates that granting GTs
higher transmit power generally enables more data bits to
be offloaded and processed, and the growth in data bits
outpaces the increase in UA V energy consumption. Moreover,
we observe that the proposed GDRS method consistently
achieves the highest energy efficiency across the entire power
range, and the performance gap between GDRS and the
baseline methods widens as the number of GTs increases.
This is because its diffusion-guided exploration and optimized
decoding order jointly convert increased transmit power into
higher throughput while mitigating multiuser interference.
Additionally, we can observe that GDRS outperforms GDFD
in terms of energy efficiency. This is because RSMA with
optimized decoding enables concurrent transmissions over
shared bandwidth, whereas orthogonal allocation of FSMA
limits spectral efficiency.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3017
Fig. 9. Energy efficiency of different methods versus the data size of
computation task of each GT.
Fig. 8 evaluates the energy efficiency versus the total
number of time slots under different multiple access schemes.
We compare the proposed RSMA-based system with repre-
sentative NOMA-based scheme and FDMA-based scheme.
First, all schemes exhibit an increase in energy efficiency
as the time horizon expands. Intuitively, with more time
slots, the UA V has greater flexibility to serve the offload-
ing requests in a staggered manner and can fly in a more
energy-conservative trajectory, thereby improving the over-
all energy efficiency. Besides, the RSMA-enabled system
achieves the highest energy efficiency, significantly outper-
forming both the NOMA and OMA cases. As the number
of time slots increases, the energy efficiency gap widens
because RSMA can more fully exploit the extra time to
optimize power allocation and decoding order among users.
Since it still allows concurrent transmissions with SIC, the
NOMA-based system is generally second-best here, but it
suffers from higher interference and less flexible rate allo-
cation than RSMA, resulting in lower efficiency. The OMA
method performs the worst energy-wise due to its poor spec-
tral utilization. By enabling part of the interference to be
treated as useful information, RSMA strikes an advantageous
balance that NOMA and OMA cannot, thus delivering bet-
ter performance especially in high-load or extended-duration
scenarios.
In Fig. 9, we analyze how the energy efficiency of the
various methods varies with the size of computation task of
GT. The plotted results indicate a general upward trend in
energy efficiency as the task size grows. When tasks are very
small, the overhead of coordination and UA V operation is
relatively significant, leading to lower energy efficiency for
all schemes. In this regime, GDRS still maintains a slight
edge over other methods, but overall efficiency is limited
by fixed costs, because its optimized decoding and resource
allocation reduce interference even for small tasks, yet the
coordination and UA V propulsion overhead dominate the
energy budget. As the task size increases, all methods become
more energy-efficient. This is because larger batches of data
can be offloaded and processed in one go, amortizing the
energy cost of UA V trajectory and link setup over more bits.
Notably, the energy efficiency of GDRS method improves
Fig. 10. Energy efficiency of GDRS and PPORS methods versus the
processed rate of UA V under different communication bandwidth.
the most rapidly and to the highest values. And the margin
between GDRS and the others widens with task size, indi-
cating that GDRS scales especially well to heavy workloads.
This is because GDRS method minimizes unnecessary UA V
movement and efficiently multiplexes the uplink transmissions
via RSMA.
Fig. 10 plots the energy efficiency of GDRS versus the
baseline PPORS against the processed rate of UA V under
different bandwidth conditions. First, we observe that increas-
ing the UA V’s processed rate leads to higher energy efficiency
for both GDRS and PPORS. With a faster onboard CPU,
the UA V can execute offloaded tasks more quickly, reduc-
ing the time GTs spend transmitting. With a faster onboard
CPU, the UA V can execute offloaded tasks more quickly,
reducing the time GTs spend on data transmission. Moreover,
the energy efficiency of GDRS consistently surpasses that
of the PPORS method, demonstrating the advantage of the
generative diffusion model in adapting to the complexity of
low-altitude MEC offloading involving mobile UA V . In addi-
tion, under a fixed UA V processed rate, energy efficiency
increases with communication bandwidth. When more band-
width is available, uplink transmissions require less time or
lower power for the same data volume, thereby improving
the energy efficiency. Notably, even under constrained band-
width conditions, GDRS outperforms the baseline, because
the diffusion model enables more effective exploration of the
hybrid action space than PPO, avoiding premature convergence
and yielding better joint optimization of power allocation and
decoding order. Specifically, when the UA V processed rate is
set to 500 cycles/s and the bandwidth to 0.1 MHz, GDRS
improves energy efficiency by approximately 47.3% compared
to PPORS, confirming that whether the bottleneck lies in
computation or communication, GDRS achieves better energy
utilization.
Fig. 11 illustrates the UA V 3D trajectories under differ-
ent methods. We observe that the proposed GDRS method
yields a more structured and energy-aware trajectory that
dynamically adapts to the spatial distribution of GTs, enabling
efficient task offloading while minimizing redundant UA V
motion. In contrast, the trajectories under PPORS and DQNRS
exhibit erratic and less adaptive patterns, reflecting the limited
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3018 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 11. UA V trajectories in 3D space for different methods.
exploration and poor generalization capability of traditional
DRL approaches in high-dimensional hybrid action spaces,
because their action sampling is restricted to local policy
distributions without structured guidance, which leads to pre-
mature convergence and prevents learning globally efficient
UA V trajectories. Additionally, the GDRS-Random method,
which employs a stochastic RSMA decoding order, results in
a degraded trajectory with inefficient hovering and detours,
further highlighting the necessity of the decoding policy
derived in Lemma 1.
V. C ONCLUSION
In this work, we developed an uplink RSMA-enabled
low-altitude MEC framework aimed at enhancing energy effi-
ciency in highly dynamic and interference-limited wireless
environments. By formulating a joint optimization problem
involving UA V three-dimensional trajectory design, user task
offloading, transmit power allocation, and RSMA decod-
ing order, we addressed the fundamental coupling between
computation and communication in airborne edge networks.
To solve this high-dimensional and non-convex problem,
we introduced a GDM-enhanced DRL algorithm, where the
integration of generative sampling within the actor network
significantly improves exploration quality and policy conver-
gence in hybrid action spaces. Moreover, a priority-based
RSMA decoding policy was derived to enable lightweight
and effective interference management through successive
interference cancellation. The simulation results confirmed that
RSMA can flexibly manage multi-user interference and that
diffusion-enhanced exploration provides superior adaptability
to dynamic task and channel variations, enabling UA Vs to
follow energy-aware trajectories while maintaining low com-
putational and communication overhead. In future research,
we will extend our framework toward robust optimization
under imperfect or delayed CSI, consider heterogeneous
mobility patterns of users, and investigate multi-antenna MEC
networks.

## § References

[1] E. Calvanese Strinati et al., “6G: The next frontier: From holographic
messaging to artificial intelligence using subterahertz and visible light
communication,” IEEE Veh. Technol. Mag., vol. 14, no. 3, pp. 42–50,
Sep. 2019.
[2] P. Porambage, J. Okwuibe, M. Liyanage, M. Ylianttila, and T. Taleb,
“Survey on multi-access edge computing for Internet of Things realiza-
tion,” IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 2961–2991, 4th
Quart., 2018.
[3] L. Nadeem et al., “Integration of D2D, network slicing, and MEC in
5G cellular networks: Survey and challenges,” IEEE Access, vol. 9,
pp. 37590–37612, 2021.
[4] Y . Jiang et al., “Integrated sensing and communication for low altitude
economy: Opportunities and challenges,” IEEE Commun. Mag., early
access, Apr. 2025, doi: 10.1109/MCOM.001.2400685.
[5] C. Zhao et al., “Generative AI-enabled wireless communications for
robust low-altitude economy networking,” 2025, arXiv:2502.18118.
[6] S. Jeong, O. Simeone, and J. Kang, “Mobile edge computing via
a UA V-mounted cloudlet: Optimization of bit allocation and path
planning,” IEEE Trans. Veh. Technol., vol. 67, no. 3, pp. 2049–2063,
Mar. 2018.
[7] Y . Mao, O. Dizdar, B. Clerckx, R. Schober, P. Popovski, and
H. V . Poor, “Rate-splitting multiple access: Fundamentals, survey, and
future research trends,” IEEE Commun. Surveys Tuts., vol. 24, no. 4,
pp. 2073–2126, 2022.
[8] X. Wang et al., “Resource allocation and user pairing for rate
splitting multiple access based wireless networked control sys-
tems,” IEEE Trans. Commun., vol. 73, no. 7, pp. 4795–4810,
Jul. 2025.
[9] H. Bastami, H. Behroozi, M. Moradikia, A. Abdelhadi, D. W. K. Ng,
and L. Hanzo, “Large-scale rate-splitting multiple access in uplink UA V
networks: Effective secrecy throughput maximization under limited feed-
back channel,”IEEE Trans. Veh. Technol., vol. 72, no. 7, pp. 9267–9280,
Jul. 2023.
[10] C. Zhang et al., “Multi-objective aerial collaborative secure com-
munication optimization via generative diffusion model-enabled deep
reinforcement learning,” IEEE Trans. Mobile Comput., vol. 24, no. 4,
pp. 3041–3058, Apr. 2025.
[11] C. Fang et al., “DRL-driven joint task offloading and resource allo-
cation for energy-efficient content delivery in cloud-edge cooperation
networks,”IEEE Trans. Veh. Technol., vol. 72, no. 12, pp. 16195–16207,
Dec. 2023.
[12] F. You and H. Du, “ReaCritic: Large reasoning transformer-
based DRL critic-model scaling for heterogeneous networks,” 2025,
arXiv:2505.10992.
[13] H. Du et al., “Enhancing deep reinforcement learning: A tutorial on
generative diffusion models in network optimization,” IEEE Commun.
Surveys Tuts., vol. 26, no. 4, pp. 2611–2646, 2024.
[14] X. Wang et al., “Generative AI enabled matching for 6G multi-
ple access,” IEEE Wireless Commun., early access, Oct. 2025, doi:
10.1109/MWC.2025.3615555.
[15] X. Xu, X. Mu, Y . Liu, H. Xing, Y . Liu, and A. Nallanathan, “Gen-
erative artificial intelligence for mobile communications: A diffusion
model perspective,” IEEE Commun. Mag., vol. 63, no. 7, pp. 98–105,
Jul. 2025.
[16] F. You, H. Du, X. Hou, Y . Ren, and K. Huang, “DRESS: Diffusion
reasoning-based reward shaping scheme for intelligent networks,” 2025,
arXiv:2503.07433.
[17] Z. Yang, S. Bi, and Y .-J.-A. Zhang, “Dynamic offloading and trajectory
control for UA V-enabled mobile edge computing system with energy
harvesting devices,” IEEE Trans. Wireless Commun., vol. 21, no. 12,
pp. 10515–10528, Dec. 2022.
[18] Z. Hu, F. Zeng, Z. Xiao, B. Fu, H. Jiang, and H. Chen, “Computation
efficiency maximization and QoE-provisioning in UA V-enabled MEC
communication systems,” IEEE Trans. Netw. Sci. Eng., vol. 8, no. 2,
pp. 1630–1645, Apr. 2021.
[19] B. Liu, Y . Wan, F. Zhou, Q. Wu, and R. Q. Hu, “Resource allocation and
trajectory design for MISO UA V-assisted MEC networks,” IEEE Trans.
Veh. Technol., vol. 71, no. 5, pp. 4933–4948, May 2022.
[20] Y . Wang, J. Zhu, H. Huang, and F. Xiao, “Bi-objective ant colony
optimization for trajectory planning and task offloading in UA V-
assisted MEC systems,” IEEE Trans. Mobile Comput., vol. 23, no. 12,
pp. 12360–12377, Dec. 2024.
[21] R. Han, Y . Wen, L. Bai, J. Liu, and J. Choi, “Rate splitting on mobile
edge computing for UA V-aided IoT systems,” IEEE Trans. Cognit.
Commun. Netw., vol. 6, no. 4, pp. 1193–1203, Dec. 2020.
[22] J. Kim, E. Hong, J. Jung, J. Kang, and S. Jeong, “Energy minimization
in reconfigurable intelligent surface-assisted unmanned aerial vehicle-
enabled wireless powered mobile edge computing systems with rate-
splitting multiple access,” Drones, vol. 7, no. 12, p. 688, Nov. 2023.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
W ANG et al.: ENERGY-EFFICIENT RSMA-ENABLED LOW-ALTITUDE MEC OPTIMIZATION 3019
[23] J. Chen et al., “Deep reinforcement learning based resource allocation
in multi-UA V-aided MEC networks,” IEEE Trans. Commun., vol. 71,
no. 1, pp. 296–309, Jan. 2023.
[24] H. Pan, B. Lin, Y . Liu, S. Liang, and C. Yuen, “Diffusion-model-
enhanced multiobjective optimization for improving forest monitoring
efficiency in UA V-enabled Internet of Things,”IEEE Internet Things J.,
vol. 12, no. 19, pp. 40980–40996, Oct. 2025.
[25] L. He et al., “Generative AI for game theory-based mobile net-
working,” IEEE Wireless Commun., vol. 32, no. 1, pp. 122–130,
Feb. 2025.
[26] Y . Fu, P. Qin, Y . Wang, L. Chen, M. Li, and X. Zhao, “Over-the-air
edge inference for low-altitude airspace: Generative AI-aided multi-task
batching and beamforming design,” IEEE Trans. Commun., vol. 73,
no. 10, pp. 9013–9027, Oct. 2025.
[27] J. Feng, X. Liu, Z. Liu, and T. S. Durrani, “Optimal trajectory
and resource allocation for RSMA-UA V assisted IoT communica-
tions,” IEEE Trans. Veh. Technol., vol. 73, no. 6, pp. 8693–8704,
Jun. 2024.
[28] H. Bastami, M. Letafati, M. Moradikia, A. Abdelhadi, H. Behroozi,
and L. Hanzo, “On the physical layer security of the cooperative rate-
splitting-aided downlink in UA V networks,” IEEE Trans. Inf. Forensics
Security, vol. 16, pp. 5018–5033, 2021.
[29] Q. Zhou, Y . Liu, H. Feng, and L. Wang, “PRU group allocation and
dynamic rate-splitting design for power minimization in IRS-assisted
UA V MEC systems with RSMA,” IEEE Trans. Green Commun. Netw.,
vol. 9, no. 3, pp. 1398–1413, Sep. 2025.
[30] J. Liu et al., “Optimizing resource allocation for multi-modal semantic
communication in mobile AIGC networks: A diffusion-based game
approach,” IEEE Trans. Cognit. Commun. Netw., vol. 11, no. 5,
pp. 3346–3360, Oct. 2025.
[31] C. Zhao et al., “Temporal spectrum cartography in low-altitude economy
networks: A generative AI framework with multi-agent learning,” 2025,
arXiv:2505.15571.
[32] X. Zhang and J. Yu, “Improve the training efficiency of DRL for wireless
communication resource allocation: The role of generative diffusion
models,” 2025, arXiv:2502.07211.
[33] X. Wang, H. Du, L. Feng, F. Zhou, and W. Li, “Effective throughput
maximization for NOMA-enabled URLLC transmission in industrial IoT
systems: A generative AI-based approach,” IEEE Internet Things J.,
vol. 12, no. 10, pp. 13327–13339, May 2025.
[34] J. Zhang, Z. Liu, X. Feng, H. Yang, and S. Liang, “Enhanced
secure beamforming for IRS-assisted IoT communication using
a generative-diffusion-model-enabled optimization approach,”
IEEE Internet Things J., vol. 12, no. 10, pp. 13398–13414,
May 2025.
[35] J. Wang et al., “A unified framework for guiding generative AI with
wireless perception in resource constrained mobile edge networks,”
IEEE Trans. Mobile Comput., vol. 23, no. 11, pp. 10344–10360,
Nov. 2024.
[36] H. Mei, K. Wang, D. Zhou, and K. Yang, “Joint trajectory-
task-cache optimization in UA V-enabled mobile edge networks for
cyber-physical system,” IEEE Access, vol. 7, pp. 156476–156488,
2019.
[37] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude
for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6,
pp. 569–572, Dec. 2014.
[38] X. Pang, N. Zhao, J. Tang, C. Wu, D. Niyato, and K.-K. Wong,
“IRS-assisted secure UA V transmission via joint trajectory and beam-
forming design,” IEEE Trans. Commun., vol. 70, no. 2, pp. 1140–1152,
Feb. 2022.
[39] S. Han, J. Wang, L. Xiao, and C. Li, “Broadcast secrecy rate maximiza-
tion in UA V-empowered IRS backscatter communications,”IEEE Trans.
Wireless Commun., vol. 22, no. 10, pp. 6445–6458, Oct. 2023.
[40] Y . Du, K. Wang, K. Yang, and G. Zhang, “Energy-efficient resource
allocation in UA V based MEC system for IoT devices,” in Proc. IEEE
Global Commun. Conf. (GLOBECOM), Dec. 2018, pp. 1–6.
[41] Z. Yang, M. Chen, W. Saad, W. Xu, and M. Shikh-Bahaei, “Sum-rate
maximization of uplink rate splitting multiple access (RSMA) commu-
nication,” IEEE Trans. Mobile Comput., vol. 21, no. 7, pp. 2596–2609,
Jul. 2022.
[42] J. Zhu, Y . Huang, J. Wang, K. Navaie, and Z. Ding, “Power efficient IRS-
assisted NOMA,” IEEE Trans. Commun., vol. 69, no. 2, pp. 900–913,
Feb. 2021.
[43] M. Zeng, X. Li, G. Li, W. Hao, and O. A. Dobre, “Sum rate maximiza-
tion for IRS-assisted uplink NOMA,” IEEE Commun. Lett., vol. 25,
no. 1, pp. 234–238, Jan. 2021.
[44] J. Zhang, L. Zhu, Z. Xiao, X. Cao, D. O. Wu, and X.-G. Xia, “Optimal
and sub-optimal uplink NOMA: Joint user grouping, decoding order,
and power control,” IEEE Wireless Commun. Lett., vol. 9, no. 2,
pp. 254–257, Feb. 2020.
[45] M. A. Abd-Elmagid, A. Ferdowsi, H. S. Dhillon, and W. Saad,
“Deep reinforcement learning for minimizing age-of-information in
UA V-assisted networks,” in Proc. IEEE Global Commun. Conf.
(GLOBECOM), Dec. 2019, pp. 1–6.
[46] H. Du et al., “Diffusion-based reinforcement learning for edge-enabled
AI-generated content services,” IEEE Trans. Mobile Comput., vol. 23,
no. 9, pp. 8902–8918, Sep. 2024.
[47] A. Q. Nichol and P. Dhariwal, “Improved denoising diffusion probabilis-
tic models,” in Proc. 38th Int. Conf. Mach. Learn., vol. 139, M. Meila
and T. Zhang, Eds., Jul. 2021, pp. 8162–8171.
[48] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,”
in Proc. Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 6840–6851.
[49] L. Zhao, Z. Fei, J. Huang, X. Wang, B. Li, and W. Yuan, “Deployment
design for multi-UA V-assisted IoT networks: A digital twin-driven deep
reinforcement learning approach,” IEEE Trans. Wireless Commun., early
access, Aug. 2025, doi: 10.1109/TWC.2025.3596864.
[50] Y . Zhao et al., “Joint deployment and resource allocation for multi-AeBS
networks: A two-timescale optimization framework using MADRL,”
IEEE Trans. Commun., vol. 73, no. 6, pp. 4272–4289, Jun. 2025.
[51] C. Liu, Y . Zhong, R. Wu, S. Ren, S. Du, and B. Guo, “Deep rein-
forcement learning based 3D-trajectory design and task offloading in
UA V-enabled MEC system,”IEEE Trans. Veh. Technol., vol. 74, no. 2,
pp. 3185–3195, Feb. 2025.
[52] T. Zhang, K. Zhu, S. Zheng, D. Niyato, and N. C. Luong, “Trajectory
design and power control for joint radar and communication enabled
multi-UA V cooperative detection systems,” IEEE Trans. Commun.,
vol. 71, no. 1, pp. 158–172, Jan. 2023.
Xudong Wang received the B.Eng. degree from the
School of Electronic and Information Engineering,
Beijing Jiaotong University, Beijing, China, in 2021.
He is currently pursuing the Ph.D. degree with the
State Key Laboratory of Networking and Switch-
ing Technology, Beijing University of Posts and
Telecommunications, Beijing. His current research
interests include low-altitude networks, wireless net-
worked control, interference management in wireless
networks, and generative AI.
Hongyang Du (Member, IEEE) received the B.Eng.
degree from Beijing Jiaotong University, China,
and the Ph.D. degree from Nanyang Technological
University, Singapore. He is currently an Assistant
Professor with the Department of Electrical and
Electronic Engineering, The University of Hong
Kong, where he directs the Network Intelligence
and Computing Ecosystem (NICE) Laboratory. His
research interests include edge intelligence, gen-
erative AI, and network management. He was a
recipient of the IEEE ComSoc Young Professional
Award for Best Early Career Researcher in 2024, the IEEE Daniel E. Noble
Fellowship Award from the IEEE Vehicular Technology Society in 2022, the
IEEE Signal Processing Society Scholarship from the IEEE Signal Processing
Society in 2023, and Singapore Data Science Consortium (SDSC) Dissertation
Research Fellowship in 2023. He serves as the Editor-in-Chief Assistant
(2022–2024) and an Editor (-2025) for IEEE C OMMUNICATIONS SURVEYS
AND TUTORIALS ; an Editor for IEEE T RANSACTIONS ON COMMUNICA -
TIONS , IEEE T RANSACTIONS ON VEHICULAR TECHNOLOGY , and IEEE
OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY ; and the Guest Editor
for IEEE Vehicular Technology Magazine.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply. 
3020 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Lei Feng (Member, IEEE) received the B.Eng. and
Ph.D. degrees in communication and information
systems from BUPT in 2009 and 2015, respec-
tively. From 2015 to 2018, he was a Post-Doctoral
Research Fellow of computer science with the
State Key Laboratory of Networking and Switching
Technology, BUPT. He is currently an Associate
Professor with the School of Computer Science,
BUPT. He has co-authored about 80 technical
peer-reviewed papers published in academic journals
and conferences, including IEEE Communications
Magazine, IEEE Wireless Communications Magazine, IEEE T RANSAC -
TIONS ON BROADCASTING , IEEE T RANSACTIONS ON COMPUTERS , IEEE
TRANSACTIONS ON VEHICULAR TECHNOLOGY , IEEE Network, and IEEE
WIRELESS COMMUNICATIONS . His research interests include resource man-
agement in wireless networks, signal processing, and integrated sensing
and communication in smart grid. He was a recipient of the 2022 IEEE
International Conference on Communications (IEEE ICC 2022) Best Paper
Award.
Kaibin Huang (Fellow, IEEE) received the B.Eng.
and M.Eng. degrees in electrical engineering from
the National University of Singapore and the Ph.D.
degree in electrical engineering from The University
of Texas at Austin. He is currently a Philip K. H.
Wong Wilson K. L. Wong Professor of electrical
engineering and the Department Head of the Depart-
ment of Electrical and Electronic Engineering, The
University of Hong Kong (HKU), Hong Kong. He is
a fellow of the U.S. National Academy of Inventors.
He was an IEEE Distinguished Lecturer. His work
was recognized with seven best paper awards from the IEEE Communication
Society. He is a member of the Engineering Panel of Hong Kong Research
Grants Council (RGC) and a RGC Research Fellow (2021 Class). He has
served on the editorial boards of five major journals in the area of wireless
communications and co-edited ten journal special issues. He has been active in
organizing international conferences, such as the 2014, 2017, and 2023 Edi-
tions of IEEE Globecom, a flagship conference in communication. He has
been named as a Highly Cited Researcher by Clarivate from 2019 to 2024 and
an AI 2000 Most Influential Scholar (Top 30 in the Internet of Things)
from 2023 to 2024.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:06:52 UTC from IEEE Xplore.  Restrictions apply.
