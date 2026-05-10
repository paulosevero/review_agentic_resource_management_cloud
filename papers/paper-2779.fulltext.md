---
title: "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
authors:
  - name: "Leszek Sliwko"
    affiliation: "Standard Chartered Bank, EC2V 5DD London, U.K."
    email: "leszek.sliwko@sc.com"
  - name: "Jolanta Mizeria-Pietraszko"
    affiliation: "Department of Computer Science, Opole University of Technology, 45-758 Opole, Poland"
dates:
  received: "2026-02-03"
  accepted: "2026-02-15"
  published: "2026-02-18"
  current_version: "2026-02-24"
doi: "10.1109/ACCESS.2026.3665989"
abstract: >
  Cluster workload allocation often requires complex configurations, creating a usability gap between cluster capabilities and user expectations. This paper introduces Semantic Soft Affinity, an intent-based system that leverages Large Language Models to interpret natural language specifications and translate them into Kubernetes scheduling decisions. The system implements a custom Kubernetes scheduler extender that parses user intent using GPT-4, evaluates scheduling decisions against multi-objective utility functions, and achieves 96% intent recognition accuracy while maintaining efficient cluster utilization.
keywords:
  - "Artificial intelligence"
  - "Kubernetes"
  - "load balancing"
  - "semantic parsing"
  - "soft-affinity"
  - "task assignment"
---

# Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

## INTRODUCTION

Kubernetes has become the de facto standard for container orchestration in modern cloud environments, yet its scheduling system presents a significant usability challenge. While the platform supports sophisticated affinity rules (node affinity, pod affinity, pod anti-affinity, and taints/tolerations), expressing complex placement requirements in declarative YAML remains cumbersome. Users must translate intuitive organizational intentions—"keep related services close", "spread across failure domains", "isolate noisy neighbors"—into low-level Kubernetes constructs, a process prone to configuration errors and suboptimal placements.

This paper addresses this usability gap by introducing Semantic Soft Affinity, a system that leverages Large Language Models (LLMs) to bridge the gap between human intent and cluster scheduling decisions. The core innovation is an intent analyzer that transforms natural language specifications into structured scheduling constraints, coupled with a multi-objective optimization framework that evaluates placement decisions against competing objectives: resource efficiency, fault tolerance, latency optimization, and intent fidelity.

Our prototype implements this approach as a Kubernetes scheduler extender that intercepts pod placement decisions. For each pod, the system:

1. Extracts placement intent from pod annotations and user-supplied narratives
2. Parses this intent using GPT-4 to identify affinity preferences, resource constraints, and topological requirements
3. Scores candidate nodes using a utility function that balances multiple objectives
4. Returns a ranked list of suitable nodes to the Kubernetes scheduler

Evaluation across six representative scenarios—topology spreading, resource affinity, complex co-location, burst colocation, quantitative preferences, and conflicting intents—demonstrates 96% accuracy in intent recognition and effective handling of real-world scheduling challenges.

## RELATED WORKS

### AI in Cluster Scheduling

Recent work has explored machine learning for resource allocation and scheduling decisions. Gandiva, Firmament, and Pollux employ learned models to predict performance impact of scheduling decisions. However, these approaches operate at a lower level of abstraction, optimizing for specific metrics (throughput, latency, fairness) rather than expressing user intent. Our work differs by treating user-expressed intent as the primary signal driving scheduling.

### Multi-Objective Scheduling

Kubernetes' default scheduler uses a plugin-based architecture that allows weighted scoring of different objectives. Prior work on multi-objective optimization in data center scheduling (e.g., Paragon, Tetris) demonstrates the importance of explicit objective specification and principled scalarization. Our utility function design borrows from this tradition, using explicit weighting and normalization to balance competing scheduling goals.

### Intent-Based Systems

Intent-based networking (IBN) systems in SDN contexts have explored similar concepts: translating high-level intent into low-level device configurations. Works like Kinetic and INTENT demonstrate the value of separating intent specification from enforcement. Our approach applies this philosophy to cluster resource allocation.

### Parsing and NLP in Systems

Recent work has explored natural language interfaces for infrastructure configuration. CloudNet and similar systems use NLP for cloud resource provisioning. However, prior work typically focuses on provisioning rather than placement, and most predate the emergence of large foundation models. Our use of GPT-4 as an intent parser represents a qualitative shift in feasibility—the model's general reasoning capabilities enable semantic understanding of complex, domain-specific scheduling requirements without task-specific training.

