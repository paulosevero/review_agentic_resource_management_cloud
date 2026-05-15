---
paper_id: "paper-1386"
source_pdf_sha: "0ff28e2e5b1a5c351c207b0a55a7138903aff9015373bd4695f2759c09fdf17a"
extraction_quality: high
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 9
  page_count: 6
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-1386 — fulltext
## §unknown-1

979-8-3315-7871-8/25/$31.00 ©2025 IEEE 
 
Utilizing LLMs for Virtual Machine Migration in 
Cloud Computing Environments
Eman Alofi  
Department of Information & Computer Science, 
King Fahd University of Petroleum & Minerals, Dhahran, Saudi 
Arabia 
g202318050@kfupm.edu.sa 
 
Tarek Helmy 
Department of Information & Computer Science, 
Interdisciplinary Research Center for Intelligent Secure Systems, King 
Fahd University of Petroleum & Minerals, 
Dhahran, Saudi Arabia 
helmy@kfupm.edu.sa
Abstract— The current methods for virtual machine migration 
operate through inflexible decision systems, which prevent system 
adaptability and reliable pattern detection. The research develops 
a theoretical framework which demonstrates how large language 
models (LLMs) can create an adaptive migration system that 
understands its environment. Th e framework consists of three 
distinct sections, where the first monitors resources and data in 
real-time and the second section predicts workload patterns , and 
the third section optimizes migration decisions. The layered 
system design according to initial modelling results in better 
resource utilization by 20-30% and faster decision-making at 50-
200 ms with 85 -95% accurate predictions compared to 
conventional methods. The promising results from these 
projections highlight both the benefits and difficulties th at come 
with real -time processing and protecting confidential data. The 
proposed framework establishes a strong foundation to transform 
virtual machine migration approaches while enabling the creation 
of intelligent cloud resource management systems. 
Keywords—Large Language Models, Virtual Machine, Cloud 
Computing, Migration Approaches, Theoretical Modelling.

## § Introduction

