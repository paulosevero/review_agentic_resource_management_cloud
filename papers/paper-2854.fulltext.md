---
paper_id: "paper-2854"
source_pdf_sha: "64df1d450e04a72ddf03b3066009a0db2eabe133c31cd97487d76556f2d91946"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 2
  page_count: 14
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2854 — fulltext
## §unknown-1

1
Toward 6G Edge Intelligence: Lightweight LLMs
for Intent-Driven Network Automation
Bing Wu, Sai Zou,Senior Member, IEEE, Minghui Liwang,Senior Member, IEEE, Wei Ni,Fellow, IEEE,
Xianbin Wang,Fellow, IEEE, and Youliang Tian,Member, IEEE
Abstract—Future 6G networks are envisaged to tightly inte-
grate communication, sensing, and computing, demanding real-
time, intent-driven intelligence at the edge. While large language
models (LLMs) excel in intent recognition and semantic rea-
soning, their application to real-time network lifecycle man-
agement at the edge is limited by heterogeneous application
intents (APPIs), dynamic network conditions, and severe re-
source constraints. This paper proposes a novel lightweight
LLM architecture, KGLlama-KD, that synergizes knowledge
graphs (KGs) with knowledge distillation (KD) to enable intent-
driven networking and enhance 6G edge intelligence. Specifically,
a KG is constructed to formally describe the relationships
among application scenarios, functional primitives, performance
requirements within APPIs, and the correspondences between
APPIs and network service requests (NSRs), thereby producing
a structured intent training dataset. Building upon the Llama 3
foundation model, a two-phase optimization framework is de-
signed to support lightweight edge deployment while preserving
translation fidelity. The LLM is first fine-tuned with KG guidance
and compressed via KD in the cloud, and then deployed on
resource-constrained edge nodes to perform real-time, accurate,
and efficient APPIs interpretation. Experiments validate that
KGLlama-KD achieves 95% accuracy for APPI understanding,
surpassing DeepSeek and Qwen by an average of 8%. The
distilled model reduces inference latency by 60% compared to
full-scale LLMs, fulfilling the sub-100 ms requirement for 6G
latency-sensitive services.
Index Terms—6G edge intelligence, application intent, network
service request, large language model, knowledge distillation,
knowledge graph.

## § Introduction

