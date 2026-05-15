<!--
Per-review CLAUDE.md migrated from v2 (legacy/CLAUDE.md) to plugin v3.2.0
schema. The original is preserved verbatim under legacy/. This file is the
authoritative protocol for this review going forward; agents read it at the
start of every command.
-->

# Rapid Review — Protocol

This file is the authoritative protocol for this review. It declares the theme, research questions, search string, inclusion/exclusion criteria, per-stage models, classifier-config paths, accumulated decision anchors, and taxonomy. Every agent in this plugin reads it before acting. It is read-only at runtime; updates happen only through checkpoint commits.

---

## 0. Meta

- **Topic:** `Agentic AI (LLM-based agents) for resource management decisions in Cloud, Edge, Fog, and the Edge-Cloud Continuum`
- **Repo:** `/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud`
- **Created:** `2026-04-25`
- **Migrated to v3.2.0:** `2026-05-09`
- **Current stage:** `06-full-text-screening (locked); next: 07-taxonomy-development`

## 1. Locks (machine-readable)

Agents use this block to decide whether a given stage can run. A stage can only start when its predecessors are all `locked`.

```yaml
locks:
  00-new-review: locked # pending | locked
  01-research-questions: locked
  02-search-string: locked
  03-parse-references-metadata: locked
  04-title-screening: locked
  05-abstract-screening: locked
  06-full-text-screening: locked
  07-taxonomy-development: iterating # phase 07a' deductive draft (iteration 1)
  08-analysis: pending
  09-report: pending
```

## 2. Theme

Resource management in cloud, edge, fog, and continuum infrastructures has historically relied on heuristics, control-theoretic policies, mixed-integer formulations, and reinforcement learning agents bound to narrow action spaces. The recent emergence of agentic AI — LLM-backed systems that perceive, reason, plan, invoke tools, and act over multi-step horizons — opens a qualitatively different design space: scheduling, placement, scaling, admission control, energy management, and fault response can now be expressed as goal-conditioned dialog with an autonomous agent rather than as fixed decision rules. This review synthesizes how that shift is being operationalized across the cloud-edge continuum, what classes of decisions are being delegated to such agents, what reasoning machinery and grounding mechanisms underlie those decisions, and how the resulting systems are evaluated.

The review covers agentic AI systems whose autonomous loop drives resource management decisions, regardless of whether the underlying infrastructure is centralized cloud, edge, fog, or a continuum. Out of scope: pre-LLM RL/MARL agents that lack the agentic loop (perception → reasoning → tool use → action over multi-step horizons), classical optimization or heuristic schedulers without an LLM-backed reasoning component, and works where the LLM is used purely as an offline analytics or recommendation tool detached from the control loop.

**Scope decisions accepted at Level 1:**

- **Boundary A — Agentic loop required.** The system must implement the autonomous perception–reasoning–tool-use–action loop. RL/MARL papers without an LLM-driven reasoning step are excluded.
- **Boundary B — Resource management as the closed loop.** The agent's actions must affect resource management decisions (scheduling, placement, scaling, admission, energy, fault response, etc.). LLMs used only for monitoring, log summarization, or offline recommendation are excluded.
- **Boundary C — Infrastructure scope.** Cloud, edge, fog, and the edge-cloud continuum are all in scope. HPC clusters, embedded single-device systems, and pure end-user device contexts are out of scope unless they appear as edge nodes in a continuum architecture.
- **Safety, governance, and accountability** are not a separate RQ; they are distributed across sub-RQs under RQ1 (guardrails design), RQ4 (safety/governance evaluation metrics), and RQ5 (open governance gaps). This decision is logged at Level 2.

**Screening doctrine.** When in doubt at title or abstract stages, include. A false positive costs one extra read at the next stage; a false negative loses a relevant paper forever. This asymmetry is operationalized via the per-stage thresholds in `protocols/screening.yaml.stage_allocation` (permissive early, strict late) and the abstract-stage `insufficient_evidence` rule in `agents/_screening-protocol.md §5.2`. The adversarial sub-agent architecture (two opposed sub-agents + deterministic consolidator + human override in the spreadsheet) is specified in `agents/_screening-protocol.md`.

## 3. Research Questions