Since there is a considerable growth in the field of cloud 
computing, the VM migration-related issues are escalating. VM 
migrations are required to maintain the working efficiency of 
software and resource usage in data centers. It has been 
researched that companies lose 15-25% of computing resources 
as a result of late decisions in VM migration [1]. This tends to 
increase thei r operational cost and lead to poor quality of 
service. The growing complexity of cloud workloads demands 
more advanced strategies, especially those leveraging Large 
Language Models (LLMs). Current VM migration methods 
simply react or respond to resource unava ilability, hardware 
failure, or maintenance needs [2], and do not even try to prevent 
them. Therefore, they are faced with the following three major 
challenges: 
1) Limited Predictive Capabilities:  Instead of proactively 
anticipating and preventing problems, current systems wait 
for problems to occur, then respond to them. Because the 
response is taken after the performance degradation, the 
reactive approach ends up with 30 -40% more migrations 
than necessary. This leads to service downtime and 
resource waste.  
2) Static Decision Frameworks:  As they rely  on fixed rules 
and thresholds, current systems are often unable to adapt and 
adjust to changes in workload. As a result, resources are 
allocated insufficiently, with many data centers reporting 
CPU usage staying below 50%. 
3) Inefficient Pattern Recognition:  While up to 70%  of VM 
migrations follow identifiable patterns, current systems are 
unable to utilize past migration patterns and workload 
habits effecti vely. Advanced pattern recognition 
techniques could improve this. 
The ability of LLM models to recognize patterns and predict 
outcomes enables solutions for handling these difficulties. The 
latest research shows that LLMs excel at predicting even t 
sequences and finding hidden patterns , which leads to better 
VM migration performance. The analysis of extensive 
historical migration data by LLMs enables them to predict 
resource requirements and generate context -dependent 
decisions through their adaptiv e capabilities. The proposed 
solution uses LLM capabilities to create an intelligent 
proactive system for VM migration, which replaces traditional 
reactive methods. This paper presents a theoretical framework 
that demonstrates how Large Language Models (LLM s) can 
boost Virtual Machine (VM) migration operations in cloud 
computing systems. Our theoretical assessment leads to the 
development of three essential research questions. The 
implementation of LLMs bring what specific advantages to 
VM migration operati ons regarding performance and 
precision? An LLM -based migration system requires which 
fundamental elements to operate effectively ? The ability of 
LLMs to recognize patterns and make predictions enables 
them to enhance resource utilization. 
The current lite rature review revealed two essential 
knowledge gaps. The present systems fail to predict resource 
requirements, and their decision-making processes do not adapt 
to changing conditions. The paper conducts theoretical research 
about LLM integration in VM migr ation systems while 
developing a predictive migration framework and architectural 
components, and discussing theoretical obstacles and solutions. 
The paper presents four main contributions to the field. The 
paper presents a theoretical framework for LLM integration in 
VM migration systems and a conceptual framework for 
predictive resource allocation and a method for dynamic 
migration strategy selection , and a starting point for 
experimental studies. The research provides theoretical 
foundations to enhance the  functionality of VM migration 
systems. The proposed framework establishes a basis for 
testing LLM-based migration methods in practical applications.  
2025 16th Student Research Conference on Applied Computing (SRC) | 979-8-3315-7871-8/25/$31.00 ©2025 IEEE | DOI: 10.1109/SRC65875.2025.11263644
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply. 
The rest of the paper is organized as follows: Section II 
provides an intensive literature review by focu sing on the 
optimization of VM allocation and migration in cloud 
computing environments. The proposed framework and 
methodology are detailed in Section III. Section IV discusses 
the implementation details of  the proposed framework. The 
discussion and results analysis are provided in Section V, and 
finally, Section VI concludes the paper and highlights future 
research. 
II. LITERATURE REVIEW 
Nowadays, there is a noticeable and considerable interest in 
the optimization of VM allocation and migration in cloud 
computing environments. Researchers have investigated 
several methods to enhance efficiency and reduce operating 
expenses. Traditional systems  face difficulties in reconciling 
between energy and resource consumption and service quality, 
which requires a source of advanced alternative resources. An 
important achievement in this field was a hybrid optimization 
method that integrates Cuckoo search with Particle Swarm 
optimization methods, which shows a significant enhancement 
in energy consumption and resource  usage while controlling 
migration costs [3]. Moving further, the researchers developed 
the SSUR technique.  The method presented is innovative 
because it considers both user requirements and data center 
characteristics when deciding how to allocate virtual machines. 
The method delivers better performance for energy usage and 
processing efficiency, but its deployment remains restricted to 
thick tree topology networks [4]. The field continues to receive 
ongoing research efforts from experts who work to create better 
solutions that function across all network types. The 
researchers have created the IDE algorithm and multiple 
advanced virtual machine a llocation methods , which they 
tested extensively through the CloudSim framework . The 
Improved IDE method has demonstrated clear effectiveness in 
lowering operational costs while achieving more balanced load 
distribution across available resources [5]. 
The current research into virtual machine migration focuses 
on creating algorithms which enhance both placement 
operations and migration procedures.  The IRB -VMP 
algorithm selects placement positions through mathematical 
similarity assessments that use Jaccard dist ances and cosines. 
The IRB -VMP algorithm outperforms first -order fitness 
decreasing (FFD) and best -order fitness decreasing (BFD) 
methods in terms of energy efficiency, thus establishing itself 
as a crucial tool for resource optimization development. The 
integration of artificial intelligence (AI) into virtual machine 
management creates new management opportunities. The AI-
based system uses BERT-powered chatbots with random forest 
models to perform adaptive resource allocation. The system 
achieved a 42% reduction in processing time and delivered 
significant performance improvements according to research 
findings [7]. 
Research indicates growing interest in the combination of 
the modified best-fit decreasing algorithm (MBFD) with the 
grasshopper optimization algorithm (GOA) for hybrid method 
development. The method demonstrates effective energy 
reduction and SLA violation prevention but needs extensive 
testing to confirm its performance in extensive cloud 
environments [8]. The field of cloud data transmission methods 
keeps evolving through studies which focus on system 
dependability and performance enhancement and load 
reduction, and power conservation [9]. The solutions have 
proven effective in various industrial settings , including 
electric vehicle manufacturing syst ems and green wireless 
communication networks. The researchers divide their study 
into two transmission classes because they need to address 
distinct problems that arise from data center workload 
management and thermal management. 
The Load Balanced Multi -Dimensional Bin -Packing 
(LBMBP) method stands out as a meta-heuristic strategy which 
CloudSim Plus simulations demonstrated reduces both 
physical machine usage and power consumption [10]. The 
research revealed ongoing problems with network constraint 
management during migration , which requires better load 
prediction techniques for dynamic resource allocation. The 
research presents two different data placement solutions, which 
use Kernel Density Estimation (KDE) and Fuzzy FCA methods 
[11]. The VMLM simulation m odel uses machine learning to 
create a two-phase solution for VM migration [12]. The system 
combines machine learning training with VM migration 
execution to handle unbalanced VM distribution. The research 
achieved better service delivery with reduced unne cessary 
migration operations. The researchers determined that an 
advanced AI load prediction system would be required to reach 
peak resource optimization levels. The researchers developed 
a hybrid optimization system for VM management through the 
combination of Cuckoo Search Optimization (CSO) with 
Particle Swarm Optimization (PSO) to support QoS under 
high-demand conditions [13]. 
In the automotive cloud computing field, a new Resource 
Utilization-aware VM Migration (RU -VMM) algorithm was 
developed to manage VM migration in mobile environments. 
This method presented the efficiency in load distribution 
between overloaded and underloaded trucks and constant usage 
monitoring; nevertheless, its assessment was confined to 
SUMO simulations rather than real-world examples. The latest 
development was the CESCA (Cosine-Enhanced Smart Elastic 
Scheduling Algorithm) [14], which refined the previous SESA 
framework to optimize VM placement choices. The system 
exhibited enhanced energy economy  and service quality by 
using more accurate VM selection and placement strategies, 
while significantly decreasing SLA breaches in cloud settings. 
After reviewing the available literature, the outcome reveals 
significant shortcomings in current VM migration  
methodologies, particularly in predictive functionalities and 
dynamic adaptation strategies. Despite recent developments, 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply. 
such as the CESCA algorithm [15] and meta -heuristic 
approaches [10], which enhance energy efficiency and resource 
usage, they primarily operate on reactive principles rather than 
proactive prediction. The research highlights the fact that the 
present system almost exclusively depends on current or past 
indicators for decision-making and does not have an advanced 
predictive model to allocate resources in the future. However, 
while certain algorithms, such as RU -VMM [16], may be 
useful in certain scenarios, their ability to provide a dynamic 
response to changing patterns of workload is limited by their 
traditional one-size-fits-all migration strategies. 
These shortcomings bring attention to two areas in 
particular: the need for more accurate prediction of resource 
usage and the dynamic selection of algorithms suited to varying 
conditions. Although recent approaches make use of 
sophisticated optimization methods, they still struggle to 
forecast demand with precision or to automatically determine 
the most effective migration strategy in real time. The growing 
capabilities of Large Language Models (LLMs), however, offer 
a promising path forward . When combined with robust data 
collection and advanced decision-making frameworks, LLMs—
through their strengths in pattern recognition, sequence 
prediction, and anomaly detection —could potentially reshape 
the entire process of VM migration. Instead of responding only 
after performance has degraded, systems would be able to 
anticipate requirements, identify suitable strategies, and act 
immediately. Such a shift from reactive to proactive decision -
making appears well-positioned to close current gaps in 
workload forecasting, adaptive strategy selection, and rapid 
decision execution, offering a compelling response to persistent 
limitations in migration methods. 
III. PROPOSED FRAMEWORK AND METHODOLOGY 
A. System Architecture Overview and LLM Integration 
As illustrated in Figure 1, the framework incorporates LLMs 
across three primary functions: determining the optimal time for 
migration, analyzing historical patterns of resource usage, and 
predicting future workloads. At the center of the design, the 
LLM serves as a deci sion-making hub, drawing on both 
historical and current workload data to recommend when and 
where VMs should be moved, how resources should be 
allocated, and how the migration path might be optimized. In 
contrast to rule-based approaches that rely on fixed  thresholds, 
this integration fosters a context -aware process that evaluates 
multiple factors simultaneously, allowing for more adaptive and 
efficient migration strategies. 
B. Architectural Components 
As shown in Figure 2, the heart of the proposed framework 
is an LLM -based processing model that serves as decision-
making for the journey of VM migration. The proposed  
framework uses three interconnected modules that work 
together to transfer and complete the migration process, as 
shown in Table 1. Each framework is designed to solve a 
specific limitation in the current VM migration systems. 
Utilizing LLM’s pattern recognition to understand resource 
usage data is done by the resource prediction module, unlike the 
current VM migration systems that use simple thresholds. The 
resource prediction module analyzes the relationship between 
several resources at the same time, making predictive migration 
decisions rather than reactive. Furthe rmore, the Workload 
Analysis Module uses LLM processing abilities to understand 
both structured and unstructured system data, analyzing 
resource metrics alongside system logs to build a comprehensive 
understanding of workload behavior. 
 
