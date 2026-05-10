---
id: paper-2178
title: Energy-Privacy Tradeoff for Task Matching in Edge Computing Power Networks
authors:
- Sui, Liyan
- Huang, Xiaoyan
- Zhang, Ke
- Zhang, Yin
- Wu, Fan
- Guan, Xin
- Xu, Shujiang
- Zhang, Yan
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2025
doi: 10.1109/TCC.2025.3614339
url: https://www.scopus.com/pages/publications/105017683345?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1315--1326
keywords:
- differential privacy
- Edge computing power network (EdgeCPN)
- energy-privacy tradeoff
- task matching
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

# paper-2178 — Energy-Privacy Tradeoff for Task Matching in Edge Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The sixth-generation (6G) networks aim to achieve ubiquitous intelligent connectivity while ensuring extremely low latency, reducing energy consumption, and enhancing privacy protection. Mobile edge computing (MEC) offers an effective solution to reduce latency and energy consumption by leveraging resources near end devices for task offloading. However, MEC faces significant challenges in meeting the requirements of 6G networks, including limited computational resources, high mobility, and strict data privacy demands. Efficiently allocating edge resources while preserving privacy has become a critical issue for realizing the objectives of 6G networks. In this paper, we propose a privacy-preserving edge computing power network (EdgeCPN) model that jointly leverages the computing resources of edge computing nodes and protects sensitive computing power information through differential privacy methods. In addition, we propose a task matching problem that aims to minimize the privacy-budget-weighted energy consumption while ensuring privacy protection and meeting task requirements. We propose a dynamic graph-based multiagent reinforcement learning (MADRL) algorithm to find the optimal strategy for task matching and computing resource allocation with privacy protection. The results show that our proposed task matching model with energy and privacy tradeoffs can minimize the energy consumption in the matching process while ensuring privacy, and the algorithm can find the optimal strategy for task matching efficiently. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2178.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