`<Hierarchical list, filled by /01-research-questions. The authoritative machine-readable form lives in protocols/screening.yaml; this section is its prose mirror. Each RQ has 1–3 sub-RQs covering dimensions of the same phenomenon (Padrão 1 — thematic decomposition).>`

- **RQ1:** How are agentic AI systems architected for resource management in cloud, edge, fog, and continuum infrastructures?
  - **RQ1.1:** Architectural patterns of the perceive-reason-act loop (single-agent vs multi-agent vs hierarchical; ReAct/Plan-and-Execute/Reflexion).
  - **RQ1.2:** Coupling to infrastructure via tools/APIs/MCP (tool surface, action grammar, integration with Kubernetes/orchestrators).
  - **RQ1.3:** Safety and guardrail mechanisms (HITL, action validators, sandboxing, policy gates, rollback).
- **RQ2:** Which classes of resource management decisions are delegated to agentic AI systems, and under what operational conditions?
  - **RQ2.1:** Classes of resource management decisions delegated.
  - **RQ2.2:** Operational conditions and autonomy level (advisory/supervised/autonomous).
- **RQ3:** What reasoning processes and grounding mechanisms do agentic AI systems employ to translate observed system state into resource management actions?
  - **RQ3.1:** Reasoning processes (CoT, ToT, ReAct, planning + reflection, debate, self-consistency).
  - **RQ3.2:** Grounding mechanisms (telemetry, RAG over runbooks/docs, episodic memory, vector DBs, knowledge graphs).
  - **RQ3.3:** Domain knowledge incorporation (fine-tuning, structured prompting, few-shot, infrastructure ontologies).
- **RQ4:** How is the behavior of agentic AI systems for resource management evaluated?
  - **RQ4.1:** Evaluation methodologies and environments (simulation, real testbed, production, synthetic benchmarks, real traces).
  - **RQ4.2:** Resource-management performance metrics (latency, cost, energy, SLA, utilization, throughput).
  - **RQ4.3:** Agent/inference overhead metrics (token usage, inference latency, monetary cost per decision, model size/footprint, agent-loop throughput).
  - **RQ4.4:** Safety and governance metrics (rate of unsafe/invalid actions, frequency of human intervention, audit coverage, policy compliance).
- **RQ5:** What open challenges, unresolved tensions, and promising future directions emerge from the synthesis of the included literature?
  - **RQ5.1:** Unresolved methodological and technical tensions (inference cost vs. decision latency, hallucination in critical environments, transferability across infrastructures).
  - **RQ5.2:** Governance, accountability, and auditability gaps (decision traceability, responsibility attribution, regulatory requirements, explainability).

## 4. Search String

**Base Boolean string:**

```
(
  "agentic AI" OR "AgenticAI" OR "agentic system" OR "agentic systems" OR
  "agentic workflow" OR "agentic workflows" OR "agentic framework" OR
  "agentic approach" OR "agentic method" OR "agentic LLM" OR "agentic LLMs" OR
  "AI agent" OR "AI agents" OR "AI-powered agent" OR "AI-powered agents" OR
  "LLM agent" OR "LLM agents" OR "LLM-agent" OR "LLM-agents" OR
  "LLM-driven agent" OR "LLM-driven agents" OR "LLM-driven" OR
  "LLM-enabled agent" OR "LLM-enabled agents" OR "LLM-enabled" OR
  "LLM-powered agent" OR "LLM-powered agents" OR "LLM-powered" OR
  "LLM-based agent" OR "LLM-based agents" OR "LLM-based" OR
  "agent-based LLM" OR "LLM" OR "LLMs" OR
  "large language model" OR "large language models" OR
  "language model" OR "language models" OR
  "language agent" OR "language agents" OR
  "foundation model" OR "foundation models" OR
  "foundational model" OR "foundational models" OR
  "foundation model agent" OR "foundation model agents" OR
  "foundational model agent" OR "foundational model agents" OR
  "generative AI" OR "generative artificial intelligence" OR "GenAI" OR
  "generative AI agent" OR "generative agent" OR "GenAI agent" OR
  "autonomous agent" OR "autonomous agents" OR "autonomous AI" OR
  "multi-agent system" OR "multi-agent systems" OR "multi agent" OR "multiagent" OR
  "intelligent agent" OR "intelligent agents" OR
  "cognitive agent" OR "reasoning agent" OR "reasoning agents" OR
  "artificial intelligence agent" OR "artificial intelligence agents"
)
AND
(
  "resource management" OR "resource allocation" OR "resource scheduling" OR
  "resource optimization" OR "resource provisioning" OR "resource orchestration" OR
  "resource control" OR "resource governance" OR
  "workload scheduling" OR "workload orchestration" OR
  "task scheduling" OR "job scheduling" OR
  "service placement" OR "container placement" OR "placement" OR "placing" OR
  "migration" OR "migrating" OR "relocation" OR "relocating" OR
  "scheduling" OR "allocation" OR "allocating" OR "provisioning" OR
  "orchestration" OR "orchestrating" OR "optimization" OR "optimizing" OR
  "scaling" OR "autoscaling" OR "auto-scaling" OR
  "load balancing" OR "routing" OR "slicing" OR "network slicing" OR
  "admission control" OR "energy management" OR
  "fault tolerance" OR "capacity planning" OR
  "infrastructure orchestration" OR "infrastructure management"
)
AND
(
  "cloud computing" OR "data center" OR "data centers" OR
  "data centre" OR "data centres" OR
  "datacenter" OR "datacenters" OR "datacentre" OR "datacentres" OR
  "edge computing" OR "fog computing" OR
  "edge-cloud continuum" OR "cloud-edge continuum" OR
  "mobile edge computing" OR "MEC" OR
  "serverless" OR "FaaS" OR "function as a service" OR
  "Kubernetes" OR "microservices" OR
  "Infrastructure as a Service" OR "IaaS" OR
  "Platform as a Service" OR "PaaS" OR
  "Software as a Service" OR "SaaS"
)
```

