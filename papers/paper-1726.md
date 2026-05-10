---
id: paper-1726
title: Development of Traffic Rules Training Platform Using LLMs and Cloud Video Streaming
authors:
- Kazarian, Artem
- Teslyuk, Vasyl
- Berezsky, Oleh
- Pitsun, Oleh
venue: Big Data and Cognitive Computing
venue_type: journal
year: 2025
doi: 10.3390/bdcc9120304
url: https://www.scopus.com/pages/publications/105025659817?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- cloud computing
- large language model
- Petri net learning model
- spherical video
- virtual simulator
- VR
- web application
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1726 — Development of Traffic Rules Training Platform Using LLMs and Cloud Video Streaming

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driving safety education remains a critical societal priority, and understanding traffic rules is essential for reducing road accidents and improving driver awareness. This study presents the development and evaluation of a virtual simulator for learning traffic rules, incorporating spherical video technology and interactive training scenarios. The primary objective was to enhance the accessibility and effectiveness of traffic rule education by utilizing modern virtual reality approaches without the need for specialized equipment. A key research component is using Petri net-based models to study the simulator’s dynamic states, enabling the analysis and optimization of system behavior. The developed simulator employs large language models for the automated generation of educational content and test questions, supporting personalized learning experiences. Additionally, a model for determining the camera rotation angle was proposed, ensuring a realistic and immersive presentation of training scenarios within the simulator. The system’s cloud-based, modular software architecture and cross-platform algorithms ensure flexibility, scalability, and compatibility across devices. The simulator allows users to practice traffic rules in realistic road environments with the aid of spherical videos and receive immediate feedback through contextual prompts. The developed system stands out from existing traffic rule learning platforms by combining spherical video technology, large language model-based content generation, and cloud architecture to create a more interactive, adaptive, and realistic learning experience. The experimental results confirm the simulator’s high efficiency in improving users’ knowledge of traffic rules and practical decision-making skills. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1726.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
