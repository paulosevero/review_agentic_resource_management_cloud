---
id: paper-0328
title: Deep q-learning and preference based multi-agent system for sustainable agricultural market
authors:
- Pérez-Pons, María E.
- Alonso, Ricardo S.
- García, Oscar
- Marreiros, Goreti
- Corchado, Juan Manuel
venue: Sensors
venue_type: journal
year: 2021
doi: 10.3390/s21165276
url: https://www.scopus.com/pages/publications/85111780597?origin=resultslist
publisher: MDPI AG
pages: ''
keywords:
- Decision support systems
- Deep Q-learning
- Edge computing
- IoT
- Multi-agent systems
- Sustainable agriculture
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0328 — Deep q-learning and preference based multi-agent system for sustainable agricultural market

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Yearly population growth will lead to a significant increase in agricultural production in the coming years. Twenty-first century agricultural producers will be facing the challenge of achieving food security and efficiency. This must be achieved while ensuring sustainable agricultural systems and overcoming the problems posed by climate change, depletion of water resources, and the potential for increased erosion and loss of productivity due to extreme weather conditions. Those environmental consequences will directly affect the price setting process. In view of the price oscillations and the lack of transparent information for buyers, a multi-agent system (MAS) is presented in this article. It supports the making of decisions in the purchase of sustainable agricultural products. The proposed MAS consists of a system that supports decision-making when choosing a supplier on the basis of certain preference-based parameters aimed at measuring the sustainability of a supplier and a deep Q-learning agent for agricultural future market price forecast. Therefore, different agri-environmental indicators (AEIs) have been considered, as well as the use of edge computing technologies to reduce costs of data transfer to the cloud. The presented MAS combines price setting optimizations and user preferences in regards to accessing, filtering, and integrating information. The agents filter and fuse information relevant to a user according to supplier attributes and a dynamic environment. The results presented in this paper allow a user to choose the supplier that best suits their preferences as well as to gain insight on agricultural future markets price oscillations through a deep Q-learning agent. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0328.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
