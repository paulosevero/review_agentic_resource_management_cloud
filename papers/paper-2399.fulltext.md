---
paper_id: "paper-2399"
source_pdf_sha: "906086ecda0dc66fa829f43fe6785ee7cce41a79a703fa0adcebe62d343193a2"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 3
  page_count: 6
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2399 — fulltext
## §unknown-1

A Human-in-Multi-Agent-Loop Intent Refinement 
Method for Task Offloading in Mobile Edge 
Computing 
 
1st Shao Yuan 
Jiangsu University of Technology 
Changzhou, China 
ZGC Institute of Ubiquitous-X Innovation and 
Applications 
Beijing, China 
2023655164@smail.jsut.edu.cn 
 
 2nd Weichen Ni 
China Mobile Research Institute 
China Mobile Communications Group Co.,Ltd 
Beijing, China 
niweichen@chinamobile.com 
 
3rd Boxiao Han 
ZGC Institute of Ubiquitous-X Innovation and 
Applications 
Beijing, China 
hanboxiao@zgc-xnet.com 
 
5th Yang Yu* 
Jiangsu University of Technology 
Changzhou, China 
dxyy@jsut.edu.cn 
4th Zuojun Dai 
ZGC Institute of Ubiquitous-X Innovation and 
Applications 
Beijing, China 
george.dai@bupt.edu.cn 
 
 
 
 
 
 
Abstract—In mobile edge computing (MEC), intent 
recognition plays a pivotal role in task offloading. To address 
this challenge, this paper proposes a Human-in-Multi-Agent-
Loop (HI MAL) intent refinement method for  MEC that 
synergistically integrates multi -agent collaboration with 
human judgment to enhance resource allocation and task 
scheduling efficiency, thereby facilitating the advancement of 
the Industrial Internet of Things (IIoT) . The proposed 
HIMAL system enhances AI decision -making through 
continuous integration of human feedback into the AI’s 
learning process, thereby enhancing both the precision of AI 
outputs and contextual awareness.  Experimental results 
demonstrate that our approach achieves significant 
performance improvements by embedding human guidance 
within large language model (LLM) workflows, where human 
operators serve as contextual interpreters to refine AI 
responses. 
Keywords-MEC;HIMAL;Task Offloading;QoSE;LLM

## § Introduction

