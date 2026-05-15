---
paper_id: "paper-2936"
source_pdf_sha: "7286f227fa0e7ca63d708d937ddde743efdd96a42f000ee7620686e340393dc4"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 1
  page_count: 10
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2936 — fulltext
## §unknown-1

IEEE Network • xx/xx xxxx
1
0890-8044 © 2026 IEEE. All rights reserved, including rights for text and data mining,  
and training of artificial intelligence and similar technologies.
Abstr Act
Traditional task offloading in Internet of Energy 
(IoE) edge environments struggles to accom -
modate heterogeneous user tasks and dynamic 
system conditions. Although Large Language 
Models (LLMs) offer potential solutions, their 
deployment is hindered by the dynamic resource 
constraints and stringent Quality of Service (QoS) 
requirements of IoE. Retrieval-augmented gen-
eration (RAG) enables LLM to overcome these 
limitations. In this paper, we propose an RAG-  
empowered adaptive task offloading framework. 
First, the framework transforms raw IoE-collected 
data into LLM-comprehensible textual inputs. Sec -
ond, we design an intelligent preference-matching 
module that guides RAG to retrieve relevant 
knowledge and cases using key QoS features. 
Third, we build a composite knowledge vector 
database with both positive and negative expe -
riences. We introduce a failure severity value 
to quantify the importance of counterexamples 
and enhance decision-making robustness. Finally, 
we design a hybrid knowledge prompt genera -
tion module. It utilizes a hierarchical filtering 
strategy and optimizes the ranking of retrieved 
knowledge for comprehensive prompts. Exper -
imental results demonstrate that our proposed 
framework significantly outperforms baselines, 
increasing cumulative reward by 48.4% while 
reducing latency and energy consumption by 
44.8% and 50.9%, respectively.
Introduct Ion
With the rapid development of the Internet of 
Energy (IoE), the energy system is undergoing 
a key transformation [1]. IoE integrates energy 
production, consumption, and communication 
for multi-energy complementarity and efficient 
coordination [2]. However, IoE faces challenges 
from massive heterogeneous data and complex 
computing tasks, overburdening traditional cloud 
architectures. Edge computing (EC) is a key tech-
nology addressing these challenges. EC moves 
resources closer to the network edge, reducing 
data transmission latency and improving system 
responsiveness. T ask offloading is a critical EC 
technique. It transfers tasks from user devices to 
edge servers, ensuring efficient resource alloca-
tion and performance.
However, existing artificial intelligence-based 
task offloading struggles with key IoE challenges. 
First, dynamic and heterogeneous environments 
lead to constantly changing resources and net -
work conditions [3] . This challenges static or 
rule-based offloading strategies. Second, diverse 
user tasks have differentiated quality of service 
(QoS) requirements, including latency, energy, 
and security. This diversity makes it difficult for a 
single optimization objective to suit all scenarios, 
resulting in a lack of fine-grained adaptability [4]. 
Finally, achieving an optimal balance among mul -
tiple conflicting QoS objectives, while ensuring 
real-time and accurate decision-making, remains a 
critical and unresolved problem [5].
Large language model (LLM) has demonstrated 
strong capabilities in language understanding 
and reasoning by learning rich world knowledge 
from large-scale text corpora. However, apply -
ing LLM directly to task offloading in the IoE 
remains challenging due to hallucination issues, 
lack of real-time data support, and limitations in 
interpreting domain-specific numerical informa-
tion. Retrieval-augmented generation (RAG) is a 
promising solution [6]. RAG integrates updatable 
knowledge into the LLM inference process. This 
enhances access to accurate, real-time domain 
knowledge [7]. It also improves reasoning accu-
racy and interpretability. In task offloading, RAG 
enables the LLM to perceive network states and 
historical knowledge. This supports timely and 
reliable decision-making.
RAG-empowered LLMs show great potential 
for IoE offloading. However, several challenges 
persist [8]. First, converting heterogeneous states 
into LLM-interpretable inputs is non-trivial. Second, 
achieving accurate and QoS-aware knowledge 
retrieval under diverse and time-varying conditions 
is difficult. Third, constructing a knowledge base 
that accumulates experience and quantifies failure 
severity to improve robustness remains challenging. 
Finally, efficient retrieval of both positive and neg -
ative historical experiences is essential to improve 
decision accuracy and professionalism.
To address these challenges, this paper 
proposes an RAG-empowered adaptive task 
Adaptive Task Offloading for Edge Computing in Internet of Energy via  
Retrieval-Augmented Generation
Xiongjie Zhou , Xin Guan , Ning Wang, Hongyang Chen , Tomoaki Ohtsuki , and Yan Zhang
LARGE AI MODELS FOR THE IOE
Digital Object Identifier:
10.1109/MNET.2026.3665502
Xiongjie Zhou and Xin Guan (corresponding author) are with the School of Computer and Big Data, Heilongjiang University, Harbin 
150080, China; Ning Wang is with State Grid Heilongjiang Electric Power Company Ltd., Harbin 150080, China; Hongyang Chen is with 
Zhejiang Laboratory, Hangzhou, Zhejiang 311121, China; Tomoaki Ohtsuki is with the Department of Information and Computer Science, 
Keio University, Yokohama 223-8522, Japan; Yan Zhang is with the School of Information and Communication Engineering, University of 
Electronic Science and Technology of China, Chengdu 611731, China.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
2
offloading framework in EC for the IoE. The 
framework efficiently transforms dynamic data 
into LLM-understandable inputs. It incorporates 
a novel hybrid retrieval mechanism. This matches 
positive and negative historical experiences 
precisely. This design enables LLM to generate 
professional, reliable, and risk-aware strategies. 
The main contributions are as follows.
1. In this paper, we propose an RAG-empow -
ered adaptive task offloading framework for 
the IoE. The framework converts numeri -
cal environment states and task demands 
into LLM-comprehensible semantic inputs, 
thereby enabling sophisticated reasoning 
and intelligent decision-making.
2. We design an intelligent preference-aware 
retrieval module. It integrates semantic sim-
ilarity between knowledge entries, contex -
tual queries, and task QoS preferences. This 
module prioritizes knowledge aligned with 
task requirements to enhance retrieval accu-
racy and system adaptability in dynamic, 
heterogeneous environments.
3. Our proposed composite knowledge 
base incorporates both positive and neg -
ative experiences, utilizing a novel failure 
severity metric to quantify negative cases. 
This mechanism enhances decision-making 
robustness by guiding the LLM to avoid 
high-risk strategies.
4. We develop a hybrid prompt generation 
module that employs hierarchical filtering 
and dual-ranking strategies for positive and 
negative cases. By optimizing knowledge 
ranking based on relevance and failure 
severity, the module constructs comprehen-
sive prompts that yield reliable offloading 
decisions.
The rest of this paper is organized as follows. 
The section “Related Work ” details the applica-
tion and latest progress of RAG technology in 
the IoE. The section “RAG-Empowered Adaptive 
Task Offloading Framework ” presents the pro -
posed RAG-empowered adaptive task offloading 
framework, and its core modules. The section 
“Performance Evaluation” presents the experiment 
design and performance evaluation results. Finally, 
section “Conclusion and Future Work” summarizes 
the work and outlines future research directions.
r el Ated  Work
RAG effectively addresses the limitations of 
LLMs in accessing real-time and domain-specific 
knowledge. Huang et al. [6] propose a 6G-ori-
ented RAG deployment framework to enhance 
service quality via data fusion and dynamic knowl-
edge base management. However, the real-time 
integration of heterogeneous multi-source data 
for knowledge base updates remains challeng -
ing. Ouyang et al. [9] propose an adaptive RAG 
framework, balancing LLM quality and latency in 
edge environments. This uses multi-level retrievers 
and online optimization. Managing this complex -
ity may introduce considerable system overhead. 
Liu et al. [10] propose an adaptive context cach-
ing framework using deep reinforcement learning 
(DRL). It improves cache hit rates and reduces 
retrieval latency. However, its performance highly 
depends on accurate user demand prediction. 
Alabbasi et al. [7] propose a telecom RAG system 
using a two-stage retriever. It enhances context 
retrieval and open-domain query performance. 
Handling ultra-long contexts still poses computa-
tional challenges on edge devices.
The integration of RAG has emerged as a 
promising approach to enhance LLM-based 
decision-making in complex task offloading sce -
narios. He et al. [11]  utilized active reasoning 
with reward-free guidance to optimize LLM-based 
offloading, though its generalization in volatile 
IoE environments remains unverified. Zeeshan 
et al. [8] propose an RAG framework that inte -
grates LLM with domain knowledge such as 
wireless standards and research publications to 
achieve resource optimization in 6G and future 
networks. Challenges persist, including real-time 
knowledge base updates and unbiased retrieval. 
Mitigating LLM hallucinations also remains unre -
solved. Zhang et al. [12] propose an interactive AI 
framework that includes pluggable LLM and RAG 
modules for constructing knowledge bases and 
contextual memory. It supports optimization prob-
lem design in next-generation networks. However, 
it faces computational overhead and real-time effi-
ciency bottlenecks in large-scale scenarios.
Although existing studies have made significant 
progress in applying LLM to task offloading, sev -
eral critical challenges remain.
• Low Robustness:  Most methods still lack 
generalizability and robustness when 
deployed in complex and dynamic edge 
environments.
• Retrieval Inaccuracy: Retrieval timeliness 
and accuracy are insufficient. This leads to 
information staleness and potential LLM 
biases.
• Static Knowledge:  Knowledge base con -
struction and dynamic updating require fur -
ther exploration.
To bridge these gaps, we propose an RAG-  
empowered adaptive task offloading framework. 
Unlike prior works, our framework integrates 
numerical-to-semantic conversion, QoS-aware 
matching, and a failure-aware composite knowl-
edge base to ensure precise, risk-aware, and 
robust decision-making in the IoE.
r AG-empo Wered  Ad Apt Ive  tAsk  o fflo Ad In G 
fr Ame Work
We propose an innovative RAG-empowered 
adaptive task offloading framework. As illus -
trated in Fig. 1 , it adopts a modular design. This 
framework integrates LLM reasoning with RAG 
knowledge enhancement to address IoE dynamic 
challenges. This facilitates intelligent strategy 
generation. The system uses a centralized edge 
intelligence architecture. The RAG-LLM module 
is deployed on a centralized edge server. It gener -
ates and distributes strategies to local EC servers 
time-slottedly. In this architecture, communication 
between the EC server and user equipment relies 
on wireless links, while communication between 
EC servers uses wired connections. Existing stud-
ies have shown that the communication overhead 
between edge servers negligible in most task off-
loading scenarios [13].
The framework’s operation proceeds as fol-
lows: We first convert real-time environmental 
states, task parameters, and QoS preferences 
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
3
into a semantic query text, Q . Leveraging a 
pre- constructed vectorized knowledge base con-
taining fundamental knowledge and historical 
cases, the system then performs QoS-aware rel-
evance matching to retrieve the most pertinent 
base knowledge, successful (Positive), and failed 
(Negative) historical cases. These retrieved texts 
are structured and integrated with Q  to form a 
comprehensive contextual prompt, P . This P  is fed 
into the LLM, which analyzes the scenario and 
contextual knowledge to output the optimal off -
loading strategy S  (including selection, resource 
allocation, and power control) and its interpreta-
ble rationale R. Finally, after execution, the system 
monitors outcomes and evaluates the failure 
degree. The execution context and performance 
feedback update the knowledge base.
The four key innovative modules of our frame -
work are detailed below.
Intell IGent  context -AWAre  Query  Gener AtIon  m odule
In the IoE, EC environments continuously generate 
massive heterogeneous real-time data, typically 
in the form of numerical arrays, images, or vid-
eos. However, LLMs have inherent limitations 
in processing such unstructured or non-textual 
data, hindering understanding and reasoning. We 
focus on numerical array data, including device 
states and task states. To bridge the seman -
tic gap between numerical data and the textual 
processing capabilities of LLM, we propose an 
intelligent context-aware query generation mod-
ule. As illustrated in Fig. 2, this module transforms 
data through the following steps:
1. Predefined Query Templates and Seman-
tic Mapping: This module uses structured 
query templates. For each numerical input 
feature, the module establishes fine-grained 
semantic mapping rules. For example, based 
FIGURE 1. RAG-empowered adaptive task offloading framework in EC for the IoE.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
4
on the value range of the device’s residu -
al energy, it maps the value to qualitative 
descriptions such as “sufficient energy” or 
“insufficient energy”.
2. QoS Preference Emphasis:  The module 
highlights the primary optimization objec -
tives in the generated query texts according 
to the explicit QoS weight factors provided 
in the input data. For instance, if the weight 
for latency is higher than that for energy 
consumption, the query will explicitly state 
that “the primary objective of this task off -
loading is to minimize latency, where reduc -
ing latency is more critical.”
Through these mechanisms, the intelligent 
context- aware query generation module success -
fully transforms complex raw data into structured 
and semantically interpretable inputs for LLM. The 
resulting semantic query texts are then encoded 
into context query embedding vectors, denoted 
as Eoriginal.
Qo s-AWAre  Intell IGent  tendency  m Atch In G m odule
Sole reliance on semantic similarity challenges 
accurate knowledge retrieval. We propose the 
QoS-aware intelligent tendency matching module. 
It biases retrieval toward entries highly aligned 
with task QoS objectives. The module dynami-
cally combines similarities between the original 
query and the QoS preference query. This steers 
results toward matching QoS goals. The specific 
implementation steps are as follows:
1. Generation of QoS-Preference Query Embed-
dings: Based on the task’s QoS preference, 
we predefine two typical descriptions repre -
senting distinct QoS orientations: minimizing 
latency and minimizing energy consumption. 
The descriptions are given as follows:
• This task highly prioritizes minimiz -
ing latency and requires extremely fast 
response times.
• This task highly prioritizes minimizing 
energy consumption and requires high 
energy efficiency.
These textual descriptions are embedded 
using a sentence embedding model to gen-
erate the corresponding QoS-preference 
query embedding vector, denoted as E QoS.
2. Multi-Dimensional Similarity Evalua -
tion and Weighted Fusion of Knowledge 
Entries: For each knowledge entry K i in the 
vector knowledge base, with embedding 
vector EKi, we simultaneously compute its 
similarity with two query vectors. First, the 
cosine similarity between the knowledge 
entry embedding E Ki and the original con-
textual query embedding E original  is calcu-
lated, denoted as Sim original (Ki). Then, the 
cosine similarity between the knowledge 
entry embedding E Ki and the QoS prefer -
ence query embedding E QoS is computed, 
denoted as SimQoS(Ki).
3. Computation of Combined Similarity 
Score:  To comprehensively consider both 
FIGURE 2. Schematic diagram of intelligent context awareness and QoS-aware intelligent tendency matching module.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
5
contextual matching and QoS preference, 
we perform a weighted combination of 
these two similarity measures to obtain the 
combined similarity for each knowledge 
entry, denoted as Simcombined(Ki).
This module ensures that the LLM generates 
task offloading strategies that are more precise 
and highly adaptive. It significantly enhances deci-
sion-making performance in the IoE.
d yn Am Ic  Ad Apt Ive  h ybr Id  k no Wled Ge b Ase  c onstruct Ion  
And  m An AG ement
To enable continuous learning from historical 
experience and enhance decision-making capa-
bilities, the proposed framework constructs a 
dynamic and adaptive composite vector knowl-
edge base. This knowledge base incorporates 
predefined expert base knowledge and dynam-
ically accumulates both positive and negative 
historical experiences generated during system 
operation. As shown in Fig. 3 , the implementation 
steps are as follows:
1. Knowledge Base Initialization and Base 
Knowledge Injection: At framework start -
up, an empty vector knowledge base is 
initialized. Preorganized expert base 
knowledge texts are transformed into 
high-dimensional vectors using an embed-
ding model. These vectors are added 
to the knowledge base as entries of the 
“Base knowledge” type. These entries pro-
vide general principles and common sense 
within the domain.
2. Real-time Case Data Capture and Process -
ing and Failure Degree Quantification:  
After each task offloading decision is exe -
cuted, the system captures the complete 
decision context, the execution action gen-
erated by the LLM, and the total reward 
feedback. The failure degree is based on the 
normalized reward, which is determined by 
first subtracting the global minimum possi-
ble reward from the total reward, and then 
dividing this difference by the total range 
of possible rewards. The failure degree is 
then obtained by subtracting the normalized 
reward from 1.0, ensuring that 0.0 signifies 
optimal performance and 1.0 signifies com-
plete failure relative to the system’s reward 
bounds. A decision is classified as a positive 
case if the failure degree is low (less than 
or equal to 0.3). A decision is classified as 
a negative case if the Failure Degree is high 
(greater than 0.3). Negative cases are fur -
ther categorized into moderate failure cases 
(failure degree between 0.3 and 0.7) and 
severe failure Cases (failure degree greater 
than 0.7).
3. Historical Case Textualization and Embed-
ding: The captured real-time case data is 
processed into a structured natural lan -
guage text block. This block details the 
scenario, decision, outcome, rationale and 
performance metrics of the current task off-
loading. Each case is labeled according to 
its failure degree, with failed cases further 
classified as severe, moderate, or minor. The 
text block is then converted into a embed-
ding vector using the embedding model.
4. Dynamic Knowledge Base Update and 
Deduplication : The generated historical 
case embedding vectors, corresponding 
texts, failure degrees, and total rewards are 
dynamically added to the knowledge base. 
The knowledge base performs deduplication 
FIGURE 3. Dynamic knowledge base with positive and negative experiences for intelligent prompt generation module.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
6
during this process to ensure each text entry 
is unique and to avoid redundancy. To main-
tain retrieval efficiency and prevent memory 
bottlenecks in large-scale deployments, an 
upper limit is set on the size of the knowl-
edge base, where the oldest cases are 
retired when this limit is reached.
Through the above procedures, the composite 
knowledge base continuously evolves with sys -
tem operation, accumulating complex real-world 
experience. Introducing the failure degree quan-
tifies the severity of negative cases, transforming 
the knowledge base from a simple information 
repository into a system embedding quantitative 
risk awareness. This significantly enhances the 
LLM’s proactive risk avoidance capability during 
decision-making.
h ybr Id  k no Wled Ge-b Ased  p rompt  Gener AtIon  m odule
To overcome the limitation of incomplete 
prompt knowledge caused by single semantic 
retrieval methods in traditional RAG frameworks, 
we propose a hybrid knowledge-based prompt 
generation module. This module ensures that 
the LLM accurately acquires and utilizes both 
positive and negative experiences. The core 
of this module is to achieve precise hierarchi-
cal retrieval based on the QoS-aware intelligent 
tendency matching module. It performs refined 
filtering and ranking on the retrieved results to 
finally construct a high-quality comprehensive 
prompt. The specific implementation steps are 
as follows:
1. Hierarchical Knowledge Retrieval Based on 
QoS-aware Similarity:
This module performs multi-channel retriev -
al on the knowledge base based on the 
QoS-aware intelligent tendency matching 
module. This mechanism divides the retriev -
al process into three independent and guar -
anteed channels:
• Base Knowledge Retrieval: The module 
filters entries labeled as base knowledge 
and retrieves several base knowledge 
items most relevant to the current con-
text and QoS preferences. To ensure 
sufficient coverage, as many results as 
possible are returned within availability 
even if the number of retrieved items is 
limited.
• Positive Historical Case Retrieval: His -
torical records marked as successful 
cases are filtered, and several success 
cases most relevant to the current con-
text and QoS preferences are retrieved. 
To avoid dominance by one case type 
leading to lack of the other, a baseline 
similarity threshold is set to guarantee a 
minimum number of positive cases (if 
available), ensuring balanced experience 
representation.
• Negative Historical Case Retrieval: His -
torical records marked as failed cases 
are filtered, and several failure cases 
most relevant to the current context and 
QoS preferences are retrieved. Similar -
ly, a baseline similarity threshold is set to 
ensure a minimum number of negative 
cases (if available), providing compre -
hensive lessons from failures.
2. Fine-Grained Ranking and Filtering:
The module further ranks and filters the 
knowledge retrieved from each channel to 
ensure that the highest quality prompt is ulti-
mately provided to the LLM.
• Base Knowledge: The top relevant items 
are directly selected as prompt for the 
LLM.
• Positive Historical Cases: The retrieved 
positive cases are ranked by a weighted 
score that combines QoS-aware com -
posite similarity, semantic similarity, and 
historical total reward. Specifically, each 
component is assigned an empirical 
weight, and the weighted score is cal -
culated as the sum of each component 
multiplied by its corresponding weight. 
The weights are set based on preliminary 
experiments to balance the influence of 
similarity and historical reward. Top cases 
according to this ranking are selected.
• Negative Historical Cases: The retrieved 
negative cases are ranked in descending 
order by failure degree. Cases with high-
er failure severity are ranked higher as 
they provide more critical lessons for the 
LLM to learn from.
3. Comprehensive Prompt Construction:
The filtered and optimized base knowledge, 
positive cases, and negative cases are inte -
grated into a comprehensive and structured 
prompt.
Through this hybrid knowledge-based prompt 
generation module, the proposed framework 
enables the LLM to receive highly relevant infor -
mation containing both positive and negative 
experiences during decision making.
p erform Ance  evAlu AtIon
exper Iment Al setup
The experiments are conducted on a server 
equipped with an NVIDIA RTX 3090 GPU. To 
simulate the dynamics and complexity in EC for 
the IoE, a custom simulation environment is estab-
lished with key parameters configured according 
to [14] . The scenario consists of a centralized 
edge server, a edge server, and five user devices. 
When a user device offloads a task and the edge 
server accepts it, the task is processed by one of 
the server’s computing units. The channel gain 
ranges from 5 dB to 14 dB, and the wireless 
bandwidth is set to 40 MHz. The edge server 
has a computing capacity of 4 GHz and a stor -
age capacity of 400 MB. The local computing 
capacity of user devices ranges from 0.4 GHz 
to 1.5 GHz. T ask data sizes range from 1 MB to 
50 MB, and task deadlines range from 0.1 s to 
1 s. The transmission power of user devices is set 
between 1 dBm and 24 dBm, and their energy 
reserves range from 0.5 MJ to 3.2 MJ. To ensure 
reproducibility, the random seed is set to 35. The 
simulation is executed over multiple episodes to 
evaluate long-term cumulative rewards and sys -
tem stability.
The implementation details of the framework 
are elaborated below. The BAAI/bge-base-en-v1.5 
model 1 serves as the embedding model across 
all modules of the framework [15]. To align with 
the real-world physical constraints identified in 
1 https://huggingface.co/
BAAI/bge-base-en-v1.5
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
7
[14], the algorithm parameters are heuristically 
configured to balance decision accuracy and sys -
tem overhead. The retriever initially fetches the 
top-K = 5 candidates for base knowledge, positive 
experiences, and negative counterexamples based 
on a weighted similarity score (0.8 for semantic 
relevance and 0.2 for QoS alignment to balance 
context and constraints). Subsequently, a re-rank -
ing process filters these candidates, selecting the 
top-2 most critical entries from each category for 
the final prompt construction to prevent prompt 
redundancy (K prompt = 2 for each type). Positive 
cases are re-ranked by historical reward, while 
negative cases are sorted by failure severity to pri-
oritize risk mitigation. For the LLM generation, we 
utilize a deterministic setting with temperature T 
= 0.2 to ensure decision stability. The capacity of 
the knowledge base is capped at 10,000 historical 
cases. We compare the proposed framework with 
the following four baseline approaches:
• Proposed Framework: In the experiments, 
we test with various LLM application pro-
gramming interfaces (APIs), including Gem-
ini series 2, Ernie series 3, and Qwen series 4. 
These models are chosen for their diversity 
in architecture and their position as wide -
ly recognized and highperforming LLMs, 
enabling the thorough evaluation of our 
framework’s generalizability across different 
scales.
• Conservative Strategy: This baseline pro-
cesses all tasks locally on user devices with-
out any offloading. The same environmental 
settings and simulation parameters as the 
proposed framework are used to ensure fair 
comparison.
• Aggressive Strategy: This baseline offloads 
all tasks to the idle edge server for process -
ing. It also shares the same simulation con-
figuration as the proposed framework to 
guarantee fair evaluation.
• DRL Baselines: We employ three DRL algo-
rithms for comparative analysis. The deep 
deterministic policy gradient (DDPG) serves 
as a classical DRL benchmark. The agent 
learns optimal policies through continuous 
environment interaction. Its hyperparame -
ters are: actor learning rate 0.0001, critic 
learning rate 0.001, discount factor 0.99, 
soft update coefficient 0.005, replay buffer 
capacity 10000, and batch size 64. The twin 
delayed deep deterministic policy gradient 
(TD3) is included as an advanced DRL base -
line. TD3 mitigates DDPG’s overestimation 
bias using twin Critic networks, delayed 
policy updates, and target policy smooth-
ing. The federated reinforcement learning 
(FRL) employs a standard FRL framework for 
distributed task offloading comparison. FRL 
clients utilize the DDPG algorithm locally, 
periodically aggregating parameters via fed-
erated averaging at the edge server, with the 
federation period set to 50 time steps.
To quantitatively evaluate the performance of 
each method, we focus on the following metrics. 
The total reward reflects the comprehensive ben-
efit of task offloading strategies and is a weighted 
function of QoS metrics such as latency and 
energy consumption. The average latency refers 
to the mean time taken from task generation 
to completion. The average energy consump -
tion indicates the mean energy used during task 
execution.
exper Iment Al r esults  And  An Alys Is
Fig. 4 presents the total reward performance of 
the proposed framework. The proposed frame -
work uses Gemini-2.5-Flash as the core LLM. 
The total reward reflects the effectiveness of 
task offloading in balancing latency and energy 
consumption. In Fig. 4(a), the framework using 
Gemini-2.5-Flash achieves faster convergence and 
higher rewards than other LLMs. Even with alter -
native LLMs, as shown in Fig. 4(c), the proposed 
framework outperforms traditional approaches, 
verifying its ability in contextual understanding 
and reasoning through retrieved knowledge. In 
Fig. 4(c), the proposed method surpasses conser -
vative, aggressive, and DDPG-based strategies. 
Fig. 4(b)  and (d)  reveal that removing RAG or 
QoS-aware guidance causes significant perfor -
mance decay, validating that retrieved knowledge 
rectifies LLM reasoning biases and aligns decisions 
with strict task constraints. The proposed frame -
work achieves an average reward improvement 
of 48.4% over 12 methods. Our reward stan -
dard deviation (0.40) is lower than DDPG (0.59), 
demonstrating that knowledge-based reasoning 
provides better decision stability than the stochas -
tic exploration typical of traditional DRL methods. 
These improvements are attributed to the synergy 
between the hybrid RAG mechanism and QoS-
aware guidance. By integrating complementary 
positive and negative historical experiences, the 
framework enables the LLM to proactively identify 
high-risk decisions. This synergy empowers the 
LLM to synthesize context-sensitive and risk-aware 
policies, facilitating faster convergence and robust 
adaptability. Consequently, the framework bridges 
the gap between raw environment data and opti -
mal offloading decisions, yielding superior rewards 
across dynamic IoE scenarios.
Fig. 5(a) illustrates the average latency, where 
our framework achieves the lowest delay across 
all evaluated methods. Unlike DRL baselines 
that rely on inefficient stochastic exploration, 
our framework leverages historical knowledge 
to bypass sub-optimal state-action trials. Abla -
tion confirms RAG and QoS-aware knowledge 
are vital. Our method achieves a 44.8% latency 
reduction over methods lacking these enhance -
ments. Thus, the framework effectively lowers 
latency, enhancing IoE system responsiveness. 
Fig. 5(b) compares energy consumption, where 
our framework yields a 50.9% reduction by intel-
ligently balancing computation and transmission 
costs. This efficiency is primarily attributed to the 
RAG architecture, which empowers the LLM to 
synthesize a comprehensive understanding of cur -
rent system states and historical experiences. By 
leveraging this retrieved knowledge, the LLM can 
identify energy-optimal strategies that traditional 
DRL baselines fail to capture, effectively minimiz -
ing resource waste in dynamic environments.
Fig. 6 demonstrates the robustness and 
scalability of our proposed framework by com-
paring its performance against DDPG, TD3 and 
FRL under increased system complexity. In Fig. 
6(a) , although all methods experience perfor -
mance degradation due to heightened resource 
2 https://gemini.google.
com/app 
 
