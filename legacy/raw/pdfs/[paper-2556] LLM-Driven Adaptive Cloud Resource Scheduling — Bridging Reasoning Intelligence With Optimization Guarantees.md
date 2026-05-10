---
title: "LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees"
authors:
  - GUANYU DING
  - SHIYU YANG
  - HAN LIN
  - ZIFAN CHEN
  - JIE SI YANG
affiliations:
  - name: "New York University"
    location: "New York, NY 10012 USA"
  - name: "University of California, Los Angeles"
    location: "Los Angeles, CA 90095 USA"
  - name: "University of Wisconsin-Madison"
    location: "Madison, WI 53706 USA"
  - name: "University of Pennsylvania"
    location: "Philadelphia, PA 19104 USA"
  - name: "The University of Utah"
    location: "Salt Lake City, UT 84112 USA"
corresponding_author: "GUANYU DING (gd2292@nyu.edu)"
doi: "10.1109/OJCS.2026.3667549"
publication_date: "24 February 2026"
received_date: "13 January 2026"
accepted_date: "21 February 2026"
abstract: |
  Cloud resource scheduling presents a fundamental challenge in modern distributed computing, where heterogeneous workloads, complex task dependencies, and multi-objective optimization requirements exceed the capabilities of traditional rule-based and small-scale machine learning approaches. Existing schedulers struggle to dynamically adapt to evolving workload patterns while simultaneously satisfying Service Level Agreement (SLA) constraints, resource efficiency targets, and fairness policies. This article introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework that synergistically combines the contextual reasoning capabilities of foundation models with the execution guarantees of classical optimization techniques. Our approach transforms heterogeneous cluster states—including task dependency graphs, real-time resource utilization metrics, and SLA specifications—into a unified structured-textual representation that leverages LLMs' few-shot learning and causal reasoning abilities to generate intelligent scheduling candidates. These candidates are subsequently refined through a lightweight Integer Linear Programming (ILP) module that ensures feasibility and optimality under resource constraints. We evaluate LLMSched on Google's production cluster trace dataset, demonstrating significant improvements over state-of-the-art baselines: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations across diverse workload scenarios. Extensive ablation studies validate the contributions of each architectural component, while robustness analysis under workload perturbations confirms the framework's practical viability. Our work establishes a new paradigm for intelligent resource management that bridges the gap between neural reasoning and algorithmic precision, opening avenues for LLM applications in systems optimization domains.
keywords:
  - "Cloud computing"
  - "Resource scheduling"
  - "Large language models (LLMs)"
  - "Adaptive optimization"
  - "Task orchestration"
  - "SLA management"
---

Received 13 January 2026; accepted 21 February 2026. Date of publication 24 February 2026; date of current version 18 March 2026. The review of this article was arranged by Associate Editor Laizhong Cui.

Digital Object Identifier 10.1109/OJCS.2026.3667549

## LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees

GUANYU DING 1 , SHIYU YANG 2 , HAN LIN 3 (Member, IEEE), ZIFAN CHEN 4 , AND JIE SI YANG 5

### Affiliations

1 New York University, New York, NY 10012 USA
2 University of California, Los Angeles, Los Angeles, CA 90095 USA
3 University of Wisconsin-Madison, Madison, WI 53706 USA
4 University of Pennsylvania, Philadelphia, PA 19104 USA
5 The University of Utah, Salt Lake City, UT 84112 USA

**Corresponding Author:** GUANYU DING (e-mail: gd2292@nyu.edu)

ABSTRACT Cloud resource scheduling presents a fundamental challenge in modern distributed computing, where heterogeneous workloads, complex task dependencies, and multi-objective optimization requirements exceed the capabilities of traditional rule-based and small-scale machine learning approaches. Existing schedulers struggle to dynamically adapt to evolving workload patterns while simultaneously satisfying Service Level Agreement (SLA) constraints, resource efficiency targets, and fairness policies. This article introduces LLMSched , a novel Large Language Model (LLM)-driven adaptive scheduling framework that synergistically combines the contextual reasoning capabilities of foundation models with the execution guarantees of classical optimization techniques. Our approach transforms heterogeneous cluster states-including task dependency graphs, real-time resource utilization metrics, and SLA specifications-into a unified structured-textual representation that leverages LLMs' few-shot learning and causal reasoning abilities to generate intelligent scheduling candidates. These candidates are subsequently refined through a lightweight Integer Linear Programming (ILP) module that ensures feasibility and optimality under resource constraints. We evaluate LLMSched on Google's production cluster trace dataset, demonstrating significant improvements over state-of-the-art baselines: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations across diverse workload scenarios. Extensive ablation studies validate the contributions of each architectural component, while robustness analysis under workload perturbations confirms the framework's practical viability. Our work establishes a new paradigm for intelligent resource management that bridges the gap between neural reasoning and algorithmic precision, opening avenues for LLM applications in systems optimization domains.

INDEX TERMS Cloud computing, resource scheduling, large language models (LLMs), adaptive optimization, task orchestration, SLA management.

## I. INTRODUCTION

Cloud computing has fundamentally reshaped modern information technology by enabling on-demand access to large-scale computational resources for applications ranging from web services to scientific computing [1], [2]. As cloud infrastructures continue to scale to millions of servers across geographically distributed datacenters [3], efficient resource scheduling has become a critical challenge affecting both operational cost and quality of service. Modern cloud platforms must coordinate heterogeneous workloads—including latency-sensitive microservices, batch analytics, and machine learning tasks—each with distinct resource demands and Service Level Agreement (SLA) requirements [4], [5].

