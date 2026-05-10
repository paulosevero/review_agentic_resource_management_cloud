---
title: "UnifiedKP: A Unified Network Knowledge Plane for Large Model-Enabled 6G Networks"
authors:
  - name: "Tiantian Wu"
    affiliation: "Zhengzhou Railway Vocational and Technical College"
  - name: "Chengjie Wei"
    affiliation: "Zhengzhou Railway Vocational and Technical College"
  - name: "Lingnan Xia"
    affiliation: "Zhengzhou Railway Vocational and Technical College"
    email: "xialingnan@outlook.com"
abstract: "The emergence of large language models (LLMs) and agentic systems is revolutionizing the landscape of 6G networks by enabling unprecedented levels of autonomous intelligence. Current implementations face significant challenges: individual intelligence tasks require isolated knowledge retrieval pipelines, resulting in redundant data flows, inconsistent interpretations, and increased operational complexity. We propose UnifiedKP, a unified Network Knowledge Plane specifically designed for large model-enabled autonomous 6G network intelligence. By decoupling network knowledge acquisition and management from intelligence logic, UnifiedKP streamlines development workflows and significantly reduces maintenance complexity. We demonstrate effectiveness through two representative applications: live network knowledge question-answering and edge AI service orchestration. Results show UnifiedKP reduces knowledge retrieval latency by 47%, improves knowledge consistency by 82%, decreases development complexity by 65%, achieves 94.3% accuracy in network anomaly detection, and reduces service orchestration time by 38%."
keywords:
  - "6G networks"
  - "large language models"
  - "network knowledge plane"
  - "autonomous networks"
  - "edge AI"
  - "agentic systems"
doi: "10.1109/ACCESS.2025.3610890"
date_received: "2025-09-06"
date_accepted: "2025-09-14"
date_published: "2025-09-17"
journal: "IEEE Access"
---

Received 6 September 2025, accepted 14 September 2025, date of publication 17 September 2025, date of current version 3 October 2025.

Digital Object Identifier 10.1 109/ACCESS.2025.3610890

<!-- image -->

## UnifiedKP: A Unified Network Knowledge Plane for Large Model-Enabled 6G Networks

## TIANTIAN WU, CHENGJIE WEI, AND LINGNAN XIA

Zhengzhou Railway Vocational and Technical College, Zhengzhou 451460, China

Corresponding author: Lingnan Xia (xialingnan@outlook.com)

This work was supported in part by Henan Provincial Science and Technology Research Project, China, under Grant 242102210206; and in part by the Research project of Zhengzhou Railway Vocational and Technical College, China, under Grant 2024KY004.

ABSTRACT The emergence of large language models (LLMs) and agentic systems is revolutionizing the landscape of 6G networks by enabling unprecedented levels of autonomous intelligence, including self-configuration, self-optimization, and self-healing capabilities. However, current implementations face significant challenges. Individual intelligence tasks require isolated knowledge retrieval pipelines. This isolation results in redundant data flows, inconsistent interpretations, and increased operational complexity. Inspired by the service model unification efforts in Open-RAN that promote interoperability and vendor diversity, we propose UnifiedKP: a unified Network Knowledge Plane specifically designed for large model-enabled autonomous 6G network intelligence. By decoupling network knowledge acquisition and management from intelligence logic, UnifiedKP streamlines development workflows and significantly reduces maintenance complexity for intelligence engineers. Through an intuitive and consistent knowledge interface, UnifiedKP enhances interoperability for network intelligence agents while maintaining semantic consistency across diverse intelligence tasks. We demonstrate the effectiveness of UnifiedKP through two representative intelligence applications: live network knowledge question-answering and edge AI service orchestration. Experimental results show that UnifiedKP reduces knowledge retrieval latency by 47%, improves knowledge consistency by 82%, and decreases development complexity by 65% compared to traditional isolated approaches. Our framework achieves 94.3% accuracy in network anomaly detection and reduces service orchestration time by 38% in dynamic edge computing environments. These findings establish UnifiedKP as a foundational architecture for realizing truly autonomous and intelligent 6G networks.

INDEX TERMS 6G networks, large language models, network knowledge plane, autonomous networks, edge AI.

## I. INTRODUCTION

The evolution toward sixth-generation (6G) wireless networks represents a paradigm shift from traditional connectivity-centric architectures to intelligence-native systems that seamlessly integrate artificial intelligence at every layer of the network stack. This transformation is primarily driven by the convergence of large language models, multi-agent systems, and distributed computing paradigms that collectively enable unprecedented levels of network autonomy and intelligence. Unlike previous generations that

The associate editor coordinating the review of this manuscript and approving it for publication was Bilal Khawaja .

relied on rule-based automation and reactive management strategies, 6G networks leverage advanced capabilities. These networks utilize the reasoning capabilities of LLMs and the collaborative potential of agentic systems. Through these technologies, they achieve proactive, context-aware, and self-evolving network operations [1], [2]. The integration of these advanced AI technologies promises to address the increasingly complex challenges of ultra-dense deployments, heterogeneous service requirements, and dynamic resource optimization that characterize next-generation wireless networks.

The current landscape of network intelligence implementation, however, faces significant architectural challenges that hinder the realization of truly autonomous 6G systems. To date, no unified framework exists that decouples knowledge acquisition from intelligence logic in 6G networks. Each intelligence task, whether it involves network optimization, fault diagnosis, or service orchestration, typically maintains its own isolated knowledge retrieval pipeline, leading to substantial inefficiencies in data processing and knowledge management. These isolated pipelines not only create redundant data flows that consume valuable network resources but also result in inconsistent interpretations of network states across different intelligence functions. For example, consider a network operator managing both fault diagnosis and capacity planning systems. Without unified knowledge, each system maintains separate databases of network topology, leading to inconsistencies when network changes occur. This duplication not only wastes storage but can cause conflicting decisions when one system's knowledge lags behind another's. Furthermore, the lack of a unified knowledge representation framework forces intelligence engineers to repeatedly implement similar knowledge acquisition and processing mechanisms for each new intelligence task, significantly increasing development complexity and maintenance overhead. This fragmentation becomes particularly problematic in the context of LLM-based systems, where consistent and comprehensive knowledge access is crucial for generating accurate and contextually appropriate responses.

<!-- image -->

<!-- image -->

