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
- **Current stage:** `05-abstract-screening (locked); next: 06-full-text-screening`

## 1. Locks (machine-readable)

Agents use this block to decide whether a given stage can run. A stage can only start when its predecessors are all `locked`.

```yaml
locks:
  00-new-review:                locked    # pending | locked
  01-research-questions:        locked
  02-search-string:             locked
  03-parse-references-metadata: locked
  04-title-screening:           locked
  05-abstract-screening:        locked
  06-full-text-screening:       pending
  07-taxonomy-development:      pending   # has intermediate `iterating` state during inductive loop
  08-analysis:                  pending
  09-report:                    pending
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
  title-screening:      claude-haiku-4-5
  abstract-screening:   claude-sonnet-4-6
  full-text-screening:  claude-sonnet-4-6

classifier_configs:
  title-screening:      protocols/classifier-config.json
  abstract-screening:   protocols/classifier-config.json
  full-text-screening:  protocols/classifier-config-fulltext.json   # split at first run of stage 06
```

Conventions:

- The runner agent (`agents/_screening-classifier-runner.md`) created the legacy split configs (`protocols/classifier-config-{title,abstract}.json`); they are preserved under `legacy/protocols/`. The consolidated v3 file at `protocols/classifier-config.json` is the abstract-stage superset (8 categories, 194 patterns, 26 overrides) translated to the v3 schema (`version`, `priority_order`, `kind`, `priority_index`).
- Patterns can opt out of a specific stage via `applicable_stages` in the config; this lets one shared file serve all three stages with stage-aware activation.
- A model is chosen by the user at the first run of each stage; the choice is committed as `[NN] claude-md: model selected (<id>)` and written here.

## 7. Active reference-reviews

`<List of citation_keys from reference-reviews/index.yaml the user has activated for this review. Agents at stages 01, 02, 04, 05, 06, 07 may consult these to inform suggestions.>`

- _none_

## 8. Taxonomy

The taxonomy is built inductively in stage `07-taxonomy-development` and iterates until the user marks it locked. Until then, this section reflects the current iteration.

**Status:** `pending` | `iterating` (with current iteration number) | `locked`

### 8.1 Axes

`<Empty while pending. During iteration, lists candidate axes proposed by the open-coding + clustering loop. Each axis has a short description and the set of permitted values.>`

- **`<axis-name>`** — `<short description>`
  - Values: `<v1, v2, v3, ...>`

### 8.2 Code book

`<Definition of each value in each axis, with 1–2 sentences explaining when a paper fits that value. Emerges during the open-coding stage; refined during clustering.>`

- `<axis>` / `<value>`: `<definition>`

### 8.3 Iteration history

Each iteration of the taxonomy is a commit `[07] iteration-<k>`; the final state is `[07] lock`.

- **Iteration 1:** `<summary: e.g., "initial open coding produced 47 free codes over 38 papers">`
- **Iteration 2:** `<summary: e.g., "clustering proposed 5 axes; user merged two overlapping ones">`
- **Iteration k:** `<...>`
- **Locked:** commit `<hash>` — `<summary>`

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
