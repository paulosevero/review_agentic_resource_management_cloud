---
paper_id: "paper-2600"
source_pdf_sha: "2144ad964b6f8ac6ddacc562b1956816f753a58b19e29f6ca4b2dd79cb938009"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 3
  page_count: 16
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2600 — fulltext
## §unknown-1

IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 1
GenAI-5GS Fusion Approach: A New Path for
Enhancing Computation Offloading Efficiency of
Complex Tasks in Internet of Vehicles
Chao He, Wenhui Jiang, Xing Wang, Wanting Wang, Hong Na, and Xin Xie
Abstract—With the advancement of real-time communication
and data interaction technologies in the Internet of Vehicles
(IoV), the pivotal role of Mobile Edge Computing (MEC) in
optimising vehicle service efficiency has become increasingly
prominent. However, existing task offloading strategies still
present significant room for improvement in handling complex
tasks, delay control, and resource allocation for Roadside Units
(RSUs). To reduce task offloading delay and enhance resource
utilization, this paper proposes an offloading method integrating
Generative Artificial Intelligence (GAI) with 5G Slicing (GenAI-
5GS). First, a Graph-GAN-based vehicle trajectory prediction
model is constructed. Operating with CPU/GPU utilization below
50% on resource-constrained RSUs, it enables precise prediction
of vehicle movements to support proactive RSU deployment.
Secondly, it innovatively integrates 5G slicing technology to
dynamically allocate Resource Blocks (RB) within the dedicated
5.9GHz IoV band. By combining multiple Modulation and Cod-
ing Schemes (MCS) to accommodate tasks of varying priorities,
which enables slicing-based management and flexible resource
allocation for RSUs. Finally, research findings demonstrate that
the proposed method enhances trajectory prediction accuracy
and resource utilization while reducing offloading delay, all
while safeguarding multi-dimensional Quality of Service (QoS)
requirements. Furthermore, this approach significantly improves
IoV complex task processing performance and system stability,
delivering safer and more efficient service experiences for in-
vehicle users, thereby possessing clear engineering deployment
value.
Index Terms —Internet of Vehicles, Mobile Edge Computing,
Complex Task Offloading, Generative Adversarial Network,
Graph Neural Network, 5G Slicing
I. I NTRODUCTION
This work was supported by the Science and Technology Research Pro-
gram of Chongqing Municipal Education Commission (Grant No. KJZD-
K202201203, KJQN202301258), the Doctoral ”Through Train” Scientific
Research Project of Wanzhou (Grant No. wzstc20230418), the Foundation of
Intelligent Ecotourism Subject Group of Chongqing Three Gorges University
(Grant No. zhlv-20221004), the Natural Science Foundation of Chongqing,
China(Grant No. CSTB2025NSCQ-GPX0246), and the Chongqing Graduate
Research and Innovation Program (Grant No. CYS25843).
C. He, W. Jiang, X. Wang, and W. Wang are with
the School of Electronic and Information Engineering,
Chongqing Three Gorges University, Chongqing, China
(e-mail:hechao@sanxiau.edu.cn; jwh2445561061@163.com;
17338367980@163.com; wangwt201228@163.com).
H. Na is with the School of Electrical Engineering, Yunnan Water Re-
sources and Hydropower V ocational College, Kunming, China(e-mail: na-
hong@ynwater.edu.cn).
X. Xie is with the School of Automation, Chongqing University of Posts
and Telecommunications, Chongqing, China(e-mail: xiexin@cqupt.edu.cn)
Manuscript received XXX, XX, 2025; revised XXX, XX, 2025.
W
ITH the deep integration of the Internet of Vehicles
(IoV) and 6G communication technology, the intel-
ligent transport system is rapidly evolving towards full-area
sensing and real-time collaboration [1]. According to industry
forecasts, the number of global intelligent vehicles will exceed
89 million units in 2026 [2], and emerging applications such
as Autonomous Driving (AD) and vehicle-circuit collaboration
have imposed stringent requirements on computing power,
communication delay and reliability. Mobile Edge Computing
(MEC) offers a promising solution to the challenges of limited
in-vehicle computing capacity and inefficient task processing
by enabling computation offloading to roadside infrastructure
such as Roadside Unit (RSU) [3]. By July 2025, more than
8,700 RSUs have been deployed in China, laying the infras-
tructure foundation for the scaled application of the IoV .
However, the offloading of IoV complex tasks still faces
two core challenges, one is the dynamic adaptation problem,
high-speed vehicle movement leads to frequent changes in
network topology and task demand [4], the traditional static
resource allocation strategy is difficult to match the spatial
and temporal distribution characteristics of the task, which
is prone to triggering resource scrambling or idling [5]. The
second is the delay control bottleneck. High priority tasks such
as self-driving control commands have extremely stringent
requirements for Ultra-reliable and Low-latency Communi-
cation (URLLC), while the existing offloading method lacks
prospective prediction of the vehicle trajectory, making it
difficult to achieve accurate pre-allocation of RSUs resources.
For example, in the morning peak dense traffic scene [6] [7],
the vehicle’s sudden environment sensing data upload and AD
decision instruction transmission concurrently, often due to
the lag in resource allocation leads to task blockage, which
directly threatens driving safety [8].
In the quest to address these challenges, Generative Arti-
ficial Intelligence (GAI) and 5G slice integrated techniques
have emerged [9]. GAI, especially deep learning-based Gener-
ative Adversarial Networks (GAN), has demonstrated powerful
data generation and pattern prediction capabilities in multiple
domains [10] [11]. In IoV environment, vehicle movement
behaviour models are constructed by integrating vehicle sensor
data, road network information and historical trajectories to
accurately predict vehicle trajectories and task demand trends,
providing a forward-looking basis for resource allocation.
Meanwhile, 5G slicing technology allows operators to create
multiple logically isolated virtual network slices on a uni-
fied physical network infrastructure, each of which can be
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 2
customised with network resources and Quality of Service
(QoS) for specific service requirements [12] [13], effectively
meeting the diverse needs of IoV services. Existing research
has explored the application of GAI in trajectory prediction,
such as the practice of Transformer-based vehicle behaviour
modelling and 5G slicing technology in resource isolation and
differentiated QoS guarantees, but there are still limitations
in the integration of the two, with insufficient real-time and
complex scene adaptability of the generative model and lack
of deep coupling of the dynamic adjustment of the 5G slices
with the vehicle movement trajectory [14], this leads to the
resource allocation efficiency of multi-priority tasks and delay
performance being difficult to be optimised in a synergistic
manner.
In order to achieve a synergistic mechanism for accurate
prediction and dynamic slicing, this paper proposes an en-
hancing computation offloading method that integrates GAI
technology with 5G slicing technology (GenAI-5GS), and the
main contributions of this work are summarised as follows.
• A Graph Neural Network (GNN) based on GAN (Graph-
GAN) vehicle trajectory prediction model is innovatively
proposed to achieve high precision prediction of vehicle
trajectories by capturing the social relationships between
vehicles and environmental associations, providing data
support for the prospective deployment of RSUs, and
breaking through the limitations of the traditional tra-
jectory prediction model that is insufficient in modelling
dynamic interactions.
• Combining the trajectory prediction results with 5G slic-
ing technology, a dynamic resource slicing model is
designed to flexibly deploy Resource Blocks (RB) based
on task priority and real-time demand, forming a closed-
loop management mechanism of ‘Prediction-Allocation-
Adjustment-Recovery’, which solves the problems of
poor adaptability of the traditional resource allocation
strategy in complex task environment, and the problem
of resource wastage or scrambling.
• Through the collaborative framework of accurate pre-
diction and dynamic slicing, the foresight of GAI and
the differentiated service capability of 5G slicing are
organically combined, which effectively improves the
resource utilization rate, delay performance and system
stability of complex task processing in IoV , and provides
an innovative paradigm for RSUs resource management
in dynamic environment.
The rest of this paper is structured as follows. Section II
reviews relevant research and identifies existing limitations.
Section III presents a system model consisting of commu-
nication and vehicle trajectory prediction models. Building
upon this, Section IV describes the algorithm, integrating
the model with 5G network slicing technology to optimise
dynamic resource allocation. Section V analyses and discusses
the experimental results, whilst Section VI summarises key
findings and outlines future research directions.
II. R ELATED RESEARCH
With the rapid development of IoV technology, MEC has
become the core support for improving vehicle service effi-
ciency [15]. However, delay control in complex task offloading
and RSUs resource allocation issues have always constrained
the further improvement of IoV system performance. To com-
prehensively analyse the current state of research in this field,
this paper provides an overview from three aspects: trajectory
prediction, resource allocation management, and integrated
technology research.
A. Trajectory Prediction in Task Offloading
In their research on vehicle trajectory prediction, researchers
have focused on vehicle interaction modelling and dynamic en-
vironment adaptation. Pazho et al. [16] proposed a VT-Former
model that combines graph isomorphism and the Transformer
architecture. Through the graph attentive tokenisation module,
which captures complex interactions between vehicles and is
used for vehicle trajectory prediction in highway monitoring
scenarios. Experiments show that it achieves or approaches
optimal performance on multiple benchmark datasets. Wang
et al. [17] proposed a hybrid trajectory prediction framework
combining attention mechanisms, which improves the trajec-
tory prediction accuracy and long-term consistency of au-
tonomous vehicles in complex traffic scenarios by integrating
spatiotemporal feature modelling, vehicle interaction dynamic
analysis, and multimodal data. He et al. [18] proposed a task
offloading strategy based on RSUs fusion, combining DRL,
CNN and other technologies to predict vehicle behaviour, and
using the Nash Equilibrium Game (NEG) algorithm to opti-
mise RSUs resource allocation. Wu et al. [19] proposed a mul-
timodal, interaction-aware vehicle trajectory prediction model
based on diffusion Graph Convolutional Network (GCN).
By leveraging dynamic graph structures to capture spatio-
temporal interactions among vehicles and incorporating mul-
timodal sensory data, the approach enables accurate trajectory
forecasting in complex traffic environments. Mistry et al. [20]
proposed a hybrid framework that combines Long Short-Term
Memory (LSTM) networks with GAN for trajectory predic-
tion in connected and autonomous vehicles. By integrating
spatio-temporal feature learning with adversarial training, the
model effectively captures vehicle interaction dynamics in
multimodal traffic scenarios, demonstrating strong accuracy
and generalization in complex environments. Lu et al. [21]
proposed a method based on a heterogeneous context-aware
GNN for trajectory prediction in the context of the IoV . By
integrating multi-source heterogeneous data to construct a
dynamic heterogeneous graph, the method models the spatio-
temporal interactions between vehicles and the contextual
dependencies of the environment, enabling high-precision tra-
jectory prediction in complex traffic scenarios.
The above research shows that traditional models are insuf-
ficient for modelling dynamic interactions between vehicles
and cannot capture the social relationships between vehicles
and their environmental connections. Some models also have
limitations in terms of long-term dependency and dynamic
interaction modelling, resulting in insufficient realism in the
generated trajectories.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 3
B. Resource Allocation and Slicing Management in MEC
To optimise delay and energy consumption, researchers
often use methods such as reinforcement learning and game
theory. Cui et al. [22] proposed a mutual dependency calcu-
lation method for MEC-assisted robot teams based on multi-
agent Deep Reinforcement Learning (DRL), enabling robots
to autonomously make task offloading and resource allocation
decisions according to environmental and task requirements.
Cao et al. [23] proposed a joint computing offloading solution
for optimising edge computing in IoV to address the issue of
task density in multi-vehicle RSUs systems. This solution aims
to minimise energy consumption while ensuring task comple-
tion delay and limited RSUs computing resources. Chen et al.
[24] proposed a federated learning framework based on risk-
aware reinforcement learning, applied to IoV scenarios, which
uses hierarchical reinforcement learning to defend against
selfish attacks, improving model accuracy while ensuring
data privacy, and enhancing the security and adaptability of
federated learning in the dynamic environment of Vehicle to
Everything (V2X) networks. Wu et al. [25] focused on het-
erogeneous vehicular edge computing scenarios, addressed the
requirements of URLLC, proposed a corresponding resource
allocation scheme, and strived to meet the URLLC queue delay
constraints while solving challenges such as the lack of global
state information, to optimize system performance. Nezami et
al. [26] employed a novel distributed optimization framework
for mobile-aware edge-to-cloud resource allocation, service
offloading, configuration, and load balancing, addressing the
demands of emerging traffic patterns and large-scale real-
time computing. Liu et al. [27] introduced an asynchronous
DRL based approach for collaborative task computation and
on-demand resource allocation in vehicular edge computing.
This method enhances task offloading efficiency and resource
utilization, thereby improving overall system performance in
complex traffic environments. Meanwhile, research on 5G
network slicing has primarily focused on dynamic resource
management and ensuring service quality. Chekired et al. [28]
proposed a scalable SDN core network solution based on 5G
slicing, which meets the ultra-low delay requirements of AD
services through customised network slicing, enabling flexible
scheduling and isolation of network resources to improve the
real-time performance and reliability of AD services. Cheng
et al. [29] focused on the issue of network slicing resource
allocation in Open Radio Access Networks (O-RAN) and
proposed a solution using reinforcement learning to improve
the throughput of target network slices.
The above studies lack deep coupling with vehicle trajectory
prediction in terms of resource allocation and network slicing.
Dynamic adjustments lag behind task changes brought about
by high vehicle mobility, and overall adaptability and opti-
mization effects are inferior to the methods proposed in this
study.
C. Cross-Domain Integration of GAI and Communication
Technology
In applied research on GAI, scholars have focused on tra-
jectory prediction and resource allocation optimization. Onim
et al. [30] leveraged GAN in GAI. Through the powerful
data augmentation capability of generative models, it broke
through the limitation that traditional visual algorithms per-
formed poorly under low-light conditions, and demonstrated
the application value of GAI in visual perception tasks. Wang
et al. [31] proposed a Unmanned Aerial Vehicles (UA V)
assisted resource allocation and task offloading strategy to
address the complexity of connected vehicle tasks and uneven
resource distribution, and improved system performance by
constructing a task dependency model. Fahime et al. [32]
explored the application of GAI in the optimization of next-
generation wireless networks, elaborated on GAI models and
wireless network communication paradigms such as 6G, and
studied their role in resource allocation and improving network
performance. Shatnawi et al. [33] utilised a GAN model to
generate new emergency vehicles, with the aim of introducing
a comprehensive expanded dataset to assist in the emergency
vehicle detection and classification process. Jiang et al. [34]
proposed the concept of intelligent slicing and constructed a
unified framework for integrating AI into 5G networks. By
on-demand instantiation and deployment of AI modules to
perform different intelligent tasks, and using neural network
channel prediction and anomaly detection to ensure industrial
network security as an example, he demonstrated the role of
this framework in solving the diversification of 5G networks.
Balevi et al. [35] proposed a method for accurately estimating
frequency-selective channels with a small amount of pilot
signals under low Signal-to-Noise Ratio (SNR) conditions
using GAN. This method uses a generative network to learn
and generate samples that conform to the distribution of real
channels, demonstrating significant performance advantages
under low SNR conditions. Zhuan et al. [36] proposed utilising
GAI to assist MEC offloading solutions in the industrial
Internet of Things (IoT) enabled by digital twins. Through
generative models, task characteristics and resource status
can be predicted to optimise computing offloading decisions,
thereby improving edge computing efficiency and industrial
IoT service quality.
The above papers have made some progress in the field of
GAI, but they lack the ‘Predict-Allocate-Adjust’ closed loop of
the IoV . Resource allocation often fails to keep pace with the
rapid task dynamics caused by high vehicle mobility, while
network slicing remains inadequately adaptive to complex
and evolving traffic scenarios. In terms of the coordinated
optimization of resource utilization and delay, they are inferior
to the fusion method proposed in this paper.
To overcome the limitations of existing solutions, this
paper proposes a GenAI-5GS fusion offloading method that
addresses these challenges by constructing a Graph-GAN
vehicle trajectory prediction model and a resource manage-
ment mechanism based on 5G slicing technology. An intuitive
comparison of the research content with existing solutions is
shown in Table I.
III. S YSTEM MODEL
A. Communications Infrastructure
The role of V2X in RSUs deployment and optimization is
crucial, which directly affects the performance and efficiency
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 4
TABLE I: Related research
Research content Mistry et al. [20] Cui et al. [22] Onim et al. [30] Zhuan et al. [36] Ours
Integration of GAN and GNN # # # # !
Prediction results combined with 5G slicing technology # # # # !
‘Precise Prediction-Dynamic Slicing’ collaborative framework # # # # !
Optimising resources using GAI technology ! # ! ! !
Research related to resource allocation or network slicing # ! # ! !
of IoV , Fig.1 shows the schematic diagram of IoV commu-
nication architecture. Among them, RSU is an important part
of Vehicle-to-Infrastructure (V2I) communication, and RSUs
deployment and optimization is the key to achieve efficient
V2I collaboration. As the core communication node in IoV ,
RSU is not only responsible for collecting road conditions
and traffic information, but also providing assisted driving
decisions and safety through real-time communication with
vehicles. Therefore, the reasonable layout of RSU is important
for enhancing the reliability of data transmission, and reducing
the communication delay.
Fig. 1: Schematic diagram of the proposed IoV communica-
tion.
The vehicle data in this study was collected from a section
of road during the morning rush hour between 8:00 and 8:20.
Due to the high vehicle density during this period, commu-
nication for autonomous vehicles and resource allocation at
the RSUs may be significantly impacted. Moreover, Vehicle-
to-Vehicle (V2V) and V2I communications become more
complex compared to normal traffic conditions. Therefore,
this road segment is selected as the study area to represent
a source of complex and demanding tasks. As shown in Fig.1,
when vehicles drive into a dense area, the network load is
increased, which is prone to triggering conditions such as
offloading delays or communication blockage. In view of this,
we deployed RSUs block [Z1, Z2, ..., Zn]. RSUs provides of-
floading service precisely for vehicles in a specific area. In this
way, the disordered vehicle tasks in complex road environment
are disassembled into multiple sub-tasks for offloading in an
orderly manner. This not only greatly improves the offloading
efficiency, but also effectively alleviates a series of traffic-
related problems such as traffic congestion and poor data
transmission.
During the offloading process, the coverage and signal
strength of the RSUs play a decisive role in the quality of the
offloading service. In this study, the Friis transmission formula
is used to describe the signal strength of the RSUs received
by the vehicle, which is also known as the received power of
the vehicle, and the formula is expressed as follows:
Pr = PtGtGr
 λ
