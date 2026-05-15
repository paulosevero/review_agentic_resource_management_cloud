---
paper_id: "paper-2779"
source_pdf_sha: "66dcfd2bc4602cd90897fa2c8ed6fe8f0a5944dfed6f703edf06af5bf00afd7a"
extraction_quality: high
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 15
  page_count: 21
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2779 — fulltext
## §unknown-1

Received 3 February 2026, accepted 15 February 2026, date of publication 18 February 2026, date of current version 24 February 2026.
Digital Object Identifier 10.1 109/ACCESS.2026.3665989
Cluster Workload Allocation: Semantic Soft
Affinity Using Natural Language Processing
LESZEK SLIWKO
 1, (Member, IEEE), AND JOLANTA MIZERIA-PIETRASZKO
 2, (Member, IEEE)
1Standard Chartered Bank, EC2V 5DD London, U.K.
2Department of Computer Science, Opole University of Technology, 45-758 Opole, Poland
Corresponding author: Leszek Sliwko (leszek.sliwko@sc.com)
This work was supported in part by the AI Research & Experiment Department, Standard Chartered Bank.
ABSTRACT Cluster workload allocation often requires complex configurations, creating a usability gap.
This paper introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural
Language Processing. The system employs a Large Language Model (LLM) integrated via a Kubernetes
scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences.
A prototype featuring a cluster state cache and an intent analyzer (using AWS Bedrock) was developed.
Empirical evaluation demonstrated high LLM parsing accuracy (>95% Subset Accuracy on an evaluation
ground-truth dataset) for top-tier models like Amazon Nova Pro/Premier and Mistral Pixtral Large, signifi-
cantly outperforming a baseline engine. Scheduling quality tests across six scenarios showed the prototype
achieved superior or equivalent placement compared to standard Kubernetes configurations, particularly
excelling in complex and quantitative scenarios and handling conflicting soft preferences. The results
validate using LLMs for accessible scheduling but highlight limitations like synchronous LLM latency,
suggesting asynchronous processing for production readiness. This work confirms the viability of semantic
soft affinity for simplifying workload orchestration and presents a proof-of-concept design.
INDEX TERMS Artificial intelligence, Kubernetes, load balancing, semantic parsing, soft-affinity, task
assignment.

## § Introduction

In any large-scale computing environment, from cloud data
center to supercomputing cluster, the scheduler is one of the
most critical components. Its fundamental purpose is to act as
a primary coordinator, intelligently assigning user-submitted
tasks, ranging from long-running services through short-
lived data analysis jobs, to the most appropriate machines.
The design of these schedulers has been a central research
topic for decades, resulting in influential systems that define
contemporary resource management. Representative exam-
ples include Google’s Borg [9], which demonstrates how
to orchestrate a vast and diverse collection of applications
at unprecedented scale; Apache Hadoop Y ARN [8], which
decouples resource management from job execution and has
become the standard for big data workloads; and the SLURM
The associate editor coordinating the review of this manuscript and
approving it for publication was Sangsoon Lim
.
Workload Manager, which dominates in High-Performance
Computing (HPC) environments.
Schedulers typically make decisions based on two cat-
egories of rules: hard and soft ones. Hard rules, also
known as constraints, represent absolute, non-negotiable
requirements that a program needs to satisfy. For example,
a graphics-intensive application may require a node equipped
with a specific type of GPU. The scheduler first filters out all
the machines that do not satisfy these constraints. If none of
them qualify, the job is not scheduled, ensuring that applica-
tions never run in incompatible environments.
Once the scheduler identifies the machines satisfying all
the hard rules, it applies the soft rules, or the preferences,
to select the optimal candidate. These act as a guidance rather
than some strict requirements, i.e. for preferring nodes that
are lightly loaded or located near a data source in order to
minimize latency. The scheduler assigns scores to the valid
machines based on these preferences, optimizing for met-
rics such as performance or energy efficiency. Considerable
28054

 2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/ VOLUME 14, 2026
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
research has focused on fairness and preference models,
including Dominant Resource Fairness (DRF), which ensures
equitable resource allocation among heterogeneous users [1].
These principles have been implemented in various
systems. The Apache Mesos scheduler introduced a
‘‘resource offer’’ mechanism to manage constraints[3], while
Firmament adopted a network-flow-based model to acceler-
ate placement decisions [2]. Despite their significant architec-
tural differences, these systems share a common limitation:
they require operators to express scheduling goals in rigid,
machine-readable syntax.
This leads to a significant semantic gap between human
intent and machine-level configuration. A developer might
express an intuitive request such as ‘‘Run this machine
learning job on a powerful node, preferably one that isn’t
overloaded and is located in Europe.’’ To achieve this in
systems like Kubernetes, users must write complex Y AML
files specifying numerous fields and weighted values. This
process is time-consuming, error-prone, and demands deep
system expertise.
This paper introduces a new system designed to bridge
that gap. The presented intelligent scheduler employs a
Large Language Model (LLM) as a translation layer between
natural-language user intent and the scheduler’s structured
directives. Developers can specify scheduling preferences
in plain English (or any other supported language), and
the model automatically generates the corresponding con-
figuration, enabling the scheduler to make human-aligned
placement decisions. The current prototype is intended as
a research artifact to demonstrate the feasibility and is not
production-ready.
The primary contribution is the design and implementation
of a semantic, intent-driven scheduling paradigm for Kuber-
netes, which leverages an LLM to translate natural-language
requirements into low-level scheduling logic. Specifically,
the other contributions are:
• Semantic Scheduling: A shift from declarative, syntax-
bound configuration (e.g., Y AML with nodeAffinity)
toward semantic, intent-based expressions. This reduces
cognitive overhead for developers and supports more
flexible workload specification.
• Dynamic and Extensible Logic: Traditional schedulers
require writing and compiling new plug-ins in the Go
programming language to incorporate custom logic. The
presented approach allows new scheduling behaviors
to be introduced dynamically by defining new Intent
classes and updating the LLM prompt, with the aim of
improving adaptability.
• Real-Time Contextual Awareness: By combining a
live cluster state cache with the reasoning capabilities
of an LLM, the system enables nuanced soft-affinity
decisions (e.g., prefer_colocate_same_deployment,
spread_zones) that go beyond static affinity and anti-
affinity mechanisms.
The remainder of this paper is structured as follows: SectionII
reviews related work in cluster scheduling, highlighting exist-
ing approaches to affinity and resource management. Sec-
tion III details the design and implementation of the prototype
system and testbed environment, including the Kubernetes
cluster simulation, the Cluster State Cache, the Score Exten-
der Service, and the LLM-based Intent Analyzer module
responsible for semantic parsing. Section IV details the
mathematical formulas underlying the intent-driven scoring
logic and explains the scalarization of the final score. Sec-
tion V presents the empirical evaluation, focusing first on the
accuracy of intent recognition using various LLMs against
an evaluation dataset and then outlining the methodology
for assessing scheduling efficiency and placement quality.
Finally, Section VI concludes the paper by summarizing
the key findings, discussing the limitations of the current
prototype, and proposing directions for future research.
II. RELATED WORKS
This section surveys foundational and contemporary research
pertinent to the proposed system, structured across four
principal domains. The first is AI in Cluster Scheduling, con-
trasting conventional policy-driven schedulers with ML and
LLM-assisted approaches. The topic of semantic soft affinity
intersects resource scheduling, ML-driven affinity prediction,
and semantic analysis, drawing from workload trace anal-
ysis and AI-based scheduling. The second, Multi-Objective
Scheduling (MOO), addresses the trade-offs in competing
performance goals. The prototype’s additive scoring model
is a weighted-sum strategy. The third, Intent-Based Systems
(IBS), focuses on bridging the ‘‘semantic gap’’ between
high-level intents and low-level configurations. Lastly, Pars-
ing and Natural Language Interfaces covers semantic parsing
for converting linguistic input into machine-interpretable
policies.
These research areas directly influence the system’s archi-
tectural design. Insights from IBS and Natural Language
Parsing (NLP) inform the Intent Analyzer. The foundations of
MOO underpin the Score Extender Service, while advances
in AI-assisted Scheduling guide the Cluster State Cache.
A. AI IN CLUSTER SCHEDULING
Cluster scheduling is a central topic in distributed sys-
tems. Foundational systems like Google Borg [9], Apache
Mesos [3], Quincy [4], and Firmament [2] established prin-
ciples of fairness and resource sharing. Hadoop Y ARN [8]
and SLURM are standards for big data and HPC. These
schedulers rely on hard-coded rules and manual, declarative
configuration.
Real-world traces, like Google’s Cluster Data, offer foun-
dations for understanding workload patterns. Alam et al. [38]
clustered workloads by resource usage, revealing job distri-
butions and symmetries. This supports semantic soft affinity
by showing how clustering can identify resource preferences
without hard constraints, enabling NLP-based grouping.
Research conducted by Mishra et al. [42] also characterized
VOLUME 14, 2026 28055
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
Google workloads, noting elasticity and variability that
inform soft affinity models.
ML is increasingly used to predict node-task affinities.
Research by [40] proposed an ML ensemble to detect con-
straint operators, achieving 98% accuracy in affinity predic-
tion. This predictive method could integrate NLP to parse
metadata for softer, meaning-based affinities. Similarly, Mao
et al. [6] introduced Decima, an RL framework that learns
scheduling policies, improving job completion times. Dec-
ima’s approach offers a basis for using NLP-derived semantic
similarities.
Reviews highlight AI’s role in overcoming traditional
scheduling limitations. A study by [39] surveyed DL
workload scheduling in GPU datacenters, noting techniques
to optimize utilization, which underscores the need for
semantic tools like NLP to handle diverse workloads. The
survey conducted by [44] on AI-driven job scheduling exam-
ines ML, RL, and hybrid models for dynamic allocation.
Zhou et al. [43] reviewed deep RL for cloud resource
scheduling, emphasizing adaptive policies for NP-hard prob-
lems and suggesting semantic parsing extensions.
ML-assisted scheduling, using models to guide placement,
is seen in systems like DeepRM[5] and Decima [6]. However,
these approaches use fixed quantitative inputs, lack a natural
language UI, and do not address the semantic gap between
intent and configuration.
The emergence of LLMs inspired research into semantic,
intent-driven configuration. OpenDevin [10] shows LLMs
can interpret natural-language DevOps commands into con-
figurations, using schema-guided extraction for deterministic
parsing. Research by [7] also shows models can translate
high-level goals into actions, though often outside latency-
critical paths.
A growing body of research explores LLM-assisted cluster
management, using natural-language understanding for con-
figuration or categorization. Recent work by Jaillet et al. [11]
focuses on scheduling LLM inference tasks with Key-V alue
cache constraints. These studies show an increasing inter-
section between natural-language reasoning and resource
management. The present work extends this by focusing on
semantic intent translation for soft-affinity scheduling, using
an LLM with a live scheduler extender and a reproducible
testbed. It contributes to integrating natural-language inter-
faces into infrastructure orchestration, emphasizing repro-
ducibility, determinism, and quantitative evaluation.
B. MUL TI-OBJECTIVE SCHEDULING
The task of cluster scheduling is fundamentally a MOO prob-
lem, requiring trade-offs between conflicting objectives [33].
For example, maximizing fault tolerance by spreading pods
(a spread_zones intent) conflicts with minimizing net-
work latency by co-locating them on the same nodes (a
prefer_colocate_same_deployment intent). Other conflicts
include balancing resource utilization versus consolidating
workloads for energy savings [31], or minimizing cost versus
minimizing job completion time [34].
Formally, these problems seek Pareto optimal solutions,
where no objective can be improved without degrading
another. Research employs two main strategies: evolutionary
algorithms (e.g., Non-dominated Sorting Genetic Algorithm
II) to find the Pareto front, or scalarization. Scalarization,
the more common approach, converts the multi-objective
problem into a single-objective one, often via a weighted-sum
method [34].
A key challenge is that presenting an entire Pareto front
is impractical for real-time decisions. This led to preference-
based optimization, using high-level user preferences to guide
the selection of a single best-fit solution. User preferences
define the weights or constraints for the scalarization func-
tion [32]. The allocation hint proposed in this work serves this
function; it is a mechanism for capturing unstructured prefer-
ences and translating them, via an LLM, into the quantitative
weights for the scheduler’s multi-objective cost function.
C. INTENT-BASED SYSTEMS
Research in IBS addresses the ‘‘semantic gap’’ between
high-level human goals and low-level system configura-
tion [13]. The premise is that operators should specify what
they want (e.g., ‘‘ensure low latency’’) rather than how to
achieve it (e.g., setting specific routing rules) [14]. This
declarative, policy-driven model aims to replace imperative,
error-prone manual configurations, reducing human error and
cognitive overhead [16]. The core challenge is translating
these abstract, human-centric goals into precise, machine-
executable instructions.
An IBS typically operates as a continuous, closed-loop
lifecycle [21]. This loop includes: intent ingestion (capturing
the objective); translation (converting the intent into formal
policies); validation (ensuring policies are achievable and
non-conflicting); actuation (orchestrating policies via con-
trollers); and assurance (continuously monitoring the state to
ensure the intent is met) [18]. If intent drift is detected, the
system takes corrective action, completing the autonomous
loop.
The intent ingestion and translation phases are most rele-
vant to this work. Traditionally, these use structured inputs
like GUIs or, more commonly, Domain-Specific Languages
(DSLs) [17]. DSLs allow operators to define complex intents
formally [20]. While an improvement, DSLs still require spe-
cialized training and present a steep learning curve, creating
a usability gap.
IBS principles are most applied in Intent-Based Network-
ing (IBN), particularly in SDN and managing 5G [24] and
6G [18] networks. Intents are used for traffic engineering, net-
work slicing, and enforcing dynamic QoS [21]. The paradigm
is also used in multi-cloud deployment [22] and defining
dynamic security policies [19].
To address the usability limitations of formal DSLs,
research has emerged to use natural language as the primary