Traditional cloud schedulers primarily rely on hand-crafted heuristics and rule-based policies [6], [7], [8]. While these approaches offer predictability and low overhead, they struggle to cope with the growing complexity of modern workloads.

In particular, static heuristics fail to capture intricate task dependencies and data locality constraints [9], adapt to temporal workload variations [10], or balance multiple conflicting objectives such as efficiency, fairness, and latency [11]. These limitations often result in suboptimal resource utilization under dynamic conditions.

Recent advances in machine learning have motivated learning-based scheduling approaches, especially those based on deep reinforcement learning (DRL) [12], [13], [14]. While such methods show promising results in controlled environments, their deployment in production systems remains challenging. DRL schedulers require extensive training data and carefully designed reward functions, making them brittle under workload distribution shifts [15]. Moreover, the black-box nature of neural policies hinders interpretability and debugging, which are essential for mission-critical cloud systems [16]. Existing models also rely on low-dimensional numerical state representations, discarding rich semantic information available in task descriptions, dependency graphs, and system logs [17].

The emergence of Large Language Models (LLMs), such as GPT-4 [18], Claude [19], and LLaMA [20], has demonstrated strong capabilities in reasoning, planning, and knowledge synthesis [21]. These models offer several properties attractive for scheduling, including contextual understanding of heterogeneous inputs [22], few-shot adaptability [23], chainof-thought reasoning [24], and semantic interpretation of natural language constraints [25]. Early studies have explored their potential in code generation, system configuration, and workflow optimization [26], [27], [28], suggesting promise for systems-level decision making.

However, directly applying LLMs to cloud scheduling poses fundamental challenges. Scheduling decisions must satisfy hard constraints that cannot be guaranteed by probabilistic language model outputs [29]. Furthermore, the inference latency of LLMs is incompatible with the high-throughput, low-latency requirements of production schedulers [30]. LLMs may also generate syntactically valid yet semantically incorrect plans that violate system invariants [31]. These issues highlight the need for a hybrid design that leverages LLM reasoning while preserving algorithmic correctness and efficiency.

In this article, we propose LLMSched, a hybrid framework that integrates LLM-driven high-level reasoning with classical optimization for adaptive cloud resource scheduling. Rather than using LLMs as end-to-end decision makers, LLMSched positions them as policy generators that explore promising regions of the solution space, while delegating constraint enforcement and fine-grained optimization to algorithmic modules. The framework consists of three stages. (1) Structured-Textual State Representation encodes heterogeneous cluster information, including task DAGs, resource metrics, historical outcomes, and SLA specifications, into a compact textual format suitable for LLM reasoning. (2) LLM-Guided Candidate Generation employs few-shot and chain-of-thought prompting to produce diverse scheduling candidates that consider data locality, load balancing, and task priorities. (3) Optimization-Based Refinement uses a lightweight Integer Linear Programming (ILP) solver to enforce hard constraints and optimize a multi-objective utility function, ensuring correctness and robustness. Especially, to mitigate inference overhead, LLMSched incorporates caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur. For routine scheduling decisions, validated strategies are executed by fast heuristic modules, achieving sub-millisecond latency while retaining adaptability.

Our contributions are summarized as follows: (1) We introduce the first LLM-driven cloud scheduling framework that systematically combines foundation model reasoning with classical optimization. (2) We design a structured-textual state representation and constraint-guided prompting strategies that enable interpretable and effective LLM-based scheduling. (3) We develop a hybrid optimization architecture that guarantees scheduling correctness through lightweight ILP refinement with practical overhead. (4) We conduct extensive evaluations on large-scale production traces, demonstrating consistent improvements over diverse baselines and providing insights into when and why LLM-guided scheduling is effective.

## II. RELATED WORKS

Traditional Cloud Scheduling Systems: Cloud scheduling has evolved from early batch systems such as Condor [32] and Sun Grid Engine to large-scale cluster managers designed for heterogeneous, multi-tenant workloads. Google's Borg [5] established a production-grade centralized scheduling architecture with admission control, priority-based preemption, and bin-packing, while Kubernetes [33], [34] operationalized these ideas for container orchestration via extensible, heuristic-driven schedulers. Alternative paradigms include two-level schedulers that delegate decisions to application frameworks (e.g., Mesos [7], YARN [8]) and optimistic concurrency control for parallel scheduling (Omega [6]). Recent work further explores fairnessand resource-aware policies, such as DRF [35], multi-dimensional bin packing (Tetris [36]), and specialized accelerators scheduling (Carbyne [37]). Despite their maturity and robustness, these systems rely predominantly on manually designed heuristics and objective-specific policies, which limits their ability to adapt to complex, evolving workload semantics.

Learning-Based Scheduling Approaches: Recent years have seen extensive efforts to apply learning-based methods to cluster and resource scheduling. Early work such as DeepRM [12] formulates scheduling as an MDP and demonstrates that deep reinforcement learning can outperform heuristic policies. Subsequent systems explore richer models and learning paradigms, including GNN-based dependency modeling for DAG jobs (Decima [38]), performance prediction via Bayesian optimization (Auto-Tune [39]), temporal workload modeling with RNNs (NNS [40]), and multi-agent reinforcement learning for distributed scheduling (Chronus [41]). Despite promising results, learning-based schedulers suffer from practical limitations, including heavy reliance on representative training traces [42], sensitivity to distribution shift [43], limited interpretability [44], and restricted state representations that overlook high-level semantic information [45]. To mitigate these issues, hybrid systems combine learning with optimization, using learned models for demand or cost estimation while relying on mathematical solvers for decision making (e.g., Cilantro [46], Harmony [47]). Our work follows this hybrid philosophy and further extends it by leveraging the reasoning capabilities of large language models.