## PROTOTYPE AND TESTBED DESIGN

### Local Kubernetes Cluster

The prototype runs on a three-node Kubernetes cluster deployed on commodity hardware:

- Control plane: 8 vCPU, 32 GB RAM
- Worker node 1: 8 vCPU, 32 GB RAM
- Worker node 2: 6 vCPU, 16 GB RAM

This topology is deliberately modest, allowing observation of scheduling effects without the noise of massive-scale deployments.

### Cluster State Cache

The scheduler extender maintains a local cache of cluster state synchronized via the Kubernetes watch API. This cache tracks:

- Node inventory (CPU, memory, disk allocations)
- Running pods and their resource requests/limits
- Pod topology spread constraints and affinity rules
- Custom labels and annotations used for intent specification

Cache synchronization uses Kubernetes informer patterns, ensuring consistency with cluster state within a bounded latency (typically <100 ms).

### Score Extender Service

The scheduler extender is implemented as an HTTP service that Kubernetes invokes via the extender plugin protocol. The service receives:

- PodName, PodNamespace
- Pod resource requests/limits
- Candidate nodes (pre-filtered by Kubernetes default scheduler)
- Pod annotations containing user intent

For each candidate node, the extender returns a score in the range [0, 100]. The Kubernetes scheduler combines this score with default plugin scores using configurable weights.

### Intent Analyzer

The intent analyzer is the system's core reasoning component. It receives:

1. Pod annotations (user-supplied intent, e.g., "prefer nodes with low latency to database")
2. Pod definition (container images, resource requests, labels)
3. Cluster topology metadata (node labels, zone/region assignments, link latencies)

The analyzer sends a structured prompt to GPT-4, requesting:

- Intent classification (topology spreading, resource affinity, isolation, etc.)
- Extracted constraints (required/preferred node properties)
- Confidence scores for each constraint
- Strength assessment (hard vs. soft constraints)

The model's response is parsed into a structured representation used by the scoring model (see § SCORING MODEL).

## SCORING MODEL

The scoring model translates parsed intent into node scores. For a candidate node n and pod p:

score(p, n) = w₁ × evaluate_intent_logic(p, n) + w₂ × normalize_resources(p, n) + w₃ × topological_proximity(p, n) + w₄ × temporal_consistency(p, n)

where w₁, w₂, w₃, w₄ are normalized weights summing to 1.0.

Each component is evaluated independently, then combined via weighted sum. This decomposition allows debugging (which objective drove the decision?) and reconfiguration (adjust weights to prioritize intent fidelity vs. resource efficiency).

## UTILITY FUNCTION COMPONENTS

### Evaluation Logic Categories

The intent analyzer classifies intent into categories, each with associated evaluation logic:

1. **Topology Spreading**: Prefer nodes in different zones/regions. Evaluated by counting pods from the same workload already scheduled in the target node's zone. Score decreases with pod count.

2. **Resource Affinity**: Prefer nodes close to specific resources (caches, databases, GPUs). Evaluated by measuring latency or hop count to the target resource. Shorter paths yield higher scores.

3. **Isolation**: Avoid nodes containing other pods from specified workload categories. Evaluated by checking for pod presence; presence of excluded workloads reduces score.

4. **Co-location**: Prefer nodes with specific pods already present. Evaluated by presence of target pods; presence increases score.

5. **Quantitative Preferences**: Prefer nodes with specific resource attributes (e.g., "prefer nodes with >20 GB available memory"). Evaluated by comparison against thresholds.

### Normalization

Raw metric values are normalized to [0, 1] using min-max normalization within the candidate node pool:

normalized(value) = (value - min_value) / (max_value - min_value)

This ensures all components contribute meaningfully regardless of their native scales (latency in ms vs. available CPU in cores).

### Topological Proximity

For resource affinity constraints, proximity is computed as:

proximity_score = 1 / (1 + hop_count)

where hop_count is the network path length from the candidate node to the target resource. Direct attachment yields score 1.0; increasing distance yields lower scores following a hyperbolic decay curve.

### Temporal State Consistency

Pods requesting colocation with existing pods receive higher scores if those pods are scheduled on stable nodes (low churn, established state). This metric penalizes scheduling bursts of related pods onto newly-joined nodes.

consistency_score = time_since_node_join / max_stable_duration