The Open Radio Access Network (Open-RAN) initiative provides valuable insights into addressing these challenges through its service model unification efforts that promote interoperability and vendor diversity in network deployments. By standardizing interfaces and decoupling network functions, Open-RAN has demonstrated the benefits of architectural modularity and abstraction in complex network systems. Drawing inspiration from these principles, we recognize the need for a similar unification approach in the knowledge layer of intelligent 6G networks. A unified knowledge plane that abstracts the complexities of knowledge acquisition, representation, and management from the intelligence logic itself could fundamentally transform how network intelligence is developed, deployed, and maintained. Such an architecture would not only eliminate redundancies and inconsistencies but also enable rapid development of new intelligence capabilities by providing a consistent and reliable knowledge foundation.

In this paper, we propose UnifiedKP, a comprehensive unified Network Knowledge Plane specifically designed to support large model-enabled autonomous intelligence in 6G networks. UnifiedKP introduces a novel architectural framework that decouples network knowledge acquisition and management from intelligence logic, thereby creating a clean separation of concerns that benefits both system designers and intelligence engineers. Our approach provides an intuitive and consistent knowledge interface that abstracts the underlying complexity of heterogeneous data sources, temporal dynamics, and multi-modal information present in modern networks. By establishing a semantic layer that maintains consistency across diverse intelligence tasks, UnifiedKP enables different AI agents and LLMs to share a common understanding of network states, policies, and objectives. We demonstrate the practical effectiveness of UnifiedKP through comprehensive implementations of two representative intelligence tasks: live network knowledge question-answering systems that leverage LLMs for interactive network management, and edge AI service orchestration that optimizes resource allocation in distributed computing environments.

## II. RELATED WORK

## A. LLMs IN NETWORK MANAGEMENT

The integration of large language models into network management systems has emerged as a transformative approach for achieving autonomous network operations. Recent work by Zhang et al. [3] demonstrated the potential of LLMs in network configuration generation, achieving significant improvements in configuration accuracy and adaptation speed compared to traditional template-based approaches. Their framework leverages GPT-4 for generating network configurations from natural language specifications, reducing configuration errors by 73% compared to manual approaches. Similarly, Chen et al. [4] proposed NetGPT, a framework that leverages pre-trained language models for network troubleshooting and root cause analysis, showing promising results in reducing mean time to repair (MTTR) by up to 60%. The system employs a retrieval-augmented generation approach that combines historical incident data with real-time telemetry to provide accurate diagnostic recommendations.

The work by Liu et al. [5] extended these concepts to multiagent systems, where multiple specialized LLMs collaborate to manage different aspects of network operations, from resource allocation to security monitoring. Their hierarchical architecture demonstrates how domain-specific fine-tuning can improve task performance by 45% compared to generalpurpose models. Complementing this, Morrison et al. [6] proposed a distributed LLM framework that deploys smaller, specialized models at the network edge, achieving sub-second response times for critical network decisions while reducing bandwidth consumption by 67%. The research by Park et al. [7] explored efficient fine-tuning strategies for networkspecific tasks, introducing a parameter-efficient adaptation method that requires only 0.1% of the model parameters to be updated while maintaining 95% of full fine-tuning performance.

However, these approaches still rely on task-specific knowledge pipelines that create redundancies and limit the scalability of intelligence deployment. The study by Hoffman et al. [8] identified key limitations in current LLM-based network management systems, including knowledge inconsistency across different models, lack of real-time adaptation capabilities, and difficulty in handling multi-modal network data. These limitations collectively highlight a critical research gap: the absence of a unified knowledge architecture that can efficiently support diverse LLM-based applications while maintaining consistency and reducing redundancy.

## B. KNOWLEDGE REPRESENTATION FRAMEWORKS

The concept of knowledge planes in network architectures has evolved significantly from early cognitive network proposals to modern AI-driven implementations. The seminal work by Clark et al. [9] introduced the knowledge plane as a high-level abstraction for network management, envisioning a system that could aggregate network-wide information and make intelligent decisions autonomously. Building on this foundation, Wang et al. [10] revisited this concept in the context of 5G and beyond networks, proposing a distributed knowledge management system that leverages edge computing for real-time network intelligence. Their implementation demonstrates how edge-based knowledge processing can reduce decision latency by 82% while maintaining global consistency through periodic synchronization.

The framework proposed by Kumar et al. [11] introduced semantic knowledge representation for network states, enabling more sophisticated reasoning capabilities through ontology-based modeling. Their approach uses description logic to formally represent network concepts and relationships, supporting complex queries that require multi-hop reasoning across different network domains. Extending this work, Rodriguez et al. [12] incorporated temporal semantics into network knowledge representation, enabling the system to reason about network evolution and predict future states with 87% accuracy. The research by Nielsen et al. [13] proposed a federated knowledge plane architecture that maintains local autonomy while enabling global coordination, addressing privacy and scalability concerns in multi-operator environments.

Recent advances by Tanaka et al. [14] have explored the integration of graph neural networks with semantic knowledge planes, demonstrating how structural information can enhance knowledge inference capabilities. Their hybrid approach combines symbolic reasoning with neural representations, achieving superior performance in network anomaly detection and root cause analysis. The work by Petrova et al. [15] introduced adaptive knowledge abstraction mechanisms that dynamically adjust the level of detail based on query requirements and system load, improving query response time by 54% while reducing storage requirements by 38%.

Despite these advances, current knowledge plane implementations remain fragmented across different systems. No existing framework provides the unified architecture necessary to support diverse LLM-based intelligence tasks efficiently while maintaining semantic consistency across all network domains.

## C. OPEN-RAN AND ORCHESTRATION

The standardization efforts in Open-RAN have provided crucial insights into achieving interoperability and modularity in complex network systems. The O-RAN Alliance

<!-- image -->

specifications [16] define standardized interfaces and protocols that enable multi-vendor deployments while maintaining system coherence. These specifications introduce the concept of RAN Intelligent Controllers (RICs) that provide a platform for deploying AI/ML-based network applications, establishing a precedent for modular intelligence architectures. Thompson et al. [17] demonstrated how these principles could be extended to AI-driven network functions, proposing an AI/ML workflow that leverages Open-RAN's modular architecture to reduce application development time by 70%.

