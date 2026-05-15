---
paper_id: "paper-2700"
source_pdf_sha: "62d5c2718168b862466a8db14d580fd3fcafb6c27e7360b320d303d1b26c8127"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 2
  page_count: 14
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2700 — fulltext
## §unknown-1

IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026 5281
Large Language Model-Empowered
Energy-Efficient Multi-UA V-Assisted
MEC Heterogeneous Networks
Ke Lv
 , Student Member , IEEE, Sai Huang
 , Senior Member , IEEE, Yuanyuan Yao
 , Member , IEEE,
Weiwei Jiang
 , Senior Member , IEEE, and Zhiyong Feng
 , Senior Member , IEEE
Abstract— The artificial general intelligence (AGI) based on
large language models (LLMs) and deep reinforcement learn-
ing (DRL) possesses cross-domain empowerment capabilities,
offering task scheduling and resource allocation in mobile edge
computing (MEC), presenting significant potential. This paper
proposes an LLM-driven DRL framework named L2D2, which
autonomously generates reward functions for DRL through
LLMs and enables dynamic model optimization through a
self-refinement loop mechanism. The reward function within the
L2D2 framework can adjust the strategy based on environmental
feedback, eliminating the need for manual redesign in complex
low-altitude scenarios and reducing debugging costs. To validate
the performance of L2D2, the framework is utilized in a
multi-unmanned aerial vehicle (UA V)-assisted MEC heteroge-
neous network operating in the low-altitude airspace to enhance
system energy efficiency. A novel dueling double deep Q-network
(D3QN) is utilized as the DRL method within L2D2, named the
L2D2-D3QN algorithm. To evaluate its effectiveness in enhancing
system energy efficiency, a comprehensive comparison is con-
ducted across various LLMs, including Deepseek-R1, GPT-4o,
Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-2.5. The simula-
tion results demonstrate that the L2D2-D3QN algorithm achieves
up to 56% higher energy efficiency compared to DRL with
human-designed reward function. Furthermore, the influence of
LLM tokenization strategies on the performance of LLM-driven
DRL is also explored.
Index Terms— Artificial general intelligence, large language
model, deep reinforcement learning, unmanned aerial vehicle,
mobile edge computing.
I. I NTRODUCTION
T
HE
low-altitude economy, defined as an economic
paradigm operating within 100 to 1000 meters above
ground, has emerged as a strategic industry, attracting
Received 6 May 2025; revised 4 September 2025 and 30 October 2025;
accepted 7 December 2025. Date of publication 17 December 2025; date
of current version 28 January 2026. This work was supported in part by
the National Natural Science Foundation of China under Grant (62422103,
62321001, 62171045, 62201090). The associate editor coordinating the review
of this article and approving it for publication was J. Wang. (Corresponding
author: Sai Huang.)
Ke Lv, Sai Huang, Weiwei Jiang, and Zhiyong Feng are with the Key
Laboratory of Universal Wireless Communications, Ministry of Educa-
tion, Beijing University of Posts and Telecommunications, Beijing 100876,
China (e-mail: kelv@bupt.edu.cn; huangsai@bupt.edu.cn; jww@bupt.edu.cn;
fengzy@bupt.edu.cn).
Yuanyuan Yao is with the Key Laboratory of Information and Communi-
cation Systems, Ministry of Information Industry, and the Key Laboratory of
Modern Measurement and Control Technology, Ministry of Education, Beijing
Information Science and Technology University, Beijing 100101, China
(e-mail: yyyao@bistu.edu.cn).
Digital Object Identifier 10.1109/TCCN.2025.3645407
widespread global attention. With line-of-sight (LoS) commu-
nication links and high mobility, the unmanned aerial vehicle
(UA V) has emerged as a central enabling technology for the
low-altitude economy [1], [2], [3]. By 2030, it is projected that
the commercial UA V sector will reach a value of $260 billion,
driving the rapid evolution of low-altitude airspace into a vital
third dimension for digital infrastructure supporting logistics,
agriculture, and public safety [4]. However, constructing and
efficiently operating this new infrastructure fundamentally
depends on reliable and scalable communication capabilities,
which are essential for ensuring connectivity and facilitating
data exchange among various systems and users.
To overcome the computing and transmission bottlenecks
in low-altitude communication scenarios, UA V-assisted mobile
edge computing (MEC) has emerged [5]. Unlike conven-
tional cloud-centric architectures, UA V-assisted MEC deploys
computational nodes directly on aircraft, alleviating the com-
putational pressure on core network [6]. By enhancing task
processing efficiency and optimizing network resource uti-
lization, it has become a vital technical solution driving the
development of this field. This innovative approach facilitates
a variety of applications, including real-time video monitoring,
delivery drones, and smart agricultural management, advanc-
ing the development of the low-altitude economy [7], [8], [9].
A. Related Works
In the low-altitude UA V-assisted MEC systems, the limited
flight endurance of UA Vs critically constrain system opera-
tional duration, making energy consumption a crucial factor
in determining overall performance sustainability. To achieve
a balance between maximizing system throughput and min-
imizing overall energy consumption, energy efficiency has
emerged as a fundamental metric. To maximize energy effi-
ciency, Li et al. [10] employed the Dinkelbach algorithm and
successive convex approximation (SCA) method to jointly
optimize user transmit power, two-dimensional (2D) UA V
trajectory, and computational load allocation. Qin et al. [11]
introduced a reconfigurable intelligent surface (RIS) into
UA V-assisted MEC systems and developed a double-loop
iterative algorithm to maximize system energy efficiency.
To maximize the energy efficiency of an RIS-assisted UA V-
enabled MEC system with non-orthogonal multiple access
(NOMA) protocol, Qin et al. [12] employed block coordinate
descent (BCD) method along with the Dinkelbach algorithm.
2332-7731 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence
and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5282 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Similarly, Liu et al. [13] explored the UA V-assisted NOMA-
MEC architecture, utilizing the SCA method and Dinkelbach
algorithm to maximize energy efficiency. Qian et al. [14]
assumed the presence of eavesdroppers in the environment and
aimed to maximize system energy efficiency by optimizing the
2D UA V trajectory, UA V transmit power, local computation
ratio, and terminal scheduling.
As the complexity of system models increases, the analytical
solution of objective functions faces significant challenges.
Conventional optimization algorithms exhibit notable limita-
tions in terms of computational efficiency, convergence, and
solution quality. Fortunately, the emerging deep reinforcement
learning (DRL) provides an innovative solution to this prob-
lem. DRL combines deep learning (DL) with reinforcement
learning (RL) to enable agents to learn optimal strategies
in complex environments through trial-and-error mechanisms
and reward feedback [15], [16], [17]. With this capabil-
ity, DRL can be effectively employed to optimize resource
allocation in MEC. Li et al. [18] utilized Q-learning from
RL to achieve dynamic coordination among heterogeneous
UA Vs, providing better services for internet of things (IoT)
devices with different tasks. Compared to existing RL algo-
rithms, Zhang et al. [19] employed deep Q-learning network
(DQN) from DRL to jointly optimize multi-UA V trajecto-
ries, power allocation, and video-level selection, achieving
maximum energy efficiency. Furthermore, Wu et al. [20]
optimized resource allocation in MEC, joint control of UA Vs,
and passive beamforming through double deep Q-learning
network (DDQN) to maximize the system energy efficiency.
Considering three-dimensional (3D) multi-UA V trajectories,
Liu et al. [21] employed DDQN and convex optimization
techniques to develop near-optimal multi-UA V trajectories
and task offloading strategies, resulting in improved energy
efficiency.
B. Contributions
The core elements of the aforementioned works are summa-
rized in Table I. Related works [10], [11], [12], [13], [14], [18],
[19], and [20] restrict UA V to 2D space, failing to explore the
full potential of UA V in 3D environments. Additionally, related
works [10], [11], [12], [13], [19], [20], and [21] focus solely on
single UA V scenarios, neglecting the collaborative capabilities
of multi-UA V . The traditional optimization methods employed
in [10], [11], [12], [13], and [14] have significant limitations,
making it challenging to address more complex problems.
Although works [19], [20], [21] utilize DQN and DDQN,
challenges such as overestimation and unstable convergence
persist. In fact, the quality of the reward function design is
crucial to the training effectiveness of DRL. An unreasonable
reward value design can negatively impact the learning effi-
ciency of the agent. The increasing complexity of network
structures presents significant challenges in designing reward
functions.
The anticipated emergence of artificial general intelligence
(AGI) is expected to achieve significant breakthroughs in
addressing the above problems in the future. The breakthrough
in language comprehension and generation capabilities repre-
sents a critical milestone in achieving AGI, which is exactly
the value of large language models (LLMs) [22], [23]. As one
of the foundational technologies supporting AGI development,
LLMs not only master the complex grammatical structure
of human language through deep training of massive text
data, but also establish a knowledge network architecture
comprising trillions of parameters [24], [25], [26]. This prob-
abilistic reasoning based network enables machines to capture
semantic associations, deconstruct logical relationships, and
even demonstrate elementary common sense reasoning capa-
bilities. Therefore, this capability of LLMs is well-suited
for addressing the design of reward functions in complex
MEC networks. To the best of our knowledge, there is less
works on leveraging DRL with LLM-designed rewards to
achieve resource allocation in MEC. The progress of mod-
els such as GPT-4, Llama, and DeepSeek marks a critical
moment in which artificial intelligence (AI) systems have
reached near-human levels in language interaction, laying
a significant foundation for the development of AGI with
general cognitive capabilities. To explore AGI, we propose
an LLM-driven DRL framework and implement it within the
low-altitude economy to verify its performance. The future
mobile communication and computing environments are inher-
ently heterogeneous, with user equipment having different
energy states and quality of service (QoS) requirements [27].
Therefore, this work considers a multi-UA V-assisted MEC
heterogeneous network that includes human-type users as well
as constrained application protocol (CoAP)-based IoT devices.
The focus is on optimizing the 3D trajectories of multi-UA Vs
and user association factors to maximize system energy effi-
ciency. The main contributions of this paper are summarized as
follows:
• A novel LLM-driven DRL framework, termed L2D2,
is proposed that autonomously generates dynamic reward
functions through semantic understanding of network
states. To the best of our knowledge, this work estab-
lishes the first LLM-based reward designing into wireless
resource allocation for MEC, effectively addressing the
limitations of manual reward engineering in complex
low-altitude environments. A closed-loop self-refinement
mechanism is designed that leverages the synergy
between real-time performance evaluation and parameter
correction, facilitating the continuous evolution of the
algorithm.
• This work experimentally investigates the tokenization
mechanism of LLMs for prompts and their effects on
decision-making performance in DRL. Focusing on the
mainstream LLM architectures, including DeepSeek-R1,
GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-
2.5, the tokenizers are evaluated based on the number of
tokens segmented from prompts. The impact of reward
functions generated by various LLMs on DRL training is
further analyzed.
• The L2D2 framework innovatively integrates dueling
double deep Q-network (D3QN) with LLM, termed the
L2D2-D3QN algorithm, effectively overcoming the inher-
ent overestimation and unstable convergence associated
with traditional DQN and DDQN. Moreover, comprehen-
sive experiments are designed to explore the capabilities
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5283
TABLE I
RELATED WORK ON UAV-ASSISTED MEC
of LLM-driven DRL. Compared to the DRL based on
human-designed reward function, the LLM-driven DRL
can provide up to a 56% improvement in system energy
efficiency.
The rest of this paper is organized as follows. Section II
describes the system model for multi-UA V-assisted MEC
heterogeneous network. Building upon this foundation,
Section III formulates the energy efficiency optimiza-
tion problem with multiple constraints. Section IV fur-
ther describes the proposed L2D2 framework and L2D2-
D3QN algorithm. Simulation results and analysis are pre-
sented in Section V, followed by the conclusions in
Section VI.
II. S YSTEM MODEL
The system model of multi-UA V-assisted MEC heteroge-
neous network is depicted in Fig. 1, where U cognitive UA Vs
assist M human-type users as well as N IoT devices based
on CoAP for MEC. For human-type users, the UA V can
directly compute the tasks, while for IoT devices, the UA V
requires AMC before computation. In addition, these devices
have different computing demands, which are represented by
Dm and Dn respectively. vh
u,t and vv
u,t are defined as the
horizontal and vertical flight speeds of the UA Vu at time slot t,
respectively. The 3D spatial coordinate positions of IoT device
n, human-type user m, and UA Vu at time slot t are defined by
Qn,t
∆
= ( xn,t, yn,t, 0), Qm,t
∆
= ( xm,t, ym,t, 0), and QUAV
u,t
∆
= 
xUAV
u,t , yUAV
u,t , HUAV
u,t

