---
id: paper-2635
title: 'MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces'
authors:
- Khan, Zafar Iqbal
- Khan, Muzafar
- Shah, Syed Nasir Mehmood
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3676311
url: https://www.scopus.com/pages/publications/105033477084?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 44165--44184
keywords:
- adaptive dynamic time quantum
- Cloud scheduling
- CloudSimPlus
- multi-agent systems
- multi-tier architecture
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
    proposed_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    winning_category: classical_agents
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
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

# paper-2635 — MAADRR: Multi-Agent Adaptive Dynamic Round Robin for Cloud Scheduling Using Real Cloud Workload Traces

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task scheduling is required to optimize the use of resources and minimize the waiting time in cloud computing systems. However, the traditional fixed scheduling techniques cannot address the variability, heterogeneity and dynamic behavior of cloud workloads. Current time-sharing schedulers use fixed CPU time quantum and do not have any dynamic mechanisms to adapt to the workload, and SLA-driven priorities, resulting in poor performance of cloud infrastructures. To overcome these drawbacks, this paper proposes a novel Multi-Agent Adaptive Dynamic Round Robin (MAADRR) scheduling model for dynamic and heterogeneous cloud systems. Compared with traditional single-layer schedulers, MAADRR has hierarchical agent-based coordination. This allows it to balance workloads across the infrastructure and have local flexibility simultaneously. The framework is implemented and evaluated on the CloudSim Plus simulator and enables realistic modelling of the multi-level cloud execution environment. The VM-level agents Adaptive Round Robin are dynamically changed by real-time quantum due to real-time workload feedback. A global coordination agent, which exists at the infrastructure layer, integrates the previously set scheduling strategies, such as Dynamic Max-Min, DRALBA, PSSLB, PSSELB, and DeRALBA, to coordinate the distribution of different tasks among the heterogeneous resources. This multi-agent design is cooperative and provides autonomous local optimization, stability, and fairness of the system. The experiments were conducted on workloads of varying sizes. The experimental results obtained from Google-Cluster-like Job (GoCJ) traces demonstrate that MAADRR is a more energy-efficient solution and outperforms the baseline methods in terms of Energy Consumption, Throughput, Average Waiting Time (AWT), Average Turnaround Time (ATAT), and Total Completion Time (TCT). The findings confirm that MAADRR is a scalable scheduling framework that is suitable for cloud environments. © 2026 The Authors.

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
- **regex_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **winning_category:** 'classical_agents'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2635.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
