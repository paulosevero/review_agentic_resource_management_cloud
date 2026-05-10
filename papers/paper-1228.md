---
id: paper-1228
title: Self-Optimizing Distributed Cloud Computing with Dynamic Neural Resource Allocation and Fault-Tolerant Multi-Agent Systems
authors:
- Tripura, N.
- Divya, P.
- Chaganti, Koushik Reddy
- Rao, Kota Venkateswara
- Rajyalakshmi, P.
- Naresh, P.
venue: Proceedings of the 4th International Conference on Ubiquitous Computing and Intelligent Information Systems, ICUIS 2024
venue_type: conference
year: 2024
doi: 10.1109/ICUIS64676.2024.10866891
url: https://www.scopus.com/pages/publications/86000235807?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1304--1310
keywords:
- Distributed Cloud
- Fault-Tolerant Systems
- Neural Resource Allocation
- Scenarios
- Transfer Learning
- Workload Management
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: RL
    winning_category: rl
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1228 — Self-Optimizing Distributed Cloud Computing with Dynamic Neural Resource Allocation and Fault-Tolerant Multi-Agent Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The exponential growth of distributed cloud systems necessitates an intelligent form of workload management that ensures optimum performance, scalability, and reliability. Traditional approaches based on static or heuristic resource allocation and fault-tolerance mechanisms cannot capture the dynamic nature of modern workloads and heterogeneous infrastructures. Drawing from this source of inspiration, this work develops a holistic framework integrating machine learning models that facilitate self-optimizing distributed cloud computing for dynamic workload management. Three components are significant in the proposed framework: (1) DNRA; this uses a hybrid GNN and RL architecture for real-time resource allocation, offering up to 25% improvement in resource utilization and a 30% reduction in task latency. (2) Workload-Aware Transfer Learning Scheduler (WATLS), leveraging transfer learning to predict workload dynamics across heterogeneous nodes, achieving 20% higher task throughput and 15% energy savings through proactive scheduling. (3) Multi-Agent Predictive Fault-Tolerant System (MAP-FTS), combining multi-agent systems with predictive fault detection to preemptively redistribute tasks and schedule maintenance, reducing system downtime by 50% and enhancing fault detection accuracy to 90%. The framework integrates novel methodologies towards answering the main challenges of resource allocation, workload prediction, and fault tolerance. The amount of progress achieved through cumulative contributions includes improvement in system reliability and scalability up to 5x their nodes and respective scalable energy efficiency without any degradation of performance. This work paves the pathway for an adaptive and intelligent next generation of distributed cloud systems. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The exponential growth of dist" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1228.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