4πd
2
(1)
where Pr is the received signal power—higher values indicate
stronger signal quality, which enhances data transmission
reliability and facilitates efficient task offloading.Pt represents
the transmission power of the RSUs. Gt and Gr are the gains
of the transmitting and receiving antennas, respectively. Higher
antenna gains lead to more directional signal propagation
and improved transmission efficiency. The parameter λ is the
signal wavelength, and d shows the distance between the
RSUs and the vehicle. In practical IoV environments, the
effective coverage of an RSU can be extended by optimizing
the relationships among these parameters.
Similarly, the data transfer rate is a key metric of com-
munication performance, directly influencing task offloading
efficiency and the responsiveness of various vehicular appli-
cations. According to the Shannon-Hartley theorem, the actual
data transfer rate Rd between the vehicle and the RSUs can
be calculated using the following formula:
Rd = Blog2

1 + Pr
N0B

(2)
where B denotes the communication bandwidth and N0
represents the noise power spectral density. When a vehicle
is within the RSU’s coverage range and the received signal
power is strong, the system can allocate additional RB to
increase the effective bandwidth, thereby significantly boosting
the data transmission rate to meet the stringent real-time
demands of high priority tasks, such as AD control commands.
Conversely, when the vehicle moves farther from the RSUs
and the received power diminishes, the system dynamically
adjusts RB allocation based on current conditions, achieving
an optimal trade-off between bandwidth and SNR to ensure
reliable, albeit lower-rate, data transmission.
In addition, the figure clearly shows the layered architecture
in the IoV environment. In the vehicle layer, V2I and V2V
communication technologies are used to achieve information
interaction with each other and with RSUs. The edge layer,
with the RSUs and the edge server as the core, processes
vehicle data in situ at the edge of the network, and through the
task offloading mechanism, each layer has a clear division of
labour and operates in concert to jointly build an efficient and
intelligent IoV communication system, which builds a solid
foundation for applications such as AD and intelligent traffic
management.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 5
B. Graph-GAN Vehicle Trajectory Prediction Model
In addition to enhancing the communication between RSUs
and vehicles, reasonable RSU deployment is also crucial to
better reduce the delay of vehicle task offloading, so we design
a Graph-GAN vehicle trajectory prediction model graph for
prospective RSUs deployment, as shown in Fig.2.
Fig. 2: Graph-GAN vehicle trajectory prediction model.
As can be seen in Fig.2, the model utilises generative and
adversarial networks along with GNN to process the vehicle
trajectory data. The main steps are as follows:
1) Input historical data: In the model input section, we
organise the vehicle’s historical trajectory, current posi-
tion information and surrounding environment data into
the form of a GNN-processable adjacency matrix, which
is used as input data to provide support for subsequent
trajectory prediction. In this matrix, the vehicle’s histor-
ical trajectory data set is H = {h1, h2, ..., hn}, where
hn denotes the n-th historical trajectory sequence, the
current position information is denoted as P = (px, py),
and the surrounding environment information is denoted
as e = ( e1, e2, ..., em). We integrate these data into
an adjacency matrix A, where the element Aij shows
the degree of association between node i and node j.
The main consideration is the combination of trajectory
similarity, positional distance and environmental factors,
and the formula is expressed as follows:
Aij = α · S (hi, hj) + β · 1
d (Pi, Pj) + υ + γ · C (ei, ej)
(3)
where S (hi, hj) is a similarity measure between trajec-
tories hi and hj, d (Pi, Pj) is the Euclidean distance
between positions Pi and Pj, v is a very small integer
to avoid a zero denominator, C (ei, ej) is a correlation
measure between environmental data ei and ej, α, β,
γ are weight coefficients, and α + β + γ = 1 . After
constructing the adjacency matrix, normalization is ap-
plied to enhance the model’s training performance. This
process ensures a consistent scale across different di-
mensions, preventing features with extreme values from
disproportionately influencing the learning process. In
this study, Laplacian normalization is employed, which
is defined by the following formula:
Ano = D− 1
2 AD− 1
2 (4)
where D is the degree matrix, whose elements are
Dii = Pn
j=1 Aij. The degree matrix D records the
number of connections for each node. Through this
normalisation operation, the impact of different node
connection strengths on model training can be effectively
balanced.
2) GAN-based trajectory prediction: In this model, the
Generator’s role is to generate fake vehicle trajectory
samples based on the input data. By learning the dis-
tribution patterns of real data, it generates samples
similar to real trajectories. The Generator continuously
optimises its parameters to make the generated fake
samples as convincing as possible to the Discriminator.
Let the Generator be denoted by G, which takes as input
a random noise vector z and an adjacency matrix A,
and outputs a generated trajectory sample ˆt = G (z, A).
Discriminator is D, the Discriminator network is re-
sponsible for distinguishing between real samples and
fake samples generated by the Generator. It evaluates the
input samples and outputs a probability value indicating
whether the sample is real. Let the Discriminator be
recorded as D. For the real trajectory sample t and
the generated trajectory sample ˆt, the Discriminator’s
outputs are D (t, A) and D
 ˆt, A