3 https://console.bce.baidu.
com/qianfan/modelcenter/
model/buildIn/detail/
am-bg7n2rn2gsbb?tab=ver-
sion 
 
4 https://bailian.console.ali-
yun.com/?tab=model#/mod-
el-market?provider=aliyun
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
8
FIGURE 5. Performance comparison of task offloading metrics. a) Comparison of average latency performance under different methods. 
b) Comparison of average energy consumption performance under different methods.
FIGURE 4. Total reward performance analysis. a) Impact of different LLM models on the proposed framework’s reward. b) Comparison 
of rewards between the proposed framework and LLM baselines without RAG. c) Comparison of rewards between the proposed 
framework and traditional baseline methods. d) Comparison of rewards between the proposed framework and methods without 
QoS knowledge assistance.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
9
contention, our framework consistently achieves 
the lowest average latency and demonstrates the 
slowest rate of decline. This resilience stems from 
the semantic abstraction capability of RAG, which 
allows the LLM to effectively manage high-di -
mensional state information that often leads to 
policy collapse in DRL-based methods. Similarly, 
Fig. 6(b) confirms the superior energy efficiency 
of our method, which achieves the lowest aver -
age energy consumption with the shallowest 
growth curve compared to the baselines. This 
advantage is attributed to the RAG architecture’s 
ability to synthesize a comprehensive understand-
ing of system states and historical experiences, 
enabling energy-conscious orchestration even as 
the network scale expands. Collectively, these 
results underscore the inherent scalability of 
the RAG-LLM paradigm and its capacity to mit -
igate the curse of dimensionality in large-scale, 
resource-constrained IoE environments.
conclus Ion  And  future  Work
To address the challenges in the IoE, this paper 
develops a robust RAG-empowered adaptive 
task offloading framework. Our framework 
overcomes the rigidity of traditional heuristic 
and RL-based methods through four synergistic 
technical pillars. First, a novel RAG-empowered 
adaptive task offloading framework is introduced 
to transform dynamic task and environment data 
into structured semantic inputs, enabling intel-
ligent decision-making. Second, an intelligent 
preference matching mechanism dynamically 
weights task QoS features to guide knowledge 
retrieval. Third, a composite knowledge base 
incorporating both positive and negative cases 
is constructed, where failure severity is quan -
tified to enhance robustness. Fourth, a hybrid 
knowledge-based prompt generation module 
is proposed, employs hierarchical retrieval with 
channel-specific thresholds and ranking optimiza-
tion to ensure relevant and professional prompts. 
Experiments demonstrate that our framework 
achieves a 48.4% improvement in cumulative 
reward compared to baselines. Most notably, the 
framework significantly mitigates system bottle -
necks, yielding 44.8% and 50.9% reductions in 
task latency and energy consumption, respec -
tively, which confirms its superior resource 
efficiency in high-load scenarios. These results 
substantiate that integrating LLM with RAG pro-
vides a highly reliable and risk-sensitive solution 
for offloading orchestration. This work contrib-
utes a versatile RAG-empowered paradigm that 
bridges the semantic gap between numerical 
IoE data and intelligent decision-making. Despite 
these advancements, future research will address 
current limitations in two directions. First, we 
will explore model compression and lightweight 
LLMs to reduce computational overhead on 
resource-constrained edge devices. Second, we 
aim to investigate decentralized RAG and hybrid 
reasoning methods to enhance system scalability 
and robustness in extreme or unseen scenarios.
Ackno Wled Gment
This work was supported by Management and 
Consulting Projects of State Grid Corporation of 
China under Grant SGHL0000DKJS2310205.

