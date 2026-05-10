---
id: paper-2801
title: 'SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds'
authors:
- Tong, Haogang
- Meng, Chunyang
- Song, Shijie
- Pan, Maolin
- Yu, Yang
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3672566
url: https://www.scopus.com/pages/publications/105032788764?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge-cloud Environ ment
- Graph Convolutional Network
- Microservice Autoscaling
- Multi-Agent Reinforcement Learning
- Quality of Service
- Service-Level Agreements
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

# paper-2801 — SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge-cloud environments constitute a heterogeneous computing paradigm that integrates resource-constrained edge servers with high-performance cloud servers. While microservices have revolutionized large-scale applications development by enhancing scalability and flexibility, achieving efficient microservice autoscaling—the dynamic adjustment of instances to maintain quality of service (QoS) and meet service-level agreements (SLA) targets—remains challenging in such environments. Most existing autoscaling techniques rely on metric forecasting and centralized or per-node control, causing them to overlook temporal evolution and server relationships and resulting in unstable and weakly coordinated scaling. To address these challenges, we present SynScale, a distributed collaborative autoscaling framework that strengthens both temporal sensitivity and structural coordination. SynScale introduces a spatiotemporal representation module that couples a temporal attention network with a multi graph convolutional model. The temporal component distills behavioral trends from recent observations to ensure coherent responses to time-varying dynamics, while the spatial component performs relational reasoning over explicitly modeled inter server correlations to yield structure-aware representations that support effective cross-node coordination. These spatiotemporal embeddings are then used within a multi-agent reinforcement learning paradigm, enabling distributed agents to generate context-aware scaling decisions that align local adaptability with system-wide efficiency. Experimental evaluations against state of-the-art autoscaling techniques show that SynScale reduces average response time by 59.32%, SLA violations by 85.71%, and P95 latency by 73.2%, while also lowering resource cost. It further improves scaling stability—reflected by lower instance time and longer instance lifetimes—and maintains lightweight, scale-stable runtime overhead, ensuring practical deployability in heterogeneous edge-cloud environments. © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2801.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