, respectively. Dur-
ing training, the Generator and Discriminator compete
against each other, and their adversarial loss function is
expressed as follows:
LGAN = z∼pz(z) [log (1 − D (G (z, A) , A))] + (5)
t∼pdata(t) [log D (t, A)]
where pdata (t) represents the distribution of real tra-
jectory samples, and pz (z) is the distribution of ran-
dom noise vectors. The objective of the Generator
is to minimise the second term in LGAN, that is
minGz∼pz(z) [log (1 − D (G (z, A) , A))], while the ob-
jective of the Discriminator is to maximise the entire
LGAN, that is maxDLGAN.
3) Graph-GAN model implementation: GNN plays a key
role in the model, as it can mine spatial and temporal
relationships in vehicle trajectory data. By learning the
adjacency matrix, GNN can capture the mutual influence
between vehicles and the relationship between vehicles
and their surrounding environment. By analysing the
trajectory changes of different vehicles in similar time
and space, it can predict the possible driving direction
and position of a vehicle at the next moment. In this
model, the node feature update formula for the l-th layer
is expressed as follows:
h(l+1)
i = σ
 X
j∈N (i)
1p
didj
W (l)h(l)
j + b(l)
!
(6)
where h(l)
i denotes the feature vector of node i at the
l-th layer, N (i) represents the set of its neighboring
nodes, and di and dj are the degrees of nodes i and
j, respectively, W (l) is the learnable weight matrix,
and b(l) is the bias vector at the l-th layer, with σ
denoting the activation function. Through multiple layers
of CNN convolutional operations, the final node feature
representations are obtained in the last layer. These
feature vectors contain rich vehicle trajectory, location,
and environmental information. To convert these feature
vectors into specific information that can be used for
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 6
trajectory prediction, a fully connected layer will be
used for processing. The predicted trajectory feature
vectors are obtained by multiplying the node feature
vectors from the final layer with the weight matrix of
the fully connected layer and then adding a bias vector,
as expressed by the following formula:
tpre = Wf cHla + bf c (7)
where Hla =
h
h(L)
1 , h(L)
2 , ..., h(L)
n
i
is the matrix com-
posed of the feature vectors of all nodes in the last
layer (layer L), Wf c shows the weight matrix of the
fully connected layer, bf c is the bias vector of the fully
connected layer, and tpre means the predicted trajectory
feature vector.
However, the predicted trajectory feature vectors obtained
are typically represented in a high-dimensional abstract space.
To obtain meaningful vehicle trajectory coordinates, further
transformation is required. We use a mapping function f to
perform this transformation, which can be learned by training
an additional regression model. Let the transformed trajectory
coordinates be Ppre = [xpre, ypre], then we have:
Ppre = f (tpre) (8)
In practice, to optimize the mapping function, we em-
ploy the Mean Squared Error (MSE) loss to quantify the
discrepancy between the predicted trajectory coordinates and
the ground-truth coordinates Ptr = [ xtr, ytr]. The objective
function is formulated as:
Lmse = 1
N
XN
i=1



P (i)
pre − P (i)
tr



2
(9)
where N is the number of training samples.
To enhance the model’s generalization capability and mit-
igate overfitting, a regularization term is incorporated during
training. Specifically, an L2 regularization term is added to the
loss functions of both the generator and the Discriminator. The
updated loss functions for the generator LG and discriminator
LD are as follows:
L
′
G = LG + λG
X
k
∥WG,k∥
2
(10)
L
′
D = LD + λD
X
k
∥WD,k∥
2
(11)
where WG,k and WD,k express the k-th learnable parameter
matrices in the Generator and Discriminator, respectively, and
λG and λD are regularisation coefficients, which are adjusted
by delay to balance the effects of the loss function and
regularisation.
During training, Stochastic Gradient Descent (SGD) and its
Adam algorithm are used to update the model parameters. In
each iteration, the Discriminator parameters are first fixed,
and the Generator parameters are updated to minimise the
Generator’s loss function. The Generator parameters are then
held constant, while the Discriminator parameters are updated
to maximize its loss function. After multiple iterations of train-
ing, the Generator is able to generate more realistic vehicle
trajectories, and the Discriminator can accurately distinguish
between real trajectories and generated trajectories, ultimately
improving the accuracy and reliability of the entire Graph-
GAN model for vehicle trajectory prediction.
C. RSUs Resource Slicing Model
In IoV environment, RSUs must simultaneously handle mul-
tiple types of tasks, including AD, environmental perception,
and task scheduling. Different tasks have significantly different
requirements for delay, bandwidth, and reliability. Traditional
resource allocation methods employ a ‘one-size-fits-all’ strat-
egy, which struggles to meet the dynamic resource demands of
complex tasks. To address this, this study combines 5G slicing
technology with Graph-GAN trajectory prediction results, as
shown in Fig.3. Based on vehicle trajectory prediction results,
traffic hotspots are identified, and independent resource slices
are dynamically allocated to different task types. Through a
dynamic resource slicing model, RSUs resources are managed
with precision.
Fig. 3: 5G slicing technology for RSUs resource traffic man-
agement.
Assume that the total resource pool of the RSU is repre-
sented by R = {R1, R2, ..., RI } available frequency domain
RB, where I is the total number of RB, to meet the differ-
entiated needs of different priority task classes. The system
divides the total resource pool into three priority slices: high,
medium, and low. Each slice class adopts a differentiated
resource allocation strategy with the following constraints:
2X
k=0
Rk (t) ≤ Rto, Rk (t) ≥ Rmin (12)
where Rk (t) denotes the number of RB allocated to priority
k at time t. Rto represents the total RB resources, adjusted
according to the actual deployed frequency band. The fre-
quency band used in this experiment is the dedicated 5.9GHz
band for IoV communications, with a channel bandwidth of
20MHz. Calculated based on each RB having a bandwidth of
180kHz, the total number of RB is 110. However, an addi-
tional 5% of QoS-guaranteed redundant RB must be reserved
within the total resource pool, exclusively for retransmission
and emergency requirements of high priority tasks to ensure
reliability compliance. Rmin = 10 signifies the minimum RB
quota guaranteed for each slice.
The dynamic allocation algorithm uses a three-layer
decision-making mechanism, with static weight allocation set
at the initial stage: high:medium:low=60:25:15. The quota is
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 7
adjusted during operation through a prediction model. The
prediction model generates estimates of future time slot task
requirements based on vehicle movement characteristics and
historical task data, as shown below:
ˆTk (t) = α · Tk (t − 1) + (1 − ε) ·
X
v∈V
Pv,k (t) (13)
where Tk (t − 1) indicates the actual task volume in the
previous time slot, Pv,k (t) shows the predicted probability
of vehicle v generating k types of tasks, and the smoothing
coefficient ε = 0 .7. Resource adjustment uses a progressive
update strategy:
Rk (t) = Rk (t − 1) + θ · ωk ·
 ˆTk (t)P ˆTk (t)