, where n ∈ N = {1, 2, 3 . . . N}, m ∈
M = {1, 2, 3 . . . M}, t ∈ T = {1, 2, 3 . . . T}, and HUAV
u,t
denotes the altitude of UA V u at time slot t, u ∈ U =
{1, 2, 3 . . . U}. The mission can be terminated once UA Vs
fulfill the computing demands of all IoT devices and human-
type users.
A. Signal Transmission Model
Considering the existence of ground obstacles, the likeli-
hood of the LoS link between the IoT device n and the UA V
Fig. 1. Multi-UA V-assisted MEC heterogeneous network.
u remains unblocked at the time slot t is modeled below [28]:
P UB
u,n,t = 1
1 + a
r
−b

arctan
 H UA V
u,t
du,n,t

− a
 , (1)
where du,n,t represents the Euclidean distance between the IoT
device n and the UA Vu at time slot t. The parameters a and b,
which are environment-specific, are derived from [28]. Like-
wise, the likelihood of the LoS link between the human-type
user m and the UA V u being unblocked at the time slot t is
P UB
u,m,t = 1
1 + a
r
−b

arctan
 H UA V
u,t
du,m,t

− a
 , (2)
where du,m,t denotes the Euclidean distance between the
human-type user m and the UA Vu at time slot t. The channel
gain from the IoT device n to the UA V u at time slot t is
denoted by hu,n,t, and hu,m,t represents the channel gain from
the human-type user m to the UA V u at time slot t [29]:
hu,n,t
∆
= α1(du,n,t)−2= α1


QUAV
u,t − Qn,t


2 , (3)
hu,m,t
∆
= α1(du,m,t)−2= α1


QUAV
u,t − Qm,t


2 , (4)
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5284 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
where α1 corresponds to the received power at a 1-meter
reference distance for a 1 W transmit power. Consequently,
the uplink data rate between the IoT device n to the UA V u
at time slot t can be expressed as
Ru,n,t = αu,n,tP UB
u,n,tP CC
u,n,tW log2

1 + Pnhu,n,t
W σ2

, (5)
where αu,n,t represents the association factor between the IoT
device n and the UA Vu at time slot t, taking values in {0, 1}.
P CC
u,n,t indicates the probability that the signal modulation of
the IoT device n can be correctly recognized by the UA V
u at time slot t, Pn denotes the transmit power of the IoT
device n, σ2 denotes the power density of additive white
Gaussian noise, and W represents the bandwidth. The adoption
of connectionless user datagram protocol (UDP) effectively
reduces communication overhead, enhancing the applicability
of CoAP-based IoT devices [30]. This enables IoT devices
to transmit signals utilizing various modulation techniques.
The RepCCNet has demonstrated impressive performance in
AMC [31]. Thus the RepCCNet is integrated into UA Vs to
enhance their cognitive capabilities. For human-type users
with uniform signal modulation, AMC is not required to be
implemented by UA Vs. Consequently, the data transmission
rate between the user m and the UA Vu at time slot t can be
expressed as
Ru,m,t = αu,m,tP UB
u,m,tW log2

1 + Pmhu,m,t
W σ2

, (6)
where αu,m,t takes values in {0, 1} to indicate the association
factor between the human-type user m and the UA Vu at time
slot t. Additionally, Pm denotes the transmit power of the
human-type user m.
B. Energy Consumption Model
In time slot t, the amount of tasks that the UA Vu is required
to handle can be expressed as
Du,t = min
 MX
m=1
NX
n=1
 
αu,m,tDR
m,t + αu,n,tDR
n,t

,
MX
m=1
NX
n=1
(αu,m,tRu,m,tτ + αu,n,tRu,n,tτ)
!
, (7)
where τ denotes the duration of each time slot. Additionally,
DR
m,t and DR
n,t indicate the remaining computing demands
for the human-type user m and the IoT device n, respectively.
Furthermore, the energy consumption of the central processing
unit (CPU) for the UA V u at time slot t is defined as
ECPU
u,t = κ
 