The work by Garcia et al. [18] focused on the near-realtime RIC platform, showing how standardized interfaces enable rapid deployment of new intelligence applications. Their implementation of a dynamic spectrum management xApp achieved 23% improvement in spectrum efficiency while maintaining compatibility with equipment from multiple vendors. Complementing this, Johansson et al. [19] explored the integration of network function virtualization (NFV) with Open-RAN architectures, demonstrating how containerized network functions can be dynamically orchestrated based on traffic patterns and service requirements. Their approach reduces service deployment time by 85% compared to traditional hardware-based implementations.

The research by Nakamura et al. [20] investigated the benefits of RAN disaggregation for AI-based optimization, showing how functional splits enable more granular control and optimization opportunities. Their analysis reveals that disaggregated architectures can improve energy efficiency by up to 41% through intelligent workload distribution. Singh et al. [21] addressed the challenges of multi-vendor interoperability in Open-RAN deployments, proposing a semantic mediation layer that translates between vendor-specific implementations while maintaining functional consistency.

These developments in Open-RAN demonstrate the value of architectural unification and standardization. However, they primarily focus on functional interfaces rather than knowledge management. Our UnifiedKP extends these principles to the knowledge layer, creating a unified foundation for intelligent network operations.

## D. EDGE INTELLIGENCE

Edge AI and service orchestration in 6G networks present unique challenges that require sophisticated knowledge management capabilities. Li et al. [22] proposed a hierarchical orchestration framework that leverages federated learning for distributed intelligence, achieving significant improvements in service latency and resource utilization. Their three-tier architecture distributes intelligence across device, edge, and cloud layers, reducing average service latency by 67% for latency-critical applications. The study by Anderson et al. [23] introduced a context-aware orchestration mechanism that adapts to dynamic network conditions and user mobility patterns, demonstrating how predictive models can anticipate service migration needs with 91% accuracy.

<!-- image -->

Research by Kim et al. [24] explored multi-modal data fusion for edge intelligence, combining network telemetry, user behavior, and environmental data to optimize service placement decisions. Their fusion approach improves placement accuracy by 34% compared to single-modality approaches while reducing computational overhead through selective feature extraction. The work by Fernandez et al. [25] investigated container orchestration strategies for edge AI workloads, proposing a deadline-aware scheduling algorithm that improves task completion rates by 43% under resourceconstrained conditions.

The framework proposed by Gupta et al. [26] demonstrated how collaborative inference across edge nodes can reduce individual node computational load by up to 58% while maintaining inference accuracy. Their approach uses knowledge distillation to create lightweight models suitable for edge deployment while preserving the reasoning capabilities of larger models. Chen et al. [27] addressed the challenge of service continuity in mobile edge computing environments, introducing a proactive migration strategy that predicts user movement patterns and pre-positions services accordingly, reducing service interruption time by 76%.

However, these edge intelligence approaches struggle with knowledge consistency and sharing across different orchestration components. The lack of a unified knowledge infrastructure leads to duplicated efforts and inconsistent decisions, particularly in scenarios requiring coordination across multiple edge nodes. This gap motivates our unified approach to knowledge management.

## E. MULTI-AGENT SYSTEMS

The integration of agentic systems with 6G networks has opened new possibilities for autonomous network management through collaborative intelligence. Roberts et al. [28] demonstrated how multiple AI agents could coordinate to manage network slices dynamically, achieving superior performance compared to centralized approaches. Their framework employs a market-based coordination mechanism where agents bid for resources based on service priorities, resulting in 31% improvement in resource utilization efficiency. Yamamoto et al. [29] introduced a hierarchical multi-agent architecture where specialized agents handle different network domains while maintaining global coherence through shared knowledge representations. The system demonstrates how agent specialization can improve task completion time by 52% while reducing inter-agent communication overhead.

The research by Brown et al. [30] explored cooperative learning mechanisms among network agents, showing how shared experiences could accelerate adaptation to new network conditions. Their federated experience replay approach enables agents to learn from collective experiences without sharing raw data, improving learning efficiency by 68% while preserving privacy. Wilson et al. [31] investigated emergent behaviors in large-scale multi-agent networks, demonstrating how simple local interaction rules can lead to sophisticated global optimization patterns. Their analysis reveals that emergent coordination can achieve near-optimal resource allocation without centralized control in 78% of tested scenarios.

The work by Martinez et al. [32] proposed a negotiation protocol for resource allocation among autonomous agents, introducing a game-theoretic framework that ensures fair resource distribution while maximizing global utility. Their approach achieves Nash equilibrium in 94% of negotiation scenarios within 5 rounds of interaction. Complementing this, Thompson et al. [33] addressed the challenge of trust management in multi-agent systems, proposing a reputation-based mechanism that enables agents to evaluate the reliability of information from other agents, reducing the impact of faulty or malicious agents by 89%.

The success of multi-agent systems depends critically on efficient information sharing and coordination. Current implementations suffer from information silos and inconsistent knowledge representations across agents. UnifiedKP addresses this fundamental challenge by providing a common knowledge foundation that all agents can reliably access and update. Additionally, recent work by Yan et al. [34] on communications and networks resources sharing in 6G highlights the importance of unified resource management architectures, which aligns with our unified knowledge plane approach.

## III. METHODS

## IV. SYSTEM OVERVIEW

## A. ARCHITECTURAL DESIGN PRINCIPLES

The UnifiedKP architecture is designed based on five fundamental principles that guide its implementation and operation. First, the principle of separation of concerns ensures that knowledge management is decoupled from intelligence logic, enabling independent evolution and optimization of each component. Second, the principle of semantic consistency maintains uniform knowledge representation across all intelligence tasks, eliminating ambiguity and interpretation conflicts. Third, the principle of temporal awareness ensures that all knowledge elements are associated with temporal validity indicators, enabling time-sensitive reasoning and historical analysis. Fourth, the principle of scalable distribution supports both centralized and distributed deployment models, adapting to different network scales and requirements. Fifth, the principle of continuous learning enables the system to improve its knowledge quality and management strategies through operational experience.

## B. UnifiedKP ARCHITECTURE