Large Language Models in Systems Large language models have recently been explored beyond NLP, first demonstrating strong capabilities in code generation and software engineering tasks (e.g., Codex [26], AlphaCode [48]), with broad adoption in developer workflows. Building on this success, a growing body of work investigates LLMs for systems problems, including failure diagnosis (D-Bot [49]), control and optimization via natural-language reasoning (LLMLight [50]), and database query optimization (xTuring [51]). LLMs have also been applied to system configuration and tuning, such as generating Kubernetes parameters (LLMAO [27]), recommending Spark configurations (Config-GPT [52]), and automating database administration tasks (AutoAdmin [53]). Despite promising results, these systems largely operate in offline or advisory settings, with human validation prior to deployment. Direct use of LLMs for real-time or safety-critical control remains limited due to fundamental challenges, including lack of hard constraint guarantees [29], high inference latency [54], and susceptibility to hallucinations in numerical or low-level reasoning [55]. Recent work therefore advocates hybrid paradigms that restrict LLMs to semantic understanding and heuristic generation while delegating constraint satisfaction to formal solvers, as exemplified by LLM-modulo frameworks [31]. Our work follows this line of thinking by explicitly separating LLM reasoning from algorithmic guarantees.

## III. PRELIMINARIES

In this section, we formalize the cloud resource scheduling problem and establish the mathematical foundations for our LLM-driven approach. We define key concepts including cluster models, task representations, resource constraints, and optimization objectives that guide our system design.

### A. Cloud Resource Model

We model a cloud cluster as a heterogeneous collection of physical machines (PMs), denoted as a set M = {M₁, M₂, . . . , Mₘ}, where m is the total number of machines. Each machine Mᵢ is characterized by its resource capacity vector cᵢ = (cpuᵢ, memᵢ, diskᵢ, gpuᵢ), representing provisioned CPU cores, memory, storage, and specialized hardware accelerators respectively. At time t, the available resource on machine Mᵢ is represented as aᵢ(t) = cᵢ − dᵢ(t), where dᵢ(t) is the total resource demand of currently running tasks. We denote the set of all running tasks at time t as T(t).

### B. Task and Job Model

A job consists of a directed acyclic graph (DAG) of interdependent tasks. We denote a job j as J = (T, E), where T = {T₁, T₂, . . . , Tₙ} is the set of tasks and E represents dependency edges. Each task Tₖ is characterized by:

<!-- formula-not-decoded -->

where:

- rₖ = (cpu, mem, disk, gpu) is the resource demand vector
- pₖ is the priority level (higher values indicate higher priority)
- sₖ and dₖ represent the earliest start time and deadline respectively
- depₖ ⊂ T denotes the set of predecessor tasks

### C. SLA and Performance Model

Service Level Agreements specify performance targets for submitted jobs. We model SLA constraints as latency bounds Lⱼ for each job j, representing the maximum acceptable job completion time from submission to completion. A job violates its SLA if its actual completion time exceeds Lⱼ. We define:

<!-- formula-not-decoded -->

where Cⱼ is the completion time of job j.

### D. Scheduling Decision Space

At each scheduling epoch, the scheduler makes placement and ordering decisions. A scheduling decision δ assigns each unscheduled task Tₖ ∈ T to a machine Mᵢ ∈ M and determines its execution order relative to other tasks on that machine, subject to:

1. Resource feasibility: the assigned machine has sufficient available resources
2. Dependency constraints: all predecessor tasks have completed
3. Time constraints: placement respects deadline and priority constraints

### E. Optimization Objective

LLMSched optimizes a multi-objective utility function that balances competing goals:

<!-- formula-not-decoded -->

where:

- α, β, γ, δ are weights balancing different objectives
- Tcompletion represents average job completion time
- Eutilization measures cluster-wide resource utilization
- VSLA represents the count of SLA violations
- Ffairness is a fairness metric ensuring equitable resource allocation

## IV. METHODOLOGY

This section describes the three-stage architecture of LLMSched: Structured-Textual State Representation, LLM-Guided Candidate Generation, and Optimization-Based Refinement.

### A. Structured-Textual State Representation

To enable effective LLM reasoning over heterogeneous cluster states, we design a compact, interpretable textual representation that captures essential scheduling information. The representation consists of five components:

1. **Cluster Status Summary**: aggregate statistics describing current machine utilization, free resource capacity, and distribution across resource types.

2. **Pending Job Queue**: a structured list of waiting jobs, each annotated with resource demands, deadlines, priorities, and dependency information encoded in a naturallanguage format.

3. **Task Dependency Graph (DAG) Encoding**: for each job, we encode the task DAG as a structured text describing task sequences, data flow, and critical path constraints.

4. **Historical Performance Data**: past scheduling decisions and their outcomes (completion times, resource contention, SLA violations) are summarized as patterns to guide LLM reasoning.

5. **SLA and Constraint Summary**: explicit statements of active SLA deadlines, resource limits, and fairness policies expressed in natural language.

The complete state representation is compiled into a single prompt context that fits within LLM context windows while preserving sufficient detail for informed decision making.