fCPU
u
3
· min

τ, Du,tCCPU
u
fCPUu

, (8)
where fCPU
u denotes the CPU frequency, CCPU
u refers to
the number of CPU cycles needed to process a single bit of
data, and κ is a factor that depends on the effective switched
capacitance of the CPU architecture. For the UA Vu, the flight
energy consumption at time slot t is
EUAV
u,t =
 
Pbla
 
1 + 3
 
vh
u,t
2
U2
tip
!
+ 1

## §2 Gρsd0

 
vh
u,t
3
+ Pind


s
1 +
 
vh
u,t
4
4v4
0
−
 
vh
u,t
2
2v2
0


1
2
+ Pd/avv
u,t

 τ,
(9)
where Pd/a denotes the constant power for ascending or
descending. Pbla and Pind represent the constant blade profile
power and the induced power during hovering, respectively.
Utip is the tip speed of rotor blade, and v0 indicates the average
induced velocity of the rotor during hovering. The parameters
G and ρ denote the rotor disc area and the air density,
respectively. Additionally, s and d0 represent the rotor solidity
and fuselage drag ratio, respectively [32]. Therefore, the total
system energy consumption at time slot t is formulated as
ESUM
t =Pmτ + Pnτ +
UX
u=1
 
EUAV
u,t + ECPU
u,t

, (10)
where Pm and Pn respectively characterize the transmit power
of human-type users and IoT devices.
III. P ROBLEM FORMULATION
Based on the analysis above, the system energy efficiency
for each time slot t can be derived as
ηEE
t =
UP
u=1
 NP
n=1
Ru,n,t +
MP
m=1
Ru,m,t

ESUM
t
. (11)
Since the objective is to maximize the average energy
efficiency of the system, the optimization problem P1 is
formulated as:
P1 : max ηEE
ave =
TP
t=1
ηEE
t
T (12)
s.t. v h
u,t ≤ vh
max, ∀u ∈ U , t ∈ T , (12a)
vv
u,t ≤ vv
max, ∀u ∈ U , t ∈ T , (12b)
xmin ≤ xu,t ≤ xmax, ∀u ∈ U , t ∈ T , (12c)
ymin ≤ yu,t ≤ ymax, ∀u ∈ U , t ∈ T , (12d)
zmin ≤ zu,t ≤ zmax, ∀u ∈ U , t ∈ T , (12e)
αu,m,t = {0, 1} , ∀u ∈ U , m ∈ M, t ∈ T , (12f)
αu,n,t = {0, 1} , ∀u ∈ U , n ∈ N , t ∈ T , (12g)
0 ≤ αu,m,t + αu,n,t ≤ 1, ∀u ∈ U , n ∈ N , t ∈ T ,
(12h)
TX
t=1
τ Ru,m,t ≥ Dm, ∀u ∈ U , m ∈ M, t ∈ T , (12i)
TX
t=1
τ Ru,n,t ≥ Dn, ∀u ∈ U , n ∈ N , t ∈ T , (12j)
where constraints (12a) and (12b) limit the flight speed of
each UA V in the horizontal and vertical directions, con-
straints (12c) to (12e) limit the 3D coordinates of each UA V ,
constraints (12f) and (12g) represent the allocation factors,
constraint (12h) restricts each UA V to communicate with only
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5285
one object within a time slot. Constraints (12i) and (12j) indi-
cate that the system needs to satisfy the computing demands of
all IoT devices and human-type users during total time slots.
IV. P ROPOSED L2D2 F RAMEWORK AND L2D2-D3QN
ALGORITHM
To advance the exploration of AGI, we integrate LLM with
DRL and propose an LLM-driven DRL framework termed
L2D2. The fundamental component of the L2D2 is self-
refinement loop, as depicted in Fig. 2. The flow of the L2D2
is outlined as follows:
I) Initial input: The initial prompt serves as the input for
LLM, containing a description of the environment in
which the agents operate as well as the tasks.
II) Initial reward function: The LLM generates the initial
reward function based on the initial prompt. At this stage,
the reward function includes system resource variables
(x1, x2) as well as weights (α , β).
III) Parameter prompt: To obtain the initial values of the
weights for the reward function, the parameter prompt
is input into the LLM. This prompt contains specific
values for the environmental variables, providing reliable
references for the LLM to calculate the weights of the
reward function.
IV) Reward function: The LLM provides the weights for the
reward function based on the parameter prompt (α = 0.2,
β = 1.5). At this point, the reward function no longer
includes variables unrelated to the environment in which
the agents operate.
V) Training: The DRL is trained utilizing the reward func-
tion provided by the LLM.
VI) Result: The results of the DRL are assessed by human
experts or the LLM. If the results meet the criteria
for satisfaction, they are considered the final output;
otherwise, the results are documented in the feedback
prompt.
VII) Feedback prompt: The feedback prompt outlines the
results of the DRL and is utilized to provide feedback
to the LLM, facilitating the fine-tuning of the weights in
the reward function.
VIII) Reward function fine-tuning: After receiving the feed-
back prompt, the LLM adjusts the weights within the
reward function, thereby generating an updated reward
function.
IX) Final output: The final output includes the ultimate
reward function, the system resource allocation strategy,
and the results.
Based on the L2D2 framework, we designed the L2D2-
D3QN algorithm, which utilizes D3QN as the DRL in L2D2.
The following subsections will introduce D3QN, the reward
design process utilizing LLM, and the algorithmic flow of
L2D2-D3QN.
A. D3QN
To effectively present the D3QN framework, we start by
providing a concise overview of DRL fundamentals. As a
foundational RL methodology, Q-learning tackles the chal-
lenge of identifying optimal policies within Markov decision
processes (MDPs) frameworks. This algorithm operates by
iteratively estimating the state-action value function Q(st, at),
which enables agents to determine optimal action selections
through direct experience interactions. Crucially, the approach
eliminates the need for explicit environmental dynamics
knowledge, including transition probabilities or reward mech-
anisms. The formula of Q(st, at) is expanded to
Q(st, at) = rt + γ · rt+1
+ . . . + γT −t−1 · rT −1, 0 ≤ t ≤ T − 1, (13)
where rt is the immediate reward at time slot t, and γ ∈ [0, 1]
is a decay factor used to balance the importance of current
rewards and future rewards. The objective of Q-learning is to
identify a strategy π that maximizes the cumulative discounted
reward after the agent takes action at in any given state st, with
the optimal state-action value function Q∗(st, at) is denoted
as
Q∗(st, at) = max Q(st, at). (14)
Moreover, it satisfies the Bellman optimality equation:
Q∗(st, at) = rt + γ · max
at+1∈A
Q∗(st+1, at+1). (15)
Q-learning iteratively updates the value of Q(st, at) through
the temporal difference method, gradually approaching
state-action value function Q∗(st, at):
Q(st, at) =
Q(st, at)+¯α ·

rt+ max
at+1∈A
Q(st+1, at+1) − Q(st, at)

,
(16)
where ¯α is the learning rate. However, when the state and
action spaces are large, storing and updating the Q-table
becomes inefficient, as the memory and computation require-
ments grow exponentially with the dimensionality of the
problem. This limitation, known as the curse of dimensionality,
makes traditional Q-learning incapable of handling complex
tasks. To overcome these challenges, DQN were developed,
combining Q-learning with deep neural networks (DNNs) to
approximate the Q-function. By leveraging the representa-
tional power of neural networks, DQN can efficiently handle
high-dimensional state spaces and learn directly from raw
input data, enabling breakthroughs in complex tasks. The
DQN has the capability of experience replay, allowing it
to store historical experiences (st, at, rt, st+1) in a replay
buffer. During training, DQN randomly samples from this
buffer, breaking data correlation. The DQN consists of two
networks: an estimation network with weights Θ and a target
network with weights Θ−. The estimation network computes
Q(st, at |Θ), which is employed to approximate Q(st, at).
Throughout training, only Θ are updated by minimizing the
loss function:
L(Θ) =