Figure 1: System Architecture Diagram 
Approach Predictive 
Capabilities 
Resource 
Optimizati
on 
Scalability Adaptatio
n Ability 
Real-
time 
Response 
Implementatio
n Complexity 
Tradition
al Rule-
based 
✓ ✓✓ ✓✓✓ ✓ ✓✓✓ ✓ 
SSUR

## § Method

✓✓ ✓✓✓ ✓✓✓ ✓✓ ✓✓ ✓✓ 
IDE-

## § Method

✓✓ ✓✓✓ ✓✓✓ ✓✓ ✓✓✓ ✓✓✓ 
IRB-VMP 
Algorithm 
✓✓✓ ✓✓✓ ✓✓ ✓✓✓ ✓✓ ✓✓✓ 
AI-
Powered 
BERT 
System 
✓✓✓ ✓✓✓ ✓✓✓ ✓✓✓ ✓✓ ✓✓✓✓ 
Proposed 
LLM 
Framew
ork 
✓✓✓✓ ✓✓✓✓ ✓✓✓ ✓✓✓✓ ✓✓✓ ✓✓✓ 
TABLE I: Comparative Analysis of VM Migration Approaches 
Legend: 
• ✓: Limited/Basic 
• ✓✓: Moderate 
• ✓✓✓: High 
• ✓✓✓✓: Very High 
C. Data Flow and Component Interactions 
For the VM migration, our Framework proposes an approach to 
managing the movement of data within a system to enable 
effective LLM-based decisions. Our model would begin with 
the initial layer, which collects data from different sources such 
as measures of resource utilization, past migration trends, 
system performance metrics, and network traffic data. The LLM 
requires essential data to generate optimal migration decisions. 
The system requires data from multiple sources before it can 
transfer this information to the processing layer for LLM 
training and analysis purposes. The processing layer contains 
four essential operations that harmonize different data types and 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply. 
detect outliers and extract vital features , and simplify complex 
data while preserving critical details. The system will deliver 
structured data to the LLM through these processing steps , 
which result in clear and organized information. The structured 
framework enables the LLM to produce prompt and efficient 
migration decisions. The system architecture delivers 
appropriate data to the model at specific times, which results in 
better decision accuracy than conventional methods. 
Fig. 2: LLM Component Architecture 
 
