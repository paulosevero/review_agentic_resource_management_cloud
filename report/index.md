# Rapid Review Report — Agentic AI for Resource Management in Cloud, Edge, Fog, and the Edge-Cloud Continuum

This report is the navigable entry point to the locked corpus, taxonomy, and analysis views. It is the table of contents for the manuscript-writing phase; the manuscript itself lives outside this plugin.

- **Theme:** Agentic AI (LLM-based agents) for resource management decisions in Cloud, Edge, Fog, and the Edge-Cloud continuum.
- **Search executed:** 2026-04-26 (Scopus, `PUBYEAR > 2016`).
- **Corpus locked at full-text:** 20 included papers (`status.06-full-text-screening == include`).
- **Taxonomy lock:** 7 axes (faceted, per CLAUDE.md §8).
- **Analysis lock:** 16 views (4 cross-cutting + 12 RQ-anchored) — see `stages/08-analysis.md`.

## Corpus summary

PRISMA-style flow, aggregated from per-paper status frontmatter:

| Stage                            | Count | Source of truth                                |
| -------------------------------- | ----- | ---------------------------------------------- |
| Imported (Scopus, dedup-merged)  | 2964  | `papers/paper-*.md` frontmatter                |
| Title screening — include        | 572   | `status.04-title-screening == include`         |
| Title screening — exclude        | 2377  | `status.04-title-screening == exclude`         |
| Abstract screening — include     | 53    | `status.05-abstract-screening == include`      |
| Abstract screening — exclude     | 519   | `status.05-abstract-screening == exclude`      |
| Full-text screening — include    | 20    | `status.06-full-text-screening == include`     |
| Full-text screening — exclude    | 33    | `status.06-full-text-screening == exclude`     |
| Taxonomy classified              | 20    | `status.07-taxonomy-development == classified` |
| Contributing to ≥1 analysis view | 20    | `status.08-analysis == analyzed`               |

Year distribution of the locked corpus: 2024 — 2; 2025 — 14; 2026 — 4 (partial; search window cuts mid-year). The 2024 figure marks the empirical onset of agentic-AI-for-resource-management work in the indexed literature.

## Protocol summary

The locked protocol lives in [`protocols/screening.yaml`](../protocols/screening.yaml). The Boolean search string (with per-database adaptations) and the typed inclusion criteria are mirrored in [`CLAUDE.md §4`](../CLAUDE.md) and [§5](../CLAUDE.md). What follows is a prose summary.

### Research questions

Five top-level RQs decompose thematically into 13 sub-RQs (see [`CLAUDE.md §3`](../CLAUDE.md) for the authoritative form):

- **RQ1** — How are agentic AI systems architected for resource management in cloud, edge, fog, and continuum infrastructures?
  - _RQ1.1_ — Architectural patterns of the perceive-reason-act loop (single-agent vs multi-agent vs hierarchical; ReAct/Plan-and-Execute/Reflexion).
  - _RQ1.2_ — Coupling to infrastructure via tools/APIs/MCP (tool surface, action grammar, integration with Kubernetes/orchestrators).
  - _RQ1.3_ — Safety and guardrail mechanisms (HITL, action validators, sandboxing, policy gates, rollback).
- **RQ2** — Which classes of resource management decisions are delegated to agentic AI systems, and under what operational conditions?
  - _RQ2.1_ — Classes of resource management decisions delegated.
  - _RQ2.2_ — Operational conditions and autonomy level (advisory/supervised/autonomous).
- **RQ3** — What reasoning processes and grounding mechanisms do agentic AI systems employ to translate observed system state into resource management actions?
  - _RQ3.1_ — Reasoning processes (CoT, ToT, ReAct, planning + reflection, debate, self-consistency).
  - _RQ3.2_ — Grounding mechanisms (telemetry, RAG over runbooks/docs, episodic memory, vector DBs, knowledge graphs).
  - _RQ3.3_ — Domain knowledge incorporation (fine-tuning, structured prompting, few-shot, infrastructure ontologies).
- **RQ4** — How is the behavior of agentic AI systems for resource management evaluated?
  - _RQ4.1_ — Evaluation methodologies and environments (simulation, real testbed, production, synthetic benchmarks, real traces).
  - _RQ4.2_ — Resource-management performance metrics (latency, cost, energy, SLA, utilization, throughput).
  - _RQ4.3_ — Agent/inference overhead metrics (token usage, inference latency, monetary cost per decision, model size/footprint, agent-loop throughput).
  - _RQ4.4_ — Safety and governance metrics (rate of unsafe/invalid actions, frequency of human intervention, audit coverage, policy compliance).
- **RQ5** — What open challenges, unresolved tensions, and promising future directions emerge from the synthesis of the included literature?
  - _RQ5.1_ — Unresolved methodological and technical tensions (inference cost vs. decision latency, hallucination in critical environments, transferability across infrastructures).
  - _RQ5.2_ — Governance, accountability, and auditability gaps (decision traceability, responsibility attribution, regulatory requirements, explainability).

### Search string

Three Boolean clauses joined by `AND`: (i) agentic-AI / LLM / autonomous-agent terms; (ii) resource-management decision terms (scheduling, placement, scaling, routing, slicing, orchestration, admission, energy, fault-tolerance, etc.); (iii) infrastructure-scope terms (cloud, edge, fog, continuum, MEC, serverless, FaaS, Kubernetes, datacenter, IaaS/PaaS/SaaS). The Scopus-ready form lives in [`CLAUDE.md §4`](../CLAUDE.md).

**Per-database adaptation:** Scopus only (Web of Science, IEEE Xplore, ACM DL were explicitly excluded by the user). Scopus field selector: `TITLE-ABS-KEY`; temporal filter: `PUBYEAR > 2016` (Transformer-era boundary).

### Screening pipeline

Two-pass screening at each stage (title, abstract, full-text):

- **Pass 1** — deterministic regex classifier (`scripts/deterministic_classifier.py` + `protocols/classifier-config.json`) emits `Proposed Decision`, `Proposed Justification`, and an `Evidence Trail` for every paper.
- **Pass 2** — single LLM reviewer reads the regex output plus the stage-allowed paper body and fills `My Final Decision` and `My Justification` per paper. Per-stage model assignments live in [`CLAUDE.md §6`](../CLAUDE.md).
- **No automated consolidation.** Final decisions are user-finalized in column L of `spreadsheet.xlsx`. Conservative tiebreak: when in doubt at title or abstract, include — the cost of a false positive is one extra read at the next stage; the cost of a false negative is losing the paper.
- **Manual-review rules** (applied as overrides in `My Final Decision`): exclude surveys, mapping studies, editorials, posters, abstracts-only, tutorials, demos without evaluation, book chapters, non-English papers, and non-peer-reviewed records.