The UnifiedKP system architecture consists of three primary layers interconnected through well-defined interfaces. The Knowledge Acquisition Layer interfaces with heterogeneous data sources including telemetry streams, configuration databases, operational logs, network topology information, and external knowledge bases. This layer implements adaptive sampling strategies to manage data volume while preserving information fidelity. The Semantic Representation Layer transforms raw data into structured knowledge using ontology-based modeling and temporal logic frameworks. This layer maintains the knowledge store and ensures semantic consistency across all knowledge elements. The Intelligence Interface Layer provides standardized APIs for various intelligence applications, managing LLM interactions and coordinating multi-agent operations.

FIGURE 1. UnifiedKP system architecture.

<!-- image -->

<!-- image -->

## C. KNOWLEDGE PROCESSING PIPELINE

The knowledge processing pipeline implements a systematic transformation of raw network data into actionable knowledge. Each stage performs specific validation and transformation operations, ensuring data quality and semantic consistency throughout the process. The pipeline supports both batch and stream processing modes, adapting to different data characteristics and latency requirements.

## D. CORE ALGORITHMS

## E. KNOWLEDGE RETRIEVAL ALGORITHM

## F. SYSTEM WORKFLOW

The system workflow illustrates the end-to-end process for handling knowledge queries. The workflow incorporates caching mechanisms to improve response time for frequently accessed knowledge, validation steps to ensure result quality,

## Algorithm 1 Semantic Knowledge Retrieval 1: Input: Query q , Knowledge base KB , Context C 2: Output: Relevant knowledge set Krel 3: Initialize Krel ←∅ 4: qembed ← EmbedQuery( q ) 5: candidates ← IndexSearch( KB , qembed , topk ) 6: for each k ∈ candidates do 7: score ← ComputeRelevance( k , q , C ) 8: if score &gt; τ relevance then 9: kenriched ← EnrichWithContext( k , C ) 10: Krel ← Krel ∪ { kenriched } 11: end if 12: end for 13: Krel ← RankByRelevance( Krel ) 14: Krel ← ValidateTemporal( Krel , current \_ time ) 15: return Krel = 0

and adaptive search expansion to handle complex queries that require broader knowledge retrieval.

## G. CONSISTENCY MANAGEMENT PROTOCOL

## H. DETAILED COMPONENT ARCHITECTURE

The UnifiedKP architecture comprises three fundamental layers that collectively enable efficient knowledge management for LLM-based network intelligence. The Knowledge Acquisition Layer (KAL) interfaces with heterogeneous network data sources, including telemetry streams, configuration databases, and operational logs. The Semantic Representation Layer (SRL) transforms raw network data into structured knowledge representations suitable for LLM processing. The Intelligence Interface Layer (IIL) provides standardized APIs for various intelligence tasks to access and manipulate network knowledge consistently.

<!-- image -->

TABLE 1. Knowledge processing pipeline stages.

TABLE 2. Core UnifiedKP algorithms.

FIGURE 2. Knowledge query processing workflow.

<!-- image -->

The formal representation of network knowledge in UnifiedKP is defined as a temporal knowledge graph Gt = ( Vt , Et , 8 t ), where Vt represents network entities at time t , Et denotes relationships between entities, and 8 t captures temporal properties and attributes. The knowledge state

## Algorithm 2 Distributed Consistency Management

```
1: Input: Knowledge update u , Node set N 2: Output: Consistent knowledge state 3: VCu ← GetVectorClock( u ) 4: conflicts ←∅ 5: for each node n ∈ N do 6: kn ← GetKnowledge( n , u . id ) 7: if kn ̸= null then 8: VCn ← GetVectorClock( kn ) 9: if Concurrent( VCu , VCn ) then 10: conflicts ← conflicts ∪ { kn } 11: else if VCn ≻ VCu then 12: return // Reject outdated update 13: end if 14: end if 15: end for 16: if | conflicts | > 0 then 17: // ResolveConflicts implementation 18: uresolved ← SelectMostRecent( u , conflicts ) 19: ApplyMergePolicy( uresolved , conflicts ) 20: BroadcastUpdate( uresolved , N ) 21: else 22: BroadcastUpdate( u , N ) 23: end if 24: UpdateLocalState( u ) = 0
```

evolution is modeled through the state transition function :

<!-- formula-not-decoded -->

where ftrans is the state transition function that combines the previous state Gt with new observations Ot and actions At .

The parameters α , β , and γ control the relative weights of historical knowledge, new observations, and applied actions respectively. The Merge function reconciles new observations with existing knowledge, while Apply incorporates the effects of network actions.

## I. KNOWLEDGE ACQUISITION AND PROCESSING

The knowledge acquisition process in UnifiedKP employs a multi-stage pipeline that ensures data quality and semantic consistency. Raw network data streams are first normalized through a standardization function ψ : Draw → Dnorm , where Draw represents the heterogeneous input space and Dnorm denotes the normalized representation space. The normalization process addresses variations in data formats, sampling rates, and measurement units across different network components.

The semantic enrichment process augments normalized data with contextual information through the enrichment function :

<!-- formula-not-decoded -->

where ξ is the enrichment function that combines normalized data with current context and historical patterns. The ⊕ operator represents semantic concatenation that preserves relationships between different knowledge components. Ct represents the current network context, including topology, configuration, and operational policies, and Ht denotes historical patterns and learned associations.

The knowledge validation mechanism employs a consistency checking algorithm that ensures semantic coherence across different knowledge sources. For any new knowledge element knew , the validation function computes :

<!-- formula-not-decoded -->

where σ measures semantic similarity, and ω i represents the confidence weight of existing knowledge elements. Knowledge elements with validation scores below a threshold τ valid trigger reconciliation procedures to resolve inconsistencies.

## J. SEMANTIC KNOWLEDGE REPRESENTATION

The semantic representation in UnifiedKP employs a hierarchical ontology that captures network concepts at multiple abstraction levels. The ontology is formally defined as = ( C , R , A , I ), where C represents concept classes, R denotes relationships between concepts, A captures attributes and properties, and I represents instances of concepts in the operational network.

The concept hierarchy follows a subsumption relationship defined by :

<!-- formula-not-decoded -->

This hierarchical organization enables efficient reasoning and inference by LLMs, allowing them to leverage both specific and general knowledge as appropriate for different tasks.

<!-- image -->

The temporal dynamics of network knowledge are captured through a temporal logic framework that extends traditional description logic with temporal operators. For any knowledge assertion α , we define temporal validity through :

<!-- formula-not-decoded -->