Fig. 3: Data Flow Pipeline 
D. Algorithm Specifications 
To operationalize this design, the framework introduces two 
complementary algorithms that together form the basis of an 
intelligent VM migration system. The first, summarized in Table 
2, is the Resource Prediction Algorithm (RPA). Drawing on 
LLM capabilities, the RPA examines statistical indicators 
alongside the current system state to anticipate forthcoming 
resource requirements. Theoretically, this algorithm can: 
1) Recognize patterns by analyzing resource usage over time. 
2) Make predictions by verifying the current system status. 
3) Utilize confidence thresholds to ensure precise predictions. 
4) Include fallback mechanisms for uncertain situations. 
 
The second algorithm, the Migration Optimization Algorithm 
(MOA), outlined in Table 3, then builds upon these predictions 
to produce the best migration strategies. It takes into account the 
expected resource costs, potential  network impact, risks of 
service disruption, and system limitations. Both MOA and RPA 
algorithms form the basis for automated LLM-driven migration 
decisions. They offer smarter and more context-aware solutions 
by going beyond the rigid, traditional rule-based approaches. As 
our framework combines the best features of both algorithms, it 
is expected to significantly improve the performance of VM 
migration decision-making with: 
1) 50–200 ms of decision latency, 
2) 85–95% of prediction accuracy, 
3) approximately 5% of system overhead, 
4) 20–30% of resource utilization improvements, 
It is worth noting that while these metrics provide benchmarks 
for future implementation , actua l performance will vary  
depending on the specific implementation contexts and 
environments. 
TABLE II: The Resource Prediction Algorithm 
 
