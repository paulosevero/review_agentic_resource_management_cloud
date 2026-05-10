---
id: paper-0853
title: Automation of AD-OHC Dashbord and Monitoring of Cloud Resources using Genrative AI to Reduce Costing and Enhance Performance
authors:
- Chavan, Parikshit
- Chavan, Peeyusha
venue: 2024 International Conference on Innovations and Challenges in Emerging Technologies, ICICET 2024
venue_type: conference
year: 2024
doi: 10.1109/ICICET59348.2024.10616299
url: https://www.scopus.com/pages/publications/85201183768?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AD-OHC Dashbord
- Cloud Computing
- Cloud Monitoring.
- Cloud Resources
- Cost Reductions
- Generative AI
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_final_decision: Exclude
    my_justification: Review
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

# paper-0853 — Automation of AD-OHC Dashbord and Monitoring of Cloud Resources using Genrative AI to Reduce Costing and Enhance Performance

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this extensive review, the incorporation of Generative Artificial Intelligence (AI) into ad-hoc dashboards and cloud resource monitoring is investigated in depth. A purpose of this work is to investigate a current research and highlight the transformational potential of generative artificial intelligence for optimising costs, automating tasks, and improving overall cost efficiency. This article includes a comprehensive analysis of a development of ad-hoc cloud computing, a relevance of cloud resource monitoring, and the role that generative artificial intelligence plays in reducing costs. Notable advantages include better user satisfaction, resource optimisation, adaptive learning, and efficient automation. Additionally, precise decision-making and resource optimisation are highlighted. By presenting actual evidence, the study highlights the association between the quality of generative artificial intelligence and the influence it has on society. It finishes with an analysis of generative artificial intelligence applications in ad-hoc dashboards, with a focus on increased resource utilisation, scalability, and timely consistency of cloud resources. In addition, the article addresses constraints and makes suggestions for future paths. These include models that protect users' privacy, efficient resource utilisation, explainable artificial intelligence, dynamic autonomy, and security-driven generative models. The paper's goal is to provide the groundwork for further study and improvement.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0853.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