## §28056 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
intent input. Early work explored NLP for translating user
commands into network control actions [23] or verifiable
policies [24]. The present work builds on this trajectory,
proposing that modern LLMs can serve as a more powerful
‘‘universal translator’’ for intent. By accepting unstructured
allocation hints, this approach aims to eliminate specialized
syntax, making intent-based scheduling accessible without
the steep learning curve of traditional IBS.
D. PARSING AND NATURAL LANGUAGE INTERFACES
The Intent Analyzer’s core function—translating an unstruc-
tured hint into a structured JSON object—is a semantic
parsing challenge. This is extensively studied in Natural Lan-
guage Interfaces to Databases (NLIDB), which aim to trans-
late plain text into a formal query language like SQL [12].
While traditional NLIDB systems struggled with ambiguity,
advances in deep learning and LLMs have significantly
enhanced semantic parser performance [15]. This research
applies these techniques to cluster scheduling, mapping text
to a scheduling policy rather than a database query.
To enable semantic soft affinity, NLP-driven clustering
of textual workload descriptions (e.g., job requirements) is
crucial. V eremyev et al. [41] apply graph-based clustering
to semantic spaces from word embeddings, revealing dense
communities that capture contextual meanings—directly
applicable to grouping similar jobs for soft allocation. This
aligns with broader NLP applications in resource manage-
ment, though explicit integration with cluster scheduling
remains underexplored.
The advent of deep learning introduced new text-to-SQL
architectures. Early sequence-to-sequence models struggled
with rigid SQL syntax[30]. This led to sketch-based methods,
where models like SQLNet learned to fill slots in a predefined
SQL sketch, improving accuracy [29]. Pre-trained transform-
ers like BERT enabled models such as SQLova to consider
both the question’s context and the database schema’s struc-
ture [27]. A critical sub-task is schema linking: identifying
relevant database tables and columns for a question. In large
databases, including the entire schema is inefficient; effective
schema linking prunes the schema to only relevant parts.
However, incorrectly omitting a required table can impede
correct query generation [26].
More recently, general-purpose LLMs have been applied to
the NLIDB problem. Unlike earlier models needing extensive
fine-tuning, LLMs can often perform text-to-SQL translation
in a zero-shot or few-shot setting, generating correct queries
for new schemas with little to no task-specific training [28].
This approach bypasses the costly data annotation process.
Despite progress, significant challenges remain [25].
Models still struggle with domain adaptation (handling spe-
cialized terminology) and logic grounding (understanding
abstract concepts). Generating highly complex SQL queries
remains a research frontier. These works form a strong foun-
dation, with gaps in NLP-specific semantic affinity offering
opportunities for novel contributions. Future research could
hybridize RL schedulers with NLP models for intent-based
soft affinities.
III. PROTOTYPE AND TESTBED DESIGN
To empirically evaluate the performance and efficacy of an
intent-based scheduling paradigm, a robust and reproducible
testbed is required. This section details the design and imple-
mentation of such an environment. The testbed is built around
a multi-node Kubernetes cluster simulated using Minikube,
alongside a custom scheduler extender. The extender inter-
cepts scheduling requests and translates high-level, natural-
language intents into concrete node-scoring decisions.
The environment (see Figure 1 for detail) is designed as a
self-contained representation of a topology-aware data cen-
ter, enabling the evaluation of complex scheduling policies
such as proximity preference, resource affinity, and workload
spreading. The core components include:
• Local Kubernetes Cluster: A multi-node Minikube
cluster deployed via Minikube with the Docker driver,
with nodes labeled to simulate a multi-level physical
topology.
• Cluster State Cache: A real-time, thread-safe subsys-
tem that maintains an up-to-date in-memory representa-
tion of cluster state.
• Score Extender Service : A stateful scheduler exten-
der microservice where the custom node-scoring logic
resides.
• Intent Analyzer: An NLP module leveraging AWS
Bedrock to access an LLM to translate user-provided
hints into structured scheduling intents.
Each of these modules, along with the testbed environment
as a whole, is described in detail in the following sections.
A. LOCAL KUBERNETES CLUSTER
The foundation of the experimental testbed is a local Kuber-
netes version 1.31.4 cluster deployed using Minikube, config-
ured with the Docker driver for node virtualization. This setup
provides a fully contained, reproducible environment suitable
for rapid iteration and controlled experimentation. Figure 2
shows how the cluster is initialized with nine nodes: one
dedicated control-plane node (minikube) and eight worker
nodes (minikube-m02 through minikube-m09). This topology
offers sufficient scale to evaluate scheduling behaviors across
multiple failure domains while maintaining the manageability
required for iterative testing.
The Minikube testbed is initialized using the Docker
driver, providing lightweight, containerized node virtualiza-
tion instead of full virtual machines. This approach offers
several advantages: it eliminates hypervisor configuration,
reduces resource overhead compared to VM-based drivers,
and shares the host’s networking stack for fast pod-scheduler
communication. These containerized nodes can be managed
via the Docker dashboard and programmatically scripted
(e.g., labeled, tainted), which makes the testbed highly repro-
ducible. This setup simplifies dependency management by
VOLUME 14, 2026 28057
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
FIGURE 1. Prototype system architecture, illustrating the interaction
between the main components: the Local Kubernetes Cluster (Minikube),
Cluster State Cache, Score Extender Service, Intent Analyzer, and AWS
Bedrock.
TABLE 1. Evaluation cluster topology.
using the host’s OS and runtime, providing a flexible platform
for experimenting with topology-aware scheduling, custom
extenders, and LLM-driven intent analysis without requiring
a production cluster.
A critical feature of the testbed is its emulation of
a physical network topology, necessary for validating
topology-aware scheduling intents such as prefer_
colocate_same_deployment, spread_zones, and prefer_
nearby_nodes_same_deployment. Immediately after cluster
initialization, a setup script programmatically labels the
worker nodes to define a hierarchical topology consistent
with standard Kubernetes conventions. The hierarchy uses
the following topology keys:
• Region (topology.kubernetes.io/region): All nodes share
a single region label, us-east-1.
• Zone (topology.kubernetes.io/zone): Two simulated
availability zones, us-east-1a and us-east-1b, are
assigned across the worker nodes.
• Rack (topology.kubernetes.io/rack): Five logical racks
(rack-1 through rack-5) are distributed across the zones,
FIGURE 2. Minikube cluster startup sequence (Kubernetes version
1.31.4). The cluster consists of nine nodes: one control-plane node
(minikube) and eight worker nodes (minikube-m02 through m09).
FIGURE 3. Minikube nodes displayed in the Docker Desktop dashboard.
This GUI tool provided a convenient way to monitor the state of the
Kubernetes cluster nodes and manage associated persisted state
(Volumes).
with two nodes per racks 1, 3, and 4, and one node per
rack 2 and 5.
Table 1 details the topology structure used in the fur-
ther evaluation scenarios. The labeling scheme enables the
prototype scheduler to interpret placement hints and make
decisions based on synthetic but realistic topology metadata,
closely mimicking the conditions of a multi-zone, multi-rack
data center environment. To ensure isolation of control-
plane operations, the control-plane node is tainted with node-
role.kubernetes.io/control-plane=:NoSchedule, preventing

