---
id: paper-2716
title: A Trustworthy Hybrid ML-GenAI Architecture for Autonomous, Behavior-Aware Resource Allocation in Internet2 Traffic
authors:
- Mehr, Shideh Yavary
- Phadke, Abhishek
venue: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
venue_type: conference
year: 2026
doi: 10.1109/CCWC67433.2026.11393743
url: https://www.scopus.com/pages/publications/105035601369?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 299--304
keywords:
- Anomaly detection
- Artificial intelligence
- Behavioral research
- Decision trees
- Edge computing
- Hybrid systems
- Learning systems
- Nearest neighbor search
- Network architecture
- Resource allocation
- Trusted computing
- Autonomous behaviors
- Bandwidth resource
- Compute resources
- Internet2
- Nearest-neighbour
- Performance research
- Random forests
- Research and education network
- Resources allocation
- Uncertainty
- Semantics
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
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: "Review"
    winning_category: review
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2716 — A Trustworthy Hybrid ML-GenAI Architecture for Autonomous, Behavior-Aware Resource Allocation in Internet2 Traffic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet2 (I2), a high-performance research and education network, faces increasing pressure to allocate bandwidth and compute resources adaptively as traffic volumes and application behaviors evolve. Traditional static resource allocation strategies cannot meet the real-time demands of large-scale scientific workflows, distributed edge computing, and data-intensive academic environments. To address this challenge, this paper introduces a trustworthy hybrid ML-GenAI architecture that autonomously predicts, explains, and optimizes I2 traffic resource allocation with high precision. Our method integrates the two complementary machine learning models: K-Nearest Neighbors (KNN) for fine-grained local pattern detection and Random Forest (RF) for robust global trend prediction - ∗∗to capture both micro-level traffic fluctuations and macro-level demand patterns. These ML signals are further augmented using a Generative AI (Gen-AI) reasoning module that performs semantic flow characterization, anomaly explanation, and uncertainty justification. The Gen-AI component provides natural-language rationales for model decisions, enabling transparent decision-making and enhanced operator trust. Trustworthiness is ensured through three mechanisms: (1) Model cross-validation and ensemble agreement between KNN and RF to reduce bias and improve reliability; (2) Gen-AI-based explanation synthesis that generates interpretable justifications for allocation decisions; and (3) Uncertainty-aware resource allocation, where Gen-AI flags high-risk predictions and triggers safe-fallback allocation policies. Experimental results on a multi-terabyte Internet 2 flow dataset (2021-2025) show that the proposed hybrid system reduces misallocation by 32%, improves anomaly detection by 21%, and enables auditable, behavior-aware decisions that outperform traditional ML-only baselines. This work represents one of the first trustworthy hybrid ML-GenAI approaches for next-generation autonomous network resource management. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen-AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen-AI" }`
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

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_a_roadmap_survey, matched_substring: "A survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