**Target databases:** Scopus only. Web of Science, IEEE Xplore, and ACM Digital Library were explicitly excluded by the user.

**Search executed on:** `2026-04-26`

**Notes on per-database adaptation:**

- **Scopus** — field: `TITLE-ABS-KEY`; temporal filter: `PUBYEAR > 2016` (pre-decided at stage 01). Full Scopus-ready query:

```
TITLE-ABS-KEY(
  (
    "agentic AI" OR "AgenticAI" OR "agentic system" OR "agentic systems" OR
    "agentic workflow" OR "agentic workflows" OR "agentic framework" OR
    "agentic approach" OR "agentic method" OR "agentic LLM" OR "agentic LLMs" OR
    "AI agent" OR "AI agents" OR "AI-powered agent" OR "AI-powered agents" OR
    "LLM agent" OR "LLM agents" OR "LLM-agent" OR "LLM-agents" OR
    "LLM-driven agent" OR "LLM-driven agents" OR "LLM-driven" OR
    "LLM-enabled agent" OR "LLM-enabled agents" OR "LLM-enabled" OR
    "LLM-powered agent" OR "LLM-powered agents" OR "LLM-powered" OR
    "LLM-based agent" OR "LLM-based agents" OR "LLM-based" OR
    "agent-based LLM" OR "LLM" OR "LLMs" OR
    "large language model" OR "large language models" OR
    "language model" OR "language models" OR
    "language agent" OR "language agents" OR
    "foundation model" OR "foundation models" OR
    "foundational model" OR "foundational models" OR
    "foundation model agent" OR "foundation model agents" OR
    "foundational model agent" OR "foundational model agents" OR
    "generative AI" OR "generative artificial intelligence" OR "GenAI" OR
    "generative AI agent" OR "generative agent" OR "GenAI agent" OR
    "autonomous agent" OR "autonomous agents" OR "autonomous AI" OR
    "multi-agent system" OR "multi-agent systems" OR "multi agent" OR "multiagent" OR
    "intelligent agent" OR "intelligent agents" OR
    "cognitive agent" OR "reasoning agent" OR "reasoning agents" OR
    "artificial intelligence agent" OR "artificial intelligence agents"
  )
  AND
  (
    "resource management" OR "resource allocation" OR "resource scheduling" OR
    "resource optimization" OR "resource provisioning" OR "resource orchestration" OR
    "resource control" OR "resource governance" OR
    "workload scheduling" OR "workload orchestration" OR
    "task scheduling" OR "job scheduling" OR
    "service placement" OR "container placement" OR "placement" OR "placing" OR
    "migration" OR "migrating" OR "relocation" OR "relocating" OR
    "scheduling" OR "allocation" OR "allocating" OR "provisioning" OR
    "orchestration" OR "orchestrating" OR "optimization" OR "optimizing" OR
    "scaling" OR "autoscaling" OR "auto-scaling" OR
    "load balancing" OR "routing" OR "slicing" OR "network slicing" OR
    "admission control" OR "energy management" OR
    "fault tolerance" OR "capacity planning" OR
    "infrastructure orchestration" OR "infrastructure management"
  )
  AND
  (
    "cloud computing" OR "data center" OR "data centers" OR
    "data centre" OR "data centres" OR
    "datacenter" OR "datacenters" OR "datacentre" OR "datacentres" OR
    "edge computing" OR "fog computing" OR
    "edge-cloud continuum" OR "cloud-edge continuum" OR
    "mobile edge computing" OR "MEC" OR
    "serverless" OR "FaaS" OR "function as a service" OR
    "Kubernetes" OR "microservices" OR
    "Infrastructure as a Service" OR "IaaS" OR
    "Platform as a Service" OR "PaaS" OR
    "Software as a Service" OR "SaaS"
  )
) AND PUBYEAR > 2016
```

