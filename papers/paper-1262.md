---
id: paper-1262
title: Scheduling a multi-agent flow shop with two scenarios and release dates
authors:
- Wang, Xinyue
- Ren, Tao
- Bai, Danyu
- Chu, Feng
- Yu, Yaodong
- Meng, Fanchun
- Wu, Chin-Chia
venue: International Journal of Production Research
venue_type: journal
year: 2024
doi: 10.1080/00207543.2023.2188646
url: https://www.scopus.com/pages/publications/85150857932?origin=resultslist
publisher: Taylor and Francis Ltd.
pages: 421--443
keywords:
- bi-scenario
- branch and bound
- co-evolution
- flow-shop scheduling
- Multi-agent
- reinforcement learning
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

# paper-1262 — Scheduling a multi-agent flow shop with two scenarios and release dates

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is widely applied in modern industrial areas due to its technological advancement, cost reduction, and applicability. Packets (tasks) belonging to different applications (agents) compete to share the common cloud resource through a series of edge nodes (processors) in pursuit of fast transmission. This paper abstracts the cloud computing system as a multi-agent flow-shop scheduling (MAFS) problem. The objective is to minimise the total completion time of several agents with the restriction that the maximum lateness cannot exceed a given bound. Given the complexity of the considered problem, a branch and bound algorithm combined with several pruning rules and lower bounds is proposed to obtain optimal solutions. Furthermore, the considered problem is generalised to a bi-scenario version, and a bi-population cooperative co-evolutionary (BCCE) algorithm is proposed to solve it. A reinforcement learning-based method is presented to generate the initial population. Several problem-specific intensification strategies are constructed to explore promising solutions. Comprehensive experiments verified the effectiveness of the proposed algorithms. The industrial data from the China Earthquake Network Centre further confirmed the superiority of the BCCE algorithm. Overall, the MAFS model and the proposed algorithms effectively enhance the user experience and reasonably guarantee revenue. © 2023 Informa UK Limited, trading as Taylor & Francis Group.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1262.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