yDQN
t − Q (st, at |Θ)
2
, (17)
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5286 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 2. The flowchart of the L2D2 framework.
yDQN
t = rt + max
at+1∈A
Q(st+1, at+1


Θ− ), (18)
where yDQN
t represents the target value, and Θ is copied
to Θ− every O steps. However, the max operator employed
by the DQN to compute the target Q-value, leading to a
overestimation of Q-values. This in turn affects the perfor-
mance and stability of the policy. To tackle this issue, DDQN
was proposed, which decouples action selection from Q-value
estimation, significantly reducing the overestimation bias and
thereby improving the robustness and convergence efficiency
of the algorithm. The target action in DDQN is chosen by the
estimation network, whereas the target Q-value is evaluated
by the target network. The loss function L(Θ) is defined as:
L(Θ) =

yDDQN
t − Q (st, at |Θ)
2
, (19)
yDDQN
t = rt + γQ
 
st+1, arg max
at+1∈A
Q(st+1, at+1 |Θ)


Θ−
!
.
(20)
By decoupling action selection from Q-value estimation,
DDQN alleviates the overestimation issue in DQN. Neverthe-
less, estimating Q(st, at) for all actions in state st employing
DQN or DDQN can still result in unstable convergence.
D3QN is an enhanced variant of DDQN, built upon the
dueling network architecture to separate the state value and
action advantage functions. Additionally, it incorporates dou-
ble Q-learning to mitigate the overestimation of Q-values.
The architecture of D3QN is illustrated in Fig. 2. Initially,
the input parameters are extracted from the replay buffer of
size F and fed into the input layer. After passing through a hid-
den layer composed of DNNs, relevant features are processed
into two distinct streams. One stream corresponds to the state
value, which is independent of the action chosen by the agent
and solely dependent on the current state st. The output of this
stream indicates the value of the current environment, referred
to as the state value function V (st), which is utilized to
evaluate the performance of the agent within that environment.
The other stream signifies the advantage of selecting action at
in state st, known as the action advantage function A(st, at).
This function evaluates the relative advantage of the agent
when selecting an action from A and assesses the significance
of action at in state st. These streams are represented as
V (st



Θ, ˜β ) and A(st, at |Θ, ˜α), where Θ, ˜α, and ˜β, represent
the parameters for the hidden layer (DNNs), the state value
function network, and the action advantage function network,
respectively.
In contrast to the DQN and the DDQN, the D3QN learns
the value and advantage components independently before
combining them for the final output. This output Q(st, at)
is expressed as Q(st, at



Θ, ˜α, ˜β ), and calculated by the fol-
lowing formula:
Q(st, at



Θ, ˜α, ˜β ) = V (st



Θ, ˜β )
+

A(st, at |Θ, ˜α) − 1
|A|
X
at+1∈A
A (st, at+1 |Θ, ˜α)

 ,
(21)
where |A| represents the dimension of the action space A.
Subtracting the mean of A(st, at |Θ, ˜α) ensures the identifia-
bility of the action advantage function, avoiding redundancy
between V (st



Θ, ˜β ) and A(st, at |Θ, ˜α). Moreover, this sep-
aration mitigates the risk of overestimation biases that can
occur when combining the two functions. By ensuring that
A(st, at |Θ, ˜α) is identifiable, D3QN can more accurately
evaluate the potential advantages of actions without conflating
them with the overall state value. The loss function for D3QN
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5287
is defined as follows:
L(Θ, ˜α, ˜β) =

yD3QN
t − Q

st, at




Θ, ˜α, ˜β
2
, (22)
yD3QN
t = rt+
γQ
 
st+1, arg max
at+1∈A
Q

st+1, at+1




Θ, ˜α, ˜β



Θ−, ˜α−, ˜β−
!
,
(23)
where Θ−, ˜α−, and ˜β−, are the parameters of the target net-
work used to estimate the updates for the periodic replications
of Θ, ˜α, and ˜β within the network.
In the multi-UA V-assisted MEC heterogeneous network,
each UA V u is regarded as an agent. The state su,t,
action au,t, and reward function rt are defined as
follows.
• State su,t: At time slot t, the system state su,t ∈ S
encompasses multiple observations that describe the envi-
ronment. These observations include the 3D coordinates
of the UA V u, the horizontal and vertical flight speeds
of the UA V u, the association factor between the UA V
u and the human-type user m, the association factor
between the UA V u and the IoT device n, the blocking
probability of the LoS link between the UA V u and the
human-type user m, the blocking probability of the LoS
link between the UA V u and the IoT device n, and the
probability that the UA V u can correctly recognize the
signal modulation of the IoT device n. Consequently,
the state space for the agent u at time slot t is defined
as
su,t =

xUAV
u,t , yUAV
u,t , HUAV
u,t , vh
u,t, vv
u,t ,
αu,m,t, αu,n,t, PBP
u,m,t, PBP
u,n,t, PCC
u,n,t
	
. (24)
• Action au,t: The UA Vu selects action au,t based on state
su,t, which comprises six components:
1. The adjustment of horizontal flight speed for the UA V
u, denoted as ∆vh
u,t ∈ {vb, −vb, 0}, where vb represents
the speed variation per time slot.
2. The adjustment of vertical flight speed for the UA V u,
denoted as ∆vv
u,t ∈ {vb, −vb, 0}.
3. The horizontal movement action of
the UA V u, denoted as ∆Lu,t ∈ 
vh
u,tt, 0

,
 
−vh
u,tt, 0

,
 
0, vh
u,tt

,
 
0, −vh
u,tt

, (0, 0)
	
.
4. The vertical movement action of the UA V u, denoted
as ∆Hu,t ∈

vv
u,tt, −vv
u,tt, 0
	
.
5. Selection of association factor between the UA Vu and
the human-type user m, denoted as αu,m,t ∈ {0, 1}.
6. Selection of association factor between the UA Vu and
the IoT device n, denoted as αu,n,t ∈ {0, 1}.
• Reward rt: The reward for UA Vs at time slot t is
determined by the LLM, which will be elaborated upon
in the subsequent section.
B. LLM-Empowered Reward Design
When employing LLM for reward function designing, a crit-
ical initial step involves enabling the LLM to comprehend the
environment and tasks associated with the agents. To achieve
Fig. 3. Initial prompt.
this fundamental understanding, the initial prompt provided
to the LLM incorporates comprehensive descriptions of both
the environmental variables and mission objectives, as visually
outlined in Fig. 3. This initial prompt ensures that the LLM
establishes appropriate contextual awareness before commenc-
ing reward function development. After obtaining the initial
reward function, it is essential to further refine the weight
values. Taking Deepseek-R1 as an example, after receiving
the initial prompt word, it generates the following reward
function:
RDS
t = ηEE
t − λ1P DS
speed − λ2P DS
bounds − λ3P DS
task,
P DS
speed =
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vv
u,t − vv
max

+ max
 
0, vh
min − vh
u,t

+ max
 
0, vv
min − vv
u,t

,
P DS
bounds =
UX
u=1
(max (0, xu,t − xmax) + max (0, xmin − xu,t)
+ max (0, yu,t − ymax) + max (0, ymin − yu,t)
+ max (0, zu,t − zmax) + max (0, zmin − zu,t)) ,
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5288 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 4. Parameter prompt and feedback prompt.
P DS
task =
MX
m=1
max
 
0, Dm −
TX
t=1
τ Ru,m,t
!
+
NX
n=1
max
 