5G and the upcoming 6G technologies [1] are crucial for 
the IIoT [2], as they provide high -speed data transmission, 
ultra-low latency, and massive connectivity. MEC  [3] 
further enhances IIoT systems by enabling distributed 
computation at the network edge, thereby reducing latency 
and bandwidth consumption while improving real -time 
decision-making. As cloud -based wireless networks 
become a major trend in 6G, the network edge will integrate 
more capabilities with MEC, such as communications, 
sensing, and computation. By processing data closer to the 
source, MEC supports critical applications such as 
autonomous control, predictive maintenance, and low -
latency industrial automation. In this context, Quality of 
Service and Experience (QoSE) is essential for ensuring 
reliable device interconnectivity, while intent recognition 
helps dynamically adjust resource allocation to meet real -
time demands, thereby enhancing both system performance 
and user satisfaction. 
In recent years, the rapid development of the IIoT has 
led scholars to focus on assessing and optimizing QoSE. 
Gajjar et al. [4] proposed a framework linking service 
quality and user experience, while Zhao et al. [5] surveyed 
the Q uality of Experience (QoE) in IIoT but lacked 
quantitative measurement standards, resulting in subjective 
assessments that overlooked the multidimensional nature of 
user intent.  Minovski et al. [6] suggested a four -layer 
framework for  objective user experience assessment . 
However, their framework fails to address both the 
functional differences among IoT devices and the varying 
impacts of network conditions, which may significantly 
affect QoSE. 
Meanwhile, LLMs are increasingly being applied in 
communication systems. Shao et al. [7] proposed a 
framework called WirelessLLM, which was specifically 
designed to adapt and enhance LLMs for addressing the 
unique challenges and requirements of wireless 
communication networks. Kalita et al. [8] developed a 
framework and its corresponding modules where LLMs can 
be effectively utilized under the protection of semantic 
communication at the network edge to achieve efficient 
communication in IoT networks. Howeve r, their approach 
failed to effectively integrate natural language processing 
with communication scheduling. Jiang et al. [9] proposed a 
multi-agent system equipped with domain -specific 
communication knowledge and tools to handle 
communication-related task s using natural language 
processing. Nevertheless, due to LLMs' limited capability 
in understanding dynamic changes in devices and 
environments, their comprehension of the physical world 
remains inadequate. Consequently, such multi-agent system 
may suffer from degraded communication efficiency or 
information loss when facing sudden network traffic surges. 
2025 IEEE 2nd International Conference on Electronics, Communications and Intelligent Science (ECIS) | 979-8-3315-1358-0/25/$31.00 ©2025 IEEE | DOI: 10.1109/ECIS65594.2025.11086847
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply. 
Therefore, this paper proposes a HIMAL intent 
refinement method based on the HITL [10] framework  to 
overcome the challenges of task offloading in MEC. The 
main contributions of this paper are summarized as follows: 
• We propose a HIMAL intent refinement method 
based on the HITL framework, accompanied by a 
HIMAL system architecture specifically designed 
for edge -cloud deployment. By synergistically  
integrating HITL with multi -agent collaboration, 
our method effectively maps human intent into 
utility functions, thereby optimizing scheduling 
decisions with improved accuracy. 
• Within the HI MAL system architecture, we 
introduce an agent model consisting of five core 
components: a centered agent, memory, action, 
perception, and brain. This edge-optimized design 
enables agents to efficiently process data locally 
while maintaining effective coordination with 
centralized cloud resources. 
• We design a novel  prompt method in the HI MAL 
system architecture to align task scheduling with 
user intentions. This approach significantly 
enhances deployment adaptability in edge -cloud 
environments, particularly in dynamic scenarios 
where real-time data and evolving user preferences 
critically influence scheduling performance. 
The remainder of this paper is organized as follows. 
Section II presents the system model of the MEC and the 
HIMAL system architecture. Section III details the 
experimental methodology and presents a thorough analysis 
of the results. Finally, Section IV concludes the paper and 
discusses future research directions. 
II. SYSTEM STRUCTURE 
A. System Model of the MEC 
The system model of the MEC comprises three distinct 
layers: the User Device Layer, the Edge Server Layer, and 
the Cloud Data Center Layer. The User Device Layer forms 
the foundation of the system, incorporating various end-user 
equipment such as IoT sensors and wearable devices. These 
devices generate service requests and offload computation-
intensive tasks to proximal edge servers. 
The Edge Server Layer serves as the intermediate tier, 
composed of computing nodes deployed at base stations, 
access points, and network edge locations. These servers 
provide localized processing capabilities for latency-critical 
tasks, substantially reducing dependence on remote cloud 
infrastructure. For computationally demanding worklo ads, 
edge servers maintain seamless interoperability with upper-
layer cloud resources. 
The Cloud Data Center Layer constitutes the uppermost 
tier of the system, delivering high -performance, elastic 
computing and storage resources. This layer specializes in 
executing resource -intensive operations, including large -
scale machine learning traini ng, comprehensive big data 
analytics, and persistent data archiving. 
B. System Architecture 
1) System Architecture 
This paper proposes a HIMAL intent refinement method 
to address the discrepancies between task scheduling 
execution and user intent in the MEC. Existing large 
language models (LLMs) struggle to comprehend the 
physical world due to their lack of real -world perception, 
which hinders their ability to accurately understand user 
intent in complex scenarios and leads to suboptimal 
decision-making. The HIMAL intent refinement method 
mitigates these challenges by incorporating human 
participation throughout the AI training process, enabling 
continuous feedback that enhances model's understanding 
of user intent and improves decision accuracy.  Building 
upon the HIMAL intent refinement method, we further  
propose the HI MAL system architecture, as illustrated in 
Figure. 1. In this architecture, the  LLM generates task 
offloading strategies by analyzing user intentions, 
environmental constraints  and resource availability in 
MEC. Humans provide iterative feedback to the LLM, 
enabling it to refine its understanding of user-specific delay 
and energy consumption requirements. Additionally, the 
architecture incorporates  a multi -agent collaboration 
method, a HIMAL workflow and a prompt method. 
Brain
1. Define QoSE goals
2. Analyze evaluation results
3. Adjust goals based on the 
results and user feedback
Action
Execute tasks with utilizing 
simulation tools, querying 
tools and others
Memory
Consist of long-term 
memory, medium-term 
memory and short-term 
memory
Perception
Involve system model 
design and prompt 
methods
Customer
Analyst
Dispatcher
Maintenance 
Engineer
Workflow
Supervision
Feedback
 
