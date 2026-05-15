---
paper_id: "paper-1999"
source_pdf_sha: "842a750f79be8157475fbeab6fc83e621d493d0a47a473544c8ab4b807957a22"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 1
  page_count: 5
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-1999 — fulltext
## §unknown-1

LLM-Guided DRL for Optimizing Energy
Efﬁciency in Multi-Cluster MEC Networks
Huiying Niu
The 54th Research Institute of CETC
Shijiazhuang, China
hui7884@163.com
Ke Lv
Key Laboratory of Universal Wireless
Communications, Ministry of Education
Beijing University of Posts
and Telecommunications
Beijing, China
kelv@bupt.edu.cn
Fei Shi*
The 54th Research Institute of CETC
Shijiazhuang, China
dragonsf@163.com
Jinglun Cai
The 54th Research Institute of CETC
Shijiazhuang, China
cetc54sjz@163.com
Sai Huang
Key Laboratory of Universal Wireless Communications, Ministry of Education
Beijing University of Posts and Telecommunications
Beijing, China
huangsai@bupt.edu.cn
Abstract—Enabled by unmanned aerial vehicles (UA Vs), multi-
cluster mobile edge computing (MEC) networks can provide
highly ﬂexible communication services for massive user connec-
tivity. However, multiple clusters signiﬁcantly increase network
complexity, obstructing the optimization of system energy ef-
ﬁciency. This paper innovatively proposes a closed-loop large
language models (LLMs)-guided deep reinforcement learning
(DRL) framework named LGD, in which the LLM can iteratively
design rewards for DRL. By combining the LGD framework with
the powerful dueling double deep Q-network (D3QN) in DRL, the
LGD-D3QN algorithm is proposed and applied to multi-cluster
MEC networks to improve energy efﬁciency. Compared to other
LLM and DRL algorithms, LGD-D3QN can achieve a signiﬁcant
improvement in energy efﬁciency.
Index Terms —Large language model, Deep reinforcement
learning, Unmanned aerial vehicle, Mobile edge computing
I. I NTRODUCTION
By ofﬂoading computation to the network edge, mobile
edge computing (MEC) effectively boosts service capabilities
at the network edge, addressing the shortcomings of traditional
centralized cloud computing regarding real-time performance
and coverage quality [1]. Nevertheless, the coverage of ﬁxed
terrestrial base stations remains geographically constrained. To
further realize ubiquitous computing, unmanned aerial vehicles
(UA Vs), with their unique mobility and ﬂexible deployment
capabilities, have become ideal aerial platforms for MEC [2].
UA Vs equipped with MEC servers can be deployed as aerial
base stations, which are capable of establishing robust line-
of-sight (LoS) links with users to offer low-latency and high-
bandwidth services. Network coverage is extended by UA Vs,
particularly in emergency communications, temporary hotspot
areas, and remote regions [3].
UA V-assisted MEC provides a new scheme for communica-
tion and computation services to ground users and has gained
This work was supported in part by the National Natural Science Foundation
of China under Grant (62422103, 62321001, 62171045, 62201090).
extensive attention from researchers. Maximizing both the
endurance of the UA V and system throughput makes energy ef-
ﬁciency a crucial evaluation criterion. Traditional optimization
methods are widely utilized to maximize energy efﬁciency.
Li et al. [4] addressed the problem by jointly optimizing
three factors: the two-dimensional (2D) UA V trajectory, the
user transmit power, and the computation load allocation.
For the solution, the Dinkelbach algorithm and the succes-
sive convex approximation (SCA) method were employed.
However, with the increasing complexity of system models,
ﬁnding an analytical solution to the objective function becomes
challenging, and conventional optimization algorithms face
considerable limitations regarding convergence, computational
efﬁciency, and solution quality. This challenge beneﬁts from
the innovative approach of deep reinforcement learning (DRL).
In the ﬁeld of DRL, Zhang et al. [5] utilized the deep Q-
learning network (DQN) to jointly optimize video layer selec-
tion, power allocation, and multi-UA V trajectories to improve
energy efﬁciency. Additionally, Liu et al. [6] tackled the three-
dimensional (3D) multi-UA V trajectory planning problem. By
integrating the double deep Q-learning network (DDQN), the
system energy efﬁciency is greatly improved.
However, the above-mentioned studies focused solely on
simple MEC scenarios, without addressing complex multi-
cluster MEC scenarios. Furthermore, as the complexity of
the system model further increases, the design of the re-
ward signiﬁcantly affects the results of DRL. Therefore,
it is necessary to design appropriate rewards to improve
the training effectiveness of DRL in complex scenarios. By
training on massive human language and knowledge, large
language models (LLMs) gain deep semantic understanding
and logical reasoning power [7]. Consequently, LLMs can be
leveraged to interpret complex task objectives and environ-
mental information, and formulate them as effective reward
functions, thus enabling DRL agents to learn efﬁciently in
2295
2025 11th International Conference on Computer and Communications
979-8-3315-4558-1/25/$31.00 ©2025 IEEE
2025 11th International Conference on Computer and Communications (ICCC) | 979-8-3315-4558-1/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICCC68654.2025.11437715
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:49:21 UTC from IEEE Xplore.  Restrictions apply. 
complex environments [8], [9]. Compared with [8] and [9],
we have added a pre-generation mechanism in the process of
LLM guiding DRL to design rewards. Before generating the
actual reward function, an initial reward function with random
weights is ﬁrst generated utilizing the environment and task
description. Then, through the ﬁrst training iteration of the
DRL, the values of these weights are gradually adjusted, rather
than generating a new reward function structure each time, or
having the reward value directly provided by the LLM. The
contributions of this paper are summarized as follows:
• A multi-cluster MEC network is considered, where each
cluster is composed of heterogeneous MEC nodes, includ-
ing human users and internet of things (IoT) devices. At
least one UA V equipped with MEC server is contained
within each cluster. Furthermore, each MEC node has
different computing demands.
• A closed-loop LLM-guided DRL framework is designed,
named LGD. The output of the DRL is encapsulated into
a prompt and then fed back to the LLM, which reﬁnes
the reward function to better guide the next training of
the DRL. Furthermore, a novel dueling double deep Q-
network (D3QN) is employed as the DRL within the LGD
framework, leading to the proposal of the LGD-D3QN
algorithm. To our knowledge, this is the ﬁrst time that
LLM-guided DRL design rewards has been applied to
multi-cluster MEC.
• The performances of ﬁve popular LLMs: DeepSeek-R1,
GPT-4o, Claude-3.7-Sonnet, Llama-3.1-70B, and Qwen-
2.5, are compared within the LGD framework, and the
impact of the tokenization mechanism on system perfor-
mance is analyzed.
This paper is structured as follows: Section II outlines the
system model; Section III discusses the problem formulation;
Section IV introduces the LGD framework and the LGD-
D3QN algorithm; Section V provides the simulation results,
while Section VI offers the conclusion.
II. S YSTEM MODEL
Communication link with 
h
uman user 
Computing demand 
Communication link with 
Io
T device 
UAV 1 
M
EC server
UAV 2 
Human user
IoT device
Ba
se station
Fig. 1. Multi-UA V-assisted multi-cluster MEC network.
The system model of multi-UA V-assisted multi-cluster MEC
network is illustrated in Fig. 1, where U UA Vs equipped
with MEC servers assist M human users as well as N
IoT devices. Each cluster contains at least one UA V . These
devices have different computing demands, denoted as Dm
and Dn respectively. vh
u,t and vv
u,t represent the horizontal
and vertical ﬂight speeds of the UA V u at time slot t,
respectively. The 3D coordinate of IoT device n, human user
m, and UA V u at time slot t are Qn,t
∆
= (x n,t,y n,t, 0),
Qm,t
∆
= (x m,t,y m,t, 0), and QUAV
u,t
∆
=
(
xUAV
u,t ,y UAV
u,t ,H UAV
u,t
)
,
where n∈N ={1, 2, 3...N }, m∈M ={1, 2, 3...M },
t∈T ={1, 2, 3...T }, and HUAV
u,t denotes the altitude of
UA Vu at time slot t, u ∈ U = {1, 2, 3...U }. Once the
UA V fulﬁlls all computing requirements of IoT devices and
human users, the task can be terminated. The probability that
the LoS link between the IoT device n and the UA Vu remains
unobstructed at the time slot t is
P UB
u,n,t = 1
1 +a
√
−b
(
arctan
(H UA V
u,t
du,n,t
)
−a
), (1)
where du,n,t denotes the distance between the IoT device n
and the UA Vu at time slott.a andb, which are speciﬁc to the
environment, are obtained from [10]. Similarly, the probability
that the LoS link between the human user m and the UA Vu
being unobstructed at the time slot t is
P UB
u,m,t = 1
1 +a
√
−b
(
arctan
(H UA V
u,t
du,m,t
)
−a
), (2)
where du,m,t is the distance between the human user m and
the UA Vu at time slott. The channel gain from the IoT device
n to the UA Vu at time slot t is denoted by hu,n,t, and hu,m,t
represents the channel gain from the human user m to the
UA Vu at time slot t [2]:
hu,n,t
∆
=α1(du,n,t)−2= α1
QUAV
u,t −Qn,t
2, (3)
hu,m,t
∆
=α1(du,m,t)−2= α1
QUAV
u,t −Qm,t
2, (4)
whereα1 represents the received power at a reference distance
of 1 meter for a transmission power of 1 W. As a result, the
uplink data rate from the IoT device n to the UA Vu at time
slot t can be represented as
Ru,n,t =αu,n,tP UB
u,n,tBlog2
(
1 +Pnhu,n,t
Bσ2
)
, (5)
where B is the bandwidth, αu,n,t is the association factor
between the IoT device n and the UA Vu at time slot t, taking
values in{0, 1}.Pn is the transmit power of the IoT device n,
and σ2 denotes the power density of additive white Gaussian
noise. Similarly, the data transmission rate between the human
user m and the UA Vu at time slot t is
Ru,m,t =αu,m,tP UB
u,m,tBlog2
(
1 +Pmhu,m,t
Bσ2
)
, (6)
where Pm is the transmit power of the human user m,
αu,m,t takes values in {0, 1} representing the association
2296
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:49:21 UTC from IEEE Xplore.  Restrictions apply. 
factor between the UA Vu and the human user m. The amount
of tasks that the UA Vu is tasked with handling in time slot t
is Du,t. In time slot t, the energy consumption of the central
processing unit (CPU) for the UA V u is deﬁned as
EC
u,t =κ
(
f C
u
)3
· min
(
τ, C C
uDu,t
f Cu
)
, (7)
whereτ denotes the duration of each time slot, fC
u denotes the
CPU frequency,κ is a factor that is inﬂuenced by the effective
switched capacitance of the CPU architecture, and CC
u is the
number of CPU cycles required to process a single bit of data.
In time slot t, the ﬂight energy consumption of the UA V u is
EU
u,t =
(
Pbla
(
1 +
3(vh
u,t)
2
U 2
tip
)
+ 1
2Gρsd0
(
vh
u,t
)3
+Pind
(√
1 + (vh
u,t)
4
4v4
0
− (vh
u,t)
2
2v2
0
) 1
2
+Pd/avv
u,t

τ,
(8)
where Pd/a, Pbla, Pind, Utip, v0, G, ρ, s, and d0 are all dy-
namic parameters involved in UA V ﬂight energy consumption
[3]. Consequently, the total system energy consumption at time
slot t can be expressed as
EToT
t =
U∑
u=1
(
EU
u,t +EC
u,t
)
+EI
t +EH
t , (9)
whereEI
t andEH
t represent the transmit power of IoT devices
and human users, respectively.
III. P ROBLEM FORMULATION
Building on the analysis above, the system energy efﬁciency
for each time slot t can be expressed as
ηEE
t =
U∑
u=1
( N∑
n=1
Ru,n,t +
M∑
m=1
Ru,m,t
)
ETOT
t
. (10)
To maximize the average energy efﬁciency of the system, the
optimization problem P1 is formulated as follows:
P1 : max ηEE
ave =
T∑
t=1
ηEE
t
T (11)
s.t. vh
u,t≤vh
max,∀u∈U ,t∈T , (12)
vv
u,t≤vv
max,∀u∈U ,t∈T , (13)
xmin≤xu,t≤xmax,∀u∈U ,t∈T , (14)
ymin≤yu,t≤ymax,∀u∈U ,t∈T , (15)
zmin≤zu,t≤zmax,∀u∈U ,t∈T , (16)
αu,m,t ={0, 1},∀u∈U ,m∈M,t∈T , (17)
αu,n,t ={0, 1},∀u∈U ,n∈N ,t∈T , (18)
0≤αu,m,t +αu,n,t≤ 1,∀u∈U ,n∈N ,t∈T , (19)
T∑
t=1
τR u,m,t≥Dm,∀u∈U ,m∈M,t ∈T , (20)
T∑
t=1
τR u,n,t≥Dn,∀u∈U ,n∈N ,t∈T , (21)
where constrains (12) and (13) limit the ﬂight speed of each
UA V in the horizontal and vertical directions, while (14) to
(16) restrict their 3D coordinates. Constraints (17) and (18)
deﬁne the allocation factors, and (19) ensures that each UA V
communicates with only one MEC node within a time slot.
Finally, (20) and (21) indicate that the system must satisfy the
computing demands of all MEC nodes across time slots.
IV. P ROPOSED LGD FRAMEWORK AND LGD-D3QN
ALGORITHM
LLM
Initial prompt
P
arameter prompt
Initial reward 
f
unction
Reward function
DRL 
Feedback prompt
Final output
Self-refinement loop
Bad
GoodResult
1
2
3
4
5
6
7
8
9
[
Environment description]
[Task description]
[Environment parameter]
[Training feedback]
Fig. 2. Flowchart of the LGD framework algorithm.
The LGD framework is shown in Fig. 2, and the speciﬁc
process is as follows:
1) Initial input: Firstly, the description of the environment
and the task is input into the LLM as the initial prompt.
2) Initial reward function: Utilizing prompt engineering
enables LLMs to comprehend the task description out-
lined in the initial prompt, including the objectives and
constraints of the task. Subsequently, the LLM formu-
lates an initial reward function based on this prompt.
Taking DeepSeek-R1 as an example, the following re-
ward function is designed:
Rt =ηEE
t −λ1Pspeed−λ2Pbounds−λ3Ptask,
Pspeed =
U∑
u=1
(
max
(
0,v h
u,t−vh
max
)
+ max
(
0,v v
u,t−vv
max
)
+ max
(
0,v h
min−vh
u,t
)
+ max
(
0,v v
min−vv
u,t
))
,
Pbounds =
U∑
u=1
(max (0,x u,t−xmax) + max (0,x min−xu,t)
+ max (0,y u,t−ymax) + max (0,y min−yu,t)
+ max (0,z u,t−zmax) + max (0,z min−zu,t)),
Ptask =
M∑
m=1
max
(
0,D m−
T∑
t=1
τR u,m,t
)
+
N∑
n=1
max
(
0,D n−
T∑
t=1
τR u,n,t
)
, (22)
where λ1, λ2, and λ3 are the weights of speed penalty
Pspeed, boundary penalty Pbounds, and task penalty
Ptask, respectively.
2297
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:49:21 UTC from IEEE Xplore.  Restrictions apply. 
3) Parameter prompt: Encapsulating the environment pa-
rameters and the initial reward function as a parameter
prompt for input into the LLM.
4) Reward function: The LLM further evaluates the
weight settings in the reward function based on the
parameter prompt, and generates a new reward function.
5) Training: Guiding DRL training with reward function
generated by the LLM.
6) Result: DRL outputs results based on the new reward
function.
7) Feedback prompt: The output of the DRL is encapsu-
lated into feedback prompt.
8) Reward function ﬁne-tuning: The feedback prompt is
input into the LLM to reﬁne the reward function.
9) Final output: The iteration stops when the output of
DRL is deemed sufﬁciently good (as judged by the
LLM) or when the preset maximum number of iterations
is reached. The best performance across all iterations is
then returned as the ﬁnal output.
By applying the D3QN as a DRL method, the LGD-
D3QN algorithm is obtained. D3QN can effectively reduce
the estimation bias of Q-values by decoupling the action
advantage from the state value, thereby improving the stability
and efﬁciency of learning. The speciﬁc implementation of the
D3QN will not be elaborated upon here and can be referenced
in our previous work [11]. In the LGD-D3QN algorithm,
each UA V is considered as an agent. The state of each agent
includes the 3D coordinates of the UA V , the ﬂight speed, and
the association factor between the UA V and the MEC node.
The action space of the agent consists of the following parts:
1. Adjustment of the horizontal ﬂight speed, represented
as ∆vh
u,t∈{v1,−v1, 0}, where v1 is the speed variation
per time slot.
2. Adjustment of the vertical ﬂight speed, represented as
∆vv
u,t∈{v1,−v1, 0}.
3. Horizontal movement action, represented as ∆Lu,t∈{(
vh
u,tt, 0
)
,
(
−vh
u,tt, 0
)
,
(
0,v h
u,tt
)
,
(
0,−vh
u,tt
)
, (0, 0)
}
.
4. Vertical movement action, represented as ∆Hu,t ∈{
vv
u,tt,−vv
u,tt, 0
}
.
5. Selection of association factor with the human user m,
represented as αu,m,t∈{ 0, 1}.
6. Selection of association factor with the IoT device n,
represented as αu,n,t∈{ 0, 1}.
Every agent shares the same global reward. Only when the
entire group performs well can each agent obtain a high return.
This encourages them to explore behaviors that are beneﬁcial
to the group, even if these behaviors may be suboptimal for
individuals in the short term.
V. S IMULATION RESULT
For a fair comparison, all DRL hyperparameters and the
initial prompts fed into the LLM are kept consistent. The
operating range of UA Vs is (0 m ∼1000 m, 0 m ∼1000 m,
100 m∼150 m), v1 = 1 m/s. According to [2], Dm = 1∼10
Mbits, Dn = 1∼10 Mbits, α0 = -50 dBm, κ = 10−28, CC
u =
200, and fC
u = 3 GHz. According to [3], a = 9.61, b = 0.16,
Pbla = 79.86 W, ρ = 1.225 kg/m, s = 0.05, G = 0.503 m 2,
Pd/a = 11.46 W, Utip = 120 m/s, v0 = 4.3 m/s, d0 = 0.6, and
σ2 = -169 dBm/Hz.
0 300 600 900 1200 1500 1800
Episodes
0
50
100
150
200Average energy efficiency (kbps/Joule)
DeepSeek-R1
GPT-4o
Llama-3.1-70B
Claude-3.7-Sonnet
Qwen-2.5
Human-1
Human-2
Fig. 3. Energy efﬁciency curves of the LGD-D3QN with different LLMs.
0 50 100 150 200
Average energy efficiency(kbps/Joule)
0
0.2
0.4
0.6
0.8
1
CDF
DeepSeek-R1
GPT-4o
Llama-3.1-70B
Claude-3.7-Sonnet
Qwen-2.5
Human-1
Human-2
Fig. 4. CDF of energy efﬁciency for the LGD-D3QN with different LLMs.
Fig. 3 and Fig. 4 compare the impact of reward functions
generated by different LLMs on the D3QN training results
in the LGD-D3QN algorithm. Evidently, the utilization of
DeepSeek-R1 in the LLM provides the most signiﬁcant boost
in system energy efﬁciency. To demonstrate the superiority of
LLM in reward function generation, a comparison is made
with rewards designed by two human experts, where human 1
directly used energy efﬁciency as the reward function. Human
2 adds a weight less than one on the basis of human 1. If
the agent does not satisfy all the constraints, the reward is
calculated by multiplying the energy efﬁciency by this weight,
resulting in a penalty. As shown in Fig. 4, LGD-D3QN can
achieve an energy efﬁciency improvement of up to 43.5%
compared to human expert-driven DRL.
2298
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:49:21 UTC from IEEE Xplore.  Restrictions apply. 
0 300 600 900 1200 1500 1800
Episodes
0
50
100
150
200Average energy efficiency (kbps/Joule)
LGD-DQN
LGD-DDQN
LGD-D3QN
Fig. 5. Energy efﬁciency curves of the LGD framework with different DRLs.
Fig. 5 compares the energy efﬁciency improvements of
the LGD framework when utilizing different DRL methods.
To ensure a fair comparison, LGD-D3QN, LGD-DDQN, and
LGD-DQN all adopt DeepSeek-R1 as the LLM. The difference
is that the DRL methods of these algorithms are D3QN,
DDQN, and DQN. Compared with DDQN and DQN, D3QN
addresses the issues of overestimation and unstable conver-
gence. It is evident that the LGD-D3QN yields the largest
energy efﬁciency improvement, which can be attributed to the
superiority of the D3QN algorithm.
DeepSeek-R1
GPT-4o
Llama-3.1-70B
Claude-3.7-Sonnet
Qwen-2.5
0
200
400
600
800
1000
1200
1400
1600Number of tokens
Initial prompt
Parameter prompt
Feedback prompt
Fig. 6. The number of tokens for prompt segmentation in different LLMs.
The number of tokens divided by LLMs for different
prompts is shown in Fig. 6. It is evident that Qwen-2.5 exhibits
the highest number of prompt divisions, which stems from its
subword-level tokenization rules that inherently possess ﬁne-
grained segmentation properties. However, an excessive num-
ber of tokens may lead to information fragmentation, making
it difﬁcult for the model to capture long-range dependencies or
process the prompt effectively, ultimately impacting the quality
of the generated reward function. Compared to other LLMs,
DeepSeek-R1 has the fewest tokens generated from the prompt
division and achieves the best energy efﬁciency improvement.
This is due to the fact that, in certain cases, fewer tokens
can lead to more efﬁcient information encoding, enabling the
model to better capture key information and generate a more
reasonable reward function structure. Therefore, investigating
the impact of tokenization on LLM behavior is expected to be
a key focus of future research.
VI. C ONCLUSION
A closed-loop LLM-guided DRL framework is proposed
in this paper, and is applied within a multi-cluster MEC
network to evaluate its effectiveness. Different LLMs and
DRL methods are introduced into the LGD framework to
comprehensively evaluate their effects on improving system
energy efﬁciency. Compared with human experts, the LGD
framework can signiﬁcantly improve system energy efﬁcien-
cy. In the future, modeling of inter-cluster interactions, task
migration, or communication overhead in multi-cluster UA Vs
will be taken into consideration.