T
HE sixth generation (6G) wireless networks are expected
to empower a closed-loop autonomous system architec-
ture with embedded intelligence by deeply integrating diverse
This work is supported in part by the National Research and Development
Programs of China (2025YFB3109801), National Natural Science Foundation
of China (62361011, U24A20246, 62271424), Guizhou Provincial Science
and Technology Plan Project (DXGA[2025]003, DXGA[2025]011), Guizhou
Province Scientist Workstation (KXJZ[2025]005), and Guizhou Province
Science and Technology Innovation Platform (JSZX(2025)020).
B. Wu, S. Zou, and Y . Tian are with the State Key Laboratory of Public
Big Data, College of Big Data and Information Engineering, Guizhou Uni-
versity, China (e-mail: bingwu gz@163.com; dr-zousai@foxmail.com; you-
liangtian@163.com). M. Liwang is with the Department of Control Science
and Engineering, Shanghai Institute of Intelligent Science and Technology, the
National Key Laboratory of Autonomous Intelligent Unmanned Systems, and
the Frontiers Science Center for Intelligent Autonomous Systems, Ministry
of Education, Tongji University, Shanghai 200092, China (e-mail: minghuili-
wang@tongji.edu.cn). W. Ni is with the School of Engineering, Edith Cowan
University, Perth, W A 6027, and the School of Computer Science and
Engineering, University of New South Wales, Sydney, NSW 2052, Australia
(e-mail: wei.ni@ieee.org). X. Wang is with the Department of Electrical and
Computer Engineering, Western University (e-mail: xianbin.wang@uwo.ca).
Corresponding authors: S. Zou and M. Liwang.
capabilities and resources, such as communication, sensing,
computing, and storage [1], [2]. A fundamental prerequisite
for such closed-loop autonomy is the network’s ability to
autonomously translateapplicationintents (APPIs) into cor-
respondingnetworkservicerequests (NSRs) under varying
network conditions [3], [4].
Largelanguagemodels (LLMs) exhibit advanced capa-
bilities in intent recognition and semantic representation by
effectively mining latent patterns within data, thereby enabling
more accurate and context-aware understanding of applica-
tion intents. By embedding lightweight LLM variants into
heterogeneous edge infrastructures, 6G networks can effec-
tively support autonomous APPI-to-NSR (A2N) interpretation,
serving as both the foundation forservice-levelagreement
(SLA)-guaranteed service provisioning and the key enabler for
minimizing end-to-end latency.
To realistically benefit from this paradigm, rapid adap-
tation of network operation to dynamic and diverse ser-
vice demands is essential [5]. For instance, in intelligent
manufacturing scenarios, abnormal behavior detected from
an assembly line prompts the upper-layer control system to
generate an APPI, which is subsequently parsed by an LLM-
based module deployed in the factory’s edge environment. The
resulting NSRs dynamically orchestrate diverse resource types
to support critical decisions, such as safety risk assessment
and emergency shutdown execution. Major related industry
players, e.g., Huawei and Cisco, has underscored the pivotal
role of autonomous APPIs interpretation in future network
architectures [6], [7].
A. Motivation and Challenges
Vertical applications enabled by 6G exhibit diverse needs
across varying scenarios [8]. This brings pronounced variations
inqualityofservice (QoS) requirements—such as latency,
reliability, and throughput—as well as heterogeneous intent
representations (e.g., for PLC4 on production line 1, guar-
anteeing end-to-end latency≤9 ms with 99.94% reliability
while maintaining stable throughput). The intent translation
process has to be adapted continuously due to the network
dynamism and changing resource conditions [9], requiring
high parsing accuracy and robustness under diverse scenarios.
To integrate these into 6G network operations, NSRs can be
serialized as linear sequences that specify the slice type and an
ordered VNF chain (e.g., eMBB|vNSSF.1c2g→vAMF.1c2g
→vSMF.1c2g→. . . ) [10], [11]. All these intricacies render
the A2N mapping process inherently many-to-many, leading
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
2
to an exponentially expanding combinatorial space. To meet
the low-latency requirements of 6G delay-sensitive services, it
is necessary to deploy LLM-empowered intent interpretation
functions near the network edge. However, this deployment
is subject to stringent constraints regarding power, computing
capacity, and storage. Collectively, these factors give rise to
three major challenges:
•The heterogeneous structural and spatio-temporal charac-
teristics of APPIs hinder the discovery and utilization of
their latent semantic and functional correlations.
•Inherent semantic and structural disparities exist between
APPIs and their corresponding NSRs. Typically, APPIs
are conveyed in natural language to express network de-
mands, whereas NSRs are structured, machine-executable
specifications that define VNFs and their associated re-
source. Developing a stable and generalizable mapping
between the semantic space of APPIs and the config-
uration space of NSRs remains a central challenge in
advancing intent-driven network automation.
•Deploying lightweight LLMs with advanced semantic
reasoning capabilities on resource-constrained edge nodes
while ensuring accurate parsing and real-time responsive-
ness to diverse APPIs constitutes another challenge.
B. Contribution
This paper addresses the critical challenges of translating
APPIs into executable NSRs responsively and accurately,
thereby enabling closed-loop autonomy in near-6G edge
networks. We propose KGLlama-KD, a lightweight frame-
work that integratesknowledgegraphs (KGs), LLMs, and
knowledgedistillation (KD) in a unified pipeline. To the best
of our knowledge, KGLlama-KD is among the early efforts
that jointly support natural-language APPI→NSR translation
with explicit KG grounding and deployment-oriented model
compression, making LLM-based intent interpretation practi-
cal on resource-constrained edge nodes. The contributions of
this work include:
•We investigate a novel problem of using LLMs for real-
time, high-fidelity translation of multi-source, heteroge-
neous APPIs into executable NSRs under resource con-
straints. We formulate the A2N mapping as a Bayesian
inference problem to maximize the posterior probability
of correct translation.
•We propose KGLlama-KD, a cloud–edge collaborative
architecture that delineates model training and inference.
In the cloud, a full-scale teacher Llama 3 model is
enhanced with KG guidance, trained offline, and com-
pressed via KD to produce a lightweight student LLM.
This compact model is then deployed near the network
edge to support real-time online inference under strict
millisecond-level latency constraints.
•To implement KGLlama-KD, we construct an A2N
knowledge graph that captures the entity-level, resource,
and spatio-temporal relationships between APPIs and
NSRs, providing structured semantic priors. These priors
are injected into a Llama 3 backbone via relation-aware
embeddings and cross-attention mechanisms, enabling
high-fidelity A2N mapping. A KD compresses the KG-
enhanced full-scale LLM into a lightweight LLM, sig-
nificantly reducing inference complexity while satisfying
the stringent resource constraints of the network edge.
•We demonstrate through extensive experiments on rep-
resentative 6G edge workloads that KGLlama-KD out-
performs the DeepSeek/Qwen benchmarks by 8% in
NSR prediction, increasing inference throughput by 60%,
while supporting the stringent end-to-end latency of less
than 100 ms.
The remainder of this paper is organized as follows. Sec-
tion II reviews the related work across three key areas.
Section III introduces the system model, including the scenario
settings and problem formulation. Section IV provides the
mathematical modeling of the optimization task. Section V
elaborates on the proposed KGLlama-KD framework. Sec-
tion VI presents experimental results to evaluate the effective-
ness of KGLlama-KD. Section VII concludes the paper and
outlines future research directions.
II. LITERATUREREVIEW
This section reviews the related works in APPI interpreta-
tion, KGs, and the integration of LLMs with KD, and high-
lights the research gaps addressed by this study. A summary
of existing works is shown in Table I.
A. Recent Studies on APPIs
Translating APPIs into executable NSRs is a key prereq-
uisite for closed-loop autonomy in 6G intent-driven manage-
ment [12], [13]. Existing studies related to APPI interpretation
span both vertical-domain intent inference and networking-
oriented intent translation. For instance, Penget al.[14]
investigated lane-change recognition using Gaussian mixture
models and Bi-LSTM, Huanget al.[15] introduced the state-
action-intent framework for closed-loop network management,
and Yuanet al.[16] leveraged traffic context for intent
inference. In the networking context, Chowdharyet al.[17]
automated intent translation to SDN flow rules, McNamara
et al.[18] applied NLP to simplify intent-driven 5G slicing,
and Wuet al.[19] integrated hypergraph modeling with
transformer architectures to enhance VNF mapping.
Despite these advances, three critical gaps still remain for
6G edge automation. First, regarding input modality, prior
works often rely on structured representations (e.g., hyper-
graphs [19]) or target low-level flow rules [17], whereas an
explicit end-to-end pipeline translating raw natural-language
APPIs directly into NSRs is less explored. Second, explicit
knowledge grounding to bridge the semantic gap between
unstructured intents and structured NSR elements is lim-
ited, which hinders robustness under heterogeneous scenarios.
Third, edge constraints (compute/power/latency) are rarely
treated as first-class objectives; in particular, deployment-
oriented model compression (e.g., distillation) and rigorous
edge-side evaluation are often absent. Motivated by these gaps,
this work advances APPI interpretation at the 6G network edge
by providing a grounded natural language APPI→NSR trans-
lation pipeline and explicitly addressing edge deployability via
teacher–student distillation.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
3
TABLE I
REPRESENTATIVEWORKS ONAPPIS, KNOWLEDGEGRAPHS,ANDLLM–KD INTEGRATION
Reference Research Field Summary of Contribution
[12] Edge Intelligence Enabling 6G services by leveraging decentralized learning in edge intelligence
[13] Edge Intelligence Coordinating edge models and task generation using a GPT-based orchestration framework
[14] Vertical Intent Inference Improving vehicular intent prediction using Gaussian mixture models and BiLSTM networks
[15] Intent-Based Networking Realizing closed-loop intent execution via a state–action–intent paradigm
[16] Vertical Intent Inference Modeling driver intention and speed through context-aware trajectory prediction
[17] Intent-Based Networking Intent-to-policy enforcement in multi-domain SDN: unifying intent rules and using bounded formal
models for compliance/conflict checking at the flow-rule level
[18] Intent-Based Networking An intent-based platform for private 5G networks with an NLP interface, enabling intent-
driven slice provisioning/positioning/service deployment and benchmarking provisioning time
(platform/controller-side automation rather than edge-side inference)
[19] Intent-Based Networking HyperTrans-CA: modeling APPI–NSR relations with structured hypergraphs and a hypergraph-
augmented Transformer with completeness assurance (assumes structured hypergraph inputs rather
than raw natural language APPIs; not targeting resource-constrained edge deployment)
[20] Graph-Enhanced Wireless Networking Improving bit error rate via transformer-based permutation decoding in the physical layer
[21] Graph-Enhanced Wireless Networking Learning power-allocation strategies with heterogeneous KGs and permutation-equivariant GNNs
[22] Graph-Enhanced Wireless Networking Optimizing large-scale wireless networks using a generalizable GNN framework
[23] Intent-Based Networking LLM-empowered ZSM configuration agents: generating/verifying network configurations from
natural-language intents for zero-touch management (output: device/configuration; the focus is not
on resource-constrained edge deployment)
[24] LLMs and Efficient Deployment Generating hardware description language code for wireless systems using LLMs in FPGA-based AI
hardware design
[25], [26] LLMs and Efficient Deployment Advancing multimodal capabilities in LLMs, with GPT-4 enabling unified language–vision reasoning
and Gemini supporting broader cross-modal understanding across image, audio, and video
[27] LLMs and Efficient Deployment Enabling open-source multimodal learning with support for structured molecular inputs and model
compression (e.g., quantization, pruning) for efficient, domain-adaptable deployment
[28] LLMs and Efficient Deployment LoRA: reducing fine-tuning cost by injecting trainable low-rank matrices
[29] LLMs and Efficient Deployment KD for compressing large-scale models while preserving task-specific performance, improving
inference efficiency on resource-constrained platforms
[30] LLMs and Efficient Deployment TinyBERT: two-stage distillation to obtain a compact Transformer for efficient inference
[31] LLMs and Efficient Deployment Multi-teacher distillation with LLM and graph convolutional networks for temporal–spatial feature
transfer (application in incomplete EEG emotion recognition)
This work Edge Intelligence KGLlama-KD: A lightweight framework for natural-language APPI-to-NSR translation via KG-
enhanced Llama 3 and KD, targeting resource-constrained edge nodes
B. Knowledge Graphs
Accurately characterizing the complex relationships be-
tween APPIs and system configurations is critical for gen-
erating executable NSRs across diverse application scenarios.
Accordingly, KGs, which employ structured graph representa-
tions to express semantic relationships, have been widely in-
vestigated to address this challenge. For instance, in communi-
cations, Caciularuet al.[20] proposed attentive graph permu-
tation selection. This method leverages a self-attention mecha-
nism to perform graph permutation selection for optimizing the
decoding of error-correcting codes. Guo and Yang [21] utilized
heterogeneous KGs to construct power allocation strategies for
multi-cell multi-user systems, effectively capturing node-level
structural correlations. Shenet al.[22] presented a unified
framework that systematically explores KG applications in
wireless networks, validating their effectiveness in large-scale
optimization through both analytical and empirical results.
While prior studies have demonstrated the effectiveness of
KGs in improving network performance, their potential for
interpreting APPIs remains largely underexplored—an aspect
explicitly considered in this work.
C. LLM and Knowledge Distillation
Recent breakthroughs in LLMs are reshaping autonomous
communication systems, granting networks unprecedented
ability to understand and act on APPIs. This impact spans
multiple system layers. At the network management level,
Liraet al.[23] introduced an LLM network configuration
generator that uses the reasoning capability of an LLM to
translate intents into verified device configurations, advancing
zero-touch operations. At the hardware-design level, Zhang
et al.[24] showed that LLMs can markedly accelerate field-
programmable gate array (FPGA)–based wireless network
development by factoring software-defined radio code and
automatically generating complex Verilog modules, e.g., a 64-
point Fast Fourier Transform. While proprietary flagships, e.g.,
OpenAI’s GPT family [25] and Google’s Gemini series [26],
demonstrate the performance ceiling of closed-source models,
practical deployment and reproducible research in networking
increasingly require open and adaptable solutions. Meta’s
Llama 3 [27] meets this need: it combines competitive bench-
mark performance with an open-source license, parameter-
efficient fine-tuning interfaces, and permissive usage terms,
making it well-suited to edge-oriented, domain-specific tasks.
Realizing these advantages at the network edge requires
lightweight models, using parameter-efficient fine-tuning and
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
4
Fig. 1.Cloud–edge collaborative architecture for real-time interpretation of APPIs. The framework integrates cloud-based offline full model
training, edge-based lightweight model deployment, APPIs online inference, and structured semantic mapping between APPIs and NSRs,
thus addressing the stringent adaptability requirements inherent to 6G edge environments.
model compression techniques. Representing efficient fine-
tuning, Huet al.[28] introducedlow-rankadaptation (LoRA),
which inserts small, trainable low-rank matrices into frozen
pretrained weights, thereby reducing both training cost and
memory footprint significantly. For direct model compression,
Hintonet al.[29] proposed KD, where a compact student
model learns from the outputs and latent representations of
a larger teacher model, striking a balance between infer-
ence efficiency, model size, and predictive accuracy. Building
on this distillation paradigm, Jiaoet al.[30] introduced a
novel two-stage KD method tailored for transformer-based
models, resulting in compact models that achieve significant
reductions in size and inference latency while maintaining
performance comparable to the originalbidirectionalencoder
representations fromtransformers (BERT) model. Zhanget
al.[31] combined graph convolutional networks with multiple
full-scale teacher models to guide student models in learn-
ing robust spatio-temporal features under incomplete-modality
conditions, thereby yielding compact models with enhanced
cross-modal generalization capabilities.
Building upon the structured semantic representations of-
fered by KGs, the advanced reasoning capabilities of Llama,
and the transferability enabled by KD, we propose a new
framework, KGLlama-KD. Enhanced with KG-derived priors
and compressed through KD, KGLlama-KD enables real-
time interpretation of APPIs and, thus, closed-loop network
automation near the 6G network edge.
III. SYSTEMOVERVIEW ANDPROBLEMDESCRIPTION
This section provides an overview of KGLlama-KD and de-
scribes the problem of interest. Key notations are summarized
in Table II.
Fig. 2.Structural representation of APPIs and NSRs with association
rules. Left: application-intent graph; middle: functional–performance
associations; right: resulting network-slicing requests. Each appli-
cation function maps to corresponding VNFs, and performance
requirements (e.g., bandwidth, latency, reliability) map to network
resources.
A. System Overview
As shown in Fig. 1, KGLlama-KD, built on a cloud–edge
collaborative architecture, performs real-time interpretation of
APPIs to meet the resource constraints of 6G edge environ-
ments. In the cloud-based offline preparation phase (top of
Fig. 1), we first preprocess industry-specific data to construct
domain KGs. Based on this, we fine-tune an LLM (e.g., via
LoRA) using these KGs, yielding a full-scale teacher model
with enhanced domain contextual understanding. Next, we
apply KD to compress the teacher model into a lightweight
student model, ensuring low-latency online inference and
efficient deployment on resource-constrained edge-computing
nodes (center of Fig. 1).
During the edge-based online interpretation phase, net-
work applications (e.g., industrial video surveillance) submit
APPIs—each specifying functional and performance require-
ments—to the edge nodes. The deployed model interprets
these APPIs in real time and adapts to varying service demands
by leveraging distilled domain knowledge. Based on its output,
the model generates the corresponding NSRs (right of Fig. 1),
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
5
TABLE II
NOTATION ANDDEFINITIONS
Notation Definition
R,SSets of APPIs and NSRs
H,P,OSets of application functionality, per-
formance metrics, and scenarios
V,CSets of VNFs and network resources
ˆTmap, ˆSmap Teacher model and student model
Go, ˆGo APPIs graph and NSRs graph
GKG capturing structural dependencies
between APPIs and NSRs
θ1
0,θ 1
1,θ 2
0,θ2
2,θ ˆSmap ,θ ˆTmap Model parameters (frozen and train-
able)
which precisely specify the required VNFs (e.g., vFWs,
vRouters, VPNs, and vIDSs) and their resource configurations
(e.g., bandwidth allocations, vCPU assignments, and security
policies). This enables intent-driven network automation by
translating APPIs into actionable NSRs within dynamic 6G
edge environments.
B. Problem Description
LetR,O,H, andPbe the sets of APPIs, application sce-
narios (e.g., office environments, industrial production), appli-
cation functionalities, and performance metrics, respectively.
In practice, an APPI is issued as a natural-language intent
statement. For rigorous modeling, we abstract each APPI by its
essential elements—invocation scenario, required functional
primitives, and performance objectives—and represent their
dependencies using a directed heterogeneous graph.
For a given scenarioo, them-th APPI is modeled as
Go
rm =
 
