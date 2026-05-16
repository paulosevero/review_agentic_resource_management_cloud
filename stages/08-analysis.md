# Stage 08 — Analysis

This stage projects the locked corpus (20 included papers, 7-axis taxonomy from §8) into views that answer the protocol's RQs and sub-RQs. Every view declares an `rq_anchor` so an empty cell or collapsing dimension is traceable to a specific question.

The corpus is small (n=20) and the taxonomy is faceted (some axes are multi-select). View choices favor density over breadth: distributions and 2-axis pivots before deeper crosses.

## Coverage of the protocol

| RQ / sub-RQ | Status | Views                                                                         |
| ----------- | ------ | ----------------------------------------------------------------------------- |
| RQ1.1       | view   | `agent-coordination-distribution`, `agentic-config-cross`                     |
| RQ1.2       | view   | `infrastructure-distribution`, `infrastructure-by-decision`                   |
| RQ1.3       | view   | `decision-role-distribution`, `metric-by-autonomy`                            |
| RQ2.1       | view   | `decision-distribution`, `infrastructure-by-decision`, `decision-by-autonomy` |
| RQ2.2       | view   | `autonomy-distribution`, `decision-by-autonomy`                               |
| RQ3.1       | view   | `reasoning-distribution`, `reasoning-by-decision`, `reasoning-temporal`       |
| RQ3.2       | view   | `reasoning-distribution` (axis consolidates RQ3.1+3.2+3.3 per §8.1)           |
| RQ3.3       | view   | `reasoning-distribution` (idem)                                               |
| RQ4.1       | view   | `evaluation-distribution`, `evaluation-by-decision`                           |
| RQ4.2       | view   | `metric-distribution`                                                         |
| RQ4.3       | view   | `metric-distribution` (axis consolidates RQ4.2+4.3+4.4 per §8.1)              |
| RQ4.4       | view   | `metric-distribution`, `metric-by-autonomy`                                   |
| RQ5.1       | synth  | corpus-level synthesis at stage 09 — not encoded as per-paper view            |
| RQ5.2       | synth  | corpus-level synthesis at stage 09 — not encoded as per-paper view            |
| RQ (cross)  | view   | `temporal-included`                                                           |

`RQ5.1` and `RQ5.2` were flagged at stage 07 as corpus-level synthesis questions and are intentionally not encoded as per-paper axes (CLAUDE.md §8). They are addressed in the final report.

## Views plan

Below: one fenced YAML block per view, in the order they will be materialized.

### 1. `decision-distribution` — what classes of resource-management decisions are delegated?

```yaml
view: decision-distribution
type: distribution
rq_anchor: RQ2.1
rows: decision
cols: null
notes: |
  Multi-select axis. Each paper may contribute to several rows.
  Expected shape: 5 rows (Scheduling, Placement & Offloading, Scaling,
  Routing & Slicing, Remediation), total > 20 (multi-counted).
```

### 2. `autonomy-distribution` — what level of autonomy is granted to the agent?

```yaml
view: autonomy-distribution
type: distribution
rq_anchor: RQ2.2
rows: autonomy_level
cols: null
notes: |
  Single-select. Expected shape: 2 rows (Supervised, Autonomous);
  Advisory was dropped at stage 07 (empirically empty).
```

### 3. `infrastructure-distribution` — which infrastructure tier does the agent control?

```yaml
view: infrastructure-distribution
type: distribution
rq_anchor: RQ1.2
rows: infrastructure
cols: null
notes: |
  Single-select. Expected shape: 2 rows (Cloud-Only, Edge-Cloud).
```

### 4. `reasoning-distribution` — which reasoning and grounding mechanisms are used?

