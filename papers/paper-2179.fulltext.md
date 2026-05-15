---
paper_id: "paper-2179"
source_pdf_sha: "a6b7ba0123217d0ca36ce9c91119b818ae4aadb357f7f89f8d8524bb0b65a591"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 3
  page_count: 8
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2179 — fulltext
## §unknown-1

IEEE Network • July/August 2025
82
0890-8044 © 2024 IEEE. All rights reserved, including rights for text and data mining,  
and training of artificial intelligence and similar technologies.
Abstr Act
Computing Power Network (CPN), as an inte -
gration of heterogeneous computing resources, 
has turned to be difficult to cope with the 
rapid growth of end users and strict task delay 
constraints due to the possible long-distance trans -
mission between its service facilities and remote 
users. To overcome this problem, we propose an 
Edge Computing Power Network (ECPN), which 
reduces long-distance transmission overhead, opti-
mizes resource utilization, and improves system 
performance by fully utilizing edge computing 
resources. In the area of resource scheduling, 
traditional machine learning is widely used due 
to its fast problem solving capabilities. However, 
traditional machine learning faces challenges in 
ECPN, particularly with handling heterogeneous 
tasks and adapting to highly dynamic network 
conditions. To address these challenges, we pro-
pose a large model-enabled ECPN framework that 
enhances the capabilities of ECPN in task offload-
ing and resource allocation while optimizing the 
deployment of large models in the framework. To 
demonstrate the advantages of this framework, we 
introduce a smart transportation application sce -
nario and employ a large language model based 
graph multi-agent deep reinforcement learning 
algorithm to determine optimal task matching 
strategies that balance energy consumption and 
privacy protection in the ECPN. Experimental 
results demonstrate that the algorithm applied 
in this framework reduces energy consumption, 
decreases the convergence time for task match-
ing, and enhances privacy protection in ECPN.
Introduct Ion
In the 5G/B5G era, Computing Power Network 
(CPN) is a service paradigm that connects com-
puting resource devices from both core networks 
and edge sides to achieve ubiquitous and pow -
erful processing capabilities [1]. However, when 
a CPN component relies on long-distance or 
low-capacity network connections, the task data 
offloading latency may increase, potentially hin-
dering the efficiency and responsiveness of the 
service process [2].
To reduce transmission latency while ensur -
ing task processing efficiency, we propose an 
Edge Computing Power Network (ECPN), which 
improves resource utilization and task processing 
efficiency by integrating the computing resources 
of edge nodes close to the task generator. 
Although traditional Machine Learning (ML) has 
been widely used in resource scheduling in vari-
ous networks, it still faces severe challenges being 
applied in ECPN with large-scale edge nodes and 
dynamic network states. These challenges include 
inefficiencies in processing concurrent heteroge -
neous tasks and the lack of adaptive resource 
allocation and energy-efficient scheduling strate -
gies tailored to diverse task requirements.
Considering these challenges, we intro -
duce large models into ECPN to leverage their 
advanced capabilities in global optimization and 
adaptive control to further improve task sched-
uling efficiency and resource utilization. Large 
models have a complete structure and a large 
number of parameters, and by training on large-
scale datasets, they can automatically extract 
features and identify patterns without relying on 
predefined features [3] . This capability makes 
large models more adaptable than traditional ML 
models when handling heterogeneous tasks and 
processing large-scale data in complex and evolv -
ing scenarios [4] . The global optimization and 
adaptive adjustment capabilities of large models 
improve task processing efficiency and reduce sys-
tem response time, especially in parallel multi-task 
scheduling and timely adaptation to dynamic envi-
ronments [5]. For example, Rong and Rutagemwa 
[6] applied large models to the intelligent control 
of a 6 G global integrated network to optimize 
internet of things services through efficient 
resource management and adaptive strategies. 
Zhang et al. [7] pioneered a diversity-driven pro-
active caching scheme to optimize network load 
and resource efficiency, which provided inspir -
ing insights for large-scale model deployment in 
edge environments. However, while these works 
have made progress in network optimization, they 
have not explore the integration of large models 
into ECPN with large-scale edge nodes and highly 
dynamic environments.
This paper introduces large models in ECPN 
for the first time to improve the efficiency and 
accuracy of resource allocation for edge comput -
ing nodes. Large models enhance the ability of 
ECPN to extract critical information from hetero-
geneous data through global feature extraction. 
Simultaneously, an adaptive adjustment mecha-
nism optimally reallocates resources in real time, 
enabling effective response to dynamic changes 
in edge computing resources and task require -
ments [8]. Furthermore, the ECPN leverages the 
parallel processing capabilities of large models 
Large Models for Resource Allocation in Edge Computing Power Networks
Liyan Sui , Ke Zhang , Fan Wu , and Xiaoyan Huang
EMPOWERING FUTURE MOBILE NETWORKS WITH  
LARGE MODELS
Digital Object Identifier:
10.1109/MNET.2024.3524611
Date of Current Version:

