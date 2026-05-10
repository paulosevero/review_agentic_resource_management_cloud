---
id: paper-0704
title: Reinforcement Learning Based Control Scheme for Emergency Vehicle Preemption with Edge Computing
authors:
- Rosayyan, Prakash
- Paul, Jasmine
- Subramaniam, Senthilkumar
- Ganesan, Saravana Ilango
venue: International Journal of Intelligent Transportation Systems Research
venue_type: journal
year: 2023
doi: 10.1007/s13177-022-00334-0
url: https://www.scopus.com/pages/publications/85143212876?origin=resultslist
publisher: Springer
pages: 48--62
keywords:
- Actor-critic network
- Edge computing technique
- Emergency vehicle flow control
- Emergency vehicle preemption
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0704 — Reinforcement Learning Based Control Scheme for Emergency Vehicle Preemption with Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper proposes a reinforcement learning-based collaborative multi-agent actor and critic scheme (RL-CMAS) under edge computing architecture for emergency vehicle preemption. The RL-CMAS deployed a parallel training process at the cloud side for building knowledge and well accelerating learning. Priority of message and model of message offloading strategy have been developed. The simulation results show that the proposed RL-CMAS is efficient in detecting even complex data. Finally, a comparison was made with other benchmark methods, namely, Regular scheduling algorithm, Alameddine’s DTOS algorithm, and independent multi-agent actor-critic. The result showed the proposed method outperforming the other three bench marking methods. The proposed RL-CMAS provides reduction in message processing delay, total delay, and an increase of message delivery success ratio of 14.22%, 18.21%, and 8.86% respectively. © 2022, The Author(s), under exclusive licence to Intelligent Transportation Systems Japan.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0704.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
