---
paper_id: "paper-1404"
source_pdf_sha: "ae36ef80bf0d423fd8f266c0c37c9fd09702aea9d447767badb43768229ceed6"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 2
  page_count: 11
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-1404 — fulltext
## §unknown-1

IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026 18305
ARM: Autonomous Remediation and Management
With LLM Agents for Intent-Driven Control
Vasilis Avgerinos
 , Kostas Ramantas
 , Luis Alonso
 , and Christos Verikoukis
Abstract—The growing complexity of cloud-native, edge, and
internet of things (IoT) infrastructures has made manual conﬁgu-
ration, fault remediation, and lifecycle management increasingly
unsustainable. Traditional automation techniques—such as rule-
based logic or bespoke machine learning pipelines—struggle
with adaptability and explainability in dynamic environments.
Recent advances in large language models (LLMs), however,
have introduced new opportunities for autonomous, intent-driven
infrastructure control. In this work, we present a closed-loop
framework that integrates LLM agents for automated root cause
analysis (RCA) and mitigation of faults within cloud–edge and
IoT systems. When service-level agreement (SLA) violations are
detected, the agent identiﬁes likely root causes and selects correc-
tive actions—such as pod rescheduling, scaling, or conﬁguration
updates—executed via a model context protocol (MCP) server
exposing management tool functionalities through an application
programming interface (API). This RCA-plus-mitigation loop
enables fault handling that is both explainable and adaptive. We
evaluate our system on a cluster running synthetic IoT workloads
under emulated stressors using a reproducible benchmarking
setup. Results show that the agent identiﬁes SLA violations
with 52.9% accuracy and mitigates 70.7% of them successfully.
Notably, the agent incorporates validation steps to ensure system
stability after interventions. These ﬁndings highlight the feasi-
bility of LLMs for real-time infrastructure healing and their
potential role in future artiﬁcial intelligence for IT operations
(AIOps) workﬂows.
Index Terms —Agentic systems, artiﬁcial intelligence for IT
operations (AIOps), autonomous infrastructure management,
closed-loop control, edge computing, intent-based networking
(IBN), internet of things (IoT) orchestration, Kubernetes, large
language models (LLMs), service-level agreement (SLA) moni-
toring,
I. I NTRODUCTION
T
HE growing complexity of deployed
infrastructures—spanning telecom, cloud–edge, and
internet of things (IoT) domains—has rendered manual
conﬁguration, fault mitigation, and lifecycle management
increasingly unsustainable. Intent-based networking (IBN)
emerged as a promising paradigm to address these issues by
Received 17 July 2025; revised 25 November 2025; accepted 11 December
2025. Date of publication 26 December 2025; date of current version 27 April
2026. This work was supported in part by European Commission Research
Projects AC3 under Grant 101093129 and in part by 6G-INTENSE under
Grant 101139266. (Corresponding author: Vasilis Avgerinos.)
Vasilis Avgerinos is with the Industrial Systems Institute, 26504 Patras,
Greece, and also with Iquadrat Informatica, 08006 Barcelona, Spain (e-mail:
avgerinos@isi.gr).
Kostas Ramantas is with Iquadrat Informatica, 08006 Barcelona, Spain
(e-mail: kramantas@iquadrat.com).
Luis Alonso is with the Universitat Polit ´ecnica de Catalunya, 08034
Barcelona, Spain (e-mail: luis.alonso@upc.edu).
Christos Verikoukis is with the Industrial Systems Institute, 26504 Patras,
Greece, and also with the University of Patras, 26504 Patras, Greece (e-mail:
chverik@gmail.com).
Digital Object Identiﬁer 10.1109/JIOT.2025.3648858
enabling high-level, goal-driven management abstractions.
However, for much of its existence, IBN remained more of
a conceptual ideal than a deployable reality, held back by
persistent challenges in translating natural language intent
into actionable conﬁgurations and behaviors [1], [2]. While
early e ﬀorts explored declarative approaches and query-
driven summaries of network state, they often lacked the
generalizability, context awareness, and autonomy required
in large-scale, dynamic systems [3], [4]. As such, despite
its potential, IBN’s practical adoption stalled until recent
years, where progress in AI-native orchestration, multiagent
systems, and network softwarization began to make its core
vision operationally viable [5].
Autonomous agentic systems—powered by recent advance-
ments in large language models (LLMs) and small language
models (SLMs), along with a rapidly expanding ecosystem of
tools and techniques [6], [7]—have moved to the forefront
of research and industry. A growing body of experiments
demonstrates the increasing capabilities of LLM-driven agents
across diverse domains: from solving novel mathematical
problems and recommending bug ﬁxes in production-grade
codebases, to assisting in clinical diagnostics through appli-
cation programming interface (API)-level interactions [8], [9],
[10]. These developments suggest that we are approaching a
level of agentic autonomy capable of transforming the long-
standing vision of true zero-touch infrastructure management
into a practical reality.
IoT infrastructures have long been a compelling testing
ground for such systems. Their inherently heterogeneous,
latency-sensitive, and dynamic nature makes them particu-
larly well-positioned to beneﬁt from these advances. As the
number of connected devices continues to grow, so too does
the demand for intelligent mechanisms capable of aligning
low-level infrastructure behavior with high-level operational
intents [11], [12], [13]. This alignment becomes especially
critical when faults or performance anomalies risk violat-
ing service-level agreements (SLAs). In such cases, agentic
systems can not only detect intent violations but also recom-
mend or autonomously execute corrective actions—such as
reconﬁguring resources or rescheduling workloads—to restore
compliance.
Traditional approaches to fault diagnosis in these environ-
ments have focused heavily on root cause analysis (RCA),
typically using machine learning models trained on historical
fault data. While e ﬀective in some scenarios, these mod-
els struggle to adapt to novel conditions and often lack
explainability—two factors that undermine operator trust.
Recent advances in Agentic AI suggest that LLM-based
agents—such as ReAct [14]—can help address these short-
2327-4662 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of artiﬁcial intelligence and
similar technologies. Personal use is permitted, but republication /redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
18306 IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026
comings by coordinating external tools via natural language
and producing transparent, traceable reasoning chains [15].
This is particularly relevant in IoT contexts, where the scale
and volatility of services demand both rapid remediation and
human-understandable diagnostics.
Based on the challenges and emerging opportunities out-
lined above, this article introduces ARM—autonomous
remediation and managment agent, leveraging the reasoning
capabilities of LLM-based autonomous systems. Our approach
seeks to bridge the gap between high-level operational intents
and low-level reconﬁguration actions by continuously mon-
itoring for SLA violations and dynamically responding to
deviations in system behavior. Users deﬁne custom intents
with deployment- or application-level scope, which spawn
dedicated monitoring loops that detect potential violations
using Prometheus-based metrics pipelines. When an anomaly
is detected—such as a performance degradation or fault
condition—an LLM agent is triggered to investigate the under-
lying cause and execute an appropriate mitigation strategy.
These strategies are implemented through an interface to
a model context protocol (MCP) server [16], o ﬀering con-
trolled access to tools like kubectl, observability modules,
or autoscaling primitives. The agent operates in a closed-
loop fashion, capable of interleaving planning, execution, and
optional replanning phases until compliance is restored.
To validate our methodology, we simulate a range of
representative fault scenarios under constrained resource con-
ditions and assess the agent’s ability to recover, stabilize, and
explain its interventions. The proposed architecture lays the
groundwork for future research in integrating LLM agents
into real-world artiﬁcial intelligence for IT operations (AIOps)
pipelines, especially within latency-sensitive, decentralized
IoT infrastructures. To the best of our knowledge, this is the
ﬁrst LLM-driven agentic system that not only identiﬁes root
causes of SLA violations but also autonomously mitigates
them through infrastructure-level actions in cloud–edge and
IoT environments.
Our key contributions are summarized as follows.
1) A novel closed-loop framework that integrates high-
level intent speciﬁcation with autonomous workload
reconﬁguration driven by LLM agents.
2) An LLM-powered control agent capable of investigating
anomalies and executing infrastructure-level reconﬁgu-
ration using tool calling and dynamic planning.
3) A reproducible evaluation cloud–edge environment
based on a K3s Kubernetes cluster running synthetic IoT
applications under emulated stressors.
4) A systematic evaluation of mitigation performance
across multiple fault scenarios, demonstrating the fea-
sibility and robustness of the proposed approach.
II. R ELATED WORK
Achieving fully autonomous IoT-edge infrastructures
depends on combining advancements from several key
research domains. Our work is positioned at the intersection
of IBN, natural language interfaces (NLIs), and runtime adap-
tation. This review outlines the current state of the art in
these ﬁelds to describe the scientiﬁc landscape and identify the
speciﬁc research gaps our work aims to address. We observe
that while each area has seen considerable progress, its holistic
integration into a cohesive, closed-loop architecture remains an
open challenge.
A. IBN for Autonomous Control
IBN has emerged as a foundational approach for automating
network and service management, particularly within struc-
tured telco and cloud domains. Contributions from [17] and
[18], for instance, showcase mature frameworks that translate
abstract service requirements into concrete resource conﬁgu-
rations for 5G network slicing and multicloud orchestration. A
primary limitation of these systems, however, is that they are
predominantly declarative and engineered for homogeneous
environments, with an emphasis on initial deployment rather
than continuous runtime adaptation.
Eﬀorts to extend IBN to the heterogeneous edge and IoT
continuum have been made, addressing domain-speciﬁc chal-
lenges such as RAN scheduling [19], vehicular mobility [20],
and serverless computing [21]. Nonetheless, these approaches
frequently lack a holistic, closed-loop architecture that inte-
grates predictive foresight and natural language understanding.
Consequently, they often remain reactive or episodic, falling
short of the continuous, proactive self-management required
by dynamic edge environments.
B. NLIs for System Conﬁguration
A key challenge in making complex infrastructures more
accessible is simplifying the human-to-system interface. To
this end, research into NLIs has yielded promising results in
automating conﬁguration tasks. Systems such as LACE [22]
translate free-form text into structured access control policies,
while other works have demonstrated the use of NLIs to
facilitate 5G service provisioning [23], generate infrastructure-
as-code for chaos engineering experiments [24], or perform
automated repair of security misconﬁgurations [25].
A notable limitation of these systems, however, is the
static nature of their outputs. They typically execute a
one-time translation from a natural language directive to
an executable artifact without incorporating mechanisms for
runtime feedback or autonomous correction. This “ﬁre-and-
forget” characteristic underscores a critical disconnect between
the initial ease of conﬁguration and the need for dynamic,
self-managing operational control in response to changing
conditions.
C. LLM Agents for Root Cause Analysis
Conceptual frameworks like ETSI ZSM have established the
principle of the closed management loop for intent assurance,
providing a foundational model for end-to-end automation
[26]. The goal of such frameworks is to create self-healing
systems where the entire incident lifecycle, from detection to
mitigation, is handled autonomously. The general architecture
and challenges of building such autonomous agents are well-
documented in recent surveys, which outline core components
like planning, memory, and action modules [27].
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
A VGERINOS et al.: ARM: AUTONOMOUS REMEDIATION AND MANAGEMENT WITH LLM AGENTS FOR INTENT-DRIVEN CONTROL 18307
To incorporate high-level reasoning into runtime control,
recent advances have explored the use of LLM-driven agents.
These agents combine the language understanding and reason-
ing capabilities of LLMs with a structured interface to interact
with external tools, environments, or APIs. By interpreting
natural language prompts and generating action plans or
decisions, they can autonomously perform tasks traditionally
requiring human intervention. Highly specialized systems like
Flow-of-Action, for example, have demonstrated robust perfor-
mance in complex diagnostic tasks by using standard operating
procedures (SOPs) to guide the agentic workﬂow [28]. This
approach enhances the reliability of RCA by imposing expert-
deﬁned constraints on the LLM, thus reducing hallucinations
and steering the diagnostic process toward a correct trajectory.
However, a signiﬁcant limitation of the current state of
the art is the overwhelming focus on problem identiﬁcation
rather than autonomous mitigation. The majority of recent
work on AI agents for IT operations centers almost exclusively
on anomaly detection and RCA. Numerous recently pro-
posed frameworks follow this pattern, developing sophisticated
agents that can decompose tasks, query knowledge bases, and
iteratively explore system data to pinpoint the source of a fault
[27], [28]. Even advanced multiagent frameworks engineered
for “Autonomous CloudOps” concentrate on orchestrating
agents to produce “accurate, reliable, and relevant insights”
for human operators, rather than executing the mitigation
itself [29]. Systems like FLASH are also designed primarily
to improve the accuracy and e ﬃciency of the diagnostic
phase [30]. While these represent a major step forward in
autonomous problem analysis, they do not execute active
mitigation. Their ﬁnal output is typically a root cause diagnosis
intended for a human operator, not an automated remedial
action. This leaves a critical gap in the closed-loop automation
vision, as the crucial step of recovery still requires manual
intervention, highlighting the need for future research to
shift focus from just diagnosis to fully autonomous problem
resolution.
III. F RAMEWORK
A. Cloud–Edge Infrastructure
We consider a distributed and heterogeneous computing
environment that spans both centralized cloud nodes and
geographically distributed edge resources. The infrastructure
is formally deﬁned as the union N =Ncloud∪Nedge, where
each node ni is associated with a capacity vector ri = (ci, mi)
describing its computational and memory capabilities. While
cloud nodes typically o ﬀer high-performance compute and
abundant memory, edge nodes are inherently constrained, often
deployed in proximity to data sources to reduce latency and
bandwidth demands.
B. Application and Service Model
Application workloads are structured as directed microser-
vice graphs A = (S,D), where vertices S denote the set
of services and edges D capture interservice dependencies
and communication ﬂows. Services are deployed as repli-
cated components across the infrastructure, subject to both
platform-speciﬁc constraints and locality awareness to satisfy
latency-sensitive use cases. This enables the ﬂexible placement
of computation closer to where data are generated, without
sacriﬁcing centralized orchestration.
C. Performance Monitoring Framework
To support intelligent decision-making, the system incor-
porates continuous monitoring of runtime behavior. For each
service si, a time-indexed vector of key performance indicators
is maintained
Mi (t) =
˚
li,95 (t), qi,success (t)
	
