---
id: paper-1318
title: 'Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics'
authors:
- Yue, Xiaofei
- Yang, Song
- Zhu, Liehuang
- Trajanovski, Stojan
- Fu, Xiaoming
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2024
doi: 10.1109/INFOCOM52122.2024.10621303
url: https://www.scopus.com/pages/publications/85201815032?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2498--2507
keywords:
- Graph neural networks
- Reinforcement learning
- Current performance
- Decisions makings
- Demeter
- Distributed data
- Fine grained
- Global services
- Large volumes
- Low latency
- Multi-agent reinforcement learning
- Service level objective
- Resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1318 — Demeter: Fine-grained Function Orchestration for Geo-distributed Serverless Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the era of global services, low-latency analytics on large-volume geo-distributed data has been a regular demand for application decision-making. Serverless computing facilitates fast function start-up and deployment, making it an attractive way for geo-distributed analytics. We argue that the serverless paradigm holds the potential to breach current performance bottlenecks via fine-grained function orchestration. However, how to configure it for geo-distributed analytics remains ambiguous. To fill this gap, we present Demeter, a scalable fine-grained function orchestrator for geo-distributed serverless analytics systems. Demeter aims to minimize the composite cost of co-existing jobs while meeting the user-specific Service Level Objectives (SLO). To handle the volatile environments and learn the diverse function demands, a Multi-Agent Reinforcement Learning (MARL) solution is used to co-optimize the per-function placement and resource allocation. The MARL extracts holistic and compact states via hierarchical graph neural networks, and then designs a novel actor network to shrink the huge decision space and model complexity. Finally, we implement Demeter and evaluate it using realistic workloads. The experimental results reveal that Demeter significantly saves costs by 23.3%∼32.7%, while reducing SLO violations by over 27.4%, surpassing state-of-the-art solutions. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1318.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