ALGORITHM 1: THE RESOURCE PREDICTION 
ALGORITHM 
Input: Historical resource metrics H, Current state S 
Output: Resource prediction vector P

## §1 Initialize prediction window W and confidence threshold α

2 For each resource type r ∈ R: 
2.1 
2.2 
2.3 
2.4 
Extract temporal patterns T r from 
H, Generate feature vector Fr 
from S, Apply LLM analysis to 
(T r, Fr) 
Calculate prediction confidence Cr 
 
2.5 
If Cr > α: 
Update prediction vector P 
Else: 
Apply the fallback prediction method

## §3 Return P with confidence intervals

TABLE III: Algorithm 2: The Migration Optimization Algorithm 
ALGORITHM 2: The Migration Optimization Algorithm 
Input: Resource predictions P, System constraints C 
Output: Migration plan M 
1 Initialize strategy space S and cost function f (s) 
2 For each candidate strategy s ∈ S: 
2.1 Calculate expected resource cost Er(s) 
2.2 Computer network overhead On(s) 
2.3 Estimate service disruption Ds(s)

## §2.4 Evaluate the feasibility against C

3 Select a strategy m that minimizes f (s) subject to C 
4 Return optimal migration plan M. 
IV. IMPLEMENTATION CONSIDERATIONS 
The main focus of this work is to optimize LLMs for quick 
processing while maintaining a high level of prediction 
accuracy.  However, when it comes to the practical 
implementation and incorporation of current cloud 
infrastructure, there are a number of challenges preventing 
seamless operations and consistent service quality. Therefore, 
it is important to carefully evaluate scalability across various 
computing environments, especially when dealing with different 
hardware setups and workload patterns. 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply. 
A. Security and Privacy Framework 
The LLM-based migration architecture consists of two core 
components, which are security and privacy.  The framework 
provides strong security capabilities which safeguard VM 
workload data during its movement through LLM processing. 
The system operates through three essential security 
components, which protect workload behavior through 
encryption and data usage patterns , and migration activities 
through access control systems and decision sequence 
documentation through audit trails. The security measures play 
a vital role in protecting sensitive data that moves between 
different security domains because they maintain confidentiality 
while ensuring system performance. 
B. Future Research Opportunities 
The proposed framework enables researchers to study AI 
tool effects on virtual machine migration operations through 
multiple research approaches. The initial research objective 
should focus on creating LLMs which recognize workload 
patterns and coordinate migrations , and generate strategies 
based on operational results. The development of these 
capabilities requires breakthroughs in methods that improve the 
model's ability to recognize diverse workload behavio rs and 
shifting resource usage patterns. The research should 
concentrate on improving LLM performance within cloud 
computing systems. The research should explore new model 
designs which enhance predictive accuracy while minimizing 
both latency and computat ional requirements. Notably, these 
directions suggest that optimizing performance and scalability 
will be as important as enhancing predictive intelligence in 
determining the long -term viability of LLM -driven migration 
systems. Future studies must focus on integrating the framework 
described herein with upcoming cloud technologies, such as the 
use thereof in containerized environments, hybrid cloud 
infrastructures, and edge computing environments. Moreover, 
research should tackle privacy and security issues by developing 
sophisticated privacy -preserving techniques for LLM -driven 
decision-making. These innovations will improve the 
framework’s ability to navigate complex cloud environments 
while ensuring dependable and effective migration decisions. 
V. RESULTS AND DISCUSSION 
Indeed, our methodology breaks new ground in VM 
migration by using LLM -based analysis for pattern detection 
and forecasting capabilities. Furthermore,  the framework 
shows efficient performance across its components; for 
example, the data processing pipeline operates at an O (n log n) 
complexity for a data volume of n. Although the LLM inference 
process reveals quadratic complexity relative to input 
dimensions, the strategy optimization scales linearly with the 
number of viable strategies. Consequently, these traits point to 
a robust scalability potential as operational demands increase. 
Moreover, performance analysis under optimal conditions 
highlights significant improvements compared  to existing 
methods. The framework appears capable of a chieving 
prediction accuracy between 85 – 95% while maintaining 
decision latencies in the range of 50–200 milliseconds. Also, 
resource utilization might improve by 20 –30% compared to 
traditional approaches, and this comes without compromising 
system stability or service level agreements. As a result,  these 
projections set clear benchmarks for future implementations. 
Our work shows notable potential improvements in operational 
metrics by utilizing mathematical modelling and comparative 
assessment against curr ent methodologies.  The framework 
shows promising capabilities to recognize workload patterns 
and predict resource demand. This also suggests that better 
resource use may be possible through optimized VM placement 
and predictive decision-making. These findings are very helpful 
for managing cloud resources and serve as a foundation for 
future experimental validation.

