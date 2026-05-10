---
id: paper-2156
title: Development of an AI-Assisted LoRa-Based Monitoring and Control System with RAG-Enabled Chatbot for Sacha Inchi Cultivation
authors:
- Sinuraya, Enda Wista
- Ramadhan, Iqbal Maulana
- Santoso, Imam
- Aji, Asnur
- Winardi, Bambang
- Setiyono, Budi
venue: International Conference on Computer, Control, Informatics and its Applications, IC3INA
venue_type: conference
year: 2025
doi: 10.1109/IC3INA68387.2025.11325178
url: https://www.scopus.com/pages/publications/105032827458?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 334--339
keywords:
- Conversational AI
- Edge Computing
- Internet of Things
- LoRa
- Precision Agriculture
- Retrieval-Augmented Generation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2156 — Development of an AI-Assisted LoRa-Based Monitoring and Control System with RAG-Enabled Chatbot for Sacha Inchi Cultivation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The cultivation of Sacha Inchi, a crop of high economic and nutritional value due to its rich omega-3, 6, and 9 content, requires precise environmental conditions that are difficult to manage manually, often leading to resource inefficiency and suboptimal yields. This paper presents the design and implementation of an AI-assisted, LoRa-based Internet of Things (IoT) system for the real-time monitoring and control of Sacha Inchi cultivation. The system implements a multi-tier architecture comprising distributed ESP32 sensor nodes, a Raspberry Pi edge gateway with a store-and-forward mechanism for data resilience, and a cloud-based backend for data aggregation. A web application developed with Next.js provides a comprehensive dashboard for data visualization and remote control of irrigation and fertilization. A key innovation is the integration of a Retrieval-Augmented Generation (RAG) enabled chatbot, which queries a knowledge base of project documentation and historical sensor data. This allows users to perform complex analytical queries (e.g., identifying sites with downward soil moisture trends despite recent irrigation) through a natural language interface, a significant improvement over standard chatbots. Testing results demonstrate the system's high responsiveness, with an average control command latency of 1.4 seconds, and the functional reliability of the user interface. The AI agent achieved a 90% success rate in handling complex queries, demonstrating its effectiveness. This work presents a robust and scalable platform, laying the groundwork for optimized resource management and enhanced productivity in precision agriculture. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2156.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