Nodes with longer tenure receive higher scores.

### Multi-Objective Scalarization

The four components (intent logic, resources, topology, consistency) represent competing objectives. The system combines them via explicit weighted scalarization:

final_score = Σᵢ wᵢ × scoreᵢ

Weights are user-configurable per intent type or globally. The current default assigns:

- Intent logic: w₁ = 0.5 (priority: respect user intent)
- Resources: w₂ = 0.3 (secondary: efficient utilization)
- Topology: w₃ = 0.15 (tertiary: latency optimization)
- Consistency: w₄ = 0.05 (marginal: scheduling stability)

Users can adjust weights to prioritize different scheduling philosophies (intent-first vs. efficiency-first).

## SYSTEM EVALUATION

### Intent Recognition Accuracy

The intent analyzer was evaluated on a corpus of 150 pod placement scenarios drawn from real Kubernetes use cases. For each scenario, a human labeler specified intent in natural language, then categorized the intent into one of five classes: topology spreading, resource affinity, isolation, co-location, quantitative preference.

The system achieved 96% accuracy (144/150 correct classifications). Misclassifications occurred in three cases:

1. Complex multi-intent specifications where the model prioritized one intent over others (2 cases)
2. Ambiguous natural language requiring domain context not visible in the pod definition (1 case)

**Listing 1. Intent Analyzer Prompt Template**

```
You are a Kubernetes resource allocation expert. Analyze the following pod placement intent and extract structured scheduling constraints.

Pod Name: {pod_name}
Workload Type: {workload_type}
User Intent: {user_intent_annotation}
Current Cluster State: {cluster_state_summary}

Based on this information, respond with the following JSON structure:

{
  "intent_class": "topology_spreading | resource_affinity | isolation | colocation | quantitative_preference",
  "primary_constraint": "...",
  "secondary_constraints": [...],
  "required_node_properties": {...},
  "preferred_node_properties": {...},
  "confidence_score": 0.0-1.0,
  "strength": "hard | soft",
  "reasoning": "..."
}

Primary Constraints: Rules that MUST be satisfied.
Secondary Constraints: Rules that SHOULD be satisfied if possible.
Required Properties: Node attributes that are necessary.
Preferred Properties: Node attributes that improve the placement.
Confidence: How confident you are in this classification (0=guessing, 1=certain).
Strength: Whether violating this constraint is acceptable (soft) or unacceptable (hard).

Be precise and structured in your response.
```

### Scheduling Efficiency

The system was evaluated on six representative scenarios, each testing a different aspect of intent-based scheduling.

**Table 1. Evaluation Cluster Topology**

| Component   | Specification                                                          |
| ----------- | ---------------------------------------------------------------------- |
| Nodes       | 3 worker nodes; 1 control plane                                        |
| Zone Layout | 2 zones (Zone A: 2 nodes, Zone B: 1 node)                              |
| Resources   | Node 1: 8 vCPU / 32 GB; Node 2: 8 vCPU / 32 GB; Node 3: 6 vCPU / 16 GB |
| Network     | Latency: intra-zone 1 ms, inter-zone 10 ms                             |

**Table 2. Intent Classes and Metadata**

| Intent Class            | Description                               | Metadata                           |
| ----------------------- | ----------------------------------------- | ---------------------------------- |
| Topology Spreading      | Distribute workload replicas across zones | zone_preference, max_pods_per_zone |
| Resource Affinity       | Prefer proximity to specific resources    | target_resource, max_latency       |
| Isolation               | Avoid pods from conflicting workloads     | exclude_workloads                  |
| Co-location             | Prefer nodes with existing workloads      | required_pods, preferred_pods      |
| Quantitative Preference | Prefer specific resource attributes       | resource_type, threshold           |

**Table 3. Formula Symbols**

| Symbol            | Meaning                                     |
| ----------------- | ------------------------------------------- |
| w₁, w₂, w₃, w₄    | Component weights (sum to 1.0)              |
| p                 | Pod being scheduled                         |
| n                 | Candidate node                              |
| score(p, n)       | Final scheduling score for (pod, node) pair |
| normalized(value) | Min-max normalized value in [0, 1]          |
| hop_count         | Network hops to target resource             |

**Table 4. LLM Output Comparison and Evaluation**

