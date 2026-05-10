---
id: paper-2367
title: Intelligent Computation Offloading and Trajectory Planning for 3-D Target Search in Low-Altitude Economy Scenarios
authors:
- Yang, Helin
- Zheng, Mengting
- Shao, Ziling
- Jiang, Yifu
- Xiong, Zehui
venue: IEEE Wireless Communications Letters
venue_type: journal
year: 2025
doi: 10.1109/LWC.2025.3527005
url: https://www.scopus.com/pages/publications/105002490253?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 949--953
keywords:
- anti-jamming
- Autonomous aerial vehicle
- edge computing
- ground vehicle
- reinforcement learning
- target search
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2367 — Intelligent Computation Offloading and Trajectory Planning for 3-D Target Search in Low-Altitude Economy Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The low-altitude economy provides new opportunities for target search, as autonomous aerial vehicles (AAVs) improve search efficiency through aerial surveillance and data collection. AAVs support overhead views of the search area, while ground vehicles (GVs) offer side views, facilitating effective collaboration in wireless networks. However, the limited battery life restrict AAVs from performing computation-intensive and latency-sensitive tasks, and their wireless communication links are susceptible to jamming attacks. Therefore, this letter proposes a joint resource scheduling approach for an edge computing enabled multi-AAV multi-GV cooperative target search system under intelligent jamming attacks. Specifically, the approach aims to minimize the uncertainty of the search area by jointly optimizing ground base station (GBS) association, task offloading rate, and 3D trajectory control. Since the problem is non-convex and the intelligent jamming behavior is dynamic, a multi-agent softmax deep double deterministic policy gradients (MA-SD3) approach is proposed to effectively perform resource management for target search and resist jamming attacks. Simulation results demonstrate that the proposed approach outperforms the baseline approaches under different settings.  © 2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2367.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
