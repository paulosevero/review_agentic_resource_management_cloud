---
id: paper-2634
title: 'Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments'
authors:
- Keum, Chaewon
- Song, Yelin
- Lee, Seoyoung
- Cho, Kyungwoon
- Bahn, Hyokyung
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/app16073484
url: https://www.scopus.com/pages/publications/105035601821?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- decentralized scheduling
- distributed hash table (DHT)
- distributed orchestration
- fault tolerance
- task scheduling
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

# paper-2634 — Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Featured Application: Decentralized resource orchestration for computing environments where nodes can freely join and leave, such as loosely coupled research infrastructures, community clusters, and edge systems. Today, many computing workloads are executed in loosely coupled, geographically distributed environments where resources are owned by different organizations. Examples include inter-institutional research infrastructures, community-operated clusters, and edge deployments. As disconnections are frequent in such environments, ensuring reliable task execution remains a fundamental challenge. Kubernetes, the de facto standard for cluster orchestration, provides centralized control and strong consistency, but suffers from slow recovery when node failures occur frequently. At the opposite extreme, blockchain-based orchestration removes centralized control but incurs substantial latency due to global consensus, making it unsuitable for time-sensitive task scheduling. This paper presents Mutual Cloud, a decentralized orchestration framework that operates between these two extremes. Mutual Cloud adopts a hybrid architecture where task admission and queue management are handled in a centralized manner similar to conventional public clouds, whereas most scheduling functions, including execution-node selection and failure handling, are performed in a decentralized manner by autonomous agents using a distributed hash table. We implement a prototype of Mutual Cloud and evaluate its performance through large-scale simulation studies. The results show that Mutual Cloud maintains stable performance comparable to centralized baselines under normal conditions while achieving approximately five-second-level recovery latency under substantial node failures. © 2026 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2634.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
