---
id: paper-2086
title: AI-Based Modeling and Optimization of AC/DC Power Systems
authors:
- Rojek, Izabela
- Mikołajewski, Dariusz
- Prokopowicz, Piotr
- Piechowiak, Maciej
venue: Energies
venue_type: journal
year: 2025
doi: 10.3390/en18215660
url: https://www.scopus.com/pages/publications/105021458922?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- artificial intelligence
- deep learning
- edge computing
- energy efficiency
- generative AI
- machine learning
- sustainability
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
    proposed_decision: Exclude
    proposed_justification: Review
    winning_category: review
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
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

# paper-2086 — AI-Based Modeling and Optimization of AC/DC Power Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This review examined the latest advances in the modeling, analysis, and control of AC/DC power systems based on artificial intelligence (AI) in which renewable energy sources play a significant role. Integrating variable and intermittent renewable energy sources (such as sunlight and wind power) poses a major challenge in maintaining system stability, reliability, and optimal system performance. Traditional modeling and control methods are increasingly inadequate to capture the complex, nonlinear, and dynamic behavior of modern hybrid AC/DC systems. Specialized AI techniques, such as machine learning (ML) and deep learning (DL), and hybrid models, have become important tools to meet these challenges. This article presents a comprehensive overview of AI-based methodologies for system identification, fault diagnosis, predictive control, and real-time optimization. Particular attention is paid to the role of AI in increasing grid resilience, implementing adaptive control strategies, and supporting decision-making under uncertainty. The review also highlights key breakthroughs in AI algorithms, including federated learning, and physics-based neural networks, which offer scalable and interpretable solutions. Furthermore, the article examines current limitations and open research problems related to data quality, computational requirements, and model generalizability. Case studies of smart grids and comparative scenarios demonstrate the practical effectiveness of AI-based approaches in real-world energy system applications. Finally, it proposes future directions to narrow the gap between AI research and industrial application in next-generation smart grids. © 2025 by the authors.

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

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_abs_this_survey, matched_substring: "This review" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-based" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI-Based" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2086.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
