# Stage 07 — Taxonomy Development

## Iteration 1 — Origin choice and seed axes

- **Date:** 2026-05-15
- **Commit:** `[07] origin: hybrid`
- **Decision:** `taxonomy.origin = hybrid`. Twelve axes seeded deductively from sub-RQs RQ1.1–RQ4.4. RQ5.1/RQ5.2 excluded (corpus-level synthesis, not per-paper labels).
- **Adversarial mode:** off.

## Iteration 1 (consolidated) — 7-axis taxonomy

- **Date:** 2026-05-15
- **Commit:** `[07] iteration-1: 7-axis taxonomy consolidated`
- **Outcome:** Twelve seed axes consolidated to seven faceted axes via user dialog and empirical validation against the 20 included papers.

Final axes (see CLAUDE.md §8.1/§8.2 for full code book):

| #   | axis                    | type | values                                                                                                                                     |
| --- | ----------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | `infrastructure`        | ⋆    | Cloud / Edge / Continuum                                                                                                                   |
| 2   | `decision`              | ▲    | Scheduling / Placement & Offloading / Scaling / Routing & Slicing / Remediation                                                            |
| 3   | `agentic_configuration` | ⋆    | Sole Decider, Single Agent / Sole Decider, Multi-Agent / Pipeline Contributor, Single Agent / Pipeline Contributor, Multi-Agent (reserved) |
| 4   | `reasoning_approach`    | ▲    | Prompting / Iterative Reasoning / Knowledge Retrieval / Model Specialization                                                               |
| 5   | `autonomy_level`        | ⋆    | Advisory / Supervised / Autonomous                                                                                                         |
| 6   | `metric`                | ▲    | RM Performance Metric / Agent Performance Metric                                                                                           |
| 7   | `evaluation_method`     | ⋆    | Simulation / Real Testbed                                                                                                                  |

## Phase 07a' — Coverage validation (provisional, awaiting user confirmation)

Cross-pass synthesis of two grep+evidence sweeps over the 20 included papers, normalized to the locked taxonomy. Cells marked `?` indicate MED confidence and need user check before Phase 07b.

| paper                    | infrastructure | decision                    | agentic_configuration               | reasoning_approach               | autonomy_level | metric                            | evaluation_method | conf |
| ------------------------ | -------------- | --------------------------- | ----------------------------------- | -------------------------------- | -------------- | --------------------------------- | ----------------- | ---- |
| 0930 Stateful NFs        | Cloud          | Placement & Offloading      | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 1157 ECO-LLM             | Continuum      | Placement & Offloading      | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 1404 ARM                 | Cloud          | Remediation                 | Sole Decider, Single Agent          | Iterative Reasoning              | Autonomous     | RM + Agent                        | Real Testbed      | HIGH |
| 1408 K8s Scheduling      | Cloud          | Scheduling                  | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Real Testbed?     | MED  |
| 1420 GenAI Mapping       | Continuum      | Placement & Offloading      | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 1496 Neurosymbolic       | Continuum      | Routing & Slicing           | Pipeline Contributor, Single Agent  | Prompting                        | Supervised     | RM                                | Simulation        | MED  |
| 1563 GP Hyper-heuristic  | Continuum      | Scheduling                  | Pipeline Contributor, Single Agent? | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | MED  |
| 1593 K8s Autoscaling     | Cloud          | Scaling                     | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Real Testbed?     | MED  |
| 1644 Digital Twin Alloc  | Cloud          | Placement & Offloading      | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 1680 MicroIntent         | Continuum      | Placement & Offloading      | Pipeline Contributor, Single Agent  | Prompting + Knowledge Retrieval  | Supervised     | RM                                | Simulation        | MED  |
| 1783 Can LLMs only talk? | Cloud          | Scheduling                  | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 1947 XAI+Llama2 ZSM      | Continuum      | Remediation                 | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Real Testbed?     | MED  |
| 1991 Agentic Offloading  | Continuum      | Placement & Offloading      | Sole Decider, Multi-Agent           | Iterative Reasoning              | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 2028 Cost-aware Sched    | Cloud          | Scheduling                  | Sole Decider, Single Agent          | Prompting + Model Specialization | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 2362 AutoHMA-LLM         | Continuum      | Scheduling                  | Sole Decider, Multi-Agent           | Iterative Reasoning              | Autonomous     | RM + Agent                        | Real Testbed?     | MED  |
| 2470 Multi-Cloud Storage | Cloud          | Placement & Offloading      | Pipeline Contributor, Single Agent  | Prompting + Model Specialization | Supervised     | RM                                | Simulation        | MED  |
| 2556 LLM Cloud Sched     | Cloud          | Scheduling                  | Sole Decider, Single Agent          | Prompting                        | Autonomous     | RM + Agent                        | Simulation        | HIGH |
| 2723 AGORA Green Orch    | Continuum      | Routing & Slicing + Scaling | Sole Decider, Single Agent          | Iterative Reasoning              | Autonomous     | RM + Agent (energy primary in RM) | Simulation        | HIGH |
| 2779 Cluster Workload    | Cloud          | Scheduling                  | Pipeline Contributor, Single Agent  | Prompting                        | Supervised     | RM                                | Simulation        | MED  |
| 2936 RAG Offloading IoE  | Continuum      | Placement & Offloading      | Pipeline Contributor, Single Agent  | Knowledge Retrieval              | Supervised     | RM                                | Simulation        | HIGH |

