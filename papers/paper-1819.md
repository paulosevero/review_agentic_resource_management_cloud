---
id: paper-1819
title: Research on Energy-Saving and Optimization Control of Data Center Cooling Systems
authors:
- Li, Yongkang
- Cen, Jian
venue: 2025 7th International Conference on Internet of Things, Automation and Artificial Intelligence, IoTAAI 2025
venue_type: conference
year: 2025
doi: 10.1109/IoTAAI66837.2025.11213074
url: https://www.scopus.com/pages/publications/105022298660?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 524--527
keywords:
- Data Center
- Distributed
- Energy Saving
- Multi-Agent
- Optimization Control
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1819 — Research on Energy-Saving and Optimization Control of Data Center Cooling Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This thesis focuses on the high energy consumption issue of data center cooling systems. The research analyzes distributed control technology, abstracting the air conditioning equipment or terminal units in the data center cooling system as a series of intelligent agent nodes with independent control capabilities. Each agent can independently perform parameter monitoring, decision-making calculations, and instruction execution, while agents can collaborate to accomplish various complex system control tasks. Compared to the centralized control architecture currently widely used, the distributed control architecture has the advantages of high flexibility, strong scalability, and high fault tolerance. Due to the "independent control and collaborative optimization"characteristics of the distributed control architecture, achieving optimized control under this architecture is a problem that needs to be solved in this field. In response to the challenges faced in practical applications, such as the high difficulty of developing distributed strategies, low distributed optimization efficiency, and reliability issues of optimization results, this paper summarizes and compares the traditional control optimization methods for data center cooling systems and multi-agent distributed control technologies through analysis. The application and promotion of these technologies will help break the current high energy consumption status of data center cooling systems and are of great significance for energy saving in the operation of public buildings.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1819.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