## § References

[1] P. Mach and Z. Becvar, “Mobile Edge Computing: A Survey on
Architecture and Computation Ofﬂoading,” IEEE Commun. Surveys
Tuts., vol. 19, no. 3, pp. 1628-1656, thirdquarter 2017.
[2] Z. Kuang, Y . Pan, F. Yang, and Y . Zhang, “Joint Task Ofﬂoading
Scheduling and Resource Allocation in AirCGround Cooperation UA V-
Enabled Mobile Edge Computing,” IEEE Trans. Veh. Technol., vol. 73,
no. 4, pp. 5796-5807, April 2024.
[3] H. Mei, K. Yang, Q. Liu, and K. Wang, “3D-Trajectory and Phase-
Shift Design for RIS-Assisted UA V Systems Using Deep Reinforcement
Learning,” IEEE Trans. Veh. Technol., vol. 71, no. 3, pp. 3020-3029,
March 2022.
[4] M. Li, N. Cheng, J. Gao, Y . Wang, L. Zhao, and X. Shen, “Energy-
Efﬁcient UA V-Assisted Mobile Edge Computing: Resource Allocation
and Trajectory Optimization,” IEEE Trans. Veh. Technol., vol. 69, no.
3, pp. 3424-3438, March 2020.
[5] Z. Zhang, Q. Zhang, J. Miao, F. R. Yu, F. Fu, J. Du, and T. Wu, “Energy-
Efﬁcient Secure Video Streaming in UA V-Enabled Wireless Networks:
A Safe-DQN Approach,” IEEE Trans. Green Commun.Netw., vol. 5, no.
4, pp. 1892-1905, Dec. 2021.
[6] C. Liu, Y . Zhong, R. Wu, S. Ren, S. Du, and B. Guo, “Deep Rein-
forcement Learning Based 3D-Trajectory Design and Task Ofﬂoading
in UA V-Enabled MEC System,” IEEE Trans. Veh. Technol., vol. 74, no.
2, pp. 3185-3195, Feb. 2025.
[7] A. T. Neumann, Y . Yin, S. Sowe, S. Decker, and M. Jarke, “An LLM-
Driven Chatbot in Higher Education for Databases and Information
Systems,” IEEE Trans. Educ., vol. 68, no. 1, pp. 103-116, Feb. 2025.
[8] S. Sun, R. Liu, J. Lyu, J. Yang, L. Zhang, and X. Li, “A large
language model-driven reward design framework via dynamic feedback
for reinforcement learning,” arXiv preprint arXiv:2410.14660, 2024.
[9] T. Xie, S. Zhao, C. H. Wu, Y . Liu, Q. Luo, V . Zhong, Y . Yang, and T. Yu,
“Text2reward: Reward shaping with language models for reinforcement
learning,” arXiv preprint arXiv:2309.11489, 2023.
[10] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP Altitude
for Maximum Coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6,
pp. 569-572, Dec. 2014.
[11] Y . Yao, K. Lv, S. Huang and W. Xiang, “3D Deployment and Energy
Efﬁciency Optimization Based on DRL for RIS-Assisted Air-to-Ground
Communications Networks,” IEEE Trans. Veh. Technol., vol. 73, no. 10,
pp. 14988-15003, Oct. 2024.
2299
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:49:21 UTC from IEEE Xplore.  Restrictions apply.