Figure. 1. HIMAL System Architecture 
2) Multi-Agent Collaboration Method 
In the HI MAL System Architecture, we propose an 
agent model centered around the agent and comprising 
four additional components: memory, action, perception, 
and brain. The specific descriptions of each component 
are as follows: 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply. 
• Agent: The agent serves as a proxy for the LLM, 
interacting with users. 
• Brain: The brain acts as the agent’s core, 
encompassing various LLMs. It is responsible for 
defining QoSE goals, analyzing evaluation 
results, and adjusting those goals based on th e 
results and user feedback. 
• Memory: The memory module consists of long -
term memory, medium-term memory, and short-
term memory.  Long-term memory is accessed 
through Retrieval-Augmented Generation (RAG) 
[11], medium-term memory is retrieved through 
word slots, and  short-term memory is directly 
obtained from historical records. 
• Action: The action module executes tasks, 
utilizing various tools such as simulation tools, 
querying tools, and others. 
• Perception: The perception module serves as the 
agent's sensory component, involving system 
model design and prompt methods. 
Additionally, we propose a method for multi -agent 
collaboration. We define four agents —the maintenance 
engineer, the dispatcher, the analyst, and the customer. 
The maintenance engineer collects and summarizes 
information about system users and network conditions. 
The dispatcher utilizes this data for initial scheduling and 
makes subsequent adjustments based on updates from the 
maintenance engineer, analysis from the analyst, 
customer requests, and previous scheduling results.  The 
analyst is responsible for analyzing the scheduling results 
provided by the dispatcher and, in conjunction with 
technical solutions, evaluating the guarantees for various 
users, businesses, and metrics. The customer reviews the 
analysis, considers contextual information, and provides 
adjustment suggestions when necessary. 
3) HIMAL Workflow 
We have studied and proposed the fundamental 
workflow of HI MAL, as presented below. The HI MAL 
workflow demonstrates the interaction between the user 
and the  multi-agent system, continuing until the user’ s 
requirements are fully satisfied. 
HIMAL Workflow 
Step: 
1. The user inputs task-related descriptions, including 
the type, arrival rate, priority, and performance metrics 
(e.g., delay, e nergy consumption), as well as a 
description of the target formula. 
2. The multi-agent system uses RAG to query the 
knowledge base, retrieves the interaction history, 
constructs prompts, and queries the LLM. 
3. The LLM generates the query results. 
4. The multi-agent system extracts result information 
and generates an optimization objective function. 
5. The multi-agent system analyzes the results and calls 
the most suitable optimization simulation tool to 
conduct the simulation, extracts the simulation results 
and forms new prompts to request  that the LLM 
analyzes the results. 
6. The LLM analyzes the results. 
7. The multi-agent system compiles the interaction 
process for this round, incorporates historical data, and 
provides feedback to the user. 
8. The user reviews and adjusts the results. 
9. Steps 2-8 are repeated until the user is satisfied with 
the results. 
4) Prompt Method 
Prompt engineering enhances the response quality of 
LLMs through optimized prompts. Notable methods 
include the Chain of Thought (CoT) proposed by Wei et 
al. [12], which decomposes tasks into sub -problems for 
sequential processing. Wang et al. [13] improved this 
approach with a self-consistent method, while Yao et al. 
[14] introduced the Tree of Thought (ToT) framework 
leveraging heuristic searches. This paper proposes a novel 
prompt method —SRR-CoT, which advances CoT 
through three key enhancements: 
• Added structured reasoning requirements : 
Complex tasks may lead to erratic or 
disorganized reasoning in LLMs, compromising 
output accuracy. To mitigate this issue, we 
explicitly require the model to follow a structured 
three-step reasoning process ( understand, 
analyze and output) within the prompt. This 
ensures logical clarity in the reasoning process 
and improves the reliability of the results. 
• Added role information of interaction objects: In 
multi-role scenarios, LLMs must distinguish the 
tasks and intentions of different roles. Thus, we 
enhance prompts by incorporating role -specific 
information (e.g., interaction objects, modes, and 
formats) to mitigate response bias caused by role 
ambiguity. 
• Added the current round of interaction: In multi-
round interactions, LLMs may encounter 
repetitive input -output pairs, risking 
comprehension deviations. To address this, we 
embed the current interaction round number in 
the prompt, enabling the model to maintain  
temporal awareness and reduce redundancy -
induced errors. 
III. SCHEDULING DECISION EXPERIMENT BASED ON 
PROMPT 
A. Simulation Setup 
This paper established a simulation environment with 
wireless battery management systems (WBMS) [15] and 
classified WBMS terminals into four types based on QoE: 
n=1 (normal, sufficient energy), n=2 (critical, sufficient 
energy), n=3 (normal, insufficient energy), and n=4 
(critical, insufficient energy).  Additionally, the task 
offloading of the WBMS is based on QoE.  The overall 
utility function of the WBMS is shown in Formula (1): 
𝑈(𝜏, 𝜀) = 𝑒∑ 𝜔𝑛,1𝑛𝑞𝑛{2,4} [ ∑ (𝜔𝑛,1𝑛 + 𝜔𝑛,2𝜀𝑛)
𝑛{1,2,3,4}
]
1−𝑞
(1) 
where 𝜏  denotes the delay, 𝜀  represents the energy 
consumption, 𝜔𝑛,1 and 𝜔𝑛,2 are the weight  of delay and 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply. 
energy consumption respectively, and q is a parameter 
bounded within the interval (0, 1). 
B. Prompt Experiment 
First, we designed corresponding prompts for four 
agents using SRR-CoT. Take the dispatcher as an 
example, its prompt template is presented  below. 
You are a dispatcher responsible for conducting the 
first round of scheduling based on the following 
summary information from the maintenance engineer. 
You need to output the simulation results and perform 
the following steps: 
1. Understand the current status of users, networks, 
etc., in the wireless battery management system. 
2. Analyze how to set the initial parameters for the 
wireless battery management system based on the 
understood status of users, networks, and resources. 
3. Output the simulation results obtained from the 
simulation conducted using the initial parameters. 
Interaction Object: Maintenance engineer  
Interaction Mode: Output 
Interaction Format: { 
Input: Summary information from the operations 
engineer 
Output: Scheduling results from this round of the 
scheduler } 
Current Round of Interaction: Round 1 
Furthermore, we conducted comparative experiments 
evaluating the SRR -CoT against the standard CoT. The 
experimental setup and the results generated by each 
prompting method are illustrated in Figure. 2. 
# Results of SRR-CoT
Question：How can the dispatcher improve the operating efficiency of the system by 
scheduling based on the summary information of the maintenance engineer?
First, you need to understand the detailed status information of each battery type. Second, you 
should analyze which battery status is most likely to affect the optimization of the system 
utility function U, and design scheduling strategies. Finally, you will implement these strategies 
to make necessary adjustments.
Input: Battery type and current status information.  
Output: Summary of specific scheduling strategies formulated for batteries:
For batteries(n=2), adjust the monitoring frequency. 
For batteries(n=3), optimize energy distribution, provide charging opportunities as soon as 
possible. 
For batteries(n=4), implement emergency response measures.
For batteries(n=1), continue to monitor.
# Results of CoT
Understanding phase: understand the current status of various battery types. 
Analysis phase: Analyze the impact of the status of each type of battery on the  system utility function U. 
Strategy formulation phase: analysis results and formulate scheduling strategies. 
Execution phase: Implement scheduling strategies.
 
