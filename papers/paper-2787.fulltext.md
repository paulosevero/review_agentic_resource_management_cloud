---
paper_id: "paper-2787"
source_pdf_sha: "cc27f384a3a025be9876a93a9107c06ddeb0c5eb3923b68eaeb350a2ac9941fa"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 1
  page_count: 6
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2787 — fulltext
## §unknown-1

5262 IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. 75, NO. 3, MARCH 2026
LLM-Based Task Ofﬂoading and Resource Allocation in
Satellite Edge Computing Networks
Minghao Sun , Jinbo Hou , Kehai Qiu ,
Kezhi Wang , Senior Member , IEEE,
Xiaoli Chu , Senior Member , IEEE, and Zitian Zhang
Abstract—Satellite Mobile Edge Computing (MEC) networks offer a
promising solution for delivering global services to terrestrial Internet of
Things (IoT) terminals in 5G and beyond. However, satellite MEC systems
face challenges such as underutilization of resources and task congestion,
leading to resource waste and increased latency. In this paper, we investigate
the joint resource allocation and task ofﬂoading problem in multi-satellite
MEC networks, aiming to minimize the average latency of IoT terminals.
To solve the joint optimization problem involving IoT terminals’ task
ofﬂoading decisions, uplink transmission power and sub-channel alloca-
tion, and satellite computation resource allocation, we propose an iterative
optimization algorithm that uses the Lagrange multipliers method to opti-
mize the satellite computation resource allocation and a Large Language
Model (LLM) based optimizer to optimize the other variables in each
iteration. Prompts and templated parameters are designed to enhance the
LLM’s inference accuracy and generalization capability across scenarios
with varying numbers of satellites and IoT terminals. Simulation results
show that our proposed LLM-based algorithm outperforms benchmark
algorithms in convergence speed and average latency of IoT terminals.
Index Terms—Satellite mobile edge computing, task ofﬂoading, resource
allocation, large language model, Internet of Things.
I. I NTRODUCTION
Internet of Things (IoT) terminals have driven numerous intelligent
applications [1]. However, terrestrial communication networks fail to
provide reliable communication services for IoT terminals in remote
areas, such as disaster zones, oceans, and deserts. Low-Earth-Orbit
(LEO) satellite Mobile Edge Computing (MEC) networks can help
provide global service coverage for IoT terminals [2], [3]. Nonethe-
less, achieving efﬁcient resource allocation and task ofﬂoading while
meeting low-latency requirements remains challenging due to limited
communication and computation resources at both satellites and termi-
nals [4].
Received 8 April 2025; revised 31 July 2025 and 13 September 2025;
accepted 15 September 2025. Date of publication 19 September 2025; date of
current version 6 March 2026. This work was supported in part by the Horizon
Europe Research and Innovation Program under Grant 101086219 and Grant
101086228, in part by U.K. Engineering and Physical Sciences Research Council
under Grant EP/X038971/1 and Grant EP/Y028031/1, in part by Royal Society
International Exchanges Award under Grant IEC/NSFC/242607, in part by the
Innovate U.K. COMET Project under Grant 10099265, and in part by the Royal
Society Industry Fellowship under Grant IF R2 23200104. The review of this
article was coordinated by Prof. Jiawen Kang. (Corresponding authors: Xiaoli
Chu; Zitian Zhang.)
Minghao Sun, Jinbo Hou, and Xiaoli Chu are with the School of Electrical and
Electronic Engineering, The University of Shefﬁeld, S10 2TN Shefﬁeld, U.K. (e-
mail: msun39@shefﬁeld.ac.uk; jhou9@shefﬁeld.ac.uk; x.chu@shefﬁeld.ac.uk).
Kehai Qiu is with the Department of Computer Science and Technology,
University of Cambridge, CB2 1TN Cambridge, U.K., and also with the Brunel
University of London, UB8 3PH Uxbridge, U.K. (e-mail: kq218@cam.ac.uk).
Kezhi Wang is with the Department of Computer Science, Brunel University
of London, UB8 3PH Uxbridge, U.K. (e-mail: kezhi.wang@brunel.ac.uk).
Zitian Zhang is with the School of Information and Electronic Engineer-
ing, Zhejiang Gongshang University, Hangzhou 314423, China (e-mail: zitian.
zhang@mail.zjgsu.edu.cn).
Digital Object Identiﬁer 10.1109/TVT.2025.3612207
Some research has been conducted in this area. The authors in [5]
minimized latency and energy consumption in a satellite MEC network
by Breadth-First Search and greedy algorithms. The latency was min-
imized by using the Genetic Algorithm (GA) and Lagrange multiplier
method in [6] and by employing game theory and many-to-one match-
ing theory in [7]. The authors in [8] solved a weighted-sum latency
minimization problem for satellite-assisted vehicle-to-vehicle networks
by Reinforcement Learning. Under limited bandwidth, effective power
and spectrum allocation schemes are necessary to overcome co-channel
interference. However, the existing works [5], [6], [7], [8] did not
consider the impact of transmission power and spectrum allocation
on the data transmission rate or latency for ofﬂoading tasks from
terrestrial terminals to satellites. Moreover, existing algorithms suffer
from issues such as limited applicability, poor generalization, and
slow convergence. Large Language Models (LLMs) have emerged
as a promising approach to solve these issues with their contextual
learning and inference abilities, which have demonstrated outstanding
optimization capability for wireless networks [9], [10].
In this paper, we aim to minimize the average latency of IoT
terminals in a multi-satellite MEC network by optimizing the satel-
lites’ computation resource allocation and the IoT terminals’ task
ofﬂoading decisions, uplink sub-channel allocation, and transmission
power allocation. Given that the formulated problem is non-convex and
challenging to solve directly, we decompose it into two sub-problems:
the computation resource allocation problem and the joint task of-
ﬂoading, power allocation, and sub-channel allocation problem. The
former is proven to be convex and can be solved using the Lagrange
multiplier method to obtain a closed-form result. For the latter, due to
its complexity, traditional optimization algorithms often suffer from
prolonged computing time [11], while existing AI algorithms typi-
cally require substantial time for model training or ﬁne-tuning [12].
By harnessing the LLM’s inference and generalization capabilities
while avoiding the costs of dedicated model training, we propose an
LLM-based optimizer that utilizes structured templates, pre-designed
prompts, and an example pool to solve the second subproblem. An
alternating optimization algorithm is devised based on the solutions to
both sub-problems to solve the original problem. Simulation results are
provided to evaluate the proposed algorithm for varying numbers of
satellites and IoT terminals.
II. S YSTEM MODEL AND PROBLEM FORMULA TION
We consider a low-density satellite-MEC scenario in a remote
area. The network contains M LEO satellites, denoted by S =
{S1,S 2,...,S M},w h i c hs e r v eN IoT terminals sparsely distributed
on the ground at ﬁxed locations via I orthogonal sub-channels, as
s h o w ni nF i g .1. Each satellite has a computational capacity FSA T
(in CPU cycle/s). The set of IoT terminals is represented by T =
{T1,T 2,...,T N}.T h e n-th IoT terminal Tn has a task ψn with
data size εn (in bits) and required computational density ρ(in CPU
cycle/bit). Each terminal has a local computational capacity of FIoT
(in CPU cycle/s). An IoT terminal can either process its task locally
or ofﬂoad it to one of the satellites. The set of sub-channels is denoted
by A = {A1,A 2,...,A I}. Each sub-channel has a bandwidth of B
and can be employed by multiple IoT terminals simultaneously. One
IoT terminal can use multiple sub-channels to send the task data to
one satellite and can allocate various power across the sub-channels,
with the total transmission power constrained by P
IoT. The scheduling
0018-9545 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and similar technologi es.
Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index. html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, VOL. 75, NO. 3, MARCH 2026 5263
Fig. 1. Satellite Mobile Edge Computing Network.
period Δ is assumed to be sufﬁciently short such that the satellite-
terminal geometry and channel fading coefﬁcients can be regarded as
quasi-static [11]. At the beginning of each scheduling period, the binary
task ofﬂoading indicators αm,n and sub-channel allocation indicators
βn,i are updated by the system. Speciﬁcally, αm,n = 1i ft a s kψn is
ofﬂoaded to satelliteSm, otherwiseαm,n = 0;βn,i = 1 if sub-channel
Ai is allocated for transmitting task ψn, otherwise, βn,i = 0.
A. Transmission Model
Since the distance from a satellite to an IoT terminal is much longer
than that between any two IoT terminals, we assume that all the IoT
terminals have approximately the same distance to the same satellite.
The distance from an IoT terminal to satelliteSm is denoted bydm and
derived as [12]:
dm =
√
R2
e +(Re +Rh)2 −2Re(Re +Rh)cos θm, (1)
θm = arccos
( Re
Re +Rh
·cosem
)
−em, (2)
whereRe andRh represent the radius of the Earth and the height of the
satellite orbit above ground, respectively;θm is the geocentric angle of
satellite Sm,a n dem is the elevation angle of Sm to an IoT terminal
with lower limit emin [13].
The channel gain of sub-channel Ai between satellite Sm and IoT
terminal Tn is given by:
Gi
m,n = Gn
( c
4πfcdm
)2
(|hi
m,n|)2, (3)
where Gn is the antenna gain (in dBi) of IoT terminal Tn, fc is the
carrier frequency,c denotes the speed of light, and hi
m,n represents the
Rician fading with factor K.
If IoT terminal Tn ofﬂoads its task to satellite Sm, i.e., αm,n = 1,
then the data rate from Tn toSm is given by:
Cm,n=
I∑
i=1
Blog2
⎛
⎜⎜⎜⎝1+ αm,nβn,iPn,iGi
m,n
N∑
n′̸=n
M∑
m′ =1
αm′ ,n′βn′ ,iPn′,iGi
m′ ,n′ +N0
⎞
⎟⎟⎟⎠, (4)
where N0 denotes the additive white Gaussian noise (AWGN) power
at the satellite receiver, and Pn,i denotes the transmission power from
IoT terminal Tn in sub-channel Ai.
In the uplink, the transmission latency δTr a n s
m,n of task ψn ofﬂoaded
to satellite Sm is:
δTr a n s
m,n = εn
Cm,n
. (5)
The downlink transmission latency is neglected since the compu-
tation result size is typically much smaller than the uplink task data
size [6].
B. Problem F ormulation
If task ψn is processed locally, the computation time is:
δIoT
n = εnρ
FIoT
, (6)
If task ψn is ofﬂoaded to satellite Sm, the computation time is:
δSA T
m,n = εnρ
F SA T
m,n
, (7)
where F SA T
m,n represents the computation resource (in CPU cycle/s) of
satelliteSm allocated for processing task ψn.
The latency experienced by an IoT terminal includes the transmission
latency and computation latency of its task. The latency of terminal Tn
is given by:
δn =
M∑
m=1
αm,n(δSA T
m,n +δTr a n s
m,n )+
(
1−
M∑
m=1
αm,n
)
δIoT
n . (8)
To minimize the average latency of all IoT terminals, we formulate
an optimization problem as follows,
min
P ,F ,α,β
1
N
N∑
n=1
δn, (9a)
s.t. 0 ≤
I∑
i=1
βn,iPn,i ≤PIoT,∀n ∈{1,...,N }, (9b)
0 ≤
N∑
n=1
αm,nF SA T
m,n ≤FSA T,∀m ∈{1,...,M }, (9c)
M∑
m=1
αm,n ≤1,∀n ∈{1,...,N }, (9d)
δn ≤Δ,∀n ∈{1,...,N }, (9e)
αm,n,βn,i ∈{0, 1}, (9f)
where P = {Pn,i|n = 1,...,N ;i = 1,...,I }, F = {F SAT
m,n |m =
1,...,M ;n= 1,...,N }, α={αm,n|m = 1,...,M ;n= 1,...,N },
andβ= {βn,i|n = 1,...,N ;i = 1,...,I }. Constraint (9b) limits the
total power allocated by a terminal across all sub-channels;(9c) imposes
the computational capacity of each satellite; (9d) ensures that a task
can be ofﬂoaded to at most one satellite; (9e) ensures that a task must
be processed within a scheduling period; and (9f) speciﬁes the binary
indicators.
III. A LGORITHM DESIGN
The problem in (9) is non-convex due to the discrete solution space
imposed by the binary variables [11]. To address this, it is divided
into two sub-problems: the satellite computation resource allocation
problem and the joint task ofﬂoading, power allocation, and sub-channel
allocation problem. We ﬁrst show that the former is convex and obtain
a closed-form solution using the Lagrange multiplier method. Then, a
novel LLM-based optimizer is proposed to solve the latter.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply. 
5264 IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, VOL. 75, NO. 3, MARCH 2026
Fig. 2. The LLM-based framework for joint optimization of task ofﬂoading, power allocation, and sub-channel allocation.
A. Satellite Computation Resource Allocation
For given values of α,βand P , problem (9) reduces to:
min
F
1
N
N∑
n=1
M∑
m=1
αm,nδSA T
m,n,
s.t. (9c). (10)
The second derivative of any element within the summation in (10)
with respect to F SA T
m,n is:
∂2(αm,nδSA T
m,n)
∂FSA T
m,n
2 = 2αm,nεnρ
F SA T
m,n
3 ≥0, (11)
whereαm,n ≥0,εn > 0,ρ>0, andF SA T
m,n > 0. So the Hessian matrix
of the objective function in (10) is a positive semi-deﬁnite matrix, and
problem (10) is convex. The Lagrangian function L(F SA T
m,n , λm) with
Lagrange multiplier λm is as follows:
L(F SA T
m,n , λm)= 1
N
( M∑
m=1
N∑
n=1
αm,nδSA T
m,n
)
+
M∑
m=1
λm
( N∑
n=1
αm,nF SA T
m,n −FSA T
)
. (12)
Taking the partial derivatives of L(F SA T
m,n , λm) with respect to F SA T
m,n
and λm, and setting the results to zero, we have:
⎧
⎪⎪
⎪
⎨
⎪⎪
⎪
⎩
∂L(F
SA T
m,n , λm)
∂FSA T
m,n
= −αm,nεnρ
F SA T
m,n
2 + λmαm,n = 0,
∂L(F SA T
m,n , λm)
∂λm
=
N∑
n=1
αm,nF SA T
m,n −FSA T= 0.
(13)
By solving the above equations, we obtain the optimal satellite compu-
tation resource allocation:
˜F SA T
m,n = FSA T
√εnρ
N∑
k=1
αm,k
√εkρ
. (14)
B. Joint Task Ofﬂoading, Power Allocation and Sub-Channel
Allocation
For givenF , problem (9) reduces to :
min
P ,α
1
N
N∑
n=1
δn, (15a)
s.t. 0 ≤
I∑
i=1
Pn,i ≤PIoT,∀n ∈{1,...,N },
(9c), (9d), (9f), (15b)
where for simplicity, the sub-channel allocation indicators βn,i are
omitted under the assumption that βn,i = 0i f Pn,i = 0a n dβn,i = 1
ifPn,i > 0.
Problem (15) is still non-convex due to the binary constraint and
fractional sum terms. To solve it, we propose an LLM-based optimizer
a ss h o w ni nF i g .2 and detailed below.
The Generator Module consists of an LLM-based decision maker
that uses prompts and an example pool as inputs to generate task
ofﬂoading and power allocation solutions as outputs. The initial prompt
includes the task description that outlines the objective based on (15),
the environment description that details the system model with key
parameters for customization, and the output format that speciﬁes the
template for generated solutions. The example pool contains an initial
solution, i.e., the best solution to (15) among 100 randomly generated
solutions, denoted by α
e,Pe,a n dδe.
The Evaluation Module is composed of an LLM output extractor
and a performance evaluation system. To avoid redundant texts due
to hallucinations, the LLM extractor uses a task ofﬂoading extraction
prompt and a power allocation extraction prompt to extract the intended
solutions from the output text generated by the LLM. The performance
of the extracted solutions αand P is evaluated by substituting them
into (15), and calculating the average latency δ=( ∑
N
n=1 δn)/N;i f
any constraint of (15) is violated, δ= ∞.
The LLM-based iterative algorithm begins by inputting the initial
prompt and example pool into the LLM-based decision maker. The
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, VOL. 75, NO. 3, MARCH 2026 5265
Algorithm 1: LLM-Based Alternating Optimization.
Input:M ,N ,I,ϵ, max_iterations
1: Initialize example pool (αe,P e,δe) and initial prompt
2: Set iteration counter i ← 0, no_update_counter ← 0
3: Prompt i ← initial prompt
4: repeat
5: Query LLM with Prompt i and extract (αnew,P new)
6: if any constraint of (15) is violated then
7: Set δnew ←∞
8: else
9: form = 1 : M andn = 1 : N do
10: F SA T
m,n ← (14)
11: end for
12: Compute average latency: δnew ← (8) and (9)
13: end if
14: if δnew <δe then
15: Update: (αe,P e,δe) ← (αnew,P new,δnew)
16: no_update_counter ← 0
17: else if (αnew,P new,δnew)=( αe,P e,δe) then
18: Prompt i+1 ← initial prompt::reminder prompt
19: no_update_counter ← no_update_counter+1
20: else
21: Prompt i+1 ← initial prompt::expert prompt
22: no_update_counter ← no_update_counter+1
23: end if
24: i ← i+ 1
25: until no_update_counter≥ϵ or i ≥max_iterations
26: returnαe,P e, F,δe
decision maker’s output is then evaluated by the Evaluation Module,
which compares δwith the average latency δe of the solution in the
example pool and determines how the inputs to the decision maker
should be updated in the next iteration as follows:
r If δ>δe: An expert prompt, based on domain-speciﬁc knowl-
edge, will be input into the Generator Module.
r If δ<δe: The extracted solutions αand P replace αe and Pe
in the example pool, respectively.
r If δ= δe: If α= αe and P = Pe, a reminder prompt will be
input into the Generator Module to prevent the LLM from being
trapped in existing solutions; otherwise, the expert prompt will
be input into the Generator Module.
The iteration process terminates when the example pool is not
updated for ϵ consecutive iterations or when the number of iterations
reaches a preset limit. The example pool returns the ﬁnal solution to
problem (15). Based on the solutions to the two sub-problems, an alter-
nating optimization algorithm is devised to solve (9). The pseudo-code
is shown in Algorithm 1.
Since most existing commercial LLM APIs are memoryless, both
task ofﬂoading and power allocation solutions must be generated
within a single conversation (i.e., a series of prompt-response ex-
changes) with the LLM. The example pool can help maintain con-
tinuity across iterations. Some open-source localized models like
Llama 3 can mitigate this issue, but currently lag behind in inference
performance.
IV . SIMULA TIONRESULTS
This section presents the performance evaluation of the proposed
LLM-based alternating optimization algorithm (LLM), building on(14)
TABLE I
SIMULA TION PARAMETERS[6], [12], [13]
and the LLM-based optimizer in Fig. 2. It is well recognized that em-
ploying commercial LLM APIs introduces additional network latency
due to data exchanges with cloud servers, whereas local deployment of
LLMs entails signiﬁcant hardware and maintenance costs. Therefore,
commercial APIs are particularly suitable for edge devices with limited
computational resources, offering access to high-performance LLMs
at relatively low costs. Conversely, local deployment ensures greater
data conﬁdentiality and, by interacting directly with local devices,
signiﬁcantly reduces communication overhead, making it preferable in
latency-sensitive and/or safety-critical scenarios. Given the substantial
hardware requirements for deploying high-performance LLMs locally,
this study utilizes different LLM models through commercial APIs for
performance evaluation. Nevertheless, our proposed algorithm is com-
patible with local deployment-based LLMs too. By testing three widely
used models, GPT-4o, LLaMA3.170B, and DeepSeek-R1-0528 under
the same prompt design and algorithmic framework, we observe that
only GPT-4o successfully converged to an optimized solution, where
both the LLaMA3.170B and DeepSeek-R1-0528 failed to complete the
algorithm due to hallucinations. The LLaMA3.170B model sometimes
returned wrong dimensions of decision matrices, while the DeepSeek-
R1-0528 model often generated non-binary values of αwithin the ﬁrst
5 iterations, both failing to complete the algorithm. Therefore, GPT-4o
is adopted in the following simulations due to its superior reliability
and reasoning performance across iterative optimization tasks. The
benchmarks for performance comparison include the GA, where the
initial population size is set at 400 with a crossover probability of
0.5 and a mutation probability of 0.2; the Deep Deterministic Policy
Gradient (DDPG) algorithm with a greedy exploration strategy, where
the exploration rate is 0.05, and both the Actor and Critic networks
contain three layers with the learning rate of 10
−5; Random Choice
(RC), where each task has an equal probability of being processed
locally or ofﬂoaded to one of the satellites, and the other optimization
variables are uniformly distributed within their allowed value ranges;
Processing All Locally (PAL), where each IoT terminal processes its
task locally and all the variables in problem (9) are set to zero. In the
simulation, the task data size ϵ
n is uniformly distributed between 0.3
MB and 0.6 MB, and other parameters are shown in Table I unless
otherwise speciﬁed.
Fig. 3 shows the convergence performance of the proposed LLM-
based algorithm for different values of temperature t, which is a
hyperparameter that controls the sharpness of the LLM’s output prob-
ability distribution, and for different prompt (DP) wording, in com-
parison with GA and DDPG. Higher temperature values lead to more
diverse and stochastic outputs. Our simulations tested temperature
values of 0.5, 0.7, 1, 1.3, and 1.5 and found that for t = 1.3 and
1.5, the LLM-based algorithm failed to complete due to occasional
dimension mismatches in the generated solutions. For t = 0.5, 0.7,
and 1, the LLM-based algorithms converge within 40 to 200 iter-
ations, signiﬁcantly faster than both DDPG and GA. The results
indicate that t = 1 offers the best balance between convergence
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply. 
5266 IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, VOL. 75, NO. 3, MARCH 2026
Fig. 3. Convergence of the LLM-based algorithm for different temperature t
and different prompt (DP) wording, GA, and DDPG forM = 3,N = 10,I = 4.
Fig. 4. Mean latency and standard deviation vs. the number of IoT terminals
for M = 3,I = 4.
Fig. 5. Average latency for different values of ( N, M, I ).
speed and latency minimization performance. Therefore, in the sub-
sequent experiments, the LLM-based algorithm adopts t = 1. Addi-
tionally, the performance of the LLM-based algorithm with different
prompt wording is close to that with the prompt wording deﬁned
in Fig. 2, suggesting that the LLM-based algorithm is not sensitive
to the wording of prompts as long as the underlying intent remains
consistent.
Fig. 4 shows the mean latency and standard deviation achieved by
different algorithms across 10 experimental runs for 5, 10, 15, and
20 IoT terminals served by 3 satellites. It shows that as the number
of terminals increases, the average latency rises for all the considered
schemes. This is mainly due to increased co-channel interference. It
also shows that the proposed LLM-based algorithm achieves the lowest
mean latency and smallest standard deviation for every considered
number of IoT terminals, followed by GA and DDPG. Although DDPG
has been widely used for solving non-convex problems, it is prone to
being stuck in local optima and is highly sensitive to hyperparameter
settings. In contrast, the proposed LLM-based algorithm encourages
broader solution exploration when repetitive solutions are detected and
avoids getting stuck in local optima through prompt-based adaptations.
Fig. 5 shows the average latency achieved by four schemes for
different values of ( N,M,I ). The proposed LLM-based algorithm
consistently outperforms RC across all scenarios. For the scenarios
of (20, 6, 4), (20, 6, 8), and (20, 3, 8), as the decision matrices contain
signiﬁcantly more ﬂoat numbers, increasing the likelihood of halluci-
nations or invalid outputs, the LLM-based algorithm is outperformed
by GA.
V. C ONCLUSIONS AND FUTURE WORK
In this work, we have proposed a novel LLM optimizer combined
with the Lagrange multiplier method to minimize the average latency
of IoT terminals in a multi-satellite MEC network. Simulation results
demonstrate that the LLM-based alternating optimization algorithm
converges signiﬁcantly faster than both GA and DDPG while obtain-
ing a lower average latency for the IoT terminals. The LLM-based
algorithm exhibits strong adaptability and effectively achieves the
optimization objective across varying numbers of IoT terminals and
satellites. Our results also show that for high-dimensional scenarios,
it would be necessary to adopt a multi-agent approach—a promising
direction for future work. In addition, we plan to investigate other
practical issues in satellite MEC networks, such as the response time
of LLMs. It is mainly determined by the latency of generating the ﬁrst
token and the subsequent time required to produce the full output text,
which scales with the number of output tokens [14].