Rto − Rk (t − 1)
!
(14)
where ωk represents the QoS weighting factor, with high
priority tasks assigned ω0 = 1 .5, medium priority tasks
ω1 = 1.0, and low priority tasks ω2 = 0.8, ensuring high-QoS
demand tasks receive resources preferentially. This strategy
maintains system stability by adjusting the step size θ = 0.3.
To further safeguard transmission reliability for high priority
tasks, this study introduces a channel quality-resource binding
mechanism. RB are dynamically allocated based on the SNR
received by vehicles. High priority tasks are prioritised for RB
with superior channel quality, thereby reducing transmission
error rates. The final allocation outcome undergoes normali-
sation processing to satisfy overall resource constraints.
Assume that the resource requirement for task type m-th
denotes rm and the delay constraint is τm. Define the binary
allocation matrix as follows:
X = [xm,n] M × N (15)
where xm,n = 1 indicates that the n-th RB is allocated to the
m-th task type, otherwise it is 0.
Although this model preliminarily correlates Graph-GAN
trajectory prediction results through a ‘Predict-Allocate’ logic,
two key limitations remain: firstly, it passively receives
prediction outcomes without accounting for how prediction
accuracy fluctuations impact resource allocation, potentially
causing high priority tasks to suffer resource shortages due
to prediction bias. Secondly, it lacks feedback regulation of
the prediction model based on resource utilization status. In
low dynamic scenarios, this may generate redundant Graph-
GAN computations, increasing computational overhead at
edge nodes. These limitations provide optimization directions
for subsequent fusion mechanism design.
The RSUs resource slicing model constructed in this study
achieves fine-grained resource management through a three-
layer decision-making mechanism, in the initial stage, it
ensures the basic resource requirements of core tasks based
on a fixed proportion. During runtime, it dynamically adjusts
quotas in conjunction with Graph-GAN trajectory prediction
results, and it balances the flexibility and stability of resource
allocation through smoothing coefficients and incremental
update strategies. The binary allocation matrix and minimum
resource quota constraints further ensure resource isolation
and task reliability, laying the groundwork for subsequent
delay optimization and hotspot area adaptation. They also
reserve technical interfaces for the design of subsequent fusion
mechanisms.
D. Bidirectional Feedback Fusion Mechanism between
Graph-GAN and 5G Slicing
To address the limitations of the RSUs resource slicing
model, this section proposes a bidirectional feedback fu-
sion mechanism integrating Graph-GAN with 5G slicing.
By dynamically correlating prediction accuracy with resource
elasticity, implementing inverse feedback between resource
efficiency and prediction frequency, and employing spatio-
temporal coordinated preactivation strategies, it achieves deep
coupling between the two technologies. This overcomes the
bottlenecks of the traditional ‘Predict-Allocate’ unidirectional
workflow. This addresses resource wastage, high priority task
blocking, and computational redundancy stemming from pre-
diction accuracy fluctuations.
Based on the trajectory prediction error output by Graph-
GAN, prediction accuracy is categorised into high, medium,
and low tiers. Correspondingly, the proportion of emergency
resource pools for 5G slices and high priority slice quotas
are adjusted to ensure resource supply aligns with prediction
reliability. The emergency resource pool is reserved from the
total RB to address resource shortfalls caused by prediction
deviations: when MSE<0.6 m, the emergency resource pool is
reduced to 5%, releasing resources to medium and low priority
slices. When 0.6 m ≤MSE≤1.2 m, the emergency resource
pool is maintained at 10%; when MSE >1.2 m, the emergency
resource pool is expanded to 15%. Concurrently, high priority
slice quotas adjust synchronously with the emergency resource
pool, quantified by the formula:
Rhigh =



