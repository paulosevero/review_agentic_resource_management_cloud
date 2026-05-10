---
id: paper-1511
title: End-Edge Collaborative Optimization of Microservice Caching in D2D-Assisted Network
authors:
- Deng, Qingyong
- Li, Mengyao
- Li, Zhetao
- Liu, Haolin
- Xie, Yong
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3582579
url: https://www.scopus.com/pages/publications/105009116604?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12162--12176
keywords:
- bandit learning
- Edge caching
- end-edge collaboration
- microservice caching
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

# paper-1511 — End-Edge Collaborative Optimization of Microservice Caching in D2D-Assisted Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Employing the caching resources of end users via Device-to-Device (D2D) communication to assist the edge server in microservice caching is promising to further alleviate the network congestion of the Internet of Things (IoT). However, significant extra energy consumption prevents the caching system from maximizing cache utility if all end users cache simultaneously. In this paper, we propose two novel end-edge collaborative microservice caching algorithms in D2D-assisted networks. First, we construct a D2D caching sharing link graph from the aspects of physical and social attributes of end users and introduce the Entropy-based Partitioning Around Medoid (EPAM) algorithm to identify critical users. Second, to address the challenges posed by unknown time-varying user preferences, we model the end-edge collaborative caching problem as a Multi-Agent Multi-Armed Bandit (MAMAB) problem, thus developing two caching decision schemes, i.e, Edge-Centric Scheme (ECS) and User-Centric Scheme (UCS), to accommodate different decision sequences. The simulation results show that the EPAM-ECS and EPAM-UCS have at least 29.2% and 39.3% improvement compared with other baseline algorithms. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1511.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
