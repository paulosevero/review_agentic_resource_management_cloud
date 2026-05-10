---
id: paper-1473
title: MAPPO-assisted Joint Task Offloading and Resource Allocation for Energy Efficiency in Dynamic NOMA-MEC Systems
authors:
- Chen, Jiao
- Wu, Yahui
- Huangfu, Xianpeng
- Ma, Wubin
- Zhou, Haohao
venue: 2025 7th International Conference on Artificial Intelligence Technologies and Applications, ICAITA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAITA67588.2025.11137900
url: https://www.scopus.com/pages/publications/105017958065?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 155--164
keywords:
- Convex Approximation
- MAPPO
- Mobile Edge Computing
- NOMA
- Quadratic Transformation
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
    my_justification: RL
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

# paper-1473 — MAPPO-assisted Joint Task Offloading and Resource Allocation for Energy Efficiency in Dynamic NOMA-MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) improves how well devices work and saves energy by moving computing tasks to nearby servers, while Non-Orthogonal Multiple Access (NOMA) makes better use of available bandwidth, making NOMA-MEC networks a very interesting area for research. However, most current research uses fixed channel assumptions and single-agent reinforcement learning methods, which do not account for the changing nature of real network channels and overlook the benefits of using multiple agents. To solve these problems, we suggest a new multi-agent reinforcement learning (MARL) system that can adjust offloading choices and resource distribution in NOMA-MEC networks as network conditions change over time. The proposed method employs quadratic transformation and convex approximation for efficient resource allocation and adopts a multi-agent MAPPO algorithm to address high-dimensional and dynamic environments. Many tests show that our new combined method uses much less energy than single-agent algorithms, and the theory behind it is supported by the results we got from experiments. Additionally, the strategy shows great flexibility and reliability in changing situations, highlighting its promise for smart resource management in future 6G-enabled MEC systems.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1473.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