## §15 July 2025

Date of Publication:

## §31 December 2024

The authors are with the School of Information and Communication Engineering, University of Electronic Science and Technology of 
China, Chengdu 611731, China. Ke Zhang is corresponding author.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
83
to concurrently manage multiple heterogeneous 
tasks, thereby improving performance and 
optimizing resource utilization in dynamic envi-
ronments [9].
Although large models demonstrate signifi-
cant potential across various domains, their 
deployment on edge devices within the ECPN 
framework faces challenges such as resource 
constraints, real-time responsiveness, and the 
maintenance and updating of models [10]. To 
address these issues, we leverage advanced tech-
niques into the large model-enabled ECPN to 
enhance real-time processing, improve model 
reuse, and ensure efficient maintenance in 
resource-constrained settings. First, model 
compression technology is used to effectively 
reduce the complexity of calculations and stor -
age requirements, making large models suitable 
for resource-constrained edge devices. Second, 
distributed inference technology distributes infer -
ence tasks to multiple devices for collaborative 
processing to meet the needs of real-time task 
response. In addition, incremental learning tech-
nology allows large models to continue learning 
new data on top of the original foundation, 
adapting to changes without retraining, thereby 
improving model reusability. To demonstrate the 
effectiveness of the applied techniques and high-
light the advantages of the large model-enabled 
ECPN, we design a multi-agent deep reinforce -
ment learning (MADRL) algorithm based on 
large language models (LLMs) to optimize the 
privacy-preserving task matching strategy for 
ECPN in smart transportation systems.
The rest of this paper is organized as follows. 
The section “Large Models Enabled Edge Com-
puting Power Networks” presents the architecture 
and key aspects of large model integration in the 
ECPN. We formulate a LLM-enabled task match-
ing problem to trade the energy and privacy 
in the section “ LLM-Enabled Privacy-Preserv -
ing Task Matching in ECPN .” Then we evaluate 
the performance of our proposed architecture 
using numerical results in the section “Numerical 
Results .” Finally, the section “Conclusion” con-
cludes this paper.
LArge  Mode Ls en Ab Led  edge  co Mput Ing  p ower  
n etworks
In this section, we propose the large models-enabled 
ECPN framework, and demonstrate applications, 
benefits, challenges, and corresponding solutions of 
the framework.
the  Arch Itecture  of  LArge  Mode L-en Ab Led  ecpn
Fig. 1 shows the architecture of the proposed large 
models empowered ECPN. While CPN integrates 
computing resources from both core networks 
and edge locations to enhance task processing 
capabilities, ECPN specifically concentrates on 
optimizing the use of edge nodes to facilitate the 
deep integration of communication and comput -
ing capabilities at the edge. ECPN improves the 
responsiveness of the system to tasks in different 
environments through a flexible edge resource 
awareness. The architecture of ECPN is composed 
of an edge computing power plane and an appli-
cation plane. In the edge computing plane, the 
FIGURE 1. The architecture for large model empowered ECPN.
Large models enhance the ability of ECPN to extract critical information from heterogeneous data 
through global feature extraction.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
84
computing power of connected edge nodes forms 
a pooled resource to provide computing ser -
vices to end devices. The edge computing nodes 
include base stations (BSs), MEC servers and the 
end devices. The application plane consists of 
tasks and requirements for different application 
scenarios, such as smart transportation, smart 
homes, and smart manufacturing, offloading these 
tasks to the edge computing power plane for pro-
cessing. Edge devices perform dual roles in the 
network. When tasks are generated, these devices 
request computing resources from other nodes 
to meet processing demands. Conversely, when 
idle and equipped with available resources, they 
provide their computing power to support tasks 
generated by other devices.
Based on the ECPN architecture, we further 
explore how to effectively integrate large mod-
els to optimize task scheduling and resource 
allocation. In ECPN, large models are deployed 
by cloud-edge collaboration, where the cloud is 
responsible for training large models and distrib-
uting the pre-trained model parameters to each 
edge node. The edge nodes locally fine-tune 
the large model according to the task require -
ments and available computing resources to 
optimize the inference capability [11]. We use 
model compression and distributed inference 
techniques on edge device to improve resource 
utilization and save computing resource on indi-
vidual edge nodes. With this approach, large 
models in ECPN are reused and maintained 
through incremental learning, enabling them to 
adapt to task requirements and data changes 
in real world scenarios. Incremental learning 
allows the model to learn new data from evolv -
ing environments continuously without retraining 
entirely. This approach reduces the costs asso-
ciated with model updates and ensures that the 
model can adapt to dynamic task requirements 
and variations in environmental data across 
diverse scenarios.
App LIc AtIon  for  LArge  Mode L-en Ab Led  ecpn
Large models enable ECPN to improve the deci-
sion-making ability and performance of the system 
through more accurate data analysis, and achieve 
improvements in the efficiency and responsive -
ness of resource allocation. The main applications 
of the large models in ECPN are as follows.
Smart Home:  Smart homes connect vari -
ous devices, such as sensors, lighting systems 
and cameras, through smart homes, automating 
services and offering personalized experiences 
to enhance user comfort. In this connected 
environment, the ECPN is able to leverage idle 
computing resources from devices like smart -
phones and computers to address additional 
needs for processing environmental data and 
executing collaborative tasks. However, when 
combined with traditional ML methods relying 
on predefined features and local information, 
ECPN faces challenges in meeting diverse and 
dynamic requirements, including handling hetero -
geneous device interactions, adapting to varying 
user preferences, and processing large volumes 
of sensor data. In comparison, large models 
have powerful data learning capabilities and can 
extract global features from heterogeneous data 
generated by multiple devices and sensors in a 
smart home. Leveraging the processing power of 
large models, ECPN effectively utilizes distributed 
computing resources to analyze device interac -
tions, user behavior, and environmental data. This 
enables optimized resource scheduling, accurate 
user need predictions, and real-time device adjust -
ments, enhancing smart home performance and 
user experience.
Smart Transportation:  Smart transporta -
tion is a system with large-scale management, 
covering multiple management areas and inter -
related block road networks, and requiring the 
processing of large environmental data. In smart 
transportation systems, ECPN leverages com -
puting resources from devices like vehicles and 
roadside units to manage tasks such as traffic 
control, route optimization, and accident detec -
tion. With the resource integration capabilities 
of ECPN, the system adapts to traffic fluctuations 
and the flexible distribution of computational 
tasks to moving vehicles and connected devices, 
enhancing the immediacy of task processing and 
the efficiency of resource allocation. When ECPN 
is combined with traditional ML methods, which 
focus on specific regions with constrained data 
related to those regions, it struggles to achieve 
global optimization across multiple areas. Con-
trastingly, large models have powerful global 
feature extraction and adaptive capabilities, and 
can quickly capture changes in a wide range of 
heterogeneous data and optimize scheduling 
strategies in real time. Therefore, ECPN com -
bines with the advantages of large models to 
achieve dynamic task allocation and resource 
allocation adjustments, enabling the system to 
operate efficiently in multiple regions, complex 
road networks, and rapidly changing traffic flows, 
improving the scheduling efficiency and adapt -
ability of smart transportation systems.
Intelligent Manufacturing:  Intelligent man -
ufacturing systems use intelligent algorithm to 
achieve differential production management, 
covering multiple production departments and 
various types of equipment, and emphasizing 
rapid response capabilities. In this scenario, ECPN 
can provide computing services for applications 
such as real-time device monitoring and produc -
tion process optimization by scheduling edge 
computing resources, supporting the needs of 
smart manufacturing. As these tasks have differ -
ent computing requirements and response times, 
they place high demands on resource alloca -
tion and task scheduling in the system. In ECPN, 
although traditional ML algorithms can process 
some tasks in parallel, they are usually limited to 
local tasks, making it difficult to achieve efficient 
parallel processing of multiple heterogeneous 
tasks. Compared with this, the large model has 
powerful parallel processing capabilities, and can 
schedule multiple heterogeneous tasks from dif -
ferent production equipment, sensors and control 
systems, and dynamically allocate computing 
resources based on task priorities and real-time 
In ECPN, although traditional ML algorithms can process some tasks in parallel, they are usually limited 
to local tasks, making it difficult to achieve efficient parallel processing of multiple heterogeneous 
tasks.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
85
requirements. Combined with a large model, 
ECPN can efficiently respond to the diverse needs 
of intelligent manufacturing in terms of differ -
ent production departments and a wide range 
of equipment, reducing task execution time and 
improving overall system performance to meet 
the requirements of rapid response.
b enef Its  for  LArge  Mode Ls In  ecpn
Benefiting from the powerful feature extraction 
capabilities and adaptability of large models in 
ECPN, the network can achieve the following 
benefits.
Improving Resource Utilization: As the num-
ber and diversity of edge devices in ECPN expand, 
the requirements for resource management and 
scheduling escalate to preserve network efficiency 
and ensure responsiveness. Therefore, improving 
the resource utilization of ECPN has become crit -
ical to ensure that the growing demand for tasks 
can be addressed and resource waste minimized, 
improving the performance of the network. Com-
pared with the traditional ML, the large model 
has the ability to perceive the state of comput -
ing nodes and task requirements in all aspects, 
understand the individual features of the device, 
and optimize resource allocation strategies. By 
introducing large models into ECPN, the network 
can efficiently integrate the idle resources of edge 
nodes, flexibly schedule computing tasks, improve 
resource utilization, meet the dynamic needs of 
complex tasks, and improve the overall network 
performance.
Enhancing Dynamic Responsiveness:  In 
ECPN, the task requirements may change rap -
idly in real time, so it is crucial to enhance the 
dynamic response speed of the network. Tradi-
tional ML usually relies on locally limited datasets 
and specific scenarios for model training. When 
the task request changes, the model needs to 
be readjusted or completely retrained leading 
to an increase in task response time. However, 
the large model has excellent dynamic response 
capabilities in the ECPN, and can flexibly uti -
lize the computing resources of edge nodes to 
adjust scheduling strategies according to real-time 
needs. When faced with complex task schedul -
ing and unpredictable loads, large models exhibit 
efficient processing capabilities and great accu -
racy, which can reduce latency and ensure the 
stable operation of the network. This is attributed 
to its training on large-scale data, which empow -
ers large models with powerful feature extraction 
capabilities, enabling them to quickly capture key 
information in dynamic environments and flexibly 
adapt to changing conditions and diverse input 
requirements.
Improving Multitask Processing Efficiency: As 
the variety and volume of heterogeneous tasks 
in the ECPN increase, the network encounters 
greater demands for effective multitasking. Con-
sequently, enhancing the capability to process 
multiple tasks simultaneously has become crucial 
for ensuring the efficient operation of the network. 
The large model has advantages over traditional 
ML models in terms of task priority management 
and intelligent scheduling, which can reduce the 
waiting time between tasks and improve multi-
task processing efficiency. ECPN combined with 
a large model can efficiently manage and execute 
multiple tasks under limited resources, avoid 
resource conflicts, and reduce scheduling delays, 
enhancing the multitask processing capabilities 
and overall performance of the network.
ch ALLenges  And  so Lut Ions  for  LArge  Mode Ls In  ecpn
Although incorporating large models into ECPN 
brings many benefits in terms of agile resource 
scheduling and improving task offloading perfor -
mance, there are still some technical challenges 
in the implementation of ECPN due to insuffi -
cient service resources and increasingly stringent 
latency constraints.
Computation Resource Constraints:  In 
ECPN, edge nodes are required to compute large 
models and process multiple heterogeneous 
tasks in the constraints of their limited comput -
ing resources. This dual requirement increases 
competition for computing resources, placing 
a heavier burden on the system and potentially 
impacting overall performance. To ensure that 
ECPN can process tasks and improve resource 
utilization, we have introduced model compres -
sion techniques such as pruning and quantization 
to compress large models. Quantization reduces 
computation and storage requirements by reduc -
ing model parameters from high to low precision. 
Pruning further reduces the computational com-
plexity of the model by removing unnecessary 
redundant weights in the model that have less 
impact on the results. These two techniques 
enable large models to work efficiently on edge 
nodes with less computing resources, reducing 
computation burden and memory consumption 
in ECPN.
Real-Time Requirements: In ECPN, with the 
increase in the number of tasks and the dynamic 
changes in network conditions, it is particularly 
important to respond quickly and offload tasks 
to suitable edge nodes in real time. However, 
when a large model performs the complete 
inference process on the edge node, it faces the 
tradeoff between the amount of data collected 
and the processing speed. Collecting extensive 
datasets can enhance the training effectiveness 
of models, although it tends to slow down pro-
cessing speeds. Conversely, utilizing smaller 
datasets accelerates model processing but may 
compromise the quality of training outcomes. 
Distributed inference provides an effective solu-
tion for this, distributing the inference task to 
multiple edge nodes for collaborative comput -
ing, enabling ECPN to efficiently distribute the 
task load and make optimal use of the comput -
ing power of multiple nodes to accelerate the 
processing of heterogeneous data. Each node 
processes a part of the tasks, effectively distrib-
uting the computational load. This distributed 
approach, which integrates completed inference 
results, alleviates the burden on individual nodes 
when managing heterogeneous data enhances 
task scheduling efficiency, and ensures real-time 
responses in dynamic environments.
Model Reuse and Maintenance:  As task 
requirements and network conditions change, 
some edge nodes need to frequently update 
large models to adapt to new tasks and data in 
the ECPN. Incremental learning can reduces the 
computation resources and time costs required 
for model updating, while also achieving 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
86
effective model maintenance, by performing 
local updates in steps as new environmental 
data is learned. Using the distributed architec -
ture of ECPN, edge nodes can flexibly allocate 
computing resources based on real-time needs, 
and gradually adapt to new environmental data 
through incremental learning, further improving 
the efficiency of model updates, to enable direct 
reuse in similar scenarios without retraining. In 
this way, the large model-enabled ECPN can 
adapt to dynamic tasks and network conditions 
while facilitating the efficient reuse and continu-
ous update of the model.
LLM-en Ab Led  p r IvAcy -p reserv Ing  tAsk  
MAtch Ing  In  ecpn
To demonstrate the performance of the proposed 
framework, this section formulates the task match-
ing problem of ECPN in smart transportation, 
aiming to optimize the tradeoff between energy 
consumption and privacy protection.
p r IvAcy -p reserv Ing  tAsk  MAtch Ing  Mode L In  ecpn
In ECPN, we use graphs to describe the rela -
tionships between edge computing nodes in 
smart transportation, in order to capture their 
interactions and represent the topology of the 
transportation network. The graph can represent 
either static or dynamic connections between 
nodes, depending on the specific traffic scenario. 
Static graphs are suitable when the node layout 
and communication links are relatively fixed, 
while dynamic graphs are used when vehicles 
move and nodes change frequently. In the graph, 
nodes represent edge devices in smart trans -
portation, edges indicate communication links 
or task dependencies between devices, and the 
state of each node includes the location, neigh-
boring devices, and processing power. The graph 
captures the distribution of devices and resources 
in a smart transportation network, adapting to 
changing traffic flows, device movements, and 
task requirements.
For task matching in smart transportation, the 
tasks generated by an end device are assigned 
to other end devices or edge servers based on 
the task size, required computing resources, and 
latency requirements [12]. We define task match-
ing as a one-to-many process aimed at finding 
the most suitable list of edge computing nodes, 
while applying differential privacy to task infor -
mation to protect the privacy of tasks. Differential 
privacy [13] is a widely used privacy protection 
framework with a strong mathematical founda-
tion, which protects data by introducing random 
noise to the query results. The noise is generated 
by a Laplace mechanism, and its scale is adjusted 
according to the sensitivity of the task information. 
The privacy budget controls the level of privacy 
protection, and the smaller the privacy budget, 
the higher the level of privacy protection. In our 
model, noise is added to the task information 
to protect the privacy of the task and the users 
involved in the matching process. During the task 
matching process, the strength of privacy pro -
tection is directly proportional to the amount of 
noise in the task information. As the degree of pri-
vacy protection increases, the smaller the privacy 
budget value, the more noise is introduced into 
the task information, which leads to an increase in 
errors in the matching process. The accumulation 
of these errors will increase the computational 
burden on the system, leading to an increase in 
energy consumption.
We formulate the task matching problem 
to minimize the energy consumption of task 
matching while protecting privacy and ensuring 
task requirements. Here the energy consump-
tion of task matching is defined as the sum of 
FIGURE 2. The task matching model based on LLMs and MADRL.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
87
the energy consumption of task transmission 
and the energy consumption of task computa-
tion. We minimize energy consumption while 
protecting the privacy of tasks by adjusting cho-
sen computing nodes, the computing resources 
allocated to subtasks, and the privacy budget of 
tasks. It is critical to note that the adjustment 
of the variables must comply with the following 
three constraints. The first is the privacy bud -
get for tasks, which should be in the common 
range of differential privacy. The second one 
ensures that the computing resources allocated 
to task by edge computing node are less than 
the maximum value of the computing resource 
of node. The last constraint ensures that the 
total latency of task is less than the latency 
requirement of task.
LLMs And  g r Aph  MAdr L d r Iven  tAsk  MAtch Ing
To address the optimization problem of task 
matching, we propose a model based on LLMs 
and graph MADRL, as shown in Fig. 2 . LLMs is 
a type of deep learning-based artificial intelli -
gence model that can process large-scale tasks 
through training on a large amount of data, which 
improve the efficiency of task scheduling in edge 
computing [14] . In task matching, LLMs pro -
vides the system with a comprehensive view of 
node states and task requirements by extracting 
global features from heterogeneous data at each 
edge node. These features cover the topologi -
cal relationships between nodes, resource status, 
computing power, task priority, and the dependen-
cies between nodes and tasks. By integrating this 
information, LLMs provides a basis for subsequent 
decision-making processes, ensuring that the net -
work can quickly adapt and respond effectively 
in the face of heterogeneous tasks and dynamic 
environments. Although LLMs does not directly 
perform the task matching decision, it improves 
the efficiency of task matching by providing crit -
ical global information support for subsequent 
optimization strategies. Combining LLMs with the 
MADRL model, the global features extracted by 
LLMs provide input for the MADRL, enabling it to 
dynamically optimize task matching and resource 
allocation and identify the optimal strategy. The 
global feature extraction and dynamic adaptability 
of LLMs become the core of ECPN task matching, 
enhancing the flexibility and efficiency in respond-
ing to environmental changes, and improving the 
performance of ECPN.
The global features extracted by the LLMs are 
processed by a Graph Attention Network (GAT) to 
further capture the spatial relationships between 
edge nodes. Then, these features are input to the 
MADRL, where a network of actors and critics is 
used to learn the optimal task matching strategy 
[15]. In this process, the actor network is responsi-
ble for selecting the task matching strategy, while 
the critic network measures the effectiveness of 
the strategy by evaluating the advantages and 
disadvantages. With continuous exploration and 
adaptation, each agent explores different task 
allocation strategies under the changing state of 
edge nodes and resources. In this way, the sys -
tem can dynamically adjust the matching strategy 
to respond to changing task requirements and 
resource constraints, and ensure optimal task 
matching and resource scheduling.
n u Mer Ic AL r esu Lts
In this section, we evaluate the performance of 
the proposed LLM-enabled energy and privacy 
tradeoffs task matching algorithm. We first per -
form global feature extraction through LLMs, 
which is responsible for extracting global environ-
ment information from the states of end devices 
and servers. These features provide key support 
for subsequent resource allocation and task 
matching. We consider simulating a real network 
scenario containing servers and L  end devices. 
The location of the end is set randomly within a 
radius of 1000 m, and the locations are random -
ized. At the same time, the end devices include 
the numbers 5, 10, 15, and 20, respectively.
FIGURE 3. Privacy budget-weighted energy consumption in different algorithms.
FIGURE 4. Comparison of the privacy budget weighted energy consumption for 
different algorithms at different numbers of devices.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
88
Fig. 3 shows the privacy budget weighted 
energy consumption of different algorithms 
including LLM-based graph MADRL, traditional 
MADRL and average offloading algorithms. 
From the figure, it can be seen that the tradi -
tional MADRL algorithm fails to converge and 
the energy consumption tends to increase. The 
reason is that the algorithm is unable to take into 
account the global features of the graph, which 
leads to slow convergence and even an increase 
in energy consumption. The weighted energy 
consumption of the average offloading algorithm 
fluctuates at the same height, and the energy 
consumption is higher than that of the proposed 
algorithm. In contrast, the proposed algorithm 
exhibits faster convergence and achieves the 
lowest energy consumption by effectively cap-
turing the spatial features of the graph, which 
enhances task matching performance in the 
ECPN and reduces privacy budget-weighted 
energy consumption.
Fig. 4 shows the privacy budget weighted 
energy consumption of the three different algo -
rithms after 100 iterations with different number 
of end devices. It can be seen that the proposed 
algorithm consistently exhibits the lowest energy 
consumption for all device configurations, which 
demonstrates its superior resource management 
in processing the multi-node situation. In con -
trast, the MADRL algorithm has not obtained an 
optimal task matching strategy in 100 iterations, 
with the highest energy consumption for all num -
ber of devices situations. The average offloading 
method instead performs better when the num-
ber of end devices becomes higher, but still not 
as good as the algorithm proposed in this paper. 
This result complements the previous conver -
gence performance analysis and further confirms 
the benefits of the proposed algorithm in reduc -
ing energy consumption and optimizing system 
performance.
Fig. 5 shows the trends in the impact of pri-
vacy budget on energy consumption under 
different numbers of end devices. From Fig. 5 , 
we can see that the privacy budget of the end 
devices is inversely proportional to the energy 
consumption. Energy consumption increases as 
the privacy budget of the end device decreases. 
The reason is that as the privacy budget 
decreases, the increase in noise introduced to 
protect data privacy leads to a decrease in the 
efficiency of computing resource allocation and 
an increase in computing complexity, which in 
turn significantly increases energy consumption. 
At the same time we can see that as the number 
of end devices increases, the energy consump-
tion increases accordingly. The reason is that 
more devices require additional computing and 
communication resources to coordinate and 
manage, which leads to a higher overall system 
energy consumption.
Fig. 6 shows the privacy budget of tasks with 
different number of end device. From the figure, 
it can be seen that the privacy budget for tasks 
is relatively stable and does not fluctuate signifi-
cantly with changes in the number of end devices. 
It shows that privacy protection strategies are 
based on the sensitivity of tasks, rather than being 
affected by the number of end devices. In addi-
tion, through this process, the system finds the 
most appropriate size of privacy budget, which 
can meet privacy protection requirements without 
increasing additional system overhead.
conc Lus Ion
In this paper, we proposed a large model-enabled 
ECPN framework to optimize resource utili -
zation and task processing efficiency in edge 
computing. The integration of large models 
enhanced the global feature extraction, adaptive 
adjustment, and multi-task parallel processing 
FIGURE 6. Privacy budget of tasks with different number of end device.
FIGURE 5. Energy consumption with privacy budget at different numbers of 
devices.
The primary problem is how to balance the accuracy of the model with the constrained resources of 
individual edge devices as the ECPN continues to expand.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply. 
IEEE Network • July/August 2025
89
capabilities, significantly improved the capability 
of the system to respond to heterogeneous tasks 
and dynamic environments. To overcome the 
resource constraints of edge nodes, we used 
model compression, distributed inference, and 
incremental learning techniques to optimize 
the deployment of large models in ECPN. Fur -
thermore, we propose integrating LLMs with a 
graph-based MADRL algorithm to develop a task 
matching policy that optimally balances energy 
consumption and privacy protection. Experimen-
tal results showed that the proposed framework 
and algorithm can reduce energy consumption, 
accelerate task matching convergence, and ensure 
privacy protection.
Although improvement has been made in 
resource allocation and large model deployment 
in large model-enabled ECPN, several problems 
remain unresolved. The primary problem is how 
to balance the accuracy of the model with the 
constrained resources of individual edge devices 
as the ECPN continues to expand. In the future, 
research should focus on improving the adaptabil -
ity of large models when network conditions and 
task requirements continue to change. In addition, 
the privacy protection mechanism of distributed 
systems should be further developed to protect 
user privacy while enhancing the protection of 
computing power information of computing 
nodes.
Acknow Ledg Ment
This work was supported in part by the National 
Natural Science Foundation of China under 
Grant 62071092, in part by the Science and 
Technology Project of Sichuan Province under 
Grant 2024YFHZ0321, and in part by the Open 
Research Fund from the Guangdong Laboratory 
of Artificial Intelligence and Digital Economy (SZ) 
under Grant GML-KF-22-10.