**Pre-decided database filters (locked at stage 01):**

- **Scopus** — apply temporal-window filter `PUBYEAR > 2016` (Transformer-era boundary; pre-LLM agentic loops out of scope). The full Boolean query above is the Scopus-specific form with this filter appended.

## 5. Inclusion Criteria (typed)

Criteria are typed (`thematic_rq` / `thematic_sub_rq` / `qa`) and weighted, declared once at stage 01, and locked alongside the rest of `protocols/screening.yaml`. This section is the readable mirror; the authoritative definition lives in the YAML. Each criterion is anchored to one or more RQ or sub-RQ ids via `refs`. When the protocol is reopened (`[01] checkpoint: revisit criteria`), this section is regenerated from the updated YAML.

Hard gates (peer-review, language, year, indexing) are not encoded as criteria in v2. Year is enforced via a database-side filter (see §4); language, document type, and source quality are enforced via the manual-review rules block below.

### `thematic_rq` (ternary at stage 04 — title screening; weight: null)

- **C1 — [T1]** — refs: `[RQ1, RQ2, RQ3, RQ4, RQ5]` — The title indicates an agentic AI system or LLM-based decision-making mechanism (agents, agentic, LLM, large language model, autonomous AI, intelligent control, conversational AI, foundation model, or related terms).
- **C2 — [T2]** — refs: `[RQ2]` — The title mentions a resource management decision (resource management, placement, scheduling, allocation, autoscaling, migration, routing, slicing, orchestration, capacity planning, governance, infrastructure management, or related).
- **C3 — [T3]** — refs: `[RQ1, RQ2, RQ3, RQ4, RQ5]` — The title mentions cloud, edge, fog, continuum, serverless, FaaS, Kubernetes, MEC, datacenter, or related distributed-infrastructure terms.

### `thematic_sub_rq` (weighted, applies at stages 05 and 06)

- **C4 — [S1]** — refs: `[RQ1.1]` — weight: 0.7 — Architectural pattern of the perceive-reason-act loop (single-agent vs multi-agent vs hierarchical; ReAct, Plan-and-Execute, Reflexion, or variants).
- **C5 — [S2]** — refs: `[RQ1.2]` — weight: 0.7 — Coupling to infrastructure (tools, APIs, MCP, integration with Kubernetes/orchestrators) and action grammar.
- **C6 — [S3]** — refs: `[RQ1.3]` — weight: 0.7 — Safety/guardrail mechanisms (HITL, action validators, sandboxing, policy gates, rollback) or explicit justification of their absence.
- **C7 — [S4]** — refs: `[RQ2.1]` — weight: 0.7 — Classes of resource management decisions delegated to the agent.
- **C8 — [S5]** — refs: `[RQ2.2]` — weight: 0.7 — Operational conditions and level of autonomy (advisory, supervised, autonomous).
- **C9 — [S6]** — refs: `[RQ3.1]` — weight: 0.7 — Reasoning process employed (CoT, ToT, ReAct, planning + reflection, debate, self-consistency).
- **C10 — [S7]** — refs: `[RQ3.2]` — weight: 0.7 — Grounding mechanisms (telemetry, RAG, episodic memory, vector DBs, knowledge graphs).
- **C11 — [S8]** — refs: `[RQ3.3]` — weight: 0.7 — Domain knowledge incorporation (fine-tuning, structured prompting, few-shot, infrastructure ontologies).
- **C12 — [S9]** — refs: `[RQ4.1]` — weight: 0.7 — Evaluation methodology and experimental environment.
- **C13 — [S10]** — refs: `[RQ4.2]` — weight: 0.7 — Resource-management performance metrics.
- **C14 — [S11]** — refs: `[RQ4.3]` — weight: 0.7 — Agent/inference overhead metrics.
- **C15 — [S12]** — refs: `[RQ4.4]` — weight: 0.7 — Safety/governance metrics.
- **C16 — [S13]** — refs: `[RQ5.1]` — weight: 0.7 — Unresolved methodological/technical tensions.
- **C17 — [S14]** — refs: `[RQ5.2]` — weight: 0.7 — Governance, accountability, or auditability gaps.

