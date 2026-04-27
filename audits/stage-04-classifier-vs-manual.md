# Stage 04 — Classifier vs. Manual Audit

- Total papers: **2949**
- Overall match: **2687/2949 (91.1%)**
- Include recall (classifier finds user's Includes): **97.2%**
- Exclude recall (classifier matches user's Excludes): **89.7%**

## Confusion matrix

| Manual \ Classifier | Include | Exclude |
|---|---|---|
| **Include** | 556 | 16 (false negatives) |
| **Exclude** | 246 (false positives) | 2131 |

## By winning category

| Category | Total | Manual=Include | Manual=Exclude | Match% |
|---|---:|---:|---:|---:|
| agent | 122 | 87 | 35 | 71.3% |
| llm_agentic_ai_generic | 410 | 255 | 155 | 62.2% |
| llm_as_workload | 134 | 2 | 132 | 98.5% |
| mas | 270 | 214 | 56 | 79.3% |
| no_signal | 1397 | 14 | 1383 | 99.0% |
| out_of_scope | 43 | 0 | 43 | 100.0% |
| review | 71 | 0 | 71 | 100.0% |
| rl | 502 | 0 | 502 | 100.0% |

## False negatives (16) — user said Include, classifier said Exclude

These are the papers the classifier MISSED. Tightening rules should focus on adding patterns that catch these.

| Paper ID | Title | Winning Category | Evidence |
|---|---|---|---|
| paper-1866 | Adaptive online task scheduling algorithm for resource regulation on heterogeneous platforms | no_signal | (none) |
| paper-571 | Efficient Resource Scheduling for Distributed Infrastructures Using Negotiation Capabilities | no_signal | (none) |
| paper-751 | SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems | no_signal | (none) |
| paper-014 | Towards a fairer negotiation for dynamic resource allocation in cloud by relying on trustworthiness | no_signal | (none) |
| paper-015 | Towards a fairer negotiation for dynamic resource allocation in cloud by relying on trustworthiness | no_signal | (none) |
| paper-034 | Elastic & Load-Spike Proof One-to-Many Negotiation to Improve the Service Acceptability of an Open SaaS Provider | no_signal | (none) |
| paper-1532 | Large-Small Model Synergy for High-Recall and Efficient UAV-based Aerial Surveillance | no_signal | (none) |
| paper-1596 | SigMorph: A Transfer-Oriented Toolkit for Fingerprint Injection in Fine-Tuned Models | no_signal | (none) |
| paper-468 | Learn to Coordinate for Computation Offloading and Resource Allocation in Edge Computing: A Rational-Based Distributed A | no_signal | (none) |
| paper-497 | Distributed Task Scheduling in Serverless Edge Computing Networks for the Internet of Things: A Learning Approach | no_signal | (none) |
| paper-635 | Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach | no_signal | (none) |
| paper-983 | Mastering Snowflake Platform: Generate, fetch, and automate Snowflake data as a skilled data practitioner | no_signal | (none) |
| paper-853 | Automation of AD-OHC Dashbord and Monitoring of Cloud Resources using Genrative AI to Reduce Costing and Enhance Perform | no_signal | (none) |
| paper-608 | RTHop: Real-Time Hop-by-Hop Mobile Network Routing by Decentralized Learning With Semantic Attention | no_signal | (none) |
| paper-1629 | Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction | llm_as_workload | Large Language Model Inference, BERT, Large Language Model, Language Model |
| paper-2041 | Joint Communication and Inference User Allocation in LLM Native Networks | llm_as_workload | Inference User Allocation in LLM, LLM |

## False positives (246) — user said Exclude, classifier said Include

These are the papers the classifier OVER-INCLUDED. Adding overrides or out-of-scope patterns can fix.

| Paper ID | Title | Winning Category | Evidence |
|---|---|---|---|
| paper-1906 | AI-Powered High-Performance Computing for Real-Time Data Processing in 6G Networks | llm_agentic_ai_generic | AI-Powered |
| paper-2092 | Network Traffic Reduction Through AI-Assisted Local Data Optimization of Synthetic Data | llm_agentic_ai_generic | AI-Assisted |
| paper-1229 | SE-DO: Navigating the 6G Frontier with Scalable and Efficient DevOps for Intelligent Agents Optimization | agent | Agents |
| paper-1264 | Toward Intelligent and Adaptive Task Scheduling for 6G: An Intent-Driven Framework | llm_agentic_ai_generic | Intent-Driven, Intent-Driven |
| paper-2441 | Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks | llm_agentic_ai_generic | AI Service |
| paper-1118 | AI-Augmented Software Development: Boosting Efficiency and Quality | llm_agentic_ai_generic | AI-Augmented |
| paper-1363 | AI-Driven Optimization of Chiplet Architectures Using Reinforcement Learning | llm_agentic_ai_generic | AI-Driven |
| paper-1962 | Integrating fourth industrial revolution (4IR) technologies with green energy systems: A framework for AI-driven smart g | llm_agentic_ai_generic | AI-driven |
| paper-2244 | Revolutionizing Network Management: The Journey to AI-native Autonomy | llm_agentic_ai_generic | AI-native |
| paper-2668 | Toward Practical Operation of Deep Reinforcement Learning Agents in Real-World Network Management at Open RAN Edges | agent | Agents |
| paper-107 | Design and analysis of distributed load management: Mobile agent based probabilistic model and fuzzy integrated model | agent | agent |
| paper-1385 | Techie: Tackling Video Prefetching at Edge Networks as POMDP Via an Intrinsically Motivated RL Agent | agent | Agent |
| paper-1497 | Management of Safety-Critical AI Services in the Compute Continuum | llm_agentic_ai_generic | AI Services |
| paper-1956 | Smart AI Applications: Integrating Raspberry Pi 3 with NLP for Edge Computing | llm_agentic_ai_generic | NLP |
| paper-1995 | An Intelli UbiAware: An Intelligent Autonomic Framework for Context-Aware Ubiquitous Computing and Smart Resource Manage | llm_agentic_ai_generic | Autonomic |
| paper-2343 | Air Pollutant Traceability Based on Federated Learning of Edge Intelligent Perception Agents | agent | Agents |
| paper-2619 | Autonomous digital twin framework for gas turbine combined cycle control loops: Comparative study of proportional-integr | agent | agents |
| paper-262 | Orchestrating heterogeneous devices and ai services as virtual sensors for secure cloud-based iot applications† | llm_agentic_ai_generic | ai services |
| paper-264 | Task scheduling, resource provisioning, and load balancing on scientific workflows using parallel SARSA reinforcement le | agent | agents |
| paper-680 | Distributed Task Allocation in Network of Agents Based on Ant Colony Foraging Behavior | agent | Agents |
| paper-730 | Privacy-Aware Intelligent Healthcare Services with Federated Learning Architecture and Reinforcement Learning Agent | agent | Agent |
| paper-178 | A cloud resource management framework for multiple online scientific workflows using cooperative reinforcement learning  | agent | agents |
| paper-179 | Online scheduling of dependent tasks of cloud’s workflows to enhance resource utilization and reduce the makespan using  | agent | agents |
| paper-2126 | Design of an Iterative AI-Driven Latency Prediction and QoS-Aware Task Scheduling in Mobile Edge Computing: A Federated  | llm_agentic_ai_generic | AI-Driven |
| paper-2159 | Dynamic Task Scheduling and Smart Caching in Fog-Cloud Architectures Using Advantage Actor-Critic Agents | agent | Agents |
| paper-302 | Development of QoS-aware agents with reinforcement learning for autoscaling of microservices on the cloud | agent | agents |
| paper-676 | Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management | agent | Agents |
| paper-1149 | Mobile Agents-Based Framework for Dynamic Resource Allocation in Cloud Computing | agent | Agents |
| paper-123 | Autonomic decentralized microservices: The Gru approach and its evaluation | llm_agentic_ai_generic | Autonomic |
| paper-1405 | A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks | llm_agentic_ai_generic | RAG |
| paper-1504 | A review of state-of-the-art techniques for large language model compression | llm_agentic_ai_generic | large language model, language model |
| paper-1583 | Research on Key Technologies of Intelligent Review Based on Large Language Model Business Scenarios | llm_agentic_ai_generic | Large Language Model, Language Model |
| paper-172 | FIPA-based reference architecture for efficient discovery and selection of appropriate cloud service using cloud ontolog | llm_agentic_ai_generic | FIPA |
| paper-2403 | Generative AI for the Internet of Vehicles: A Review of Advances in Training, Decision-Making, and Security | llm_agentic_ai_generic | Generative AI |
| paper-2466 | A Review on Edge Large Language Models: Design, Execution, and Applications | llm_agentic_ai_generic | Large Language Models, Language Models |
| paper-2808 | Bio-inspired AI Algorithms for Autonomous Agents: Revolutionizing Decision-Making, Resource Allocation, and Adaptability | agent | Agents |
| paper-292 | Mobile agent-based service migration in mobile edge computing | agent | agent |
| paper-2949 | Explainable AI and Multi-Agent Systems for Energy Management in IoT-Edge Environments: A State of the Art Review | mas | Multi-Agent, Agent |
| paper-325 | An agent-based model for resource provisioning and task scheduling in cloud computing using DRL | agent | agent |
| paper-2050 | Demonstrating Smart Scaling of AI-Services for Future Networks | llm_agentic_ai_generic | AI-Services |
| paper-1549 | Partial Decentralized Gossip-Based Federated Learning Protocol for Heterogeneous IoT Multi-Agents Systems | mas | Multi-Agents, Agents |
| paper-1594 | AI-Enabled Circular Supply Chain Framework for Sustainable Returns Management: A Multi-Technology Integration Approach | llm_agentic_ai_generic | AI-Enabled |
| paper-1751 | Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS | agent | Agents |
| paper-1998 | Nexus Search: A Scalable and Distributed Search Engine Powered by Open Source LLMs | llm_agentic_ai_generic | LLMs |
| paper-2073 | AI-Driven Hybrid Edge-Cloud Architecture for Real-Time Big Data Analytics and Scalable Communication in Retail Supply Ch | llm_agentic_ai_generic | AI-Driven |
| paper-2154 | Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches | agent | Agent, AI Agent |
| paper-2580 | AI-Enabled Vehicular Data Offloading for Sustainable Smart Cities: Taxonomy, KPI Models, and Open Challenges | llm_agentic_ai_generic | AI-Enabled |
| paper-2806 | Agent AI-as-a-Service (AIaaS) in Multi-Cloud Environments: Challenges, Opportunities, and the Future of Autonomous AI-Dr | agent | Agent, Agent AI, AI-Driven |
| paper-2921 | Service reliability of intelligent computing cluster systems for large language models | llm_agentic_ai_generic | large language models, language models |
| paper-984 | Generative Artificial Intelligence for Biomedical and Smart Health Informatics | llm_agentic_ai_generic | Generative Artificial Intelligence |

_…and 196 more false positives._