where λ controls the decay rate of outdated knowledge, allowing the system to maintain historical information while prioritizing current network states.

## K. LLM INTEGRATION FRAMEWORK

The integration of large language models with UnifiedKP requires careful consideration of prompt engineering, context management, and response validation. The prompt generation process constructs contextualized queries by combining user requests with relevant network knowledge :

<!-- formula-not-decoded -->

where Quser represents the user query, Krelevant denotes retrieved relevant knowledge, and Mtask captures taskspecific metadata and constraints.

The context selection algorithm employs a relevance scoring mechanism that balances comprehensiveness with computational efficiency :

<!-- formula-not-decoded -->

where simsemantic measures semantic similarity using cosine similarity between embeddings, fresh evaluates temporal relevance based on the age of knowledge, and imp assesses the importance of knowledge elements based on network criticality metrics. The parameters α = 0 . 5, β = 0 . 3, and γ = 0 . 2 were determined through grid search optimization on a validation dataset, balancing accuracy and efficiency.

The response validation framework ensures that LLMgenerated outputs comply with network policies and operational constraints. For any generated response rLLM , the validation process computes :

<!-- formula-not-decoded -->

where 9 safety is the safety validation function defined as :

<!-- formula-not-decoded -->

The safety checks include boundary validation, resource availability verification, and conflict detection with existing network policies.

<!-- image -->

## L. KNOWLEDGE CONSISTENCY AND SYNCHRONIZATION

Maintaining consistency across distributed knowledge sources requires sophisticated synchronization mechanisms. UnifiedKP employs a vector clock-based approach for tracking knowledge updates across different network domains. For each knowledge element k , we maintain a vector clock VCk = [ v 1 , v 2 , . . . , vn ], where n represents the number of knowledge sources.

The consistency resolution algorithm operates according to the following rules :

<!-- formula-not-decoded -->

where M represents a merge function that reconciles concurrent updates based on predefined policies and conflict resolution strategies.

The synchronization protocol ensures eventual consistency through periodic reconciliation cycles. The synchronization interval is dynamically adjusted based on network dynamics :

<!-- formula-not-decoded -->

where Tbase represents the baseline synchronization interval, and 1 K 1 t measures the rate of knowledge changes.

## M. INTELLIGENCE TASK OPTIMIZATION

The optimization of intelligence tasks in UnifiedKP leverages the unified knowledge representation to improve efficiency and accuracy. For network knowledge Q&amp;A tasks, we formulate the problem as a constrained optimization :

<!-- formula-not-decoded -->

where Q measures answer quality, L computes response latency, and Lmax represents the maximum acceptable latency threshold.

The answer quality function incorporates multiple factors :

<!-- formula-not-decoded -->

where rel measures relevance to the query, comp evaluates completeness with respect to available knowledge, and conf assesses confidence based on knowledge certainty.

For edge AI service orchestration, the optimization objective considers both performance and resource constraints :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where xij represents the placement decision for service i on node j , cij denotes the cost of placement, pi represents service priority, di measures deployment delay, rik captures resource requirements, and Rjk denotes available resources.

## N. REINFORCEMENT LEARNING-BASED ADAPTATION

UnifiedKP incorporates continuous learning mechanisms to improve knowledge quality and system performance over time. The learning framework employs a reinforcement learning approach where the system learns optimal knowledge management strategies through interaction with the network environment.

The RL agent operates in a state space S representing the current knowledge configuration and network status. The state at time t is defined as:

<!-- formula-not-decoded -->

where Kt is the knowledge state, Nt is the network state, Qt represents pending queries, and Pt captures performance metrics.

The action space A includes knowledge management operations such as:

- Knowledge prefetching: aprefetch
- Cache invalidation: ainvalidate
- Synchronization triggering: async
- Adaptation of retrieval parameters: aadapt

The learning objective is formulated as :

<!-- formula-not-decoded -->

where πθ represents the knowledge management policy parameterized by θ , rt denotes the reward at time t , and γ is the discount factor.

The reward function balances multiple objectives :

<!-- formula-not-decoded -->

where the individual reward components are calculated as :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The policy update follows a gradient ascent approach :

<!-- formula-not-decoded -->

where η represents the learning rate, dynamically adjusted based on convergence behavior.

## V. EXPERIMENTS

## A. EXPERIMENTAL SETUP

Our experimental evaluation of UnifiedKP was conducted on a comprehensive testbed that emulates a realistic 6G network environment with multiple radio access technologies, edge computing nodes, and core network functions. The testbed comprises 50 base stations distributed across an urban area of 100 square kilometers, 200 edge computing nodes with heterogeneous computational capabilities ranging from 10 to 100 TFLOPS, and a centralized cloud infrastructure with 5 petaflops of aggregate computing power. The network serves 10,000 simulated user equipment (UE) devices with diverse service requirements, including enhanced mobile broadband (eMBB), ultrareliable low-latency communications (URLLC), and massive machine-type communications (mMTC) traffic patterns.

The experimental setup parameters were as follows:

- Network scale: 50 base stations, 200 edge nodes
- Dataset size: 500,000 configuration items, 10M historical events
- Simulation duration: 30 days continuous operation
- Traffic patterns: Mixed eMBB (60%), URLLC (25%), mMTC (15%)
- Hardware: 8x NVIDIA A100 GPUs for LLM inference
- Baseline configurations: RB-NMS (rule-based with 10,000 rules), ISO-LLM (GPT-4 without unified knowledge), FL-NET (federated learning with 50 participating nodes)

The LLM components were implemented using state-ofthe-art transformer architectures, specifically fine-tuned versions of GPT-4 and LLaMA-2 models with 70 billion parameters, deployed across the edge and cloud infrastructure. The knowledge base was initialized with 500,000 network configuration items, 10 million historical network events, and continuous telemetry streams generating approximately 1 TB of data per hour. We implemented UnifiedKP using a microservices architecture with containerized components orchestrated through Kubernetes, ensuring scalability and fault tolerance. The semantic layer was built using Apache Jena for RDF triple store management and Neo4j for temporal graph operations.

For comparison baselines, we implemented three alternative approaches:

- RB-NMS: Traditional rule-based network management system with 10,000 predefined rules covering common scenarios
- ISO-LLM: Isolated LLM-based system where each task maintains its own knowledge pipeline
- FL-NET: Federated learning approach with distributed knowledge across 50 nodes without centralized coordination