## § References

[1] F. Guo, F. R. Y u, H. Zhang, X. Li, H. Ji, and V . C. M. Leung, “Enabling
massive IoT toward 6G: A comprehensive survey,” IEEE Internet Things
J., vol. 8, no. 15, pp. 11891–11915, Aug. 2021.
[2] W.-C. Chien, C.-F. Lai, M. S. Hossain, and G. Muhammad, “Heteroge-
neous space and terrestrial integrated networks for IoT: Architecture and
challenges,” IEEE Netw., vol. 33, no. 1, pp. 15–21, Jan./Feb. 2019.
[3] M. De Sanctis, E. Cianca, G. Araniti, I. Bisio, and R. Prasad, “Satellite
communications supporting Internet of Remote Things,” IEEE Internet
Things J., vol. 3, no. 1, pp. 113–123, Feb. 2016.
[4] K. Zhang et al., “Energy-efﬁcient ofﬂoading for mobile edge computing in
5G heterogeneous networks,” IEEE Access, vol. 4, pp. 5896–5907, 2016.
[5] X. Gao et al., “Hierarchical dynamic resource allocation for computation
ofﬂoading in LEO satellite networks,” IEEE Internet Things J. , vol. 11,
no. 11, pp. 19470–19484, Jun. 2024.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, VOL. 75, NO. 3, MARCH 2026 5267
[6] L. Zhao, Y . Liu, A. Hawbani, N. Lin, W. Zhao, and K. Y u, “QoS-aware
multi-hop task ofﬂoading in satellite-terrestrial edge networks,” IEEE
Internet Things J., vol. 11, no. 19, pp. 31453–31466, Oct. 2024.
[7] S. Zhang, G. Cui, Y . Long, and W. Wang, “Joint computing and communi-
cation resource allocation for satellite communication networks with edge
computing,” China Commun., vol. 18, no. 7, pp. 236–252, Jul. 2021.
[8] G. Cui, Y . Long, L. Xu, and W. Wang, “Joint ofﬂoading and resource
allocation for satellite assisted V ehicle-to-V ehicle communication,”IEEE
Syst. J., vol. 15, no. 3, pp. 3958–3969, Sep. 2021.
[9] S. Xu, C. K. Thomas, O. Hashash, N. Muralidhar, W. Saad, and N.
Ramakrishnan, “Large multi-modal models (LMMs) as universal foun-
dation models for AI-native wireless systems,” IEEE Netw., vol. 38, no. 5,
pp. 10–20, Sep. 2024.
[10] L. Qiao, M. B. Mashhadi, Z. Gao, C. H. Foh, P . Xiao, and M. Bennis,
“Latency-aware generative semantic communications with pre-trained
diffusion models,” IEEE Wireless Commun. Lett. , vol. 13, no. 10,
pp. 2652–2656, Oct. 2024.
[11] Y . Zhang, H. Zhang, K. Sun, J. Huo, N. Wang, and V . C. M. Leung, “Partial
computation ofﬂoading in satellite-based three-tier cloud-edge integration
networks,” IEEE Trans. Wireless Commun. , vol. 23, no. 2, pp. 836–847,
Feb. 2024.
[12] Z. Zhao, M. Feng, C. Ke, Z. Chen, and T. Jiang, “Federated deep recurrent
Q-learning for task partitioning and resource allocation in satellite mobile
edge computing assisted industrial IoT,” IEEE Internet Things J., vol. 11,
no. 15, pp. 26444–26458, Aug. 2024.
[13] J. M. Gongora-Torres, C. V argas-Rosales, A. Aragón-Zavala, and
R. Villalpando-Hernandez, “Link budget analysis for LEO satellites
based on the statistics of the elevation angle,” IEEE Access , vol. 10,
pp. 14518–14528, 2022.
[14] H. Zhou et al., “Generative AI as a service in 6G edge-cloud: Generation
task ofﬂoading by in-context learning,” IEEE Wireless Commun. Lett. ,
vol. 14, no. 3, pp. 711–715, Mar. 2025.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:07:06 UTC from IEEE Xplore.  Restrictions apply.
