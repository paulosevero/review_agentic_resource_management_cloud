---
id: paper-0644
title: Federated Online Learning Aided Multi-Objective Proactive Caching in Heterogeneous Edge Networks
authors:
- Li, Tan
- Song, Linqi
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2023
doi: 10.1109/TCCN.2023.3262243
url: https://www.scopus.com/pages/publications/85151558235?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1080--1095
keywords:
- federated online learning
- heterogeneous edge network
- multi-objective learning
- Proactive caching
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

# paper-0644 — Federated Online Learning Aided Multi-Objective Proactive Caching in Heterogeneous Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the drastic increase in multimedia traffic volume, mobile edge caching (MEC) has been exploited to reduce redundant data transmissions by equipping computation and storage capacity at the edge network. Previous works on learning-based caching problems often only concern pre-storing popular contents to satisfy users' demands. In this work, we investigate the cache strategy design problem with two possibly conflicting objectives, namely, cache hit and cache profit, in heterogeneous multi-MEC server networks when content profiles are unknown. We then formulate this multi-objective caching problem as a Multi-agent Multi-objective Combinatorial Multi-Armed bandit (MMC-MAB) problem and propose a two-step caching framework that estimates content properties first and then optimizes cache placement. Specifically, to accommodate the system heterogeneity in estimation, we utilize an adaptive federated learning-based estimation to approach the unknown content popularity and profit profiles, which wisely use both local and external observations by adjusting the mixing factors. To address the multiple objective optimizations, we propose two effective methods, based on individual dominance and combinatorial dominance, to achieve adequate Pareto-optimal cache placement. Both theoretical results and comprehensive experiments clearly validate the effectiveness and efficiency of our proposed approaches.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0644.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