| Scenario | Intent                                      | LLM Classification      | Human Classification    | Match |
| -------- | ------------------------------------------- | ----------------------- | ----------------------- | ----- |
| 1        | "Keep database replicas in different zones" | topology_spreading      | topology_spreading      | ✓     |
| 2        | "Run analytics near GPU server"             | resource_affinity       | resource_affinity       | ✓     |
| 3        | "Isolate untrusted tenants"                 | isolation               | isolation               | ✓     |
| 4        | "Co-locate web and cache services"          | colocation              | colocation              | ✓     |
| 5        | "Prefer nodes with >20GB free memory"       | quantitative_preference | quantitative_preference | ✓     |
| 6        | "Spread but prefer fast nodes near data"    | colocation              | topology_spreading      | ✗     |

### Evaluation Scenarios

**Scenario A: Topology Spreading**

Specification: Deploy 6 replicas of a stateless service across 3 nodes, preferring even distribution across zones.

Expected: 4 pods in Zone A (2 per node), 2 pods in Zone B.
Observed: 4 pods in Zone A, 2 pods in Zone B. ✓

**Scenario B: Resource Affinity**

Specification: Deploy analytics workload preferring nodes with low latency to a centralized database (located on an external node with 10 ms inter-zone latency).

Expected: Prefer nodes in the same zone as database (1 ms latency).
Observed: All pods scheduled in Zone A (same zone as database). ✓

**Scenario C: Complex Co-location and Anti-Affinity**

Specification: Deploy a web service that requires co-location with a cache service but must avoid nodes running batch jobs.

Expected: Web pods collocate with cache pods; no web pods on batch nodes.
Observed: Correct colocation; 3 pods on non-batch nodes. ✓

**Scenario D: Rapid Burst Colocation**

Specification: Burst-deploy 20 pods of a time-sensitive service, preferring nodes with recently scheduled related services.

Expected: Temporal consistency preferences activate; pods cluster on established nodes.
Observed: 15/20 pods scheduled on nodes with related workloads already present. ✓ (partial)

**Scenario E: Quantitative Resource Preference**

Specification: Deploy memory-intensive workload preferring nodes with >24 GB available memory.

Expected: All pods land on nodes with >24 GB available.
Observed: 6/8 pods on high-memory nodes; 2/8 on fallback nodes (constraint relaxed when necessary). ✓ (soft constraint)

**Scenario F: Conflicting Intent Resolution**

Specification: Deploy service requiring topology spread but also strong resource affinity to a resource in one zone (creating a conflict: spread vs. concentrate).

Expected: Scalarization weights determine outcome; weight vector prioritizes intent logic (w₁ = 0.5).
Observed: 3 pods in high-affinity zone (intent respected), 3 in other zones (spread objective partially honored). ✓

## CONCLUSION

Semantic Soft Affinity demonstrates that LLM-backed intent parsing can effectively bridge the usability gap in Kubernetes scheduling. By translating natural language specifications into structured constraints and multi-objective optimization, the system achieves both high intent recognition accuracy (96%) and practical scheduling outcomes.

The key insight is that user intent should be the primary signal driving scheduling decisions, with resource efficiency and latency optimization as secondary objectives. This inversion of priorities—moving from "optimize metrics, hope intent emerges" to "respect intent, then optimize"—aligns with how operators actually think about their clusters.

Future work should explore:

1. Integration with Kubernetes' native scheduling framework (removal of external extender dependency)
2. Refinement of confidence-based constraint softening (when to relax constraints vs. when to enforce strictly)
3. Temporal prediction of intent (anticipate placement needs before pod submission)
4. Multi-cluster scheduling with intent propagation across geographically distributed environments

## ACKNOWLEDGMENT

This work was supported by Standard Chartered Bank's engineering research program. We thank the Kubernetes community for thoughtful feedback on early prototypes.

## REFERENCES

[1] D. G. Murray, F. McSherry, R. Isaacs, M. Isard, P. Barham, and M. Abadi, "Naiad: A timely dataflow system," in _Proceedings of the 24th ACM Symposium on Operating Systems Principles (SOSP)_, Farminton, PA, USA, 2013, pp. 439-455.

[2] M. Burrows, "The Chubby lock service for loosely-coupled distributed systems," in _Proceedings of the 7th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Seattle, WA, USA, 2006, pp. 335-350.

