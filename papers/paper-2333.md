---
id: paper-2333
title: Edge-Collaborative Model Reuse for Low-Latency AI Task Scheduling with Attention-based Soft Actor-Critic
authors:
- Xu, Zhifei
- Tang, Zhiqing
- Xie, Xuan
- Lou, Jiong
- Guo, Jianxiong
venue: 2025 International Conference on Sensor-Cloud and Edge Computing System, SCECS 2025
venue_type: conference
year: 2025
doi: 10.1109/SCECS65243.2025.11065659
url: https://www.scopus.com/pages/publications/105012244960?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 173--178
keywords:
- Attention
- I Task
- Low-latency Scheduling
- Soft Actor-CriticA
- Soft Actor-CriticI Task
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

# paper-2333 — Edge-Collaborative Model Reuse for Low-Latency AI Task Scheduling with Attention-based Soft Actor-Critic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing use of AI and large language models has driven the deployment of Generative AI (GenAI) in cloud data centers. However, the inherent latency and high resource costs associated with large AI models are problematic for latency-sensitive edge users. While edge server deployment can reduce transmission times, it often leads to underutilized resources and suboptimal trade-offs between inference latency and quality. This paper introduces an Edge-Collaborative AI Task scheduling (CAT) algorithm that combines model reuse to reduce latency. We address AI task scheduling for edge servers by segmenting tasks and distributing patches, considering model distribution and cold starts. We propose a soft actor-critic-based algorithm, CAT, which uses an attention layer to learn complex edge system dynamics. Simulations in a task scheduling environment demonstrate that CAT reduces inference latency by up to 25% compared to baseline methods.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2333.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