. (1)
Here, li,95(t) reﬂects the 95th percentile response latency,
while the metric qi,success(t) captures the ratio of successful
requests. These signals are benchmarked against service-
speciﬁc baseline proﬁles Bi, established during periods of
stable operation. Such baselines act as a reference for runtime
anomaly detection.
D. Intent-Based Autonomous Intervention Model
To enable self-adaptive behavior, the system includes a
lightweight autonomous agent capable of reactive intervention.
Rather than relying on static threshold rules, the agent is acti-
vated by high-level performance violation intents—structured,
context-rich alerts that encapsulate both metric deviations
and system state. These intents allow the agent to engage
in intelligent diagnosis and response actions tailored to the
scenario at hand.
1) Trigger and Intent Generation: Intervention is initiated
when the system detects deviations between live metrics and
baseline proﬁles. In such events, a structured intent object
I(t) is generated, designed to encode the operational snapshot
needed for agent reasoning
I (t) =
˝
namespace, timestamp, Bi, Mi (t),C (t)
˛
. (2)
The ﬁeld C(t) refers to the current contextual snapshot of
the system, including topology, deployments, and constraints.
This representation decouples intent processing from low-level
monitoring and equips the agent with a holistic view of the
anomaly landscape.
2) Agent Intervention and Recovery Evaluation: Once trig-
gered, the autonomous agent executes a bounded diagnostic
and mitigation sequence A(t) guided by its reasoning model.
Recovery eﬃcacy is evaluated by remeasuring the monitored
indicators post-intervention and comparing them to the origi-
nal baseline Bi. This process enables a closed feedback loop
for assessing intervention quality and building long-term trust
in autonomous decisions.
The complete high-level architecture of the framework can
be seen in Fig. 1(a).
IV. LLM A GENT METHODOLOGY AND DESIGN
A. Core Loop Architecture
Our autonomous agent, depicted in Fig. 1(b), is designed
around a closed-loop, round-based control paradigm that
seamlessly integrates monitoring, reasoning, and corrective
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
18308 IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026
Fig. 1. Overview of the ARM system components. (a) End-to-end remediation ﬂow from infrastructure monitoring to agent activation. (b) Internal agent loop
for planning, tool invocation, and reasoning. (c) Structured tool layer categorized by functionality.
TABLE I
TOOL CATEGORIES AND REPRESENTATIVE OPERATIONS
actions. Inﬂuenced by the React framework [14], which
extends chain-of-thought (CoT) prompting techniques [31] by
interleaving reasoning and acting in a more interactive manner,
the agent incrementally assembles a cumulative context at
each iteration. This context includes the intent speciﬁcation,
system snapshots, outputs from previously invoked tools, and
records of prior decisions. Importantly, this evolving context
serves only as transient in-context information for the under-
lying model, and no parameter updates or external learning
processes occur. The agent then queries the LLM, which
selects the next tool to execute along with its parameters.
To prevent redundant operations, only novel calls proceed to
execution through temporal caching and recent-call ﬁltering.
The iterative process terminates when the LLM issues the
generate_operational_summary call, or the maxi-
mum number of rounds is reached.
This architecture allows the agent to reason incremen-
tally and adjust its behavior dynamically, while maintaining
transparency. In contrast to multiagent or planner–executor
frameworks, our single-agent loop is easier to audit and
explain: each decision is informed by prior evidence, executed
in a structured manner, and followed by immediate contextual
integration of the result.
B. Tool Abstraction Layer
The agent’s operational capabilities are encapsulated in a
structured tool layer that provides safe, validated access to
Kubernetes actions, metric collection, coordination primitives,
and planning operations. Tools are grouped into four categories
shown in Table I, each exposing typed inputs and producing
structured outputs that are parsed and integrated into the
agent’s evolving context.
Planning tools are central to the agent’s reasoning.
The create_action_plan tool encodes structured intent
through ﬁelds such as a natural language objective,
a list of explicit steps, and a set of risk-mitigation
considerations. These ﬁelds provide a concrete plan trace
that guides future decisions and helps external observers
interpret the agent’s rationale. At the end of execution,
generate_operational_summary produces a detailed
record of completed actions, observed results, and ﬁnal status.
Kubernetes tools expose core resource management oper-
ations to the LLM, including scaling deployments, deleting
pods, or inspecting system state. These tools operate through
an intermediary MCP interface to ensure policy compliance
and encapsulate error handling. By presenting these actions
through abstracted calls (e.g., kubectl_scale with target
namespace and desired replica count), the LLM can issue safe
changes without low-level access. Additionally, safeguards and
human approval workﬂows can be conﬁgured per tool to
ensure that critical changes are carefully controlled and the
system remains protected.
Monitoring tools retrieve time-series data from Prometheus
using domain-speciﬁc ﬁlters. The most frequently used,
prometheus_get_timeseries, allows queries over
CPU, latency, error rate, and other key metrics. Important
parameters include the duration (e.g., “2m”) and the
namespace or service_name to scope the analysis.
These allow the agent to build temporal baselines, detect
anomalies, and validate remediations. Other tools, such as
prometheus_get_service_topology, expose depen-
dency graphs that support causal reasoning during fault
diagnosis.
Finally, utility tools such as sleep_seconds allow the
agent to enforce stabilization delays after disruptive actions
(e.g., pod deletions), ensuring that system metrics reﬂect
steady-state behavior before proceeding.
Each tool call is followed by an immediate reasoning step
in the loop. The agent records what was learned from the tool,
how it a ﬀected the plan, and what should be done next. This
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
A VGERINOS et al.: ARM: AUTONOMOUS REMEDIATION AND MANAGEMENT WITH LLM AGENTS FOR INTENT-DRIVEN CONTROL 18309
inline reﬂection mechanism is central to maintaining decision
quality and justiﬁability.
C. System Prompt Philosophy
The behavior of the LLM agent is governed by a
carefully engineered system prompt that blends structural
constraints with heuristic guidance. This prompt deﬁnes the
agent’s operational role, enforces a disciplined planning-
ﬁrst lifecycle, embeds completion criteria, and encourages
resolution-oriented behavior. Together, these mechanisms
shape the agent’s decision-making while preserving adaptabil-
ity in dynamic infrastructure contexts.
1) Role Deﬁnition and Behavioral Constraints: At its core,
the prompt frames the LLM as an autonomous operator
with the authority to execute corrective actions . This role
assignment is critical; it moves beyond passive diagnostics to
an active, accountable execution model. The prompt encodes
hard constraints that deﬁne legal agent behavior over the
course of each loop. Three structural rules are enforced.
1) The ﬁrst function call must always be
create_action_plan.
2) If the agent’s observations contradict its current assump-
tions, it must reinvoke create_action_plan to
revise the strategy.
3) Termination is allowed only after a
generate_operational_summary has been
issued.
These rules ensure that every agent execution is bounded by
an explicit plan and ends with a structured report. The planning
call encodes an operational objective, a list of steps, and
associated risks—enabling explainable reasoning and traceable
execution. The ﬁnal summary captures what actions were
taken and why, o ﬀering post hoc transparency and account-
ability. Appendix presents an example planning-summary pair,
demonstrating the structured reporting and traceability of agent
actions.
2) Evidence-Guided Reasoning and Completion Criteria:
To promote disciplined reasoning, the system prompt mandates
an evidence-ﬁrst methodology . The agent is not allowed to
intervene until it has gathered suﬃcient data to justify the pro-
posed action. This prevents speculative behavior and ensures
that every step in the plan is grounded in observable system
state.
The prompt also embeds an action bias, which discourages
overanalysis. The agent is instructed to prioritize resolution
over exhaustive diagnosis and to keep progressing toward
remediation. In practice, this means that the agent continually
collects evidence and reﬂects on its progress, but with the
clear expectation that a ﬁx—or a justiﬁed decision to not
intervene—must eventually be produced.
To avoid premature termination, the system deﬁnes mul-
tipart completion criteria: execution can only end when:
1) system metrics trend toward baseline and 2) the agent
provides a convincing rationale for inaction. These constraints
ensure that the agent never halts in an ambiguous or unresolved
state.
3) Heuristic Guidance and Pattern-to-Action Mappings:
While structural rules enforce discipline, the prompt also
TABLE II
EXAMPLE EVIDENCE -TO-ACTION MAPPINGS
provides soft heuristics to guide decision-making. Among
these are pattern-to-action mappings —lookup tables embed-
ded directly in the prompt that associate known symptom
signatures with recommended interventions. For example, the
pairing of high CPU usage and elevated latency suggests either
scaling the workload or modifying resource limits. Table II
oﬀers a simpliﬁed extract of these mappings for illustrative
purposes, noting that the full actionable logic embedded within
the prompt is too extensive to be presented in its entirety.
These heuristics are not binding but serve as priors for
tool selection. They accelerate convergence by steering the
LLM toward common ﬁxes while preserving ﬂexibility for less
canonical cases. This dual strategy—ﬁrm structural scaﬀolding
and soft procedural suggestions—allows the agent to remain
both predictable and adaptive, a critical balance in high-stakes
infrastructure automation.
V. E XPERIMENTAL FRAMEWORK
A. Infrastructure and Cluster Setup
Our experimental framework is deployed on a virtualized
cloud–edge cluster that emulates geographically distributed
IoT environments. The infrastructure consists of seven nodes
organized across three zones: two cloud nodes, four edge
nodes (two per edge site), and one management node respon-
sible for orchestration and observability. Each node runs as an
independent virtual machine connected via a shared overlay
network.
The cluster reﬂects realistic compute asymmetry between
cloud and edge environments: cloud nodes are provisioned
with 4 vCPUs and 4 GB of memory, while edge nodes operate
with 2 vCPUs and 2 GB of memory. All nodes are pinned
to dedicated host cores to ensure performance isolation and
repeatability. Cluster management and workload scheduling
are handled by a k3s Kubernetes distribution deployed on
top of QEMU-virtualized servers. Prometheus and Grafana are
integrated for metrics collection and visualization, while the
control node coordinates chaos experiments, recovery actions,
and data logging.
B. IoT Application Emulator and Scenarios
1) Emulator: To emulate realistic IoT workloads, we
employ an extended version of the MuBench [32] microser-
vice benchmarking framework. MuBench is used to generate
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
18310 IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026
TABLE III
CHAOS FAULT TAXONOMY AND EXPERIMENT DISTRIBUTION
synthetic but semantically coherent microservice applications
that mimic typical IoT service chains. The framework deﬁnes
service dependencies, computational loads, and placement
aﬃnities that determine the deployment of microservices
across the cloud–edge hierarchy.
Each application is speciﬁed via a workmodel.json
conﬁguration, which encodes the set of microservices, their
interservice calls, and associated resource stressors (CPU,
memory, disk, and network). This representation allows repro-
ducible deployments of varying complexity—from lightweight
gateway systems to multitier analytics pipelines—while main-
taining consistent observability and fault injection capabilities
across all experiments.
2) Application Scenarios: Three representative IoT applica-
tions are deployed using the emulator; the microservice graphs
and deployment layouts appear in Fig. 2 (see the dedicated
section/ﬁgure for full diagrams).
1) IoT Gateway System (Three Microservices): Hybrid
edge–cloud setup with most tra ﬃc processed at the
edge for real-time device interaction and cloud handling
complex analytics.
2) Smart Manufacturing System (Eight Microservices):
High-throughput, low-latency data processing focused
on safety-critical operations and predictive maintenance.
3) Smart City Tra ﬃc Management (12 Microservices):
Multitier microservices with diverse latency and
throughput needs, integrating real-time monitoring,
emergency coordination, and analytics.
C. Chaos Engineering and Anomaly Injection
The fault injection campaign follows chaos engineering
principles to systematically evaluate system resilience. Faults
are injected at two primary scopes: 1) service-level (pod-
level) anomalies, including CPU and memory stress and pod
disruptions, which target one or all instances of a given
microservice, and 2) node-level anomalies that simulate host-
wide CPU or memory contention using the chaosd library. The
complete taxonomy of fault modes and experiment counts is
presented in Table III.
As shown in Table III, each experiment group covers both
localized (pod-level) and system-wide (node-level) stressors,
in addition to baseline control executions. The separation by
scope emphasizes how di ﬀerent classes of anomalies a ﬀect
both microservice behavior and overall application latency. In
total, each application undergoes 20 experiments, yielding 60
fault scenarios across all deployments.
D. Four-Phase Experimental Evaluation Protocol
Our evaluation framework employs a systematic four-phase
protocol to assess autonomous agent performance under fault
conditions:
Phase 1 (System Reset and Warmup): We reset the system
by removing any existing node constraints and deploy a fresh
application instance in the cluster. The system then initiates
traﬃc generation and performs service warmup with latency
stabilization detection. This ensures all microservices reach
steady-state operation before baseline measurement.
Phase 2 (Baseline Collection): During stable operation,
the framework captures comprehensive baseline vectors Bi
for each service si, recording key indicators such as 95th
percentile latency li,95(t) and request success rate qi,success(t).
These proﬁles are later used to determine whether recovery
actions have restored normal conditions.
Phase 3 (Chaos Injection): Fault injection occurs while the
system continues serving tra ﬃc, allowing real-time observa-
tion of performance degradation patterns. The deviation of
runtime metrics Mi(t) from Bi also triggers the generation of
structured alert intents I(t), initiating agent activation.
Phase 4 (Agent Recovery): Upon receiving the intent object
I(t), the autonomous agent executes its diagnosis and reme-
diation loop, continuously observing updated Mi(t) vectors to
guide its tool selection. After execution concludes, we evaluate
whether post-intervention metrics satisfy the success condition
described in (3).
This four-phase design enables controlled evaluation of
recovery latency, stability, and correctness under diverse
anomalies, ensuring repeatability and comparability across all
applications.
E. Experiment Success Criterion
We deﬁne a successful recovery as one where the agent
brings each monitored performance indicator back close to its
original baseline. Formally, for any metric xi∈{ li,95, qi,success}
of service si, the recovery at time t′ is considered successful
if ˇˇxi (t′)− xbaseline
i
ˇˇ
xbaseline
i
≤ϵx (3)
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
A VGERINOS et al.: ARM: AUTONOMOUS REMEDIATION AND MANAGEMENT WITH LLM AGENTS FOR INTENT-DRIVEN CONTROL 18311
TABLE IV
AGENT PERFORMANCE COMPARISON BY FAULT TAXONOMY
where xbaseline
i is drawn from the baseline vector Bi and xi(t′)
is the corresponding post-recovery value. In our experiments,
we instantiate the tolerances as
ϵli,95 = 0.15
 