### B. LLM-Guided Candidate Generation

We employ a two-stage prompting strategy to generate diverse, high-quality scheduling candidates:

**Stage 1 — Chain-of-Thought Reasoning**: The LLM is prompted to reason through the scheduling problem step-by-step, considering task priorities, resource availability, data locality, and deadline constraints. Prompts are designed to elicit explicit reasoning about trade-offs between efficiency, fairness, and latency. Example prompt template:

> You are a cloud resource scheduler. Given the cluster state and pending jobs, reason through the following: (1) Which jobs have the most urgent deadlines? (2) Which tasks have the highest resource contention? (3) Where can data locality be exploited? (4) How should priorities be balanced? Based on your reasoning, propose a scheduling decision.

**Stage 2 — Candidate Enumeration**: Building on the reasoning trace, we prompt the LLM to generate k diverse candidate placements, explicitly instructing the model to explore different trade-off points along the Pareto frontier (efficiency vs. latency vs. fairness). This diversification is critical for downstream optimization refinement.

### C. Optimization-Based Refinement

The candidates generated by the LLM, while semantically reasonable, may violate hard resource or temporal constraints. To guarantee feasibility and achieve optimality, we employ a lightweight Integer Linear Programming (ILP) solver to refine candidates. The ILP formulation captures:

1. **Feasibility Constraints**: resource capacity constraints, dependency precedence, and temporal ordering.

2. **Optimality Objective**: maximize utility across efficiency, fairness, and SLA compliance.

The ILP solver operates in two modes:

- **Refinement Mode**: if a candidate is infeasible, the solver repairs it by adjusting task placements while minimizing perturbation from the LLM-suggested solution.
- **Optimization Mode**: if a candidate is feasible, the solver performs limited local optimization to improve objective value subject to a timeout budget.

Both modes use solver time budgets (typically 10-100 ms) to ensure scheduling latency remains acceptable for production deployments.

### D. Caching and Adaptive Triggering

To mitigate LLM inference overhead, LLMSched implements an adaptive triggering mechanism:

1. **State Change Detection**: monitor cluster state and incoming job queue for significant changes (e.g., new high-priority job arrival, resource availability drop below threshold, SLA violation risk).

2. **LLM Invocation Decision**: trigger LLM reasoning only when state changes exceed predefined thresholds. For stable states, rely on cached decisions from previous epochs validated by heuristic checks.

3. **Fallback Heuristic**: during periods of high arrival load or LLM unavailability, a fast bin-packing heuristic ensures continuous scheduling operation without LLM dependency.

### E. Implementation Details

LLMSched is implemented as a modular Python system with the following components:

- **State Encoder**: translates cluster state snapshots into structured-textual prompts.
- **LLM Client**: interfaces with OpenAI's GPT-4 API (or compatible LLM services).
- **Candidate Generator**: orchestrates multi-stage prompting and collects diverse candidates.
- **ILP Solver**: wraps the Gurobi optimization solver for constraint refinement.
- **Scheduler Loop**: integrates all components into a continuous event-driven scheduling service.

The system is designed to operate with production cluster management systems (e.g., Kubernetes, Borg-like schedulers) by translating LLMSched decisions into native scheduling commands.

### F. Computational Complexity and Latency Analysis

The per-scheduling-epoch latency is dominated by LLM inference time (100-500 ms for GPT-4 depending on prompt size) and ILP solver time (10-100 ms). Total end-to-end latency ranges from ~150-600 ms per epoch. This is acceptable for batch and analytics workloads but may be challenging for ultra-latency-sensitive services. The adaptive triggering mechanism reduces effective frequency of LLM invocation to ~10-20% of scheduling epochs in typical workloads, bringing average latency overhead to acceptable levels.

## V. EXPERIMENTS

### A. Experimental Setup

**Cluster Traces**: We evaluate LLMSched using Google's Cluster Trace v2 dataset, which contains 12.5 million jobs scheduled across a heterogeneous cluster over 30 days. The trace includes detailed task resource demands, temporal patterns, and job dependencies, representing realistic production workloads.

**Baseline Strategies**: We compare against:

1. **Borg-Style Bin Packing** (BP): a heuristic baseline implementing Google's production Borg scheduler logic.
2. **Best Fit Decreasing (BFD)**: a classical bin-packing algorithm.
3. **DeepRM**: a deep reinforcement learning scheduler trained on the same trace data.
4. **Decima**: a GNN-based learning scheduler optimized for DAG job completion time.
5. **Harmony**: a hybrid optimization-learning scheduler combining learned cost models with mathematical optimization.

**Evaluation Metrics**:

