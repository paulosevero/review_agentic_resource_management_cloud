---
id: paper-1409
title: AI-Driven Edge Cloud Collaboration Framework With Autonomous Resource Allocation for Standardized 6G Healthcare Networks
authors:
- Balakrishnan, S.
- Senbagavalli, M.
- Manikandan, M.
- Sumathi, D.
- Ravi, Navyatha
- Shabaz, Mohammad
venue: IEEE Communications Standards Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOMSTD.2025.3634733
url: https://www.scopus.com/pages/publications/105024108933?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud analytics
- Edge computing
- Health care
- Changing workload
- Collaboration framework
- Critical applications
- Edge clouds
- Healthcare systems
- Intelligent Services
- Low latency
- Real time performance
- Resource requirements
- Resources allocation
- Cognitive systems
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
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

# paper-1409 — AI-Driven Edge Cloud Collaboration Framework With Autonomous Resource Allocation for Standardized 6G Healthcare Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> 6G networks are booming, and they will transform healthcare; ultra-low latency, massive connections, and intelligent services will finally reach critical applications. Real-time performance, standardization, and scalability of healthcare networks are impacted by having various categories of devices, changing workloads, and changing resource requirements. This paper suggests a new AI-based method for standardized 6G healthcare systems, referred to as the Cognitive Autonomous Resource and Edge Collaboration Framework (CARE-6G). The use of cognitive AI agents together with edge-cloud cooperation in CARE-6G enables automated prediction, allocation, and optimization of computing, storage, and networking resources. The framework is constructed hierarchically such that edge nodes perform low-latency processing, while cloud infrastructure performs big-scale analytics. AI-based predictive orchestration ensures that the needs for workloads and healthcare services can shift. The experiments indicated that CARE-6G is 35% quicker, 30% more resource-efficient, and 27% more reliable than the existing practices. When compared to the best methods available, CARE-6G was 39% faster, 30% better at using resources, 27% more reliable, 25% less power-hungry, and 15% better at getting things done.  © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-based" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1409.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