60% (Rto − Rem) ,MSE < 0.6m;
65% (Rto − Rem) ,0.6m ≤ MSE ≤ 1.2m;
70% (Rto − Rem) ,MSE > 1.2m,
(16)
where Rem represents the proportion of emergency resources,
ensuring high priority tasks still receive adequate resources
when prediction errors are significant.
To avoid redundant computations in Graph-GAN, a resource
utilization efficiency metric is introduced to optimise the
prediction update frequency of Graph-GAN. This efficiency
is defined as ηuse, expressed by the following formula:
ηuse = Rac
Ral
(17)
where Rac denotes the actual number of RB occupied by the
task, and Ral represents the number of RB allocated to the
slice. When ηuse > 90%, the Graph-GAN update frequency
decreases from 10 Hz to 5 Hz, reducing edge computing
power consumption. When ηuse < 70%, the update frequency
increases to 15 Hz while simultaneously triggering emergency
resource pool expansion. When 70% ≤ ηuse ≤ 90%, the
baseline frequency of 10 Hz is maintained. This feedback
mechanism dynamically aligns Graph-GAN’s computational
overhead with resource demands. During off-peak periods with
sparse traffic, it reduces computational delay by 30%, thereby
preventing computational resource wastage.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 8
To address the switching lag issue of slice models during
high speed vehicle movement, a strategy was devised by
integrating Graph-GAN trajectory prediction capabilities. On
the temporal dimension, based on the Graph-GAN predicted
sequence of the vehicle’s future positions over the next 5
seconds, the estimated time Ten for the vehicle to enter the
next RSU coverage area is derived using the vehicle’s current
speed and the distance to the RSUs. The formula is expressed
as follows:
Ten = dR − dcu
vcu/3.6 (18)
where dR represents the deployment spacing between RSUs,
dcu represents the vehicle’s current distance to the next RSU,
and vcu indicates the vehicle’s current speed. When Ten ≤200
ms, the high priority slice configuration of the current RSU is
synchronised in advance to the target RSUs, reducing handover
delay to 18 ±3 ms. In the spatial dimension, when Graph-
GAN predicts vehicle density in a region will exceed 120
vehicles/km, it dispatches low priority redundant RB from two
neighbouring RSUs to supplement the high priority slices of
the hotspot RSU, thereby preventing task blocking.
The bidirectional feedback fusion mechanism between
Graph-GAN and 5G slicing overcomes the limitations of
the RSUs resource slicing model through three core design
elements. This reduces slicing handover delay from 50 ms to
below 18 ms, thereby overcoming resource scheduling delays
during high speed vehicle movement. This establishes the
foundational architecture for subsequent experimental valida-
tion, enabling enhanced resource utilization and reduced delay.
IV. P ROBLEM DESCRIPTION
After clarifying the infrastructure and allocation mechanism
of the RSUs resource slicing model, to further achieve dy-
namic resource scheduling and precise optimization of task
delay, practical algorithmic processes must be designed based
on specific scenarios. This section will focus on the practical
application of 5G slicing technology in delay control and
resource efficiency improvement to meet the differentiated
needs of complex tasks in the IoV .
In the context of the IoV communication, there are various
types of tasks, and different tasks have significantly different
requirements for resources and delay. To achieve refined
resource allocation, this study categorises tasks into the fol-
lowing three priority levels and clarifies their characteristics:
1) High priority tasks: These include AD control com-
mands and emergency avoidance signals, which require
URLLC, which must meet URLLC requirements. Data
volume is L <10 KB, with a delay constraint of T < 50
ms, delay jitter of Tji <5 ms, and a task completion
rate of 100%. Transmission reliability must be greater
than or equal to 99.999%. Employing QPSK modulation
with a hybrid automatic repeat request mechanism, the
maximum retransmission count is less than or equal to
3.
2) Medium priority tasks: These include environmental
perception data and vehicle-to-infrastructure informa-
tion exchange, the system must meet the following
requirements, low delay of T < 100 ms, data volume
of 10 KB <L<1 MB, task completion rate greater than
or equal to 95%, and bandwidth fluctuation tolerance
of ±10%. Dynamic bandwidth adjustment is supported
to prevent data transmission interruptions caused by
channel fluctuations.
3) Low priority tasks: These include in-vehicle entertain-
ment streaming and software OTA updates, with a delay
tolerance of T > 500 ms, data volume of L > 1 MB,
and a task completion rate requirement of greater than
or equal to 90%. Non-real-time transmission is permis-
sible, with temporary caching of files during network
congestion.
To ensure communication quality, RB for similar tasks must
be allocated consecutively, namely, for the m-th type of task,
there are start block sm and end block em, such that xm,n = 1,
with the following constraints:
(
sm ≤ n ≤ em
em − sm + 1 ≥ rm
(19)
When there are insufficient available contiguous RB, the
dynamic borrowing mechanism is triggered, allowing high
priority tasks to temporarily occupy non-guaranteed RB of
low priority tasks and automatically return them when the
resources become available, thereby preventing low priority
tasks from experiencing prolonged starvation.
It is assumed that the processing delay of the m-th task Tm
not only needs to consider transmission delay and processing
delay, but also for handover delays when vehicles transition
between RSUs coverage areas, queuing delays, and retrans-
mission delays. The delay model is expressed as follows:
Tm = Lm
Bm · ηSNR
+ ρ
µ · (1 − ρ) + maxRe · Tso
1 − Per
+ td + τs (20)
where maxRe = 3 is the maximum retransmission count,
Tso=1ms represents the TDMA slot duration, and Per sig-
nifies the bit error rate, ensuring 1 − Per ≥99.999%. If
retransmissions attempts exceed the threshold without success,
emergency resource allocation is triggered, utilising reserved
redundant RB. Lm means the task data volume, Bm represents
the bandwidth allocated to this task, and ηSNR signifies the
channel quality factor. This factor describes the impact of SNR
on transmission rates and is a non-constant value, with its
values expressed as follows:
ηSNR =



0.95,SNR > 20 dB;
0.7,10 dB ≤ SNR ≤ 20 dB;
0.4,SNR < 10 dB,
(21)
where SNR= Pr
N0·B+IMUI
, IMUI=5 dBm shows neighbouring ve-
hicle interference power, and N0 = −174 dBm/Hz represents
the thermal noise power spectral density. td=5 ms is the fixed
RSU processing delay, τs=2 ms denotes the handover delay,
and when the vehicle does not switch RSUs, τs = 0. Bm is
positively correlated with the number of RB rm, expressed as
follows:
Bm = k · rm (22)
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 9
where k indicates the bandwidth per RB, set at 180 kHz. At
this point, the delay model must satisfy Tm ≤ τm, where
τm represents the maximum tolerable delay for the m-th task
category.
Different Modulation and Coding Schemes (MCS) are em-
ployed for tasks of varying priority levels. High priority tasks
utilise QPSK modulation with a data transmission rate of:
Rm = Bm · log2Mh · Rc (23)
where Rc = 0 .8 expresses the coding rate. Medium priority
tasks employ 16QAM modulation with Mm = 16 and a coding
rate Rc = 0.7. Low priority tasks utilise 64QAM modulation
with Ml = 64 and a coding rate Rc = 0.6.
Additionally, the high priority task category employs QPSK
modulation, with the bit error rate expressed by the following
formula:
Per = erf c
 r
SNR · log2Mh
Mh − 1
!
(24)
where Mh = 4 denotes the number of QPSK symbols, and
erfc represents the complementary error function. Must ensure
Per < 10−5, should the threshold not be met, retransmission
shall be triggered, with the retransmission delay factored into
the total delay.
After the algorithm delay study is completed, this study
will continue to investigate the RSUs resource situation.
Using the Graph-GAN model to predict the location distri-
bution of vehicles in the future time period t as P (t) =
{p1 (t) , p2 (t) , ..., pK (t)} (K is the number of vehicles), the
task density of each region can be calculated as follows:
ρ (t) = Nt
a (25)
where Nt is the number of regional tasks, and a shows the
regional area. Based on density, the RSUs coverage area is
divided into Q hotspot regions Ωq (q = 1, 2, ..., Q), with each
region corresponding to a set of task type distributions {λq,m},
where λq,m represents the proportion of the m-th task type in
the region Ωq.
On this basis, the goal of dynamically adjusting resource
slices is to maximise global resource utilization η, that is:
max η =
XQ
q=1
XM
m=1
 
rac
q,m − ral
q,m

(26)
where ral
q,m is the number of RB allocated to the m-th type of
task in region Ωq, and rac
q,m represents the actual number of
RB required. The Lagrange Multiplier method is introduced
to solve this optimization problem, transforming the global re-
source utilization maximisation problem into a local optimiza-
tion problem of resource allocation in each region, ensuring
that resource idleness or insufficiency is minimised as much
as possible while satisfying regional resource constraints. The
Lagrange function is constructed as follows:
L =
X
q,m
 
ral
q,m − rac
q,m

+
X
q
µq
X
m
ral
q,m − Rt
q

(27)
where Rt
q denotes the total number of RB allocated to region
Ωq, and µq is the Lagrange multiplier. By taking the partial
derivative of ral
q,m and setting it to zero, the optimal allocation
strategy can be obtained as follows:
ral
q,m = min
 
rac
q,m + µq, Rt
q

(28)
where through iterative updating of µq, resources can be
dynamically balanced across regions to avoid overloading
resources in hotspot areas.
Considering that vehicle movement may cause the RSUs
slice in a certain area to be unable to process the corresponding
tasks in a timely manner, a task change rate threshold δ (δ
=30%) is set for each area. When vehicle movement causes
the task density in the area to exceed the threshold, the slice
switching mechanism is triggered.
Based on the future ∆T -period trajectory distribution gen-
erated by the Graph-GAN model, the task density variation
rate for each region is computed as follows:
ρd = |ρp − ρc|
ρc (29)
where ρp represents the predicted task density for the region,
and ρc shows the current task density for the region. When
ρd ≥ δ/2 , the pre-allocation process is initiated to reserve
20% of emergency RB for the target region in advance, as
shown below:
Rp =

0.2 ·
XM
m=1
rp
q,m

(30)
When ρd ≥ δ, trigger formal slice switching. We set a
resource difference to indicate the degree of current RSUs
slice resource shortage or excess. When ∆Rq > 0, request
new resources. When ∆Rq < 0, release redundant resources,
as shown below:
∆Rq = Rn
q − Ro
q (31)
where Ro
q represents the currently allocated resources, and
Rn
q denotes calculated based on the predicted task density
ρp
q, reflecting the resource requirements for future periods, as
shown below:
Rn
q =

ρp
q · ru

(32)
where ru is the number of RB corresponding to the unit
density.
To clearly illustrate the implementation logic of the afore-
mentioned 5G slice dynamic resource allocation mechanism,
particularly the differences between the ‘Predict-Allocate-
Adjust’ closed-loop process in the GenAI-5GS method and tra-
ditional methods, the following provides its core pseudocode
to visually demonstrate the dynamic adjustment process of the
GenAI-5GS method.
Through the above mechanism, the delay of slice switch-
ing can be controlled within 50 ms, and resource recovery
efficiency can be improved to over 95%, effectively solving
the problem of resource fragmentation in dynamic scenarios in
IoV . Combined with the predictive capabilities of Graph-GAN,
a closed-loop management system of ‘Prediction-Allocation-
Adjustment-Recovery’ is formed, providing a solid foundation
for the efficient offloading of complex tasks.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 10
Algorithm 1 Implementation process of the GenAI-5GS

## § Method

Require: Vehicle trajectory dataset H, simulation duration T ,
total RSUs RB I
Ensure: Resource utilization η, average task delay Tm
initializeHistory()
1: Initialize RSUs with I RB, coverage radius 300m
2: Load vehicles V from H; initialize predictor P
3: Set initial slices: High=60, Medium=25, Low=15, adjust-
ment factor=0.3
4: for t = 1 to T do
5: Update vehicle positions/speeds from H
6: Generate tasks for vehicles in RSUs range (probability
∝ speed)
7: if method = ”GenAI-5GS” then
8: predicted tasks = P .predict(V, t)
9: ideal alloc = propor-
tional allocation(predicted tasks, I)
10: slices[τ] += 0.3 × (ideal alloc[τ] − slices[τ])
11: EnsureP slices = I
12: else if method = ”Dynamic” then
13: alloc = proportional allocation(RSUs.queue, I)
14: else
15: alloc: High=50, Medium=30, Low=20
16: end if
17: Process tasks:
18: Compute delay as:
19: (task.size ×8 × 103) / (alloc[task.type] ×180 ×
103) +5ms
20: Record delay if task completes
21: Record utilization =
P alloc
I
22: end for
23: Return η = avg(utilization history), Tm =
avg(recorded delays)
V. R ESULTS AND DISCUSSION
A. Experimental Setup
In this experiment, we selected a section of complex road
conditions for study, which includes a multi-lane lane change
scenario in a highway intersection area. Vehicle density during
the morning peak period (8:00–8:20) can reach two high-
density gradients of 80 vehicles/km and 120 vehicles/km.,
with 70% being small passenger cars, 20% being trucks, and
10% being emergency vehicles. The average vehicle speed
ranges is 40-80 km/h, the acceleration values is -3-2 m/s 2,
exhibiting typical characteristics of dynamic dense traffic.
RSUs are deployed every 500 m and 300 m along the road,
with a coverage radius of 300 m, a transmission power of
23 dBm, an antenna gain of 2 dBi, and operating on the
5.9GHz frequency band (dedicated to IoV communication).
This deployment complies with the design specifications for
road-vehicle coordination facilities, they support V2I/V2V
communication.
The experiment utilised the V2I communication channel
defined in 3GPP TR 36.885, pecifically incorporating Rayleigh
Fading, multipath number is set to 6, and Log-Normal Shad-
owing Fading, spatial correlation distance set to 50 m, whilst
incorporating multi-user interference correction for SNR cal-
culation. The Media Access Control (MAC) layer employs a
TDMA scheduling mechanism with a 1 ms timeslot duration
and 0.5 ms scheduling delay, supporting high priority tasks
preempting non-guaranteed RB from low priority tasks. The
network layer incorporates an M/M/1 queueing model to
compute queueing delay, with high priority task jitter required
to satisfy Tji <5 ms to meet URLLC standards.
The experimental data comes from public datasets, includ-
ing fusion perception data from roadside lidar, millimeter-wave
radar, and on-board unit devices, collected at a frequency
of 10 Hz. And data covers the historical trajectories, real-
time locations, and environmental parameters of 2000 test
vehicles. This experiment employs the NVIDIA Jetson Xavier
NX, a typical hardware platform for resource-constrained
RSUs, to simulate real deployment environments. Testing was
conducted using Python, with PyTorch 2.0 serving as the deep
learning framework. Each test was repeated 30 times, with
averages taken to mitigate random variation. By comparing
the delay distribution with publicly available IoV test datasets
from NGSIM and ApolloScape, the error was controlled within
10%, thereby validating the model’s effectiveness. The specific
simulation parameter settings are shown in Table II.
B. Results Analysis
1) Trajectory Prediction
This experiment is divided into model trajectory prediction
simulation and RSUs resource allocation simulation based
on 5G slicing technology on the Graph-GAN model. The
effectiveness of the Graph-GAN model is evaluated based
on the trajectory prediction losses in both the Generator and
Discriminator, as well as the accuracy of the model’s output.
Additionally, the rationality and applicability of 5G network
slicing in RSUs resource allocation are also assessed.
This experiment compares the Generator and Discriminator
losses of the CNN-GAI vehicle trajectory prediction model
and the proposed Graph-GAN model during trajectory predic-
tion, as illustrated in Fig.4. The comparison aims to provide
a preliminary assessment of the Graph-GAN model’s superior
performance in trajectory prediction.
As evident from the two plots in Fig.4, the Generator
Loss of the CNN-GAI model exhibits significant fluctuations
in the early stages and remains markedly higher than the
Discriminator Loss in the later stages. Furthermore, the error
bars corresponding to the Generator Loss are consistently
longer than those for the Discriminator Loss. This indicates
that the Generator’s capabilities are weaker than those of the
Discriminator, resulting in insufficient training stability and an
inadequate learning of the true trajectory distribution. In con-
trast, the loss curve for the Graph-GAN model demonstrates
that both Generator and Discriminator losses decline rapidly in
the early stages before stabilising throughout the remainder of
training. The gap between Generator and Discriminator losses
remains narrow, and the corresponding error bars for both are
compact. This indicates that the Generator and Discriminator
have achieved a favourable equilibrium in their competitive
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 11
TABLE II: Experimental Parameters
Symbol Description
Zn RSUs block deployment
Pr, Pt Power of the vehicle receiving the RSUs signal and the
RSUs transmitting the signal
Gt, Gr Transmitting antenna and receiving antenna benefits
λ Signal wavelength
Rd Actual data transmission rate between vehicles and RSU
Bm, B Frequency domain bandwidth and communication band-
width of each RSUs RB are both 180 KHz
rm Number of allocated RB
N0 Noise power spectral density
α, β, γ Weighting factor, and α + β + γ = 1
P , Ppre, Ptr Vehicle’s current location information, predicted trajectory
information, and actual trajectory information
L
′
G, L
′
D Updated Generator and Discriminator loss functions
λG, λD Regularisation coefficient
Rk (t) Number of RB allocated to priority k at time t
η Global resource utilization rate, with the research objective
of maximising it
Pv,t Vehicle-mounted transmit power, set to 20dBm
Gv,r Vehicle-mounted receiving antenna gain, rated at 2dBi
ε Smoothness coefficient,and ε = 0.7
Tm Processing delay for m-th class tasks, and Tm ≤ τm, τm
is the maximum tolerable delay
Pv,k (t) Predicted probability of vehicle v generating k types of
tasks
ρ (t) Task density in each region
λq,m Proportion of task type m in region Ωq
ral
q,m, rac
q,m Number of RB allocated for the m-th type of task in region
Ωq and actual number of RB required
Rt
q Total number of RB allocated to region Ωq
fd Doppler shift, expressed by the formula: fd = v·fc
c
fc Operating frequency band, set to 5.9GHz
σR, σS Standard deviation of the Rayleigh Fading coefficient and
the Log-Normal Shadowing Fading coefficient are 0.1dB
and 8dB respectively
IMUI Multi-user interference, value of 5dBm
SNR Signal interference
N0 Thermal noise power spectral density, value of Thermal
noise power spectral density, value of -174dBm/Hz
Tq M/M/1 queueing model calculates queueing delay using
the formula: Tq = ρ
µ·(1−ρ)
ρ Queue utilization rate, formula: ρ = λ
µ
λ Arrival rate of tasks with different priorities, λh = 100/s,
λm =50/s
µ Service rate, formula: µ = k · rm, where k =180KHz/RB
interaction, with robust training stability. The Generator has
successfully produced trajectories approximating the true dis-
tribution, rendering the Discriminator unable to accurately
distinguish between real and generated trajectories. This arises
because graph neural networks effectively capture complex
vehicle interactions, while GAN continuously optimise Gener-
ator and Discriminator performance through their adversarial
mechanism. This accelerates convergence and enhances sta-
bility during training, thereby improving trajectory prediction
quality and reliability.
As we can see, Fig.4 shows that the Graph-GAN model is
more stable in training. Next, we will discuss the trajectory
prediction results. We selected five groups of vehicle samples
on the road, with each group containing 100 vehicle trajecto-
ries. By calculating the average of the 100 trajectory positions,
this paper compares the prediction results of the Graph-GAN
vehicle trajectory prediction model, the CNN-GAI [37], the
CNN [38], and the Particle Swarm Optimization (PSO) [39],
as shown in Fig.5.
(a) CNN-GAI trajectory model
(b) Graph-GAN trajectory model
Fig. 4: Trajectory prediction model of different strategy.
As shown in Fig.5, the Graph-GAN model exhibits the
highest degree of alignment between its predicted trajectories
and actual trajectories, with an average positional error of just
0.85 m and a standard deviation of 0.32 m, demonstrating
strong predictive accuracy and stability. In contrast, the CNN-
GAI model has an average error of 1.52 m and a standard
deviation of 0.48 m. While its prediction results are close
to the actual trajectory, the deviation increases in dynamic
scenarios such as turns. The error of the CNN model further
increases to 2.37 m with a standard deviation of 0.76 m, while
the PSO algorithm model performs the worst, with an average
error of 3.14 m and a standard deviation of 1.05 m, showing
significant trajectory fluctuations and severe deviations. These
quantitative data further validate the superiority of the Graph-
GAN model. By synergistically optimising GAN and GNN,
which significantly improves trajectory prediction accuracy in
complex scenarios while maintaining a low standard deviation,
providing a more reliable data foundation for subsequent RSUs
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 12
(a) Graph-GAN model
 (b) CNN-GAI model