### `qa` (weighted, applies at stage 06 — full-text screening)

- **C18 — [Q1]** — refs: `[RQ1, RQ2]` — weight: 0.6 — Agentic-AI-for-resource-management design described with sufficient detail to understand how the system works.
- **C19 — [Q2]** — refs: `[RQ4]` — weight: 0.4 — Evaluation of the proposed agentic AI system is presented.

### Stage allocation and thresholds (locked at Level 4)

- **Title (stage 04):** types `[thematic_rq]`, scale `ternary`, threshold `0.67`.
- **Abstract (stage 05):** types `[thematic_sub_rq]`, scale `weighted`, threshold `0.35`.
- **Full-text (stage 06):** types `[thematic_sub_rq, qa]`, scale `weighted`, threshold `0.55`.

### Manual review rules

Hard gates that are easier to enforce by reading the record's metadata than by an LLM judgment. Applied during stages 04 and 05 via the `My Final Decision` column of the per-stage spreadsheet, which overrides the automatic screening decision.

1. **Document type.** Exclude surveys, systematic reviews, mapping studies, editorials, posters, abstracts-only, tutorials, demos without evaluation, and book chapters.
2. **Language.** Exclude papers not written in English.
3. **Source quality.** Exclude non-peer-reviewed records (e.g., arXiv-only, preprint-only, unpublished technical reports).

## 6. Models & Classifier Configs

Per-stage assignments. The `models` block names the LLM model used by `_screening-llm-reviewer` (pass 2 of each screening stage). The `classifier_configs` block names the path the `_screening-classifier-runner` reads/writes for pass 1.

Stages 04 (title) and 05 (abstract) were screened in the legacy pipeline (pre-v3.2.0); their decisions are migrated into the per-paper markdown files under `papers/`. The models and classifier-config below are the v3.2.0 baseline. Stage 06 (full-text) will refine the classifier-config via Q&A on first run of `/04-screen --stage full-text`.

```yaml
models:
  title-screening: claude-haiku-4-5
  abstract-screening: claude-sonnet-4-6
  full-text-screening: claude-haiku-4-5

classifier_configs:
  title-screening: protocols/classifier-config.json
  abstract-screening: protocols/classifier-config.json
  full-text-screening: protocols/classifier-config-fulltext.json # split at first run of stage 06
```

Conventions:

- The runner agent (`agents/_screening-classifier-runner.md`) created the legacy split configs (`protocols/classifier-config-{title,abstract}.json`); they are preserved under `legacy/protocols/`. The consolidated v3 file at `protocols/classifier-config.json` is the abstract-stage superset (8 categories, 194 patterns, 26 overrides) translated to the v3 schema (`version`, `priority_order`, `kind`, `priority_index`).
- Patterns can opt out of a specific stage via `applicable_stages` in the config; this lets one shared file serve all three stages with stage-aware activation.
- A model is chosen by the user at the first run of each stage; the choice is committed as `[NN] claude-md: model selected (<id>)` and written here.

## 7. Active reference-reviews

`<List of citation_keys from reference-reviews/index.yaml the user has activated for this review. Agents at stages 01, 02, 04, 05, 06, 07 may consult these to inform suggestions.>`

- _none_

## 8. Taxonomy

The taxonomy is built in stage `07-taxonomy-development` and iterates until the user marks it locked. Until then, this section reflects the current iteration.