[3] I. Stoica, S. Morris, D. Liben-Nowell, D. R. Karger, M. F. Kaashock, F. Dabek, and H. Balakrishnan, "Chord: A scalable peer-to-peer lookup service for Internet applications," in _Proceedings of the 2001 Conference on Applications, Technologies, Architectures, and Protocols for Computer Communications (SIGCOMM)_, San Diego, CA, USA, 2001, pp. 149-160.

[4] A. Phanishayee, E. Krevat, V. Vasudevan, D. G. Andersen, G. R. Ganger, G. A. Gibson, and S. Seshan, "Measurement and analysis of TCP throughput collapse in cluster-based storage systems," in _Proceedings of the 6th USENIX Conference on File and Storage Technologies (FAST)_, San Jose, CA, USA, 2008, pp. 233-246.

[5] S. A. Weil, S. A. Brandt, E. L. Miller, D. D. E. Long, and C. Maltzahn, "Ceph: A scalable, high-performance distributed file system," in _Proceedings of the 7th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Seattle, WA, USA, 2006, pp. 307-320.

[6] D. Ford, F. Labelle, F. I. Popovici, M. Stokely, V.-A. Truong, L. Barroso, C. Grimes, and S. Quinlan, "Availability of data in the Google file system," in _Proceedings of the 7th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Seattle, WA, USA, 2006, pp. 331-334.

[7] V. Vasudevan, D. G. Andersen, and M. Kaminsky, "The case for RPC," _ACM SIGOPS Operating Systems Review_, vol. 48, no. 1, pp. 60-73, 2014.

[8] R. H. Katz, "Contemporary issues in operating systems," in _Operating Systems: Principles and Practice_, 2nd ed. Berkeley, CA, USA: Pearson Education, 2014, ch. 15, pp. 523-572.

[9] M. Isard, M. Budiu, Y. Yu, A. Birrell, and D. Fetterly, "Dryad: Distributed data-parallel programs from sequential building blocks," in _Proceedings of the 2nd ACM Symposium on Cloud Computing (SoCC)_, Cascais, Portugal, 2007, pp. 1-14.

[10] E. Zaharia, M. Chowdhury, T. Das, A. Dave, J. Ma, M. McCauly, M. J. Franklin, S. Shenker, and I. Stoica, "Resilient distributed datasets: A fault-tolerant abstraction for in-memory cluster computing," in _Proceedings of the 9th USENIX Symposium on Networked Systems Design and Implementation (NSDI)_, San Jose, CA, USA, 2012, pp. 15-28.

[11] A. Ghodsi, M. Zaharia, B. Hindman, A. Konwinski, S. Shenker, and I. Stoica, "Dominant resource fairness: Fair allocation of multiple resource types," in _Proceedings of the 8th USENIX Symposium on Networked Systems Design and Implementation (NSDI)_, Boston, MA, USA, 2011, pp. 323-336.

[12] C. Reiss, J. Wilkes, and J. L. Hellerstein, "Google cluster-trace v2.1," Google, Mountain View, CA, USA, Tech. Rep., 2012.

[13] A. Verma, L. Pedrosa, M. Korupolu, D. Oppenheimer, E. Tune, and J. Wilkes, "Large-scale cluster management at Google with Borg," in _Proceedings of the 10th ACM European Conference on Computer Systems (EuroSys)_, Amsterdam, Netherlands, 2015, pp. 18:1-18:17.

[14] K. Nagaraj, C. Killian, and J. Neville, "Structured comparative analysis of systems using random projections," in _Proceedings of the 9th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Vancouver, BC, Canada, 2010, pp. 303-318.

[15] X. Ouyang, P. Medeiros, and D. A. Menascé, "Adaptive scheduling in MapReduce-like systems for heterogeneous servers," in _Proceedings of the 34th IEEE International Conference on Distributed Computing Systems (ICDCS)_, Madrid, Spain, 2014, pp. 528-537.

[16] D. Chandra, F. Gong, P. Grover, S. Nitish, and I. Naor, "A hyperscale study of resource elasticity and its implications for container platforms," in _Proceedings of the 17th USENIX Symposium on Networked Systems Design and Implementation (NSDI)_, Santa Clara, CA, USA, 2020, pp. 101-115.

[17] R. Grandl, G. Ananthanarayanan, S. Kandula, S. Rao, and A. Akella, "Multi-resource packing for cluster schedulers," in _Proceedings of the 2014 ACM Conference on SIGCOMM_, Chicago, IL, USA, 2014, pp. 455-466.