0, Dn −
TX
t=1
τ Ru,n,t
!
, (25)
where Pspeed indicates the penalty for UA Vs violating speed
limits, Pbounds indicates the penalty for UA Vs violating 3D
space constraints, and Ptask represents a penalty for unsatisfied
computational requirements. These penalties can be calculated
from environmental parameters. Therefore, only the weights
λ1, λ2, and λ3 remain unknown in the reward function.
To further determine the initial values of the reward weights,
the parameter prompt containing the environmental parameters
is provided to the LLM, as shown in Fig. 4. After obtaining the
initial weights of the reward function (λ1 = 0.1, λ2 = 0.5, and
λ3 = 0.05), the reward function is provided to the D3QN for
training. Once the training is complete, the results will serve
as feedback prompt to promote the LLM in further fine-tuning
the reward function, as shown in Fig. 4. The final reward
function is obtained after several iterations. The algorithmic
flow of the L2D2-D3QN is presented in Algorithm 1. The
computational complexity of the L2D2-D3QN algorithm is
O (|S1| · |A1| · k), where |S1| and |A1| are the number of
states and actions of the L2D2-D3QN algorithm, respectively.
V. S IMULATION RESULT
To ensure a fair comparison, both the estimation network
and target network of the DRL algorithms presented in this
paper consist of 2 layers, each containing 20 neurons, main-
taining consistent hyperparameters as outlined in Table II. The
activity space for UA Vs is defined as (0 m to 1000 m, 0 m to
1000 m, 100 m to 150 m), with IoT devices and human-type
users distributed randomly. The simulation parameters are
detailed in Table III.
To explore the reward functions generated by different
LLMs, the Deepseek-R11, GPT-4o2, Llama-3.1-70B3, Claude-
1https://deepseek-r1.com/
2https://openai.com/index/hello-gpt-4o/
3https://www.llama.com/llama3_1/
Algorithm 1 L2D2-D3QN Algorithm
Initialization: Initial prompt, environment parameters, the Θu
and Θ−
u of the evaluation network Qu (·) and target network
Q−
u (·), experience replay buffer F .
Provide initial prompt to LLM;
Provide parameter prompt to LLM;
The reward function obtained from LLM is recorded as R1;
for k = 1, . . . , K
for episode = 1, . . . , E
Initialize the system state s0;
while t = 1, . . . , T
Each agent u randomly selects au,t with probability ε,
otherwise
selects au,t by the training network;
Utilize RepCCNet to obtain P CC
u,m,t;
Each agent u calculates the reward based on Rk;
Update su,t to su,t+1 based on au,t;
Store sample (su,t, au,t, ru,t, su,t+1) in the experience
replay
buffer;
for u = 1, . . . , U
Agent u selects a mini-batch of random samples from
the
experience replay buffer;
Update Θu by gradient descent step on Eq. (22);
Update the target networks every O steps: Θ−
u = Θu;
u = u + 1;
end for
if the result meet the criteria for satisfaction
break;
end if
end while
end for
k = k + 1;
Provide the feedback prompt to LLM and record the
reward function
obtained as Rk;
end for
TABLE II
HYPERPARAMETERS OF THE DRL A LGORITHMS
3.7-Sonnet4, and Qwen-2.5 5 are deployed as LLMs in the
L2D2 framework. These LLMs are popular for their wide
range of applications and robust performance, with excellent
generation and comprehension capabilities. The final reward
function generated by Deepseek-R1 is as follows:
4https://www.anthropic.com/claude/sonnet
5https://chat.qwen.ai/
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5289
TABLE III
SIMULATION SETTINGS
RDS
t = ηEE
t − λ1P DS
speed − λ2P DS
bounds − λ3P DS
task,
P DS
speed =
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vv
u,t − vv
max

+ max
 
0, vh
min − vh
u,t

+ max
 
0, vv
min − vv
u,t

,
P DS
bounds =
UX
u=1
(max (0, xu,t − xmax) + max (0, xmin − xu,t)
+ max (0, yu,t − ymax) + max (0, ymin − yu,t)
+ max (0, zu,t − zmax) + max (0, zmin − zu,t)) ,
P DS
task =
MX
m=1
max
 
0, Dm −
TX
t=1
τ Ru,m,t
!
+
NX
n=1
max
 
0, Dn −
TX
t=1
τ Ru,n,t
!
, (26)
where Pspeed indicates the penalty for UA Vs violating speed
limits, Pbounds indicates the penalty for UA Vs violating 3D
space constraints, and Ptask represents a penalty for unsatisfied
computing demands. The values of λ1, λ2, and λ3 are 0.25,
0.4, and 0.01, respectively.
The final reward function generated by GPT-4o is:
RGPT
t = ηEE
t − λ1P GPT
speed − λ2P GPT
bounds − λ3P GPT
task ,
P GPT
speed =
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vh
min − vh
u,t

+ max
 
0, vv
u,t − vv
max

+ max
 
0, vv
min − vv
u,t

,
P GPT
bounds =
UX
u=1
(max (0, xu,t − xmax) + max (0, xmin − xu,t)
+ max (0, yu,t − ymax) + max (0, ymin − yu,t)
+ max (0, zu,t − zmax) + max (0, zmin − zu,t)) ,
P GPT
task =
MX
m=1
max
 
0, Dm −
TX
t=1
τ Ru,m,t
!
+
NX
n=1
max
 
0, Dn −
TX
t=1
τ Ru,n,t
!
, (27)
where P GPT
speed indicates the penalty for UA Vs violating speed
limits, P GPT
bounds indicates the penalty for UA Vs violating 3D
space constraints, and P GPT
task represents a penalty for unsatis-
fied computational requirements. The values of λ1, λ2, and λ3
are 0.1, 0.5, and 1, respectively. It is evident that Deepseek-
R1 and GPT-4o have similar idea in constructing the reward
function. However, their differing perceptions of the feedback
results ultimately lead to different fine-tuned reward weights.
In contrast to Deepseek-R1 and GPT-4o, the Llama-3.1-
70B introduces a distinct approach when generating the reward
function. It separates the penalties for UA Vs that exceed speed
limits from those that violate 3D space constraints. Addi-
tionally, Llama-3.1-70B removes the penalty of unsatisfied
computing demands and instead employs completed tasks as
a positive reward to motivate the agent. The final reward
function generated by Llama-3.1-70B is shown below:
RLlama
t = ηEE
t + λ1
UX
u=1
MX
m=1
τ Ru,m,t + λ2
UX
u=1
NX
n=1
τ Ru,n,t
− λ3P Llama
hspeed − λ4P Llama
vspeed − λ5P Llama
xbound
− λ6P Llama
ybound − λ7P Llama
zbound,
P Llama
hspeed =
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vh
min −vh
u,t

,
P Llama
vspeed =
UX
u=1
 
max
 
0, vv
u,t − vv
max

+ max
 
0, vv
min −vv
u,t

,
P Llama
xbound =
UX
u=1
(max (0, xu,t − xmax) + max (0, xmin −xu,t)),
P Llama
ybound =
UX
u=1
(max (0, yu,t − ymax) + max (0, ymin −yu,t)),
P Llama
zbound =
UX
u=1
(max (0, zu,t − zmax) + max (0, zmin −zu,t)),
(28)
where P Llama
hspeed, P Llama
vspeed, P Llama
xbound, P Llama
ybound, and P Llama
zbound repre-
sent the penalties incurred by UA Vs for violating the horizontal
speed constraint, vertical speed constraint, x-axis boundary
constraint, y-axis boundary constraint, and z-axis boundary
constraint, respectively. The values of λ1, λ2, λ3, λ4, λ5, λ6,
and λ7 are 0.05, 0.5, 0.5, 0.5, 0, 0, and 0.1, respectively.
Compared to the LLMs described previously, the final
reward function generated by Claude-3.7-Sonnet is more com-
plex:
RClaude
t = ηEE
t + λ1CClaude
demand + λ2CClaude
con + λ3CClaude
progress,
CClaude
demand =
UX
u=1
MX
m=1
αu,m,t
Ru,m,t
Dm
τ +
UX
u=1
NX
n=1
αu,n,t
Ru,n,t
Dn
τ,
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5290 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
CClaude
con = −P1
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vv
u,t − vv
max

+ max
 
0, vh
min − vh
u,t

+ max
 
0, vv
min − vv
u,t

− P2
UX
u=1
(max (0, xu,t − xmax) + max (0, xmin − xu,t)
+ max (0, yu,t − ymax) + max (0, ymin − yu,t)
+ max (0, zu,t − zmax) + max (0, zmin − zu,t)) ,
CClaude
progress =
MP
m=1
min
 tP
τ=1
τ Ru,m,τ , Dm

MP
m=1
Dm +
NP
n=1
Dn
+
NP
n=1
min
 tP
τ=1
τ Ru,n,τ , Dn

