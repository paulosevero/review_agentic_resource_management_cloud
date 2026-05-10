---
id: paper-2617
title: Personalized LLM Service Updating in Collaborative Edge-Enabled Vehicle Autonomous System
authors:
- Huo, Dongkun
- Yin, Jiajie
- Liu, Hongbo
- Hao, Yixue
- Wang, Rui
- Hu, Long
- Mo, Yijun
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2026
doi: 10.1109/TCE.2025.3644688
url: https://www.scopus.com/pages/publications/105025430401?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1923--1935
keywords:
- communication
- Edge network
- LLM
- multi-agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2617 — Personalized LLM Service Updating in Collaborative Edge-Enabled Vehicle Autonomous System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Personalized services are increasingly critical for autonomous systems such as smart vehicles, where Large Language Models (LLMs) enhance the driving experience. However, efficiently deploying and continuously updating these models is challenging due to resource constraints and dynamic environments. Existing approaches often neglect personalization and effective cross-edge collaboration, leading to inconsistent service quality and inefficient resource utilization. To address these gaps, we propose a vehicle-edge-cloud collaborative framework centered on our Intent-Driven Multi-Agent Communication (IDMAC) algorithm. IDMAC intelligently coordinates the LLM update lifecycle. It utilizes an intent encoder to model the short-term goals of each edge server from its trajectory. This explicit intent then guides attention mechanisms to facilitate efficient, goal-aligned communication, reducing network overhead and focusing on relevant information. This allows for the dynamic scheduling and routing of parameter-efficient model patches. In our architecture, lightweight models are deployed on vehicles, edge servers handle specialized fine-tuning, and the cloud periodically aggregates global knowledge to create unified updates. Experimental results show that the proposed framework significantly improves service quality and adaptability. IDMAC also strengthens inter-edge collaboration while reducing latency and energy consumption. © 2015 IEEE. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2617.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
