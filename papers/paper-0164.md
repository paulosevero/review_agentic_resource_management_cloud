---
id: paper-0164
title: 'Automated Negotiations Under User Preference Uncertainty: A Linear Programming Approach'
authors:
- Tsimpoukis, Dimitrios
- Baarslag, Tim
- Kaisers, Michael
- Paterakis, Nikolaos G.
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2019
doi: 10.1007/978-3-030-17294-7_9
url: https://www.scopus.com/pages/publications/85064942807?origin=resultslist
publisher: Springer Verlag
pages: 115--129
keywords:
- Commerce
- Economic and social effects
- Electric power transmission networks
- Electronic trading
- Information use
- Linear programming
- Smart power grids
- Automated negotiations
- High-frequency trading
- Limited information
- Linear optimization
- Pair-wise comparison
- Partial information
- Partial information model
- Preference uncertainty
- Autonomous agents
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
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-0164 — Automated Negotiations Under User Preference Uncertainty: A Linear Programming Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous agents negotiating on our behalf find applications in everyday life in many domains such as high frequency trading, cloud computing and the smart grid among others. The agents negotiate with one another to reach the best agreement for the users they represent. An obstacle in the future of automated negotiators is that the agent may not always have a priori information about the preferences of the user it represents. The purpose of this work is to develop an agent that will be able to negotiate given partial information about the user’s preferences. First, we present a new partial information model that is supplied to the agent, which is based on categorical data in the form of pairwise comparisons of outcomes instead of precise utility information. Using this partial information, we develop an estimation model that uses linear optimization and translates the information into utility estimates. We test our methods in a negotiation scenario based on a smart grid cooperative where agents participate in energy trade-offs. The results show that already with very limited information the model becomes accurate quickly and performs well in an actual negotiation setting. Our work provides valuable insight into how uncertainty affects an agent’s negotiation performance, how much information is needed to be able to formulate an accurate user model, and shows a capability of negotiating effectively with minimal user feedback. © Springer Nature Switzerland AG 2019.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0164.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