Full reproducibility material: [`protocols/screening.yaml`](../protocols/screening.yaml), [`protocols/classifier-config.json`](../protocols/classifier-config.json), [`protocols/classifier-config-fulltext.json`](../protocols/classifier-config-fulltext.json).

## Findings per RQ

Findings are anchored to the locked analysis views from [`stages/08-analysis.md`](../stages/08-analysis.md). Each sub-section lists the sub-RQ text, the synthesis paragraph, the views, the axes they touch, the contributing papers, and 2–3 representative quotes.

### Cross-cutting view (anchor: `RQ1`)

**How are agentic AI systems architected for resource management in cloud, edge, fog, and continuum infrastructures?**

The cross-cutting `temporal-included` view sanity-checks the corpus emergence: agentic-AI-for-resource-management work crosses the screening bar starting in 2024, accelerates through 2025, and continues into the (partial) 2026 window.

##### View `temporal-included`

- **Type:** `temporal` · **Anchor:** `RQ1` · **Shape:** rows: `year`
- **Spreadsheet tab:** [`temporal-included`](../spreadsheet.xlsx)

| value | count |
| ----- | ----- |
| 2024  | 2     |
| 2025  | 14    |
| 2026  | 4     |

2024: 2 · 2025: 14 · 2026: 4. The 2026 count is partial because the search window cuts mid-year. The 2024 figure marks the empirical onset of agentic-AI-for-resource-management work in the indexed literature (the field only crosses the screening bar in 2024).

**Axes touched:**

- `year` — Publication year of the paper.

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> _LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence_ — [paper-2556](../papers/paper-2556.md) (2026)
>
> _AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks_ — [paper-2723](../papers/paper-2723.md) (2026)
>
> _Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language_ — [paper-2779](../papers/paper-2779.md) (2026)

### RQ1 — How are agentic AI systems architected for resource management in cloud, edge, fog, and continuum infrastructures?

#### RQ1.1 — Architectural patterns of the perceive-reason-act loop (single-agent vs multi-agent vs hierarchical; ReAct/Plan-and-Execute/Reflexion).

The corpus is overwhelmingly single-agent (18/20); the two multi-agent papers ([paper-1991](../papers/paper-1991.md), [paper-2362](../papers/paper-2362.md)) both adopt explicit Iterative Reasoning loops — a multi-agent topology in this corpus implies planning/reflection rather than one-shot prompting. The 2×2 of `decision_role × coordination_topology` shows three populated cells and one empty cell (`Pipeline Contributor × Multi-Agent`), which is flagged as a research-opportunity observation rather than a taxonomy gap.

##### View `agent-coordination-distribution`

- **Type:** `distribution` · **Anchor:** `RQ1.1` · **Shape:** rows: `agentic_configuration.coordination_topology` (single-select)
- **Spreadsheet tab:** [`agent-coordination-distribution`](../spreadsheet.xlsx)

| value        | count |
| ------------ | ----- |
| Single Agent | 18    |
| Multi-Agent  | 2     |

Single-agent topology dominates (18/20). The two Multi-Agent papers (1991, 2362) both adopt Iterative Reasoning, hinting that multi-agent is currently coupled with explicit planning/reflection loops rather than one-shot prompting.

**Axes touched:**

