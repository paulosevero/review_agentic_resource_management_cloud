---
id: paper-1125
title: Digital Twin-Assisted Space-Air-Ground Integrated Networks for Vehicular Edge Computing
authors:
- Paul, Anal
- Singh, Keshav
- Nguyen, Minh-Hien T.
- Pan, Cunhua
- Li, Chih-Peng
venue: IEEE Journal on Selected Topics in Signal Processing
venue_type: journal
year: 2024
doi: 10.1109/JSTSP.2023.3340107
url: https://www.scopus.com/pages/publications/85179791398?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 66--82
keywords:
- deep reinforcement learning
- Digital twin
- space-air-ground integrated networks
- ultra-reliable low-latency communications
- vehicular edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1125 — Digital Twin-Assisted Space-Air-Ground Integrated Networks for Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we present a framework that integrates digital twin (DT) technology into space-air-ground integrated networks (SAGINs) to enhance vehicular edge computing (VEC). Our objective is to efficiently offload tasks in ultra-reliable low-latency communications (URLLC)-enabled vehicular networks, focusing on minimizing overall latency for requested tasks by reducing transmission time for task offloading and edge processing requirements. The proposed framework leverages DT-assisted SAGINs to minimize task offloading latency, expand network coverage, and reduce energy consumption. Key components of our framework include partial task offloading, distributed edge computing, latency modeling, energy consumption analysis, mobility, and channel modeling. We formulate a non-convex optimization problem considering various network constraints to achieve the system objective. To solve this optimization problem, we develop a novel multi-agent deep reinforcement learning (DRL) algorithm, enabling intelligent decision-making by individual agents. Through extensive simulations, we validate the effectiveness of our proposed system in advancing VEC by integrating DT technology into SAGINs.  © 2007-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1125.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