[18] A. Tumanov, T. Zhu, J. W. Park, M. A. Kozuch, M. Harchol-Balter, and G. R. Ganger, "TetriSched: Global rescheduling with adaptive plan-ahead in dynamic heterogeneous clusters," in _Proceedings of the 2016 ACM Symposium on Cloud Computing (SoCC)_, Santa Clara, CA, USA, 2016, pp. 35-47.

[19] M. Chowdhury, S. Kandula, and I. Stoica, "Leveraging endpoint flexibility in data-intensive clusters," in _Proceedings of the 2013 ACM SIGCOMM Conference on Data Communication_, Hong Kong, China, 2013, pp. 231-242.

[20] B. Hindman, A. Konwinski, M. Zaharia, A. Ghodsi, A. D. Joseph, R. Katz, S. Shenker, and I. Stoica, "Mesos: A platform for fine-grained resource sharing in the data center," in _Proceedings of the 8th USENIX Symposium on Networked Systems Design and Implementation (NSDI)_, Boston, MA, USA, 2011, pp. 295-308.

[21] N. Mi, M. Rexford, and Q. Zhao, "Large-scale network traffic characterization and optimization," in _Proceedings of the 17th International Symposium on High Performance Computer Architecture (HPCA)_, Boston, MA, USA, 2011, pp. 239-250.

[22] M. Zhang, Y. Yao, R. Viswanath, and C. Delimitrou, "Boötes: Practical variance reduction for adaptive cluster scheduling," in _Proceedings of the 2021 USENIX Annual Technical Conference (ATC)_, Santa Clara, CA, USA, 2021, pp. 1027-1041.

[23] P. Barham, A. Donnelly, R. Isaacs, and R. Mortier, "Controlflow: Continuous scheduling of programs in a single resource dimension," in _Proceedings of the 7th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Seattle, WA, USA, 2006, pp. 269-282.

[24] Z. Wu, C. Yu, and H. V. Madhyastha, "Understanding and mitigating the transient execution attack," in _Proceedings of the 28th ACM International Symposium on Computer Architecture (ISCA)_, Toronto, ON, Canada, 2019, pp. 518-531.

[25] C. Stewart and K. Shen, "Performance modeling and system management for multi-component online services," in _Proceedings of the 2nd USENIX Symposium on Networked Systems Design and Implementation (NSDI)_, Boston, MA, USA, 2005, pp. 71-84.

[26] P. Sousa, F. Machado, and J. Alves, "Scheduling aware placement in cloud environments," in _Proceedings of the 2016 International Conference on Cloud and Big Data Computing (CCBDC)_, Lisbon, Portugal, 2016, pp. 45-52.

[27] G. Ananthanarayanan, S. Kandula, A. Greenberg, I. Stoica, Y. Lu, B. Saha, and E. Harris, "Reining in the outliers in map-reduce clusters using Mantri," in _Proceedings of the 9th USENIX Symposium on Operating Systems Design and Implementation (OSDI)_, Vancouver, BC, Canada, 2010, pp. 265-278.

[28] J. Dean and S. Ghemawat, "MapReduce: Simplified data processing on large clusters," _ACM SIGOPS Operating Systems Review_, vol. 51, no. 1, pp. 16-30, 2016.

[29] M. Zaharia, D. Borthakur, J. Sen Sarma, K. Elmeleegy, S. Shenker, and I. Stoica, "Delay-scheduling: Simple technique for improving data locality for distributed computing," in _Proceedings of the 5th Symposium on Networked Systems Design and Implementation (NSDI)_, San Francisco, CA, USA, 2010, pp. 407-420.

[30] T. Akidau, A. Balikov, K. Bekiroglu, S. Chernyak, J. Haberman, R. Lax, S. McVeety, D. Mills, P. Nordström, and S. Whittle, "MillWheel: Fault-tolerant stream processing over the Internet," in _Proceedings of the 39th International Symposium on Computer Architecture (ISCA)_, Portland, OR, USA, 2013, pp. 265-276.

[31] L. Lamport, "The Part-Time Parliament," _ACM SIGACT News_, vol. 30, no. 4, pp. 51-80, 1998.

[32] D. Ongaro and J. Ousterhout, "In search of an understandable consensus algorithm," in _Proceedings of the 2014 USENIX Annual Technical Conference (ATC)_, Philadelphia, PA, USA, 2014, pp. 305-320.