- `agentic_configuration.coordination_topology` — How many LLM-agents coordinate inside the loop (`Single Agent` vs `Multi-Agent`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "directly applying LLMs to cloud scheduling poses fundamental challenges" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `agentic_configuration.coordination_topology` = `Single Agent`

> "a hybrid agent-based workflow that synergizes human-agent collaboration and multi-agent coordination" (§I Introduction)
>
> — [paper-1991](../papers/paper-1991.md), axis `agentic_configuration.coordination_topology` = `Multi-Agent`

##### View `agentic-config-cross`

- **Type:** `pivot` · **Anchor:** `RQ1.1` · **Shape:** rows: `agentic_configuration.decision_role` × cols: `agentic_configuration.coordination_topology`
- **Spreadsheet tab:** [`agentic-config-cross`](../spreadsheet.xlsx)

| value                | Single Agent | Multi-Agent | total |
| -------------------- | ------------ | ----------- | ----- |
| Sole Decider         | 12           | 2           | 14    |
| Pipeline Contributor | 6            | 0           | 6     |

Three of the four cells of the 2×2 are populated; `Pipeline Contributor × Multi-Agent` is empty in the current corpus. This vacancy is reported as a research-opportunity observation, not a coverage gap of the taxonomy (the two facets remain independently valid). The dominant configuration is `Sole Decider × Single Agent` (12/20).

**Axes touched:**

- `agentic_configuration.decision_role` — Who holds authority over the final RM action (`Sole Decider` vs `Pipeline Contributor`).
- `agentic_configuration.coordination_topology` — How many LLM-agents coordinate inside the loop (`Single Agent` vs `Multi-Agent`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLM-Guided Candidate Generation employs few-shot and chain-of-thought prompting to produce diverse scheduling candidates" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `agentic_configuration.decision_role` = `Sole Decider`

> "the scheduler assigns scores to the valid machines based on these preferences" (§I Introduction)
>
> — [paper-2779](../papers/paper-2779.md), axis `agentic_configuration.decision_role` = `Pipeline Contributor`

> "LLMs perceive key factors—such as device location, task type, and context—and adjust task allocation parameters dynamically. They then guide agents to use appropriate tools and perform optimized scheduling" (§Abstract)
>
> — [paper-1991](../papers/paper-1991.md), axis `agentic_configuration.decision_role` = `Sole Decider`

#### RQ1.2 — Coupling to infrastructure via tools/APIs/MCP (tool surface, action grammar, integration with Kubernetes/orchestrators).

Both infrastructure tiers are well-represented (Edge-Cloud 11, Cloud-Only 9). Decision classes split cleanly by tier: Placement & Offloading skews Edge-Cloud (6/9), Scheduling skews Cloud-Only (5/7), Remediation appears exclusively in Edge-Cloud (2/2), Routing & Slicing exclusively in Cloud-Only (1/1). No paper in the corpus reports a pure edge-only configuration under the §8.2 code-book.

##### View `infrastructure-distribution`

- **Type:** `distribution` · **Anchor:** `RQ1.2` · **Shape:** rows: `infrastructure` (single-select)
- **Spreadsheet tab:** [`infrastructure-distribution`](../spreadsheet.xlsx)

| value      | count |
| ---------- | ----- |
| Edge-Cloud | 11    |
| Cloud-Only | 9     |

Edge-Cloud (11) and Cloud-Only (9) are close to parity. Every paper that mentions an edge tier also reaches a cloud tier — a pure edge-only configuration is empirically absent under the §8.2 code-book definition.

**Axes touched:**

- `infrastructure` — Tier of infrastructure controlled by the agent (`Cloud-Only` vs `Edge-Cloud`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "decisions must span heterogeneous domains, including the data plane, Multi-access Edge Computing (MEC), and the 5G core" (§I Introduction)
>
> — [paper-2723](../papers/paper-2723.md), axis `infrastructure` = `Edge-Cloud`

> "Cloud resource scheduling presents a fundamental challenge in modern distributed computing" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `infrastructure` = `Cloud-Only`

##### View `infrastructure-by-decision`

- **Type:** `pivot` · **Anchor:** `RQ1.2` · **Shape:** rows: `decision` (multi-select) × cols: `infrastructure`
- **Spreadsheet tab:** [`infrastructure-by-decision`](../spreadsheet.xlsx)

| value                  | Edge-Cloud | Cloud-Only | total |
| ---------------------- | ---------- | ---------- | ----- |
| Placement & Offloading | 6          | 3          | 9     |
| Scheduling             | 2          | 5          | 7     |
| Remediation            | 2          | 0          | 2     |
| Scaling                | 1          | 1          | 2     |
| Routing & Slicing      | 1          | 0          | 1     |

Placement & Offloading skews Edge-Cloud (6 of 9). Scheduling skews Cloud-Only (5 of 7). Remediation and Routing & Slicing appear only in Edge-Cloud or only in Cloud-Only respectively; Scaling is split 1:1.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `infrastructure` — Tier of infrastructure controlled by the agent (`Cloud-Only` vs `Edge-Cloud`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Task offloading is a critical EC technique. It transfers tasks from user devices to edge servers" (§Introduction)
>
> — [paper-2936](../papers/paper-2936.md), axis `decision` = `Placement & Offloading`

> "introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `decision` = `Scheduling`

> "The goal is to allocate each workload w j to a..." (§3 Problem Definition)
>
> — [paper-1644](../papers/paper-1644.md), axis `decision` = `Placement & Offloading`

#### RQ1.3 — Safety and guardrail mechanisms (HITL, action validators, sandboxing, policy gates, rollback).

Guardrails are described structurally rather than as a separate axis: the Pipeline Contributor role (6/20) is the structural form of the guardrail boundary — a non-LLM component lands the final action. The same boundary appears, viewed from the metric side, as the `Supervised × Agent-Performance` cell being empty in `metric-by-autonomy`: Supervised systems do not surface agent-side overhead/audit metrics, while every Autonomous system does.

##### View `decision-role-distribution`

- **Type:** `distribution` · **Anchor:** `RQ1.3` · **Shape:** rows: `agentic_configuration.decision_role` (single-select)
- **Spreadsheet tab:** [`decision-role-distribution`](../spreadsheet.xlsx)

| value                | count |
| -------------------- | ----- |
| Sole Decider         | 14    |
| Pipeline Contributor | 6     |

Sole Decider outnumbers Pipeline Contributor 14:6. The Pipeline Contributor group is structurally the same set as the Supervised autonomy group plus paper-1563 (GP hyper-heuristic) — the LLM feeds a downstream non-LLM decider that holds the final say.

**Axes touched:**

- `agentic_configuration.decision_role` — Who holds authority over the final RM action (`Sole Decider` vs `Pipeline Contributor`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLM-Guided Candidate Generation employs few-shot and chain-of-thought prompting to produce diverse scheduling candidates" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `agentic_configuration.decision_role` = `Sole Decider`

> "the scheduler assigns scores to the valid machines based on these preferences" (§I Introduction)
>
> — [paper-2779](../papers/paper-2779.md), axis `agentic_configuration.decision_role` = `Pipeline Contributor`

##### View `metric-by-autonomy`

- **Type:** `pivot` · **Anchor:** `RQ4.4` · **Shape:** rows: `metric` (multi-select) × cols: `autonomy_level`
- **Spreadsheet tab:** [`metric-by-autonomy`](../spreadsheet.xlsx)

| value                    | Autonomous | Supervised | total |
| ------------------------ | ---------- | ---------- | ----- |
| RM Performance Metric    | 15         | 5          | 20    |
| Agent Performance Metric | 15         | 0          | 15    |

Strong, near-deterministic pattern: all 15 Autonomous papers report Agent Performance Metric (token cost, inference latency, decision accuracy); 0 of the 5 Supervised papers do. Every paper, regardless of autonomy, reports an RM Performance Metric. The vacancy in the Supervised × Agent-Performance cell is the strongest single signal in the corpus and the central evidence for the RQ4.4 governance-gap discussion.

**Axes touched:**

- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).
- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `metric` = `RM Performance Metric + Agent Performance Metric`

> "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations" (§Abstract)
>
> — [paper-2779](../papers/paper-2779.md), axis `metric` = `RM Performance Metric`

### RQ2 — Which classes of resource management decisions are delegated to agentic AI systems, and under what operational conditions?

#### RQ2.1 — Classes of resource management decisions delegated.

Five decision classes are observed: Placement & Offloading (9), Scheduling (7), Scaling (2), Remediation (2), Routing & Slicing (1). The head of the distribution (16 of 20 papers contribute to Placement or Scheduling) reflects the easiest mapping from LLM output to executable action: a placement plan or a schedule is a discrete data structure the agent can emit directly, whereas Remediation and Scaling pipelines additionally need closed-loop telemetry to act on.

##### View `decision-distribution`

- **Type:** `distribution` · **Anchor:** `RQ2.1` · **Shape:** rows: `decision` (multi-select)
- **Spreadsheet tab:** [`decision-distribution`](../spreadsheet.xlsx)

| value                  | count |
| ---------------------- | ----- |
| Placement & Offloading | 9     |
| Scheduling             | 7     |
| Remediation            | 2     |
| Scaling                | 2     |
| Routing & Slicing      | 1     |

Placement & Offloading (9) and Scheduling (7) dominate the corpus: 16 of 20 papers contribute to one of these two classes. Scaling (2), Remediation (2), and Routing & Slicing (1) appear in the long tail; Remediation is uniformly tied to root-cause-analysis + repair pipelines, and Routing & Slicing surfaces only in 6G/network-management work.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Task offloading is a critical EC technique. It transfers tasks from user devices to edge servers" (§Introduction)
>
> — [paper-2936](../papers/paper-2936.md), axis `decision` = `Placement & Offloading`

> "introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `decision` = `Scheduling`

> "the agent identifies likely root causes and selects corrective actions—such as pod rescheduling, scaling, or configuration updates" (§Abstract)
>
> — [paper-1404](../papers/paper-1404.md), axis `decision` = `Remediation`

##### View `infrastructure-by-decision`

- **Type:** `pivot` · **Anchor:** `RQ1.2` · **Shape:** rows: `decision` (multi-select) × cols: `infrastructure`
- **Spreadsheet tab:** [`infrastructure-by-decision`](../spreadsheet.xlsx)

| value                  | Edge-Cloud | Cloud-Only | total |
| ---------------------- | ---------- | ---------- | ----- |
| Placement & Offloading | 6          | 3          | 9     |
| Scheduling             | 2          | 5          | 7     |
| Remediation            | 2          | 0          | 2     |
| Scaling                | 1          | 1          | 2     |
| Routing & Slicing      | 1          | 0          | 1     |

Placement & Offloading skews Edge-Cloud (6 of 9). Scheduling skews Cloud-Only (5 of 7). Remediation and Routing & Slicing appear only in Edge-Cloud or only in Cloud-Only respectively; Scaling is split 1:1.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `infrastructure` — Tier of infrastructure controlled by the agent (`Cloud-Only` vs `Edge-Cloud`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Task offloading is a critical EC technique. It transfers tasks from user devices to edge servers" (§Introduction)
>
> — [paper-2936](../papers/paper-2936.md), axis `decision` = `Placement & Offloading`

> "introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `decision` = `Scheduling`

> "The goal is to allocate each workload w j to a..." (§3 Problem Definition)
>
> — [paper-1644](../papers/paper-1644.md), axis `decision` = `Placement & Offloading`

##### View `decision-by-autonomy`

- **Type:** `pivot` · **Anchor:** `RQ2.2` · **Shape:** rows: `decision` (multi-select) × cols: `autonomy_level`
- **Spreadsheet tab:** [`decision-by-autonomy`](../spreadsheet.xlsx)

| value                  | Autonomous | Supervised | total |
| ---------------------- | ---------- | ---------- | ----- |
| Placement & Offloading | 5          | 4          | 9     |
| Scheduling             | 6          | 1          | 7     |
| Remediation            | 2          | 0          | 2     |
| Scaling                | 2          | 0          | 2     |
| Routing & Slicing      | 1          | 0          | 1     |

Scheduling (6/7), Remediation (2/2), Scaling (2/2), and Routing & Slicing (1/1) are predominantly Autonomous. Placement & Offloading is the only class with substantial Supervised representation (4 of 9), reflecting the intent-/policy-compilation pipelines that emit placement plans for downstream solvers.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLMSched incorporates caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `autonomy_level` = `Autonomous`

> "automating complex architectural and operational decisions, our framework enables adaptive, constraint-aware application deployment" (§I Introduction)
>
> — [paper-1420](../papers/paper-1420.md), axis `autonomy_level` = `Autonomous`

> "We design an intelligent preference-aware retrieval module. It integrates semantic similarity between knowledge entries, contextual queries, and task QoS preferences." (§Introduction (contribution 2))
>
> — [paper-2936](../papers/paper-2936.md), axis `autonomy_level` = `Supervised`

#### RQ2.2 — Operational conditions and autonomy level (advisory/supervised/autonomous).

Autonomous deployments outnumber Supervised 15:5. Across decision classes, Scheduling, Remediation, Scaling, and Routing & Slicing are predominantly Autonomous; Placement & Offloading is the only class with substantial Supervised representation (4 of 9), and that subset coincides with the intent-/policy-compilation pipelines where the LLM emits a placement plan for a downstream non-LLM solver to land.

##### View `autonomy-distribution`

- **Type:** `distribution` · **Anchor:** `RQ2.2` · **Shape:** rows: `autonomy_level` (single-select)
- **Spreadsheet tab:** [`autonomy-distribution`](../spreadsheet.xlsx)

| value      | count |
| ---------- | ----- |
| Autonomous | 15    |
| Supervised | 5     |

Autonomous deployments outnumber Supervised 15:5. The Supervised group concentrates around intent-/policy-translation pipelines (1496, 1680, 2470, 2779, 2936) where a non-LLM component lands the final action; the Autonomous group covers every paper where the LLM emits the executable decision.

**Axes touched:**

- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLMSched incorporates caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `autonomy_level` = `Autonomous`

> "The current prototype is intended as a research artifact to demonstrate the feasibility and is not production-ready." (§I Introduction)
>
> — [paper-2779](../papers/paper-2779.md), axis `autonomy_level` = `Supervised`

##### View `decision-by-autonomy`

- **Type:** `pivot` · **Anchor:** `RQ2.2` · **Shape:** rows: `decision` (multi-select) × cols: `autonomy_level`
- **Spreadsheet tab:** [`decision-by-autonomy`](../spreadsheet.xlsx)

| value                  | Autonomous | Supervised | total |
| ---------------------- | ---------- | ---------- | ----- |
| Placement & Offloading | 5          | 4          | 9     |
| Scheduling             | 6          | 1          | 7     |
| Remediation            | 2          | 0          | 2     |
| Scaling                | 2          | 0          | 2     |
| Routing & Slicing      | 1          | 0          | 1     |

Scheduling (6/7), Remediation (2/2), Scaling (2/2), and Routing & Slicing (1/1) are predominantly Autonomous. Placement & Offloading is the only class with substantial Supervised representation (4 of 9), reflecting the intent-/policy-compilation pipelines that emit placement plans for downstream solvers.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLMSched incorporates caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `autonomy_level` = `Autonomous`

> "automating complex architectural and operational decisions, our framework enables adaptive, constraint-aware application deployment" (§I Introduction)
>
> — [paper-1420](../papers/paper-1420.md), axis `autonomy_level` = `Autonomous`

> "We design an intelligent preference-aware retrieval module. It integrates semantic similarity between knowledge entries, contextual queries, and task QoS preferences." (§Introduction (contribution 2))
>
> — [paper-2936](../papers/paper-2936.md), axis `autonomy_level` = `Supervised`

### RQ3 — What reasoning processes and grounding mechanisms do agentic AI systems employ to translate observed system state into resource management actions?

#### RQ3.1 — Reasoning processes (CoT, ToT, ReAct, planning + reflection, debate, self-consistency).

Prompting dominates (15/20). Iterative Reasoning (4) is the only paradigm that spans all five decision classes, suggesting a thin but broad presence across the corpus. The temporal slice shows Prompting carries across 2024–2026 unchanged; the other three paradigms accumulate on top rather than displace it.

##### View `reasoning-distribution`

- **Type:** `distribution` · **Anchor:** `RQ3.1 (also answers RQ3.2, RQ3.3)` · **Shape:** rows: `reasoning_approach` (multi-select)
- **Spreadsheet tab:** [`reasoning-distribution`](../spreadsheet.xlsx)

| value                | count |
| -------------------- | ----- |
| Prompting            | 15    |
| Iterative Reasoning  | 4     |
| Knowledge Retrieval  | 2     |
| Model Specialization | 2     |

Prompting dominates at 15/20. Iterative Reasoning (4), Knowledge Retrieval (2), and Model Specialization (2) appear, often combined with Prompting in the same paper (multi-select). No paper uses Knowledge Retrieval or Model Specialization in isolation without a prompt-driven outer loop.

**Axes touched:**

- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "few-shot adaptability [23], chain-of-thought reasoning [24], and semantic interpretation of natural language constraints" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `reasoning_approach` = `Prompting`

> "Leveraging an Large Language Model (LLM), the agentic framework can perform reasoning and planning, use tools, manage memory, and collaborate with other agents" (§I Introduction)
>
> — [paper-2723](../papers/paper-2723.md), axis `reasoning_approach` = `Iterative Reasoning`

> "This dataset is then used to fine-tune the LLM via LoRA, enhancing its generalization capability" (§I Introduction)
>
> — [paper-2028](../papers/paper-2028.md), axis `reasoning_approach` = `Prompting + Model Specialization`

##### View `reasoning-by-decision`

- **Type:** `pivot` · **Anchor:** `RQ3.1` · **Shape:** rows: `reasoning_approach` (multi-select) × cols: `decision` (multi-select)
- **Spreadsheet tab:** [`reasoning-by-decision`](../spreadsheet.xlsx)

| value                | Placement & Offloading | Scheduling | Remediation | Scaling | Routing & Slicing | total |
| -------------------- | ---------------------- | ---------- | ----------- | ------- | ----------------- | ----- |
| Prompting            | 7                      | 6          | 1           | 1       | 0                 | 15    |
| Iterative Reasoning  | 1                      | 1          | 1           | 1       | 1                 | 5     |
| Knowledge Retrieval  | 2                      | 0          | 0           | 0       | 0                 | 2     |
| Model Specialization | 1                      | 1          | 0           | 0       | 0                 | 2     |

Prompting is used across every decision class except Routing & Slicing (1 paper, Iterative Reasoning). Iterative Reasoning spans all five classes at low count (1 each). Knowledge Retrieval is observed only in Placement & Offloading. Model Specialization appears once each in Placement and Scheduling.

**Axes touched:**

- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).
- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Using structured prompts, the LLM considered the context of each service (functional type, performance profile, constraints, tags) and recommended an optimal mapping" (§V Use Case)
>
> — [paper-1420](../papers/paper-1420.md), axis `reasoning_approach` = `Prompting`

> "few-shot adaptability [23], chain-of-thought reasoning [24], and semantic interpretation of natural language constraints" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `reasoning_approach` = `Prompting`

> "Influenced by the React framework [14], which interleaving reasoning and acting in a more interactive manner" (§IV (Agent design))
>
> — [paper-1404](../papers/paper-1404.md), axis `reasoning_approach` = `Iterative Reasoning`

##### View `reasoning-temporal`

- **Type:** `temporal` · **Anchor:** `RQ3.1` · **Shape:** rows: `year` × cols: `reasoning_approach` (multi-select)
- **Spreadsheet tab:** [`reasoning-temporal`](../spreadsheet.xlsx)

| value | Prompting | Iterative Reasoning | Knowledge Retrieval | Model Specialization | total |
| ----- | --------- | ------------------- | ------------------- | -------------------- | ----- |
| 2024  | 2         | 0                   | 0                   | 0                    | 2     |
| 2025  | 11        | 3                   | 1                   | 2                    | 17    |
| 2026  | 2         | 1                   | 1                   | 0                    | 4     |

2024 corpus members (2) use Prompting only. 2025 (14) introduces Iterative Reasoning (3), Knowledge Retrieval (1), and Model Specialization (2). 2026 (4) drops one of each into the mix. The Prompting-only baseline persists across years; new reasoning paradigms accumulate on top rather than displace it.

**Axes touched:**

- `year` — Publication year of the paper.
- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "LLMs elegantly bypass this training bottleneck with their powerful zero-shot and few-shot reasoning capabilities" (§I Introduction)
>
> — [paper-1408](../papers/paper-1408.md), axis `reasoning_approach` = `Prompting`

> "Influenced by the React framework [14], which interleaving reasoning and acting in a more interactive manner" (§IV (Agent design))
>
> — [paper-1404](../papers/paper-1404.md), axis `reasoning_approach` = `Iterative Reasoning`

> "FlowMage sends a comprehensive prompt containing (i) a general introduction... (ii) a section detailing the specific information... (iii) a brief directive specifying the desired response format" (§3.1 Prompt Formulation)
>
> — [paper-0930](../papers/paper-0930.md), axis `reasoning_approach` = `Prompting`

#### RQ3.2 — Grounding mechanisms (telemetry, RAG over runbooks/docs, episodic memory, vector DBs, knowledge graphs).

Grounding via external retrieval is rare — only 2 papers ([paper-2936](../papers/paper-2936.md), [paper-2470](../papers/paper-2470.md) per the taxonomy classification) use Knowledge Retrieval, and both appear in Placement & Offloading. No paper uses Knowledge Retrieval in isolation — it always wraps a Prompting outer loop. This is the sub-RQ with the most concentrated coverage (single axis, multi-select), and the data point is the absence as much as the presence.

##### View `reasoning-distribution`

- **Type:** `distribution` · **Anchor:** `RQ3.1 (also answers RQ3.2, RQ3.3)` · **Shape:** rows: `reasoning_approach` (multi-select)
- **Spreadsheet tab:** [`reasoning-distribution`](../spreadsheet.xlsx)

| value                | count |
| -------------------- | ----- |
| Prompting            | 15    |
| Iterative Reasoning  | 4     |
| Knowledge Retrieval  | 2     |
| Model Specialization | 2     |

Prompting dominates at 15/20. Iterative Reasoning (4), Knowledge Retrieval (2), and Model Specialization (2) appear, often combined with Prompting in the same paper (multi-select). No paper uses Knowledge Retrieval or Model Specialization in isolation without a prompt-driven outer loop.

**Axes touched:**

- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "few-shot adaptability [23], chain-of-thought reasoning [24], and semantic interpretation of natural language constraints" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `reasoning_approach` = `Prompting`

> "Leveraging an Large Language Model (LLM), the agentic framework can perform reasoning and planning, use tools, manage memory, and collaborate with other agents" (§I Introduction)
>
> — [paper-2723](../papers/paper-2723.md), axis `reasoning_approach` = `Iterative Reasoning`

> "This dataset is then used to fine-tune the LLM via LoRA, enhancing its generalization capability" (§I Introduction)
>
> — [paper-2028](../papers/paper-2028.md), axis `reasoning_approach` = `Prompting + Model Specialization`

#### RQ3.3 — Domain knowledge incorporation (fine-tuning, structured prompting, few-shot, infrastructure ontologies).

Domain knowledge entered via fine-tuning or adapters (Model Specialization) appears in only 2 papers, and only in Placement & Offloading or Scheduling. The dominant route to domain knowledge in this corpus remains structured prompting plus, in two cases, retrieval — no paper combines all three (specialization + retrieval + prompting).

##### View `reasoning-distribution`

- **Type:** `distribution` · **Anchor:** `RQ3.1 (also answers RQ3.2, RQ3.3)` · **Shape:** rows: `reasoning_approach` (multi-select)
- **Spreadsheet tab:** [`reasoning-distribution`](../spreadsheet.xlsx)

| value                | count |
| -------------------- | ----- |
| Prompting            | 15    |
| Iterative Reasoning  | 4     |
| Knowledge Retrieval  | 2     |
| Model Specialization | 2     |

Prompting dominates at 15/20. Iterative Reasoning (4), Knowledge Retrieval (2), and Model Specialization (2) appear, often combined with Prompting in the same paper (multi-select). No paper uses Knowledge Retrieval or Model Specialization in isolation without a prompt-driven outer loop.

**Axes touched:**

- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "few-shot adaptability [23], chain-of-thought reasoning [24], and semantic interpretation of natural language constraints" (§I Introduction)
>
> — [paper-2556](../papers/paper-2556.md), axis `reasoning_approach` = `Prompting`

> "Leveraging an Large Language Model (LLM), the agentic framework can perform reasoning and planning, use tools, manage memory, and collaborate with other agents" (§I Introduction)
>
> — [paper-2723](../papers/paper-2723.md), axis `reasoning_approach` = `Iterative Reasoning`

> "This dataset is then used to fine-tune the LLM via LoRA, enhancing its generalization capability" (§I Introduction)
>
> — [paper-2028](../papers/paper-2028.md), axis `reasoning_approach` = `Prompting + Model Specialization`

### RQ4 — How is the behavior of agentic AI systems for resource management evaluated?

#### RQ4.1 — Evaluation methodologies and environments (simulation, real testbed, production, synthetic benchmarks, real traces).

Simulation (13) outnumbers Practical Testbed (7), but the split is not uniform: Scheduling is evaluated exclusively in Simulation (7/7), while Remediation, Scaling, and Routing & Slicing are exclusively Practical Testbed. Placement & Offloading mixes (6 Sim / 3 Testbed). The pattern suggests evaluation venue follows infrastructure tooling maturity (simulators exist for scheduling, less so for remediation pipelines) rather than algorithmic novelty.

##### View `evaluation-distribution`

- **Type:** `distribution` · **Anchor:** `RQ4.1` · **Shape:** rows: `evaluation_method` (single-select)
- **Spreadsheet tab:** [`evaluation-distribution`](../spreadsheet.xlsx)

| value             | count |
| ----------------- | ----- |
| Simulation        | 13    |
| Practical Testbed | 7     |

Simulation (13) is more common than Practical Testbed (7). The split is not random: Scheduling work uses simulation exclusively, while Remediation, Scaling, and Routing & Slicing use real testbeds exclusively (see `evaluation-by-decision`).

**Axes touched:**

- `evaluation_method` — Empirical environment (`Simulation` vs `Practical Testbed`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Hardware Configuration: Experiments run on a simulated" (§V-A Experiment Setup)
>
> — [paper-2556](../papers/paper-2556.md), axis `evaluation_method` = `Simulation`

> "All experiments were conducted on the FABRIC testbed [40] using an OpenStack-based compute node" (§IV-B Infrastructure and Compute Platform)
>
> — [paper-2723](../papers/paper-2723.md), axis `evaluation_method` = `Practical Testbed`

##### View `evaluation-by-decision`

- **Type:** `pivot` · **Anchor:** `RQ4.1` · **Shape:** rows: `decision` (multi-select) × cols: `evaluation_method`
- **Spreadsheet tab:** [`evaluation-by-decision`](../spreadsheet.xlsx)

| value                  | Simulation | Practical Testbed | total |
| ---------------------- | ---------- | ----------------- | ----- |
| Placement & Offloading | 6          | 3                 | 9     |
| Scheduling             | 7          | 0                 | 7     |
| Remediation            | 0          | 2                 | 2     |
| Scaling                | 0          | 2                 | 2     |
| Routing & Slicing      | 0          | 1                 | 1     |

Sharp axis-aligned split: Scheduling (7/7) is evaluated exclusively in Simulation; Remediation (2/2), Scaling (2/2), and Routing & Slicing (1/1) are exclusively Practical Testbed. Placement & Offloading mixes (6 Sim / 3 Testbed). The pattern suggests that evaluation venue follows the maturity of the underlying infrastructure tooling rather than the algorithmic novelty.

**Axes touched:**

- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `evaluation_method` — Empirical environment (`Simulation` vs `Practical Testbed`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "Hardware Configuration: Experiments run on a simulated" (§V-A Experiment Setup)
>
> — [paper-2556](../papers/paper-2556.md), axis `evaluation_method` = `Simulation`

> "a custom simulation environment is established" (§Performance Evaluation — Experimental Setup)
>
> — [paper-2936](../papers/paper-2936.md), axis `evaluation_method` = `Simulation`

> "the experimental setup of the IBSM system consists of a client, server, and large-scale multi-cloud exchange platform" (§IV-A Experimentation setup)
>
> — [paper-2470](../papers/paper-2470.md), axis `evaluation_method` = `Practical Testbed`

#### RQ4.2 — Resource-management performance metrics (latency, cost, energy, SLA, utilization, throughput).

Every paper (20/20) reports at least one resource-management performance metric (latency, throughput, completion time, utilization, SLA violations, energy, cost). The distribution is uniform — there is no included paper without an RM-side outcome metric, which is structurally guaranteed by Q2 of the quality assessment.

##### View `metric-distribution`

- **Type:** `distribution` · **Anchor:** `RQ4.2 (also answers RQ4.3, RQ4.4)` · **Shape:** rows: `metric` (multi-select)
- **Spreadsheet tab:** [`metric-distribution`](../spreadsheet.xlsx)

| value                    | count |
| ------------------------ | ----- |
| RM Performance Metric    | 20    |
| Agent Performance Metric | 15    |

RM Performance Metric is reported by every paper (20/20). Agent Performance Metric is reported by 15/20 — exactly the Autonomous subset; the 5 Supervised papers do not surface agent-side metrics (token cost, inference latency, decision accuracy) at all (see `metric-by-autonomy`).

**Axes touched:**

- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `metric` = `RM Performance Metric + Agent Performance Metric`

> "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations" (§Abstract)
>
> — [paper-2779](../papers/paper-2779.md), axis `metric` = `RM Performance Metric`

#### RQ4.3 — Agent/inference overhead metrics (token usage, inference latency, monetary cost per decision, model size/footprint, agent-loop throughput).

Agent-side overhead metrics (token usage, inference latency, decision accuracy, monetary cost per decision) are reported by 15/20 papers — exactly the Autonomous subset. The agent-overhead reporting rate is 100% within Autonomous and 0% within Supervised; the Supervised papers do not surface any agent-side metric, even when the LLM call is the most expensive step of the pipeline.

##### View `metric-distribution`

- **Type:** `distribution` · **Anchor:** `RQ4.2 (also answers RQ4.3, RQ4.4)` · **Shape:** rows: `metric` (multi-select)
- **Spreadsheet tab:** [`metric-distribution`](../spreadsheet.xlsx)

| value                    | count |
| ------------------------ | ----- |
| RM Performance Metric    | 20    |
| Agent Performance Metric | 15    |

RM Performance Metric is reported by every paper (20/20). Agent Performance Metric is reported by 15/20 — exactly the Autonomous subset; the 5 Supervised papers do not surface agent-side metrics (token cost, inference latency, decision accuracy) at all (see `metric-by-autonomy`).

**Axes touched:**

- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `metric` = `RM Performance Metric + Agent Performance Metric`

> "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations" (§Abstract)
>
> — [paper-2779](../papers/paper-2779.md), axis `metric` = `RM Performance Metric`

#### RQ4.4 — Safety and governance metrics (rate of unsafe/invalid actions, frequency of human intervention, audit coverage, policy compliance).

Safety/governance metrics live inside `Agent Performance Metric` (rate of unsafe actions, audit-trace coverage, policy compliance). The `metric-by-autonomy` view shows zero Supervised papers report this family, while 15/15 Autonomous papers do. The vacancy is the strongest single signal in the corpus and motivates the stage 09 governance-gap discussion.

##### View `metric-distribution`

- **Type:** `distribution` · **Anchor:** `RQ4.2 (also answers RQ4.3, RQ4.4)` · **Shape:** rows: `metric` (multi-select)
- **Spreadsheet tab:** [`metric-distribution`](../spreadsheet.xlsx)

| value                    | count |
| ------------------------ | ----- |
| RM Performance Metric    | 20    |
| Agent Performance Metric | 15    |

RM Performance Metric is reported by every paper (20/20). Agent Performance Metric is reported by 15/20 — exactly the Autonomous subset; the 5 Supervised papers do not surface agent-side metrics (token cost, inference latency, decision accuracy) at all (see `metric-by-autonomy`).

**Axes touched:**

- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `metric` = `RM Performance Metric + Agent Performance Metric`

> "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations" (§Abstract)
>
> — [paper-2779](../papers/paper-2779.md), axis `metric` = `RM Performance Metric`

##### View `metric-by-autonomy`

- **Type:** `pivot` · **Anchor:** `RQ4.4` · **Shape:** rows: `metric` (multi-select) × cols: `autonomy_level`
- **Spreadsheet tab:** [`metric-by-autonomy`](../spreadsheet.xlsx)

| value                    | Autonomous | Supervised | total |
| ------------------------ | ---------- | ---------- | ----- |
| RM Performance Metric    | 15         | 5          | 20    |
| Agent Performance Metric | 15         | 0          | 15    |

Strong, near-deterministic pattern: all 15 Autonomous papers report Agent Performance Metric (token cost, inference latency, decision accuracy); 0 of the 5 Supervised papers do. Every paper, regardless of autonomy, reports an RM Performance Metric. The vacancy in the Supervised × Agent-Performance cell is the strongest single signal in the corpus and the central evidence for the RQ4.4 governance-gap discussion.

**Axes touched:**

- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).
- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).

**Contributing papers:**

- [paper-2556](../papers/paper-2556.md) — 2026 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
- [paper-2723](../papers/paper-2723.md) — 2026 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks
- [paper-2779](../papers/paper-2779.md) — 2026 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
- [paper-2936](../papers/paper-2936.md) — 2026 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
- [paper-1404](../papers/paper-1404.md) — 2025 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control
- [paper-1408](../papers/paper-1408.md) — 2025 — Intelligent Kubernetes Scheduling with Large Language Models
- [paper-1420](../papers/paper-1420.md) — 2025 — Generative AI for Optimizing Service Mapping in the Edge-Cloud
- [paper-1496](../papers/paper-1496.md) — 2025 — Investigating Neurosymbolic AI for Intent-based Service Management
- [paper-1563](../papers/paper-1563.md) — 2025 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
- [paper-1593](../papers/paper-1593.md) — 2025 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
- …and 10 more (full list in `spreadsheet.xlsx`, tab `00-included`).

**Representative evidence:**

> "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" (§Abstract)
>
> — [paper-2556](../papers/paper-2556.md), axis `metric` = `RM Performance Metric + Agent Performance Metric`

> "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations" (§Abstract)
>
> — [paper-2779](../papers/paper-2779.md), axis `metric` = `RM Performance Metric`

### RQ5 — What open challenges, unresolved tensions, and promising future directions emerge from the synthesis of the included literature?

#### RQ5.1 — Unresolved methodological and technical tensions (inference cost vs. decision latency, hallucination in critical environments, transferability across infrastructures).

Flagged at stage 07 as a corpus-level synthesis question and intentionally not encoded as a per-paper axis (see [`CLAUDE.md §8`](../CLAUDE.md)). The synthesis below is grounded in the locked views.

**Unresolved tensions surfaced by the views:**

- **Inference cost vs. decision latency.** Agent Performance Metric is reported by 15/15 Autonomous papers and 0/5 Supervised papers (see [`metric-by-autonomy`](#view-metric-by-autonomy)). The Autonomous subset reports token usage / inference latency / cost-per-decision — the Supervised subset does not. The tension is therefore visible only in one half of the corpus; cross-paper comparison of agent-side overhead remains structurally hard.
- **Hallucination in critical environments.** No paper in the corpus reports a quantitative measure of unsafe-action rate that is comparable across systems. The `Pipeline Contributor` design (6/20) is the structural workaround — a downstream non-LLM component vetoes hallucinated actions before they reach infrastructure.
- **Transferability across infrastructures.** The clean axis-aligned split in [`evaluation-by-decision`](#view-evaluation-by-decision) — Scheduling exclusively Simulation, Remediation/Scaling/Routing exclusively Practical Testbed — suggests that the choice of evaluation venue (and therefore the transferability claim) is driven by the maturity of the supporting tooling, not by the agent design.

#### RQ5.2 — Governance, accountability, and auditability gaps (decision traceability, responsibility attribution, regulatory requirements, explainability).

Flagged at stage 07 as a corpus-level synthesis question and intentionally not encoded as a per-paper axis (see [`CLAUDE.md §8`](../CLAUDE.md)). The synthesis below is grounded in the locked views.

**Governance, accountability, and auditability gaps surfaced by the views:**

- **The `Supervised × Agent-Performance` vacancy.** All five Supervised papers omit agent-side metrics (see [`metric-by-autonomy`](#view-metric-by-autonomy)). When a human-in-the-loop or rule-based gate is the safety mechanism, the system as evaluated provides no quantitative trace of the agent's behavior — audit coverage, decision traceability, and policy-compliance rate are not reported.
- **The empty `Pipeline Contributor × Multi-Agent` cell** in [`agentic-config-cross`](#view-agentic-config-cross). The combination of a multi-agent reasoning loop with a downstream non-LLM decider is an open design space — the absence is reported as a research opportunity for systems that want auditable multi-agent reasoning without ceding the final action to an LLM.
- **Explainability is structurally optional.** Only one paper ([paper-1947](../papers/paper-1947.md)) treats explainability as a first-class concern by combining XAI with LLMs for zero-touch network and service management. The rest of the corpus treats it implicitly through Pipeline Contributor designs or omits it.

## Taxonomy reference

The full taxonomy — origin, seed axes, value tables, code book, iteration history, and per-axis adversarial-mode flags — lives in [`CLAUDE.md §8`](../CLAUDE.md). Quick reference:

- `infrastructure` — Tier of infrastructure controlled by the agent (`Cloud-Only` vs `Edge-Cloud`).
- `decision` — Class(es) of resource-management decision delegated to the agent (`Scheduling`, `Placement & Offloading`, `Scaling`, `Routing & Slicing`, `Remediation`).
- `agentic_configuration.decision_role` — Who holds authority over the final RM action (`Sole Decider` vs `Pipeline Contributor`).
- `agentic_configuration.coordination_topology` — How many LLM-agents coordinate inside the loop (`Single Agent` vs `Multi-Agent`).
- `reasoning_approach` — Reasoning/grounding mechanism (`Prompting`, `Iterative Reasoning`, `Knowledge Retrieval`, `Model Specialization`).
- `autonomy_level` — Authority the agent holds over the action that reaches the system (`Supervised` vs `Autonomous`).
- `metric` — Families of metrics reported (`RM Performance Metric` vs `Agent Performance Metric`).
- `evaluation_method` — Empirical environment (`Simulation` vs `Practical Testbed`).

Notation: ⋆ marks single-select axes (one value per paper); ▲ marks multi-select axes (one or more values per paper). The taxonomy is **faceted** — every included paper classifies on every axis with ≥ MED confidence (no orphan permitted). The full code book with borderline-case definitions is in [`CLAUDE.md §8.2`](../CLAUDE.md).

Per-paper classifications (Phase 07b blocks with verbatim evidence and neighbor-not-chosen rationale) live in each [`papers/paper-NNNN.md` `## 07 — Taxonomy`](../papers/) block.

## How to read the spreadsheet

`spreadsheet.xlsx` is the canonical, sortable, filterable form of the corpus. The tab layout is:

- **`00-included`** — one row per included paper, with all 8 taxonomy cells, the year, the venue, the DOI, and a clickable link to `papers/paper-NNNN.md`.
- **One tab per analysis view** (16 tabs, named exactly as the `view` field in `stages/08-analysis.md`). Each tab is the pivot or distribution table for that view; cells reference the contributing papers.
- **Screening tabs** (`04-title`, `05-abstract`, `06-full-text`) — proposed/final decision per paper, with bolded keywords in the rich-text cells and red/green background fill on the ID and Title columns (Excluded rows first, then Included; within each block sorted by sub-agent disagreement descending). The formatting spec lives in [`protocols/spreadsheet-formatting.md`](../protocols/spreadsheet-formatting.md).

To trace a finding in this report back to its evidence:

1. From the report, click the view name (e.g., [`metric-by-autonomy`](../spreadsheet.xlsx)) to open the corresponding tab.
2. From the tab, follow the per-paper IDs to the relevant `papers/paper-NNNN.md`.
3. In the per-paper file, [`## 07 — Taxonomy`](#) holds the verbatim quote and `§` location for every axis cell; [`## 08 — Analysis contributions`](#) lists exactly which views the paper feeds.

## Reproducibility

To regenerate the materialized artifacts of this review from the locked protocol and corpus:

```bash
# Pass-1 deterministic classifier (per stage)
uv run scripts/deterministic_classifier.py --stage title
uv run scripts/deterministic_classifier.py --stage abstract
uv run scripts/deterministic_classifier.py --stage full-text

# Materialize the spreadsheet from per-paper markdown + view specs
uv run scripts/build_spreadsheet.py

# Regenerate this report
# (idempotent — re-runs of /rapid-review:07-report overwrite report/index.md)
```

Locked-artifact hashes at report-generation time:

- `protocols/screening.yaml` — `sha256:73b4d8ce8fca6ebab639f388dfdc7595ec3728c0249fe556f6bb1231e32d4514`
- `protocols/classifier-config.json` — `sha256:f4d1f37325cb92dfc49c6f010e075eaa8d905b10d540ef21cb18b4a99cc1ffdc`
- `protocols/classifier-config-fulltext.json` — `sha256:9d48689fe2361684b96377c428d92323eb7ec1d11de413596d0b2833e40efe8c`

Corpus size at lock: 20 included papers (`status.06-full-text-screening == include`), all classified along 7 taxonomy axes, all contributing to ≥1 of 16 analysis views.

Source-of-truth references for downstream manuscript work:

- Protocol: [`CLAUDE.md`](../CLAUDE.md) and [`protocols/screening.yaml`](../protocols/screening.yaml).
- Taxonomy: [`CLAUDE.md §8`](../CLAUDE.md) and [`stages/07-taxonomy-development.md`](../stages/07-taxonomy-development.md).
- Analysis: [`stages/08-analysis.md`](../stages/08-analysis.md) and [`spreadsheet.xlsx`](../spreadsheet.xlsx).
- Per-paper evidence: [`papers/paper-NNNN.md`](../papers/) (`§07` for taxonomy quotes, `§08` for view contributions).