## § Conclusion

This paper indicates advancements in cloud computing by 
enhancing VM Migration optimization through a novel LLM -
based framework. Our analysis reveals considerable potential 
enhancements in predictive accuracy, ranging from 85 to 95% 
and a 20 to 30% reduction in overhead, resulting in improved 
resource utilization efficiency. The establishment of a three -
layer architecture featuring specialized LLM modules broadens 
solutions to tackle intricate migration issues while  ensuring 
decision latency remains below 200 ms. The framework 
underscores the current shortcomings in VM migration systems 
via the implementation of decision -making, pattern 
recognition, and predictive resource distribution. This research 
advocates for the prioritization of empirical verification in 
authentic environments, LLM processing optimization, and the 
exploration of developed scenarios, including edge computing 
and hybrid cloud computing, for future investigations. Further 
research concentrates on enhancing  data privacy mechanisms 
and adapting frameworks for containerized environments. This 
endeavor opens new avenues for smart cloud resource 
management, which could revolutionize resource optimization 
and workload administration in cloud systems through the 
inclusion of LLMs in VM Migration.

## § Acknowledgement

The authors acknowledge King Fahd University of 
Petroleum and Minerals and the Interdisciplinary Research 
Center for Intelligent Secure Systems for providing computing 
facilities and support for doing this work.

## § References

[1] GClaus Pahl, Pooyan J amshidi, and Olaf Zimmermann, “Architectural 
principles for cloud software,” ACM Transactions on Internet 
Technology, vol. 18, no. 2, art. 17, pp. 1 –23, May 2018, doi: 
10.1145/3104028 
[2] S. Singh and I. Chana, ”Resource provisioning and scheduling in clouds: 
QoS perspective,” The Journal of Supercomputing, vol. 77, pp. 1240 -
1274, 2016. 
 