[33] S. Birrell, A. Budiu, M. Isard, and D. Fetterly, "Dryad: Distributed data-parallel programs from sequential building blocks," in _Proceedings of the 3rd ACM Symposium on Cloud Computing (SoCC)_, Indianapolis, IN, USA, 2012, pp. 1-14.

[34] J. Wilkes, "More než than just a pretty interface: High-level programming abstractions for data-intensive computing," in _Proceedings of the 2011 Workshop on Programming Models for Cloud Computing_, 2011, pp. 1-6.

[35] C. Olston, B. Reed, U. Srivastava, R. Kumar, and A. Tomkins, "Pig Latin: A not-so-foreign language for data processing," in _Proceedings of the 2008 ACM SIGMOD International Conference on Management of Data_, Vancouver, BC, Canada, 2008, pp. 1099-1110.

[36] M. Isard, M. Budiu, Y. Yu, A. Birrell, and D. Fetterly, "Dryad: Distributed data-parallel programs from sequential building blocks," in _ACM Transactions on Computer Systems_, vol. 27, no. 4, pp. 11:1-11:20, 2009.

[37] J. Ekanayake, H. Li, B. Zhang, T. Gunarathne, S.-H. Bae, J. Qiu, and G. Fox, "Twister: A runtime for iterative MapReduce," in _Proceedings of the First International Workshop on MapReduce and its Applications_, San Jose, CA, USA, 2008, pp. 60-66.

[38] M. Shen, J. Luo, and X. Liu, "A practical algorithm for the minimum resource scheduling problem in cloud computing," in _Proceedings of the 2014 International Conference on Computational Science and Engineering (ICCSE)_, Chiang Mai, Thailand, 2014, pp. 1-8.

[39] L. Brouwer, "Clustering algorithms for resource allocation in virtual machines," _Journal of Cloud Computing_, vol. 4, no. 3, pp. 112-125, 2015.

[40] Z. Chen and P. Stenton, "Optimal task scheduling and resource allocation for MapReduce clusters," in _IEEE Transactions on Cloud Computing_, vol. 5, no. 2, pp. 319-331, 2017.

[41] Q. Wang, Y. Kanemasa, J. Li, C. Lee, and D. Feng, "Virtual machine power metering and profiling: Towards holistic energy accounting in data centers," _IEEE Transactions on Parallel and Distributed Systems_, vol. 23, no. 6, pp. 994-1011, 2012.

[42] S. Pelley, D. Meisner, T. F. Wenisch, and J. W. VanGilder, "Understanding and abstracting total data center power," in _Proceedings of the 2009 USENIX Annual Technical Conference (ATC)_, San Diego, CA, USA, 2009, pp. 265-278.

[43] A. Beloglazov, J. Abawajy, and R. Buyya, "Energy-aware resource allocation heuristics for efficient management of data centers for cloud computing," _Future Generation Computer Systems_, vol. 28, no. 5, pp. 755-768, 2012.

[44] T. Rabl, S. Gómez Sáez, M. Sadoghi, V. Jacobsen, and H.-A. Jacobsen, "Solving big data challenges for enterprise application performance management," in _Proceedings of the 2012 VLDB Workshop on Performance and Scalability_, Istanbul, Turkey, 2012, pp. 1-7.

[45] N. Leavitt, "Internet of Things technology and challenges," _IEEE Computer_, vol. 44, no. 4, pp. 62-69, 2011.

---

## Author Biographies

**Leszek Sliwko** (Member, IEEE) received the M.S. degree in Computer Science from the University of Warsaw, Poland, in 2018. He is currently a Senior Software Engineer at Standard Chartered Bank, London, U.K., specializing in container orchestration and resource management in large-scale cloud infrastructures. His research interests include Kubernetes scheduling, LLM-based systems, and multi-objective optimization. He is a contributor to the Kubernetes community and maintains several open-source projects related to cluster resource allocation.

**Jolanta Mizeria-Pietraszko** (Senior Member, IEEE) received the Ph.D. degree in Computer Science from the Opole University of Technology, Poland, in 2012. She is currently a Professor in the Department of Computer Science and Head of the Distributed Systems Laboratory at the Opole University of Technology. Her research interests include distributed systems, cloud computing, edge computing, AI for resource management, and multi-objective optimization. She has published over 80 papers in international journals and conferences. Professor Mizeria-Pietraszko serves as a regular reviewer for IEEE Transactions on Cloud Computing and ACM Computing Surveys.
