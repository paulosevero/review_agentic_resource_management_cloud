---
id: paper-2411
title: 'AdaptiFlow: An Extensible Framework for Event-Driven Autonomy in Cloud Microservices'
authors:
- Zemtsop Ndadji, Brice Arléon
- Bliudze, Simon
- Quinton, Clément
venue: Electronic Proceedings in Theoretical Computer Science, EPTCS
venue_type: conference
year: 2025
doi: 10.4204/EPTCS.438.7
url: https://www.scopus.com/pages/publications/105028571355?origin=resultslist
publisher: Open Publishing Association
pages: 123--147
keywords:
- adaptive workflows
- autonomic computing
- cloud microservices
- decentralized adaptation
- MAPE-K loop
- self-adaptive systems
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

# paper-2411 — AdaptiFlow: An Extensible Framework for Event-Driven Autonomy in Cloud Microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern cloud architectures demand self-adaptive capabilities to manage dynamic operational conditions. Yet, existing solutions often impose centralized control models ill-suited to microservices’ decentralized nature. This paper presents AdaptiFlow, a framework that leverages well-established principles of autonomous computing to provide abstraction layers focused on the Monitor and Execute phases of the MAPE-K loop. By decoupling metrics collection and action execution from adaptation logic, AdaptiFlow enables microservices to evolve into autonomous elements through standardized interfaces, preserving their architectural independence while enabling system-wide adaptability. The framework introduces: (1) Metrics Collectors for unified infrastructure/business metric gathering, (2) Adaptation Actions as declarative actuators for runtime adjustments, and (3) a lightweight Event-Driven and rule-based mechanism for adaptation logic specification. Validation through the enhanced Adaptable TeaStore benchmark demonstrates practical implementation of three adaptation scenarios targeting three levels of autonomy—self-healing (database recovery), self-protection (DDoS mitigation), and self-optimization (traffic management)—with minimal code modification per service. Key innovations include a workflow for service instrumentation and evidence that decentralized adaptation can emerge from localized decisions without global coordination. The work bridges autonomic computing theory with cloud-native practice, providing both a conceptual framework and concrete tools for building resilient distributed systems. Future work includes integration with formal coordination models and application of adaptation techniques relying on AI agents for proactive adaptation to address complex adaptation scenarios. © B.A. Zemtsop Ndadji, S. Bliudze & C. Quinton.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2411.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