95th percentile latency

ϵqi,success = 0.01
 
request success rate

. (4)
These metric-speciﬁc thresholds provide a uniﬁed bench-
mark across all applications and anomaly types, facilitating
comparative evaluation of both recovery e ﬃciency and cor-
rectness.
VI. R ESULTS AND DISCUSSION
This section presents a comprehensive evaluation of two
autonomous agents built on GPT-5 and GPT-5-mini, respec-
tively, in identifying and mitigating system anomalies within
the simulated cloud–edge environment. We analyze diagnostic
accuracy, remediation success rates, decision rounds, wall-
clock time, and tool utilization patterns, highlighting both the
advantages of the larger model and the limitations that emerge
for the smaller baseline in more complex scenarios.
All experiments utilize GPT-5 as the primary autonomous
remediation agent and GPT-5-mini as a lightweight baseline,
both operating over the same cloud–edge topologies, failure
injections, and observability and actuation tools.
A. Agent Performance by Fault Type
Table IV summarizes performance across the fault taxon-
omy. Across control and node-level anomalies, GPT-5 achieves
near-perfect fault identiﬁcation, correctly recognizing the no-
failure baseline and all node CPU stress cases (100.0%
identiﬁcation accuracy). GPT-5-mini fails to recognize the
baseline as healthy (0.0%) and is slightly less reliable under
node CPU stress (88.9% accuracy).
Remediation success for node CPU stress appears moderate
for both agents (55.6% for GPT-5 and 44.4% for GPT-5-mini)
when viewed through a binary success metric. However, this
binary classiﬁcation obscures the extent of the recovery. Under
our emulation regime, heavily constrained virtual machines
often leave few viable scheduling or scaling options, meaning
that a return to exact baseline levels is not always physically
possible. To quantify the partial mitigation achieved, we intro-
duce the latency recovery metric
Rlat =
lchaos
i,95 − li,95 (t′)
lchaos
i,95 − lbase
i,95
× 100 (5)
where lchaos
i,95 represents the peak 95th percentile latency
observed during the fault injection, li,95(t′) is the post-recovery
latency, and lbase
i,95 is the original baseline value.
Applying this metric reveals that despite the lower binary
success rates, GPT-5 successfully reclaimed 80.4% of the
performance degradation induced by CPU stress, while GPT-
5-mini reclaimed 79.4%. This indicates that even when an
optimal solution was infeasible due to resource exhaustion,
the agents e ﬀectively identiﬁed the root cause and applied
mitigations that substantially alleviated the system bottleneck.
At the pod level, GPT-5 sustains strong diagnostic per-
formance, with identiﬁcation accuracies between 50.0% and
100.0% across CPU, memory, and failure scenarios. GPT-5-
mini, in contrast, struggles particularly with single-pod failures
and memory anomalies, where identiﬁcation can drop to 0.0%
while still achieving moderate to high remediation success.
GPT-5 also completes pod-level incidents in substantially
fewer reasoning rounds (10.2–23.0 versus 27.7–34.2 rounds
for GPT-5-mini) and typically in less wall-clock time.
An apparent discrepancy where remediation success exceeds
identiﬁcation accuracy is particularly pronounced for the
smaller model. For example, in Pod Memory (All Pods) sce-
narios (Table IV), GPT-5-mini records 100.0% success despite
0.0% identiﬁcation accuracy. This arises from how success is
measured in our framework; it is deﬁned purely in terms of
the recovery of latency and success-rate metrics relative to the
pre-fault baseline. In cases where the injected fault is subtle
and fails to produce drastic observable degradation, the smaller
model often fails to classify the speciﬁc root cause (resulting in
0% identiﬁcation) but does not trigger erroneous actions that
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
18312 IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026
TABLE V
AGENT PERFORMANCE BY APPLICATION
Fig. 2. Topologies of the three representative IoT applications, showcasing their microservice interconnections and deployment across edge and cloud
environments.
worsen the state. Consequently, because the metrics remain
within acceptable bounds, the run is algorithmically scored as
a success. This highlights a limitation in the baseline model’s
sensitivity to latent faults compared to GPT-5, which maintains
higher identiﬁcation alignment.
B. Agent Performance by Application
Table V details the performance by application complex-
ity. In the simpler IoT Gateway (three services), GPT-5
signiﬁcantly outperforms the baseline (85.7% versus 40.0%
identiﬁcation accuracy) while requiring fewer decision rounds.
As complexity increases to Smart Manufacturing (7 services)
and Smart City (12 services), GPT-5 maintains robust relia-
bility (identiﬁcation accuracy >80% and success ≥ 80%). In
contrast, GPT-5-mini struggles to scale, dropping to 64.7%
identiﬁcation accuracy in the largest topology and generally
requiring more rounds to converge.
In terms of e ﬃciency, GPT-5 typically completes remedi-
ations faster than GPT-5-mini (e.g., 5.2 versus 12.8 min for
IoT Gateway), utilizing its capacity to plan more e ﬀectively.
The exception is the Smart City topology, where GPT-5-mini
exhibits lower resolution time (7.4 versus 11.8 min), likely
reﬂecting shorter, less thorough reasoning trajectories. Overall,
the larger model leverages its reasoning capabilities to achieve
higher quality outcomes with comparable or better end-to-end
latency.
The consistent stability of GPT-5 across varying topolo-
gies indicates that the model already possesses the requisite
reasoning capacity to manage complex distributed systems.
Consequently, e ﬀective scaling to broader enterprise-grade
microservice architectures relies less on increasing model size
and more on optimizing the information interface. Future
developments should therefore prioritize intelligent context
Fig. 3. Distribution of tool calls made by the agent during experiments.
Observability tools (logs and metrics) dominate the interaction volume,
reﬂecting the high cost of context gathering versus actuation.
compression and highly conﬁgurable tooling, enabling the
agent to dynamically ﬁlter and prioritize vast telemetry data.
This ensures that the model’s reasoning potential is not bottle-
necked by context limits, but rather empowered by a reﬁned
and eﬃcient information architecture.
C. Tool Utilization Analysis
Tool usagestatistics (Fig. 3) reveal distinct behavioral pat-
terns despite a shared focus on observability. GPT-5 exhibits
a streamlined execution proﬁle, utilizing kubectl_apply
(3.77%) for decisive conﬁguration updates while requir-
ing fewer planning iterations ( generate_action_plan:
11.75%). In contrast, GPT-5-mini displays a more frag-
mented workﬂow, relying heavily on granular debugging
tools like kubectl_describe and logs (combined 7.6%)
and invoking generate_action_plan signiﬁcantly more
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
A VGERINOS et al.: ARM: AUTONOMOUS REMEDIATION AND MANAGEMENT WITH LLM AGENTS FOR INTENT-DRIVEN CONTROL 18313
Fig. 4. Service metrics under CPU stress. Left: edge-based sensor data ingestion showing recovery after a disruptive intervention at t≈ 750 s.
Right: cloud-based predictive maintenance analytics showing sustained analysis followed by e ﬀective mitigation at t≈ 1100 s.
often (14.97%). This increased reliance on replanning and
localized patching ( kubectl_patch: 6.48%) suggests that
the smaller model often resorts to iterative trial-and-error,
whereas the larger model acts with greater conviction and
system-level awareness.
The relatively low frequency of actuation calls (e.g., scaling
and restarting pods) compared to diagnostic calls indicates that
the agent is cautious, preferring to gather su ﬃcient evidence
to rule out false positives. This ratio is critical for production
environments, where the cost of a wrong action (such as
restarting a healthy critical service) is high.
D. Agent Mitigation Dynamics
To illustrate the agent’s behavior across di ﬀerent infrastruc-
ture layers, Fig. 4 depicts the remediation trajectories for two
distinct services within the Smart Manufacturing application:
the edge-resident sensor-data-ingestion service and
the cloud-hosted predictive-maintenance-
analytics service.
Both traces exhibit a characteristic “diagnostic plateau”
following the agent’s activation (indicated by the start of
the yellow region). During this phase, the agent is actively
querying observability tools to isolate the root cause from
potential noise.
In the edge scenario (left), the persistence of high latency
until t ≈ 750 s suggests the agent ﬁrst exhausted nondis-
ruptive scaling options—which are naturally limited on edge
nodes—before resorting to a pod restart. This decisive action
is evidenced by the transient dip in success rate, which imme-
diately precedes the return to baseline latency. Conversely, in
the cloud scenario (right), the agent restores performance at
t≈ 1100 s without incurring request failures, leveraging the
greater resource elasticity available in the cloud tier to scale
out the workload. These traces demonstrate the agent’s ability
to adapt its remediation strategy to the speciﬁc constraints
of the deployment environment, prioritizing stability while
ultimately ensuring a return to optimal performance.
VII. C ONCLUSION AND FUTURE WORK
In this work, we introduced a closed-loop framework for
intent-driven infrastructure management that leverages LLM
agents to autonomously detect and remediate SLA viola-
tions in Kubernetes-based IoT and edge environments. Across
three representative IoT applications, the GPT-5-based agent
restores SLA metrics in roughly 80% of fault injection runs
while correctly identifying the underlying condition in about
78% of cases, indicating that LLM agents can e ﬀectively
close the loop in complex cloud–edge topologies. At the same
time, the results reveal some important limitations, including
nonnegligible wall-clock remediation times for the largest
topology, and a distinct performance gap between model sizes,
suggesting that the intricate causal reasoning required for
truly autonomous, zero-touch control currently necessitates the
advanced capabilities of frontier-class models.
Looking ahead, addressing scalability, safety, and integra-
tion with production IoT deployments will be particularly
valuable. On the scalability front, we plan to investigate
improved context-compression paradigms and deeper agent
architectures equipped with a more diverse tool set spanning
low-level metric queries to ML-based anomaly detection algo-
rithms, as well as ﬁne-tuning smaller models to better trade
oﬀ accuracy versus model size in this domain. In parallel, we
aim to formalize and evaluate safety safeguards around high-
impact actions and to deploy the framework in larger, more
heterogeneous IoT testbeds that more closely reﬂect real-world
operational constraints.

