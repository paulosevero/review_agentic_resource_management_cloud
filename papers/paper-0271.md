---
id: paper-0271
title: A novel reinforcement-learning-based approach to workflow scheduling upon infrastructure-as-a-service clouds
authors:
- Chen, Peng
- Xia, Yunni
- Yu, Chun
venue: International Journal of Web Services Research
venue_type: journal
year: 2021
doi: 10.4018/IJWSR.2021010102
url: https://www.scopus.com/pages/publications/85100428243?origin=resultslist
publisher: IGI Global
pages: 21--33
keywords:
- Cloud workflows
- Cost
- Markov game model
- Multi-Agent Reinforcement Learning (MARL)
- Turnaround time
- Workflow scheduling
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0271 — A novel reinforcement-learning-based approach to workflow scheduling upon infrastructure-as-a-service clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, the cloud computing paradigm has become increasingly popular in large-scale and complex workflow applications. The workflow scheduling problem, which refers to finding the most suitable resource for each task of the workflow to meet user defined quality of service, attracts considerable research attention. Multi-objective optimization algorithms in workflow scheduling have many limitations (e.g., the encoding schemes in most existing heuristic-based scheduling algorithms require prior experts' knowledge), and thus, they can be ineffective when scheduling workflows upon dynamic cloud infrastructures with real time. A novel reinforcement-learning-based algorithm to multi-workflow scheduling over IaaS is proposed. It aims at optimizing make-span and dwell time and is to achieve a unique set of correlated equilibrium solution. The proposed algorithm is evaluated for famous workflow templates and real-world industrial IaaS by simulation and compared to the current state-of-the-art heuristic algorithms. The result shows that the algorithm outperforms compared algorithm. Copyright © 2021, IGI Global. Copying or distributing in print or electronic forms without written permission of IGI Global is prohibited.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0271.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