MP
m=1
Dm +
NP
n=1
Dn
− t
T , (29)
where CClaude
demand is denoted as the reward progress toward
meeting computing demands, and CClaude
con penalizes constraint
violations. The structure of CClaude
demand is unique, as the sum
of the first two components indicates the proportion of the
currently fulfilled computing demand relative to the total
demand, serving as a positive incentive. The third component
reflects the proportion of the current time relative to the
total time, representing the percentage of time consumed.
By adopting percentage-based metrics, unit dependency issues
are eliminated, enabling standardized evaluation across tasks
of varying scales and timeframes. Therefore, CClaude
demand essen-
tially measures the efficiency of task completion. When it is
positive, it means that the task is completed faster than the
time consumed. In contrast, when it is negative, it means
that the task is completed behind the time schedule. The
values of λ1, λ2, λ3, P1, and P2 are 1.8, 1.2, 6, 1.5, and 1,
respectively.
The Qwen-2.5 further decomposes the penalty for unsatis-
fied computational requirements:
RQwen
t = ηEE
t + P Qwen
demand + P Qwen
con ,
P Qwen
demand = −λm max
 
0,
MX
m=1
 
Dm −
TX
t=1
UX
u=1
τ Ru,m,t
!!
− λn max
 
0,
NX
n=1
 
Dn −
TX
t=1
UX
u=1
τ Ru,n,t
!!
,
P Qwen
con = −γh
UX
u=1
 
max
 
0, vh
u,t − vh
max

+ max
 
0, vh
min − vh
u,t

− γv
UX
u=1
 
max
 
0, vv
u,t − vv
max

+ max
 
0, vv
min − vv
u,t

− γx
UX
u=1
max ((0, xu,t − xmax) + max (0, xmin − xu,t))
− γy
UX
u=1
max ((0, yu,t − ymax) + max (0, ymin − yu,t))
Fig. 5. Flight trajectories of UA Vs (LLM=Deepseek-R1).
Fig. 6. Flight trajectories of UA Vs (LLM=GPT-4o).
Fig. 7. Flight trajectories of UA Vs (LLM=Llama-3.1-70B).
− γz
UX
u=1
max ((0, zu,t − zmax) + max (0, zmin − zu,t)),
(30)
where P Qwen
demand represents demand satisfaction penalty, and
P Qwen
con represents constraint violation penalty. The values of
λm, λn, γh, γv, γx, γy and γz are 4, 4, 4.06, 5.64, 0, 0, and
0.44, respectively. When LLMs in the L2D2 algorithm are
Deepseek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet,
and Qwen-2.5, the corresponding UA Vs trajectories are shown
in Fig. 5, Fig. 6, Fig. 7, Fig. 8, and Fig. 9.
A. Comparison With Different LLMs
Different LLM designs feature distinct reward function con-
structions and varying weights, resulting in different reward
values upon convergence of the L2D2-D3QN algorithm.
Therefore, it is unfair to compare the reward values of L2D2-
D3QN driven by different LLMs. Although the designs of the
reward functions differ, the energy efficiency indicators that
the LLMs ultimately optimize adhere to a unified standard.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5291
Fig. 8. Flight trajectories of UA Vs (LLM=Claude-3.7-Sonnet).
Fig. 9. Flight trajectories of UA Vs (LLM=Qwen-2.5).
Fig. 10. Average energy efficiency curves of L2D2-D3QN with different
LLMs.
Consequently, it is practical significance to compare different
LLM schemes based on system energy efficiency. Fig. 10
presents the convergence curves of average energy efficiency
for L2D2-D3QN across different LLMs and human-designed
reward functions.
The reward function designed by human-1 is identical to the
reward functions presented in [19] and [21], as shown below:
RHuman1
t = ηEE
t . (31)
This design does not consider the punishment of constraints
on the agent. In addition, the reward function designed by
human-2 is the same as in [20]:
RHuman2
t =
 ηEE
t , δ t = 1
ω · ηEE
t , δ t = 0 , (32)
Fig. 11. CDF of average energy efficiency for L2D2-D3QN with different
LLMs.
where δt = 1 indicates that the agents satisfy all constraints,
while δt = 0 signifies that the agents do not meet all the con-
straints. The discount factor ω = 0.5 signifies that the reward
decreases when the agent fails to comply with the constraint.
Compared to other LLMs, the curve of DeepSeek-R1 is the
most stable and offers the highest improvement in energy
efficiency. In addition, compared with the human-designed
reward functions, the reward functions designed by LLMs
can provide more significant improvements in system energy
efficiency.
Fig. 11 presents the cumulative distribution function (CDF)
of average energy efficiency, where the reward functions in
L2D2-D3QN is designed by Deepseek-R1, GPT-4o, Llama-
3.1-70B, Claude-3.7-Sonnet, Qwen-2.5, and humans. The
corresponding value where CDF = 1 represents the maximum
energy efficiency achievable by L2D2-D3QN. As shown in
the figure, compared to GPT-4o, Llama-3.1-70B, Claude-
3.7-Sonnet, Qwen-2.5, human-1, and human-2, L2D2-D3QN
driven by Deepseek-R1 can achieve energy efficiency improve-
ments of 7%, 9%, 16%, 17%, 30%, and 56%, respectively,
highlighting the advantages of Deepseek-R1 in reward func-
tion design. As a result, if no penalties are considered for
the agents, as seen in the case of human-1, the learning
performance of agents will be poor. On the contrary, if the
considerations are overly complex, as seen in the case of
Qwen-2.5, it becomes challenging to achieve excellent reward
parameters through fine-tuning.
Additionally, the effect of different LLM token mechanisms
on energy efficiency improvement is also explored. Fig. 12
illustrates the number of tokens for different LLMs, cate-
gorized by initial prompt, parameter prompt, and feedback
prompt, with token counts determined by Tiktokenizer 6 and
Token Counter7. For different LLMs, the word count of the
initial prompt provided to them is identical. It can be seen that
DeepSeek-R1 divides the initial prompt into the lowest number
of tokens. Since different LLM designs employ varying reward
functions, the word counts for parameter prompt and feedback
6https://tiktokenizer.vercel.app/
7https://tokencounter.org/
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5292 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
Fig. 12. The number of tokens for prompt segmentation in different LLMs.
prompt differ slightly. Qwen-2.5 generates the highest num-
ber of token divisions for prompts due to its subword-level
tokenization, which features fine-grained segmentation. The
differences in the number of tokens generated by tokenizers
of different LLMs for the same text can impact the ability
of model to handle context. For instance, a higher token
count may fragment information, making it difficult for the
model to capture long-range dependencies or process prompts
efficiently, ultimately affecting the quality of the generated
reward function. Compared with other LLMs, Qwen-2.5 has
the highest number of token divisions for prompts, and its
generated reward function is also the most complex. An overly
complex reward function makes it challenging to fine-tune
the reward weights of Qwen-2.5, ultimately resulting in low
system energy efficiency. In contrast, DeepSeek-R1 primarily
utilizes a word-based segmentation strategy, which involves
dividing the input text into complete words while minimizing
the total number of tokens. This approach preferentially uti-
lizes whole words or combinations of high-frequency phrases
to divide the input text, which results in a reduced number
of token divisions. In some scenarios, fewer tokens can lead
to more efficient information encoding, allowing the model
to better capture key information and generate a more rea-
sonable reward function structure. Therefore, if an LLM can
dynamically adapt its tokenization strategies to suit different
tasks, it has the potential to achieve significant performance
improvements. This is expected to become a key focus of
future research.
B. Comparison With Different DRL Methods
To investigate the impact of different DRLs on maximizing
system energy efficiency, Fig. 13 presents the convergence
curves of energy efficiency when the LLM in L2D2 is
enabled by Deepseek-R1, with DRLs including DQN, DDQN,
and D3QN. These are referred to as L2D2-DQN, L2D2-
DDQN, and L2D2-D3QN, respectively. Compared with DQN
and DDQN, D3QN clearly delivers greater improvements
in energy efficiency and achieves more stable convergence.
Furthermore, Fig. 14 shows the CDF of energy efficiency
for L2D2-DQN, L2D2-DDQN, and L2D2-D3QN. Compared
to DQN and DDQN, D3QN can achieve energy efficiency
improvements of 40% and 34%, respectively.
Fig. 13. Average energy efficiency curves of L2D2 with different DRLs.
Fig. 14. CDF of average energy efficiency for L2D2 with different DRLs.
C. Comparison With Different Trajectories
To investigate the impact of UA V flight trajectories on
energy efficiency, the trajectory generated by L2D2-D3QN
(Deepseek-R1) is compared with both the straight trajec-
tory [34] and the circular trajectory [35]. In all cases, the
initial location of UA Vs is set at (0 m, 0 m, 100 m). From
a horizontal perspective, circle 1 represents the UA Vs flying
clockwise from (0 m, 0 m) to (1000 m, 0 m), while circle
2 denotes the UA Vs flying counterclockwise from (0 m, 0 m)
to (0 m, 1000 m). The straight trajectory involves the UA Vs
flying directly from (0 m, 0 m) to (1000 m, 1000 m). For
a fair comparison, the baseline trajectories maintain a fixed
horizontal path for UA Vs, while the remaining variables are
optimized employing L2D2-D3QN (Deepseek-R1). Further-
more, to avoid collisions, UA Vs are assigned different altitudes
when following the same baseline trajectory. As demonstrated
in Fig. 15, the trajectory generated by L2D2-D3QN exhibits a
significant improvement in energy efficiency, highlighting its
superiority in trajectory optimization.
D. Comparison With Different Numbers of UA Vs and MEC
Nodes
Moreover, the impact of the number of UA Vs and MEC
nodes on system energy efficiency has been explored, as illus-
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
LV et al.: LLM-EMPOWERED ENERGY-EFFICIENT MULTI-UA V-ASSISTED MEC HETEROGENEOUS NETWORKS 5293
Fig. 15. The CDF of the average energy efficiency for different trajectories.
Fig. 16. The impact of the number of UA Vs and MEC nodes on system
energy efficiency, where u denotes the number of UA Vs.
trated in Fig. 16. For a single UA V , L2D2-D3QN significantly
improves energy efficiency when MEC nodes are few. How-
ever, as MEC nodes increase, the UA V struggles to meet
computational demands under constraints, resulting in a grad-
ual decline in energy efficiency. With two UA Vs, energy
efficiency rises alongside the number of MEC nodes. Nev-
ertheless, the rate of improvement decreases once the number
exceeds 16, suggesting that the capacity of the two UA Vs is
approaching its limits. In scenarios with three or four UA Vs,
the increase in the number of UA Vs raises the flight energy
consumption, resulting in low system energy efficiency when
the number of MEC nodes is relatively few. As a result, it is
crucial to select the appropriate number of UA Vs based on
the number of MEC nodes to optimize energy efficiency in
practical applications.
VI. C ONCLUSION
An LLM-driven DRL framework (L2D2) and an algorithm
(L2D2-D3QN) are proposed in this paper to maximize the
system energy efficiency in multi-UA V-assisted MEC hetero-
geneous networks, exploring the potential of the low-altitude
airspace. Through comprehensive experiments, the effects
of various LLMs (Deepseek-R1, GPT-4o, Llama-3.1-70B,
Claude-3.7-Sonnet, and Qwen-2.5) and DRLs (DQN, DDQN,
and D3QN) on system energy efficiency improvement are sys-
tematically evaluated. In addition, the impact of tokenization
strategies of LLMs on system performance has been explored.
The reward function under the L2D2 framework can adjust the
strategy according to environmental feedback without manual
redesign, effectively enhancing the potential of UA Vs in low-
altitude space. In the future, we will explore the integration
of sensing and communication technologies [36], [37], [38]
along with visual language models [39] to provide promising
steps for AGI.

