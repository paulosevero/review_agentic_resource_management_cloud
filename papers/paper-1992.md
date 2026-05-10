---
id: paper-1992
title: AI-assisted Stochastic Optimization for GPU Data Centers Lifecycle Planning
authors:
- Nie, Chengyi
- Xing, Anna
- Latif, Imran
- Liu, Zhenhua
venue: E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems
venue_type: conference
year: 2025
doi: 10.1145/3679240.3735099
url: https://www.scopus.com/pages/publications/105016353557?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 870--873
keywords:
- Artificial intelligence
- Computer hardware
- Data centers
- Graphics processing unit
- Green computing
- Heuristic methods
- Life cycle
- Operating costs
- Optimization
- Program processors
- Stochastic systems
- Datacenter
- Hardware performance
- Optimization framework
- Performance degradation
- Planning method
- Power
- Power limitations
- Resources utilizations
- Stochastic optimizations
- Uncertainty
- Stochastic models
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1992 — AI-assisted Stochastic Optimization for GPU Data Centers Lifecycle Planning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The recent advancement in artificial intelligence (AI) boosts the demand for AI-related workloads, significantly increasing GPU deployment and associated power consumption in data centers. This trend accelerates hardware upgrades, introducing the need for GPU upgrades planning, reallocation, and retirement. Existing lifecycle planning methods typically rely on static provisioning or heuristic-based strategies, which make it challenging to address uncertainties in workload demand, hardware performance degradation, power limitations, etc. As a result, poor resource utilization and increased operating costs are common in data centers. We propose an AI-assisted stochastic optimization framework for GPU lifecycle planning in data centers. This framework utilizes large language models to generate predictive scenarios for future workload demands, hardware performance decay, etc., in different cases. These AI-generated insights are integrated into a stochastic optimization model, which helps stakeholders make decisions about the timing of upgrades and retirements of GPU and cooling systems in data centers. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-assisted" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-assisted" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI-assisted" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI-assisted" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1992.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
