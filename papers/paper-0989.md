---
id: paper-0989
title: 'Don’t Train, Just Prompt: Towards a Prompt Engineering Approach for a More Generative Container Orchestration Management'
authors:
- Kratzke, Nane
- Drews, André
venue: International Conference on Cloud Computing and Services Science, CLOSER - Proceedings
venue_type: conference
year: 2024
doi: 10.5220/0012710300003711
url: https://www.scopus.com/pages/publications/85194172887?origin=resultslist
publisher: Science and Technology Publications, Lda
pages: 248--256
keywords:
- Automation
- cloud-native
- Container
- DevOps
- GPT-3.5
- GPT-4
- Intelligent
- Kubernetes
- Large Language Model
- Llama2
- LLM
- Mistral
- Orchestration
- Prompt Engineering
- Service Management
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0989 — Don’t Train, Just Prompt: Towards a Prompt Engineering Approach for a More Generative Container Orchestration Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Background: The intricate architecture of container orchestration systems like Kubernetes relies on the critical role of declarative manifest files that serve as the blueprints for orchestration. However, managing these manifest files often presents complex challenges requiring significant DevOps expertise. Methodology: This position paper explores using Large Language Models (LLMs) to automate the generation of Kubernetes manifest files through natural language specifications and prompt engineering, aiming to simplify Kubernetes management. The study evaluates these LLMs using Zero-Shot, Few-Shot, and Prompt-Chaining techniques against DevOps requirements and the ability to support fully automated deployment pipelines. Results show that LLMs can produce Kubernetes manifests with varying degrees of manual intervention, with GPT-4 and GPT-3.5 showing potential for fully automated deployments. Interestingly, smaller models sometimes outperform larger ones, questioning the assumption that bigger is always better. Conclusion: The study emphasizes that prompt engineering is critical to optimizing LLM outputs for Kubernetes. It suggests further research into prompt strategies and LLM comparisons and highlights a promising research direction for integrating LLMs into automatic deployment pipelines. © 2024 by SCITEPRESS – Science and Technology Publications, Lda.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Prompt Engineering" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "prompt engineering" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
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
  - `{ category: review, pattern_id: rev_a_roadmap_survey, matched_substring: "a comprehensive review" }`
  - `{ category: review, pattern_id: rev_a_roadmap_survey, matched_substring: "A comprehensive survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "survey" }`
  - `{ category: review, pattern_id: rev_comprehensive_survey, matched_substring: "comprehensive review" }`
  - `{ category: review, pattern_id: rev_comprehensive_survey, matched_substring: "comprehensive survey" }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
