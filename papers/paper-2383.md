---
id: paper-2383
title: 'Productive Intelligence: AI and Generative AI for Production Optimization and Predictive Maintenance in Oil and Gas Fields - Case Studies from the USA and India'
authors:
- Yenugu, Malleswar
venue: Society of Petroleum Engineers - ADIPEC 2025
venue_type: conference
year: 2025
doi: 10.2118/229678-MS
url: https://www.scopus.com/pages/publications/105033789866?origin=resultslist
publisher: Society of Petroleum Engineers
pages: ''
keywords:
- Failure (mechanical)
- Gas industry
- Gasoline
- Learning algorithms
- Learning systems
- Machine learning
- Oil well production
- Outages
- Petroleum industry
- Predictive maintenance
- Reliability
- Well stimulation
- Case-studies
- Machine learning algorithms
- Oil and gas fields
- Oil and gas well
- Performance
- Predictive maintenance
- Production optimization
- Real-world
- Well production
- World views
- Predictive analytics
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Out of scope
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

# paper-2383 — Productive Intelligence: AI and Generative AI for Production Optimization and Predictive Maintenance in Oil and Gas Fields - Case Studies from the USA and India

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper describes real-world views of how Artificial Intelligence (AI) and Generative AI (Gen AI) can be employed to enhance oil and gas well production optimization and predictive maintenance. We employed machine learning algorithms to predict and analyze day-to-day production, pressure, and equipment sensor readings. Generative models were used in parallel to simulate possible failure modes. From India and US case studies, we demonstrate how smart systems perceive and facilitate decision-making in order to improve production efficiency. Implementation of the methodology provided measurable improvement in performance. Downtime resulting from failures due to maintenance was predicted 15 to 20 percent more accurately and there was reduction in unplanned downtime by up to 18 percent. Overall, the findings show predictive analytics with generative simulation is a battle-tested, scalable solution that maximizes reliability and optimizes production for many operating conditions. They operated by taking in historical and real-time well data into machine learning models that were programmed to pick up on patterns that might otherwise be overlooked through traditional analysis. Gen AI, when married with digital twin-based modeling, allowed for predictive maintenance and failure scenario simulation, not only making operations smarter but also more responsive. Secondly, through the use of edge-computing models, the information produced could be retrieved nearly instantaneously by field personnel, enhancing response time to anomalies and maximizing daily operational tactics. This paper provides suggestions as to how contemporary AI methodologies can be adapted to the actual issues encountered in upstream oilfield activities, particularly in operations with sensor reliability problems, excessive gas-to-oil ratios, pump inefficiency, and challenging production conditions. Through three different case studies and proof of quantifiable performance improvement, we lay a compelling basis for incorporating AI and Gen AI into current digital transformation initiatives in the petroleum industry. Copyright © 2025, Society of Petroleum Engineers.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2383.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