- **Average Job Completion Time (AJCT)**: mean time from submission to completion across all jobs.
- **Resource Utilization**: cluster-wide average utilization across all resource types.
- **SLA Violations**: percentage of jobs exceeding their deadline constraints.
- **Fairness Index (Jain's Index)**: measures equitable resource allocation across jobs.

**LLMSched Configuration**: We use GPT-4 as the underlying LLM, k=5 candidate generation, ILP solver timeout of 50 ms, and triggering threshold set to detect 15% state change magnitude.

### B. Main Results

LLMSched achieves significant improvements over all baselines:

<!-- formula-not-decoded -->

**Key Findings**:

1. **Completion Time**: LLMSched reduces AJCT by 23.7% compared to Borg, the strongest heuristic baseline. Improvements are driven by better task ordering and data locality exploitation via LLM reasoning.

2. **Resource Utilization**: LLMSched improves cluster-wide utilization by 18.4% over Borg, suggesting more efficient task-to-machine assignments that reduce fragmentation.

3. **SLA Compliance**: LLMSched achieves a 31.2% reduction in SLA violations compared to Borg, indicating superior adherence to deadline constraints.

4. **Fairness**: LLMSched maintains or slightly improves fairness compared to baselines, avoiding concentration of resources in high-priority jobs at the expense of lower-priority ones.

5. **Computational Overhead**: The average per-epoch latency is ~220 ms, but with adaptive triggering reducing LLM invocation frequency to ~15%, the effective scheduling latency overhead remains acceptable.

### C. Sensitivity Analysis

We analyze the impact of key design parameters:

**LLM Model Size**: Smaller models (GPT-3.5) produce lower-quality candidates, reducing AJCT improvement to ~15%. Larger models (GPT-4-Turbo) provide marginal additional gains (~2%) at higher cost.

**Candidate Count (k)**: Increasing k from 1 to 7 shows diminishing returns. k=5 offers a good balance between solution quality and computational cost.

**ILP Solver Timeout**: Increasing timeout from 10 ms to 100 ms provides modest improvements (~3-5%), but diminishing returns suggest 50 ms is near-optimal for production use.

**Triggering Threshold**: Lower thresholds trigger LLM more frequently, improving solution quality but increasing latency. Threshold of 15% provides a practical balance.

### D. Ablation Study

We evaluate the contribution of each component:

<!-- formula-not-decoded -->

**Findings**:

- **Structured-Textual Representation Effectiveness**: removing LLM reasoning (using only random candidate generation) reduces improvements to <5%, validating that LLM reasoning provides substantial value.
- **Optimization-Based Refinement**: disabling ILP refinement causes 8-12% degradation in SLA compliance, as infeasible or suboptimal candidates from LLM are not corrected.
- **Caching and Adaptive Triggering**: disabling the triggering mechanism (invoking LLM every epoch) improves solution quality by ~2-3% but increases latency by 4-5×, making it impractical.

### E. Robustness Under Workload Perturbations

We test LLMSched resilience to workload distribution shifts by evaluating on synthetic traces generated via:

1. **Job arrival rate variation**: ±25% perturbation to inter-arrival times.
2. **Resource demand scaling**: ±20% uniform scaling of task resource vectors.
3. **Deadline tightening**: reducing deadline slack by 15%.

Results show LLMSched maintains performance degradation <8% under these perturbations, outperforming baselines (which degrade 15-25%), suggesting better generalization.

### F. Generalization to Smaller Clusters

We evaluate scalability by running experiments on sub-sampled traces representing smaller clusters (100 machines, 1000 machines, 5000 machines vs. the full 10,000 machines in the original trace). LLMSched maintains improvement margins across all cluster sizes, with slightly larger improvements on smaller clusters due to reduced problem complexity.

### G. Real System Deployment

We conducted a limited production trial integrating LLMSched with a Kubernetes cluster hosting internal microservices (scope: ~200 nodes, ~5000 running containers). Over a one-week trial period, we observed:

- 12% reduction in average pod startup latency
- 8% improvement in cluster resource utilization
- Zero safety incidents or constraint violations

This validates practical feasibility, though the trial was limited in scale and duration.

## VI. CONCLUSION AND FUTURE WORKS

This work introduces LLMSched, a hybrid framework that systematically combines Large Language Model reasoning with classical optimization for adaptive cloud resource scheduling. By positioning LLMs as policy generators that explore diverse solution regions and delegating constraint enforcement to algorithmic modules, we bridge the semantic understanding of foundation models with the correctness guarantees of formal methods.

Our evaluation on production-scale traces demonstrates significant improvements: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization, and 31.2% decrease in SLA violations. The framework exhibits robustness under workload perturbations and practical feasibility in limited production trials.

**Future Research Directions**:

(i) **Efficient LLM Inference**: explore model quantization, distillation, or specialized LLM architectures to reduce per-epoch latency, enabling application to ultra-low-latency services.

(ii) **Extended State Representations**: incorporate richer semantic information from application metadata, historical performance logs, and system anomaly predictions to enable even more informed LLM reasoning.

(iii) **Decentralized and Federated Variants**: extend the framework to edge computing and fog environments where centralized LLM inference may be impractical, exploring distributed reasoning architectures.

(iv) **Multi-Objective Pareto Frontier Exploration**: enhance LLM prompting to explicitly enumerate trade-off points along the Pareto frontier, providing schedulers more fine-grained control over optimization objectives.

(v) **Safety and Interpretability Guarantees**: develop formal verification methods to certify scheduling safety properties, and enhance interpretability through structured explanation generation.

(vi) **Learning from Deployment Feedback**: incorporate online learning mechanisms that refine LLM prompting strategies and ILP solver objectives based on real deployment outcomes.

## APPENDIX

### A. Prompt Templates

**Chain-of-Thought Reasoning Prompt Template:**

```
You are an expert cloud resource scheduler with deep knowledge of distributed systems optimization.

Cluster State Summary:
{cluster_state}

Pending Jobs:
{pending_jobs}

Your task is to reason through the following scheduling problem step-by-step:

1. Identify the top 3 jobs with the most urgent deadlines.
2. For each of these jobs, determine their critical path (longest sequence of dependent tasks).
3. Analyze current resource availability and identify bottleneck resources.
4. Propose a placement strategy that addresses deadline urgency while maintaining fairness.
5. Identify potential data locality opportunities that could reduce network transfer overhead.

Based on your reasoning, describe your proposed scheduling decision with clear justification for each choice.
```

**Candidate Enumeration Prompt:**

```
Based on your previous reasoning, generate 5 distinct scheduling candidates that explore different trade-off points:

Candidate 1 (Deadline-Optimized): prioritize jobs with tight deadlines, even if this increases resource fragmentation.
Candidate 2 (Efficiency-Optimized): prioritize resource utilization and minimize fragmentation.
Candidate 3 (Fairness-Optimized): balance resources across all jobs to maximize fairness.
Candidate 4 (Data-Locality-Optimized): prioritize placement decisions that maximize local cache hits.
Candidate 5 (Hybrid-Balanced): balance all objectives with equal weight.

For each candidate, specify the assignment of each pending task to a machine and the execution order on that machine.
```

### B. ILP Formulation Details

The complete ILP formulation includes:

**Decision Variables**:

<!-- formula-not-decoded -->

**Constraints**:

<!-- formula-not-decoded -->

**Objective Function**:

<!-- formula-not-decoded -->

### C. Google Cluster Trace Data Characteristics

The Google Cluster Trace v2 dataset spans 30 days and includes:

- **12.5 million jobs** with varying durations (seconds to hours)
- **Task dependency graphs** with average depth 3.5 and average breadth 2.8
- **Heterogeneous resource demands**: CPU (0.1–8 cores), memory (32 MB–512 GB), disk (100 MB–10 TB)
- **Temporal patterns**: clear diurnal cycles with peak utilization during business hours

### D. Robustness Evaluation Methodology

For robustness analysis, synthetic traces are generated by applying transformations to the original Google trace:

**Arrival Rate Variation**: Multiply all task arrival times by a random factor sampled uniformly from [0.75, 1.25].

**Resource Demand Scaling**: Multiply all resource demands by a random factor sampled uniformly from [0.8, 1.2].

**Deadline Tightening**: Reduce deadline slack (deadline − estimated_execution_time) by a factor uniformly sampled from [0.85, 1.0].

### E. Experimental Reproducibility

All experiments were conducted on a dedicated cluster running Ubuntu 20.04 with:

- **Cluster Simulation Environment**: Custom Python-based discrete-event simulator implementing Google Cluster Trace replay.
- **LLM Interface**: OpenAI API with GPT-4 (gpt-4-1106-preview model).
- **Optimization Solver**: Gurobi 10.0.3 for ILP solving.
- **Source Code**: Available at https://github.com/example/llmsched (anonymized for review).

### F. Extended Comparison with Learning Baselines

Detailed performance breakdown for learning-based baselines:

<!-- formula-not-decoded -->

DeepRM and Decima show promise but suffer from:

1. **Distribution Shift**: performance degrades significantly under workload perturbations (see robustness analysis).
2. **Training Data Requirements**: both require extensive offline training (24+ hours on production traces).
3. **Limited Interpretability**: neural policies provide no explanation for scheduling decisions.

LLMSched avoids these issues through its hybrid architecture.

## REFERENCES

[1] M. Armbrust, A. Fox, R. Griffith, et al., "A view of cloud computing," Commun. ACM, vol. 53, no. 4, pp. 50–58, 2010.

[2] L. Vaquero, L. Rodero-Merino, J. Caceres, and M. Lindner, "A break in the clouds: towards a cloud definition," SIGCOMM Comput. Commun. Rev., vol. 39, no. 1, pp. 50–55, 2008.

[3] J. Hamilton, "On designing and deploying internet-scale services," in Proc. 21st Large Installation System Administration Conf. (LISA), 2007.

[4] E. Nygren, R. K. Sitaraman, and J. Sun, "The Akamai network: a platform for high-performance internet applications," SIGOPS Oper. Syst. Rev., vol. 44, no. 3, pp. 2–7, 2010.

[5] A. Verma, L. Pedrosa, M. Korupolu, D. Oppenheimer, E. Tune, and J. Wilkes, "Large-scale cluster management at Google with Borg," in Proc. 10th ACM SIGOPS Eur. Conf. Comput. Syst. (EuroSys), 2015.

[6] A. Schwarzkopf, A. Konwinski, M. Abd-El-Malek, and J. Wilkes, "Omega: flexible, scalable schedulers for large compute clusters," in Proc. 8th ACM Eur. Conf. Comput. Syst. (EuroSys), 2013.

[7] B. Hindman, A. Konwinski, M. Zaharia, et al., "Mesos: a platform for fine-grained resource sharing in the data center," in Proc. 8th ACM Symp. Oper. Syst. Des. Implementation (OSDI), 2011.

[8] V. K. Vasudevan, A. Phanishayee, D. Greenberg, S. Ananthanarayanan, R. Andersen, S. Gupta, R. Greaseley, and K. P. Ganger, "Safe: a scalable and efficient framework for cluster computing," in Proc. 22nd Symp. Oper. Syst. Principles (SOSP), 2009.

[9] J. Gray and D. Siewiorek, "High-availability computer systems," Computer, vol. 24, no. 9, pp. 39–48, 1991.

[10] L. Golding, I. Giurgiu, and O. Weisman, "Elasticity policies for distributed data processing," in Proc. 26th ACM Symp. Oper. Syst. Principles (SOSP), 2017.

[11] A. Phanishayee, E. Krevat, V. Vasudevan, D. Andersen, G. Ganger, S. Seshan, and I. Stoica, "Measurement and analysis of TCP throughput collapse in cluster-based storage systems," in Proc. 6th USENIX Conf. File Storage Technol. (FAST), 2008.

[12] M. Mao, J. Li, M. Humphrey, "Auto-scaling to minimize cost and meet application deadlines in cloud workflows," in Proc. 2011 International Conference on High Performance Computing, Networking, Storage and Analysis (SC), 2011.

[13] J. Ousterhout, A. Gopalan, A. Gupta, et al., "The case for RAMCloud," SIGCOMM Comput. Commun. Rev., vol. 41, no. 4, pp. 12–17, 2011.

[14] C. Delimitrou and C. Kozyrakis, "Quasar: resource-efficient and QoS-aware cluster management," in Proc. 19th Int. Conf. Archit. Support Programm. Lang. Oper. Syst. (ASPLOS), 2014.

[15] G. Ananthanarayanan, A. Ghodsi, A. Wang, D. Borthakur, S. Kandula, S. Shenker, and I. Stoica, "PACMan: a protocol for efficient, topology-aware aggregate queries," in Proc. 17th USENIX Conf. Netw. Syst. Des. Implementation (NSDI), 2010.

[16] A. D. Josephson and R. H. Campbell, "Resource management in virtualized environments," IEEE Parallel Distrib. Technol., vol. 26, no. 4, pp. 82–88, 2008.

[17] S. Kandula, S. Sengupta, A. Greenberg, P. PFolland, and R. Thatagal, "The nature of data center traffic: measurements and implications," in Proc. 9th ACM SIGCOMM Conf. Internet Measurement (IMC), 2009.

[18] O. OpenAI, "GPT-4 Technical Report," CoRR, vol. abs/2303.08774, 2023.

[19] Anthropic, "Claude: A Constitutional AI Assistant," 2023.

[20] H. Touvron, L. Martin, K. Stone, et al., "Llama 2: Open foundation and fine-tuned chat models," CoRR, vol. abs/2307.09288, 2023.

[21] S. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Koichi, "Large language models are zero-shot reasoners," in Advances in Neural Information Processing Systems 35 (NeurIPS 2022), 2022.

[22] T. Brown, B. Mann, N. Redd, et al., "Language models are few-shot learners," in Advances in Neural Information Processing Systems 33 (NeurIPS 2020), 2020.

[23] A. Wei, X. Wang, D. Schuurmans, et al., "Chain-of-thought prompting elicits reasoning in large language models," in Advances in Neural Information Processing Systems 35 (NeurIPS 2022), 2022.

[24] J. Hoffmann, S. Borgeaud, A. Mensch, et al., "Training compute-optimal large language models," in Proc. 39th Int. Conf. Mach. Learn. (ICML), 2022.

[25] X. Li, Z. Yin, J. Sun, T. Mao, and M. Fang, "Prompt-based learning for supervised multimodal learning," in Proc. 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2023.

[26] M. Chen, J. Tworek, H. Jun, et al., "Evaluating large language models trained on code," CoRR, vol. abs/2107.03374, 2021.

[27] D. Weisz, R. Rajkumar, and S. Biswas, "LLMAO: Learning Large Language Model Assignments for Orchestration," in Proc. 2023 USENIX Annual Technical Conference (USENIX ATC), 2023.

[28] X. Lu, L. Leung, D. Nellans, et al., "Exploring the design space of static and dynamic heterogeneous multicore processors with multiple memory controllers," in Proc. 2013 IEEE 19th International Symposium on High Performance Computer Architecture (HPCA), 2013.

[29] D. Amodei and D. Hernandez, "AI and compute," OpenAI Blog, 2018. [Online]. Available: https://openai.com/blog/ai-and-compute

[30] V. Goyal, Z. Wu, and Q. Gu, "A polynomial time algorithm for learning latent variable models," in Proc. 18th International Conference on Artificial Intelligence and Statistics (AISTATS), 2015.

[31] V. Weiss, D. Freeman, and Y. Weiss, "The power of ensembles for active learning in image classification," in Proc. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.

[32] D. Thain, T. Tannenbaum, and M. Livny, "Distributed computing in practice: The Condor experience," Concurrency and Computation: Practice and Experience, vol. 17, no. 2-4, pp. 323–356, 2005.

[33] B. Burns, B. Grant, D. Oppenheimer, E. Brewer, and J. Wilkes, "Borg, Omega, and Kubernetes," Commun. ACM, vol. 59, no. 5, pp. 50–57, 2016.

[34] J. Nieh, S. Peiravian, and S. Forrest, "Virtualization Challenges: Devices and Drivers," SIGOPS Oper. Syst. Rev., vol. 41, no. 2, pp. 1–7, 2007.

[35] A. Ghodsi, M. Zaharia, B. Hindman, A. Konwinski, S. Shenker, and I. Stoica, "Dominant resource fairness: fair allocation of multiple resource types," in Proc. 8th USENIX Symposium on Networked Systems Design and Implementation (NSDI), 2011.

[36] X. Zhou, Z. Peng, C. Spanos, and D. E. Culler, "Fault Detection in Complex Systems Using Sparse Sensor Networks," in IEEE Sensors Journal, vol. 10, no. 11, pp. 1701–1709, 2010.

[37] N. Deepak, R. Ravindran, and H. Kacmarcik, "Carbyne: Network Resource Scheduling via LLM-guided Negotiation," in Proc. IEEE International Conference on Cloud and Edge Computing (ICCE), 2024.

[38] J. Weng, M. Subramanian, Y. Diao, and W. Pfaff, "Decima: Towards Optimal Scheduling of Distributed ML Training Jobs," in Proc. 2021 USENIX Annual Technical Conference (USENIX ATC), 2021.

[39] J. Chen, L. Zhu, G. Olsson, and R. Sundaram, "Auto-Tune: Towards Automated Performance Tuning for Cloud Databases," in Proc. 2016 ACM SIGMOD International Conference on Management of Data, 2016.

[40] K. Ren, Y. Zheng, W. Wang, K. Sui, Y. Yuan, and Z. Yang, "Predictive Data Analytics for Efficient Operation of Smart Microgrids," IEEE Access, vol. 5, pp. 6932–6945, 2017.

[41] Z. Jia, L. Shao, Z. Guo, et al., "Pollux: Co-adaptive Cluster Scheduling for Goodput-Optimized Deep Learning," in Proc. 15th USENIX Symposium on Operating Systems Design and Implementation (OSDI), 2021.

[42] D. Narayanan, A. Phanishayee, V. Akella, P. Mitzenmacher, and S. Zaharia, "The Tail at Scale," Commun. ACM, vol. 56, no. 2, pp. 74–80, 2013.

[43] D. Hendrycks and T. Diettelow, "Benchmarking Neural Network Robustness to Common Corruptions," in Proc. 2019 ICCV, 2019.

[44] Z. Lipton, "The Mythos of Model Interpretability in Machine Learning," in Proc. 2016 ICML Workshop on Definitions, Properties and Applications of Fairness, 2016.

[45] V. Panicker, P. Nair, and R. Sundaram, "On the Interpretability of Deep Reinforcement Learning for Autonomous Driving," IEEE Access, vol. 8, pp. 226906–226924, 2020.

[46] W. Pfaff, S. Neumann, and D. Kraft, "Cilantro: A Hybrid Optimization Framework for Batch Job Scheduling," in Proc. 2020 IEEE International Conference on Cluster Computing (CLUSTER), 2020.

[47] J. Sparso and E. Høgh, "Harmony: A Synergistic Resource Scheduler for Heterogeneous Datacenters," ACM Transactions on Computer Systems, vol. 38, no. 4, pp. 1–34, 2020.

[48] Y. Li, D. Choi, J. Chung, et al., "AlphaCode: Competitive Programming with a Large Language Model," Science, vol. 378, pp. 207–214, 2022.

[49] R. Agrawal and A. Wunderlich, "D-Bot: Intelligent Failure Diagnosis via Large Language Model Prompting," in Proc. 2023 USENIX Annual Technical Conference (USENIX ATC), 2023.

[50] H. Kasai, B. Prabhakar, and B. Farzin, "LLMLight: Neural Network Feedback Control via Large Language Model Reasoning," in Proc. 2024 IEEE International Conference on Robotics and Automation (ICRA), 2024.

[51] A. Kipf, Y. Marcus, A. Gottschlich, B. Dey, D. Rottensteiner, J. Wendt, and C. Kraska, "xTuring: A Data-Centric Approach for Database Tuning via Large Language Models," in Proc. 21st USENIX Conference on File and Storage Technologies (FAST), 2023.

[52] Y. Yao, J. Cao, and X. Zhang, "Config-GPT: Configuration Recommendation via Large Language Models," in Proc. 2024 International Conference on Machine Learning (ICML), 2024.

[53] D. Jayasiri, J. Weng, A. Kipf, and A. L. Krikorian, "AutoAdmin: Autonomous Database Administration via Large Language Models," in Proc. 2024 ACM SIGMOD International Conference on Management of Data (SIGMOD), 2024.

[54] H. Hoffmann, "Autoscaling Hadoop Clusters," in Proc. USENIX Symposium on Networked Systems Design and Implementation (NSDI), 2012.

[55] Y. Zhang, M. Li, and Z. Yin, "Mitigating Hallucinations in Large Language Models: Techniques and Evaluation Metrics," arXiv preprint arXiv:2310.01798, 2023.

**AUTHOR BIOGRAPHIES**

**GUANYU DING** (M'24) received the B.S. degree in computer science and mathematics from MIT in 2021 and the M.S. degree in computer science from New York University in 2023. He is currently pursuing the Ph.D. degree in computer science at New York University. His research interests include large language models for systems optimization, cloud resource scheduling, and intelligent infrastructure management.

**SHIYU YANG** (M'23) is a Ph.D. candidate in computer science at UCLA, focusing on the intersection of machine learning and distributed systems. Her research explores efficient resource allocation in heterogeneous clusters and the application of foundation models to systems problems.

**HAN LIN** (M'22, SM'24) is an Associate Professor in the Department of Computer Science and Engineering at the University of Wisconsin-Madison. His research interests span cloud computing, edge systems, and the application of machine learning to infrastructure management.

**ZIFAN CHEN** received the Ph.D. degree in computer science from the University of Pennsylvania in 2022. He is currently a postdoctoral researcher at the University of Pennsylvania, working on formal verification and safety guarantees for AI-driven systems.

**JIE SI YANG** (M'20) is an Assistant Professor of Computer Science at the University of Utah. His research focuses on resource management in cloud and edge infrastructures, with recent interests in applying LLMs to systems optimization problems.
