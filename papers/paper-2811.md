---
id: paper-2811
title: Collective intelligence-based service migration enabling zoom-in functionality within industry 5.0
authors:
- Venanzi, Riccardo
- Colombi, Lorenzo
- Tazzioli, Davide
- Dahdal, Simon
- Tortonesi, Mauro
- Foschini, Luca
venue: Internet of Things (The Netherlands)
venue_type: journal
year: 2026
doi: 10.1016/j.iot.2025.101830
url: https://www.scopus.com/pages/publications/105023660952?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Artificial intelligence
- Collective intelligence
- Industrial internet of things
- Industry 5.0
- Kubernetes
- Service migration
- Zoom-In functionality
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

# paper-2811 — Collective intelligence-based service migration enabling zoom-in functionality within industry 5.0

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid evolution of Industry 5.0 emphasizes the integration of human expertise with machine intelligence to create resilient, adaptive, and human-centric industrial systems. This paper introduces a novel Collective Intelligence (CI)-based service migration framework designed for Industry 5.0 environments, enabling dynamic orchestration of stateful services across heterogeneous edge-to-cloud infrastructures. At its core, the framework leverages Kubernetes (K8s) enhanced with AI-driven decision-making and human-in-the-loop collaboration to address the limitations of traditional orchestration in industrial settings. A key innovation of this work is the Zoom-In functionality, which empowers human operators to escalate anomaly detection and analysis by deploying advanced machine learning models on demand, seamlessly migrating services to resource-rich nodes when deeper investigation is warranted. The proposed framework integrates Large Language Models (LLMs) to translate operator intent into actionable policies, ensuring context-aware and explainable decision-making. Experimental validation in real industrial scenarios demonstrates high anomaly detection accuracy (F1-scores up to 1.0), reliable operator intent translation (over 70 % correct JSON generations with lightweight LLMs), and efficient multi-criteria scheduling with millisecond-level decision times. Moreover, the proposed migration mechanism reduces downtime by more than 50 % compared to vanilla Kubernetes, ensuring service continuity in mission-critical tasks. This work advances the vision of collaborative intelligence in IoT systems, bridging the gap between human judgment and automated orchestration for Industry 5.0 applications. © 2025 The Author(s)

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2811.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
