---
id: paper-0944
title: 'AFL-DMAAC: Integrated Resource Management and Cooperative Caching for URLLC-IoV Networks'
authors:
- Hazarika, Bishmita
- Singh, Keshav
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2024
doi: 10.1109/TIV.2023.3303932
url: https://www.scopus.com/pages/publications/85167816815?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5101--5117
keywords:
- Caching
- federated learning
- Internet of Vehicles (IoV) networks
- resource management
- ultra-reliable low-latency communication (URLLC)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0944 — AFL-DMAAC: Integrated Resource Management and Cooperative Caching for URLLC-IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, we propose a novel approach for optimal resource management and caching in ultra-reliable low-latency communication (URLLC)-enabled Internet of Vehicles (IoV) networks. The proposed framework includes mobile edge computing (MEC) servers integrated into roadside units (RSUs), unmanned aerial vehicles (UAVs), and base stations (BSs) for hybrid vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication. To enhance the accuracy of the global model while considering the mobility characteristics of vehicles, we leverage an asynchronous federated learning (AFL) algorithm. The problem of optimal resource allocation is formulated to achieve the best allocation of frequency, computation, and caching resources while complying with the delay restrictions. To solve the non-convex problem, a multi-agent actor-critic type deep reinforcement learning algorithm called DMAAC algorithm is introduced. Additionally, a cooperative caching scheme based on the AFL framework called Co-Ca is proposed, utilizing a Dueling Deep-Q-Network (DDQN) to predict frequently accessed contents and cache them efficiently. Extensive simulation results show the effectiveness of the proposed framework and algorithms compared to existing schemes. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0944.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
