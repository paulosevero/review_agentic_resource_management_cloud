---
id: paper-1863
title: A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents
authors:
- Liu, Ya
- Yang, Kai
- Zhu, Yu
- Yang, Keying
- Jian, Chengtao
- Ni, Wuguang
- Ye, Xiaozhou
- Ouyang, Ye
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-8186-0_1
url: https://www.scopus.com/pages/publications/105009402614?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 3--15
keywords:
- Fine-tuning
- Large language models
- Zeroth-order optimization
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

# paper-1863 — A Nested Zeroth-Order Fine-Tuning Approach for Cloud-Edge LLM Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) are transforming the landscape of generative AI. Yet, their immense model sizes tether most LLMs to cloud environments, hindering their adaptability to specific downstream tasks and presenting challenges for scenarios involving private data. To address these issues, we propose a novel fine-tuning approach for end-to-end collaboration between a cloud-hosted LLM and an edge-based LLM agent, leveraging a Sandwiched Tuning framework. This approach not only boosts flexibility and scalability but also empowers users with heightened security and compliance, allowing tradeoffs between performance and cost. The proposed framework models cloud-edge collaboration as a nested optimization problem, which is under a grey-box constraint due to the cloud LLM’s parameters’ unavailability. Tailored to the unique problem structure, we introduce a computationally efficient nested Zeroth-order Cutting Plane (ZoCP) algorithm. We explore various collaboration modes, both parallel and serial, and conduct experiments to verify our effectiveness in each mode. Our extensive experiments reveal that our method delivers up to a 47.9% performance improvement over traditional methods. Additionally, we establish a convergence rate for ZoCP that is independent of the number of optimization parameters, highlighting its scalability on large-scale edge LLMs. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1863.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