### Per-axis distribution (provisional)

- **infrastructure:** Cloud 10 / Edge 0 / Continuum 10.
- **decision** (multi-select): Scheduling 9, Placement & Offloading 9, Scaling 2, Routing & Slicing 2, Remediation 2. (Total 24; multi-counted.)
- **agentic_configuration:** `Sole Decider, Single Agent` 12, `Sole Decider, Multi-Agent` 2, `Pipeline Contributor, Single Agent` 6, `Pipeline Contributor, Multi-Agent` 0.
- **reasoning_approach** (multi-select): Prompting 17, Iterative Reasoning 5, Knowledge Retrieval 2, Model Specialization 2.
- **autonomy_level:** Advisory 0, Supervised 6, Autonomous 14.
- **metric** (multi-select): RM Performance Metric 20, Agent Performance Metric 14.
- **evaluation_method:** Simulation 16, Real Testbed 4 (3 of which are MED).

### Reserved cell check

`Pipeline Contributor, Multi-Agent` is empty in the corpus (validated). Kept in the taxonomy for conceptual closure of the 2×2 matrix.

### Flagged cells (needing user check or fulltext verification)

1. **paper-1408 K8s Scheduling — evaluation_method:** Real Testbed vs Simulation. Kubernetes scheduler plugins are commonly evaluated on real clusters; classification provisional.
2. **paper-1496 Neurosymbolic Intent — decision:** `Routing & Slicing` is the most likely class given "Intent-based Service Management" framing; could also be `Placement & Offloading` if intents drive service mapping.
3. **paper-1563 GP Hyper-heuristic — agentic_configuration:** Single Agent classification rests on whether the GP framework is the final decision-maker (Pipeline Contributor) or the LLM is. Title suggests GP is the framework, LLM generates heuristics — Pipeline Contributor.
4. **paper-1593 K8s Autoscaling — evaluation_method:** Same as 1408; K8s autoscaling typically real-cluster.
5. **paper-1947 XAI+Llama2 — evaluation_method:** Pass-2 said Real Testbed; needs fulltext verification.
6. **paper-2362 AutoHMA-LLM — evaluation_method:** Pass-2 said real scenario; whether this is a cloud cluster or a robotics testbed needs verification.
7. **paper-2470 Multi-Cloud Storage — autonomy_level:** Supervised vs Autonomous. Intent compilation through fine-tuned LLM into policies — the policy execution may be deterministic (Pipeline Contributor) and the LLM never lands actions directly → Supervised is defensible.
8. **paper-2779 Cluster Workload — agentic_configuration:** GPT-4 parses constraints one-shot; Kubernetes scheduler executes. Pipeline Contributor.

### Recommendation

- The 7 axes provide full coverage on all 20 papers; no orphan papers; no axis where >5 papers are LOW confidence.
- Lock the taxonomy after user reviews the 8 flagged cells above (most are HIGH-vs-MED distinctions on Simulation vs Real Testbed or Sole Decider vs Pipeline Contributor).
- Reserved cell `Pipeline Contributor, Multi-Agent` remains intentionally empty.

## Phase 07a' — Post-validation refinements and resolved flagged cells

User checkpoint resolved 2026-05-15. Three structural refinements + 8 cell resolutions.

