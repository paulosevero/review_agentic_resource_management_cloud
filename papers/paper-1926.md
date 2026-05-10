---
id: paper-1926
title: A deep multi-agent reinforcement learning approach for the micro-service migration problem with affinity in the cloud
authors:
- Ma, Ning
- Tang, Angjun
- Xiong, Zifeng
- Jiang, Fuxin
venue: Expert Systems with Applications
venue_type: journal
year: 2025
doi: 10.1016/j.eswa.2025.126856
url: https://www.scopus.com/pages/publications/85218173202?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Deep reinforcement learning
- Invoking traffic
- Micro-service
- Migration
- Resource optimization
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

# paper-1926 — A deep multi-agent reinforcement learning approach for the micro-service migration problem with affinity in the cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper focuses on the micro-service migration problem with affinity, stemming from the cloud computing industry. Because of periodically creating and deleting micro-services to satisfy users’ demands, the deployment of micro-services in the cloud needs to be regularly adjusted, which is referred to as a micro-service migration. An optimal migration schedule should minimize the number of activated physical machines as well as maximize total internal invoking traffic (affinity). A cooperative multi-agent reinforcement learning (MARL) is proposed, which is enhanced by integrating Hindsight Reward Shaping and by fine-tuning the state encoder using a pre-trained ResNet model. The proposed MARL is validated on both synthetic datasets and real cloud traces of ByteDance and Alibaba, compared with four baseline algorithms: Migration Ant Colony Optimization, Migration Neighborhood Search, Single-Agent Reinforcement Learning, and the optimization solver CPLEX. Finally, an evaluation mechanism called Matching Score is proposed to explain the superior performance of MARL. © 2025 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1926.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
