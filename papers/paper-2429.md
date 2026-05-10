---
id: paper-2429
title: 'End-to-Network Load Balancing for AI Data Center Networks: A Convergence-Based Approach to Enhance Training Efficiency'
authors:
- Zhang, Ran
- Zhao, Xuan
- Han, Yingying
- Yang, Yubin
- Ruan, Jun
- Zhang, Jianqin
- Chen, Donglin
- Wang, Heng
venue: Transactions on Emerging Telecommunications Technologies
venue_type: journal
year: 2025
doi: 10.1002/ett.70249
url: https://www.scopus.com/pages/publications/105017008505?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- AI data center networks
- end-to-network convergence
- load balancing
- network simulation
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: false
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

# paper-2429 — End-to-Network Load Balancing for AI Data Center Networks: A Convergence-Based Approach to Enhance Training Efficiency

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In large-scale language model training, network performance is a crucial determinant of training efficiency. Traditional load balancing methods, such as equal-cost multipath (ECMP), often suffer from hash polarization, leading to suboptimal traffic distribution—particularly in scenarios with limited flow counts and a dominance of elephant flows. To mitigate this challenge, this paper introduces end-to-network load balancing (ENLB), a novel and readily deployable scheme that optimizes uplink utilization through coordinated server-switch traffic scheduling. Leveraging end-to-network convergence principles, ENLB enhances bandwidth efficiency while minimizing flow completion times. Simulation and experimental evaluations demonstrate that ENLB improves network bandwidth utilization by up to 38% and reduces model training task durations by over 3% compared to conventional ECMP-based approaches. These findings underscore ENLB's potential as a scalable solution for modern AI Data Center (AIDC) networks. © 2025 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2429.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
