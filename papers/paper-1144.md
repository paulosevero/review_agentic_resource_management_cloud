---
id: paper-1144
title: Toward Decentralized Task Offloading and Resource Allocation in User-Centric MEC
authors:
- Qin, Langtian
- Lu, Hancheng
- Chen, Yuang
- Chong, Baolin
- Wu, Feng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2024.3399766
url: https://www.scopus.com/pages/publications/85193249922?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11807--11823
keywords:
- Mobile edge computing
- resource allocation
- task offloading
- user-centric network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1144 — Toward Decentralized Task Offloading and Resource Allocation in User-Centric MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the traditional cellular-based mobile edge computing (MEC), users at the edge of the cell are prone to suffer severe inter-cell interference and signal attenuation, leading to low throughput even transmission interruptions. Such edge effect severely obstructs offloading of tasks to MEC servers. To address this issue, we propose user-centric mobile edge computing (UCMEC), a novel MEC architecture integrating user-centric transmission, which can ensure high throughput and reliable communication for task offloading. Then, we formulate an long-term delay minimization problem by jointly optimizing task offloading, power allocation, and computing resource allocation in UCMEC. To solve the intractable problem, we propose two decentralized joint optimization schemes based on multi-agent deep reinforcement learning (MADRL) and convex optimization, which consider both cooperation and non-cooperation among network nodes. Simulation results demonstrate that the proposed schemes in UCMEC can significantly improve the uplink transmission rate by at least 176.99% and reduce the long-term average total delay by at least 16.36% compared to traditional cellular-based MEC. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1144.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