### Structural refinements

1. **`infrastructure` renamed.** `Cloud` → `Cloud-Only`; `Continuum` → `Edge-Cloud Continuum`; `Edge` dropped (empirically empty — every "edge" paper in the corpus also reaches the cloud). Final values: `Cloud-Only`, `Edge-Cloud Continuum`.
2. **`autonomy_level` reduced.** `Advisory` dropped (empirically empty). Final values: `Supervised`, `Autonomous`.
3. **`agentic_configuration` split into two facets.** Cross-product values replaced by two single-select facets evaluated independently: `decision_role` (`Sole Decider` / `Pipeline Contributor`) and `coordination_topology` (`Single Agent` / `Multi-Agent`). The corpus vacancy at `Pipeline Contributor × Multi-Agent` is reported in stage 09 as a research opportunity, not as a coverage gap.

### Resolved flagged cells

| paper      | axis                                  | resolution                      | evidence                                                                                                                                                                                                                                                                                    |
| ---------- | ------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| paper-1408 | `evaluation_method`                   | `Simulation`                    | "we develop a discrete-time, event-driven simulator. The simulator's architecture faithfully reproduces the Kubernetes scheduling flow."                                                                                                                                                    |
| paper-1496 | `decision`                            | `Placement & Offloading` (only) | "JSON ... used to create a symbolic representation of the problem using ASP ... Clingo solver is used to extract all the possible service-to-cluster matching solutions."                                                                                                                   |
| paper-1563 | `agentic_configuration.decision_role` | `Pipeline Contributor`          | Abstract: "an LLM-enhanced Genetic Programming Hyper-Heuristic (LLM-GPHH) algorithm to evolve heuristics" — GP is the final decision-maker; LLM evolves operators.                                                                                                                          |
| paper-1593 | `evaluation_method`                   | `Real Testbed`                  | "Data are collected every 30 seconds and stored in CSV format by autoscaler service running in the Kubernetes cluster as deployment ... output is then used to automatically update the number of deployment replicas through an autoscaler service that has access to the Kubernetes API." |
| paper-1947 | `evaluation_method`                   | `Real Testbed`                  | "Our experimental setup ... includes two machines hosting the Kubernetes-based cluster and the Llama2 LLM, respectively."                                                                                                                                                                   |
| paper-2362 | `evaluation_method`                   | `Simulation`                    | "We simulated intelligent logistics scenarios using MATLAB 9.12, in which cars, UAVs and robots collaborate."                                                                                                                                                                               |
| paper-2470 | `autonomy_level`                      | `Supervised`                    | Algorithmic validation of parsed intents (no HITL but deterministic gate before action).                                                                                                                                                                                                    |
| paper-2779 | `agentic_configuration.decision_role` | `Pipeline Contributor`          | GPT-4 parses NL constraints; Kubernetes scheduler executes the placement.                                                                                                                                                                                                                   |

### Final per-axis distribution (post-refinement)

- `infrastructure`: `Cloud-Only` 10 · `Edge-Cloud Continuum` 10.
- `decision` (multi-select): `Scheduling` 9 · `Placement & Offloading` 10 · `Scaling` 2 · `Routing & Slicing` 1 · `Remediation` 2 (multi-count 24).
- `agentic_configuration.decision_role`: `Sole Decider` 14 · `Pipeline Contributor` 6.
- `agentic_configuration.coordination_topology`: `Single Agent` 18 · `Multi-Agent` 2.
- `reasoning_approach` (multi-select): `Prompting` 17 · `Iterative Reasoning` 5 · `Knowledge Retrieval` 2 · `Model Specialization` 2.
- `autonomy_level`: `Supervised` 5 · `Autonomous` 15.
- `metric` (multi-select): `RM Performance Metric` 20 · `Agent Performance Metric` 14.
- `evaluation_method`: `Simulation` 17 · `Real Testbed` 3.

### Status

Coverage validation clean. All structural refinements + cell resolutions captured. Ready for Phase 07b.

## Next steps

- Phase 07b: write `### 07b — Final classification` block into each `papers/paper-NNNN.md` with verbatim evidence + 1-sentence rationale per axis (neighboring-value-not-chosen captured for single-select axes).
- On Phase 07b completion: flip `taxonomy.status` to `locked` in CLAUDE.md §8; commit `[07] lock`.
