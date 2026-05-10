---
id: paper-1448
title: 'Softwarized Edge Intelligence for Advanced IIoT Ecosystems: A Data-Driven Architecture Across the Cloud/Edge Continuum'
authors:
- Carrascal, David
- Díaz-Fuentes, Javier
- Manso, Nicolas
- Lopez-Pajares, Diego
- Rojas, Elisa
- Savi, Marco
- Arco, Jose M.
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app151910829
url: https://www.scopus.com/pages/publications/105031710917?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- AI-driven orchestration
- cloud/edge continuum
- distributed intelligence
- Industrial Internet of Things (IIoT)
- softwarized edge computing
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

# paper-1448 — Softwarized Edge Intelligence for Advanced IIoT Ecosystems: A Data-Driven Architecture Across the Cloud/Edge Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The evolution of Industrial Internet of Things (IIoT) systems demands flexible and intelligent architectures capable of addressing low-latency requirements, real-time analytics, and adaptive resource management. In this context, softwarized edge computing emerges as a key enabler, supporting advanced IoT deployments through programmable infrastructures, distributed intelligence, and seamless integration with cloud environments. This paper presents an extended and publicly available proof of concept (PoC) for a softwarized, data-driven architecture designed to operate across the cloud/edge/IoT continuum. The proposed architecture incorporates containerized microservices, open standards, and ML-based inference services to enable runtime decision-making and on-the-fly network reconfiguration based on real-time telemetry from IIoT nodes. Unlike traditional solutions, our approach leverages a modular control plane capable of triggering dynamic adaptations in the system through RESTful communication with a cloud-hosted inference engine, thus enhancing responsiveness and autonomy. We evaluate the system in representative IIoT scenarios involving multi-agent collaboration, showcasing its ability to process data at the edge, minimize latency, and support real-time decision-making. This work contributes to the ongoing efforts toward building advanced IoT ecosystems by bridging conceptual designs and practical implementations, offering a robust foundation for future research and deployment in intelligent, software-defined industrial environments. © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1448.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
