---
id: paper-2632
title: 'MADQL: Multi-Agent Deep Q-Learning for Optimized Job Scheduling in Serverless Computing'
authors:
- Kaur, Jasmine
- Chana, Inderveer
- Bala, Anju
venue: Arabian Journal for Science and Engineering
venue_type: journal
year: 2026
doi: 10.1007/s13369-025-10461-x
url: https://www.scopus.com/pages/publications/105012030425?origin=resultslist
publisher: Springer Nature
pages: 5701--5720
keywords:
- AWS Lambda
- Job scheduling
- Multi-agent deep Q-Learning
- Performance
- Serverless computing
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
    my_justification: RL
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

# paper-2632 — MADQL: Multi-Agent Deep Q-Learning for Optimized Job Scheduling in Serverless Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing has gained significant interest as it allows service providers to manage resources efficiently. In serverless systems, providers are highly motivated to use their infrastructure cost-effectively due to the detailed billing modules involved. However, the dynamic nature of serverless workloads presents challenges in maintaining function performance and resource efficiency in parallel processing and distributed computing applications. The existing heuristic scheduling techniques fail to capture the true dynamism and often overlook resource efficiency and application performance. The Single-Agent Deep Q-Learning (SADQL) approach optimizes decisions in simpler environments but struggles to handle the complexity and demand of dynamic serverless environments. A multi-agent Deep Q-Learning (MADQL) framework has been proposed to overcome these limitations. Multiple agents interact with the system that dynamically scales up or down by addressing overutilization and underutilization in serverless applications. Further, experimental analysis has been conducted on a real-world dataset through AWS Lambda. It demonstrates significant improvements, including a 0.96% reduction in average response time, a 1.46% decrease in costs, a 2.43% reduction in energy consumption, and a 15.79% decrease in CPU utilization. © King Fahd University of Petroleum & Minerals 2025.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2632.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