(c) CNN model
 (d) PSO algorithm model
Fig. 5: Trajectories comparison of different prediction model.
resource scheduling.
2) Resource Allocation
To validate the practical effectiveness of the proposed
GenAI-5GS integrated offloading method, this experiment
further combined the trajectory prediction results of Graph-
GAN to conduct a simulation analysis of the performance
of 5G slicing technology in RSUs resource allocation. The
experiment covered the entire morning rush hour simulation
cycle using 100 time steps, focusing on evaluating two key
metrics, resource utilization rate and task offloading delay.
These metrics were compared with those of traditional Static
Resource Allocation (Static-RA) [40] methods and Dynamic
Resource Allocation (Dynamic-RA) [41] methods.
Resource utilization serves as a key metric for evaluating
the efficiency of resource allocation within the RSUs. In this
paper, resource utilization specifically denotes the RB utiliza-
tion rate of the RSUs, defined as the ratio of the actual number
of RB allocated to tasks to the total number of available RB
within the RSUs. The RB actually allocated must satisfy two
conditions. Firstly, they must be assigned to high, medium,
or low priority task slices. Secondly, they must be actively
occupied by tasks within the time step. The dynamic resource
allocation across high, medium, and low priority tasks based
on 5G slicing technology is illustrated in Fig.6. This diagram
depicts the dynamic resource allocation process within the
proposed method, where the initial allocation ratio of the
three priority levels is set at 60:25:15. Using this baseline,
the allocation quotas are adjusted during runtime through a
predictive model, enabling dynamic resource allocation and
management.
As shown in Fig.6, high priority tasks initially occupy
approximately 60% of the resource quota. When a surge in
high priority tasks is predicted, such as during the morning
rush hour from 8:10 to 8:15 (step length 40-60), vehicles
Fig. 6: Time variation between different task priorities in
GenAI-5GS resource allocation methods.
merge from ramps onto the main road, Graph-GAN anticipates
high-density areas and shifts 5% of resource slices toward high
priority tasks, maintaining a utilization rate of 98%, thereby
validating the accuracy of prediction-driven adjustments. The
medium priority quota ensures basic requirements while dy-
namically adapting to changes in high priority tasks. Low
priority tasks are always guaranteed a minimum threshold
of 10 RB, with only minor adjustments made when system
resources are surplus or scarce, ensuring the continuous pro-
cessing of non-real-time tasks. Following task prioritisation,
resource utilization is analysed as illustrated in Fig.7. The
resource utilization data is calculated based on actual RB
occupancy within each time step, with averages taken every
10 time steps.
Fig. 7: Comparison chart of resource utilization rates for
different resource allocation methods.
As shown in Fig.7, the Static-RA method achieves 100%
utilization because it allocates all RB statically. However, ap-
proximately 25% of RB remain idle resources occupied by low
priority tasks, resulting in an actual effective utilization rate of
only 75%±3%. This may cause high priority tasks to become
blocked due to resources being permanently occupied by low
priority tasks. The Dynamic-RA method dynamically adjusts
resources based on real-time task queues, demonstrating re-
sponsiveness to task variations. However, relying solely on
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 13
current queue information without forward-looking prediction
introduces allocation lag during high-speed vehicle movement
or sudden task surges, resulting in resource idleness. The
GenAI-5GS approach integrates Graph-GAN trajectory predic-
tion with 5G slice dynamic management, achieving near 100%
utilization with idle RB accounting for less than 1%. This
closed-loop mechanism of ‘Predict-Allocate-Adjust-Recover’
pre-allocates resource slices for forecasted vehicle trajectories
in hotspot areas, ensuring precise resource matching during
traffic fluctuations. This integrated technology demonstrates
significant advantages in balancing resource utilisation effi-
ciency with dynamic adaptability.
As we can see, Fig.6 and Fig.7 clearly illustrates the
dynamic resource allocation logic between tasks of different
priorities in the GenAI-5GS method based on 5G slicing
technology, validating the effectiveness of the baseline quota
and predictive adjustment mechanism in fine-grained resource
management. Next, we will further analyse the differences
in delay control between the GenAI-5GS method and tra-
ditional Static-RA and Dynamic-RA methods, as shown in
Fig.8, thereby providing direct evidence for evaluating the
optimization effect of integrated technology on the real-time
performance of complex tasks.
Fig. 8: Task offloading delay comparison.
As shown in Fig.8, the Dynamic-RA method exhibits the
greatest delay fluctuations and the highest number of extreme
spikes. This stems from its reliance solely on real-time task
queues for resource adjustment, resulting in pronounced lag
and difficulty in handling sudden task surges. The Static-RA
method exhibits fluctuating but milder delay, stemming from
certain high priority tasks failing outright due to resource
shortages under fixed allocation, thus not being included
in delay statistics. The GenAI-5GS approach demonstrated
optimal performance, owing to the synergistic collaboration
between Graph-GAN prediction and 5G slicing. Proactive re-
source allocation prevents queuing, while dynamic adjustment
mechanisms ensure stable delay. Furthermore, to further vali-
date the stability of the GenAI-5GS approach, we conducted
comparative experiments on high priority tasks under varying
SNR conditions, as illustrated in Fig.9. The SNR range for this
experiment was set from 5 dB to 30 dB, with delay statistics
calculated using the same methodology as in Fig.8.
Fig. 9: Comparison of average delay for high priority tasks
under different SNR.
As shown in Fig.9, the delay of all three methods decreases
with increasing SNR. However, the GenAI-5GS method
consistently maintains optimal performance, with signifi-
cantly lower delay fluctuations than traditional approaches. At
SNR=5dB, GenAI-5GS achieves an average delay reduction
of 28.2% compared to Dynamic-RA and 41.0% compared to
Static-RA. This advantage stems from Graph-GAN trajectory
prediction proactively identifying low quality channel regions.
Through a bidirectional feedback mechanism, it expands the
emergency resource pool by 15%, prioritising retransmission
resources for critical tasks and mitigating retransmission con-
gestion caused by poor channel conditions. As SNR increased
to 20 dB, transmission delay decreased significantly. The dy-
namic resource allocation of the 5G slice precisely matched the
predicted task demands, reducing the proportion of queueing
delay from 21.7% at SNR=5dB to 8.4%. As SNR further
increases to 30 dB, GenAI-5GS maintains stable delay, with
bit error rate approaching the URLLC requirement of 10 -5
and retransmission delay becoming negligible. The GenAI-
5GS approach’s advantage lies in its precise resource matching
through ‘Prediction-Slicing’ synergy. By using Graph-GAN to
pre-allocate RB to high SNR zones where vehicles are about
to enter, it effectively avoids the real-time adjustment lag of
Dynamic-RA and the fixed resource wastage of Static-RA.
C. QoS Multi-dimensional Performance Analysis
To further validate the GenAI-5GS method’s capability
in safeguarding multi-dimensional QoS requirements, rather
than relying solely on radio block count to measure service
quality, this experiment introduces three core QoS metrics:
transmission reliability, delay jitter, and bandwidth stability.
The performance differences between GenAI-5GS and tra-
ditional methods Static-RA and Dynamic-RA are compared,
with results shown in Fig.10.
As shown in Fig.10, GenAI-5GS delivers optimal perfor-
mance across all QoS dimensions. For high priority URLLC
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 14
(a) Transmission reliability (high priority)
 (b) Time delay jitter (high priority)
