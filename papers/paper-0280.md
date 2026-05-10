---
id: paper-0280
title: An Effective Multi-Agent Ant Colony Optimization Algorithm for QoS-Aware Cloud Service Composition
authors:
- Dahan, Fadl
venue: IEEE Access
venue_type: journal
year: 2021
doi: 10.1109/ACCESS.2021.3052907
url: https://www.scopus.com/pages/publications/85099725722?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17196--17207
keywords:
- ant colony optimization
- cloud services composition
- metaheuristic algorithm
- Quality of Service
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-0280 — An Effective Multi-Agent Ant Colony Optimization Algorithm for QoS-Aware Cloud Service Composition

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, service composition has gained increased attention as an auspicious paradigm to optimize the data accessibility, integrity, and interoperability of cloud computing. In this work, to solve the cloud service composition (CSC) problem, we introduce an efficient agent-based ant colony optimization (ACO) algorithm. The CSC problem aims to satisfy complex and challenging requirements of enterprises/users in a cloud environment. The challenge of such problem is the proliferation of providing similar services having similar functionality with varying quality of service (QoS) properties from different providers. Several swarm-based algorithms were introduced to solve this problem because the complexity of the problem is characterized as NP-hard, which is high. These algorithms aim to maintain a good balance between exploration and exploitation mechanisms, and to achieve this, a multi-agent based on ACO is proposed and compared with four different algorithms using 25 different real datasets. The computational results on 25 real datasets confirm the effectiveness of the multi-agent distribution of ACO process. Moreover, comparisons against the results of the four algorithms in the literature indicate that the multi-agent ACO approach is competitive with state-of-the-art algorithms. © 2013 IEEE.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0280.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