## § References

[1] S. Yukun et al., “Computing power network: A survey,” China 
Commun., vol. 21, no. 9, pp. 109–145, Sep. 2024.
[2] B. Lai et al., “Resource-efficient generative mobile edge 
networks in 6G era: Fundamentals, framework and case 
study,” IEEE Wireless Commun., vol. 31, no. 4, pp. 66–74, 
Aug. 2024.
[3] L. Yue and T. Chen, “AI large model and 6G network,” in 
Proc. IEEE Globecom Workshops (GC Wkshps), Dec. 2023, 
pp. 2049–2054.
[4] F. Jiang et al., “Large AI model-based semantic communica-
tions,” IEEE Wireless Commun. , vol. 31, no. 3, pp. 68–75, 
Jun. 2024.
[5] Z. Lin et al., “Pushing large language models to the 6G 
edge: Vision, challenges, and opportunities,” 2023, 
arXiv:2309.16739.
[6] B. Rong and H. Rutagemwa, “Leveraging large language 
models for intelligent control of 6G integrated TN-NTN with 
IoT service,” IEEE Netw., vol. 38, no. 4, pp. 136–142, Jul. 
2024.
[7] Y. Zhang et al., “Diversity-driven proactive caching for 
mobile networks,” IEEE Trans. Mobile Comput., vol. 23, no. 7, 
pp. 7878–7894, Jul. 2024.
[8] Y. Sun et al., “Empowering digital twins with large language 
models for global temporal feature learning,” J. Manuf. Syst., 
vol. 74, pp. 83–99, Jun. 2024.
[9] L. Wang et al., “A survey on large language model based 
autonomous agents,” Frontiers Comput. Sci. , vol. 18, no. 6, 
Mar. 2024, Art. no. 186345.
[10] S. Bhardwaj, P. Singh, and M. K. Pandit, “A survey on the 
integration and optimization of large language models in 
edge computing environments,” in Proc. 16th Int. Conf. 
Comput. Autom. Eng. (ICCAE), Mar. 2024, pp. 168–172.
[11] Y. Huang et al., “Large language models for network -
ing: Applications, enabling techniques, and challenges,” 
IEEE Netw., early access, Jul. 30, 2024, doi: 10.1109/
MNET.2024.3435752.
[12] Y. Lin et al., “Meta-networking: Beyond the Shannon limit 
with multi-faceted information,” IEEE Netw., vol. 37, no. 4, 
pp. 256–264, Jul. 2023.
[13] C. Dwork, “Differential privacy,” in Proc. Int. Colloq. Autom-
ata, Lang., Program., Jul. 2006, pp. 1–12.
[14] W. X. Zhao et al., “A survey of large language models,” 
2023, arXiv:2303.18223.
[15] R. Lowe et al., “Multi-agent actor-critic for mixed cooper -
ative-competitive environments,” in Proc. Adv. Neural Inf. 
Process. Syst., vol. 30, 2017, pp. 1–12.
BiogRaphies
Liyan  Sui (202311012319@std.uestc.edu.cn) received the M.S. 
degree from Heilongjiang University, China, in 2023. She is 
currently pursuing the Ph.D. degree with the School of Infor -
mation and Communication Engineering, University of Elec -
tronic Science and Technology of China. Her research interests 
include mobile edge computing, computing power networks, 
and graph neural networks.
Ke Zhang  (Member, IEEE) (zhangke@uestc.edu.cn) received 
the Ph.D. degree from the University of Electronic Science and 
Technology of China in 2017. He is currently an Associate Pro-
fessor with the School of Information and Communication Engi-
neering, University of Electronic Science and Technology of 
China. His research interests include scheduling of mobile edge 
computing, design and optimization of next-generation wireless 
networks, smart grid, and the Internet of Things.
Fan  Wu  (wufan@uestc.edu.cn) received the Ph.D. degree from 
the University of Electronic Science and Technology of China, 
China, in 2015. He is currently an Associate Professor with 
the School of Information and Communication Engineering, 
University of Electronic Science and Technology of China. His 
research interests include intelligent wireless networks, UAV 
networks, and optimization techniques in resource allocation 
of wireless networks.
Xiaoyan  h uang  (xyhuang@uestc.edu.cn) received the Ph.D. 
degree from the University of Electronic Science and Technol-
ogy of China, Chengdu, China, in 2012. She is currently an 
Associate Professor with the School of Information and Com-
munication Engineering, University of Electronic Science and 
Technology of China. Her research interests include edge intelli-
gence, wireless communications and networking, and the Inter -
net of Things.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:17:04 UTC from IEEE Xplore.  Restrictions apply.
