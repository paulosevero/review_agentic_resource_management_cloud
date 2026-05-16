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

- **Topic:** `Agentic AI (LLM-based agents) for resource management decisions in Cloud, Edge, Fog, and the Edge-Cloud`
- **Repo:** `/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud`
- **Created:** `2026-04-25`
- **Migrated to v3.2.0:** `2026-05-09`
- **Current stage:** `08-analysis (locked); next: 09-report`

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
  07-taxonomy-development: locked
  08-analysis: locked
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

**Status:** `locked` (iteration 1; all 20 included papers classified with §07b blocks).

**Origin:** `hybrid`. Iteration 1 began with 12 deductively seeded axes (one per sub-RQ in RQ1.1–RQ4.4) and converged, through user review against the corpus, on 7 faceted axes that span the same conceptual ground but at a coarser granularity better suited to a 20-paper corpus. RQ5.1/RQ5.2 are corpus-level synthesis questions handled in stages 08–09 and are not encoded as per-paper labels.

`taxonomy.origin: hybrid`
`taxonomy.seed_axes: [RQ1.1, RQ1.2, RQ1.3, RQ2.1, RQ2.2, RQ3.1, RQ3.2, RQ3.3, RQ4.1, RQ4.2, RQ4.3, RQ4.4]`

**Adversarial mode:** `off` for this iteration. May be flipped on per-axis at Phase 07b if any axis proves contentious.

**Notation:** ⋆ marks single-select axes (one value per paper); ▲ marks multi-select axes (one or more values per paper).

### 8.1 Axes

Seven axes; every included paper must classify on every axis with ≥ MED confidence (faceted taxonomy, no orphan permitted).

- **`infrastructure`** (⋆) — Tier of the infrastructure the agent controls. — seed_for: RQ1.2 (infrastructure scope of coupling).
  - Values: `Cloud-Only`, `Edge-Cloud`.

- **`decision`** (▲) — Class(es) of resource-management decision delegated to the agent. — seed_for: RQ2.1.
  - Values: `Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`.

- **`agentic_configuration`** — Configuration of the agentic system, captured as a two-facet axis. A paper carries exactly one value in each facet; the facets are evaluated independently and reported jointly. The cross-product `Pipeline Contributor × Multi-Agent` is empirically empty in the current corpus, and that vacancy is noted as a research-opportunity observation rather than a coverage gap — the two facets remain valid axes on their own. — seed_for: RQ1.1 + RQ1.3 (architecture + role).
  - Facet **`decision_role`** (⋆): `Sole Decider`, `Pipeline Contributor`.
  - Facet **`coordination_topology`** (⋆): `Single Agent`, `Multi-Agent`.

- **`reasoning_approach`** (▲) — Reasoning and grounding mechanisms employed by the agent. Multi-select: a paper may combine, e.g., `Prompting` + `Knowledge Retrieval`. — seed_for: RQ3.1 + RQ3.2 + RQ3.3.
  - Values: `Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`.

- **`autonomy_level`** (⋆) — Authority the agent holds over the action that reaches the system. — seed_for: RQ2.2 + RQ1.3.
  - Values: `Supervised`, `Autonomous`.

- **`metric`** (▲) — Families of metrics reported in the evaluation. Multi-select: every paper reports at least `RM Performance Metric`; many also report `Agent Performance Metric`. — seed_for: RQ4.2 + RQ4.3 + RQ4.4.
  - Values: `RM Performance Metric`, `Agent Performance Metric`.

- **`evaluation_method`** (⋆) — Empirical environment in which the results are produced. Use of production traces or synthetic benchmarks is discussed in the text under the chosen value, not encoded as a separate value. — seed_for: RQ4.1.
  - Values: `Simulation`, `Practical Testbed`.

### 8.2 Code book

One- to two-sentence definitions of every value. Borderline cases trigger checkpoints that may refine these definitions.

**`infrastructure`**

- `Cloud-Only`: Centralized datacenters operated by a hyperscaler or in-house provider. Includes Kubernetes clusters in a single region, IaaS/PaaS/SaaS scopes, and multi-cloud arrangements that remain inside cloud datacenters. Edge or fog resources are not part of the controlled tier.
- `Edge-Cloud`: Cloud + Edge/Fog are jointly considered; decisions can place, move, route, scale, or remediate across tiers. Papers framed as "edge computing" that nevertheless reach back to a cloud layer (typical case in the corpus) fall here.

