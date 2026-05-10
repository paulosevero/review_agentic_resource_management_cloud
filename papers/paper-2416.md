---
id: paper-2416
title: Adaptive GPU Resource Allocation for Multi-Agent Collaborative Reasoning in Serverless Environments
authors:
- Zhang, Guilin
- Guo, Wulan
- Tan, Ziqi
venue: 2025 7th Computing, Communications and IoT Applications Conference, ComComAp 2025
venue_type: conference
year: 2025
doi: 10.1109/ComComAp68359.2025.11353145
url: https://www.scopus.com/pages/publications/105033494984?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 334--339
keywords:
- collaborative reasoning
- GPU resource allocation
- Multi-agent systems
- serverless computing
- workload scheduling
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_modifier_by_llm
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
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

# paper-2416 — Adaptive GPU Resource Allocation for Multi-Agent Collaborative Reasoning in Serverless Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-agent systems powered by large language models have emerged as a promising paradigm for solving complex reasoning tasks through collaborative intelligence. However, efficiently deploying these systems on serverless GPU platforms presents significant resource allocation challenges due to heterogeneous agent workloads, varying computational demands, and the need for cost-effective scaling. This paper presents an adaptive GPU resource allocation framework that achieves 85% latency reduction compared to round-robin scheduling while maintaining comparable throughput to static allocation, using an O(N) complexity algorithm for real-time adaptation. Our approach dynamically allocates GPU resources based on workload characteristics, agent priorities, and minimum resource requirements, enabling efficient utilization while maintaining quality of service. The framework addresses three key challenges: (1) heterogeneous computational demands across lightweight coordinators and heavyweight specialists, (2) dynamic workload fluctuations requiring millisecond-scale reallocation, and (3) capacity constraints in serverless environments. Through comprehensive simulations modeling realistic multi-agent workflows with four heterogeneous agents, we demonstrate that adaptive allocation outperforms static equal and round-robin strategies across latency, cost, and GPU utilization metrics. The framework provides a practical solution for deploying cost-efficient multiagent AI systems on serverless GPU infrastructure.  © 2025 IEEE.

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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_modifier_by_llm', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: llm_as_workload, pattern_id: ovr_modifier_by_llm, matched_substring: "powered by large language" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "large language models have eme" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2416.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
