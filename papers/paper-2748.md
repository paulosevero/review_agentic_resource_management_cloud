---
id: paper-2748
title: Fault-tolerant routing in BCube based on an enhanced local safe information model
authors:
- Qi, Wenwen
- Wang, Guijuan
- Dong, Anming
- Yu, Jiguo
venue: Journal of Network and Computer Applications
venue_type: journal
year: 2026
doi: 10.1016/j.jnca.2026.104463
url: https://www.scopus.com/pages/publications/105035654190?origin=resultslist
publisher: Academic Press
pages: ''
keywords:
- BCube
- Data center network
- Enhanced local safe information model
- Fault-tolerant routing algorithm
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2748 — Fault-tolerant routing in BCube based on an enhanced local safe information model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the applications of artificial intelligence (AI) and large language models (LLM), data center networks serve as a core infrastructure supporting massive computing and data transmission, where their reliability and fault tolerance are critical to ensuring service continuity. BCube can offer superior fault tolerance and maintain high scalability, while servers and links frequently fail when the data center network scales up, decreasing the communication stability and efficiency. Most existing safe information models typically consider either faulty servers or faulty links separately, lacking a comprehensive solution. In such a case, this paper proposes an enhanced local safe information model (ELSIM) that address both faulty servers and faulty links simultaneously. Also, a fault-tolerant routing algorithm of BCube based on ELSIM is designed, which ensures reliable communication between any two fault-free servers with high efficiency. Finally, simulation results demonstrate that, compared with three existing routing algorithms based on safe information models, the proposed algorithm achieves the highest transmission success rate, shorter average path length and higher shortest path ratio. Notably, even with 20% of servers and 20% of links in BCube failing, our algorithm still maintains a transmission success rate above 90%. © 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2748.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