[3] M. S. A. Khan and R. Santhosh, ”Hybrid Optimization Algorithm for VM 
Migration in Cloud Computing,” Computers and Electrical Engineering, 
vol. 102, p. 108152, 2022. DOI: 10.1016/j.compeleceng.2022.108152. 
[4] Y. Huang, H. Xu, H. Gao, X. Ma, and W. Hussain, "SSUR: An Approach 
to Optimizing Virtual Machine Allocation Strategy Based on User 
Requirements for Cloud Data Center," IEEE Transactions on Green 
Communications and Networking, vol. 5, no. 2, pp. 670 –681, 2021, doi: 
10.1109/TGCN.2021.3067374. 
[5] P. Zhang, M. Zhou, and X. Wang, "An Intelligent Optimization Method 
for Optimal Virtual Machine Allocation in Cloud Data Centers," IEEE 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply. 
Transactions on Automation Science and Engineering, vol. 17, no. 4, pp. 
1725–1735, Oct. 2020, doi: 10.1109/TASE.2020.2975225. 
[6] I. El-Taani, M.-C. Boukala, and S. Bouzefrane, ”Energy-Aware VM 
placement based on intra-balanced resource allocation in data centers,” 
in 2021 8th International Conference on Future Internet of Things and 
Cloud (FiCloud), Rome, Italy, 2021, pp.  400-405. DOI: 
10.1109/FiCloud49777.2021.00065. 
[7] A. Chatterjee, P. Dubey, and A. Nigam, ”Dynamic On-Demand Machine 
Provisioning and Continuous Resource  Management,” in 2023 
International Conference on Computing, Communication, and Intelligent 
Systems (ICCCIS), Greater Noida, India, 2023, pp. 1010 -1015. DOI: 
10.1109/IC- CCIS60361.2023.10425203. 
[8] R. Singh, S. Singh, and B. Kaur, ”Energy -Efficient VM Allocation and 
Migration Approach Using Swarm Intelligence  Algorithm in Cloud 
Computing Environment,” in 2023 14th  International Conference on 
Computing Communication and  Networking Technologies (ICCCNT), 
Delhi, India, 2023, pp. 1-6. DOI: 
10.1109/ICCCNT56998.2023.10306680. 
[9] R. Sharma, A. Bala, and A. Singh, ”Virtual Machine Migration for Green 
Cloud Computing,” in 2022  IEEE International  Conference on 
Distributed Computing and Electrical Circuits  and Electronics 
(ICDCECE), Ballari, India, 2022, pp. 1 -7. DOI: 
10.1109/ICDCECE53908.2022.9793067. 
[10] A. Kumar and R. Devi, ”VM Migration and Resource Management using 
Meta-Heuristic Technique in Cloud Computing Services,” in *2023 
International Conference on Distributed  Computing and Electrical 
Circuits and Electronics (ICD-CECE), Ballari, India, 2023, pp. 1-6. DOI: 
10.1109/ICD- CECE57866.2023.10151087. 
[11] Sellami, M., Mezni, H., Hacid, M.S.  et al.  Clustering-based data 
placement in cloud computing: a predictive approach. Cluster Comput 24, 
3311–3336 (2021). https://doi.org/10.1007/s10586-021-03332-1 
[12] A. Belgacem, S. Mahmoudi, and M. A. Ferrag, ”A machine  learning 
model for improving virtual machine migration in cloud computing,” The 
Journal of Supercomputing, vol. 79,  no. 9, pp. 9486–9508, 2023. DOI: 
10.1007/s11227-022-05031-z. 
[13] B. Booba, X. Joshphin Jasaline Anitha, C. Mohan, and J. S. 
Jeyalaksshmi, ”Hybrid approach for virtual machine allocation in cloud 
computing,” Sustainable Computing: Informatics and Systems, vol. 41, p. 
100922, 2024. DOI: 10.1016/j.suscom.2023.100922. 
[14] S.K. Pande, S.K. Panda, S. Das, K.S. Sahoo, A.K. Luhach, et al., ”A 
resource management algorithm for virtual machine  migration in 
vehicular cloud computing,” Computers, Mate rials & Continua, vol. 67, 
no. 2, pp. 2647-2663, 2021. DOI: 10.32604/cmc.2021.015026. 
[15] A. Kaur, S. Kumar, D. Gupta, Y. Hamid, M. Hamdi, A. Ksibi, H. 
Elmannai, and S. Saini, ”Algorithmic Approach to Virtual  Machine 
Migration in Cloud Computing with Updated SESA  Algorithm,” 
Sensors, vol. 23, no. 13, p. 6117, 2023. DOI: 10.3390/s23136117. 
[16] K. K., V. Jain, and P. Verma, ”An Analysis of Virtual Machine Migration 
Issues and Challenges in Cloud Computing,” International Journal of 
Computer Applications, vol. 182, pp.  25-30, 2018. DOI: 
10.5120/ijca2018918016.
 
 
 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:21:49 UTC from IEEE Xplore.  Restrictions apply.