Figure. 2. The problem and the results generated by CoT and SRR-
CoT. 
The comparison of results demonstrates that the CoT 
outlines scheduling in stages. In contrast, the SRR-CoT 
not only details the dispatcher’s process of understanding, 
analyzing, and outputting but also summarizes its inputs 
and outputs, thereby providing richer content than CoT. 
Finally, We further designed a comparative 
experiment for the scenarios of WBMS deployment in 
medium enterprise to investigate the impact of CoT and 
SRR-CoT methods on the accuracy of QoE evaluation of 
LLMs. The experiment systematically tested four 
representative LLM models (ChatGPT-4o-mini, Llama3-
8B, Qwen2.5 -72B-Instruct, and DeepSeek -V3).The 
experimental results are illustrated in Figure. 3. 
Experimental results show that SRR-CoT has 
significantly higher QoE evaluation accuracy compared 
to CoT across  the four models . Furthermore, we 
quantitatively compared the computational overhead 
between SRR-CoT and CoT on the same hardware. The 
results demonstrate that SRR -CoT introduces an 
additional 25%-30% inference time compared to standard 
CoT. However, this overhead is justified by an average 
accuracy improvement of 46%, particularly in MEC 
environments where high precision is critical. Therefore, 
we argue that such a trade-off is reasonable for accuracy-
sensitive scenarios like MEC. 
 