**`decision`**

- `Scheduling`: Temporal ordering of jobs, tasks, or requests onto resources already allocated (queue management, batch dispatch, time-slot assignment).
- `Placement & Offloading`: One-shot or recurring mapping of services, containers, or tasks to hosts (`placement`) and local-vs-remote execution decisions (`offloading`). Includes migration of running workloads between hosts/tiers when described as a placement decision.
- `Scaling`: Adjusting replica counts, resource shapes (CPU/memory limits), or throttling parameters in response to observed or predicted load. Covers horizontal, vertical, and autoscaling.
- `Routing & Slicing`: Steering requests or traffic across network paths, service instances, or service-mesh routes; includes network-slice composition and admission control on slices.
- `Remediation`: Closed-loop response to faults, anomalies, or incidents (root-cause analysis followed by an automated repair action: restart, rollback, reconfigure, scale-out as repair).

**`agentic_configuration`** (two facets)

Facet `decision_role` — Who holds the authority over the final RM action.

- `Sole Decider`: The LLM-agent(s) emit the final resource-management action; no non-LLM mechanism (heuristic, optimizer, rules, RL, classical scheduler) decides in their place. Tools and retrievers invoked by the agent are subordinate (they execute the agent's plan but do not decide).
- `Pipeline Contributor`: The LLM-agent(s) contribute to a larger pipeline in which a non-LLM mechanism participates actively in the decision. The LLM suggests candidates, parses intent, generates a heuristic, classifies inputs, or translates to policy, but the non-LLM component holds the final say.

Facet `coordination_topology` — How many LLM-agents coordinate inside the loop.

- `Single Agent`: One LLM-agent in the loop. Auxiliary modules (XAI, retrievers, solvers, schedulers) are not themselves LLM-agents.
- `Multi-Agent`: Two or more LLM-agents cooperate in the loop, either as peers (debate, vote, message-passing) or as a coordinator + specialized executors. Topology details (peer vs hierarchical) are described in the text.

Cross-product `Pipeline Contributor × Multi-Agent` is empirically empty in the current corpus and reported in stage 09 as a research-opportunity observation, not as a coverage gap of the taxonomy.

**`reasoning_approach`**

- `Prompting`: The decision is emitted by a single LLM call; covers zero-shot, few-shot, and Chain-of-Thought reasoning _elicited inside the prompt itself_. There is no multi-turn agent loop and no external retrieval at decision time.
- `Iterative Reasoning`: Multi-turn agent loop in which the LLM reasons across steps with or without tool calls between turns: ReAct, plan-and-execute, reflexion / self-refine, self-consistency aggregation, multi-agent debate. The loop scaffolding — not the prompt — drives the reasoning.
- `Knowledge Retrieval`: External content is recovered and injected into the prompt at decision time: RAG over documents/runbooks, vector-DB lookup, episodic memory, knowledge graph or ontology query. Grounding via _external_ retrieval is the defining feature.
- `Model Specialization`: The model itself is adapted to the domain before deployment: full fine-tuning, LoRA / adapter, RLHF, or instruction-tuning on infrastructure data. Can be combined with any of the above at inference time.

**`autonomy_level`**

- `Supervised`: The agent acts, but an external gate (human-in-the-loop, deterministic validator, policy engine like OPA, or dry-run sandbox) can intercept, approve, edit, or veto the action before its effect reaches the system.
- `Autonomous`: The agent's decisions reach the system without any external human or rule-based gate. Self-imposed safety mechanisms internal to the LLM (e.g., self-reflection on its own plan) still count as `Autonomous`.

**`metric`**

- `RM Performance Metric`: Metrics that evaluate the outcome of the resource-management decision on the system. Includes job/task completion time, latency / delay / response time, throughput / goodput, utilization (CPU/memory/bandwidth), SLA / SLO violations, energy / power / carbon consumption, monetary infrastructure cost, queue length, makespan. Synonyms collapse to the canonical metric name (`latency` ≡ `delay` ≡ `response time`; `accuracy` ≡ `success rate` when applied to RM outcome; `cost` ≡ `monetary cost` when referring to infrastructure cost).
- `Agent Performance Metric`: Metrics that evaluate the agent itself, independent of the RM outcome. Includes decision accuracy / success rate (of the agent's own plan or output), inference latency per decision, token usage per decision or episode, number of LLM calls / agent-loop iterations, monetary cost per decision (from inference), model size / footprint, audit-trace coverage, rate of unsafe or malformed actions proposed.

**`evaluation_method`**

- `Simulation`: Experiments run inside a simulator or emulator (CloudSim, EdgeSimPy, custom-built). Workloads can be synthetic, drawn from a benchmark suite, or replayed from real traces; the discriminating fact is that the _execution substrate_ is simulated.
- `Practical Testbed`: Experiments run on a physical cluster or cloud-hosted resources provisioned for the study. Includes Kubernetes clusters in real clouds, on-prem racks, and edge testbeds. Replay of production traces against real resources falls here, not under `Simulation`.

### 8.3 Iteration history

Each iteration of the taxonomy is a commit `[07] iteration-<k>`; the final state is `[07] lock`.

- **Iteration 1 — `[07] origin: hybrid`:** Seeded 12 deductive axes from RQ1.1–RQ4.4 (Phase 07a' first draft). RQ5.1/RQ5.2 excluded as synthesis-level. Adversarial mode off. _Outcome:_ draft too granular for a 20-paper corpus; flagged for consolidation against user feedback and corpus validation.
- **Iteration 1 (consolidated) — `[07] iteration-1: 7-axis taxonomy consolidated`:** Twelve seed axes consolidated to seven faceted axes through user dialog and empirical validation against the 20 included papers. Decisions captured: (a) `decision` drops `Energy` as a class (energy is cross-cutting and lives in `metric.RM Performance Metric`); (b) `agentic_configuration` initially unified role-in-cycle and coordination-topology into a single 2×2 axis (4 cells, 1 reserved); (c) `reasoning_approach` consolidates 3 seed axes (RQ3.1+RQ3.2+RQ3.3) into 4 multi-select families; (d) `metric` consolidates RQ4.2+RQ4.3+RQ4.4 into 2 multi-select families with energy living inside RM Performance Metric; (e) `evaluation_method` reduces to `Simulation` / `Practical Testbed` with production-traces and synthetic-benchmarks discussed in text; (f) safety/governance dimensions live within `autonomy_level` (gate posture) and `metric.Agent Performance Metric` (governance metrics).
- **Iteration 1 (lock) — `[07] lock`:** Phase 07b classification written into every `papers/paper-NNNN.md` (verbatim evidence + neighbor-not-chosen rationale per axis cell). Two final renames applied for clarity: `Edge-Cloud Continuum` → `Edge-Cloud` (broader; not every cloud+edge system is a continuum) and `Real Testbed` → `Practical Testbed`. Five evidence-driven cell corrections applied after Phase 07b: paper-0930, paper-1157, paper-2470, paper-2723 → `evaluation_method = Practical Testbed`; paper-1404 → `infrastructure = Edge-Cloud`. Final distribution: `infrastructure` Cloud-Only 9 / Edge-Cloud 11; `agentic_configuration.decision_role` Sole Decider 14 / Pipeline Contributor 6; `agentic_configuration.coordination_topology` Single Agent 18 / Multi-Agent 2; `autonomy_level` Supervised 5 / Autonomous 15; `evaluation_method` Simulation 13 / Practical Testbed 7. Multi-select totals in stages/07-taxonomy-development.md.
- **Iteration 1 (refined post-validation) — `[07] iteration-1: post-validation refinements`:** After Phase 07a' coverage validation on the 20 papers, three refinements were applied to eliminate empty single-value cells and restructure the agentic-system axis. (a) `infrastructure` renamed `Cloud` → `Cloud-Only` and `Continuum` → `Edge-Cloud`; `Edge` dropped (empirically empty — every "edge" paper in the corpus also reaches the cloud, so all such papers fall under `Edge-Cloud`). (b) `autonomy_level` dropped `Advisory` (empirically empty in the corpus); axis is now `Supervised` / `Autonomous`. (c) `agentic_configuration` restructured from a single axis with cross-product values to a two-facet axis: facet `decision_role` (`Sole Decider` / `Pipeline Contributor`) and facet `coordination_topology` (`Single Agent` / `Multi-Agent`). The two facets are valid axes on their own; the absence of the `Pipeline Contributor × Multi-Agent` combination in the corpus is reported in stage 09 as a research opportunity, not a taxonomy gap. _Status:_ coverage validation re-confirmed clean across all 20 papers; awaiting Phase 07b classification before final lock.

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