## § Appendix

Initial Action Plan
Objective: Investigate and remediate performance degrada-
tion in namespace app smart manufacturing to restore
latency and success rate to baseline.
Situation: Alert indicates p95 latency increased from 0.207
to 0.451 s (+ 118%) with success rate dropping from 100% to
99.25% as of 2025-11-13T09:29:21Z. Root cause unknown;
need to conﬁrm scope /severity and correlate with pod /node
resource signals.
Steps:
1) Phase 1—Scope and Severity: Query 2-min time-
series for latency, CPU, and memory in namespace
app smart manufacturing ; query node CPU
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
18314 IEEE INTERNET OF THINGS JOURNAL, VOL. 13, NO. 9, 1 MAY 2026
timeseries; get node readiness /health via kubectl
get nodes -o wide .
2) Phase 2—Pattern Analysis: Correlate workload met-
rics with node metrics; list pods with placement
via kubectl get pods -o wide ; inspect service
topology for upstream /downstream hotspots.
3) Decision Branch:
a) If node_cpu≫ pod_cpu on a node with colo-
cated pods showing high latency, cordon+drain that
node.
b) If a speciﬁc pod shows runaway CPU /memory or
restarts, delete/restart the pod.
c) If CPU saturation across replicas, patch HPA to
raise min/max replicas appropriately.
d) If memory pressure is causing OOM /restarts, raise
limits or scale out via HPA.
4) Phase 3—Response and Validation: Execute selected ﬁx,
wait 60 s, recheck latency /CPU, and iterate if needed.
5) Completion: When p95 latency trends back toward base-
line and success rate ≥ 99.9%, produce operational
summary with problem locations identiﬁed.
Expected Outcomes:
1) Quantiﬁed severity window and implicated resources
identiﬁed (pods/nodes).
2) If node-level contention: a ﬀected node drained and
workloads rescheduled.
3) If pod-level issue, problematic pod restarted and stabi-
lized.
4) If a capacity issue, HPA scaled to add replicas, reducing
per-pod CPU and latency.
5) Validated improvement with metrics trending toward
baseline.
Operational Summary (Post-Execution)
Objective: Resolve performance degradation in namespace
app smart manufacturing by mitigating CPU satura-
tion and restoring latency toward baseline.
Status: COMPLETED—CPU saturation mitigated via HPA
scale-out and aﬃnity relaxation; latency trending toward base-
line and node CPU normalized.
Actions Completed:
1) Collected 2-m namespace latency and CPU
metrics; identiﬁed predictive-maintenance-
analytics-cloud pods consuming∼3.3 cores each
with cloud-worker-1/2 node CPU ∼3.9 cores
(saturation).
2) Veriﬁed HPA constraints causing ScalingLimited;
patched predictive-maintenance-
analytics-cloud-autoscaler to minReplicas
= 3 and maxReplicas = 6.
3) Validated limited improvement; inspected deployment
aﬃnity (restricted to zone = cloud).
4) Patched deployment predictive-maintenance-
analytics-cloud nodeAﬃnity to allow zones
[cloud, edge-site-1, edge-site-2] and restarted rollout to
redistribute workload.
5) Revalidated metrics: pods rescheduled across edge and
cloud nodes; node CPU normalized; service latencies
dropped.
Results Achieved:
1) Predictive-maintenance-analytics-cloud
replicas increased to 6 and distributed across cloud and
edge nodes (observed new pods on edge-site-1 /2 and
cloud workers).
2) Cloud worker CPU pressure reduced (node
pod_cpu/host CPU from ∼3.4/3.9 cores down to
≤ 0.5 cores).
3) Latency improved across services: centralized
data lake cloud ∼450–480ms → 48–86ms;
ingestion services reduced to ∼97-287 ms, trending
toward baseline 207 ms.
Problem Location:
1) Predictive-maintenance-analytics-cloud
(deployment).
2) Predictive-maintenance-analytics-cloud-
autoscaler (hpa).
3) Cloud-worker-1 (node).
4) Cloud-worker-2 (node).