```yaml
view: reasoning-distribution
type: distribution
rq_anchor: RQ3.1
rows: reasoning_approach
cols: null
notes: |
  Multi-select. Axis consolidates seed sub-RQs RQ3.1+RQ3.2+RQ3.3
  (reasoning processes, grounding, domain knowledge). Anchor on RQ3.1
  by convention; the same view also answers RQ3.2 and RQ3.3.
  Expected shape: 4 rows (Prompting, Iterative Reasoning,
  Knowledge Retrieval, Model Specialization).
```

### 5. `evaluation-distribution` — what empirical environment is used?

```yaml
view: evaluation-distribution
type: distribution
rq_anchor: RQ4.1
rows: evaluation_method
cols: null
notes: |
  Single-select. Expected shape: 2 rows (Simulation, Practical Testbed).
```

### 6. `metric-distribution` — which families of metrics are reported?

```yaml
view: metric-distribution
type: distribution
rq_anchor: RQ4.2
rows: metric
cols: null
notes: |
  Multi-select. Axis consolidates seed sub-RQs RQ4.2+RQ4.3+RQ4.4
  (RM performance, agent overhead, safety/governance). Every paper
  contributes ≥1 row (RM Performance Metric). Expected shape: 2 rows.
```

### 7. `agent-coordination-distribution` — single-agent vs multi-agent topology

```yaml
view: agent-coordination-distribution
type: distribution
rq_anchor: RQ1.1
rows: agentic_configuration.coordination_topology
cols: null
notes: |
  Facet of agentic_configuration. Expected shape: 2 rows
  (Single Agent, Multi-Agent).
```

### 8. `decision-role-distribution` — who holds the final say over the RM action

```yaml
view: decision-role-distribution
type: distribution
rq_anchor: RQ1.3
rows: agentic_configuration.decision_role
cols: null
notes: |
  Facet of agentic_configuration. Anchored at RQ1.3 because the
  Sole Decider / Pipeline Contributor split is the structural form
  of the guardrail boundary (who lands the action).
  Expected shape: 2 rows (Sole Decider, Pipeline Contributor).
```

### 9. `agentic-config-cross` — decision_role × coordination_topology (the 2×2 with the empirically empty cell)

```yaml
view: agentic-config-cross
type: pivot
rq_anchor: RQ1.1
rows: agentic_configuration.decision_role
cols: agentic_configuration.coordination_topology
notes: |
  Reports the 2×2 cross-product of the two facets. The cell
  Pipeline-Contributor × Multi-Agent is expected to be empty per
  the stage 07 lock; the view confirms the empty cell on the
  current corpus and feeds the research-opportunity discussion
  for stage 09.
```

### 10. `infrastructure-by-decision` — where each decision class operates (cloud vs continuum)

```yaml
view: infrastructure-by-decision
type: pivot
rq_anchor: RQ1.2
rows: decision
cols: infrastructure
notes: |
  Rows are multi-select (a paper can be in several rows). Anchors
  on RQ1.2 (coupling to infrastructure) because the cross reveals
  whether certain decision classes only appear in one tier.
```

### 11. `decision-by-autonomy` — operational autonomy by decision class

```yaml
view: decision-by-autonomy
type: pivot
rq_anchor: RQ2.2
rows: decision
cols: autonomy_level
notes: |
  Rows multi-select. Reveals whether the agent is more often
  trusted to act autonomously for some decision classes than for
  others (e.g., Remediation under HITL vs Scheduling autonomous).
```

### 12. `reasoning-by-decision` — which reasoning mode is used for which decision

```yaml
view: reasoning-by-decision
type: pivot
rq_anchor: RQ3.1
rows: reasoning_approach
cols: decision
notes: |
  Both axes multi-select. Reveals the mapping between reasoning
  paradigm and the kind of resource-management action it produces.
```

### 13. `evaluation-by-decision` — which decision classes are evaluated in simulation vs real testbeds

```yaml
view: evaluation-by-decision
type: pivot
rq_anchor: RQ4.1
rows: decision
cols: evaluation_method
notes: |
  Rows multi-select. Reveals whether some classes (e.g., Remediation)
  lean toward Practical Testbed while others (e.g., Placement) lean
  toward Simulation, which informs the reproducibility discussion.
```