(c) Bandwidth stability (medium priority)
 (d) Task completion rate (low priority)
Fig. 10: Multidimensional performance comparison of differ-
ent QoS methods.
tasks, its transmission reliability reaches 99.9995%, surpassing
Dynamic-RA by 0.0495 percentage points and Static-RA by
0.0795 percentage points. This advantage stems from the
model’s allocation of 5% QoS-guaranteed redundant RB for
high priority tasks. When the channel bit error rate approaches
the 10-5 threshold, these redundant RB rapidly trigger HARQ
retransmissions, preventing task failure. Regarding delay jitter,
GenAI-5GS exhibits a high priority task delay fluctuation of
3.2±0.5 ms, representing merely 36.8% of Static-RA and
50.8% of Dynamic-RA. This is because Graph-GAN proac-
tively predicts vehicle channel quality changes, prioritising
high priority tasks for scheduling onto high quality RB with
SNR>20 dB, thereby mitigating delay jitter caused by channel
fluctuations.
For medium priority tasks, GenAI-5GS exhibits bandwidth
stability of less than or equal to 8%, meeting the industry
tolerance threshold of ±0.5 ms. In contrast, Dynamic-RA
experiences bandwidth fluctuations of 15.2% due to lag in real-
time adjustments, while Static-RA, with its fixed allocation,
demonstrates lower volatility but incurs 25% idle resources.
Regarding task completion rates for low priority tasks, GenAI-
5GS achieved 92.3%, slightly outperforming both Dynamic-
RA and Static-RA. It further supports temporary buffering
during network congestion, thereby preventing frequent task
discards.
In summary, the Graph-GAN model reduces vehicle tra-
jectory prediction errors by 44% compared to the CNN-GAI
model, providing a high precision foundation for resource
scheduling. Furthermore, the GenAI-5GS fusion algorithm
achieves synergistic optimization in both resource utiliza-
tion and task delay dimensions. Compared to conventional
approaches, resource utilisation improved by 14.9%, while
baseline delay decreased by 16% relative to Static-RA and
by 22% relative to Dynamic-RA. Delay performance across
varying SNR conditions also demonstrated optimality for the
GenAI-5GS fusion algorithm. Furthermore, the GenAI-5GS
approach achieves optimization from single RB quantity to
multi-dimensional QoS assurance through redundant resource
reservation, combined with channel quality binding and QoS
weight allocation. This fully demonstrates the effectiveness of
generative AI and 5G slicing fusion technology in offloading
complex IoV tasks, providing a viable paradigm for refined
RSUs resource management in dynamic scenarios.
When considering overall metrics, GenAI-5GS demon-
strates a 14.9% improvement in resource utilization compared
to Dynamic-RA, a 16% reduction in task delay relative to
Static-RA, and 22% lower than Dynamic-RA. This synergistic
optimization with QoS guarantees demonstrates that the deep
integration of generative AI with 5G slicing can effectively
adapt to complex task demands in dynamic IoV scenarios,
providing a practical technical paradigm for refined RSUs
resource management.
VI. C ONCLUSION
The proposed GenAI-5GS integrated offloading approach
effectively resolves the challenges of dynamic adaptation and
latency control in complex IoV task offloading through the
deep coupling of Graph-GAN and 5G slicing technology, with
simulation experiments demonstrating significant efficacy. The
Graph-GAN vehicle trajectory prediction model, leveraging
synergistic optimization of GAN and GNN, achieves an aver-
age positional error of 0.85 m, single-prediction processing
time of 12.3 ±1.5 milliseconds, and a parameter count of
1.2×106 while maintaining CPU/GPU utilisation below 50%
on resource-constrained RSUs. This not only provides high
precision support for resource pre-allocation but also guides
RSUs forward-looking deployment through the mapping logic
of ‘Tier-1 hotspots 300 m, Secondary Hotspot 500 m’ mapping
logic to guide proactive RSUs deployment. The GenAI-5GS
approach dynamically calculates resource blocks within the
dedicated 5.9GHz V2X band, adapts to multiple modula-
tion coding schemes, and establishes a ‘Predict-Allocation-
Adjustment-Recovery’ closed-loop mechanism. This achieves
near 100% resource utilization, reduces task offloading latency
by 16% compared to Static-RA, and 22% lower than Dynamic-
RA. It simultaneously guarantees 99.9995% transmission reli-
ability for high priority URLLC tasks, 3.2 ±0.5 ms delay jitter,
and less than or equal to 8% bandwidth stability for medium
priority tasks. The innovative ‘Prediction Accuracy-Resource
Elasticity’ bidirectional feedback mechanism overcomes lim-
itations of single-technology approaches. However, research
shortcomings remain, the model has not been validated in real
extreme scenarios such as heavy rain or dense fog, Graph-
GAN’s real-time performance requires enhancement in scenar-
ios exceeding 120 vehicles/km, and its adaptability for multi-
RSUs collaborative scheduling warrants further exploration.
Future work will involve field testing to optimise robustness in
non-ideal environments, lightweight Graph-GAN architectures
to accelerate response times, and integration with 6G technol-
ogy to expand multi-RSUs collaborative scenarios. This will
provide more robust support for the large-scale deployment of
intelligent transport systems.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 15

## § Acknowledgment

The authors gratefully acknowledge the insightful comments
from the anonymous reviewers.

## § References

