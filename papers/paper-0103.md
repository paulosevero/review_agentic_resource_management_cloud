---
id: paper-0103
title: 'Task Allocation in Multiagent Systems: A Survey of Some Interesting Aspects'
authors:
- Wu, Jun
- Zhang, Lei
- Qiao, Yu
- Wang, Chongjun
venue: Interactions In Multiagent Systems
venue_type: book-chapter
year: 2018
doi: 10.1142/9789813208742_0006
url: https://www.scopus.com/pages/publications/85128041600?origin=resultslist
publisher: World Scientific Publishing Co.
pages: 107--147
keywords: []
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-0103 — Task Allocation in Multiagent Systems: A Survey of Some Interesting Aspects

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task allocation is an approach for coordination and cooperation in multiagent systems (MAS). It is an important problem in MAS research and is widely applied in fields such as multirobot systems, crowdsourcing, wireless sensor networks, web services, cloud computing, distributed intrusion detection, and so on. Intrinsically, task allocation is a class of optimization problems, that is, how to allocate a set of tasks to a MAS, in order to achieve a certain objective subject to some constraints. In different applications, the above problem can be formalized as different forms and requires different techniques for designing algorithms. The problem space of task allocation is rather large. However, due to the fact that task allocation is more or less independently studied in several subdomains of computer science and artificial intelligence, a global view on the problem space of task allocation is still missing. In this chapter, we briefly summarize several important directions of task allocation research, including taxonomy study; allocating tasks that are constrained, complex, or dynamic; allocating tasks to agents that are rational, dynamic, or connected by network; and control models which are currently a spectrum between centralized and distributed models. By the above work, we aim to correlate current task allocation research, preliminarily depict the problem space of task allocation, and locate problems that are well-studied or potentially interesting for future study. © 2019 by World Scientific Publishing Co. Pte. Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0103.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