Ao
m, E o
m

,(1)
whichG o
rm denotes a graph to describe such an APPI instance
in scenarioo,r m ∈ R. Besides, node setA o
m is given by
Ao
m =H o
m ∪P o
m, H o
m ⊆ H, P o
m ⊆ P,(2)
whereH o
m ={h o
m,1, . . . , h o
m,z, . . . , h o
m,|H om|}andP o
m =
{po
m,1, . . . , p o
m,ˆz, . . . , p o
m,|P om|}, withh o
m,z being thez-th
functionality node andp o
m,ˆzdenoting theˆz-th performance-
metric node associated with them-th APPI under scenarioo.
The directed edge setE o
m captures two types of dependen-
cies:(a)functional-dependency edges between functionality
nodes, representing precedence or coupling relationships; and
(b)function-to-performance constraint edges, indicating that
each functionality node should satisfy its associated per-
formance objectives. Specifically, if functionality nodeh o
m,1
depends on functionality nodeh o
m,2, there exists a directed
edge − − − − − − − − →(ho
m,1, h o
m,2)∈E o
m; if functionality nodeh o
m,1 is
constrained by performance nodep o
m,ˆz, then there exists a
directed edge − − − − − − − − →(ho
m,1, p o
m,ˆz)∈E o
m. Here, − − →(·,·)represents
a directed dependency from the first node to the second,
reflecting functional or performance constraints.
Similarly, letS,V, andCdenote the sets of NSRs, VNFs,
and network resource requirements, respectively. Each NSR
comprises a set of VNFs associated with specific resource
consumption (e.g., computing, storage, or communication re-
sources), leading to heterogeneity in functional composition
and resource demands. Considering the dependencies among
VNFs, theˆm-th NSRs ˆmunder scenarioois modeled as a
directed heterogeneous graph given by
Go
s ˆm=
  ˆAo
ˆm, ˆEo
ˆm

