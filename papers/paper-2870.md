---
id: paper-2870
title: Dynamic Task Allocation of Edge–Cloud System for Low-Altitude Economy via Multiagent Actor–Critic-Queuing Computational Framework
authors:
- Xue, Lei
- Hu, Yuwen
- Ye, Haichuan
- Zhai, Xiaomeng
- Yang, Jie
- Jin, Shi
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3621859
url: https://www.scopus.com/pages/publications/105019557268?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5655--5668
keywords:
- Actor–critic algorithm
- dynamic task allocation
- edge-cloud system
- low-altitude economy
- queue theory
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

# paper-2870 — Dynamic Task Allocation of Edge–Cloud System for Low-Altitude Economy via Multiagent Actor–Critic-Queuing Computational Framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of the low-altitude economy has driven edge-cloud systems to develop resource-optimal task management strategies. The key challenge lies in optimizing computing resource allocation to guarantee real-time responsiveness and feedback. Therefore, to address the task allocation problems within the edge-cloud system for low-altitude economy, we propose a computing framework named multiagent actor–critic-queuing (MA2CQ). Leveraging queueing theory and a multiagent actor–critic architecture, MA2CQ optimizes resource efficiency by minimizing long-term latency and maximizing throughput, formalized via the Witte performance metric. The framework employs rapid parameter iteration updates through the policy gradient reinforcement learning algorithm, enabling real-time scheduling and quick adaptability. Furthermore, we mathematically prove the convergence of the algorithm. The experimental results validate the effectiveness of the designed algorithm. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2870.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
