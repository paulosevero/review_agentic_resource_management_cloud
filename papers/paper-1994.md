---
id: paper-1994
title: 'Data Center Scale Disaggregated Computing with Next Generation Computing Technology: ExpEther (“ExpressEther”)'
authors:
- Niino, Ryuta
- Higuchi, Junichi
- Hidaka, Yoichi
venue: 2025 PhotonIcs and Electromagnetics Research Symposium - Fall, PIERS-FALL 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.23919/PIERS-Fall62445.2025.11393997
url: https://www.scopus.com/pages/publications/105035828515?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computer architecture
- Computer resource management
- Data centers
- Distributed computer systems
- Graphics processing unit
- Program processors
- Computing architecture
- Computing technology
- Cooling performance
- Datacenter
- Market sizes
- Performance
- Power densities
- Resources utilizations
- Traditional computers
- Utilization efficiency
- Network architecture
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

# paper-1994 — Data Center Scale Disaggregated Computing with Next Generation Computing Technology: ExpEther (“ExpressEther”)

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, the rapid adoption of generative AI has led to a surge in demand for AI data centers, and the market size is expected to reach about five times its 2025 size by 2032. Along with this, new issues such as increasing power density, ensuring cooling performance, and improving GPU utilization efficiency due to the massive use of high-performance GPUs have become new challenges. Traditional computer architectures have a fixed connection between the CPU and GPU, limiting flexibility in cooling and resource utilization. To solve these problems, this paper proposes a next-generation disaggregated computing architecture that can separate the CPU from GPUs and other I/O by combining three types of technologies: distributed PCI Express switch technology, low-latency and high-reliability Ethernet network technology, and flexible resource management technology. © PIERS-FALL 2025.All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1994.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