,(3)
wheres ˆm∈ S, and the node set ˆAo
ˆmis given by
ˆAo
ˆm=V o
ˆm∪C o
ˆm, V o
ˆm⊆ V, C o
ˆm⊆ C,(4)
whereV o
ˆm ={v o
ˆm,1, . . . , v o
ˆm,j, . . . , v o
ˆm,|Vo
ˆm|}andC o
ˆm =
{co
ˆm,1, . . . , c o
ˆm,ˆj, . . . , c o
ˆm,|Co
ˆm|}, withv o
ˆm,jdenoting thej-th
VNF andc o
ˆm,ˆj denoting the ˆj-th resource requirement of
NSRs ˆm. The directed edge set ˆEo
ˆmcaptures two types of
dependencies:(a)if VNFv o
ˆm,1depends on VNFv o
ˆm,2, a
functional dependency edge − − − − − − − − →(vo
ˆm,1, v o
ˆm,2)∈ ˆEo
ˆmis created;
(b)if VNFv o
ˆm,1consumes resourcec o
ˆm,1, a resource-coupling
edge − − − − − − − − →(vo
ˆm,1, c o
ˆm,1)∈ ˆEo
ˆmis established.
The fulfillment of a graph-structured APPIG o
rm using the
service capabilities of a graph-based NSRG o
s ˆmis interpreted
as a graph mapping problem between their respective structural
representations. The application functionalities specified in
H o
m should be fulfilled by VNFs withinV o
ˆm. The objectives in
P o
m should be satisfied by the corresponding network resources
inC o
ˆm. Two types of mapping relationships are defined:
•Each application functionalityh o
m,z ∈H o
m should be
realized by a specific subset of VNFs{v o
ˆm,j, . . .} ⊆V o
ˆm.
This establishes a non-empty correspondence whereby
everyh o
m,z is mapped to one or more VNFs capable of
implementing the required function.
•Each performance metricp o
m,ˆz∈P o
m imposes a constraint
that should be satisfied through the network resources
associated with the mapped VNFs. Satisfyingp o
m,ˆz re-
quires identifying and configuring an appropriate subset
of resource elementsc o
ˆm,ˆj ∈C o
ˆmto meet the specified
performance requirements.
Determining a suitable NSRs ˆmand constructing valid
functional and performance correspondences for a given APPI
rm constitutes a core challenge, particularly in dynamic and
resource-constrained 6G edge environments. This matching
process should not only preserve the complex functional and
performance dependencies encoded within the directed hetero-
geneous graphsG o
rm and ˆGo
s ˆm, but also satisfy the stringent
latency, computational, and resource constraints characteristic
of edge nodes. Accordingly, the task can be regarded as a con-
strained subgraph matching or graph homomorphism problem
subject to multiple optimization objectives. The symbolsm,
ˆm,z,ˆz,j, and ˆjall represent natural numbers.
IV. MODELING ANDPROBLEMFORMULATION
This section formalizes the A2N mapping problem. To
determine suitable VNFs for satisfying an APPIr m, we
introduce a binary decision variableb o
m,ˆm,jindicating whether
thej-th VNF in theˆm-th NSR candidateV o
ˆmis selected to
server m under scenarioo:
bo
m,ˆm,j=
(
1,ifv o
ˆm,jis selected forr m;
0,otherwise, (5)
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
6
wherev o
ˆm,j ∈ Vis thej-th VNF inV o
ˆm withj∈
{1, . . . ,|V o
ˆm|}, and eachv o
ˆm,jis associated with a resource
configurationc o
ˆm,j.
VNF dependencies may exist under SLAs. If− − − − − − − − →(vo
ˆm,j, vo
ˆm,j′)∈ ˆEo
ˆm in the NSR graph ˆGo
s ˆm, selecting
vo
ˆm,jrequires selectingv o
ˆm,j′:
bo
m,ˆm,j≤b o
m,ˆm,j′,∀ − − − − − − − − →(vo
ˆm,j, vo
ˆm,j′)∈ ˆEo
ˆm.(6)
Some VNFs are mutually exclusive. For any exclusive pair
(vo
ˆm,j, vo
ˆm,j′′):
bo
m,ˆm,j+b o
m,ˆm,j′′ ≤1.(7)
We adopt an order-preserving one-to-one alignment between
parsed APPI units and NSR chain positions:h o
m,j aligns with
vo
ˆm,j, andp o
m,j aligns withc o
ˆm,j; adjacency is preserved:
− − − − − − − − − − →(ho
m,j, ho
m,j+1)⇒ − − − − − − − − − →(vo
ˆm,j, vo
ˆm,j+1)∈ ˆEo
ˆm,(8)
for all validj.
We model the A2N mapping quality using a Bayesian
framework. Lets ∗ denote the NSR configuration induced by
the mapping. For each(m, o), we select a single best NSR
candidateˆm∗ from{V o
ˆm}to instantiates ∗; thus VNFs are not
mixed across candidates. The joint probability ofr m being
satisfied bys ∗ is
Pr(rm, s∗)∝

Y
j
Pr
 
ho
m,j




Y
j
Pr
 
po
m,j



×
Y
j
L
 
vo
ˆm∗,j, co
ˆm∗,j |r m, bo
m,ˆm∗,j

.(9)
The priorsPr(h o
m,j)andPr(p o
m,j)are estimated offline from
the training APPI corpus using normalized occurrence fre-
quencies with Laplace smoothing. Specifically,Pr(h o
m,j)takes
the prior of the corresponding functionality tokenh o, and
Pr(po
m,j)takes the prior of the corresponding performance
tokenp o, as given by
Pr(ho) = cnto(ho) +λP
h′∈Ho cnto(h′o) +λ|H o| ,
Pr(po) = cnto(po) +λP
p′∈P o cnto(p′o) +λ|P o| ,
(10)
wherecnt o(·)is counted from parsed intents under scenarioo
andλ= 1. If the scenario labels are unavailable, we aggregate
counts across scenarios to compute global priors.
The likelihood contribution of a candidate VNF and its
resource configuration is
L
 
vo
ˆm∗,j, co
ˆm∗,j |r m, bo
m,ˆm∗,j

=


Pr

vo
ˆm∗,j |h o
m,j

Pr

co
ˆm∗,j |p o
m,j

,ifb o
m,ˆm∗,j = 1;
1,ifb o
m,ˆm∗,j = 0.
(11)
For numerical stability, we use the log-likelihood form.
Taking the logarithm of (9) and dropping constants yields
ln Pr(rm, s∗) =
X
j
ln Pr
 
ho
m,j

+
X
j
ln Pr
 
po
m,j

+
X
j
bo
m,ˆm∗,j ln Pr
 
vo
ˆm∗,j |h o
m,j

+
X
j
bo
m,ˆm∗,j ln Pr
 
co
ˆm∗,j |p o
m,j

.
(12)
LetBdenote the set of decision variablesb o
m,ˆm∗,j. We
maximize the aggregated log-likelihood across all APPIs and
scenarios:
max
B
X
o∈O
X
m∈R
ln Pr (rm, s∗)(13a)
s.t. (6),(7),(8),
bo
m,ˆm∗,j ∈ {0,1},
∀o∈ O, m∈ R, j∈ {1, . . . ,|V o
ˆm∗ |}.(13b)
where (6)–(7) enforce VNF dependency and mutual exclu-
sion, and (8) enforces order-preserving consistency between
the APPI unit sequence and the selected NSR chain. The
log-likelihood form improves numerical stability by avoiding
underflow from products of small probabilities.
Fig. 3.KGLlama-KD integrates KGs, the Llama model, and KD.
Relational knowledge from KGs is injected into the Llama-based
teacher model and subsequently distilled into a compact student
model for lightweight deployment at the edge.
V. DESIGN OFKGLLAMA-KD
The optimization problem formulated in (13) is a non-
linearmixedintegerprogram (MIP) characterized by high-
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
7
dimensional discrete variables and complex logical inter-
dependencies. Given its NP-hard nature, traditional exact
solvers are computationally prohibitive for the stringent real-
time requirements of edge-native deployments. To circumvent
this intractability, we propose KGLlama-KD, a generative
framework that reformulates the combinatorial optimization
as a constraint-grounded sequence generation task. The core
philosophy of KGLlama-KD is to internalize the mathematical
feasibility space into the model’s learned distribution: the
mutual-exclusion and dependency constraints defined in (6)–
(8) are explicitly encoded as relational priors in the A2N
KG. During the KG-guided fine-tuning phase, the teacher
model learns to navigate this constrained search space, effec-
tively capturing the underlying logical structure of the MIP.
This constraint-aware expertise is subsequently transferred to
a lightweight student via KD. Consequently, KGLlama-KD
avoids the iterative overhead of MIP solvers while ensuring
that the generated NSRs remain functionally consistent with
the original logical constraints, enabling executable and real-
time slice orchestration at the network edge.
A. A2N Knowledge Graph Construction
To support structured semantic modeling, we first prepare
asupervisedfine-tuning (SFT) dataset for intent semantic
parsing (i.e., information extraction) from natural-language
APPIs. LetD SFT ={(X i,T i)}N
i=1 denote the dataset, where
the raw input is a free-form natural-language APPI sentence,
andT i is its structured semantic form represented as a set (or a
linearized sequence) of extracted entity–relation–entity triples.
In the rest of this paper,iandjrepresent positive integers,
i.e.,i, j∈N + withi̸=j, unless otherwise specified.
The token embedding sequence of thei-th APPI instance is
denoted by
Xi = (xi,1, . . . ,xi,t, . . . ,xi,Ti),(14)
wherex i,t ∈R d1 is the embedding of thet-th token andT i
is the sequence length.
The stage trains a Llama-based parserπ (θ1
0 +θ1
1 ) to perform
token-to-entity alignment (and relation cueing) for triple ex-
traction. Specifically, givenX i, the model outputs a sequence
of entity-label distributions, defined as follows
ˆYi = (ˆyi,1, . . . , ˆyi,t, . . . , ˆyi,Ti), ˆyi,t ∈∆ d3−1,(15)
where∆ d3−1 is the probability simplex. The final triple set ˆTi
is obtained by aggregating the predicted entity labels together
with relation patterns (details in Algorithm 1).
During parsing (e.g., entity alignment), we adopt a scaled
dot-product attention mechanism over candidate entities. For
tokenx i,t, the query is
Qi,t =W Q
1 xi,t,(16)
and the candidate keys are
Kj =W K
1 ecand
j , j= 1, . . . , d 3,(17)
whereW Q
1 ∈R dk×d1 andW K
1 ∈R dk×d1 are
The token-to-entity matching logits and the resulting distri-
bution are computed as
ℓi,t,j = Q⊤
i,tKj
√dk
, ˆyi,t = softmax
 
ℓi,t,1:d3

.(18)
The trainable parametersθ 1
1 are optimized by minimizing
the cross-entropy (or equivalently,kullback–leibler (KL) diver-
gence) between the predicted distribution ˆyi,t and the ground-
truth entity label distributiony i,t:
L(θ1
1) =− 1
N
NX
i=1
1
Ti
TiX
t=1
d3X
j=1
yi,t,j log ˆyi,t,j.(19)
After intent information extraction, we obtain structured
intent triples from each natural-language APPI, and then
construct an A2N KGG= (A,E), where the node set is
A=O ∪ H ∪ P ∪ V ∪ C,(20)
Here,O,H, andPdenote scenario, functionality, and per-
formance entities extracted from APPIs, respectively; andV
andCindicate VNF and resource-consumption entities derived
from NSR specifications and the VNF catalogue. We build and
maintain a versioned VNF catalogue and an NSR specification
repository, which incorporate explicit dependency and exclu-
sion rules. These resources are relatively stable within each
offline model-preparation and evaluation cycle.
To establish inter-node relationships, FP-growth [32] is
employed to mine frequent co-occurrence patterns from the
training transactions, enabling the discovery of implicit asso-
ciations among heterogeneous nodes inA(e.g.,H → Vand
P → C). For any two nodesa 1, a2 ∈ A, the support and
confidence of the rulea 1 →a 2 are defined as
support(a1 →a 2) = count(a1 ∪a 2)
|D| ,(21)
confidence(a1 →a 2) = count(a1 ∪a 2)
count(a1) ,(22)
wherecount(·)denotes occurrence counts in the transaction
database and|D|is the total number of transactions. The
detailed KG construction procedure is summarized in Algo-
rithm 1.
B. Offline Cloud Training of KGLlama
This section presents the offline cloud training ofKGLlama,
a KG-grounded LLM that translates APPIs into executable
NSRs by conditioning on a triple-based KG context. We
leverage a pre-constructed A2N knowledge graphG(cf. Al-
gorithm 1) as external domain priors.
Given a natural-language APPI instance, we perform in-
tent information extraction to obtain its core intent triple
(Oi, Hi, Pi). We then form the KG input token sequenceT kg
i
by linearizing the corresponding triple context (anchored at
(Oi, Hi, Pi)) fromGunder a fixed token budget, with length
Lkg
i .
The sequenceT kg
i is tokenized and mapped to continuous
representations by the Llama 3 token embedding layer, yield-
ingX kg
i ∈R d1×Lkg
i , whered 1 is the embedding dimension
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
8
Algorithm 1:Knowledge Graph Construction
Input:D SFT ={(X (n),Y (n))}N
n=1; Candidate Entity
EmbeddingsY cand; Extractor LLMLLM 1; Frozen
Model Paramsθ 1
0; Trainable Paramsθ 1
1;
Hyperparams:η 1, σmin, γmin; Transaction Database
D; number of epochs|E|;
Output:G={A,E}
1forepoch= 1→ |E|do
2foreach(X (n),Y (n))∈ D SFT do
3 ˆY(n) ←π (θ1
0 +θ1
1 )(X(n))
4L(θ 1
1)←Loss( ˆY(n),Y (n))
5Updateθ 1
1 via gradient descent w.r.t.L(θ 1
1);
6end
7end
8Initialize setsO ext,H ext,P ext
9foreachX (n) in datasetdo
10 ˆY(n) ←π (θ1
0 +θ1
1 )(X(n))
11(O n, Hn, Pn)←ExtractEntities( ˆY(n))
12AddO n, Hn, Pn toO ext,H ext,P ext respectively
13end
14RetrieveV(VNFs) andC(metrics)
15A ←O ext ∪ Hext ∪ Pext ∪ V ∪ C
16InitializeE ← ∅
17Rules←FP Growth(D, σmin)
18foreachrule(a 1 →a 2)∈Rulesdo
19conf← count(a1∪a2)
count(a1) ,supp← count(a1∪a2)
|D|
20ifconf≥γ min andsupp≥σ min then
21E ←e a1,a2
22end
23end
24returnG={A,E}
andL kg
i is the input length. Our goal is to learn an autore-
gressive mapping from the KG-conditioned input to a target
NSR token sequence. Specifically, under our serialized linear
representation, the ground-truth NSR for instanceiis written
ass i = (ˆai,1, . . . ,ˆai, ˆLi
), where ˆLi is the output length and
each tokenˆa i,t ∈ ˆA. The vocabulary ˆAcorresponds to the
token set used by our serialized NSR representation.
We adopt a Llama 3 architecture where the base parameters
θ2
0 remain frozen, and introduce trainable parametersθ 2
2
via PEFT, specifically LoRA [28]. This setup models the
conditional distributionPr(s i |T kg
i )under RoPE.
At decoding stept, we define the decoder input token
sequence as
T in
i,t ≜concat
 
T kg
i ,ˆai,<t

,(23)
whereˆai,<t denotes the previously generated tokens. The
causal self-attention fuses the KG context and generation
history, producing the hidden stateh dec
i,t ∈R d1.
A linear output layer, parameterized by ˆW2 ∈R d1×| ˆA| and
ˆb2 ∈R | ˆA| (where ˆW2, ˆb2 ∈θ 2
2), projectsh dec
i,t to logits over
ˆA. The probability of the next token is obtained via softmax:
Pr
  ˆA′
i,t = ˆai,t


 T in
i,t;θ 2
2

= softmax
 
hdec
i,t ˆW2 + ˆb2

ˆa.(24)
The trainable parametersθ 2
2 are optimized by minimizing
Algorithm 2:Offline Cloud Training of KGLlama
Input:KG-augmented datasetD kg ={(T kg
n , skg
n )}N
n=1;
Translator modelLLM 2; frozen backbone paramsθ 2
0;
initial LoRA paramsθ 2
2; learning rateη; batch size
B; number of epochs|E|; lossL(·)
Output:Optimized LoRA paramsθ 2
2
1forepoch←1to|E|do
2D kg ←Shuffle(D kg)
3foreachmini-batchB ⊆ D kg of sizeBdo
4(x,y)←PrepareInputs(B)
5 ˆy←f (LLM2)
θ2
0 ,θ 2
2
(x)
6ℓ← L( ˆy,y)
7g← ∇ θ2
2
ℓ
8θ 2
2 ←AdamW(θ 2
2,g, η)
9end
10end
11returnθ 2
2
the negative log-likelihood (NLL):
L(θ2
2) =− 1
N
NX
i=1
ˆLiX
t=1
log Pr
  ˆA′
i,t = ˆai,t


 T in
i,t;θ 2
2

,(25)
whereNdenotes the number of training instances (computed
over mini-batches in practice). Optimization is performed
using gradient-based methods (e.g., Adam with learning rate
η2). Algorithm 2 summarizes the training procedure.
C. Knowledge Distillation for Lightweight LLM Deployment
To develop an efficient model suitable for deployment in
near-6G edge environments, KD is employed. The distillation
process is conducted in the cloud and is initiated upon re-
ceiving A2N data pairs collected from the edge. This allows
the student model to inherit relevant knowledge tailored to
real-world deployment scenarios. Specifically, knowledge is
distilled from the full-scale KGLlama teacher model (denoted
as ˆTmap, based on Llama 3 7B with parametersθ ˆTmap
) into a
lightweight student model (denoted as ˆSmap, based on Llama 3
1B with parametersθ ˆSmap
). The distillation is carried out
with respect to the A2N mapping task, and incorporates PEFT
techniques, such as LoRA, during training.
The objective of this stage is to train the lightweight student
model ˆSmap under the guidance of the KG-enhanced teacher
model ˆTmap. The distillation is performed on a structured
mapping dataset, comprising inputsX kg
i and corresponding
target NSR sequencess kg
i .
The distillation process employs a composite loss function,
LKDmap, which combines a supervised loss (L Supmap) based
on ground-truth data with an imitation loss (L Immap) that en-
courages the student to mimic the teacher’s output distribution.
The components of the loss function are defined as follows:
• L Supmap: Standard NLL loss for auto-regressive se-
quence generation, calculated using the ground-truth NSR
sequencess kg
i , as given by
LSupmap=− 1
N
NX
i=1
LiX
t=1
logP ˆSmap
 
ynsr
i,t |y nsr
i,<t,X kg
i ;θ ˆSmap

,
(26)
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
9
Algorithm 3:KD with LoRA for Edge Deployment
Input:Training datasetD={(X kg
i , s i)}N
i=1;
Frozen teacher model parametersθ ˆTmap;
Student model architecture (Llama 3 1B with LoRA) with
parametersθ ˆSmap;
Hyperparameters: loss weightα, temperatureτ map, max
number of epochs|E|.
Output:Optimized student model parametersθ ˆSmap.
1Initializeθ ˆSmap with LoRA adapters;
2forepoch= 1→ |E|do
3foreachmini-batch(X kg, s)inDdo
4U ˆTmap ← ˆTmap(X kg);
5U ˆSmap ← ˆSmap(X kg);
6L Supmap ←NLL(s,U ˆSmap);
7L Immap ←
KL

softmax

U ˆTmap
τmap
 



 softmax

U ˆSmap
τmap

;
8L KDmap ←αL Supmap + (1−α)τ map LImmap;
9Updateθ ˆSmap via gradient descent;
10Validateand apply early stopping if necessary;
11returnθ ˆSmap
whereP ˆSmap
(·)denotes the token probability predicted by the
student model for the ground-truth token indexy nsr
i,t .
• L Immap: The KD loss based on the KL divergence,
encouraging the student ˆSmap to mimic the softened output
distribution of the teacher ˆTmap. The softened distributions
are obtained using the softmax function with a temperature
τmap >1to the models’ logits (U ˆTmap,i,t andU ˆSmap,i,t), as
given by
LImmap =
1
N
NX
i=1
LiX
t=1
KL

softmax
U ˆTmap,i,t
τmap

∥softmax
U ˆSmap,i,t
τmap

.
(27)
The final loss function for optimizingθ ˆSmap
, incorporating
the scaling factorτ 2
map as suggested in [29], and using the
balancing hyperparameterα∈[0,1], is given by
LKDmap =αL Supmap + (1−α)τ 2
mapLImmap .(28)
By minimizingL KDmap, we train the lightweight student
model ˆSmap, based on Llama 3 1B. This yields an efficient
A2N mapping model suitable for deployment on edge nodes.
The detailed procedure is outlined in Algorithm 3.
VI. EVALUATIONS
To validate the proposed KGLlama-KD framework, we
conducted comprehensive experiments focusing on three di-
mensions: semantic translation accuracy, generalization to
unseen APPIs, and deployability under edge resource con-
straints. Benchmarking against state-of-the-art LLMs includ-
ing DeepSeek R1 7B, Llama 3 7B, Qwen 2.5 7B, HyperTrans-
CA and Transformer, we investigate the followingresearch
questions (RQs), using the same underlying dataset across all
models for fairness:
•RQ1: How does KGLlama (the teacher model trained
offline in the cloud) improve the A2N translation accuracy,
as measured by cosine similarity and Levenshtein accuracy?
•RQ2: To what extent does KGLlama improve inference
throughput, measured by the number of APPIs processed per
unit time, and reduce response latency?
•RQ3: How does the distilled student model perform in
translation accuracy, inference efficiency, including throughput
and response latency, and resource overhead during edge
deployment?
To quantify the semantic alignment and lexical fidelity of the
A2N mapping, we employ two quality-oriented metrics: cosine
similarity and Levenshtein accuracy [33]. To assess schema-
level constraint adherence of the generated NSR chains, we
also report theconstraintviolationrate (CVR).
Letϕ(·)denote a text embedding function that maps
a serialized output to ad-dimensional vector. We define
ˆTp =ϕ(ˆy)and ˆTl =ϕ(y)as the vector representations of
the predicted and reference outputs, respectively. The cosine-
similarity-based metric, denoted asSim, is defined as
Sim( ˆTp, ˆTl) =
Pd
i=1 ˆTp,i · ˆTl,iqPd
i=1 ˆT 2
p,i ·
qPd
i=1 ˆT 2
l,i
.(29)
The Levenshtein accuracy, denoted asLevAcc, evaluates
order-sensitive string fidelity by normalizing the Levenshtein
edit distance between the predicted serialized stringˆyand the
reference serialized stringy:
LevAcc(ˆy, y) = 1− dlev(ˆy, y)
max(|ˆy|,|y|),(30)
whered lev(·,·)denotes the Levenshtein edit distance com-
puted on the serialized strings, and| · |denotes the string
length. A largerLevAccindicates that fewer edit operations
are required to transformˆyintoy, implying higher order-
sensitive fidelity of the generated NSR chain.
To report the CVR, we predefine a rule set consisting
of dependency rules(v a ⇒v b)and mutual-exclusion rules
(va ⊥v c)over the VNF catalog. For each predicted chain,
we parse its serialized form and check whether it (i) violates
any dependency by containingv a but missing the required
vb, or (ii) violates any mutual exclusion by containing any
prohibited pair(v a, vc). CVR is defined as the proportion of
test instances where the predicted chains violate at least one
rule. A smaller CVR indicates higher compliance with the
schema-level dependency and mutual-exclusion constraints.
A. Model Training and Knowledge Distillation
Experiments were conducted on the Guizhou University
Cloud–Edge Collaborative Platform, which consists of homo-
geneous server nodes (Table III). The hardware setup included
a cloud server equipped with three NVIDIA RTX 4090 GPUs
for offline model preparation (e.g., fine-tuning and distillation),
and a dedicated edge server equipped with a single NVIDIA
RTX 4090 GPU for online inference evaluation.
To validate the proposed method, we constructed an A2N
benchmark dataset comprising 16,730 samples, built upon the
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
10
0 2 004 006 008 000510152025 Learn Rate 2E-3 Learn Rate 2E-4 Learn Rate 2E-5S
tepL
oss0
.00.10.20.30.40.50.60.7-
0.10.00.10.20.30.40.50.60.7
(a)Impact of different learning rates on teacher-
model fine-tuning convergence.
0 2 004 006 008 00-0.10.00.10.20.30.40.50.60.7 Learn Rate 2E-5 Cosine Annealing Learn RateS
tepL
oss-
0.20.00.20.40.60.81.01.21.41.61.82.0
(b)Effect of the cosine-annealing learning-
rate schedule on teacher-model convergence.
/s76/s111/s115 /s115 
/s83 /s116 /s101/s112
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s50/s44 /s116 /s97/s117/s61 /s49
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s50/s44 /s116 /s97/s117/s61 /s50
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s50/s44 /s116 /s97/s117/s61 /s52
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s53/s44 /s116 /s97/s117/s61 /s49
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s53/s44 /s116 /s97/s117/s61 /s50
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s53/s44 /s116 /s97/s117/s61 /s52
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s54/s44 /s116 /s97/s117/s61 /s49
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s54/s44 /s116 /s97/s117/s61 /s50
/s32/s97/s108 /s112/s104/s97/s61 /s48/s46 /s54/s44 /s116 /s97/s117/s61 /s52
(c)Convergence behavior under different
distillation hyperparameters ((α), (τ)).
Fig. 4.Convergence analysis under different learning-rate and distillation-hyperparameter settings.
TABLE III
EXPERIMENTALPLATFORMCONFIGURATION
Component Specification
CPU Intel(R) Xeon(R) Gold 6330 CPU @ 2.00 GHz
GPU NVIDIA GeForce RTX 4090×3, 24 GB GDDR6X
CUDA Version 12.2
Operating System Ubuntu 20.04 LTS
Virtualization Docker + Kubernetes
Framework PyTorch 2.3.1
TABLE IV
BUDGET-MATCHED7B FINE-TUNINGSETUP
Item Setting (identical across all 7B LLM base-
lines)
Data split Train/Val = 0.8/0.2
Max seq length cutoff len = 2048
Training budget 5 epochs
Effective batch size 16
Optimizer AdamW
Learning rate2×10 −4
LR scheduler cosine
Precision & acceleration bf16; FlashAttention enabled
LoRA configuration target = all,r= 8,α= 16, dropout = 0.1
raw resources and problem definitions provided in [34]. The
dataset was partitioned into training and validation splits with
a 0.8/0.2 ratio.
Regarding KGLlama (Llama 3 7B-based), we constructed
the A2N mapping teacher ˆTmap on a KG-enhanced Llama 3
7B backbone and adapt it using LoRA. DeepSeek and Qwen
are representative LLM baselines with a comparable 7B pa-
rameter scale. To ensure a controlled and fair comparison,
all 7B LLM baselines were fine-tuned under an identical,
budget-matched protocol; the budget-defining settings were
summarized in Table IV. HyperTrans-CA and the Transformer
baseline are implemented with a 10-layer encoder and a 10-
layer decoder.
We additionally employed noisy-embedding regularization
withα NE = 5. For KGLlama-KD (Llama 3 1B-based), we
distilled ˆTmap into the compact student ˆSmap using distillation
weightα= 0.2and temperatureτ map = 1.
B. Hyperparameter Optimization
Key hyperparameters were tuned under a consistent exper-
imental protocol using the validation split. For the mapping
stage, Fig. 4a compares different learning rates and indicates
that2×10 −4 provides a better trade-off between convergence
speed and stability, whereas larger rates (e.g.,2×10 −3) lead
to noticeable oscillations and less stable training dynamics.
Fig. 4b shows that a cosine-annealing learning-rate schedule
yields smoother convergence than a constant learning rate,
since it adaptively reduces the step size as optimization
progresses.
For the distillation stage, we perform a sensitivity analysis
with respect to the distillation weightαand the temperature
τ. Fig. 4c presents the training loss trajectories under different
(α, τ)configurations. The curves exhibit stable and rapid
convergence across the evaluated range, without apparent
divergence, suggesting that the distillation optimization is
not unduly sensitive to these hyperparameters in our setting.
To connect convergence behavior with translation quality,
Fig. 5 reports a heatmap of theVNF component-setoverlap
(VSO) under different(α, τ)choices. The VSO varies only
marginally across configurations, indicating robust component-
level alignment of the distilled student model; among the
evaluated settings,α= 0.2andτ= 1yield the highest
validation VSO. Accordingly, we adoptα= 0.2andτ= 1as
the default configuration for all reported results.
/s48/s46/s57/s57/s57/s51
/s48/s46/s57/s57/s55/s49 /s48/s46/s57/s57/s54/s49
/s48/s46/s57/s57/s55/s57 /s48/s46/s57/s57/s52/s55 /s48/s46/s57/s57/s52/s53
/s116/s97/s117/s61/s52
/s97/s108/s112/s104/s97/s61/s48/s46/s50
/s48/s46/s57/s57/s52/s49
/s48/s46/s57/s57/s52/s56
/s48/s46/s57/s57/s53/s54
/s48/s46/s57/s57/s54/s51
/s48/s46/s57/s57/s55/s49
/s48/s46/s57/s57/s55/s56
/s48/s46/s57/s57/s56/s54
/s48/s46/s57/s57/s57/s51
/s86/s83/s79
/s116/s97/s117/s61/s50/s116/s97/s117/s61/s49
/s97/s108/s112/s104/s97/s61/s48/s46/s53 /s97/s108/s112/s104/s97/s61/s48/s46/s54
Fig. 5.Sensitivity heatmap of VNF component-set overlap under
different distillation hyperparameters ((α, τ)).
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
11
0 2 004 006 008 0005
1
01
5LossS
tep 
DeepSeek Llama KGLlama Qwen
(a) Convergence speed comparison.
/s75 /s71 /s76/s108/s97/s109/s97 /s68/s101/s101/s112/s83 /s101/s101/s107 /s81 /s119/s101/s110 /s76/s108/s97/s109/s97
/s48/s46 /s48
/s48/s46 /s50
/s48/s46 /s52
/s48/s46 /s54
/s48/s46 /s56
/s49/s46 /s48
/s49/s46 /s50
/s86 /s78/s70 /s32 /s67/s111/s109 /s112/s111/s115 /s105/s116 /s105/s111/s110/s32 /s83 /s105/s109 /s105/s108/s97/s114 /s105/s116 /s121 
/s32/s75 /s71 /s76/s108/s97/s109/s97 /s32 /s32/s68/s101/s101/s112/s83 /s101/s101/s107
/s32/s81 /s119/s101/s110 /s32/s76/s108/s97/s109/s97
/s48 /s46 /s57 /s55 /s54 /s32 /s177 /s32 /s48 /s46 /s48 /s50 /s50 
/s48 /s46 /s57 /s48 /s53 /s32 /s177 /s32 /s48 /s46 /s48 /s52 /s48 
/s48 /s46 /s57 /s50 /s56 /s32 /s177 /s32 /s48 /s46 /s48 /s51 /s52 
/s48 /s46 /s56 /s57 /s52 /s32 /s177 /s32 /s48 /s46 /s48 /s54 /s50 (b) VNF Component-Set Overlap in NSRs.
0 1 2 3 4 5 6 7 8 9 1 01 10501001502002503003509
C
umulative processed APPIsP
rocessing time (s) 
Qwen KGLlama DeepSeek Llama HyperTrans-CA Transformer (c) Processing throughput.
Fig. 6. Performance evaluation of KGLLama against baseline algorithms in A2N translation: (a) convergence speed, (b) VNF Component-Set Overlap in
NSRs, and (c) Processing throughput.
TABLE V
PERFORMANCECOMPARISON FORA2N MAPPING
Method SCA VSO VC-EM CVR Latency.
(ms/sample)
DeepSeek 0.71 0.89 0.86 0.00 33.6
Qwen 0.88 0.92 0.89 0.00 45.4
Llama 0.83 0.90 0.84 0.00 39.5
HyperTrans-CA 0.86 0.92 0.89 0.00 221.7
Transformer 0.73 0.83 0.76 0.00 349.6
KGLlama 1.00 0.97 0.96 0.00 50.01+33.3
KGLlama-KD 0.96 0.95 0.93 0.00 31.2+21.7
SCA: Slice Classification Accuracy; VSO: VNF-set Overlap (order-agnostic); VC-EM: VNF chain exact match
(order-sensitive), measured by Levenshtein accuracy;
C. Experimental Results and Analysis
•Response to RQ1:As shown in Fig. 6a and Table V, our
KGLlama attains the highest VSO for the predicted NSRs,
achieving a mean similarity of 0.976, compared with Qwen
(0.928), Llama (0.905), DeepSeek (0.894), HyperTrans-CA
(0.92), and the Transformer baseline (0.83). This improvement
is attributed to the complementary effects of a pretrained
LLM and KG grounding: the pretrained LLM supports robust
natural-language understanding for inferring implicit require-
ments from free-form intents, while KG grounding introduces
explicit intent–VNF relational priors that regularize VNF
selection and mitigate semantic drift. Consequently, under
identical supervision and decoding protocols, KGLlama more
consistently recovers the target VNF composition.
KGLlama exhibits stable optimization behavior. As illus-
trated in Fig. 6a, its training loss starts at a moderate level
(around 6) and decreases rapidly to a near-zero region within
approximately 120–150 update steps with a smooth trajectory.
In comparison, DeepSeek and Llama start from slightly higher
losses (around 6.5–7) and typically require more steps to
reach a similar regime. Although Qwen reaches the near-zero
region earlier (around 100 steps), it starts from a substantially
higher initial loss (around 15–16), indicating a sharper early-
stage loss decrease. Fig. 6a suggests that KGLlama achieves
a favorable trade-off between convergence speed and training
stability among the evaluated baselines.
•Response to RQ2:As shown in Fig. 6c, over a 10 s
observation window, Qwen, Llama, DeepSeek, and KGLlama
process approximately 220, 250, 290, and 300 APPIs, re-
spectively, corresponding to throughputs of about 22, 25, 29,
and 30 APPI/s. These throughputs imply average per-APPI
inference latencies of roughly 45 ms (Qwen), 40 ms (Llama),
34 ms (DeepSeek), and 33 ms (KGLlama), estimated as the
inverse of throughput.
Importantly, Fig. 6c reports only the steady-state throughput
of the LLM during the translation stage (i.e., A2N generation).
Table V provides a more practical end-to-end latency break-
down for KGLlama by decomposing the per-sample latency
into two sequential components: 50.01 ms for KG reason-
ing/construction and 33.3 ms for A2N translation, resulting
in a total latency of 83.31 ms per sample. Consequently,
the overall response time can be substantially increased by
additional non-LLM overhead, including KG reasoning, tok-
enization/preprocessing, and runtime scheduling. This obser-
vation motivates the lightweight KGLlama-KD variant, which
is designed to reduce end-to-end latency while preserving
translation quality.
•Response to RQ3:As shown in Figs. 7a–7b, KGLlama-KD
retains competitive A2N translation quality after distillation,
achieving a mean VSO of 94.1% (±0.039) and a meanVNF
chainexactmatch (VC-EM) of 93.0% (±0.051). As reported
in Table V, the CVR is 0.00 on the evaluated test split
under the predefined dependency/mutual-exclusion rule set,
indicating that the predicted chains satisfy the schema-level
structural constraints of our NSR definition.
In terms of efficiency, Fig. 7c shows that KGLlama-
KD processes about 500 APPIs within 10 s (approximately
50 APPI/s), implying an average per-APPI processing time of
roughly 20 ms for the A2N translation stage under steady-
state execution. Together with the 31.2 ms KG construction
and reasoning latency reported in Table V, the two main
stages sum to approximately 51.2 ms per APPI, remaining
below 100 ms in our experimental setting. Moreover, Figs. 8
and 9 indicate high teacher–student agreement in terms of
both VNF-chain ordering (approximately 97% by Levenshtein
accuracy) and VNF component composition (approximately
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
12
/s75 /s71 /s76/s108/s97/s109 /s97/s45 /s75 /s68
/s75 /s71 /s76/s108/s97/s109 /s97 /s68/s101/s101/s112/s83 /s101/s101/s107 
/s81 /s119/s101/s110 /s76/s108/s97/s109 /s97
/s72/s121 /s112/s101/s114 /s84 /s114 /s97/s110/s115 /s45 /s67/s65 
/s84 /s114 /s97/s110/s115 /s102 /s111/s114 /s109 /s101/s114 
/s48/s46 /s48
/s48/s46 /s50
/s48/s46 /s52
/s48/s46 /s54
/s48/s46 /s56
/s49/s46 /s48
/s49/s46 /s50
/s49/s46 /s52
/s86 /s78/s70 /s32 /s67/s111/s109 /s112/s111/s115 /s105/s116 /s105/s111/s110/s32 /s83 /s105/s109 /s105/s108/s97/s114 /s105/s116 /s121 
/s32/s75 /s71 /s76/s108/s97/s109/s97/s45 /s75 /s68 /s32 /s32/s75 /s71 /s76/s108/s97/s109/s97
/s32/s68/s101/s101/s112/s83 /s101/s101/s107 /s32/s81 /s119/s101/s110
/s32/s76/s108/s97/s109/s97 /s32 /s32/s72/s121 /s112/s101/s114 /s84/s114 /s97/s110/s115 /s45 /s67/s65 /s32 
/s32/s84/s114 /s97/s110/s115 /s102/s111/s114 /s109/s101/s114 
/s48 /s46 /s57 /s52 /s49 /s32 /s177 /s32 /s48 /s46 /s48 /s51 /s57 
/s48 /s46 /s56 /s51 /s53 /s32 /s177 /s32 /s48 /s46 /s48 /s53 /s50 
/s48 /s46 /s57 /s50 /s55 /s32 /s177 /s32 /s48 /s46 /s48 /s52 /s53 
/s48 /s46 /s57 /s48 /s53 /s32 /s177 /s32 /s48 /s46 /s48 /s52 /s48 
/s48 /s46 /s57 /s50 /s56 /s32 /s177 /s32 /s48 /s46 /s48 /s51 /s52 
/s48 /s46 /s56 /s57 /s52 /s32 /s177 /s32 /s48 /s46 /s48 /s54 /s50 
/s48 /s46 /s57 /s55 /s54 /s32 /s177 /s32 /s48 /s46 /s48 /s50 /s50 
(a) VNF Component-Set Overlap in NSRs
/s75 /s71 /s76/s108/s97/s109 /s97/s45 /s75 /s68
/s75 /s71 /s76/s108/s97/s109 /s97 /s68/s101/s101/s112/s83 /s101/s101/s107 
/s81 /s119/s101/s110 /s76/s108/s97/s109 /s97
/s72/s121 /s112/s101/s114 /s84 /s114 /s97/s110/s115 /s45 /s67/s65 
/s84 /s114 /s97/s110/s115 /s102 /s111/s114 /s109 /s101/s114 
/s48/s46 /s52
/s48/s46 /s54
/s48/s46 /s56
/s49/s46 /s48
/s49/s46 /s50
/s49/s46 /s52
/s76/s101/s118 /s101/s110/s115 /s104/s116 /s101/s105/s110/s32 /s65 /s99 /s99 /s117/s114 /s97/s99 /s121 /s32 
/s32/s75 /s71 /s76/s108/s97/s109/s97/s45 /s75 /s68 /s32 /s32/s75 /s71 /s76/s108/s97/s109/s97
/s32/s68/s101/s101/s112/s83 /s101/s101/s107 /s32/s81 /s119/s101/s110
/s32/s76/s108/s97/s109/s97 /s32 /s32/s72/s121 /s112/s101/s114 /s84/s114 /s97/s110/s115 /s45 /s67/s65 /s32 
/s32/s84/s114 /s97/s110/s115 /s102/s111/s114 /s109/s101/s114 
/s48 /s46 /s57 /s51 /s48 /s32 /s177 /s32 /s48 /s46 /s48 /s53 /s49 
/s48 /s46 /s57 /s54 /s54 /s32 /s177 /s32 /s48 /s46 /s48 /s51 /s48 
/s48 /s46 /s56 /s52 /s53 /s32 /s177 /s32 /s48 /s46 /s48 /s53 /s57 
/s48 /s46 /s56 /s57 /s50 /s32 /s177 /s32 /s48 /s46 /s48 /s52 /s57 
/s48 /s46 /s56 /s54 /s54 /s32 /s177 /s32 /s48 /s46 /s48 /s55 /s55 
/s48 /s46 /s56 /s57 /s55 /s32 /s177 /s32 /s48 /s46 /s48 /s53 /s52 
/s48 /s46 /s55 /s54 /s55 /s32 /s177 /s32 /s48 /s46 /s48 /s53 /s55 (b) Levenshtein accuracy of predicted NSR
chains.
0 1 2 3 4 5 6 7 8 9 1 01 1050100150200250300350400450500550600D ata processing speed increased by 60%C
umulative processed APPIsP
rocessing time (s) 
Qwen KG-Llama DeepSeek Llama KGLlama-KD HyperTrans-CA Transformer
(c) Processing throughput.
Fig. 7. Comparison of KGLlama-KD and baselines for A2N translation: (a) VNF component-set overlap in NSRs, (b) Levenshtein accuracy of NSR chains,
and (c) Processing throughput.
1
1 0 .8811 0 .9691
2 3 4 5 0.00
.20
.40
.60
.81
.01
.2/s84/s101/s97/s99/s104/s101/s114/s8211/s83/s116/s117/s100/s101/s110/s116/s32/s65/s103/s114/s101/s101/s109/s101/s110/s116G
roup
Fig. 8.Teacher–student agreement on VNF-chain ordering across
groups, measured by Levenshtein-based chain similarity.
1
1 0 .9211 0 .9841
2 3 4 5 0.00
.20
.40
.60
.81
.01
.2/s84/s101/s97/s99/s104/s101/s114/s8211/s83/s116/s117/s100/s101/s110/s116/s32/s65/s103/s114/s101/s101/s109/s101/s110/s116G
roup
Fig. 9.Teacher–student agreement on VNF component composition
across groups, measured by VNF set overlap.
98% by VSO). As illustrated in Figs. 10 and 11, KGLlama-
KD consumes significantly less GPU power than the teacher
model during both training and inference, indicating that KG-
guided distillation can reduce energy-related overheads across
the model lifecycle. Such an efficiency profile is important
for real-world, large-scale deployments, especially in network-
edge server environments where near-real-time intent trans-
lation is required to enable rapid operational actions under
bounded compute and energy budgets.
0 2 004 006 008 001 0001 20005
01
001
502
002
503
00GPU PowerT
ime /s 
KGLlama-KD KGLlama
Fig. 10.GPU power consumption of KGLlama and KGLlama-KD
during training.
0 1 2 3 4 5 6 7 8 9 1 01 11 205
01
001
502
002
503
00Average GPU PowerT
ime /s 
KGLlama-KD KGLlama
Fig. 11.GPU power consumption of KGLlama and KGLlama-KD
during inference.
VII. CONCLUSION ANDFUTUREWORK
To advance the practical applicability of 6G intent-driven
autonomous networks, this paper presents KGLlama-KD, a
lightweight framework that augments a Llama 3 founda-
tion model with domain KGs and compresses it via KD
for network-edge use. Extensive experiments show improved
translation accuracy and reduced inference latency in our
experimental setting, suggesting a viable pathway toward
deployment-friendly intent translation at the network edge.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
13
More broadly, our results highlight KG-guided distillation as
a promising avenue to make large model based intent trans-
lation more deployment-friendly in cloud–edge collaborative
architectures.
While our current evaluation focuses on a high-performance
edge-server setting, future work will benchmark KGLlama-
KD on representative gateway-class far-edge platforms (e.g.,
Jetson-class devices and industrial edge gateways) and study
multi-site deployment considerations in real-world large-scale
settings. We will investigate additional compression (e.g.,
quantization-aware distillation) under stricter power and ther-
mal budgets. Furthermore, we will explore reinforcement
learning (RL)-based self-adaptation for decentralized intent
interpretation at the network edge, developing lightweight,
resource-aware RL strategies that balance adaptation effective-
ness with model compactness.

## § References

[1] IMT-2030 (6G) Promotion Group, “6G Vision And Candidate Technolo-
gies,” Ministry of Industry And Information Technology (MIIT), Tech.
Rep., Jun. 2021, accessed: 17 Apr. 2025.
[2] Z. Feng, Z. Wei, X. Chen, H. Yang, Q. Zhang, and P. Zhang, “Joint
Communication, Sensing, And Computation Enabled 6G Intelligent
Machine System,”IEEE Netw., vol. 35, no. 6, pp. 34–42, 2021.
[3] S. Zou, M. Liwang, B. Wu, W. Wu, Y . Sun, and W. Ni, “Intent-Oriented
Network Slicing With Hypergraphs,”IEEE Netw, pp. 1–1, 2024.
[4] A. Clemm, L. Ciavaglia, L. Qiang, and J. Tantsura, “Intent-Based Net-
working—concepts And Definitions,” Internet Engineering Task Force
(IETF), Internet-Draft draft-irtf-nmrg-ibn-concepts-definitions-07, 2020,
work in Progress.
[5] D. Wang, S. Zou, M. Liwang, W. Ni, and X. Wang, “Intent-Driven
Cognitive XDFC Bridge In Endogenous Intelligent IIot: A Systematic
Review And S²Croft Architecture With Bayesian-CRO-Fuzzy Synergy,”
IEEE Trans. Netw. Sci. Eng., 2025, submitted for publication.
[6] Huawei Technologies Co., Ltd., “6G: The Next Horizon,” Huawei
Technologies, Tech. Rep., Jul. 2022, accessed: 17 Apr. 2025.
[7] Cisco Systems, Inc., “Intent-Based Networking And Extending The En-
terprise,” Cisco Systems, Tech. Rep., Oct. 2022, accessed: 17 Apr. 2025.
[8] P. Yang, X. Xi, T. Q. S. Quek, J. Chen, X. Cao, and D. Wu, “How Should
I Orchestrate Resources Of My Slices For Bursty URLLC Service
Provision?”IEEE Trans. Commun., vol. 69, no. 2, pp. 1134–1146, 2021.
[9] A. Matencio-Escolar, Q. Wang, and J. M. Alcaraz Calero,
“SliceNetVSwitch: Definition, Design And Implementation Of 5G
Multi-Tenant Network Slicing In Software Data Paths,”IEEE Trans.
Netw. Serv. Manag., vol. 17, no. 4, pp. 2212–2225, 2020.
[10] K. Qu, W. Zhuang, Q. Ye, X. Shen, and J. Rao, “Dynamic Flow
Migration For Embedded Services In SDN/NFV-Enabled 5G Core
Networks,”IEEE Trans. Commun., vol. PP, no. 99, pp. 1–1, 2020.
[11] W. Zhuang, Q. Ye, F. Lyu, N. Cheng, and J. Ren, “SDN/NFV-empowered
Future Iov With Enhanced Communication, Computing, And Caching,”
Proceedings of the IEEE, vol. 108, no. 2, pp. 274–291, 2019.
[12] K. B. Letaief, Y . Shi, J. Lu, and J. Lu, “Edge Artificial Intelligence For
6G: Vision, Enabling Technologies, And Applications,”IEEE J. Sel.
Areas Commun., vol. 40, no. 1, pp. 5–36, 2022.
[13] Y . Shen, J. Shao, X. Zhang, Z. Lin, H. Pan, D. Li, J. Zhang, and K. B.
Letaief, “Large Language Models Empowered Autonomous Edge AI
For Connected Intelligence,”IEEE Commun. Mag., vol. 62, no. 10, pp.
140–146, 2024.
[14] J. Peng, H. Tang, C. Wang, X. Gu, and H. Peng, “Intelligent Vehicles
Lane-Changing Intention Identification Method With Driving Style
Recognition,” inProc. 27th Int. Conf. Comput. Supported Cooperative
Work Des. (cscwd), 2024, pp. 3036–3041.
[15] J. Huang, C. Yang, S. Kou, and Y . Song, “A Brief Survey And Imple-
mentation On AI For Intent-Driven Network,” inProc. 27th Asia–pacific
Conf. Commun. (apcc), 2022, pp. 413–418.
[16] T. Yuan, X. Zhao, R. Liu, Q. Yu, X. Zhu, S. Wang, and K. Meinke,
“Driving Intention Recognition And Speed Prediction At Complex
Urban Intersections Considering Traffic Environment,”IEEE Trans.
Intell. Transp. Syst., vol. 25, no. 5, pp. 4470–4488, 2024.
[17] A. Chowdhary, A. Sabur, N. Vadnere, and D. Huang, “Intent-Driven
Security Policy Management For Software-Defined Systems,”IEEE
Trans. Netw. Serv. Manag., vol. 19, no. 4, pp. 5208–5223, 2022.
[18] J. Mcnamara, D. Camps-Mur, M. Goodarzi, H. Frank, L. Chinchilla-
Romero, F. Ca ˜nellas, A. Fern ´andez-Fern´andez, and S. Yan, “NLP
Powered Intent Based Network Management For Private 5G Networks,”
IEEE Access, vol. 11, pp. 36 642–36 657, 2023.
[19] B. Wu, S. Zou, M. Liwang, W. Ni, and X. Wang, “Explainable
Application Intent For Zero-touch Networking: An Incorporation Of
Hypergraph And Transformer,”IEEE Trans. Commun., pp. 1–1, 2025.
[20] A. Caciularu, N. Raviv, T. Raviv, J. Goldberger, and Y . Be’ery,
“Perm2Vec: Attentive Graph Permutation Selection For Decoding Of
Error Correction Codes,”IEEE J. Sel. Areas Commun., vol. 39, no. 1,
pp. 79–88, 2021.
[21] J. Guo and C. Yang, “Learning Power Allocation For Multi-Cell-Multi-
User Systems With Heterogeneous Graph Neural Networks,”IEEE
Trans. Wireless Commun., vol. 21, no. 2, pp. 884–897, 2022.
[22] Y . Shen, J. Zhang, S. H. Song, and K. B. Letaief, “Graph Neural
Networks For Wireless Communications: From Theory To Practice,”
IEEE Trans. Commun., vol. 22, no. 5, pp. 3554–3569, 2023.
[23] O. G. Lira, O. M. Caicedo, and N. L. S. d. Fonseca, “Large Language
Models For Zero Touch Network Configuration Management,”IEEE
Commun. Mag., pp. 1–8, 2024.
[24] Y . Du, H. Deng, S. C. Liew, K. Chen, Y . Shao, and H. Chen, “The
Power Of Large Language Models For Wireless Communication Sys-
tem Development: A Case Study On Fpga Platforms,”arXiv preprint
arXiv:2307.07319, 2023.
[25] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman,
D. Almeida, J. Altenschmidt, S. Altman, S. Anadkatet al., “GPT-4
Technical Report,”arXiv preprint arXiv:2303.08774, 2023, accessed:
17 Apr. 2025. [Online]. Available: https://arxiv.org/abs/2303.08774
[26] G. Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut,
J. Schalkwyk, A. M. Dai, A. Hauth, K. Millicanet al., “Gemini:
A Family Of Highly Capable Multimodal Models,”arXiv preprint
arXiv:2312.11805, 2023, accessed: 17 Apr. 2025. [Online]. Available:
https://arxiv.org/abs/2312.11805
[27] S. Sadeghi, A. Bui, A. Forooghi, J. Lu, and A. Ngom, “Can Large
Language Models Understand Molecules?” 2024. [Online]. Available:
https://arxiv.org/abs/2402.00024
[28] E. J. Hu, Y . Shen, P. Wallis, Z. Allen-Zhu, Y . Li, S. Wang,
L. Wang, and W. Chen, “LoRA: Low-rank Adaptation Of Large
Language Models,”arXiv preprint arXiv:2106.09685, 2021, accessed:
17 Apr. 2025. [Online]. Available: https://arxiv.org/abs/2106.09685
[29] G. Hinton, O. Vinyals, and J. Dean, “Distilling The Knowledge In
A Neural Network,”arXiv preprint arXiv:1503.02531, 2015, accessed:
17 Apr. 2025. [Online]. Available: https://arxiv.org/abs/1503.02531
[30] X. Jiao, Y . Yin, L. Shang, X. Jiang, X. Chen, L. Li, F. Wang, and Q. Liu,
“TinyBERT: Distilling BERT for Natural Language Understanding,”
arXiv preprint arXiv:1909.10351, 2019.
[31] Y . Zhang, H. Liu, Y . Xiao, M. Amoon, D. Zhang, D. Wang, S. Yang,
and C. Quek, “LLM-Enhanced Multi-Teacher Knowledge Distillation
For Modality-Incomplete Emotion Recognition In Daily Healthcare,”
IEEE J. Biomed. Health Inform., 2024, early Access.
[32] J.-F. Qu, P. Fournier-Viger, M. Liu, B. Hang, and C. Hu, “Mining High
Utility Itemsets Using Prefix Trees And Utility Vectors,”IEEE Trans.
Knowl. Data Eng., vol. 35, no. 10, pp. 10 224–10 236, 2023.
[33] J. Wang and Y . Dong, “Measurement of text similarity: a survey,”
Information, vol. 11, no. 9, p. 421, 2020.
[34] J. Li, S. Zou, Y . Sun, H. Gao, and W. Ni, “Business Intent And Network
Slicing Correlation Dataset From Data-Driven Perspective,”SCI DATA,
vol. 12, no. 1, p. 419, 2025.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply. 
14
Bing WuBing Wu received an M.S. degree in
the Department of Science and Technology, Com-
munication University of China (CUC), China, in
2019. From 2019 to 2021, he worked as a Cloud
Computing Engineer at China Unicom Southeast
Research Institute. From 2021 to 2022, he worked
as a Big Data Mining Engineer at Henan Shuanghui
Investment and Development Co., Ltd. He is cur-
rently pursuing a Ph.D. degree in Big Data and
Information Engineering at Guizhou University. His
research interests include 6G networks, data mining,
and next-generation networks.
Sai Zou(Senior Member, IEEE) Sai Zou received
a Ph.D. degree in Communication Engineering from
Xiamen University, China, in 2018, an M.S. degree
in Software Engineering from Hunan University,
China, in 2007, and a B.S. degree in Computer
Science from Hengyang Normal University, China,
in 2004. Currently, he is the director of the Guizhou
Cloud-Network Collaborative Innovation Center and
the Guizhou Cloud-Network Collaborative Deter-
ministic Transmission Engineering Center, and a
professor with Guizhou University, China. He was
a visiting research scholar at CSIRO, Sydney, Australia, from 2017 to 2018,
and a postdoctoral fellow at UESTC, China, from 2020 to 2022. He received
the “Thousand Innovative Talents” title in Guizhou Province and the “Young
Bayu Scholar” title in Chongqing. His research interests include 5G/6G
technologies, the Internet of Things, and machine learning.
Minghui Liwang[M’19] (Senior Member, IEEE) is
currently an associate professor with the Department
of Control Science and Engineering and the Shang-
hai Research Institute for Intelligent Autonomous
Systems, Tongji University, China. Her research in-
terests include multi-agent systems, edge computing,
and distributed learning, as well as economic models
and applications.
Wei Ni(M’09-SM’15-F’24) received the B.E. and
Ph.D. degrees in Electronic Engineering from Fudan
University, Shanghai, China, in 2000 and 2005,
respectively. He is the Associate Dean (Research) in
the School of Engineering, Edith Cowan University,
Perth, and a Conjoint Professor at the University
of New South Wales, Sydney, Australia. He also
serves as Technical Expert at Standards Australia in
the area of artificial intelligence and big data. He
was a Deputy Project Manager at the Bell Labs,
Alcatel/Alcatel-Lucent from 2005 to 2008; a Senior
Research Engineer at Devices R&D, Nokia from 2008 to 2009; and a
Senior Principal Research Scientist and Group Leader at the Commonwealth
Scientific and Industrial Research Organisation (CSIRO) from 2009 to 2025.
He has co-authored four books, eleven book chapters, over 550 technical
papers, 27 patents, and ten standard proposals accepted by IEEE. His research
interests include machine learning, online learning, stochastic optimization,
and their applications to system efficiency and integrity.
Dr. Ni has been an Editor for IEEE Transactions on Wireless Com-
munications since 2018, IEEE Transactions on Vehicular Technology since
2022, IEEE Transactions on Information Forensics and Security and IEEE
Communication Surveys and Tutorials since 2024, and IEEE Transactions on
Network Science and Engineering since 2025. He served first as Secretary,
then Vice-Chair and Chair of the IEEE VTS NSW Chapter from 2015 to
2022, Track Chair for VTC-Spring 2017, Track Co-chair for IEEE VTC-
Spring 2016, Publication Chair for BodyNet 2015, and Student Travel Grant
Chair for WPMC 2014.
Xianbin Wang[S’98, M’99, SM’06, F’17](Fellow,
IEEE) received his Ph.D. degree in electrical and
computer engineering from the National University
of Singapore in 2001. He has been with Western
University, Canada, since 2008, where he currently
serves as a Distinguished University Professor and
a Tier-1 Canada Research Chair in Trusted Commu-
nications and Computing. Prior to joining Western
University, he was with the Communications Re-
search Centre Canada as a Research Scientist and
later a Senior Research Scientist from 2002 to 2007.
From 2001 to 2002, he was a System Designer at STMicroelectronics. His
current research interests include 5G/6G technologies, Internet of Things,
machine learning, communications security, digital twin, and intelligent com-
munications. He has over 600 highly cited journals and conference papers,
in addition to over 30 granted and pending patents and several standard
contributions.
Dr. Wang is a Fellow of the Canadian Academy of Engineering and a Fellow
of the Engineering Institute of Canada. He has received many prestigious
awards and recognitions, including the IEEE Canada R. A. Fessenden Award,
Canada Research Chair, Engineering Research Excellence Award at Western
University, Canadian Federal Government Public Service Award, Ontario
Early Researcher Award, and ten Best Paper Awards. He is currently a
member of the Senate, Senate Committee on Academic Policy and Senate
Committee on University Planning at Western. He also serves on NSERC
Discovery Grant Review Panel for Computer Science. He has been involved
in many flagship conferences, including IEEE GLOBECOM, ICC, VTC,
PIMRC, WCNC, CCECE, and ICNC, in different roles, such as General Chair,
TPC Chair, Symposium Chair, Tutorial Instructor, Track Chair, Session Chair,
and Keynote Speaker. He serves/has served as the Editor-in-Chief, Associate
Editor-in-Chief, Area Editor, and editor/associate editor for over ten journals.
He was the Chair of the IEEE ComSoc Signal Processing and Computing for
Communications (SPCC) Technical Committee and is currently serving as the
Central Area Chair of IEEE Canada.
Youliang Tianreceived the B.Sc. degree in math-
ematics and applied mathematics and the M.Sc.
degree in applied mathematics from Guizhou Uni-
versity, China, in 2004 and 2009, respectively, and
the Ph.D. degree in cryptography from Xidian Uni-
versity, Xi’an, China, in 2012. From 2012 to 2015,
he was a Postdoctoral Researcher with the State Key
Laboratory of the Chinese Academy of Sciences.
He is currently a Professor and Ph.D. Supervisor
with the College of Big Data and Information Engi-
neering, Guizhou University. His research interests
include algorithmic game theory, cryptography, and security protocols.
This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3678546
© 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted,
but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 01:08:01 UTC from IEEE Xplore.  Restrictions apply.
