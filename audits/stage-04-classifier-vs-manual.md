# Stage 04 — Classifier vs. Manual Audit

- Total papers: **2949**
- Overall match: **2650/2949 (89.9%)**
- Include recall (classifier finds user's Includes): **92.5%**
- Exclude recall (classifier matches user's Excludes): **89.2%**

## Confusion matrix

| Manual \ Classifier | Include | Exclude |
|---|---|---|
| **Include** | 558 | 45 (false negatives) |
| **Exclude** | 254 (false positives) | 2092 |

## By winning category

| Category | Total | Manual=Include | Manual=Exclude | Match% |
|---|---:|---:|---:|---:|
| agent | 121 | 86 | 35 | 71.1% |
| llm_agentic_ai_generic | 412 | 253 | 159 | 61.4% |
| llm_as_workload | 123 | 14 | 109 | 88.6% |
| mas | 279 | 219 | 60 | 78.5% |
| no_signal | 1408 | 21 | 1387 | 98.5% |
| out_of_scope | 47 | 4 | 43 | 91.5% |
| review | 66 | 0 | 66 | 100.0% |
| rl | 493 | 6 | 487 | 98.8% |

## False negatives (45) — user said Include, classifier said Exclude

These are the papers the classifier MISSED. Tightening rules should focus on adding patterns that catch these.

| Paper ID | Title | Winning Category | Evidence |
|---|---|---|---|
| paper-1496 | Investigating Neurosymbolic AI for Intent-based Service Management | no_signal | (none) |
| paper-1866 | Adaptive online task scheduling algorithm for resource regulation on heterogeneous platforms | no_signal | (none) |
| paper-571 | Efficient Resource Scheduling for Distributed Infrastructures Using Negotiation Capabilities | no_signal | (none) |
| paper-910 | Realizing Intent-Driven Network Management with TM Forum Standards | no_signal | Intent-Driven |
| paper-2779 | Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing | no_signal | (none) |
| paper-751 | SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems | no_signal | (none) |
| paper-014 | Towards a fairer negotiation for dynamic resource allocation in cloud by relying on trustworthiness | no_signal | resource allocation |
| paper-015 | Towards a fairer negotiation for dynamic resource allocation in cloud by relying on trustworthiness | no_signal | resource allocation |
| paper-034 | Elastic & Load-Spike Proof One-to-Many Negotiation to Improve the Service Acceptability of an Open SaaS Provider | no_signal | (none) |
| paper-1532 | Large-Small Model Synergy for High-Recall and Efficient UAV-based Aerial Surveillance | no_signal | (none) |
| paper-1596 | SigMorph: A Transfer-Oriented Toolkit for Fingerprint Injection in Fine-Tuned Models | no_signal | (none) |
| paper-172 | FIPA-based reference architecture for efficient discovery and selection of appropriate cloud service using cloud ontolog | no_signal | (none) |
| paper-2736 | LAGTrust: Language-Augmented Graph Representation Learning for Trust Evaluation in Cloud-Network Convergence | no_signal | (none) |
| paper-2809 | Model-Driven Development of Chatbot Microservices | no_signal | (none) |
| paper-468 | Learn to Coordinate for Computation Offloading and Resource Allocation in Edge Computing: A Rational-Based Distributed A | no_signal | Resource Allocation |
| paper-497 | Distributed Task Scheduling in Serverless Edge Computing Networks for the Internet of Things: A Learning Approach | no_signal | (none) |
| paper-635 | Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach | no_signal | (none) |
| paper-983 | Mastering Snowflake Platform: Generate, fetch, and automate Snowflake data as a skilled data practitioner | no_signal | (none) |
| paper-853 | Automation of AD-OHC Dashbord and Monitoring of Cloud Resources using Genrative AI to Reduce Costing and Enhance Perform | no_signal | (none) |
| paper-608 | RTHop: Real-Time Hop-by-Hop Mobile Network Routing by Decentralized Learning With Semantic Attention | no_signal | Routing |
| paper-066 | Towards Autonomic Mobile Network Operators | no_signal | (none) |
| paper-1001 | Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Le | rl | Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning, Multi-Agent, Agent |
| paper-1011 | CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices | llm_as_workload | LLM Inference, LLM |
| paper-1094 | Understanding Performance Implications of LLM Inference on CPUs | llm_as_workload | LLM Inference, LLM |
| paper-1143 | MADRL-Based URLLC-Aware Task Offloading for Air-Ground Vehicular Cooperative Computing Network | rl | MADRL |
| paper-1248 | Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks | llm_as_workload | Large Language Model Fine-Tuning, Large Language Model, Language Model |
| paper-1522 | LLM Compression for Enhanced Performance: A Comparative Study of Structured and Unstructured Pruning Techniques | llm_as_workload | LLM Compression for Enhanced Performance: A Comparative Study of Structured and Unstructured Pruning, LLM |
| paper-1686 | Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications | llm_as_workload | LLM Inference, LLM |
| paper-2239 | Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures | llm_as_workload | LLM Inference, LLM |
| paper-585 | Leftover: Improving Large Language Model Inference Efficiency by Leveraging Idle Resources | llm_as_workload | Large Language Model Inference, Large Language Model, Language Model |
| paper-1214 | Performance Improvement for UAV-Assisted Mobile Edge Computing with Multi-Agent Deep Reinforcement Learning | rl | Performance Improvement for UAV-Assisted Mobile Edge Computing with Multi-Agent Deep Reinforcement Learning, Multi-Agent, Agent |
| paper-1569 | Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks | llm_as_workload | Inference Optimization for Large Language Model, Large Language Model, Language Model |
| paper-1813 | Multiagent Reinforcement-Learning-Based AAV Path and Resource Allocation for Ground-to-Air Communication Network | rl | Multiagent Reinforcement-Learning, Resource Allocation, Multiagent, Multiagent |
| paper-1821 | SAC-Based Latency Optimization for Collaborative Inference of Distributed Large Language Models in Industrial IoT | llm_as_workload | Inference of Distributed Large Language Models, Large Language Models, Language Models |
| paper-2500 | Dynamic Micro-Batch and Token-Budget Scheduling for IoT-Scale Pipeline-Parallel LLM Inference | llm_as_workload | LLM Inference, LLM |
| paper-2674 | Reliable and Efficient LLM Inference on Resource-Constrained Mobile Devices via Dynamic Scheduling | llm_as_workload | LLM Inference, LLM |
| paper-1197 | Practical Assessment of Large Language Models in Cloud Computing Using Real-World Data Applications | out_of_scope | Practical Assessment of Large Language Models, Large Language Models, Language Models |
| paper-1425 | VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture | out_of_scope | Video Summarization by Prompt, Prompt Engineering |
| paper-1449 | Building Artificial Intelligence Agents with Large Language Models for Autonomous Interpretation of Equipment Sensor Dat | out_of_scope | Autonomous Interpretation of Equipment Sensor Data, with Large Language Models, Agents, Large Language Models, Language Models |
| paper-1460 | Adaptive layer splitting for wireless large language model inference in edge computing: a model-based reinforcement lear | llm_as_workload | large language model inference, large language model, language model |
| paper-1471 | Length Instruction Fine-Tuning with Chain-of-Thought (LIFT-COT): Enhancing Length Control and Reasoning in Edge-Deployed | llm_as_workload | Fine-Tuning with Chain-of-Thought (LIFT-COT): Enhancing Length Control and Reasoning in Edge-Deployed Large Language Models, Large Language Models, Language Models, Chain-of-Thought |
| paper-1526 | Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading | out_of_scope | Smart Assistant on a Microcontroller, LLM |
| paper-215 | Efficient transformer-based large scale language representations using hardware-friendly block structured pruning | llm_as_workload | transformer-based large scale language representations using hardware-friendly block structured pruning, transformer |
| paper-2651 | DT-MASAC: A Digital Twin-Augmented Multi-Agent Framework for AoI-Oriented Resource Allocation in Vehicular Networks | rl | MASAC, Resource Allocation, Multi-Agent, Agent |
| paper-895 | Multi-Agent-Deep-Reinforcement-Learning-Enabled Offloading Scheme for Energy Minimization in Vehicle-to-Everything Commu | rl | Multi-Agent-Deep-Reinforcement-Learning, Multi-Agent, Agent |

## False positives (254) — user said Exclude, classifier said Include

These are the papers the classifier OVER-INCLUDED. Adding overrides or out-of-scope patterns can fix.

| Paper ID | Title | Winning Category | Evidence |
|---|---|---|---|
| paper-1906 | AI-Powered High-Performance Computing for Real-Time Data Processing in 6G Networks | llm_agentic_ai_generic | AI-Powered |
| paper-2092 | Network Traffic Reduction Through AI-Assisted Local Data Optimization of Synthetic Data | llm_agentic_ai_generic | AI-Assisted |
| paper-1229 | SE-DO: Navigating the 6G Frontier with Scalable and Efficient DevOps for Intelligent Agents Optimization | agent | Agents |
| paper-2441 | Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks | llm_agentic_ai_generic | Resource Allocation, AI Service |
| paper-1118 | AI-Augmented Software Development: Boosting Efficiency and Quality | llm_agentic_ai_generic | AI-Augmented |
| paper-1363 | AI-Driven Optimization of Chiplet Architectures Using Reinforcement Learning | llm_agentic_ai_generic | AI-Driven |
| paper-1962 | Integrating fourth industrial revolution (4IR) technologies with green energy systems: A framework for AI-driven smart g | llm_agentic_ai_generic | AI-driven |
| paper-2244 | Revolutionizing Network Management: The Journey to AI-native Autonomy | llm_agentic_ai_generic | AI-native |
| paper-2668 | Toward Practical Operation of Deep Reinforcement Learning Agents in Real-World Network Management at Open RAN Edges | agent | Agents |
| paper-107 | Design and analysis of distributed load management: Mobile agent based probabilistic model and fuzzy integrated model | agent | agent |
| paper-1384 | The Role of Large Language Models in Designing Reliable Networks for Internet of Things: A Short Review of Most Recent D | llm_agentic_ai_generic | Large Language Models, Language Models |
| paper-1385 | Techie: Tackling Video Prefetching at Edge Networks as POMDP Via an Intrinsically Motivated RL Agent | agent | Agent |
| paper-1495 | The Integration of Agentic AI in 6G Wireless Networks: State-of-the-Art, Challenges, and Future Perspectives | llm_agentic_ai_generic | Agentic |
| paper-1497 | Management of Safety-Critical AI Services in the Compute Continuum | llm_agentic_ai_generic | AI Services |
| paper-2343 | Air Pollutant Traceability Based on Federated Learning of Edge Intelligent Perception Agents | agent | Agents |
| paper-2619 | Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integr | agent | agents |
| paper-262 | Orchestrating heterogeneous devices and ai services as virtual sensors for secure cloud-based iot applications† | llm_agentic_ai_generic | ai services |
| paper-264 | Task scheduling, resource provisioning, and load balancing on scientific workflows using parallel SARSA reinforcement le | agent | load balancing, agents |
| paper-680 | Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior | agent | Agents |
| paper-730 | Privacy-Aware Intelligent Healthcare Services with Federated Learning Architecture and Reinforcement Learning Agent | agent | Agent |
| paper-178 | A cloud resource management framework for multiple online scientific workflows using cooperative reinforcement learning  | agent | agents |
| paper-179 | Online scheduling of dependent tasks of cloud’s workflows to enhance resource utilization and reduce the makespan using  | agent | agents |
| paper-2126 | Design of an Iterative AI-Driven Latency Prediction and QoS-Aware Task Scheduling in Mobile Edge Computing: A Federated  | llm_agentic_ai_generic | AI-Driven |
| paper-2159 | Dynamic Task Scheduling and Smart Caching in Fog-Cloud Architectures Using Advantage Actor-Critic Agents | agent | Agents |
| paper-302 | Development of QoS-aware agents with reinforcement learning for autoscaling of microservices on the cloud | agent | agents |
| paper-676 | Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management | agent | Agents |
| paper-1149 | Mobile Agents-Based Framework for Dynamic Resource Allocation in Cloud Computing | agent | Resource Allocation, Agents |
| paper-1405 | A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks | llm_agentic_ai_generic | RAG |
| paper-1504 | A review of state-of-the-art techniques for large language model compression | llm_agentic_ai_generic | large language model, language model |
| paper-1583 | Research on Key Technologies of Intelligent Review Based on Large Language Model Business Scenarios | llm_agentic_ai_generic | Large Language Model, Language Model |
| paper-2403 | Generative AI for the Internet of Vehicles: A Review of Advances in Training, Decision-Making, and Security | llm_agentic_ai_generic | Generative AI |
| paper-2466 | A Review on Edge Large Language Models: Design, Execution, and Applications | llm_agentic_ai_generic | Large Language Models, Language Models |
| paper-2808 | Bio-inspired AI Algorithms for Autonomous Agents: Revolutionizing Decision-Making, Resource Allocation, and Adaptability | agent | Resource Allocation, Agents |
| paper-292 | Mobile agent-based service migration in mobile edge computing | agent | agent |
| paper-2949 | Explainable AI and Multi-Agent Systems for Energy Management in IoT-Edge Environments: A State of the Art Review | mas | Multi-Agent, Agent |
| paper-325 | An agent-based model for resource provisioning and task scheduling in cloud computing using DRL | agent | agent |
| paper-2050 | Demonstrating Smart Scaling of AI-Services for Future Networks | llm_agentic_ai_generic | AI-Services |
| paper-1549 | Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems | mas | Multi-Agents, Agents |
| paper-1594 | AI-Enabled Circular Supply Chain Framework for Sustainable Returns Management: A Multi-Technology Integration Approach | llm_agentic_ai_generic | AI-Enabled |
| paper-1751 | Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS | agent | Agents |
| paper-1998 | Nexus Search: A Scalable and Distributed Search Engine Powered by Open Source LLMs | llm_agentic_ai_generic | LLMs |
| paper-2154 | Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches | agent | Agent, AI Agent |
| paper-2580 | AI-Enabled Vehicular Data Offloading for Sustainable Smart Cities: Taxonomy, KPI Models, and Open Challenges | llm_agentic_ai_generic | AI-Enabled |
| paper-2806 | Agent AI-as-a-Service (AIaaS) in Multi-Cloud Environments: Challenges, Opportunities, and the Future of Autonomous AI-Dr | agent | Agent, Agent AI, AI-Driven |
| paper-2921 | Service reliability of intelligent computing cluster systems for large language models | llm_agentic_ai_generic | large language models, language models |
| paper-984 | Generative Artificial Intelligence for Biomedical and Smart Health Informatics | llm_agentic_ai_generic | Generative Artificial Intelligence |
| paper-988 | Scaling Generative AI for E&P | llm_agentic_ai_generic | Generative AI |
| paper-1163 | Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations | llm_agentic_ai_generic | LLM |
| paper-1491 | Optimizing Financial Decision-Making in Cloud Environments: A GenAI-driven Approach to Convert Natural Language to SQL | llm_agentic_ai_generic | GenAI, GenAI |
| paper-1787 | CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network | llm_agentic_ai_generic | LLM Training, Load Balancing, LLM |

_…and 204 more false positives._
