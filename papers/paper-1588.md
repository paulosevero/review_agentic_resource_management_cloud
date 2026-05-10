---
id: paper-1588
title: 'Demo: Conversational AI Agent for ML Infrastructure Monitoring and Analysis'
authors:
- Ghaleb, Rami
- Dharmaraj, Mithun
- Prayaga, Srikar
- Banka, Tarun
venue: Proceedings - International Conference on Network Protocols, ICNP
venue_type: conference
year: 2025
doi: 10.1109/ICNP65844.2025.11192362
url: https://www.scopus.com/pages/publications/105020669332?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Agents
- Model Context Protocol
- Root Cause Analysis
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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
    - ovr_rca
    my_final_decision: Exclude
    my_justification: DEMO sem avaliação — regra manual (exclusão de demos sem avaliação).
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

# paper-1588 — Demo: Conversational AI Agent for ML Infrastructure Monitoring and Analysis

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present a conversational AI framework for monitoring and analysis of distributed AI/ML infrastructure based on a multi-agent architecture. The system incorporates specialized agents for topology discovery, health assessment, network flow analysis, and root cause analysis (RCA), accessible through a natural language interface. An agent orchestration component parses and routes user queries, allowing the platform to support a range of cluster observability and troubleshooting tasks using both sequential and parallel agent workflows. Each agent interacts with dedicated analytical microservices via Model Context Protocol (MCP), enabling modular and extensible evaluation of infrastructure state. We detail the system architecture, agent design, setup used for experiments and discuss the implications of conversational AI agents for automated RCA and operational efficiency in monitoring and troubleshooting large-scale ML infrastructure. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_rca']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
  - `{ category: llm_as_workload, pattern_id: ovr_rca, matched_substring: "RCA" }`
  - `{ category: llm_as_workload, pattern_id: ovr_rca, matched_substring: "RCA" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "DEMO sem avaliação — regra manual (exclusão de demos sem avaliação)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1588.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
