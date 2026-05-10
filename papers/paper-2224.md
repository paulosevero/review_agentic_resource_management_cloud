---
id: paper-2224
title: Intent-driven network automation through sustainable multimodal generative
  AI
authors:
- Trantzas, Kostis
- Brodimas, Dimitrios
- Agko, Besiana
- Tziavas, Georgios Christos
- Tranoris, Christos
- Denazis, Spyros
- Birbas, Alexios
venue: Eurasip Journal on Wireless Communications and Networking
venue_type: journal
year: 2025
doi: 10.1186/s13638-025-02472-x
url: https://www.scopus.com/pages/publications/105007145126?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Intent-based networking
- Large language models
- Management and orchestration
- Network standards
- Sustainable multimodal generative artificial intelligence
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource
      management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_decision: Exclude
    proposed_justification: Review
    winning_category: review
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Problema estritamente de RAN/5G/6G/spectrum sem substrato
      cloud/edge RM.
    winning_category: E_strict_telecom
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2224 — Intent-driven network automation through sustainable multimodal generative AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The concept of Network-as-a-Service involves deploying and reconfiguring next-generation networks, in a flexible and dynamic manner, to always cater to the needs of the respective stakeholders. It presents a complex challenge to manage and orchestrate computational and telecommunication resources across the cloud-edge continuum, especially with the growing focus on cost efficiency and energy consumption. To address this complexity, several technology enablers are considered, but the recent advancements in Large Language Models research have inevitably brought Intent-Based Networking to the forefront. This paper explores the architecture and implementation of an intent-based automation framework that adheres to contemporary industry standards, while also considering sustainability. To achieve this, a translation pipeline is introduced, based on emerging multimodal Generative Artificial Intelligence models, which transforms a high-level description of desired network capabilities and supplementary deployment files into machine-consumable information digested by the network itself. Therefore, several state-of-the-art online and locally deployed models are compared. The ultimate motivation of this work is to validate the feasibility and accuracy of the proposed framework, promoting sustainability through minimal resource consumption and cost efficiency. Additionally, the framework ensures compatibility with modern orchestrators and next-generation Operational Support System that follow the same industry standards. © The Author(s) 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_abs_state_of_the_art, matched_substring: "state-of-the-art on" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-Based" }`
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

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Problema estritamente de RAN/5G/6G/spectrum sem substrato cloud/edge RM."
- **winning_category:** 'E_strict_telecom'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: E_strict_telecom, pattern_id: strict_telecom_only, matched_substring: "6g system adopting multimodal generative AI, in 2024 Joint European Conference on Networks and Commu" }`


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