### 14. `metric-by-autonomy` — do supervised systems report different metric families than autonomous ones?

```yaml
view: metric-by-autonomy
type: pivot
rq_anchor: RQ4.4
rows: metric
cols: autonomy_level
notes: |
  Anchored at RQ4.4 because safety/governance metrics — when they
  exist — live inside `metric.Agent Performance Metric`. The cross
  with `autonomy_level` exposes whether Supervised systems report
  agent-side metrics at the same rate as Autonomous ones.
```

### 15. `reasoning-temporal` — chronology of reasoning approaches in the corpus

```yaml
view: reasoning-temporal
type: temporal
rq_anchor: RQ3.1
rows: year
cols: reasoning_approach
notes: |
  Year × reasoning_approach. Cols multi-select. Reveals whether
  Iterative Reasoning / Knowledge Retrieval / Model Specialization
  appear later in the timeline than Prompting (which dominates).
```

### 16. `temporal-included` — top-level chronology of included papers

```yaml
view: temporal-included
type: temporal
rq_anchor: RQ1
rows: year
cols: null
notes: |
  Cross-cutting view. Anchored at RQ1 (the architecture RQ) as the
  most general per-paper RQ; the count is a sanity-check of the
  field's emergence (2024 onset).
```

## Materialization log

### `decision-by-autonomy`

- **Type:** `pivot` · **rq_anchor:** `RQ2.2` · **rows:** `decision` · **cols:** `autonomy_level`
- **Coverage:** 20/20 papers contribute (21 cell entries; multi-counted for multi-select axes).

| value | Autonomous | Supervised | total |
| --- | --- | --- | --- |
| Placement & Offloading | 5 | 4 | 9 |
| Scheduling | 6 | 1 | 7 |
| Remediation | 2 | 0 | 2 |
| Scaling | 2 | 0 | 2 |
| Routing & Slicing | 1 | 0 | 1 |

Scheduling (6/7), Remediation (2/2), Scaling (2/2), and Routing & Slicing (1/1) are predominantly Autonomous. Placement & Offloading is the only class with substantial Supervised representation (4 of 9), reflecting the intent-/policy-compilation pipelines that emit placement plans for downstream solvers.

### `infrastructure-by-decision`

- **Type:** `pivot` · **rq_anchor:** `RQ1.2` · **rows:** `decision` · **cols:** `infrastructure`
- **Coverage:** 20/20 papers contribute (21 cell entries; multi-counted for multi-select axes).

| value | Edge-Cloud | Cloud-Only | total |
| --- | --- | --- | --- |
| Placement & Offloading | 6 | 3 | 9 |
| Scheduling | 2 | 5 | 7 |
| Remediation | 2 | 0 | 2 |
| Scaling | 1 | 1 | 2 |
| Routing & Slicing | 1 | 0 | 1 |

Placement & Offloading skews Edge-Cloud (6 of 9). Scheduling skews Cloud-Only (5 of 7). Remediation and Routing & Slicing appear only in Edge-Cloud or only in Cloud-Only respectively; Scaling is split 1:1.

### `agentic-config-cross`

- **Type:** `pivot` · **rq_anchor:** `RQ1.1` · **rows:** `agentic_configuration.decision_role` · **cols:** `agentic_configuration.coordination_topology`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | Single Agent | Multi-Agent | total |
| --- | --- | --- | --- |
| Sole Decider | 12 | 2 | 14 |
| Pipeline Contributor | 6 | 0 | 6 |

Three of the four cells of the 2×2 are populated; `Pipeline Contributor × Multi-Agent` is empty in the current corpus. This vacancy is reported as a research-opportunity observation, not a coverage gap of the taxonomy (the two facets remain independently valid). The dominant configuration is `Sole Decider × Single Agent` (12/20).