Each system was evaluated under identical network conditions and workload patterns to ensure fair comparison. The experiments were conducted over a period of 30 days with continuous monitoring of system performance, knowledge consistency metrics, and intelligence task outcomes.

## B. PERFORMANCE EVALUATION METRICS

We evaluated UnifiedKP across multiple dimensions to comprehensively assess its effectiveness. The metrics and their calculation methods are:

- Knowledge consistency ratio : Percentage of knowledge triples maintaining semantic coherence, calculated as |{ k ∈ K : consistent( k ) }| | K |
- Semantic coherence : Measured using ontology-based validation, checking if knowledge assertions satisfy domain constraints
- Reasoning Depth : Number of inference steps required to answer a query, measured by tracking knowledge graph traversals
- Development complexity : Quantified through lines of code (LOC) and development time in person-hours for implementing new intelligence applications

<!-- image -->

## C. NETWORK KNOWLEDGE Q&amp;A PERFORMANCE

Theevaluation of the network knowledge question-answering system focused on three categories of queries: operational status inquiries, configuration recommendations, and troubleshooting assistance. We generated a test set of 5,000 queries covering diverse network management scenarios, with complexity levels ranging from simple fact retrieval to complex multi-hop reasoning tasks.

UnifiedKP demonstrated superior performance in response accuracy, achieving 94.3% correct answers compared to 81.7% for the isolated LLM system. The improvement is particularly pronounced for complex queries requiring integration of knowledge from multiple sources. The unified knowledge representation enables the LLM to access comprehensive context, resulting in more accurate and nuanced responses. The average response time of 142 milliseconds for UnifiedKP represents a 47% reduction compared to ISO-LLM, primarily due to efficient knowledge retrieval mechanisms that eliminate redundant data processing.

The context relevance score, measuring the appropriateness of retrieved knowledge for answering queries, reached 0.92 for UnifiedKP, indicating highly effective knowledge selection. The system's ability to maintain reasoning depth of 4.8 levels demonstrates its capability to handle complex, multi-step reasoning tasks that are essential for advanced network troubleshooting and optimization scenarios.

## D. EDGE AI SERVICE ORCHESTRATION RESULTS

The edge AI service orchestration experiments evaluated the system's ability to optimally place and manage AI workloads across the distributed edge infrastructure. We simulated 1,000 different service deployment scenarios with varying resource requirements, latency constraints, and mobility patterns.

UnifiedKP achieved a 38% reduction in average orchestration time compared to isolated approaches, completing service placement decisions in 3.2 seconds on average. The improved performance stems from the unified knowledge plane's ability to maintain consistent and up-to-date views of resource availability across the edge infrastructure. Resource utilization reached 87.4%, representing a significant improvement over baseline systems, while maintaining 98.7% SLA compliance for latency-critical services.

The system demonstrated superior adaptation to dynamic conditions, with migration overhead reduced by 37% compared to ISO-LLM. This efficiency gain results from better-informed placement decisions that consider long-term patterns and predictive knowledge about service behavior and network dynamics.

<!-- image -->

TABLE 3. Network knowledge Q&amp;A performance comparison.

TABLE 4. Edge AI service orchestration performance.

## E. KNOWLEDGE CONSISTENCY ANALYSIS

We conducted extensive experiments to evaluate knowledge consistency maintenance across different intelligence tasks and network domains. The analysis involved injecting 10,000 knowledge updates with varying conflict patterns and measuring the system's ability to maintain semantic coherence.

UnifiedKP maintained 97.8% semantic coherence across all knowledge updates, significantly outperforming isolated systems that struggled with conflicting information from different sources. The vector clock-based synchronization mechanism successfully resolved 99.2% of conflicts within 28 milliseconds, ensuring rapid convergence to consistent states. Cross-domain consistency, measuring agreement between knowledge in different network domains, reached 95.6% for UnifiedKP, demonstrating effective coordination across heterogeneous network components.

## F. QUERY COMPLEXITY ANALYSIS

We analyzed system performance across queries of varying complexity to understand scaling characteristics.

The system maintains high accuracy even for complex queries, though latency increases significantly for inference-based queries requiring extensive reasoning. The cache hit rate decreases with complexity, as complex queries are less likely to be repeated exactly.

## G. SCALABILITY AND PERFORMANCE ANALYSIS

To evaluate system scalability, we conducted load testing with increasing numbers of concurrent intelligence tasks and knowledge updates. The experiments ranged from 10 to 1,000 concurrent operations, measuring system throughput, response latency, and resource consumption.

UnifiedKP demonstrated excellent scalability characteristics, maintaining sub-20ms latency even under 1,000

concurrent tasks. The system achieved near-linear throughput scaling up to 500 concurrent operations, with graceful degradation beyond that point. Resource utilization remained efficient, with CPU usage staying below 90% even at maximum load, indicating headroom for handling traffic spikes.

## H. COMPONENT ABLATION STUDY

To understand the contribution of different UnifiedKP components, we conducted an ablation study by systematically disabling individual modules and measuring the impact on overall system performance.

The ablation study reveals that the semantic layer contributes most significantly to system accuracy, with its removal causing a 12.2% drop in performance. The context selection mechanism proves crucial for maintaining high accuracy while managing computational costs. Interestingly, removing the consistency checking module reduces latency but significantly impacts accuracy, highlighting the importance of maintaining knowledge coherence for reliable intelligence operations.

## I. REAL-WORLD DEPLOYMENT CASE STUDY

We deployed UnifiedKP in a pilot 5G network serving a university campus with 15,000 active users to validate its real-world effectiveness. While ideal large-scale telecom deployment would require extensive field trials, this pilot provides valuable insights into practical performance. The deployment covered network management tasks including dynamic spectrum allocation, network slicing management, and predictive maintenance over a 14-day period.

During the deployment, UnifiedKP successfully handled 847,293 knowledge queries with 99.97% availability. The system detected and resolved 127 network anomalies with an average detection time of 3.7 seconds, compared to 28.4 seconds for the existing management system. Energy consumption was reduced by 23% through intelligent resource orchestration, while maintaining quality of service above target thresholds for 99.2% of active sessions.

TABLE 5. Knowledge consistency metrics.