## § References

[1] R. Huang et al., “Dynamic task offloading for multi-UA Vs in
vehicular edge computing with delay guarantees: A consensus admm-
based optimization,” IEEE Trans. Mobile Comput., vol. 23, no. 12,
pp. 13696–13712, Aug. 2024.
[2] G. Cheng, X. Song, Z. Lyu, and J. Xu, “Networked ISAC for low-altitude
economy: Transmit beamforming and UA V trajectory design,” in Proc.
IEEE/CIC Int. Conf. Commun. China (ICCC), Aug. 2024, pp. 78–83.
[3] Y . Li, Q. Zeng, C. Shao, P. Zhuo, B. Li, and K. Sun, “UA V localization
method with keypoints on the edges of semantic objects for low-altitude
economy,” Drones, vol. 9, no. 1, p. 14, Dec. 2024.
[4] W. Yuan et al., “From ground to sky: Architectures, applica-
tions, and challenges shaping low-altitude wireless networks,” 2025,
arXiv:2506.12308.
[5] Y . Luo, W. Ding, and B. Zhang, “Optimization of task scheduling
and dynamic service strategy for multi-UA V-enabled mobile-edge com-
puting system,” IEEE Trans. Cognit. Commun. Netw., vol. 7, no. 3,
pp. 970–984, Sep. 2021.
[6] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and L. Hanzo,
“Multi-agent deep reinforcement learning-based trajectory planning for
multi-UA V assisted mobile edge computing,” IEEE Trans. Cognit.
Commun. Netw., vol. 7, no. 1, pp. 73–84, Mar. 2021.
[7] J. Miao, S. Bai, S. Mumtaz, Q. Zhang, and J. Mu, “Utility-oriented
optimization for video streaming in UA V-aided MEC network: A
DRL approach,” IEEE Trans. Green Commun. Netw., vol. 8, no. 2,
pp. 878–889, Jun. 2024.
[8] J. Xu, X. Liu, A. G. Neiat, L. Chu, X. Li, and Y . Yang, “A holistic and
hybrid service selection strategy for MEC-based UA V last-mile delivery
systems,” IEEE Trans. Services Comput., vol. 17, no. 6, pp. 3022–3036,
Aug. 2024.
[9] M. Akbari, A. Syed, W. S. Kennedy, and M. Erol-Kantarci, “Con-
strained federated learning for AoI-limited SFC in UA V-aided MEC for
smart agriculture,” IEEE Trans. Mach. Learn. Commun. Netw. , vol. 1,
pp. 277–295, 2023.
[10] M. Li, N. Cheng, J. Gao, Y . Wang, L. Zhao, and X. Shen, “Energy-
efficient UA V-assisted mobile edge computing: Resource allocation and
trajectory optimization,” IEEE Trans. V eh. Technol., vol. 69, no. 3,
pp. 3424–3438, Mar. 2020.
[11] X. Qin, W. Yu, Z. Song, T. Hou, Y . Hao, and X. Sun, “Energy efficiency
optimization for RIS-assisted UA V-enabled MEC systems,” in Proc.
IEEE Globecom Workshops (GC Wkshps), Dec. 2022, pp. 1164–1169.
[12] X. Qin, Z. Song, T. Hou, W. Yu, J. Wang, and X. Sun, “Joint optimization
of resource allocation, phase shift, and UA V trajectory for energy-
efficient RIS-assisted UA V-enabled MEC systems,”IEEE Trans. Green
Commun. Netw., vol. 7, no. 4, pp. 1778–1792, Dec. 2023.
[13] Z. Liu, J. Qi, Y . Shen, K. Ma, and X. Guan, “Maximizing energy effi-
ciency in UA V-assisted NOMA–MEC networks,”IEEE Internet Things
J., vol. 10, no. 24, pp. 22208–22222, Dec. 2023.
[14] X. Xing, Y . Huo, Q. Gao, H. Li, X. Gao, and J. Qian, “An enhanced
energy efficiency scheme for secure computing in UA V-MEC networks,”
Int. J. Sensor Netw., vol. 44, no. 1, pp. 23–35, 2024.
[15] V . Saxena, J. Jaldén, and H. Klessig, “Optimal UA V base station
trajectories using flow-level models for reinforcement learning,” IEEE
Trans. Cognit. Commun. Netw., vol. 5, no. 4, pp. 1101–1112, Dec. 2019.
[16] H. Zhang, H. Wang, Y . Li, K. Long, and A. Nallanathan, “DRL-driven
dynamic resource allocation for task-oriented semantic communication,”
IEEE Trans. Commun., vol. 71, no. 7, pp. 3992–4004, Jul. 2023.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply. 
5294 IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING, VOL. 12, 2026
[17] W. Lei, Y . Ye, and M. Xiao, “Deep reinforcement learning-based
spectrum allocation in integrated access and backhaul networks,” IEEE
Trans. Cognit. Commun. Netw., vol. 6, no. 3, pp. 970–979, Sep. 2020.
[18] J. Li et al., “A reinforcement learning-based stochastic game for
energy-efficient UA V swarm-assisted MEC with dynamic clustering
and scheduling,” IEEE Trans. Green Commun. Netw., vol. 9, no. 1,
pp. 255–270, Mar. 2025.
[19] Z. Zhang et al., “Energy-efficient secure video streaming in UA V-enabled
wireless networks: A safe-DQN approach,”IEEE Trans. Green Commun.
Netw., vol. 5, no. 4, pp. 1892–1905, Dec. 2021.
[20] M. Wu et al., “UA V-mounted RIS-aided mobile edge computing system:
A DDQN-based optimization approach,” Drones, vol. 8, no. 5, p. 184,
May 2024.
[21] C. Liu, Y . Zhong, R. Wu, S. Ren, S. Du, and B. Guo, “Deep rein-
forcement learning based 3D-trajectory design and task offloading in
UA V-enabled MEC system,”IEEE Trans. V eh. Technol., vol. 74, no. 2,
pp. 3185–3195, Feb. 2025.
[22] A. F. Mohammad, B. Clark, R. Agarwal, and S. Summers, “LLM/GPT
generative AI and artificial general intelligence (AGI): The next frontier,”
in Proc. Congr . Comput. Sci., Comput. Eng., Appl. Comput. (CSCE),
Jul. 2023, pp. 413–417.
[23] R. Zhang et al., “Generative AI agents with large language model for
satellite networks via a mixture of experts transmission,” IEEE J. Sel.
Areas Commun., vol. 42, no. 12, pp. 3581–3596, Dec. 2024.
[24] A. T. Neumann, Y . Yin, S. Sowe, S. Decker, and M. Jarke, “An
LLM-driven chatbot in higher education for databases and information
systems,” IEEE Trans. Educ., vol. 68, no. 1, pp. 103–116, Feb. 2025.
[25] Q. Lang, S. Tian, M. Wang, and J. Wang, “Exploring the answering
capability of large language models in addressing complex knowledge
in entrepreneurship education,” IEEE Trans. Learn. Technol., vol. 17,
pp. 2053–2062, 2024.
[26] J. Gong, L. G. Foo, Y . He, H. Rahmani, and J. Liu, “LLMs are good sign
language translators,” in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
Recognit. (CVPR), Jun. 2024, pp. 18362–18372.
[27] M. A. Hossain, A. R. Hossain, and N. Ansari, “AI in 6G: Energy-efficient
distributed machine learning for multilayer heterogeneous networks,”
IEEE Netw., vol. 36, no. 6, pp. 84–91, Nov. 2022.
[28] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude
for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6,
pp. 569–572, Dec. 2014.
[29] Z. Kuang, Y . Pan, F. Yang, and Y . Zhang, “Joint task offloading schedul-
ing and resource allocation in air–ground cooperation UA V-enabled
mobile edge computing,” IEEE Trans. V eh. Technol., vol. 73, no. 4,
pp. 5796–5807, Apr. 2024.
[30] S. Sinche et al., “A survey of IoT management protocols and frame-
works,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 1168–1190,
2nd Quart., 2020.
[31] N. Tang, X. Wang, F. Zhou, S. Tang, and Y . Lyu, “Reparameterization
causal convolutional network for automatic modulation classification,”
IEEE Trans. V eh. Technol., vol. 73, no. 6, pp. 8576–8583, Jun. 2024.
[32] H. Mei, K. Yang, Q. Liu, and K. Wang, “3D-trajectory and phase-shift
design for RIS-assisted UA V systems using deep reinforcement learn-
ing,” IEEE Trans. V eh. Technol., vol. 71, no. 3, pp. 3020–3029,
Mar. 2022.
[33] X. Zhang, M. Peng, and C. Liu, “Sensing-assisted beamforming and
trajectory design for UA V-enabled networks,”IEEE Trans. V eh. Technol.,
vol. 73, no. 3, pp. 3804–3819, Mar. 2024.
[34] Y . Guo, C. You, C. Yin, and R. Zhang, “UA V trajectory and commu-
nication co-design: Flexible path discretization and path compression,”
IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3506–3523, Nov. 2021.
[35] X. Diao, W. Yang, L. Yang, and Y . Cai, “UA V-relaying-assisted multi-
access edge computing with multi-antenna base station: Offloading and
scheduling optimization,” IEEE Trans. V eh. Technol., vol. 70, no. 9,
pp. 9495–9509, Sep. 2021.
[36] J. Wang et al., “Generative AI based secure wireless sensing
for ISAC networks,” IEEE Trans. Inf. F orensics Security, vol. 20,
pp. 5195–5210, 2025.
[37] J. Wang et al., “Generative AI enabled robust data augmentation for
wireless sensing in ISAC networks,” IEEE J. Sel. Areas Commun., early
access, Sep. 24, 2025, doi: 10.1109/JSAC.2025.3613672.
[38] J. Wang et al., “Generative artificial intelligence assisted wireless sens-
ing: Human flow detection in practical communication environments,”
IEEE J. Sel. Areas Commun., vol. 42, no. 10, pp. 2737–2753, Oct. 2024.
[39] C. Xie et al., “Disrupting vision-language model-driven navigation
services via adversarial object fusion,” 2025, arXiv:2505.23266.
Ke Lv (Student Member, IEEE) received the B.E.
and M.S. degrees from Beijing Information Sci-
ence and Technology University, Beijing, China,
in 2021 and 2024, respectively. He is currently
pursuing the Ph.D. degree with Beijing University of
Posts and Telecommunications. His current research
interests include wireless communication, unmanned
aerial vehicle, mobile edge computing, and cognitive
radio.
Sai Huang (Senior Member, IEEE) is currently a
Full Professor with the Department of Information
and Communication Engineering, Beijing University
of Posts and Telecommunications (BUPT). He is
an Academic Secretary with the Key Laboratory
of Universal Wireless Communications, Ministry
of Education, China. His research interests include
machine learning assisted intelligent signal process-
ing, statistical spectrum sensing and analysis, fast
detection and depth recognition of universal wireless
signals, millimeter wave signal processing, and cog-
nitive radio networks. He is a reviewer of international journals, such as IEEE
TRANSACTIONS ON WIRELESS COMMUNICATIONS , IEEE T RANSACTIONS
ON VEHICULAR TECHNOLOGY , IEEE W IRELESS COMMUNICATIONS LET-
TERS , and IEEE T RANSACTIONS ON COGNITIVE COMMUNICATIONS AND
NETWORKING , and international conferences, such as IEEE ICC and IEEE
GLOBECOM.
Yuanyuan Yao (Member, IEEE) received the Ph.D.
degree in information and communication engi-
neering from Beijing University of Posts and
Telecommunications, Beijing, China, in 2017. She
is currently a Professor with the School of Infor-
mation and Communication Engineering, Beijing
Information Science and Technology University,
Beijing. Her research interests include cooperative
communication of UA V , RIS assisted communica-
tion, stochastic geometry and its applications in
large-scale wireless networks, and intelligent radio
resource allocation in 6G.
Weiwei Jiang (Senior Member, IEEE) received
the B.Sc. and Ph.D. degrees from the Department
of Electronic Engineering, Tsinghua University,
Beijing, China, in 2013 and 2018, respectively. He is
currently an Assistant Professor with the School of
Information and Communication Engineering and
the Key Laboratory of Universal Wireless Communi-
cations, Ministry of Education, Beijing University of
Posts and Telecommunications. His current research
interests include artificial intelligence for networking
and communication, satellite communication, and
smart grid communication.
Zhiyong Feng (Senior Member, IEEE) received the
B.S., M.S., and Ph.D. degrees from BUPT, Beijing,
China, in 1993, 1997, and 2009, respectively. She
is currently a Full Professor with BUPT, where she
is the Director of the Key Laboratory of Universal
Wireless Communications, Ministry of Education.
Her research interests include 5G mobile networks,
ISAC system design, wireless network architecture
design, cognitive wireless networks, universal signal
detection and identification, and network informa-
tion theory. She is a Technical Advisor of NGMN.
She is active in ITU-R WP5A/5C/5D, IEEE 1900, ETSI, and CCSA stan-
dards. She is an Editor of IET Communications and KSII Transactions on
Internet and Information Systems and a reviewer of IEEE T RANSACTIONS
ON WIRELESS COMMUNICATIONS , IEEE T RANSACTIONS ON VEHICULAR
TECHNOLOGY , and IEEE J OURNAL ON SELECTED AREAS IN COMMUNI -
CATIONS .
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:05:39 UTC from IEEE Xplore.  Restrictions apply.
