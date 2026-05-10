---
id: paper-1592
title: 'Federated Load Balancing in Smart Cities: A 6G, Cloud, and Agentic AI Perspective'
authors:
- Gillgallon, Rohin
- Bergami, Giacomo
- Morgan, Graham
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app152010920
url: https://www.scopus.com/pages/publications/105020024432?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- Agentic AI
- cloud simulator
- edge simulator
- IoT simulator
- osmotic simulator
- SimulatorOrchestrator
- VANET Simulator
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
    my_justification: Out of scope
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

# paper-1592 — Federated Load Balancing in Smart Cities: A 6G, Cloud, and Agentic AI Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern smart cities are comprised of multiple sensors, all with their own collection of communicating devices transmitting data towards cloud data centres for analysis. Smart cities have limited bandwidth resources, which, if not managed correctly, can lead to network bottlenecks. These bottlenecks are commonly addressed through bottleneck mitigation strategies and load balancing algorithms, which aim to maximise the throughput of a smart city’s network infrastructure. Network simulators are a crucial tool for developing and testing bottleneck mitigation and load balancing techniques before deployment in real systems; however, many network simulators are developed as single-purpose tools, aiming to simulate a particular subset of an overarching use case. Such tools are therefore unable to model a real-world smart city infrastructure, which receives communications across a wide range of scenarios and from a wide variety of devices. This paper surveys the current state-of-the-art for network simulation tools, modern bottleneck mitigation strategies and load balancing techniques, evaluating each in terms of its suitability for smart cities and smart city simulation. This survey finds there is a lack of current network simulation tools up to the task of modelling smart city infrastructure and found no such simulation tools capable of modelling both smart city infrastructure and implementing the state-of-the-art bottleneck mitigation and load balancing strategies outlined within this work, highlighting this as a significant gap in current research before providing future work suggestions, including a federated approach for future simulation tools. © 2025 by the authors.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1592.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
