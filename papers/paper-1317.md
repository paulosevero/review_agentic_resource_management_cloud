---
id: paper-1317
title: 'Orchestration of Emulator Assisted 6G Mobile Edge Tuning for AI Foundation Models: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Yu, Wenhan
- Chua, Terence Jie
- Zhao, Jun
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2024
doi: 10.1109/VTC2024-Spring62846.2024.10683262
url: https://www.scopus.com/pages/publications/85206185746?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6G
- deep reinforcement learning
- foundation model
- Mobile edge computing
- parameter efficient finetuning
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

# paper-1317 — Orchestration of Emulator Assisted 6G Mobile Edge Tuning for AI Foundation Models: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The efficient deployment and fine-tuning of foundation models are pivotal in contemporary artificial intelligence. In this study, we present a groundbreaking paradigm inte-grating 6G Mobile Edge Computing (MEC) with foundation models, specifically designed to enhance local task performance on user equipment (UE). Central to our approach is the innovative Emulator-Adapter architecture, segmenting the foundation model into two cohesive modules. This design not only conserves computational resources but also ensures adaptability and fine-tuning efficiency for downstream tasks. Additionally, we introduce an advanced resource allocation mechanism that is fine-tuned to the needs of the Emulator-Adapter structure in decentralized settings. To address the challenges presented by this system, we employ a hybrid multi-agent Deep Reinforcement Learning strategy, adept at handling mixed discrete-continuous action spaces, ensuring dynamic and optimal resource allocations. Our comprehensive simulations and validations underscore the practical viability of our approach, demonstrating its robustness, efficiency, and scalability. Collectively, this work offers a fresh perspective on deploying foundation models and balancing computational efficiency with task proficiency. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1317.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