[1] GSM Association, “Global Mobile Economy Development 2022 report,”
2022.
[2] F. Tang, B. Mao, N. Kato et al., “Comprehensive Survey on Machine
Learning in Vehicular Network: Technology, Applications and Chal-
lenges,” IEEE Commun. Surv. Tutorials. , vol. 23, no. 3, pp. 2027–2057,
2021, doi:10.1109/COMST.2021.3089688.
[3] Y . Lu, X. Huang, K. Zhang et al., “Blockchain Empowered Asyn-
chronous Federated Learning for Secure Data Sharing in Internet of
Vehicles,” IEEE Trans. Veh. Technol. , vol. 69, no. 4, pp. 4298–4311,
2020, doi:10.1109/TVT.2020.2973651.
[4] T. Deng, Y . Chen, G. Chen et al., “Task Offloading Based on edge Collab-
oration in MEC-Enabled IoV Networks,” ACM Trans. Internet Technol. ,
vol. 25, no. 2, pp. 197–207, 2023, doi:10.23919/JCN.2023.000004.
[5] Y . -J. Ku, S. Baidya and S. Dey, ”Uncertainty-Aware Task Offloading
for Multi-Vehicle Perception Fusion Over Vehicular Edge Computing,”
IEEE Trans. Veh. Technol. , vol. 72, no. 11, pp. 14906-14923, 2023,
doi:10.1109/TVT.2023.3284369.
[6] W. Zhao, Y . Cheng and Z. Liu, ”Advancing RSU-assisted Auto-
mated Vehicle Networks: A DRL Empowered Distributed Task Offload-
ing Framework,” IEEE Network. , vol. 39, no. 2, pp. 242-249, 2025,
doi:10.1109/MNET.2024.3449851.
[7] M. Khabbaz, ”Deadline-Constrained RSU-to-Vehicle Task Offloading
Scheme for Vehicular Fog Networks,” IEEE Trans. Veh. Technol. , vol.
72, no. 11, pp. 14955-14961, 2023, doi:10.1109/TVT.2023.3285255.
[8] B. Ko, S. Liu, S. Son et al., ”RSU-Assisted Adaptive Scheduling
for Vehicle-to-Vehicle Data Sharing in Bidirectional Road Scenarios,”
IEEE Trans. Intell. Transp. Syst. , vol. 22, no. 2, pp. 977-989, 2021,
doi:10.1109/TITS.2019.2961705.
[9] K. Moghaddasi, S. Rajabi, F. S. Gharehchopogh, “An advanced
deep reinforcement learning algorithm for three-layer D2D-edge-
cloud computing architecture for efficient task offloading in the In-
ternet of Things,” Sustainable Comput. Inf. Syst. , vol. 43, 2024,
doi:10.1016/j.suscom.2024.100992.
[10] K. Asghari, M. Masdari, F. S. Gharehchopogh, “Multi-swarm and
chaotic whale-particle swarm optimization algorithm with a selection
method based on roulette wheel,” Expert Syst. , vol. 38, no. 8, 2021,
doi:10.1111/exsy.12779.
[11] M. Yan, H. Guo, C. A. Chan et al., “Semantic Communication-Enabled
Multi-Access Edge Computing Network Resource Optimization in the 6G
Era,” IEEE Wireless Commun., 2025, doi:10.1109/MWC.2025.3600791.
[12] Y . Guo, Y . Zhang, L. Niu et al., “Conflict Probability based
Path Planning Algorithm for Internet of Vehicles,” IAEAC., 2021,
doi:10.1109/IAEAC50856.2021.9390979.
[13] M. Yan, R. Xiong, Y . Wang et al., “Edge Computing Task Offloading
Optimization for a UA V-assisted Internet of Vehicles via Deep Reinforce-
ment Learning,”IEEE Trans. Veh. Technol., vol. 73, no. 4, pp. 5647–5658,
2024, doi:10.1109/TVT.2023.3331363.
[14] T. Z. H. Ernest and A. S. Madhukumar, “Computation Offloading in
MEC-Enabled IoV Networks: Average Energy Efficiency Analysis and
Learning-Based Maximization,” IEEE Trans. Mob. Comput. , vol. 23, no.
5, pp. 6074–6087, 2024, doi:10.1109/TMC.2023.3315275.
[15] F. S. Gharehchopogh, S. Ghafouri, M. Namazi et al., “Advances in Manta
Ray Foraging Optimization: A Comprehensive Survey,” J Bionic Eng. ,
vol. 21, pp. 953–990, 2024, doi:10.1007/s42235-024-00481-y.
[16] A. D. Pazho, G. A. Noghre, V . Katariya et al., “VT-Former: An
Exploratory Study on Vehicle Trajectory Prediction for Highway Surveil-
lance through Graph Isomorphism and Transformer,” CVPRW., 2024,
doi:10.1109/CVPRW63382.2024.00574.
[17] M. Wang, L. Zhang, J. Chen et al., “A Hybrid Trajectory Predic-
tion Framework for Automated Vehicles With Attention Mechanisms,”
IEEE Trans. Transp. Electrif. , vol. 10, no. 3, pp. 6178–6194, 2024,
doi:10.1109/TTE.2023.3346668.
[18] C. He, W. Jiang, X. Wang et al., “Deep Reinforcement Learning and
Nash Equilibrium Game-Based Task Offloading Optimization Strategy
for the IoV ,” IEEE Sens. J. , vol. 25, no. 10, pp. 18384–18393, 2025,
doi:10.1109/JSEN.2025.3558228.
[19] K. Wu, H. Shi, X. Li et al., “Graph-Based Interaction-Aware Multimodal
2D Vehicle Trajectory Prediction Using Diffusion Graph Convolutional
Networks,” IEEE Trans. Intell. Veh., vol. 9, no. 2, pp. 3630–3643, 2024,
doi:10.1109/TIV .2023.3341071.
[20] V . Mistry, B. Vaidya and H. T. Mouftah, “Evaluation of LSTM GAN for
Trajectory Prediction in Connected and Autonomous Vehicles,” IWCMC.,
2024, doi:10.1109/IWCMC61514.2024.10592580.
[21] Y . Lu, W. Wang, X. Hu et al., “Vehicle Trajectory Prediction in
Connected Environments via Heterogeneous Context-Aware Graph Con-
volutional Networks,” IEEE Trans. Intell. Transp. Syst. , vol. 24, no. 8,
pp. 8452–8464, 2023, doi:10.1109/TITS.2022.3173944.
[22] Q. Cui, X. Zhao, W. Ni et al., “Multi-Agent Deep Reinforcement
Learning-Based Interdependent Computing for Mobile Edge Computing-
Assisted Robot Teams,” IEEE Trans. Veh. Technol. , vol. 72, no. 5, pp.
6599–6610, 2023, doi:10.1109/TVT.2022.3232806.
[23] D. Cao, N. Gu, R. S. Sherratt et al., “Energy-Efficient Multi-
Vehicle Edge Networks: A Joint Optimization Algorithm for Task
Splitting Offloading and Resource Allocation,” SmartIoT., 2023,
doi:10.1109/SmartIoT58732.2023.00021.
[24] Y . Chen, Z. Liu, X. Lu et al., “Risk-Aware Reinforcement Learn-
ing Based Federated Learning Framework for IoV ,” WCNC., 2024,
doi:10.1109/WCNC57260.2024.10571032.
[25] Q. Wu, W. Wang, P. Fan et al., “URLLC-Awared Resource Allocation for
Heterogeneous Vehicular Edge Computing,” IEEE Trans. Veh. Technol.,
vol. 73, no. 8, pp. 11789–11805, 2024, doi:10.1109/TVT.2024.3370196.
[26] Z. Nezami , E. Chaniotakis and E. Pournaras, “When Computing follows
Vehicles: Decentralized Mobility-Aware Resource Allocation for Edge-to-
Cloud Continuum,” IEEE Internet Things J. , vol. 12, no. 13, pp. 23324–
23340, 2025, doi:10.1109/JIOT.2025.3552504.
[27] L. Liu, J. Feng, X. Mu et al., “Asynchronous Deep Reinforcement Learn-
ing for Collaborative Task Computing and On-Demand Resource Alloca-
tion in Vehicular Edge Computing,”IEEE Trans. Intell. Transp. Syst., vol.
24, no. 12, pp. 15513–15526, 2023, doi:10.1109/TITS.2023.3249745.
[28] D. A. Chekired, M. A. Togou, L. Khoukhi, et al., “5G-Slicing-Enabled
Scalable SDN Core Network: Toward an Ultra-Low Latency of Au-
tonomous Driving Service,” IEEE J. Sel. Areas Commun. , vol. 37, no.
8, pp. 1769–1782, 2019, doi:10.1109/JSAC.2019.2927065.
[29] N. Cheng, T. Pamukiu and E. Melike, “Reinforcement Learning Based
Resource Allocation for Network Slices in O-RAN Midhaul,” CCNC.,
2023, doi:10.1109/CCNC51644.2023.10059966.
[30] M. S. Onim, H. Nyeem, H. Arnob et al., “Unleashing the power of
generative adversarial networks: A novel machine learning approach for
vehicle detection and localisation in the dark,” Cognit. Comput. Syst., vol.
5, no. 3, pp. 169–180, 2023, doi:10.1049/ccs2.12085.
[31] X. Wang, C. He, W. Jiang et al., “Generative AI-Based Dependency-
Aware Task Offloading and Resource Allocation for UA V-Assisted
IoV ,” IEEE Open J. Commun. Soc. , vol. 6, pp. 3932–3949, 2025,
doi:10.1109/OJCOMS.2025.3562720.
[32] K. Fahime and H. Ekram, “Generative AI for the Optimiza-
tion of Next-Generation Wireless Networks: Basics, State-of-the-
Art, and Open Challenges,” IEEE Commun. Surv. Tutorials. , 2024,
doi:10.1109/COMST.2025.3535554.
[33] M. Shatnawi and M. Bani Younes, ”An Enhanced Model for Detect-
ing and Classifying Emergency Vehicles Using a Generative Adver-
sarial Network (GAN),” Vehicles., vol. 6, no. 5, pp. 1114-1139, 2024,
doi:10.3390/vehicles6030053.
[34] W. Jiang, S. Anton and H. Schotten “Intelligence Slicing: A Uni-
fied Framework to Integrate Artificial Intelligence into 5G Networks,”
WMNC., 2019, doi:10.23919/WMNC.2019.8881402.
[35] E. Balevi and J. Andrewa “Wideband Channel Estimation With a
Generative Adversarial Network,” IEEE Trans. Wireless Commun. , vol.
20, no. 5, pp. 3049–3060, 2020, doi:10.1109/TWC.2020.3047100.
[36] C. Zhuan, P. Li, Y . Liu et al., “Generative AI-Assisted Mobile-
Edge Computation Offloading in Digital-Twin-Enabled IIoT,” IEEE
Internet Things J. , vol. 12, no. 10, pp. 13248–13258, 2025,
doi:10.1109/JIOT.2025.3547370.
[37] C. He, W. Jiang, X. Wang et al., “Generative AI-Enhanced Task
Offloading Strategy for the IoV: An RSU-RSU Load-Balancing Per-
spective,” IEEE Networking Lett. , vol. 7, no. 3, pp. 161–165, 2025,
doi:10.1109/LNET.2025.3542094.
[38] R. Izquierdo, A. Quintanar, D. F. Llorca et al., “Vehicle trajectory
prediction on highways using bird eye view representations and deep
learning,”Appl Intell., vol. 53, pp. 8370–8388, 2022, doi:10.1007/s10489-
022-03961-y.
[39] Y . Jiang, B. Zhu, S. Yang et al., “Vehicle Trajectory Prediction Con-
sidering Driver Uncertainty and Vehicle Dynamics Based on Dynamic
Bayesian Network,” IEEE Trans. Syst. Man Cybern.: Syst. , vol. 53, no.
2, pp. 689–703, 2022, doi:10.1109/TSMC.2022.3186639.
[40] Q. Gao, S. Lin and G, Zhu, “Joint Vehicular and Static Users Mul-
tiplexing Transmission With Hierarchical Modulation for Throughput
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply. 
IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY , VOL. XX, NO. XX, XXX 2025 16
Maximization in Vehicular Networks,” IEEE Trans. Intell. Transp. Syst. ,
vol. 21, no. 9, pp. 3835–3847, 2020, doi:10.1109/TITS.2019.2934597.
[41] Y . Luo, Y . Wang, Y . Lei et al., “Decentralized User Alloca-
tion and Dynamic Service for Multi-UA V-Enabled MEC System,”
IEEE Trans. Veh. Technol. , vol. 73, no. 1, pp. 1306–1321, 2024,
doi:10.1109/TVT.2023.3308589.
Chao He received the B.E. and M.E. degrees from
School of Electronic and Information Engineering,
Chongqing Three Gorges University, and the Ph.D.
degree from School of Communication and Infor-
mation Engineering, Chongqing University of Posts
and Telecommunications, in 2014 and 2017, respec-
tively. Currently, he is a lecturer in the School of
Electronic and Information Engineering, Chongqing
Three Gorges University. His main research interests
are in modern communication technology. He has
published more than 10 papers in his research area,
including more than 5 papers in refereed journals.
Wenhui Jiang received the B.S. degree in computer
science and Technology from Weifang University in
2023, and is currently pursuing for a master’s degree
in School of Telecommunications, Chongqing Three
Gorges University. Her research direction is task
offloading for IoV , and she has published 3 articles.
Xing Wang received the bachelor’s degree from
the School of Information Engineering, Chongqing
V ocational and Technical University of Mechatron-
ics, Chongqing, China, in 2023. She is currently
pursuing for a master’s degree in the School of
Electronic and Information Engineering, Chongqing
Three Gorges University. Her research focuses on
task offloading in the IoV .
Wanting Wang received the bachelor’s degree from
the School of Electronic and Information Engineer-
ing, Hubei University of Automotive Technology,
Hubei, China, in 2023. She is currently studying in
School of Electronic and Information Engineering,
Chongqing Three Gorges University, Chongqing,
China.Her research interest is mainly IoV .
Hong Na is the Dean of the School of Electric Power
Engineering at Yunnan V ocational College of Water
Resources and Hydropower, Kunming, China. His
research focuses on vehicle-to-grid (V2G) technol-
ogy, smart grid integration, and the development of
practical energy systems for vocational education.
He has led several provincial-level research projects
and actively promotes the application of intelligent
energy technologies in the teaching and training
process.
Xin Xie is a Lecturer/Postdoctoral Fellow with the
School of Automation, Chongqing University of
Posts and Telecommunications, Chongqing, China.
He is mainly engaged in the research of Industrial In-
ternet of Things, information age, real-time schedul-
ing, edge computing, vision-assisted millimeter-
wave communication, and other directions. In recent
years, he has presided over a number of scientific
research projects. He has published eight academic
articles, applied for seven invention patents, and
published one textbook.
This article has been accepted for publication in IEEE Transactions on Vehicular Technology. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TVT.2026.3660468
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:04:35 UTC from IEEE Xplore.  Restrictions apply.