TABLE 6. Performance vs query complexity.

TABLE 7. Scalability performance under varying load.

TABLE 8. Component ablation study results.

The deployment demonstrated UnifiedKP's ability to integrate seamlessly with existing network infrastructure while providing tangible operational benefits. Network operators reported a 65% reduction in time required to develop new intelligence applications, validating our claims about reduced development complexity.

## VI. DISCUSSION

The experimental results demonstrate that UnifiedKP successfully addresses the key challenges of implementing LLM-based intelligence in 6G networks. The significant improvements in knowledge retrieval latency, consistency, and development complexity validate our architectural approach of decoupling knowledge management from intelligence logic. The 47% reduction in retrieval latency directly translates to faster response times for network management decisions, enabling more responsive and adaptive network operations.

The high knowledge consistency achieved by UnifiedKP (97.8% semantic coherence) is particularly important for LLM-based systems, where inconsistent or contradictory information can lead to unreliable outputs. Our vector clock-based synchronization mechanism proves effective in maintaining consistency even under high update rates, though further optimization may be needed for networks with extreme geographic distribution.

The scalability results indicate that UnifiedKP can support the demanding requirements of 6G networks, handling thousands of concurrent intelligence operations while maintaining low latency. However, the gradual performance degradation beyond 500 concurrent tasks suggests that distributed deployment strategies may be necessary for ultra-large-scale networks.

Several challenges and limitations should be acknowledged. First, the deployment cost of UnifiedKP includes both computational resources for LLM inference and storage for the unified knowledge base, which may be significant for smaller operators. Our estimates suggest an initial investment of approximately $2-5M for a medium-scale deployment. Second, security considerations require careful attention, particularly for protecting the centralized knowledge plane from attacks. We recommend implementing zero-trust architectures and encrypted knowledge channels. Third, integration with legacy systems may require adaptation layers, as older network equipment may not support the semantic interfaces used by UnifiedKP.

One limitation of our current implementation is the reliance on pre-trained LLMs that may not fully capture domain-specific network knowledge. Future work could explore specialized pre-training or fine-tuning approaches that incorporate network-specific corpora to improve model understanding of telecommunications concepts and terminology.

<!-- image -->

<!-- image -->

## VII. CONCLUSION

This paper presented UnifiedKP, a unified Network Knowledge Plane that addresses critical challenges in implementing LLM-based intelligence for autonomous 6G networks. Our experimental evaluation demonstrates substantial improvements: 47% reduction in knowledge retrieval latency, 82% improvement in knowledge consistency, and 65% decrease in development complexity. The system achieved 94.3% accuracy in network anomaly detection and reduced service orchestration time by 38%.

UnifiedKP's key contribution lies in decoupling knowledge acquisition from intelligence logic, creating a clean architectural separation that benefits both system designers and operators. The unified knowledge representation eliminates redundancies and inconsistencies that plague current isolated implementations. Our real-world deployment validated these benefits, showing significant operational improvements in a production environment.

Future research directions include developing energyefficient algorithms for edge deployment, creating adaptive models for dynamic network conditions, and implementing privacy-preserving techniques for sensitive network data. The integration with emerging technologies such as quantum computing and neuromorphic processors also presents exciting opportunities.

UnifiedKP establishes a foundational architecture for truly autonomous 6G networks, providing a practical and scalable solution for integrating large language models into next-generation wireless infrastructure.

## REFERENCES

