---
id: paper-2779
title:
  "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language
  Processing"
authors:
  - Sliwko, Leszek
  - Mizeria-Pietraszko, Jolanta
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3665989
url: https://www.scopus.com/pages/publications/105030579766?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 28054--28074
keywords:
  - Artificial intelligence
  - Kubernetes
  - load balancing
  - semantic parsing
  - soft-affinity
  - task assignment
language: English
source:
  databases:
    - Scopus
  exports:
    - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ""
status:
  04-title-screening: include
  05-abstract-screening: include
  06-full-text-screening: include
  07-taxonomy-development: classified
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification:
      C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: NLP talvez implique em LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
      - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied: []
    my_final_decision: "Include (Borderline)"
    my_justification: "GPT-4 faz one-shot NLP parsing de annotations de usuário para extrair semantic soft affinity constraints; o scheduler Kubernetes consome esses constraints e toma a decisão."
    agrees_with_regex: false
    divergence_reason:
      Regex flagged as llm_agentic_ai_generic; full-text reveals
      NLP parsing is support tool, not agentic RM loop.
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Cloud-Only
  decision:
    - Scheduling
  agentic_configuration:
    decision_role: Pipeline Contributor
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
  autonomy_level: Supervised
  metric:
    - RM Performance Metric
  evaluation_method: Simulation
---

# paper-2779 — Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cluster workload allocation often requires complex configurations, creating a usability gap. This paper introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural Language Processing. The system employs a Large Language Model (LLM) integrated via a Kubernetes scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences. A prototype featuring a cluster state cache and an intent analyzer (using AWS Bedrock) was developed. Empirical evaluation demonstrated high LLM parsing accuracy (>95% Subset Accuracy on an evaluation ground-truth dataset) for top-tier models like Amazon Nova Pro/Premier and Mistral Pixtral Large, significantly outperforming a baseline engine. Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations, particularly excelling in complex and quantitative scenarios and handling conflicting soft preferences. The results validate using LLMs for accessible scheduling but highlight limitations like synchronous LLM latency, suggesting asynchronous processing for production readiness. This work confirms the viability of semantic soft affinity for simplifying workload orchestration and presents a proof-of-concept design. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "NLP talvez implique em LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include (Borderline)
- **my_justification:** GPT-4 faz one-shot NLP parsing de annotations de usuário para extrair semantic soft affinity constraints; o scheduler Kubernetes consome esses constraints e toma a decisão.
- **agrees_with_regex:** False
- **divergence_reason:** Regex flagged as llm_agentic_ai_generic; full-text reveals NLP parsing is support tool, not agentic RM loop.
- **addressed_hint:** hint_categories=[devops] partially applies — system is config/orchestration tooling, not resource management (placement is deterministic post-parsing).
- **evidence_sections:** ["INTRODUCTION: 'intent analyzer that transforms natural language...[into]...constraints...coupled with...multi-objective...framework'", "PROTOTYPE AND TESTBED DESIGN > Intent Analyzer: 'sends structured prompt to GPT-4...parsed into structured representation used by scoring model'", 'SCORING MODEL: deterministic utility-function evaluation, no autonomous iteration']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                 | evidence                                                                                                                                                                                  | location                          | rationale (neighbor not chosen)                                                                                                                                          |
| ------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| infrastructure                              | Cloud-Only            | "introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural Language Processing"                                                                          | §Abstract                         | Not `Edge-Cloud` because the target is a Kubernetes datacenter cluster; no edge tier.                                                                          |
| decision                                    | Scheduling            | "The system employs a Large Language Model (LLM) integrated via a Kubernetes scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences." | §Abstract                         | _multi-select; the LLM informs Kubernetes scheduling (pod placement at job-time), not service placement, scaling, routing, or remediation._                              |
| agentic_configuration.decision_role         | Pipeline Contributor  | "the scheduler assigns scores to the valid machines based on these preferences"                                                                                                           | §I Introduction                   | Not `Sole Decider` because the LLM parses intent into soft-affinity preferences that feed the Kubernetes Score Extender; final scheduling is performed by the scheduler. |
| agentic_configuration.coordination_topology | Single Agent          | "an intent analyzer (using AWS Bedrock) was developed"                                                                                                                                    | §Abstract                         | Not `Multi-Agent` because one LLM (via Bedrock) handles intent parsing per pod.                                                                                          |
| reasoning_approach                          | Prompting             | "The presented approach allows new scheduling behaviors to be introduced dynamically by defining new Intent classes and updating the LLM prompt"                                          | §I Introduction                   | _structured prompting with Intent class schemas; no iterative ReAct loop, no fine-tuning, no external KB retrieval._                                                     |
| autonomy_level                              | Supervised            | "The current prototype is intended as a research artifact to demonstrate the feasibility and is not production-ready."                                                                    | §I Introduction                   | Not `Autonomous` because the prototype runs as a research artifact, with developers providing the natural-language hints per workload.                                   |
| metric                                      | RM Performance Metric | "Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations"                             | §Abstract                         | _single-select; placement-quality (RM-side) is the headline metric; LLM accuracy is reported but the locked classification keeps RM only._                               |
| evaluation_method                           | Simulation            | "The testbed is built around a multi-node Kubernetes cluster simulated using Minikube"                                                                                                    | §III Prototype and Testbed Design | Not `Practical Testbed` because the experiments run on a simulated Minikube-based cluster, not a deployed production environment.                                             |

**Confidence (weakest axis):** MED
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Scheduling`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Supervised`.