### `decision-role-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ1.3` · **rows:** `agentic_configuration.decision_role` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Sole Decider | 14 |
| Pipeline Contributor | 6 |

Sole Decider outnumbers Pipeline Contributor 14:6. The Pipeline Contributor group is structurally the same set as the Supervised autonomy group plus paper-1563 (GP hyper-heuristic) — i.e., the LLM feeds a downstream non-LLM decider that holds the final say.

### `agent-coordination-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ1.1` · **rows:** `agentic_configuration.coordination_topology` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Single Agent | 18 |
| Multi-Agent | 2 |

Single-agent topology dominates (18/20). The two Multi-Agent papers (1991, 2362) both adopt Iterative Reasoning, hinting that multi-agent is currently coupled with explicit planning/reflection loops rather than one-shot prompting.

### `metric-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ4.2` · **rows:** `metric` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (35 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| RM Performance Metric | 20 |
| Agent Performance Metric | 15 |

RM Performance Metric is reported by every paper (20/20). Agent Performance Metric is reported by 15/20 — exactly the Autonomous subset; the 5 Supervised papers do not surface agent-side metrics (token cost, inference latency, decision accuracy) at all (see `metric-by-autonomy`).

### `evaluation-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ4.1` · **rows:** `evaluation_method` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Simulation | 13 |
| Practical Testbed | 7 |

Simulation (13) is more common than Practical Testbed (7). The split is not random: Scheduling work uses simulation exclusively, while Remediation, Scaling, and Routing & Slicing use real testbeds exclusively (see `evaluation-by-decision`).

### `reasoning-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ3.1` · **rows:** `reasoning_approach` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (23 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Prompting | 15 |
| Iterative Reasoning | 4 |
| Knowledge Retrieval | 2 |
| Model Specialization | 2 |

Prompting dominates at 15/20. Iterative Reasoning (4), Knowledge Retrieval (2), and Model Specialization (2) appear, often combined with Prompting in the same paper (multi-select). No paper uses Knowledge Retrieval or Model Specialization in isolation without a prompt-driven outer loop.

### `infrastructure-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ1.2` · **rows:** `infrastructure` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Edge-Cloud | 11 |
| Cloud-Only | 9 |

Edge-Cloud accounts for 11 of 20 papers vs 9 for Cloud-Only — close to parity. Every paper that mentions an edge tier also reaches a cloud tier (per §8.2 code-book definition), so a pure edge-only configuration is empirically absent.

### `autonomy-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ2.2` · **rows:** `autonomy_level` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (20 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Autonomous | 15 |
| Supervised | 5 |

Autonomous deployments outnumber Supervised 15:5. The Supervised group concentrates around intent-/policy-translation pipelines (1496, 1680, 2470, 2779, 2936) where a non-LLM component lands the final action; the Autonomous group includes every paper where the LLM emits the executable decision.

### `decision-distribution`

- **Type:** `distribution` · **rq_anchor:** `RQ2.1` · **rows:** `decision` · **cols:** `—`
- **Coverage:** 20/20 papers contribute (21 cell entries; multi-counted for multi-select axes).

| value | count |
| --- | --- |
| Placement & Offloading | 9 |
| Scheduling | 7 |
| Remediation | 2 |
| Scaling | 2 |
| Routing & Slicing | 1 |

Placement & Offloading and Scheduling dominate (9 + 7 of 21 multi-counted contributions, 16 of the 20 papers contribute to one of these two classes). Scaling, Routing & Slicing, and Remediation appear in 5 papers combined; Remediation is uniformly tied to root-cause-analysis + repair pipelines, and Routing & Slicing only surfaces in 6G/network-management work.

(One entry per view as it is committed; populated below as the views are written.)

## Checkpoints

(None opened yet. Any empty/near-empty view that surfaces during materialization is recorded here per the skill's diagnostic-empty-view path.)