## § References

[1] B. T. Loo et al., “Declarative networking,” Commun. ACM , vol. 52,
no. 11, pp. 87–95, Nov. 2009.
[2] R. Birkner, D. Drachsler-Cohen, L. Vanbever, and M. Vechev, “Net2Text:
Query-guided summarization of network forwarding behaviors,” in Proc.
15th USENIX Symp. Networked Syst. Design Implement. (NSDI 18) ,
Apr. 2018, pp. 609–623. [Online]. Available: https: //www.usenix.org/
conference/nsdi18/presentation/birkner
[3] A. Adewa, V . Anyah, O. David Olufemi, A. Ojo Oladejo, and T. Olaifa,
“The impact of intent-based networking on network conﬁguration man-
agement and security,” Global J. Eng. Technol. Adv. , vol. 22, no. 1,
pp. 63–68, Jan. 2025.
[4] J. Kim, H. Okhravi, D. Tian, and B. E. Ujcich, “Security challenges
of intent-based networking,” Commun. ACM, vol. 67, no. 7, pp. 56–65,
Jul. 2024.
[5] S. T. Arzo, C. Naiga, F. Granelli, R. Bassoli, M. Devetsikiotis, and
F. H. P. Fitzek, “A theoretical discussion and survey of network
automation for IoT: Challenges and opportunity,” IEEE Internet Things
J., vol. 8, no. 15, pp. 12021–12045, Aug. 2021.
[6] P. Lewis et al., “Retrieval-augmented generation for knowledge-intensive
NLP tasks,” 2020, arXiv:2005.11401.
[7] T. Schick et al., “Toolformer: Language models can teach themselves
to use tools,” in Proc. Conf. Neural Inf. Process. Syst. , vol. 36, 2023,
pp. 68539–68551.
[8] A. Novikov et al., “AlphaEvolve: A coding agent for scientiﬁc and
algorithmic discovery,” 2025, arXiv:2506.13131.
[9] D. Huang, J. M. Zhang, M. Luck, Q. Bu, Y . Qing, and H. Cui,
“AgentCoder: Multi-agent-based code generation with iterative testing
and optimisation,” 2023, arXiv:2312.13010.
[10] H. Zhang et al., “HuatuoGPT, towards taming language model to be a
doctor,” 2023, arXiv:2305.15075.
[11] L. Bao, S. Yun, J. Lee, and T. Q. S. Quek, “LLM-hRIC: LLM-
empowered hierarchical RAN intelligent control for O-RAN,” 2025,
arXiv:2504.18062.
[12] S. Kou, C. Yang, and M. Wu, “SAFLA: Semantic-aware full
lifecycle assurance designed for intent-driven networks,” 2024,
arXiv:2404.12305.
[13] B. Adnan, S. Miryala, A. Sambu, K. Vaidhyanathan, M. De Sanctis, and
R. Spalazzese, “Leveraging llms for dynamic IoT systems generation
through mixed-initiative interaction,” in Proc. IEEE 22nd Int. Conf.
Softw. Archit. Companion (ICSA-C) , Mar. 2025, pp. 488–497.
[14] S. Yao et al., “ReAct: Synergizing reasoning and acting in language
models,” 2022, arXiv:2210.03629.
[15] A. Vitui and T.-H. Chen, “Empowering AIOps: Leveraging large lan-
guage models for IT operations management,” 2025, arXiv:2501.12461.
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply. 
A VGERINOS et al.: ARM: AUTONOMOUS REMEDIATION AND MANAGEMENT WITH LLM AGENTS FOR INTENT-DRIVEN CONTROL 18315
[16] X. Hou, Y . Zhao, S. Wang, and H. Wang, “Model context protocol
(MCP): Landscape, security threats, and future research directions,”
2025, arXiv:2503.23278.
[17] B. Martini, M. Gharbaoui, and P. Castoldi, “Intent-based network slicing
for SDN vertical services with assurance: Context, design and prelimi-
nary experiments,” Future Gener. Comput. Syst., vol. 142, pp. 101–116,
May 2023.
[18] S. Braghin and L. Nedoshivina, “MIMO: A framework for extensible
and ﬂexible intent-based workload meta-orchestration,” in Proc. 2nd Int.
Workshop MetaOS Cloud-Edge-IoT Continuum , 2025, pp. 1–6.
[19] S. Mostafa, M. P. Mota, A. Valcarce, and M. Bennis, “Intent-
aware DRL-based NOMA uplink dynamic scheduler for IIoT,”
IEEE Trans. Cognit. Commun. Netw. , vol. 11, no. 6, pp. 4041–4049,
Dec. 2025.
[20] T. He, A. N. Toosi, N. Akbari, M. T. Islam, and M. A. Cheema,
“An intent-based framework for vehicular edge computing,” in Proc.
IEEE Int. Conf. Pervasive Comput. Commun. (PerCom) , Mar. 2023,
pp. 121–130.
[21] N. Filinis et al., “Intent-driven orchestration of serverless applications
in the computing continuum,” Future Gener. Comput. Syst. , vol. 154,
pp. 72–86, May 2024.
[22] Y . Cheng et al., “Say what you mean: Natural language access
control with large language models for Internet of Things,” 2025,
arXiv:2505.23835.
[23] J. Mcnamara et al., “NLP powered intent based network management for
private 5G networks,” IEEE Access, vol. 11, pp. 36642–36657, 2023.
[24] D. Kikuta, H. Ikeuchi, and K. Tajiri, “ChaosEater: Fully
automating chaos engineering with large language models,” 2025,
arXiv:2501.11107.
[25] Z. Ye, T. Huynh Minh Le, and M. Ali Babar, “LLMSecConﬁg: An
LLM-based approach for ﬁxing software container misconﬁgurations,”
2025, arXiv:2502.02009.
[26] K. Mehmood, K. Kralevska, and D. Palma, “Intent-driven autonomous
network and service management in future cellular networks: A struc-
tured literature review,” Comput. Netw. , vol. 220, Jan. 2023, Art. no.
109477.
[27] D. Ziqi Zhou and M. Fokaefs, “AI assistants for incident lifecycle
in a microservice environment: A systematic literature review,” 2024,
arXiv:2410.04334.
[28] C. Pei et al., “Flow-of-action: SOP enhanced LLM-based multi-agent
system for root cause analysis,” in Proc. ACM Web Conf. , 2025,
pp. 422–431.
[29] K. Parthasarathy et al., “Engineering LLM powered multi-agent frame-
work for autonomous CloudOps,” 2025, arXiv:2501.08243.
[30] X. Zhang et al., “Flash: A workﬂow automation agent for diagnosing
recurring incidents,” Microsoft Res., Redmond, W A, USA, Tech. Rep.,
2024.
[31] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
language models,” 2022, arXiv:2201.11903.
[32] A. Detti, L. Funari, and L. Petrucci, “ µ Bench: An open-source factory
of benchmark microservice applications,” IEEE Trans. Parallel Distrib.
Syst., vol. 34, no. 3, pp. 968–980, Mar. 2023.
Authorized licensed use limited to: Universidade Federal dos Pampas (UNIPAMPA). Downloaded on May 15,2026 at 20:20:44 UTC from IEEE Xplore.  Restrictions apply.