Figure. 3. Comparison of QoE evaluation accuracy of LLMs in 
medium enterprise using CoT and SRR-CoT 
C. Experiment 1: Basic Scheduling Process 
After designing prompts for the four agents, we 
conducted basic scheduling. Taking on the role of the 
dispatcher, the scheduling is performed based on the 
summary information provided by the maintenance 
engineer. The prompts, inputs, and output results for the 
dispatcher are illustrated in Figure. 4. 
：Maintenance engineer ：dispatcher
：In the wireless edge-based battery management system, batteries are divided into four types 
(n={1,2,3,4}), where n=1 means that the battery has enough energy and no alarm; n=2 means that the 
battery has enough energy, but the battery has a ciritical alarm; n=3 means that the battery has 
insufficient energy, but no alarm; n=4 means that the battery has insufficient energy and has a ciritical 
alarm. The overall utility function of the system is U=U1 to the qth power*U2 to the (1 -q)th power. 
Among them, U1 is the dangerous performance, which is only affected by the delay T(n) (n=4). U2 is 
the service performance, which is affected by the delay T(n) and energy consumption E(n) (n={1,2,3,4}).
You are a dispatcher responsible for the first round of dispatching based on the summary information of 
the operation and maintenance engineer.
You need to determine the initial parameters w(n,1) and w(n,2) (n={1,2,3,4}, and w(n,1)+w(n,2)=1) and q 
(1 value), and perform the following steps: 
1. Understand the current status of users, networks, resources, etc. of the wireless battery management 
system based on the summary information of the operation and maintenance engineer.
2. Analyze how to set the initial parameters for the wireless battery management system based on the 
understanding of the status of users, networks, resources, etc.
3. Output the Simulation results obtained by simulating according to the initial parameters.
Interaction object: Operation and maintenance engineer
Interaction mode: Output
Interaction format: {
-Input: Summary information of the operation and maintenance engineer
-Output: The dispatch result of the dispatcher in this round
Output format: Output as text
Current interaction round number: Round 1
# Prompts for Dispatcher
# Input
：Values ​​of delay for different types of batteries
Battery (n=1): 0.00160054, 0.00140023, 0.00130987, 0.00151234,  0.00105097, ...
Battery (n=2): 0.00141909, 0.00089466 ,0.00123145, 0.00125078, 0.00130012, ...
Battery (n=3): 0.00106189, 0.00076755 , 0.00091234, 0.00095067, 0.00099999, ...
Battery (n=4): 0.00167570, 0.00134056, 0.00151273, 0.00162849, 0.00100486, ...
Values ​​of energy consumption for different types of batteries
Battery (n=1): 0.00005999, 0.00005623, 0.00005587, 0.00005314,  0.00004054, ...
Battery (n=2): 0.00006310, 0.00005025, 0.00004567, 0.00004988,  0.00003291, ...
Battery (n=3): 0.00009339, 0.00004596 , 0.00007012, 0.00007545, 0.00008122, ...
Battery (n=4): 0.00006305, 0.00003806 , 0.00005112, 0.00005534, 0.00005278, ...
# Output
 
Figure. 4. The prompt and input and output of the dispatcher (first 
round). 
D. Experiment 2: Refining Process 
Then, we focus on intent refinement. First, the role of 
the analyst is assumed to analyze the results of the first 
round of scheduling. Next, the role of the customer is 
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply. 
taken to provide feedback on the analyst’s results based 
on the current background information and to make 
adjustment requests. Then, the second round begins with 
the dispatcher’s role, consolidating the previous 
scheduling results, the maintenance engineer’s summary 
information, the analysis results, and the adjustment 
requests to draw conclusions on scheduling criteria and 
call the scheduling tool for the next round of scheduling. 
Finally, the above three processes are repeated until the 
customer is satis fied with the analysis results. The 
prompts, inputs, and output results for the analyst, the 
customer, the dispatcher are illustrated in Figure. 5, 6, 7. 
：Values ​​of delay for different types of batteries
Battery (n=1): 0.00160054, 0.00140023, 0.00130987, 0.00151234,  0.00105097, ...
Battery (n=2): 0.00141909, 0.00089466 ,0.00123145, 0.00125078, 0.00130012, ...
Battery (n=3): 0.00106189, 0.00076755 , 0.00091234, 0.00095067, 0.00099999, ...
Battery (n=4): 0.00167570, 0.00134056, 0.00151273, 0.00162849, 0.00100486, ...
Values ​​of energy consumption for different types of batteries
Battery (n=1): 0.00005999, 0.00005623, 0.00005587, 0.00005314,  0.00004054, ...
Battery (n=2): 0.00006310, 0.00005025, 0.00004567, 0.00004988,  0.00003291, ...
Battery (n=3): 0.00009339, 0.00004596 , 0.00007012, 0.00007545, 0.00008122, ...
Battery (n=4): 0.00006305, 0.00003806 , 0.00005112, 0.00005534, 0.00005278, ...
You are an analyst responsible for analyzing the scheduling results.
You need to determine the average, maximum and minimum values ​​of the delay and energy consumption of 
different types of batteries and perform the following steps: 
1. Understand the delay and energy consumption information of different types of batteries simulated based on 
the scheduling results of this round of dispatchers.
2. Analyze the delay and energy consumption information of different types of batteries from the perspectives 
of average, maximum and minimum values.
3. Output the average, maximum and minimum values ​​of the delay and energy consumption of different types 
of batteries.
Interaction object: dispatcher
Interaction mode: output
Interaction format: {
- Input: Scheduling results
- Output: The analysis results of the analyst in this round (the average, maximum and minimum values ​​of the 
delay and energy consumption of different types of batteries)}
Current number of interaction rounds: Round 1
：dispatcher ：analyst
# Prompts for Analyst
# Input
# Output
：Average, maximum and minimum values ​​of delay for different types of batteries
Battery (n=1): normal - average: 0.00135071, maximum: 0.00160054, minimum: 0.00105097
Battery (n=2): full - average: 0.00122047, maximum: 0.00141909, minimum: 0.00089466
Battery (n=3): loss - average: 0.00092895, maximum: 0.00106189, minimum: 0.00076755
Battery (n=4): critical - average: 0.00141011, maximum: 0.00167570, minimum: 0.00100486
Average, maximum and minimum values ​​of energy consumption for different types of batteries
Battery (n=1): normal - average: 0.00005449, maximum: 0.00005999, minimum: 0.00004054
Battery (n=2): full - average: 0.00004892, maximum: 0.00006310, minimum: 0.00003291
Battery (n=3): loss - average: 0.00006904, maximum: 0.00009339, minimum: 0.00004596
Battery (n=4): critical - average: 0.00005066, maximum: 0.00006305, minimum: 0.00003806
 
Figure. 5. The prompt and input and output of the analyst. 
：Average, maximum and minimum values ​​of delay for different types of batteries
Battery (n=1): normal - average: 0.00135071, maximum: 0.00160054, minimum: 0.00105097
Battery (n=2): full - average: 0.00122047, maximum: 0.00141909, minimum: 0.00089466
Battery (n=3): loss - average: 0.00092895, maximum: 0.00106189, minimum: 0.00076755
Battery (n=4): critical - average: 0.00141011, maximum: 0.00167570, minimum: 0.00100486
Average, maximum and minimum values ​​of energy consumption for different types of batteries
Battery (n=1): normal - average: 0.00005449, maximum: 0.00005999, minimum: 0.00004054
Battery (n=2): full - average: 0.00004892, maximum: 0.00006310, minimum: 0.00003291
Battery (n=3): loss - average: 0.00006904, maximum: 0.00009339, minimum: 0.00004596
Battery (n=4): critical - average: 0.00005066, maximum: 0.00006305, minimum: 0.00003806
You are a customer and I am responsible for commenting on the analysis results of this round of analysts 
based on the following background.
Background: {The current demand is urgent processing, which needs to be completed within 1ms so as not 
to affect the work of its users. In addition, insufficient battery energy will affect the work of its users and 
bring poor experience to users, so the battery life needs to be extended. }
You need to make adjustment requirements and perform the following steps:
1. Understand the background of the current system.
2. Comment on the analysis results of this round of analysts based on the background learned.
3. Based on the comments, give relevant suggestions on how to adjust the latency and energy consumption 
of different types of batteries.
Interaction object: Analyst
Interaction mode: Output
Interaction format: {
- Input: Analysis results of this round of analysts (average, maximum and minimum values ​​of latency and 
energy consumption of different types of batteries)
- Output: Adjustment requirements of this round of customers (suggestions on latency and energy 
consumption of different types of batteries)}
Current number of interaction rounds: Round 1
：analyst
# Prompts for Customer
# Input
# Output
: Suggestions for Adjustments
1.Optimize Algorithms  :Reassess and optimize the al gorithms used for processing to ensure that they 
can execute faster. Look into performance enhancements. such as using more efficient data structures 
or parallel processing techni ques. 2.Enhance Battery Management: Implement smarter battery 
management techniques that can dynamically adjust power distribution based on  immediate 
processing needs, minimizing delay times . 3.Prioritize Fast Response Batteries: Consider focusing on 
using battery type n=3 for operations that require quicker response times, as it currently shows the 
lowest average delay. Further improvements could be made to reduce its average delay closer to the 
required threshold. 4. Energy-efficient Protocols:  Investigate and adopt energy-efficient 
communication protocols and operational methods that reduce energy  consumption while 
maintaining performance . 5.Battery Cycle Management: Implement intelligent battery cycle 
management strategies, which ensure that batteries are used efficiently during peak demand periods 
and allow for recharge or maintenance during off -peak times. 6.Energy Recovery Systems: Explore 
options for energy recovery systems or regenerative braking (if applicable) to extend battery life by  
recharging during operation.
：customer
 
Figure. 6. The prompt and input and output of the customer. 
：customer
：Maintenance engineer ：dispatcher
You are a dispatcher who is responsible for gathering the dispatch results of the first round of dispatchers, the 
analysis results of analysts, the adjustment requirements of customers, and the summary information of operation 
and maintenance engineers, and conducting the second round of dispatching.
You need to determine the adjusted parameters W(n,1) and W(n,2) (n={1,2,3,4}, and w(n,1)+w(n,2)=1) and q (1 
value), and perform the following steps: 
1. Gather the dispatch results of the first round of dispatchers, the analysis results of analysts, the adjustment 
requirements of customers, and the summary information of operation and maintenance engineers.
2. Analyze how to adjust the parameters of the wireless battery management system based on all the gathered 
information.
3. Output the Simulation results obtained by simulating according to the adjusted parameters .
Interaction object: operation and maintenance engineers, analysts, customers
Interaction mode: output
Interaction format: {
-Input: dispatcher's dispatch results in the first round, analyst's analysis results, customer's adjustment 
requirements and operation and maintenance engineer's summary content
-Output: dispatcher's dispatch results in this round
Output format: Output as text
Current interaction round number: 2nd round
：analyst
# Prompts for Dispatcher
# Input
：The dispatch result of the dispatcher in the first round
： Summary information of the operation and maintenance engineer
： Suggestions for Adjustments
1.Optimize Algorithms  :Reassess and optimize the al gorithms used for processing to ensure that they can 
execute faster. Look into performance enhancements. such as using more efficient data structures or 
parallel processing techni ques 2.Enhance Battery Management: Implement smarter battery management 
techniques that can dynamically adjust power distribution based on  immediate processing needs, 
minimizing delay times .
3.Prioritize Fast Response Batteries: Consider focusing on using battery type n=3 for operations that 
require quicker response times, as it currently shows the lowest average delay. Further improvements 
could be made to reduce its average delay closer to the required threshold
4. Energy-efficient Protocols:  Investigate and adopt energy-efficient communication protocols and 
operational methods that reduce energy  consumption while maintaining performance
5.Battery Cycle Management: Implement intelligent battery cycle management strategies, which ensure 
that batteries are used efficiently during peak demand periods and allow for recharge or maintenance 
during off-peak times.
6.Energy Recovery Systems: Explore options for energy recovery systems or regenerative braking (if 
applicable) to extend battery life by  recharging during operation.
# Output
：Values ​​of delay for different types of batteries
Battery (n=1): 0.00140054, 0.00120023, 0.00120987, 0.00141234, 0.00115097, ...
Battery (n=2): 0.00131909, 0.00079466, 0.00113145, 0.00115078, 0.00120012, ...
Battery (n=3): 0.00116189, 0.00086755, 0.00101234, 0.00105067, 0.00109999, ...
Battery (n=4): 0.00157570, 0.00124056, 0.00141273, 0.00152849, 0.00120486, ...
Values ​​of energy consumption for different types of batteries
Battery (n=1): 0.00006399, 0.00006023, 0.00005887, 0.00005614, 0.00005054, ...
Battery (n=2): 0.00006510, 0.00005225, 0.00004867, 0.00005188, 0.00003591, ...
Battery (n=3): 0.00008339, 0.00003596, 0.00006012, 0.00006545, 0.00007122, ...
Battery (n=4): 0.00007305, 0.00004806, 0.00006112, 0.00006534, 0.00005878, ...
：Analysis results of this round of analysts (average, maximum and minimum values ​​of latency and 
energy consumption of different types of batteries)
 
Figure. 7. The prompt and input and output of the dispatcher 
(second round). 
After multiple interaction rounds in the experiment, 
we summarized the weight adjustments, illustrated in 
Figure. 8,9. Initially, all weights fluctuated with increased 
interactions. However, after 15 rounds, they stabilized as 
the customer, satisfied with the analyst's results, made 
fewer suggestions on delay and energy consumption for 
different battery types. 
 
Figure. 8.  Delay weight summary after multiple rounds of interaction. 
           
                               
 
   
   
   
   
   
   
   
   
   
 
            
                              
                              
                              
                              
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply. 
 
Figure. 9.  Energy consumption summary after multiple rounds of 
interaction. 
E. Experiment on the Accuracy of QoE Evaluation of 
LLMs 
To investigate the impact of the HI MAL intent 
refinement method on the WBMS deployment across 
enterprises of different scales (small, medium, and large), 
we designed a comparative experiment to analyze its 
effect on the accuracy of QoE evaluation in LLMs. The 
experiment employed ChatGPT-4o-mini and Llama3-8B 
as test models, c omparing their performance before and 
after applying the HIMAL intent refinement method. The 
experimental results are illustrated in Figure. 10. 
 
Figure. 10.  Comparison of the accuracy of QoE evaluation of LLMs 
before and after using HIMAL intent refinement method 
The experimental results demonstrate that the QoE 
evaluation accuracy of both models shows significant 
improvement after implementing the HI MAL intent 
refinement method across enterprises of all scales (small, 
medium, and large). 
IV. SUMMARY 
This paper proposes a HI MAL intent refinement 
method for task offloading in MEC. First, we establish a 
comprehensive system model for MEC. Second, we 
design a HIMAL system architecture. Finally, we conduct 
scheduling decision experiments using our proposed 
prompt method and perform a detailed experimental 
analysis. The experimental results demonstrate that  the 
HIMAL intent refinement method significantly enhances 
system performance by incorporating human expertise as 
interpreters within the LLM’s workflow. Furthermore, 
the HI MAL system effectively integrates human 
feedback with AI learning processes, thereby improving 
both the accuracy of AI outputs and contextual 
understanding capabilities. For future work, we plan to 
focus on optimizing performance with PEER  [16] or 
DOE patterns, and integrating RAG functionalities and 
word slot system to broaden application scenarios.

## § Acknowledgment

This work is funded by China Mobile 
Communications Group Co.,Ltd.

## § References

[1] Zhang, P., Xu, W, Gao, H., et al.  Toward wisdom-evolutionary 
and primitive -concise 6G: A new paradigm of semantic 
communication networks[J]. Engineering, 2022, 8: 60-73. 
[2] Wang, Zhenpo., Yuan, Changgui., Li, Xiaoyu. Analysis on 
technical challenges and development trends of power battery 
safety management for new energy vehicles[J]. Automotive 
Engineering, 2021, 42(12): 1606-1620. 
[3] Hou X, Ren Z, Yang K, et al. IIoT -MEC: A novel mobile edge 
computing framework for 5G -enabled IIoT[C]//2019 IEEE 
Wireless Communications and Networking Conference 
(WCNC). IEEE, 2019: 1-7. 
[4] Gajjar, V., Bhagat, S., Awasthi, A. Towards a Framework for 
Quality of Service and Experience in IoT[J]. IEEE Access, 2020, 
8, 187583-187599. 
[5] Zhao, Y., Zhang, L. A Comprehensive Survey on Quality of 
Experience in Industrial IoT[J]. IEEE Internet of Things Journal, 
2021, 8(1), 32-45. 
[6] Minovski, D. Quality of Experience in Industrial Internet of 
Things[D]. Luleå  University of Technology, 2021. 
[7] Shao, J., Tong, J., Wu, Q., et al. WirelessLLM: Empowering 
Large Language Models Towards Wireless Intelligence[J]. 
arXiv preprint arXiv:2405.17053, 2024.  
[8] Kalita, A. Large Language Models (LLMs) for Semantic 
Communication in Edge-based IoT Networks[J]. arXiv preprint 
arXiv:2407.20970, 2024. 
[9] Jiang, F., Peng , Y., Dong , L., et al.  Large language model 
enhanced multi-agent systems for 6G communications[J]. IEEE 
Wireless Communications, 2024. 
[10] Zhang, R., Du, H., Liu, Y., et al. Interactive AI with retrieval -
augmented generation for next generation networking[J]. IEEE 
Network, 2024. 
[11] Zhao P, Zhang H, Yu Q, et al. Retrieval-augmented generation 
for ai -generated content: A survey[J]. arXiv preprint 
arXiv:2402.19473, 2024. 
[12] Wei J, Wang X, Schuurmans D, et al. Chain -of-thought 
prompting elicits reasoning in large language models[J]. 
Advances in neural information processing systems, 2022, 35: 
24824-24837. 
[13] Wang X, Wei J, Schuurmans D, et al. Self-consistency improves 
chain of thought reasoning in language models[J]. arXiv 
preprint arXiv:2203.11171, 2022. 
[14] Yao S, Yu D, Zhao J, et al. Tree of thoughts: Deliberate problem 
solving with large language models[J]. Advances in neural 
information processing systems, 2023, 36: 11809-11822. 
[15] Cao Z, Gao W, Fu Y, et al. Wireless battery management 
systems: innovations, challenges, and future perspectives[J]. 
Energies, 2024, 17(13): 3277. 
[16] Wang Y, Li X, Wang B, et al. PEER: Expertizing Domain -
Specific Tasks with a Multi -Agent Framework and Tuning 
Methods[J]. arXiv preprint arXiv:2407.06985, 2024. 
 
           
                               
 
   
   
   
   
   
   
   
   
   
 
            
                                           
                                           
                                           
                                           
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 00:18:09 UTC from IEEE Xplore.  Restrictions apply.
