---
id: paper-0730
title: Privacy-Aware Intelligent Healthcare Services with Federated Learning Architecture and Reinforcement Learning Agent
authors:
- Tam, Prohim
- Song, Inseok
- Kang, Seungwoo
- Kim, Seokhoon
venue: Lecture Notes in Electrical Engineering
venue_type: conference
year: 2023
doi: 10.1007/978-981-99-1252-0_78
url: https://www.scopus.com/pages/publications/85164005729?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 583--590
keywords:
- Federated learning
- Intelligent healthcare
- Internet of healthcare things
- Network functions virtualization
- Reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0730 — Privacy-Aware Intelligent Healthcare Services with Federated Learning Architecture and Reinforcement Learning Agent

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of digital health systems, Internet of Healthcare Things (IoHT), and Deep Learning (DL) offers intelligent healthcare services to deploy in medical software development with extended decision-making modules. However, the communication reliability and information privacy of data-driven model integration remain a challenging topic to further discuss by researchers and standard organizations. From a real-time communication perspective, the standard of Quality-of-Service requirements in smart healthcare is within real-time services, which permits extremely low packet delay budget and error loss rate. To jointly generate a delay-aware, reliability-aware, and privacy-aware approaches in intelligent healthcare services (e.g. DL-based medical software), there are three key essential aspects, namely distributed edge learning, resource virtualization, and model slicing orchestration. This paper presents optimized Federated Learning (FL) architecture based on autonomous agent policies (resource placement and slicing orchestration) using reinforcement learning. The system architecture outlines large-scale IoHT deployment in wireless cellular networks, network functions virtualization-enabled edge computing placement, and converged FL components. The communication and computation models tackle the utilization efficiencies of bandwidth, energy, and computing capacities. This proposed optimization approach strengthens privacy and reliability by orchestrating through different weights of slicing prioritization in multi-intelligent healthcare services such as non-real-time/real-time modelling, telemedicine, and remote operation (e.g. telesurgery). © 2023, The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0730.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