## §28058 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
the placement of user workloads and reserving the node
exclusively for critical cluster management services such as
etcd, kube-apiserver, and kube-scheduler.
The Score Extender Service, which encapsulates the
semantic intent-based scheduling logic, is integrated directly
into the Kubernetes control-plane via a custom sched-
uler configuration file. This configuration modifies the
kube-scheduler manifest to include the custom extender and
adjust its scheduling behavior. Two configuration aspects are
especially important:
• Extender Weight: The extender’s weight in the sched-
uler configuration is set to 100, the maximum possible
value. This ensures that the extender’s node scores (rang-
ing from 0-100) dominate those from Kubernetes’ native
scoring plugins, giving the prototype primary control
over node selection.
• Disabling Default Scoring Plugins: To isolate the
effects of intent-based scheduling, several built-in
Kubernetes scoring plugins are explicitly disabled,
including NodeResourcesFit, TaintToleration, Inter-
PodAffinity, and DefaultPodTopologySpread. Disabling
these ensures that all node scoring and prioritization
decisions originate from the custom NLP-driven sched-
uler extender, allowing for accurate evaluation of its
independent behavior.
This Minikube-based testbed thus provides a controlled,
topology-aware sandbox that replicates key aspects of
real-world cluster scheduling while remaining lightweight
and reproducible. It enables precise measurement of schedul-
ing latency, accuracy, and correctness under various intent
configurations, while isolating the impact of the LLM-driven
logic from external Kubernetes behaviors. Notably, in Kuber-
netes, the scheduler evaluates resource availability based on
requested values rather than real-time monitoring of current
CPU load. Pod specifications include requests and limits
for CPU and memory, which are used during the filtering
phase to ensure a node has enough unallocated capacity to
satisfy a pod’s requirements. During this initial filtering phase
(/filter), native Kubernetes plugins like NodeResourcesFit
remain active to exclude nodes that cannot support the pod’s
mandatory resource needs. Only after nodes have passed
these hard-rule filters are they sent to the prioritization phase
(/prioritize), where the prototype’s custom extender applies
its additive scoring logic.
B. CLUSTER STATE CACHE
The scheduler extender must make rapid decisions based on
the current state of the entire cluster. Continuously querying
the Kubernetes API server for each /prioritize request is
computationally infeasible, as it would introduce prohibitive
latency and place an unsustainable load on the API server.
To address this, a thread-safe state management subsystem
the Cluster State Cache was implemented.
The Cluster State Cache is designed as a distributed
state synchronization mechanism that balances low-latency
responsiveness with eventual consistency. This service main-
tains a continuously updated, in-memory representation of
all nodes and pods, effectively serving as a high-speed local
mirror of the cluster’s state. It employs a hybrid update strat-
egy designed to balance real-time accuracy with long-term
consistency and fault tolerance:
• Real-time Watchers : The cache’s low-latency syn-
chronization is achieved through a set of real-time
watchers. Two dedicated background threads estab-
lish persistent watch connections to the Kubernetes
API server: the first for v1.list_node and the second
for v1.list_pod_for_all_namespaces. These watchers
are event-driven, receiving immediate notifications for
ADDED, MODIFIED, and DELETED events. Upon
receiving an event, the cache acquires a lock and updates
its internal dictionaries, ensuring that the in-memory
state reflects cluster changes with sub-second latency.
This real-time stream is essential for maintaining accu-
rate, up-to-date context for the scheduler’s scoring logic.
• Periodic Refresh: To protect against transient fail-
ures, missed events, or watch disconnects, the watcher
model is complemented by a periodic reconciliation
thread. This background process performs a full re-list
of all nodes and pods at regular intervals (e.g., every
60 seconds). This brute-force refresh ensures eventual
consistency and acts as a self-healing mechanism to
recover from desynchronization or partial state loss. All
modifications to shared data structures are protected
by lock objects guaranteeing full thread safety under
concurrent access.
To quantify the impact of cache update delays on dynamic
affinity intents, the Effective Pod Set (P eff ) model is defined.
During high-velocity pod bursts, the system compensates
for the inherent latency of the Kubernetes API by merging
confirmed API state (Papi) with a short-lived, 10-second TTL
local placement cache ( Plocal). This hybrid approach effec-
tively neutralizes race conditions, ensuring that subsequent
scheduling requests are aware of pending placements before
they are persisted in the central etcd datastore.
Furthermore, the performance loss associated with the
cache locking mechanism is mitigated through a data nor-
malization strategy. Rather than storing raw Kubernetes
API objects, the system converts them into lightweight
CachedNode and CachedPod data classes upon receipt.
During this one-time conversion, all computationally com-
plex parsing and normalization steps, such as converting
resource strings (’’100m’’, ‘‘10Gi’’) into numeric values,
and filtering topology labels, are performed. As a result, the
scoring logic can directly access pre-computed fields like
cached_node.cpu_count or cached_node.topology_labels,
eliminating runtime parsing overhead and significantly accel-
erating the scoring loop. By converting raw API objects into
lightweight data classes during the update phase, all com-
putationally expensive parsing is performed once and stored
in memory. This enables the scoring logic to achieve O (1)
VOLUME 14, 2026 28059
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
complexity for metadata access, representing a significant
theoretical efficiency gain over the O (N ) complexity and
network I/O overhead required by a full API query model.
C. SCORE EXTENDER SERVICE
The core of the custom scheduling logic resides in an external
microservice, implemented as a Python Flask application,
which exposes endpoints adhering to the Kubernetes sched-
uler extender webhook API [35]. This service is reachable by
the kube-scheduler process and handles two types of requests:
• /filter: This verb is used by the kube-scheduler to pre-
filter nodes. The current implementation performs min-
imal validation, such as ensuring nodes do not possess a
NoSchedule taint.
• /prioritize: This verb is responsible for scoring. The
kube-scheduler sends the pod specification and a list of
candidate nodes (those that passed the filter phase) to
this endpoint. The service returns a list of nodes with an
integer score from 0 to 100.
The extender service is stateful and integrates two key
subsystems: the Cluster State Cache and the Intent Ana-
lyzer. A significant challenge in this design is handling the
high-velocity burst-like creation of pods, such as during
a deployment scale-up. The Kubernetes API-driven Clus-
ter State Cache may not observe the placement of Pod
1 before Pod 2 is already being scheduled. This race
condition would render intents like spread_nodes or pre-
fer_colocate_same_deployment ineffective during the burst.
To mitigate this, the service implements a secondary, local
cache of recent placements with a very short time-to-live
(10 seconds). When the /prioritize endpoint selects a node,
it immediately writes this decision into the local cache. Sub-
sequent scoring requests query an ‘‘effective’’ list of pods,
a composite of the main Cluster State Cache and the recent
placements cache, ensuring that affinity logic functions cor-
rectly even during rapid, successive scheduling events.
The scoring logic within the /prioritize endpoint is a multi-
step process. First, the service retrieves the allocation hint
from the pod’s annotations and passes it to the Intent Ana-
lyzer. This module returns a structured dictionary of detected
Intent objects, along with their LLM-derived confidence and
strength scores. Once the intents are parsed, the service iter-
ates through each candidate node, calculating a final node
score that starts at zero. A base score is calculated for each
intent (100 divided by the total number of intents) to provide
an initial weight. The system then applies specific logic based
on the Intent class:
• Resource Preferences: For intents like prefer_gpu or
prefer_memory_gb, the service compares the meta-
data value from the intent (e.g., prefer_gpu_cores:
4.0) against the node’s corresponding property (e.g.,
cached_node.gpu_count) retrieved from the Cluster
State Cache.
• Topology Preferences: For intents like prefer_zones
or avoid_racks, the service checks the node’s topology
labels against the list of zones or racks provided in the
intent’s metadata.
• Dynamic Affinity: For colocation intents like pre-
fer_colocate_same_deployment, the service queries the
‘‘effective’’ pod list and counts existing pods from the
same deployment on the node.
• Spread Logic: For spread_ intents (e.g., spread_zones,
spread_nodes), the system builds a histogram of existing
pods from the ‘‘effective’’ pod list across the relevant
topology (e.g., {’zone-a’: 5, ’zone-b’: 2}). A least-
loaded algorithm is applied, assigning the highest score
to nodes in the least-populated domains.
If a node satisfies an intent, the calculated score is added
to its node score. This score is multiplied by both the intent
confidence and strength values provided by the Intent Ana-
lyzer. This weighting ensures that a high-confidence, high-
strength (e.g., ‘‘must have’’) intent has a greater impact
than a low-confidence, low-strength (e.g., ‘‘maybe prefer’’)
one. Conversely, ‘‘avoid’’ intents subtract a weighted score.
Finally, after all nodes are scored, the service normalizes the
results: the highest-scoring node is deterministically assigned
a score of 100, and all other nodes are scaled between 1 and
99. This deterministic step ensures a single, unambiguous
node is selected by the kube-scheduler in the event of a tie.
The scoring functions are detailed in the Section IV.
D. INTENT ANAL YZER
The core technical challenge Intent Analyzer solves is an NLP
task known as semantic parsing [36]: translating an unstruc-
tured natural language utterance into a structured, machine-
readable scheduling policies - in this case: a JSON object with
intents and metadata. Intent Analyzer key functionalities are
as follows:
• Reading and Sanitizing Allocation Hints: The Intent
Analyzer retrieves a natural language string from the
allocation_hint annotation on the Pod object, passed via
the /prioritize REST call. The hint is first processed
through a sanitization function to strip potentially mali-
cious characters and mitigate prompt injection risks.
• LLM-Based Intent Translation : The sanitized hint is
sent to an LLM endpoint as a part of larger prompt
(see Listing 1). In the testbed, AWS Bedrock with the
Amazon Nova Pro model is used by default. The prompt
instructs the LLM to analyze the hint and return a JSON
object mapping the user’s request to a predefined list of
intents along with accompanying metadata. To ensure
deterministic behavior and repeatable results, the model
parameters are set to temperature = 0.0 and nucleus
sampling (top-p) = 1.0. The maximum response length
is limited to 512 tokens; however, token encoding con-
ventions vary between models, so this limit may be
interpreted differently depending on the model used.
• Strength and Confidence Annotation: The LLM is
prompted to return not only the detected intents but also
a confidence score (0.0-1.0) and a strength multiplier