## § References

[1] T. Gong et al., “Edge intelligence in intelligent transportation 
systems: A survey,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 
9, pp. 8919–8944, Sep. 2023.
[2] A. Naghib, F. S. Gharehchopogh, and A. Zamanifar, “A com-
prehensive and systematic literature review on intrusion 
detection systems in the Internet of Medical Things: Current 
status, challenges, and opportunities,” Artif. Intell. Rev., vol. 
58, no. 4, p. 114, Jan. 2025.
[3] M. Yan et al., “Two-timescale hierarchical contract for joint 
computation offloading and energy management in edge 
computing system,” IEEE Trans. Netw. Sci. Eng., vol. 12, no. 3, 
pp. 1745–1760, May 2025.
[4] X. Zhou et al., “Digital twin empowered task offloading for 
mobile-edge computing in 6G Internet of Vehicles,” IEEE 
Internet Things J., vol. 12, no. 15, pp. 29189–29202, Aug. 
2025.
[5] J. Liu et al., “VLC-enabled UAV network for IoT with co-chan-
nel interference: Joint spatial deployment and resource 
allocation,” IEEE Internet Things J. , vol. 12, no. 12, pp. 
20707–20721, Jun. 2025.
[6] X. Huang et al., “Toward effective retrieval augmented gener-
ative services in 6G networks,” IEEE Netw., vol. 38, no. 6, pp. 
459–467, Nov. 2024.
[7] N. Alabbasi et al., “TeleOracle: Fine-tuned retrieval-augmented 
generation with long-context support for networks,” IEEE Inter-
net Things J., vol. 12, no. 10, pp. 13170–13182, May 2025.
[8] H. M. A. Zeeshan et al., “LLM-based retrieval-augmented 
generation: A novel framework for resource optimization 
in 6G and beyond wireless networks,” IEEE Commun. Mag. , 
vol. 63, no. 10, pp. 60–67, Oct. 2025.
[9] T. Ouyang et al., “AdaRAG: Adaptive optimization for retriev-
al augmented generation with multilevel retrievers at the 
edge,” in Proc. IEEE INFOCOM Conf. Comput. Commun., 
London, U.K., May 2025, pp. 1–10.
[10] G. Liu et al., “Adaptive contextual caching for mobile edge 
large language model service,” 2025, arXiv:2501.09383.
FIGURE 6. Performance comparison across varying user device numbers. a) Comparison of average task offloading latency performance. 
b) Comparison of average energy consumption performance.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • xx/xx xxxx
10
[11] Y. He et al., “Large language models (LLMs) inference off-
loading and resource allocation in cloud-edge computing: 
An active inference approach,” IEEE Trans. Mobile Comput., 
vol. 23, no. 12, pp. 11253–11264, Dec. 2024.
[12] R. Zhang et al., “Interactive AI with retrieval-augmented 
generation for next generation networking,” IEEE Netw., vol. 
38, no. 6, pp. 414–424, Nov. 2024.
[13] S. Song et al., “Joint bandwidth allocation and task offload-
ing in multi-access edge computing,” Expert Syst. Appl., vol. 
217, May 2023, Art. no. 119563.
[14] T. Z. Gebrekidan, S. Stein, and T. J. Norman, “Combina-
torial client-master multiagent deep reinforcement learning 
for task offloading in mobile edge computing,” in Proc. Int. 
Joint Conf. Auto. Agents Multiagent Syst., May 2024, pp. 
2273–2275.
[15] S. Xiao et al., “C-pack: Packaged resources to advance gen-
eral Chinese embedding,” in Proc. Int. ACM SIGIR Conf. Res. 
Dev. Inf. Retr. (SIGIR), Washington, DC, USA, May 2024, pp. 
2273–2275.
BiogRaphies
Xiongjie  Zhou  (zxj2221896@gmail.com) is with Heilongjiang 
University, China. His current research interests include the Inter -
net of Things, edge computing, and large language model.
Xin g uan  (Member, IEEE) (guanxin.hlju@gmail.com) is currently 
a Professor with Heilongjiang University, China. His research 
interests include the Internet of Things, energy internet, and 
machine learning.
n ing  Wang  (wn007@126.com) currently works as the Deputy 
Director with the Dispatching and Control Center, State Grid 
Heilongjiang Electric Power Company Ltd., China. His research 
interests include electrical operation of power plant, power 
dispatching management, power grid operation technology, and 
renewable energy operation management.
h ongyang  Chen  (Senior Member, IEEE) (dr.h.chen@ieee.org) 
is currently a Senior Research Expert with Zhejiang Laborato-
ry, China. His research interests include the Internet of Things, 
data-driven intelligent networking and systems, machine learn-
ing, localization, location-based big data, B5G, and statistical 
signal processing.
Tomoaki  o h Tsuki  (Senior Member, IEEE) (ohtsuki@ics.keio.
ac.jp) is currently a Professor at Keio University, Japan. His 
research interests include wireless communications, optical com-
munications, signal processing, and information theory.
yan  Zhang  (Fellow, IEEE) (yanzhang@ieee.org) is currently a Full 
Professor with the University of Electronic Science and Tech-
nology of China, China. His current research interests include 
next-generation wireless networks leading to 5G beyond and 
green and secure cyber-physical systems (e.g., smart grid, health-
care, and transport).
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:14 UTC from IEEE Xplore.  Restrictions apply.
