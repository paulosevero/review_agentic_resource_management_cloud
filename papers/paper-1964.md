---
id: paper-1964
title: Enhancing Adaptability, Security, and Resource Optimization by Converging Generative AI with IoT
authors:
- Molakatala, Nagamani
- Deepa, R.
- Chandra, Saurabh
- Kayathri, T.L.
- Bhutani, Monica
- Dwaramwar, Pravin A.
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-6715-4_29
url: https://www.scopus.com/pages/publications/105020022390?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 415--432
keywords:
- Autonomous systems
- Edge computing
- Federated learning
- Generative AI
- Internet of Things
- IoT applications
- Predictive maintenance
- Smart cities
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1964 — Enhancing Adaptability, Security, and Resource Optimization by Converging Generative AI with IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Generative AI combined with the IoT can lead to revolution and evolution across industries, giving intelligence and adaptability solutions along with prediction systems. In this paper, the author discusses the implementation of Generative AI in IoT systems and why it is useful to use generative models to optimize IoT operations such as data generation, predictive maintenance, and decision-making. We consider the main use cases where generative models can improve IoT functioning and address existing challenges: smart cities, healthcare, and security. However, this convergence has a number of challenges still persisting, such as computation, data privacy, and system integration issues. Cutting-edge breakthroughs in edge computing, low-power AI hardware, and federated learning play a vital role in dismantling these barriers and opening a path to self-evolving IoT landscapes driven by Generative AI. With respect to the four areas of exploration presented in this paper, this review offers a future viewpoint on the future of Generative AI for progressing the next-generation IoT applications addressing technical, ethical, and regulatory capabilities. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: review, pattern_id: rev_abs_this_survey, matched_substring: "this review" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1964.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
