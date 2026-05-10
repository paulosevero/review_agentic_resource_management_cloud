---
id: paper-0844
title: A migration strategy based on cluster collaboration predictions for mobile edge computing-enabled smart rail system
authors:
- Cao, Junjie
- Yu, Zhiyong
- Yang, Jian
venue: Journal of Supercomputing
venue_type: journal
year: 2024
doi: 10.1007/s11227-024-06058-0
url: https://www.scopus.com/pages/publications/85189207776?origin=resultslist
publisher: Springer
pages: 15330--15361
keywords:
- Deep reinforcement learning
- Markov decision processes
- Service migration strategies
- Smart rail system
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

# paper-0844 — A migration strategy based on cluster collaboration predictions for mobile edge computing-enabled smart rail system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As an important part of modern transportation, smart rail system need to handle a large number of delay-sensitive and task-intensive tasks in a high-speed mobile state. However, high-speed mobility challenges the traditional information processing modes a lot, such as service interruptions and information congestion. In order to solve these problems, we proposed a service migration strategy based on intelligent agent group cooperative prediction combined with edge computing service migration technology. The aim is to reduce system latency and overhead and ensure service continuity. Firstly, we constructed a cloud-edge-end collaborative scheduling network architecture model for distributed smart rail system is constructed, integrating mobility management and business orchestration to provide effective support for intelligent decision-making. Then we proposed an intelligent grouping collaborative migration strategy by consolidating resources for similar or identical tasks and employing a group negotiation mechanism, where the migration process is divided into four steps: detection, interaction, coordination and execution. Finally, a deep reinforcement learning algorithm is utilized to train multi-agent models for group collaborative prediction in edge migration strategies. The strategy dynamically adjusts task migration between edge nodes and the cloud based on real-time system status and task requirements to optimize its performance. Experimental results show that the proposed architecture and algorithm can effectively reduce total task delay and system overhead. Instead it can guarantee migration rate for task-intensive requirements, and effectively improve the reliability, effectiveness, and safety of smart rail system services. The present study lays a foundation for the future researches on applications of smart rail system. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0844.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