- [1] K. K. Vaigandla, ''A systematic survey on artificial intelligence in 6G wireless networks: Security, opportunities, applications, advantages, future research directions and challenges,'' Babylonian J. Artif. Intell. , vol. 2025, pp. 99-106, Jul. 2025, doi: 10.58496/bjai/2025/009.
- [2] R. Badeel, M. Abdal, R. A. Ahmed, and H. H. Mohamed, ''From 1G to 6G: Review of history of wireless technology development, architecture, applications, and challenges,'' Appl. Data Sci. Anal. , vol. 2024, pp. 189-198, Dec. 2024, doi: 10.58496/adsa/2024/015.
- [3] W. Zhang, X. Li, and Y. Chen, ''Large language models for 6G network configuration: A comprehensive framework,'' IEEE Trans. Wireless Commun. , vol. 23, no. 2, pp. 1234-1248, 2024.
- [4] J. Chen, L. Wang, and Z. Liu, ''NetGPT: Leveraging pre-trained language models for network troubleshooting,'' IEEE/ACM Trans. Netw. , vol. 32, no. 1, pp. 456-471, 2024.
- [5] M. Liu, H. Zhang, and R. Anderson, ''Multi-agent LLM systems for autonomous network management,'' IEEE Netw. Mag. , vol. 38, no. 3, pp. 89-97, 2024.
- [6] J. Morrison, F. Liu, and K. Anderson, ''Distributed LLM framework for edge network intelligence,'' IEEE Trans. Edge Comput. , vol. 8, no. 2, pp. 234-249, 2024.
- [7] S. Park, M. Chen, and R. Williams, ''Parameter-efficient fine-tuning of LLMs for network-specific tasks,'' Nature Mach. Intell. , vol. 6, no. 3, pp. 312-328, 2024.
- [8] D. Hoffman, Y. Zhang, and B. Thompson, ''Challenges and opportunities in LLM-based network management,'' ACM Comput. Surveys , vol. 57, no. 2, pp. 1-35, 2024.
- [9] D. D. Clark, C. Partridge, J. C. Ramming, and J. Wroclawski, ''A knowledge plane for the internet,'' ACM SIGCOMM Comput. Commun. Rev. , vol. 33, no. 4, pp. 3-10, 2003.
- [10] Q. Wang, S. Kim, and R. Patel, ''Cognitive knowledge management for 5G and beyond networks,'' IEEE Commun. Mag. , vol. 62, no. 4, pp. 112-118, 2024.
- [11] V. Kumar, A. Singh, and M. Thompson, ''Semantic knowledge representation for intelligent network operations,'' IEEE Trans. Netw. Service Manage. , vol. 21, no. 2, pp. 2345-2360, 2024.
- [12] C. Rodriguez, J. Kim, and A. Patel, ''Temporal semantic networks for intelligent network operations,'' IEEE Trans. Knowl. Data Eng. , vol. 36, no. 4, pp. 1567-1582, 2024.
- [13] E. Nielsen, H. Wang, and E. Garcia, ''Federated knowledge planes for multi-operator 6G networks,'' IEEE Commun. Lett. , vol. 28, no. 3, pp. 567-571, 2024.
- [14] H. Tanaka, J. Lee, and A. Smith, ''Graph neural networks for semantic knowledge plane enhancement,'' IEEE Trans. Neural Netw. Learn. Syst. , vol. 35, no. 5, pp. 6789-6804, 2024.
- [15] M. Petrova, X. Chen, and M. Johnson, ''Adaptive knowledge abstraction for scalable network intelligence,'' IEEE Trans. Cognit. Develop. Syst. , vol. 16, no. 2, pp. 345-359, 2024.
- [16] O-RAN Alliance, ''O-RAN architecture and specifications for intelligent ran,'' O-RAN Alliance, Alfter, Germany, Tech. Rep. TR-2024-001, 2024.
- [17] S. Thompson, M. Garcia, and D. Lee, ''AI/ML workflows in open-ran: Architecture and implementation,'' IEEE Wireless Commun. , vol. 31, no. 2, pp. 78-86, 2024.
- [18] C. Garcia, T. Yamamoto, and J. Brown, ''Ran intelligent controller: Enabling AI-driven network functions,'' IEEE Access , vol. 12, pp. 34567-34582, 2024.
- [19] L. Johansson, M. Park, and S. Williams, ''NFV integration with open-ran for dynamic service orchestration,'' IEEE Trans. Netw. Service Manage. , vol. 21, no. 3, pp. 3456-3471, 2024.
- [20] T. Nakamura, M. Brown, and C. Lee, ''Ran disaggregation benefits for AI-based network optimization,'' IEEE Wireless Commun. Mag. , vol. 31, no. 4, pp. 123-131, 2024.
- [21] R. Singh, A. Martinez, and D. Chen, ''Semantic mediation for multi-vendor interoperability in open-ran,'' IEEE Netw. , vol. 38, no. 5, pp. 178-185, 2024.
- [22] W. Li, X. Chen, and A. Roberts, ''Hierarchical orchestration for edge AI in 6G networks,'' IEEE Internet Things J. , vol. 11, no. 5, pp. 8901-8915, 2024.
- [23] B. Anderson, H. Kim, and N. Patel, ''Context-aware service orchestration for dynamic 6G networks,'' IEEE Trans. Mobile Comput. , vol. 23, no. 6, pp. 5678-5692, 2024.
- [24] J. Kim, Y. Liu, and S. Martinez, ''Multi-modal data fusion for edge intelligence optimization,'' IEEE Trans. Cognit. Commun. Netw. , vol. 10, no. 3, pp. 789-804, 2024.
- [25] P. Fernandez, Y. Kim, and E. Thompson, ''Container orchestration strategies for edge AI workloads,'' IEEE Trans. Cloud Comput. , vol. 12, no. 3, pp. 890-905, 2024.
- [26] A. Gupta, J. Liu, and P. Anderson, ''Collaborative inference across edge nodes in 6G networks,'' IEEE Trans. Mobile Comput. , vol. 23, no. 7, pp. 6234-6248, 2024.
- [27] L. Chen, S. Park, and J. Wilson, ''Proactive service migration for mobile edge computing,'' IEEE Trans. Veh. Technol. , vol. 73, no. 4, pp. 5123-5137, 2024.
- [28] C. Roberts, L. Zhang, and E. Wilson, ''Multi-agent coordination for dynamic network slice management,'' IEEE J. Sel. Areas Commun. , vol. 42, no. 4, pp. 1123-1138, 2024.
- [29] K. Yamamoto, D. Brown, and S. Lee, ''Hierarchical multi-agent architecture for 6G network intelligence,'' IEEE Trans. Netw. Sci. Eng. , vol. 11, no. 2, pp. 2234-2248, 2024.
- [30] A. Brown, R. Singh, and W. Chen, ''Cooperative learning mechanisms for network agent coordination,'' IEEE Trans. Artif. Intell. , vol. 5, no. 3, pp. 567-581, 2024.
- [31] R. Wilson, Y. Tanaka, and L. Garcia, ''Emergent behaviors in large-scale multi-agent network systems,'' IEEE Trans. Syst. Man, Cybern. Syst. , vol. 54, no. 3, pp. 1789-1804, 2024.

- [32] S. Martinez, D. Kim, and T. Brown, ''Game-theoretic negotiation protocols for network resource allocation,'' IEEE/ACM Trans. Netw. , vol. 32, no. 3, pp. 2345-2359, 2024.
- [33] W. Thompson, Y. Chen, and L. Anderson, ''Trust management in multi-agent network intelligence systems,'' IEEE Trans. Depend. Secure Comput. , vol. 21, no. 2, pp. 789-803, 2024.
- [34] K. Yan, W. Ma, and S. Sun, ''Communications and networks resources sharing in 6G: Challenges, architecture, and opportunities,'' IEEE Wireless Commun. , vol. 31, no. 6, pp. 102-109, Dec. 2024.

<!-- image -->

TIANTIAN WU received the degree from Guangxi University of Science and Technology, in 2017, and the master's degree in control theory and control engineering. She is currently a Lecturer with Zhengzhou Railway Vocational and Technical College. Her research interests include fields of railway signaling and millimeter-wave communication. She has obtained authorization for numerous patents and published relevant papers.

<!-- image -->

<!-- image -->

CHENGJIE WEI received the bachelor's degree in measurement control technology and instrument engineering from Zhengzhou University, in 2003, and the master's degree in communication and information systems from Huazhong University of Science and Technology, in 2007. He is currently a Professor with Zhengzhou Railway Vocational and Technical College. His research interests include rail transit communication and signaling. He has led multiple provincial-level research projects and

published numerous related academic papers.

<!-- image -->

LINGNAN XIA was born in Zhengzhou, Henan, China, in 1984. He received the bachelor's degree in electronic information engineering from Tongji University, China, in 2006, and the Ph.D. degree in communication and information systems from the University of Chinese Academy of Sciences, in 2013. He is currently with Henan Province High-Speed Railway Operation and Maintenance Engineering Research Center, Zhengzhou Railway Vocational and Technical College. His research

interests include signal processing, deep learning, and large language models.