## §28060 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
(0.5, 1.0, or 1.5), reflecting the perceived importance of
each request. For transparency and auditing purposes,
the LLM also includes a strength explanation field,
briefly describing the rationale for the assigned strength
value.
To improve efficiency, the results of allocation hint analysis
are cached. Since pods within a single deployment frequently
share identical allocation hints, analyzing each pod individ-
ually would be redundant and slow. The Intent Analyzer
stores the structured JSON output keyed by the hint string,
ensuring that the expensive LLM call is performed only once
per unique allocation hint.
Table 2 outlines the specific scheduling intents recognized
by the Intent Analyzer. Each row specifies a unique intent,
its semantic meaning, and the required metadata, including
field names, data types, and example formats. The description
content is incorporated directly into the LLM prompt during
analysis to guide intent extraction. The intents are logically
grouped according to their scope or type of scheduling pref-
erence. This hierarchical organization mirrors the operational
scope of each scheduling rule:
• Colocation / Proximity: Placement of pods relative to
others within the same deployment.
• Topological Constraints: Region-level, zone-level, and
rack-level intents for preferring, avoiding, or distributing
pods across these boundaries.
• Node-level: Target specific servers based on node char-
acteristics.
• Deployment-level: Focus on proximity or separation
relative to pods from other applications.
• Resource-based: Define requirements related to intrin-
sic node characteristics, such as CPU, memory,
GPU/TPU availability, storage type, or network features.
This structure enables the LLM to systematically map natural
language hints to actionable scheduling policies while main-
taining clarity, reproducibility, and operational relevance.
Listing 1 presents the comprehensive prompt template
engineered to direct the AI in its specialized capacity as a
semantic parser for the Kubernetes scheduler. The prompt
explicitly establishes an accurate structured data extraction
task, assigning the LLM the persona of an ‘‘expert AI assis-
tant’’. This role definition aims to prime the model for pre-
cision and adherence to instructions. Its articulated ‘‘ONL Y
goal’’ is to analyze the unstructured allocation hint annotation
provided by users and translate it solely based on a predefined
list of intents into a machine-readable JSON format, adhering
strictly to the specified output format and extraction rules.
The core of the prompt is the ‘‘CRITICAL INSTRUC-
TIONS’’ section. These rules guide the AI’s behavior and
were developed through testing:
• Defining the Input Text: The prompt clearly marks
where the user’s request begins and ends using delim-
iters (—HINT START— and —HINT END—). This
instruction ensures the LLM focuses precisely on the
user’s text and does not misinterpret the surrounding
instructions.
• Matching Requests to Defined Intents: The AI is pro-
vided with a list of known scheduling requests, i.e.,
Intents. It must match phrases from the user’s hint to
these predefined intents. The instructions emphasize
selecting only obvious and clearly stated matches, mini-
mizing guesswork or subjective interpretation by the AI.
• Extracting Details Correctly (Metadata): This is a
vital and carefully refined instruction. When an intent is
matched, the AI must extract specific details accurately:
(i) using exact names - the AI must use the exact
predefined names for details (e.g., prefer_cpu_cores)
so the scheduler program correctly interprets them;
(ii) maintaining correct formats - details must adhere to
specified formats, e.g., numbers as floats (like 16.0), lists
as JSON arrays (like [‘ ‘us-east-1a’ ’, ‘ ‘us-east-1b’ ’]);
(iii) listing all Items - if the user lists multiple items
(like several regions), the AI is explicitly instructed to
list all of them exactly as written, without summarizing
or using wildcards (like us-east-1∗). This prevents loss of
information needed by the Score Extender Service; and
(iv) applying defaults - if the AI identifies an intent but
cannot confidently extract a required detail from the text,
it is instructed to use a default value (1.0 for numbers, []
for lists) rather than omitting the field. This ensures the
output JSON maintains a consistent structure.
• Indicating Confidence: For each intent identified, the
AI must provide a confidence score (0.0 to 1.0). This
score quantifies the AI’s certainty about the match,
allowing the scheduler logic to potentially weigh more
confident interpretations more heavily.
• Assessing Importance (Strength): The AI assigns a
strength score based on specific keywords identified in
the hint. A simplified three-point scale (0.5 for weak
words like ‘‘prefer’’, ‘‘maybe’’; 1.5 for strong words
like ‘‘must’’, ‘‘critical’’; 1.0 otherwise) is used, as initial
tests showed nuanced (i.e., float values between 0.0 to
1.0) scores were unreliable. If a non-default strength
is assigned, the AI must provide a brief explanation
quoting the keyword that justified it.
• Adhering to JSON Output Format: The prompt
strictly mandates that the AI output ONL Y a single,
valid JSON object, without any extra conversational text,
explanations, or code formatting. This is essential so the
scheduler program can directly parse the output without
needing complex pre-processing.
• Handling Untrusted Input: The user’s hint is explicitly
labeled as untrusted, and the AI is instructed not to
follow any instructions it might contain. This serves as
a safeguard, directing the AI to treat the hint purely as
text for analysis according to the predefined rules, rather
than as commands to execute.
Below the main instructions, the prompt template also
dynamically builds a list of possible intents with descriptions
VOLUME 14, 2026 28061
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
and metadata fields. This section provides the definitive list
(schema) of all valid scheduling requests the AI can identify.
Including detailed descriptions and metadata requirements
(see Table 2 ) helps the AI perform the matching task accu-
rately. Finally, the prompt also includes the JSON output
example, reinforcing the required format, data types, and
overall organization.
Together, these designed sections and instructions aim
to guide the LLM effectively, ensuring it reliably trans-
forms user requests into the structured data needed for the
intent-based scheduling system. The detailed nature of the
prompt reflects the iterative refinement process informed by
empirical evaluation on multiple LLMs.
IV. SCORING MODEL
The decision-making engine within the Score Extender Ser-
vice employs a deterministic, weighted additive utility func-
tion to evaluate candidate nodes. Unlike traditional binary
filtering, this approach allows for nuanced trade-offs between
conflicting soft preferences. Table 3 summarizes the symbols
used in the following equations.
Formally, letN represent the set of candidate nodes filtered
by the Kubernetes scheduler, and let J represent the set of
unique scheduling intents extracted by the Intent Analyzer.
The system calculates a raw score, Sraw (n), for each node
n ∈ N . The fundamental scoring equation is defined as the
summation of the weighted utility of all identified intents:
Sraw (n) =
∑
i∈I
µ (n, i) (1)
where µ (n, i) represents the utility function of a specific
intent i applied to node n. This utility function is derived from
the base weight of the intent relative to the total number of
directives, modulated by the LLM’s confidence and the user’s
semantic intensity.
V. UTILITY FUNCTION COMPONENTS
The utility function µ (n, i) is calculated as follows:
µ (n, i) = β · Ci · Wi · φi (n) (2)
The components are defined as:
• Base Weight (β): To ensure equal initial influence
among multiple directives, a base weight is calculated
dynamically as β = 100/ |J |.
• Confidence (C i): A scalar value Ci ∈ [0, 1], provided
by the Intent Analyzer, representing the probability that
the intent was correctly identified.
• Strength (W i): A multiplier Wi ∈ {0.5, 1.0, 1.5}
derived from linguistic modifiers, allowing the user’s
urgency to scale the impact of specific rules.
• Evaluation Logic (φ_i(n)): A domain-specific evalu-
ation function that returns a scalar value based on how
well node n satisfies intent i.
A. EVALUATION LOGIC CATEGORIES
The evaluation logic φi (n) varies based on the semantic
category of the intent:
φpref (n) =
{
1 if n satisfies condition
0 otherwise (3)
1. Binary Preference Logic: For resource or topology
attributes (e.g., prefer_gpu), the function acts as a
binary indicator:
φavoid (n) =
{
−2 if n matches criteria
0 otherwise (4)
2. Avoidance Penalty Logic: For negative constraints
(e.g., avoid_zones), the system applies a weighted
penalty. To enforce avoidance strongly, the prototype
applies a doubled magnitude subtraction:
φspread (n) = M − kn + 1
M + 1 (5)
3. Distribution and Spreading Logic: For intents requir-
ing high availability (e.g., spread_zones), the system
calculates a least-loaded score. Let kn be the count of
pods belonging to the same deployment in the topology
domain of node n, and M be the maximum count of
such pods in any domain. The spreading score is nor-
malized as:
B. NORMALIZATION AND DETERMINISTIC SELECTION
To ensure compatibility with the Kubernetes scheduler exten-
der API, raw scores are normalized to the range [0, 100].
First, negative scores are clamped to zero. Then, scores are
scaled relative to the highest raw score observed in the current
iteration:
Snorm (n) = max (0, Sraw (n))
max
m∈N
(Sraw (m)) × 100 (6)
To eliminate non-determinism in tie-breaking scenarios, the
system enforces an only-one-winner-node adjustment. The
node nbest with the highest score (resolving ties alphabeti-
cally) is assigned a final score of 100, while all other nodes
are clamped to [1, 99]:
Sfinal (n) =
{
100 if n = nbest
min (99, max (1, Snorm (n))) otherwise
(7)
C. TOPOLOGICAL PROXIMITY QUANTIFICATION
For intents requiring topological affinity (e.g., pre-
fer_nearby_nodes_same_deployment), the system employs a
hierarchical proximity function. This function quantifies the
‘‘gravitational pull’’ of existing workloads on a candidate
node by aggregating pod counts across three topological
boundaries: Rack, Zone, and Region.

## §28062 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
TABLE 2. Intent classes with required metadata.
VOLUME 14, 2026 28063
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
Let T = {rack , zone, region} be the set of topological
domains. We define kn,t as the count of existing pods belong-
ing to the target deployment within the specific domain t of
node n. To prioritize tighter locality, the system assigns a
decaying weight vector ω to the domains:
ω = {ω rack : 2.0, ωzone : 0.5, ωregion : 0.2} (8)
The raw proximity score P (n) is calculated as the dot
product of the weight vector and the topology counts:
P (n) = ωrack · kn,rack + ωzone · kn,zone + ωregion · kn,region
(9)
To prevent unbounded growth of this score in large clusters,
P (n) is normalized against the maximum observed proximity
score across all candidate nodes in the current scheduling
cycle. The final evaluation logic φprox (n) is defined as:
φprox (n) = P(n)
max
m∈N
(P(m)) (10)
This hierarchical weighting ensures that nodes sharing a
rack with existing pods are mathematically favored over those
sharing a zone or region, aligning the scheduler’s decisions
with physical network topology constraints.
D. TEMPORAL STATE CONSISTENCY
To mitigate the latency inherent in asynchronous Kubernetes
API updates which can lead to race conditions during high-
velocity ‘‘burst’’ scheduling, the system implements a hybrid
state model.
Let Papi represent the set of confirmed pods retrieved
from the Kubernetes API (via the Cluster State Cache), and
let Plocal represent the set of tentative scheduling decisions
recorded in the extender’s local short-term memory. The local
set is defined by a Time-To-Live (TTL) constraint τ , set to
10 seconds:
Plocal = p ∈ Pdecisions | (tnow − tscheduled (p)) < τ (11)
The Effective Pod Set, Peff , used for all affinity and
anti-affinity calculations (such as the count kn in Eq. 5 and
Eq. 9), is the union of these two sets, ensuring that subse-
quent scheduling requests within a burst are aware of pending
placements before they are persisted in etcd:
Peff = Papi ∪ Plocal (12)
This consistency model ensures that for any dynamic scor-
ing function f (n, P), the evaluation is performed against the
most current state approximation: Score (n) = f
(
n, Peff
)
.
E. MUL TI-OBJECTIVE SCALARIZATION
The scheduling problem is modeled as a Multi-Objective
Optimization (MOO) task, where the goal is to identify a
node n that maximizes a vector of objective functions8 (n) =
[φ1 (n) , φ2 (n) , . . . , φk (n)].
TABLE 3. Formula symbols.
To resolve conflicts between objectives (e.g., spread vs.
affinity) in real-time, the system employs a linear scalariza-
tion strategy. We define a dynamic weight vector W where
each element wi is the product of the base weight, confidence,
and strength:
wi = β · Ci · Wi (13)
The scalarized global objective function F (n), which cor-
responds to the code’s implementation of the additive scoring
loop, is the dot product of the weight and objective vectors:
F (n) = W · 8 (n) =
|J |∑
i=1
wiφi (n) (14)
Finally, to ensure strict determinism guaranteeing that
the scheduler makes identical decisions for identical state
inputs regardless of asynchronous race conditions, the system
imposes a Lexicographical Total Ordering on the set of
optimal candidates. Let Nopt be the set of nodes achieving
the maximum score.
The selected node n∗ is defined mathematically as the
minimum element under lexicographical order (≺ lex) among
the highest-scoring nodes:
n∗ = min
<lex
{
n ∈ N | Sfinal(n) = max
m∈N
Sfinal (m)
}
(15)
This formalization proves that the system avoids random
tie-breaking, a critical property for reproducibility in cluster
orchestration.
VI. SYSTEM EVALUATION
To validate the efficacy and performance of the proposed
semantic, intent-driven scheduling paradigm, a series of
quantitative experiments were conducted using the prototype
testbed. The evaluation focuses on two critical aspects of
the system: firstly, on the accuracy with which the Intent
Analyzer translates natural language allocation hint anno-
tations into structured, actionable intents and their associ-
ated metadata; and secondly, on the quality and efficiency

## §28064 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
of the resulting pod placements compared to the default
Kubernetes scheduler configured with traditional affinity
and anti-affinity rules, i.e., using standard directives like
nodeSelector, podAffinity, and podAntiAffinity to achieve a
similar outcome. These experiments aim to provide empir-
ical evidence supporting the hypothesis that an LLM-based
approach can effectively bridge the gap between high-level
user requirements and low-level scheduling decisions, while
also identifying the performance characteristics and limita-
tions of the prototype implementation.
A. INTENT RECOGNITION ACCURACY
The first experiment tests the core of the semantic claim,
i.e., how accurately does the LLM translate natural language
into structured intents? The hypothesis is as follows: the
LLM-based Intent Analyzer can accurately and consis-
tently parse unstructured allocation hint text into the
correct, structured Intent objects and their associated
metadata.
To validate the semantic parsing performance of the Intent
Analyzer, a benchmark ground-truth evaluation dataset was
systematically constructed. The dataset v1, used to evaluate
the LLM, can be found on the Model Hub [37](file: schedule-
intent-evaluation-v1.json). This dataset is foundational to this
experiment, as it provides the means to quantify the accuracy,
precision, and recall of the system’s core function: translating
unstructured, natural-language of allocation hint text into
structured, machine-readable JSON objects.
The 314-prompt evaluation dataset was created using a
structured four-category methodology. This approach ensures
comprehensive test coverage across all 25 Intent types, while
also testing the model’s robustness against complex, nuanced,
and invalid inputs. Each of the prompts is paired with a
manually authored JSON object representing the expected
ground truth. The dataset is segmented into four distinct cate-
gories, each designed to test a specific aspect of the analyzer’s
performance:
• Categorical & Paraphrasing: Tests in this category
establish baseline accuracy for all 25 Intent types. For
each individual intent, multiple prompts were authored
using different paraphrasing and natural language varia-
tions. This component tests the model’s semantic equiv-
alence detection (e.g., recognizing that ‘‘needs a GPU’’,
‘‘I want an NVIDIA card’’, and ‘‘this is a CUDA job’’
all map to the prefer_gpu intent).
• Combinatorial (Complex): This category assesses the
LLM’s ability to parse complex prompts containing mul-
tiple, distinct intents. Prompts were authored to combine
two or more directives, often mixing resource require-
ments with topology constraints (e.g., ‘‘High-memory
pod (64GB), please spread across zones’’). This evalu-
ates the model’s parsing completeness and its ability to
handle non-trivial, realistic scheduling requests.
• Strength & Nuance: Those tests focus on the model’s
interpretation of qualitative language. Prompts were
authored to include specific qualifier words indicative
of scheduling priority (e.g., ‘‘must run’’, ‘‘critical’’,
‘‘strongly prefer’’ vs. ‘‘if possible’’, ‘‘maybe’’, ‘‘nice
to have’’). This allows for a quantitative evaluation of
the generated strength and confidence scores, which are
critical for effective, weighted scheduling decisions.
• Negative & Irrelevant (Noise): This category measures
the model’s specificity and its resilience to false posi-
tives. It consists of prompts containing no valid schedul-
ing intents, including empty strings, irrelevant technical
metadata (‘‘pod image: nginx’’), ambiguous statements
(‘‘this is a test pod’’), or random gibberish. This validates
the model’s ability to correctly identify and reject non-
actionable input.
The resulting 314-prompt evaluation dataset provides a
balanced mix of simple coverage, complex combinations,
and realistic noise, enabling a robust evaluation of the sys-
tem’s precision, recall, and overall effectiveness. The test
dataset and evaluation results were also utilized to incre-
mentally refine the prompt template for LLM models, intent
descriptions, and to select the best performing model. Notable
lessons learned are summarized below:
• Iterative refinement is an essential approach, and the ini-
tial
prompt - model combination required several iterations
to achieve satisfactory results. Systematic evaluation
against a ground-truth dataset - followed by failure anal-
ysis and targeted prompt adjustments - proved crucial
for improving performance. Multiple iterations were
necessary to reach the final results.
• The research initially experimented with the
amazon.nova-micro-v1:0 model (128K token context
window), but this model proved too small to capture
the nuances required for detailed metadata extraction
and strength interpretation. Subsequently, larger models
such as Amazon Nova Lite / Pro (300K token context
window), Amazon Nova Premium (1M token context
window) were employed - the Pro model providing an
effective balance between model size and cost. Large
models especially excel at metadata identification and
subsequent extraction into correct format.
• The most significant improvements came from mak-
ing the prompt instructions highly specific and rule-
based, i.e., by providing explicit guidance within the
prompt. Adding explicit rules for data types (e.g., float,
JSON list), precise naming conventions, handling of
defaults, and especially negative constraints (e.g., ‘‘DO
NOT summarize lists’’, ‘‘DO NOT use wildcards’’) dra-
matically improved metadata accuracy. However, overly
strict prompt instructions (e.g., requiring perfect meta-
data extraction or omitting intent) led to an increase
in missed metadata values when the model was uncer-
tain. Modifying the prompt to allow reasonable defaults
(e.g., 1.0 for counts, [] for lists) when extraction failed
VOLUME 14, 2026 28065
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
improved robustness without significantly compromis-
ing accuracy.
• Asking the model for nuanced strength interpretation,
i.e., float values within ranges (e.g., 0.5-2.0), performed
poorly. Simplifying the scale to three distinct values (0.5,
1.0, 1.5) and explicitly linking them to specific keywords
in the prompt instructions led to much higher accuracy.
• Defining intent descriptions to serve as in-prompt guid-
ance proved highly beneficial. Adding clear statements
such as ‘‘MUST be a JSON list of strings’’ or ‘‘MUST
be a float’’ directly within the descriptions reinforced
the expected output format for each intent’s metadata.
Including concrete examples within these descriptions
(e.g., [’us-east-1a’, ’us-east-1b’], 128.0 for 128 GB) fur-
ther clarified the target format and improved consistency
across outputs.
The evaluation systematically compared the performance
of eleven LLMs in parsing natural language scheduling
hints into structured intents and metadata. The selection of
the 11 LLMs for evaluation was aimed at a robust comparison
across provider diversity, model size, cost, and availability on
the AWS Bedrock platform. The models were chosen from
five different providers (Amazon, Anthropic, Meta, AI21,
Mistral) to assess varying architectures. The inclusion of
different model sizes within families (e.g., Nova Micro, Lite,
Pro, Premier; Claude 3 Haiku, Sonnet) allowed for analysis
of capability scaling, ultimately finding Nova Pro offered a
good balance.
Cost-effectiveness was also considered, with the cheaper
Nova models initially used for prompt refinement. Finally,
practical availability constraints influenced the selection,
excluding Claude 3 Opus (enterprise-only access) and
larger Llama 3 models (EU restrictions). This multi-faceted
approach ensured a comprehensive assessment of LLM per-
formance for the specific task of semantic intent parsing.
All models were evaluated against the 314-item ground-truth
evaluation dataset using the final, highly refined prompt and
intent descriptions to ensure a fair comparison of their capa-
bilities.
The findings presented in Table 4 indicate significant
performance disparities between models but establish a
clear top tier of high-capability models. Amazon Nova
Premier, Mistral Pixtral Large, Amazon Nova Pro, and
Anthropic Claude 3 Sonnet all demonstrated exceptional per-
formance, particularly in intent classification. Conversely,
smaller or less-optimized models like Amazon Nova Micro,
Claude 3 Haiku, Mistral 7B, and especially AI21 Jamba Mini
and the Llama 3 (3B) variant, showed significant deficiencies,
particularly in intent detection recall.
The original intention of using Amazon Nova models in the
early research was to refine the prompt template and intent
descriptions and to determine the required model size while
saving on cost, as Nova models are substantially cheaper
per token. However, during the research, it was found that
Amazon Nova models could stand on their own. As shown
in Table 4, the performance of models like Amazon Nova Pro
and Amazon Nova Premier was demonstrated to be compara-
ble to other top-tier models, such as Anthropic Claude 3 Son-
net and Mistral Pixtral Large.
Additionally, to establish a non-AI baseline, a Regular
Expressions (Regex) Engine was implemented with a set of
hardcoded sentence and keywords matching expressions, and
evaluated against the same dataset. As shown in Table 4,
the Regex Engine offers virtually instantaneous performance,
with average and P95 latencies under a millisecond. Never-
theless, its ability to accurately parse the semantic nuances
of the natural language hints proved significantly inferior
to the top-tier LLMs. The Regex Engine achieved a Subset
Accuracy of only 29.62%, indicating it correctly identified
the full set of intents in less than a third of cases, compared to
over 95% for models like Nova Premier and Mistral Pixtral
Large. Its Macro F1-score (0.38) and Recall (0.30) were dras-
tically lower than the best LLMs (0.98 and 0.98, respectively),
highlighted by an extremely high number of False Negatives
(240 missed intents). While Metadata V alue Accuracy was
somewhat better (78.67%), it still lagged behind the top
LLMs and struggled significantly with list extraction (e.g.,
avoid_zones 0% accuracy). This demonstrates that while
regular expressions-based logic is very fast, it is too brittle
and lacks the semantic understanding required to reliably
interpret the varied phrasing, complex combinations, strength
indicators, and paraphrasing inherent in natural language
scheduling requests, justifying the use of more sophisticated
LLMs despite their higher latency.
Regarding intent classification, the ability to identify the
correct set of user directives, the top-tier models were out-
standing. Amazon Nova Premier achieved the highest Subset
Accuracy at 97.45%, closely followed by Mistral Pixtral
Large (95.86%), Amazon Nova Pro (93.63%), and Anthropic
Claude 3 Sonnet (93.63%).
These models all achieved Macro F1-scores of 0.95 or
higher, demonstrating near-perfect precision and recall with
minimal errors (Aggregated False Positives 10-17, False Neg-
atives 9-18). In stark contrast, smaller models like Nova
Micro, Claude 3 Haiku, and Mistral 7B showed significant
deficiencies, with Subset Accuracies between 68-78% and
much higher False Negative counts (64-103). The Llama 3
(3B) and Jamba Mini models performed very poorly, failing
to classify intents correctly in the vast majority of cases.
In metadata value extraction, which assesses the accuracy
of parsing quantities and entities, performance was strong
among the top models. Claude 3 Sonnet achieved the high-
est accuracy at 95.22%, closely followed by Nova Micro
(94.57%), Nova Pro (94.40%), and Mistral Pixtral Large
(93.75%). This indicates that when models (even smaller
ones like Micro) correctly identify an intent, the refined
prompt is very effective at guiding data extraction. Notably,
all high-performing models achieved perfect or near-perfect
Metadata Completeness, successfully providing all required
fields for the intents they detected. Still persistent minor
weaknesses were observed across all models, particularly

## §28066 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
LISTING 1. Prompt template.
in accurately extracting complex lists without simplification
(e.g., substituting specific regions with generic terms like
‘Asia’ or ‘Europe’) and in correctly applying default numeri-
cal values (often defaulting to 1.0) for prefer_network_speed
and prefer_ephemeral_storage when only qualitative terms
were used.
The system’s multilingual robustness was validated using
Spanish (47 hints) and German (62 hints), yielding accuracies
of 93.62% and 90.32%, respectively, leveraging the native
capabilities of Amazon Nova Pro. The evaluation datasets are
available in [37] (files: schedule-intent-evaluation-v1es.json
and schedule-intent-evaluation-v1ge.json).
B. SCHEDULING EFFICIENCY AND QUALITY
With optimized prompt and selected model Amazon Nova
Pro (pro-v1:0), the second experiment focused on evaluating
the quality of placements, i.e., how the created solution com-
pares with the default Kubernetes scheduler? The hypothesis
was formulated as follows: the intent-driven Score Exten-
der Service-based scheduler produces pod placements
that are quantifiably superior in fulfilling user intent
compared to the default scheduler.
In the Minikube testbed, the control-plane node runs
within the kube-system namespace, and all core Kubernetes
components, including the kube-apiserver, kube-scheduler,
etcd, and kube-controller-manager, are deployed as individ-
ual pods (Figure 4). This design provides several practical
advantages for testing and debugging. Since each system
component is containerized and placed within unique names-
paces, it is straightforward to list and inspect errors, monitor
resource usage, and collect detailed scheduling logs.
Administrators can access component-specific logs via
standard Kubernetes tools such as kubectl logs, enabling
fine-grained visibility into the scheduler’s decision-making
process and making it easier to trace the impact of cus-
tom scheduler extenders, intent analysis, and topology-aware
placement policies. This setup provides a fully observable and
debuggable control-plane environment without affecting the
worker nodes running user workloads. In addition, it proved
particularly convenient for implementing low-level modifica-
tions required by this investigation, as well as for tracking the
outcome, i.e., the resulting allocations for further evaluation.
Notably, matching the labels, i.e., the metadata.labels and
selector .matchLabelsfields (as specified in Table 5 ) ensures
the Deployment controller can correctly identify, count, and
manage the Pods it is responsible for, as labels are the link
between the controller and the objects it controls.
Table 5 captures both the baseline Kubernetes manifests
and manifests with allocation hints. The experiment utilized
VOLUME 14, 2026 28067
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
six distinct scenarios comparing the prototype’s decisions
against baseline Kubernetes configurations. The results for
these scenarios are detailed in Table 5 and summarized below.
The relevant configuration sections in the deployment mani-
fests were additionally bolded.
• Scenario A - Topology Spreading: This test evalu-
ated a high-availability policy using the hint ‘‘spread
these pods evenly across all available zones for high
availability’’. Both the baseline scheduler (using topol-
ogySpreadConstraints) and the intent-driven scheduler
achieved a perfect 3:3 split of the six replicas across the
two simulated zones, successfully fulfilling the objec-
tive.
• Scenario B - Resource Affinity: This scenario tested
resource preferences with a ‘‘critical ML training job,
it must run on nodes with GPUs’’ hint. Both the base-
line (using nodeAffinity) and the intent-driven scheduler
successfully placed all 6 out of 6 pods (100%) on the
minikube-m02 node, which was labeled as having a
GPU. This demonstrated that the prototype correctly
interpreted the ‘‘must run’’ hint as a strong preference
and that its scoring logic functioned as intended.
• Scenario C - Complex Co-location and Anti-Affinity:
This scenario evaluated expressiveness with a mixed
intent: ‘‘prefer to be in the same region as the ‘database’
and ‘cache’ deployments, but avoid being on the same
node as the ‘logging-agent’ pods’’. The baseline sched-
uler, using complex podAffinity and podAntiAffinity
rules, successfully placed all 6 pods correctly. It avoided
the minikube-m02 node (running the logging-agent) and
distributed the pods across minikube-m03, m06, m07,
m08, and m09. The intent-driven scheduler also placed
all 6 pods correctly, successfully avoiding minikube-
m02. Furthermore, it fulfilled both objectives by placing
all pods on minikube-m03, satisfying the anti-affinity
rule while also adhering to the preference to be near the
‘cache’ deployment.
• Scenario D - Rapid Burst Colocation: This test vali-
dated the recent placements cache’s effectiveness during
a high-velocity creation of 20 replicas with the hint
‘‘Collocate all pods from this deployment on a single
node’’. Both the baseline (using a hard podAffinity rule)
and the intent-based scheduler successfully achieved the
ideal outcome, placing all 20 pods onto a single distinct
node.
• Scenario E - Quantitative Resource Preference: This
scenario tested the full pipeline: parsing quantitative
metadata from the hint ‘‘at least 100 Gbps network
speed’’ and executing the resulting placement prefer-
ence. The baseline scheduler, configured with an equiv-
alent soft nodeAffinity preference, placed only 1 of
6 pods (16.7%) on the correct high-speed node. This
failure occurred because the default Kubernetes sched-
uler’s other plugins, such as those for topology spread-
ing, outweighed the soft preference. In contrast, the
FIGURE 4. Example output of kubectl get pods command used to list all
pods across namespaces in the Minikube testbed. Similar listings were
captured during evaluation to validate the correctness and quality of the
resulting pod allocations.
intent-driven scheduler successfully parsed the numer-
ical requirement and placed all 6 of 6 pods (100%) on
the correct node labeled with 100 Gbps network speed.
This result validates the system’s ability to interpret
specific numerical metadata and demonstrates that its
high extender weight effectively prioritizes the user’s
intent over other default scoring logic.
• Scenario F - Conflicting Intent Resolution: This test
evaluated the system’s behavior when given logically
contradictory hints (‘‘collocate all pods on a single
node’’ and ‘‘you must also spread these pods across
all zones’’). As expected, the baseline scheduler, con-
figured with contradictory hard constraints (podAffinity
and topologySpreadConstraints), failed to schedule the
pod, which remained in a Pending state. The intent-
driven scheduler, however, processed the contradictory
soft preferences. Its additive scoring logic resolved the
conflict to find a best-fit solution, allowing the pod
to be scheduled. This outcome highlights the proto-
type’s ability to resolve conflicting soft preferences,
which is a known behavior of the additive scoring
model.
The strength of this experimental design lies in their strategic
coverage. The set of six scenarios effectively validates the
prototype from multiple critical perspectives:
• Core Effectiveness: Scenarios A, B, and E test the
scheduler’s primary function, i.e., correctly placing pods
based on common topology and resource requirements.
Scenario E, in particular, validates the full pipeline from
quantitative metadata parsing to placement.
• Expressiveness Claim: Scenario C directly supports the
paper’s main hypothesis by testing a complex, mixed-
intent request (affinity and anti-affinity) that is notori-
ously cumbersome to express using traditional Kuber-
netes rules.
• Technical Robustness: Scenario D is a crucial stress
test. It validates a specific architectural component (the
recent placements cache) that was explicitly designed to
handle a real-world performance challenge (burst scal-
ing), which is a non-obvious but critical detail.

## §28068 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
TABLE 4. Comparison of LLM outputs and evaluation.
• System Limitations: Scenario F demonstrates the sys-
tem’s boundaries. By explicitly testing a known lim-
itation (the additive scorer’s handling of conflicting
intents), the evaluation moves beyond a simple proof-
of-concept and provides a rigorous assessment of the
prototype’s current capabilities.
This combination of scenarios provides the necessary evi-
dence to validate the scheduler’s effectiveness and demon-
strates a view of the system’s limitations and future work.

## § Conclusion

A core premise of this work is the reduction of cognitive
overhead, which became immediately apparent during the
configuration of the baseline experiments (as presented
in Section IV.B). For instance, achieving the baseline
behaviors in experimental Scenarios A and C required
complex, multi-level Y AML structures. These baselines
relied on Kubernetes’ default directives, such as topolo-
gySpreadConstraints and a combination of podAffinity and
VOLUME 14, 2026 28069
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
TABLE 5. Evaluation scenarios A-F.

## §28070 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
TABLE 5. (Continued.) Evaluation scenarios A-F.
podAntiAffinity, respectively. Such configurations are ver-
bose, difficult to author correctly, and prone to error. In con-
trast, the prototype required only a single allocation-hint
annotation (e.g., ‘‘spread across zones’’), demonstrating a
significant and practical simplification in expressing user
intent.
The development and evaluation of the semantic schedul-
ing prototype revealed several key insights into integrating
LLMs within latency-sensitive infrastructure systems. First,
while LLMs demonstrated strong capability in translating
natural-language hints into structured scheduling directives,
their decoding reliability remains a central challenge. Even
small misinterpretations of intents or metadata can lead to
significant scheduling deviations.
The need for deterministic, verifiable parsing underscores
that LLMs should paired with strict schema validation, nor-
malization layers, and human-readable audit trails to ensure
operational safety in production environments.
In addition to these operational challenges, ethical
and security issues must also be addressed. Algorith-
mic bias in LLM interpretations could result in unfair
resource allocation. Because user hints are untrusted,
strong protections against prompt injection attacks are
required to safeguard cluster stability. Moreover, the risk
of intentional resource exhaustion through crafted seman-
tic requests underscores the need for robust admission
controls.
The investigation has demonstrated that effective prompt
design and schema constraints are as critical as model selec-
tion. Incremental improvements in prompt phrasing, output
examples, and metadata formatting directly reduced false
positives and extraction errors. This experience reinforced
that LLM integration is as much an engineering discipline as
a modeling challenge; robustness depends on careful pipeline
design, not model capability alone.
The production deployment of the Score Extender involves
operational challenges, specifically the complex configura-
tion of kube-scheduler manifest files required to integrate
custom extenders. Furthermore, because Kubernetes Control
Plane nodes are typically isolated within secure namespaces,
ensuring the implemented webhook endpoints are reach-
able from the control-plane node requires network policy
management to maintain cluster security without obstructing
scheduling communication.
The project also highlighted the importance of architectural
separation between intent analysis and scheduling execution.
The prototype exposed fundamental differences between
research feasibility and production readiness: (i) embedding
an LLM call within the synchronous /prioritize path intro-
duced unacceptable latency for real-world use, and (ii) the
single-threaded Flask server, static scoring logic, and lack of
fault tolerance are acceptable for evaluation but unsuitable for
real workloads. Transitioning to a scalable, asynchronous ser-
vice architecture and incorporating caching, concurrency, and
adaptive fallback mechanisms will be essential for deploy-
ment in real clusters. The below list details the most crucial
limitations in the current design:
• A Single-threaded Python Flask Server : While the
prototype performed well during controlled evaluations,
its Python Flask-based implementation is inherently
single-threaded, making it unsuitable for production-
scale workloads. Under concurrent scheduling requests,
this architecture would quickly become a bottleneck,
as each request must wait for the current one to complete
before being processed. This serialization severely limits
VOLUME 14, 2026 28071
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
throughput and scalability, particularly in high-load
cluster environments where multiple scheduling opera-
tions occur in parallel. A production-ready deployment
would require migrating to a multi-threaded or asyn-
chronous framework like FastAPI or aiohttp, and also
to set up a load balancer to provide resilience.
• Intent Classification Errors: The scheduler’s behav-
ior depends critically on the correct identification of
a presence of an intent. While top-tier models such
as Amazon Nova Premier and Mistral Pixtral Large
achieved high subset accuracy (97.45% and 95.86%,
respectively), their performance is not flawless. The 9-
18 aggregated false negatives represent cases where a
user’s hint (e.g., spread_zones) was completely missed,
leading to violations of the intended scheduling policy.
Conversely, the 10-17 aggregated false positives corre-
spond to hallucinated intents, where the model inferred pref-
erences not expressed by the user. Such misclassifications can
result in unpredictable or suboptimal scheduling outcomes,
as the system might apply unintended placement preferences
or ignore critical user directives.
• Metadata Extraction Errors: Even when an intent
is correctly identified, its associated metadata can be
misinterpreted or extracted incorrectly. As shown in
Table 4, the best-performing models on this metric,
i.e., Claude 3 Sonnet (95.22%) and Amazon Nova
Pro (94.40%), still exhibit nontrivial error rates. This
limitation, observed repeatedly during prompt refine-
ment, becomes particularly pronounced with complex
list extractions. For instance, a hint such as ‘‘avoid us-
east-1a and us-east-1b’’ might be erroneously parsed as
[’us-east-1’], preventing the scheduler from excluding
the specified zones. Similarly, an implicit hint like
‘‘high memory’’ may be incorrectly assigned a default
numeric value (e.g., 1.0), rendering the resulting pre-
fer_memory_gb intent ineffective. Such metadata errors
can silently degrade scheduling accuracy, as the scoring
logic depends on precise, structured values.
• Unreliable Strength Interpretation: The most signif-
icant decoding weakness, as highlighted in Table 4,
is unreliable strength interpretation. The Overall
Strength Accuracy metric measuring how well models
map linguistic modifiers like ‘‘must’’ (strength= 1.5) or
‘‘prefer’’ (strength = 0.5) proved the most challenging.
Even the best-performing models, Nova Premier and
Mistral Pixtral Large, achieved only 71.79% accuracy,
while the chosen Nova Pro model reached 67.85%.
Consequently, in roughly one-third of cases, the model
misinterprets the user’s intended priority. A ‘‘critical’’
directive (strength 1.5) misclassified as a standard pref-
erence (strength 1.0) would cause the scheduler to treat
it as a weak suggestion, allowing less important factors
to dominate the decision. This systematic degradation
of the intent strength undermines user expectations and
highlights the need for explicit strength calibration or
post-processing normalization in future iterations.
Overall, these lessons demonstrate that while LLM-driven
intent recognition holds strong promise for advancing declar-
ative scheduling, reliability, observability, and performance
isolation must remain first-class design goals. Future iter-
ations should focus on modularizing these components,
enabling general-purpose, platform-agnostic scheduling aug-
mentation built on stable, interpretable NLP foundations. The
future works should cover the following:
• Intent Analysis Prior to Scoring: Although the
prototype demonstrates the feasibility of translating
natural-language hints into scheduling directives, its
architecture introduces a significant performance bottle-
neck. The current design performs a synchronous LLM
call within the /prioritize handler, adding P95 latencies
ranging from 0.87s to 5.34s, depending on the model.
In production, this delay would be unacceptable during
scheduling. A production-ready solution should move
the LLM call outside the scheduling loop, likely most
effectively to be implemented via a MutatingAdmission-
Webhook that analyzes intents at pod creation, stores the
structured JSON output in an annotation, and allows the
scheduler extender to read it locally during /prioritize.
This would remove the synchronous dependency, elim-
inating latency and making semantic scheduling viable
for high-throughput clusters.
• Expanding Evaluation Dataset with Compound
Multi-Objective Prompts: The current 314-prompt
evaluation dataset primarily covers cases translating into
one or two intent objects. Future work should extend this
dataset to include multi-level and conflicting scheduling
intents, reflecting real-world scenarios where objec-
tives such as co-location and fault tolerance interact.
Incorporating such complex and contradictory prompts
will better test the LLM’s reasoning and consistency,
highlighting the need for larger, context-aware models
capable of resolving competing directives and handling
richer semantic structures. This work has already com-
menced with the creation of the v2 dataset, available on
the Model Hub [37] (file: schedule-intent-evaluation-
v2.json), which introduces two new categories: Multi-
Objective Optimization (focused on encoding multiple
Intents) and Contradictory Prompt (providing opposing
hints).
• Pareto Frontier Optimization: A key direction for
future work is the integration of Pareto-based scoring
into the scheduling framework. This approach would
allow multiple, potentially conflicting objectives to be
evaluated simultaneously, while preserving the domi-
nance of higher-priority intents. Implementing a tiered
logic scheme, where lower-strength objectives act as
tie-breakers only when no higher-strength objective
dominates, could improve decision-making in complex

## §28072 VOLUME 14, 2026

L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
scheduling scenarios. Future iterations will explore the
design and evaluation of this method.
• Evaluation in a Parallel Execution Environment:
A notable limitation of the current prototype is its
execution environment. While the Minikube testbed
simulates a multi-node cluster, the core scoring logic
within the Extender Service operates sequentially due
to Flask’s single-threaded nature. This means that even
if multiple pod scheduling requests arrive concurrently
at the extender, they are processed one after another.
This sequential processing does not accurately reflect
a production scenario where a busy scheduler exten-
der handles numerous /prioritize requests in parallel.
Future work should involve reimplementing the extender
logic using a multi-threaded server capable of parallel
request handling. Evaluating the system under such
concurrent load is crucial, as it will likely necessitate
the introduction of sophisticated locking mechanisms.
Specifically, concurrent scoring of pods belonging to the
same deployment (e.g., during a scale-up) could lead to
race conditions when updating or querying the recent
placements cache or when calculating dynamic scores
for spread_ and colocate_ intents. Therefore, imple-
menting appropriate concurrency controls will be essen-
tial for ensuring the correctness and scalability of the
intent-based scoring logic in a realistic, high-throughput
environment.
• General-Purpose Scheduling Grammar: A key direc-
tion for future research is to decouple the core
scheduling logic from its current tight integration with
Kubernetes. In the prototype, Intent definitions and
scoring logic depend on Kubernetes-specific topology
labels (e.g., zone, rack) and its scheduler extender API.
To generalize this concept, a universal scheduling gram-
mar should be introduced - an abstract intermediary
format for defining soft-affinity scheduling preferences.
The LLM would translate natural-language hints into
this grammar, while platform-specific adapters would
convert it into concrete directives for systems such as
Kubernetes, Mesos, or SLURM. This approach would
decouple NLP-based intent recognition from any sin-
gle platform, enabling a general-purpose framework
for semantic workload orchestration across diverse
environments.
In summary, this work successfully validates the core premise
that LLMs can bridge the semantic gap in cluster schedul-
ing, demonstrating high accuracy in translating human intent
into structured scheduling policies. The prototype proves
the concept of semantic soft affinity, shifting the bottleneck
from human configuration error to the engineering challenges
of integration, specifically regarding synchronous latency
and reliable metadata decoding. This research thus confirms
the viability of intent-driven orchestration while clearly out-
lining the architectural and reliability engineering required
to transition such a system from a novel prototype to a
production-grade infrastructure component.

## § Acknowledgment

The authors wish to express their sincere gratitude to Standard
Chartered Bank for its material support, which contributed
significantly to the research and investigation.

## § References

[1] W. Wang, B. Li, and B. Liang, ‘‘Dominant resource fairness in cloud
computing systems with heterogeneous servers,’’ in Proc. IEEE Conf.
Comput. Commun., Apr. 2014, pp. 583–591.
[2] I. Gog, M. Schwarzkopf, A. Gleave, R. N. M. Watson, and S. Hand,
‘‘Firmament: Fast, centralized cluster scheduling at scale,’’ in Proc.
12th USENIX Symp. Operating Syst. Design Implement. (OSDI), 2016,
pp. 99–115.
[3] B. Hindman, A. Konwinski, M. Zaharia, A. Ghodsi, A. D. Joseph, R. Katz,
S. Shenker, and I. Stoica, ‘‘Mesos: A platform for fine-grained resource
sharing in the data center,’’ in Proc. 8th USENIX Symp. Networked Syst.
Design Implement., 2011, pp. 1–14.
[4] M. Isard, V . Prabhakaran, J. Currey, U. Wieder, K. Talwar, and A. Goldberg,
‘‘Quincy: Fair scheduling for distributed computing clusters,’’ in Proc.
ACM SIGOPS 22nd Symp. Operating Syst. Princ., Oct. 2009, pp. 261–276.
[5] H. Mao, M. Alizadeh, I. Menache, and S. Kandula, ‘‘Resource manage-
ment with deep reinforcement learning,’’ in Proc. 15th ACM workshop hot
topics Netw., Sep. 2016, pp. 50–56.
[6] H. Mao, M. Schwarzkopf, S. B. V enkatakrishnan, Z. Meng, and
M. Alizadeh, ‘‘Learning scheduling algorithms for data processing clus-
ters,’’ in Proc. ACM Special Interest Group Data Commun., Aug. 2019,
pp. 270–288.
[7] E. Zeydan and Y . Turk, ‘‘Recent advances in intent-based networking: A
survey,’’ inProc. IEEE 91st V eh. Technol. Conf. (VTC-Spring), May 2020,
pp. 1–5.
[8] V . K. V avilapalli, A. C. Murthy, C. Douglas, S. Agarwal, M. Konar, R.
Evans, T. Graves, J. Lowe, H. Shah, S. Seth, B. Saha, C. Curino, O.
O’Malley, S. Radia, B. Reed, and E. Baldeschwieler, ‘‘Apache Hadoop
Y ARN: Y et another resource negotiator,’’ inProc. 4th Annu. Symp. Cloud
Comput., 2013, pp. 1–16.
[9] A. V erma, L. Pedrosa, M. Korupolu, D. Oppenheimer, E. Tune, and
J. Wilkes, ‘‘Large-scale cluster management at Google with Borg,’’ in
Proc. 10th Eur . Conf. Comput. Syst., Apr. 2015, pp. 1–17.
[10] X. Wang et al., ‘‘OpenHands: An open platform for AI software developers
as generalist agents,’’ 2024, arXiv:2407.16741.
[11] P . Jaillet, J. Jiang, K. Mellou, M. Molinaro, C. Podimata, and Z. Zhou,
‘‘Online scheduling for LLM inference with KV cache constraints,’’ 2025,
arXiv:2502.07115.
[12] I. Androutsopoulos, G. D. Ritchie, and P . Thanisch, ‘‘Natural language
interfaces to databases—An introduction,’’ Natural Lang. Eng., vol. 1,
no. 1, pp. 29–81, Mar. 1995.
[13] J. Silvander, K. Wnuk, and M. Svahnberg, ‘‘Systematic literature review on
intent-driven systems,’’IET Softw., vol. 14, no. 4, pp. 345–357, Aug. 2020.
[14] A. Clemm, L. Ciavaglia, L. Z. Granville, and J. Tantsura,
‘‘Internet research task force (IRTF), RFC 9315: Intent-based
networking-concepts and definitions,’’ Oct. 2022. [Online]. Available:
https://datatracker.ietf.org/doc/html/rfc9315
[15] P . Xuan, X. Sihan, C. Xiangrui, W. Y anlong, and Y . Xiaojie, ‘‘Survey on
deep learning based natural language interface to database,’’ J. Comput.
Res. Develop., vol. 58, no. 9, pp. 1925–1950, Sep. 2021.
[16] M. Tageldien, B. Selim, and L. Sboui, ‘‘Large language models in intent-
based networking: A comprehensive survey across the intent lifecycle,’’ in
Proc. Int. Telecommun. Conf. (ITC-Egypt), Jul. 2025, pp. 810–817.
[17] B. Wang, Z. Wang, X. Wang, Y . Cao, R. A. Saurous, and Y . Kim,
‘‘Grammar prompting for domain-specific language generation with large
language models,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2023,
pp. 65030–65055.
[18] D. Brodimas, K. Trantzas, B. Agko, G. C. Tziavas, C. Tranoris, S. Denazis,
and A. Birbas, ‘‘Towards intent-based network management for the 6G
system adopting multimodal generative AI,’’ inProc. Joint Eur . Conf. Netw.
Commun. 6G Summit (EuCNC/6G Summit), Jun. 2024, pp. 848–853.
VOLUME 14, 2026 28073
L. Sliwko, J. Mizera-Pietraszko: Semantic Soft Affinity Using Natural Language Processing
[19] A. Chowdhary, A. Sabur, N. V adnere, and D. Huang, ‘‘Intent-driven secu-
rity policy management for software-defined systems,’’ IEEE Trans. Netw.
Service Manage., vol. 19, no. 4, pp. 5208–5223, Dec. 2022.
[20] B. Martini, M. Gharbaoui, and P . Castoldi, ‘‘Intent-based network slicing
for SDN vertical services with assurance: Context, design and prelimi-
nary experiments,’’ Future Gener . Comput. Syst., vol. 142, pp. 101–116,
May 2023.
[21] L. Pang, C. Y ang, D. Chen, Y . Song, and M. Guizani, ‘‘A survey on intent-
driven networks,’’ IEEE Access, vol. 8, pp. 22862–22873, 2020.
[22] A. Singh, ‘‘Intent-based networking in multi-cloud environments,’’
J. Eng. Appl. Sci. Technol., vol. 288, pp. 1–7, Feb. 2025, doi:
10.47363/jeast/2025(7)288.
[23] B. K. Saha, L. Haab, and L. Podleski, ‘‘Intent-based industrial network
management using natural language instructions,’’ inProc. IEEE Int. Conf.
Electron., Comput. Commun. Technol. (CONECCT), Jul. 2022, pp. 1–6.
[24] J. Mcnamara, D. Camps-Mur, M. Goodarzi, H. Frank, L. Chinchilla-
Romero, F. Cañellas, A. Fernández-Fernández, and S. Y an, ‘‘NLP powered
intent based network management for private 5G networks,’’IEEE Access,
vol. 11, pp. 36642–36657, 2023.
[25] N. Deng, Y . Chen, and Y . Zhang, ‘‘Recent advances in text-to-SQL: A
survey of what we have and what we expect,’’ 2022, arXiv:2208.10099.
[26] M. Glass, M. Eyceoz, D. Subramanian, G. Rossiello, L. Vu, and A. Gliozzo,
‘‘Extractive schema linking for text-to-SQL,’’ 2025, arXiv:2501.17174.
[27] W. Hwang, J. Yim, S. Park, and M. Seo, ‘‘A comprehensive explo-
ration on WikiSQL with table-aware word contextualization,’’ 2019,
arXiv:1902.01069.
[28] B. Li, J. Zhang, J. Fan, Y . Xu, C. Chen, N. Tang, and Y . Luo, ‘‘Alpha-
SQL: Zero-shot text-to-SQL using Monte Carlo tree search,’’ 2025,
arXiv:2502.17248.
[29] X. Xu, C. Liu, and D. Song, ‘‘SQLNet: Generating structured
queries from natural language without reinforcement learning,’’ 2017,
arXiv:1711.04436.
[30] V . Zhong, C. Xiong, and R. Socher, ‘‘Seq2SQL: Generating struc-
tured queries from natural language using reinforcement learning,’’ 2017,
arXiv:1709.00103.
[31] A. Beloglazov and R. Buyya, ‘‘Energy efficient resource management in
virtualized cloud data centers,’’ inProc. 10th IEEE/ACM Int. Conf. Cluster ,
Cloud Grid Comput., May 2010, pp. 826–831.
[32] J. Chen, T. Du, and G. Xiao, ‘‘A multi-objective optimization for resource
allocation of emergent demands in cloud computing,’’ J. Cloud Comput.,
vol. 10, no. 1, p. 20, Dec. 2021.
[33] W. Khallouli and J. Huang, ‘‘Cluster resource scheduling in cloud comput-
ing: Literature review and research challenges,’’ J. Supercomput., vol. 78,
no. 5, pp. 6898–6943, Apr. 2022.
[34] R. Sissodia, M. M. S. Rauthan, and K. Naithani, ‘‘A survey on
multi-objective tasks and workflow scheduling algorithms in cloud com-
puting,’’ in Proc. Int. J. Cloud Appl. Comput., Aug. 2022, no. 1, pp. 1–6.
[35] (Sep. 4, 2025). Kube-Scheduler Configuration V1. [Online]. Available:
https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/
[36] H. Poon and P . Domingos, ‘‘Unsupervised semantic parsing,’’ in Proc.
Conf. Empirical Methods Natural Lang., vol. 1, 2009, pp. 1–10.
[37] L. Sliwko. (Feb. 3, 2026). Poc-Schedule-Intent-Evaluation. [Online].
Available: https://huggingface.co/datasets/lsliwko/poc-schedule-intent-

## § Evaluation

[38] M. Alam, K. A. Shakil, and S. Sethi, ‘‘Analysis and clustering of workload
in Google cluster trace based on resource usage,’’ in Proc. IEEE Int. Conf.
Comput. Sci. Eng. (CSE) IEEE Int. Conf. Embedded Ubiquitous Comput.
(EUC) 15th Int. Symp. Distrib. Comput. Appl. Bus. Eng. (DCABES),
Aug. 2016, pp. 740–747.
[39] Z. Y e, W. Gao, Q. Hu, P . Sun, X. Wang, Y . Luo, T. Zhang, and Y . Wen,
‘‘Deep learning workload scheduling in GPU datacenters: A survey,’’ACM
Comput. Surv., vol. 56, no. 6, pp. 1–38, Jun. 2024.
[40] L. Sliwko, ‘‘Cluster workload allocation: A predictive approach
leveraging machine learning efficiency,’’ IEEE Access, vol. 12,
pp. 194091–194107, 2024.
[41] A. V eremyev, A. Semenov, E. L. Pasiliao, and V . Boginski, ‘‘Graph-based
exploration and clustering analysis of semantic spaces,’’ Appl. Netw. Sci.,
vol. 4, no. 1, p. 104, Dec. 2019.
[42] A. K. Mishra, J. L. Hellerstein, W. Cirne, and C. R. Das, ‘‘Towards char-
acterizing cloud backend workloads: Insights from Google compute clus-
ters,’’ ACM SIGMETRICS Perform. Eval. Rev., vol. 37, no. 4, pp. 34–41,
Mar. 2010.
[43] G. Zhou, W. Tian, R. Buyya, R. Xue, and L. Song, ‘‘Deep reinforcement
learning-based methods for resource scheduling in cloud computing: A
review and future directions,’’ Artif. Intell. Rev., vol. 57, no. 5, p. 124,
Apr. 2024.
[44] Y . Sanjalawe, S. Al-E’Mari, S. Fraihat, and S. Makhadmeh, ‘‘AI-driven
job scheduling in cloud computing: A comprehensive review,’’Artif. Intell.
Rev., vol. 58, no. 7, p. 197, Apr. 2025.
[45] (2025). Llama 4 Acceptable Use Policy. [Online]. Available:
https://github.com/meta-llama/llama-models/blob/main/models/llama
LESZEK SLIWKO (Member, IEEE) received the
Ph.D. degree in parallel and distributed comput-
ing from the University of Westminster, Lon-
don, U.K., in 2019, for his work on developing
a novel AI-driven load balancer for cloud sys-
tems. He has presented at international events,
including IEEE conferences, Machine Intelli-
gence Research Laboratory lectures, and popu-
lar seminars, such as Scala in the City, JVM
Roundabout, and Scala Central. He has been
an IEEE Professional Member, since 2019. His talks are available at
https://www.youtube.com/@lsliwko. He is keen on experimenting with the
latest technologies, particularly those related to high-performance computing
and machine learning. A brief description of his selected projects can be
found at https://meta-analyzer.com/projects/.
JOLANTA MIZERIA-PIETRASZKO (Member,
IEEE) received the M.Sc. degree in computer
science from the University of Economics and
the Ph.D. degree in computer science from Wroc
University of Science and Technology, Poland,
in 2014. She is currently with Opole Univer-
sity of Technology, Poland. She authored and
co-authored more than 100 papers in conference
proceedings and journals, including an innovative
MT model published by Patent Office of Republic
of Poland. Her research interests include multilingual natural language pro-
cessing, medical informatics (she has been the Head of the Medical Infor-
matics Research Group), computational linguistics, data and text mining,
web systems, information retrieval, automated translation, and cybersecurity
in military systems. She serves on the ACM Europe Technology Policy
Committee in Differential AI and Data Science. She is an ACM Professional
Member, the British Computer Society Member, the Information Retrieval
Specialist Group Member, and the IEEE ComSoc Member. She has chaired
and served on TPC of around 80 international conferences. She serves as an
Associate Editor for IEEE ACCESS; a Featured Reviewer for ACM Computing
Reviews; an Editorial Advisory Board Member for Recent Advances in
Computer Science and Communications; and a Guest Editor for some ISI
journals, such as Big Data Research, Computing journal, and Journal of
Universal Computer Science. She is an Expert for European Commission
in evaluation of research projects on AI under HORIZON and some national
Polish research agencies.

## §28074 VOLUME 14, 2026

<empty>
