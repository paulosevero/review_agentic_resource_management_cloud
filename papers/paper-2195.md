---
id: paper-2195
title: 'AI-Driven Cloud Resource Optimization: An in-Depth Analysis'
authors:
- Tajane, Kapil
- Ahire, Prashant
- Pitale, Rahul
venue: 2025 9th International Conference on Computing, Communication, Control and Automation, ICCCBEA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCUBEA65967.2025.11283710
url: https://www.scopus.com/pages/publications/105031877249?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI Agent
- Cloud Computing
- Load Balancing
- Optimization
- resource allocation
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
    proposed_decision: Exclude
    proposed_justification: Review
    winning_category: review
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2195 — AI-Driven Cloud Resource Optimization: An in-Depth Analysis

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing enabled access to computing resources is disruptive in how we provide and manage computing resources, by making resources flexible, scalable and available on-demand utilizing a pay-as-you-go model. Finding the right resource and managing it efficiently still remains an ongoing challenge, due to the dynamic workloads that have fixed and flexible qualities, dynamic application requirements, and complex heterogeneous cloud environments. This study provides a comprehensive survey of the literature on artificial intelligence (AI) techniques that are used for optimizing resource allocation in cloud computing. This study presents a review and discussion of the use of AI-based methods, including reinforcement learning, predictive analytics, and hybrid optimization methods, across multiple cloud deployment scenarios. The study undertakes a systematic review of recently published papers - sorting and categorizing the AI resourcing allocation methods to describe the current state-of-the-art, describing and investigating the key performance indicators to identify research gaps and provide future research recommendations. This study concludes that AI-based resource allocation methods consider more variables than ad-hoc and heuristic models; and that the use of those variables allows the AI-based models to improve efficiency, cost savings, energy-efficiency and service performance - with reported improvements between 15 - 60% across the research papers. © 2025 IEEE.

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

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`
  - `{ category: review, pattern_id: rev_systematic_review, matched_substring: "systematic review" }`
  - `{ category: review, pattern_id: rev_comprehensive_survey, matched_substring: "comprehensive survey" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-based" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2195.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