**Status:** `iterating` (iteration 1, phase 07a' deductive draft)

**Origin:** `hybrid` — twelve axes seeded deductively from sub-RQs RQ1.1–RQ4.4; RQ5.1/RQ5.2 are corpus-level synthesis questions handled in stages 08–09, not per-paper labels. Inductive open coding (Phase 07a) is reserved for emergent dimensions exposed when the seeded axes fail to cover a paper.

`taxonomy.origin: hybrid`
`taxonomy.seed_axes: [RQ1.1, RQ1.2, RQ1.3, RQ2.1, RQ2.2, RQ3.1, RQ3.2, RQ3.3, RQ4.1, RQ4.2, RQ4.3, RQ4.4]`

**Adversarial mode:** `off` for this iteration. May be flipped on per-axis at Phase 07b if any axis proves contentious.

### 8.1 Axes

Twelve axes, each linked to one sub-RQ. Value sets are first-pass drafts based on the sub-RQ text and prior literature on agentic AI for systems management; they will be refined during coverage validation. Multi-valued papers use the `mixed` suffix; papers without explicit treatment use `not_reported` or `none`.

- **`agent_architecture`** — Topology of the perceive-reason-act loop. — seed_for: RQ1.1
  - Values: `single_agent`, `multi_agent_collaborative`, `multi_agent_hierarchical`, `single_agent_with_tools_subroutines`, `not_specified`
- **`infra_coupling`** — Mechanism by which the agent's action grammar binds to infrastructure controllers. — seed_for: RQ1.2
  - Values: `kubernetes_api`, `cloud_provider_api`, `custom_tools_api`, `mcp_protocol`, `simulator_only`, `prompt_only_no_tools`, `mixed`
- **`safety_guardrails`** — Mechanisms that constrain or vet agent actions before they reach the system. — seed_for: RQ1.3
  - Values: `none_explicit`, `human_in_the_loop`, `action_validator`, `policy_gate`, `sandbox_or_dry_run`, `rollback_or_recovery`, `multiple`
- **`decision_class`** — Resource-management decision delegated to the agent. — seed_for: RQ2.1
  - Values: `scheduling`, `placement`, `scaling_autoscaling`, `offloading`, `migration`, `routing_or_traffic_steering`, `energy_or_power_management`, `remediation_fault_response`, `mixed`
- **`autonomy_level`** — Authority the agent has over the final decision. — seed_for: RQ2.2
  - Values: `advisory`, `supervised`, `autonomous`
- **`reasoning_process`** — Reasoning strategy invoked by the agent during decision-making. — seed_for: RQ3.1
  - Values: `direct_prompting`, `chain_of_thought`, `react`, `plan_and_execute`, `reflection_or_self_refine`, `debate_or_multi_agent_consensus`, `self_consistency`, `mixed`
- **`grounding_mechanism`** — How current system state is brought into the agent's reasoning context. — seed_for: RQ3.2
  - Values: `telemetry_only`, `rag_over_docs_or_runbooks`, `episodic_memory`, `vector_db`, `knowledge_graph`, `mixed`
- **`domain_knowledge`** — How the LLM is conditioned with infrastructure-management knowledge. — seed_for: RQ3.3
  - Values: `zero_shot`, `few_shot_examples`, `structured_prompting_or_dsl`, `fine_tuning`, `ontology_or_schema`, `mixed`
- **`evaluation_environment`** — Where empirical results are produced. — seed_for: RQ4.1
  - Values: `simulation`, `real_testbed`, `production`, `synthetic_benchmark`, `real_traces`, `mixed`
- **`rm_perf_metrics`** — Resource-management performance metrics reported. — seed_for: RQ4.2
  - Values: `latency`, `cost`, `energy`, `sla_violations`, `utilization`, `throughput`, `multiple`
- **`agent_overhead_metrics`** — Agent / inference overhead metrics reported. — seed_for: RQ4.3
  - Values: `not_reported`, `token_usage`, `inference_latency`, `monetary_cost_per_decision`, `model_size_or_footprint`, `agent_loop_throughput`, `multiple`
- **`safety_governance_metrics`** — Safety / governance metrics reported. — seed_for: RQ4.4
  - Values: `not_reported`, `unsafe_or_invalid_action_rate`, `human_intervention_frequency`, `audit_coverage`, `policy_compliance`, `multiple`

### 8.2 Code book

One- to two-sentence definitions of each value. The code book is the contract the classifier follows; ambiguous cases trigger checkpoints that may refine these definitions.

**`agent_architecture`**

- `single_agent`: One LLM-driven loop reasons over the full state and emits the action; tool calls do not introduce additional autonomous agents.
- `multi_agent_collaborative`: Two or more peer agents exchange messages or vote without a fixed coordinator; consensus emerges horizontally.
- `multi_agent_hierarchical`: A coordinator/planner agent dispatches sub-tasks to specialized executor agents with a clear top-down structure.
- `single_agent_with_tools_subroutines`: A single primary agent invokes non-agentic helpers (XAI module, predictor, GP/heuristic solver, RAG retriever) that do not themselves run an autonomous loop.
- `not_specified`: The paper proposes an agentic mechanism but does not pin down the topology.

**`infra_coupling`**

- `kubernetes_api`: Actions are realized through Kubernetes primitives (scheduler plugin, HPA/VPA, kubectl, operator).
- `cloud_provider_api`: Actions go through hyperscaler SDKs/CLIs (AWS/Azure/GCP) without a Kubernetes layer.
- `custom_tools_api`: The paper defines a bespoke tool surface for the agent to call (simulator hooks, REST endpoints, in-house orchestrator).
- `mcp_protocol`: Model Context Protocol is the explicit binding between agent and infrastructure tools.
- `simulator_only`: The agent acts inside a simulator/emulator with no real-system coupling.
- `prompt_only_no_tools`: The LLM emits text (a schedule, a plan) consumed externally; no tool-calling layer.
- `mixed`: Combination of the above (e.g., kubernetes_api + custom_tools_api).

**`safety_guardrails`**

- `none_explicit`: No explicit guardrail mechanism is described.
- `human_in_the_loop`: A human operator approves, edits, or vetoes actions before execution.
- `action_validator`: A deterministic check (schema, simulator, constraint solver) validates each proposed action.
- `policy_gate`: Declarative policies (OPA, intent rules) gate execution.
- `sandbox_or_dry_run`: Actions are first executed in an isolated/dry-run environment before propagation.
- `rollback_or_recovery`: Reversal mechanism kicks in when an action's effect is bad.
- `multiple`: Two or more of the above mechanisms.

**`decision_class`**

- `scheduling`: Selecting which workload runs when on which resource (queue, job, batch).
- `placement`: One-shot mapping of a service/container to a node/region; no ongoing dynamics.
- `scaling_autoscaling`: Adjusting replica counts or resource shapes in response to load.
- `offloading`: Choosing whether to execute locally or send work to another tier (edge↔cloud).
- `migration`: Moving an already-running workload between hosts/tiers.
- `routing_or_traffic_steering`: Steering requests/traffic across network paths or service instances.
- `energy_or_power_management`: Decisions whose primary objective is energy/power/carbon.
- `remediation_fault_response`: Closed-loop response to faults, anomalies, or incidents.
- `mixed`: The agent handles two or more of the above.

**`autonomy_level`**

- `advisory`: Output is a recommendation; a human or external policy decides whether to apply it.
- `supervised`: The agent acts, but a human or rule-based monitor can intervene/approve before effect.
- `autonomous`: The agent's decisions reach the system without human or rule-based gating.

**`reasoning_process`**

- `direct_prompting`: One-shot LLM call emits the decision; no explicit reasoning scaffold.
- `chain_of_thought`: Step-by-step reasoning traces are elicited before the action.
- `react`: Interleaved reasoning and tool actions over multiple turns.
- `plan_and_execute`: A plan is produced first, then executed by the same or a sub-agent.
- `reflection_or_self_refine`: The agent critiques and revises its own output before commitment.
- `debate_or_multi_agent_consensus`: Multiple agents argue; the resolution drives the action.
- `self_consistency`: Multiple sampled reasonings are aggregated (majority/vote).
- `mixed`: Multiple of the above explicitly combined.

**`grounding_mechanism`**

- `telemetry_only`: Live metrics/logs/traces injected into the prompt; nothing else.
- `rag_over_docs_or_runbooks`: Retrieval over external documents (runbooks, manuals, policies).
- `episodic_memory`: Past episodes/decisions stored and queried for similarity.
- `vector_db`: An explicit vector database backs retrieval (RAG or memory).
- `knowledge_graph`: Structured graph (ontology, topology) consulted at decision time.
- `mixed`: Two or more of the above explicitly combined.

**`domain_knowledge`**

- `zero_shot`: A general-purpose model is used without examples or fine-tuning.
- `few_shot_examples`: Examples of decisions or interactions are included in the prompt.
- `structured_prompting_or_dsl`: Decision domain is captured in a structured schema/DSL the model fills in.
- `fine_tuning`: The model is fine-tuned, LoRA-adapted, or RLHF-tuned on domain data.
- `ontology_or_schema`: An explicit infrastructure ontology/schema scaffolds the prompt.
- `mixed`: Combination (e.g., few_shot + ontology).

**`evaluation_environment`**

- `simulation`: Experiments run inside a simulator (CloudSim, EdgeSimPy, custom).
- `real_testbed`: Physical or cloud-hosted cluster set up for the experiment.
- `production`: Live production deployment data is used.
- `synthetic_benchmark`: Workload generator/benchmark suite drives the evaluation.
- `real_traces`: Real production traces replayed in simulation or testbed.
- `mixed`: Two or more of the above explicitly combined.

**`rm_perf_metrics`**

- `latency`: Response time, queuing delay, makespan, end-to-end latency.
- `cost`: Monetary cost of infrastructure (not inference cost).
- `energy`: Energy/power consumption or carbon intensity of execution.
- `sla_violations`: SLA/SLO miss rate or constraint violation count.
- `utilization`: CPU/memory/bandwidth utilization.
- `throughput`: Request rate, job rate, goodput.
- `multiple`: Two or more of the above reported jointly.

**`agent_overhead_metrics`**

- `not_reported`: No agent/inference overhead metric is reported.
- `token_usage`: Tokens consumed per decision/episode.
- `inference_latency`: Wall-clock time of the agent's decision step.
- `monetary_cost_per_decision`: USD/decision or USD/episode from inference.
- `model_size_or_footprint`: Parameter count, memory footprint.
- `agent_loop_throughput`: Decisions per second the agent can sustain.
- `multiple`: Two or more of the above reported jointly.

**`safety_governance_metrics`**

- `not_reported`: No safety/governance metric is reported.
- `unsafe_or_invalid_action_rate`: Frequency of malformed, infeasible, or unsafe proposed actions.
- `human_intervention_frequency`: How often a human override is triggered.
- `audit_coverage`: Fraction of decisions accompanied by audit logs/traces.
- `policy_compliance`: Compliance rate with declared policies/intents.
- `multiple`: Two or more of the above reported jointly.

### 8.3 Iteration history

Each iteration of the taxonomy is a commit `[07] iteration-<k>`; the final state is `[07] lock`.

- **Iteration 1 (pending review):** seeded 12 deductive axes from RQ1.1–RQ4.4 (Phase 07a' draft). Excluded RQ5.1/RQ5.2 from taxonomic dimensions (synthesis-level questions). Adversarial mode off.

## 9. Anchors

Decisions accepted at checkpoints become anchors for subsequent decisions in the same or later stages. Anchors are NOT a parallel criteria system — they are concrete examples the agent can cite when a borderline case resembles one already decided. Each anchor links to the commit that created it.

### Inclusion anchors

- `<paper-id>` — `<brief reason>` — commit `<hash>` — stage `<NN>`

### Exclusion anchors

- `<paper-id>` — `<brief reason>` — commit `<hash>` — stage `<NN>`

### Taxonomy anchors

Populated during `07-taxonomy-development`. Each anchor pins a paper to a prototypical position on one or more axes.

- `<paper-id>` — axis `<axis>` = `<value>` — `<reason>` — commit `<hash>`

## 10. Notes

**Spreadsheet formatting requirements (stages 05 and 06):** The full spec lives in `protocols/spreadsheet-formatting.md`. Every agent that writes a screening tab must apply all three rules before committing:

1. Background fill on ID and Title columns — green (`#e7ffee`) for Include, red (`#ffeff0`) for Exclude.
2. Sort order — Excluded rows first (red block), then Included rows (green block); within each block sort by sub-agent disagreement descending.
3. Bold strategic keywords in Title and Abstract cells using rich-text cell formatting (not markdown) to surface the reason for inclusion/exclusion at a glance.

---

<!--
Change history: do not edit manually. The git log on this file is the authoritative history of
protocol changes.
-->
