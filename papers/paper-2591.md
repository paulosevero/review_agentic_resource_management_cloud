---
id: paper-2591
title: Distributionally robust co-optimization of computing workloads and renewable energy uncertainties in geo-distributed data centers considering multi-element influences
authors:
- Han, Juntao
- Tong, Nannan
- Lin, Jiayu
- Han, Yibo
- Wang, Yongzhen
- Han, Kai
- Li, Yaping
venue: 'Energy Conversion and Management: X'
venue_type: journal
year: 2026
doi: 10.1016/j.ecmx.2025.101432
url: https://www.scopus.com/pages/publications/105024313604?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Geo-distributed data center
- Integrated energy system
- Renewable energy uncertainty
- Spatiotemporal load balancing
- Thermal awareness
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2591 — Distributionally robust co-optimization of computing workloads and renewable energy uncertainties in geo-distributed data centers considering multi-element influences

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paradigm evolution of digital economies, epitomized by artificial intelligence large models, has precipitated an exponential escalation in data centers energy consumption and carbon emissions. However, the collaborative optimization of spatiotemporal load migration and renewable energy uncertainty offers a promising pathway towards low-carbon and economical operations in geo-dispersed data center. Therefore, this study innovatively constructs a spatiotemporal load balancing and energy management collaborative optimization model for geo-distributed data center, integrating renewable energy uncertainty, thermal awareness, and data network transmission. This model is solved by combining the column and constraint generation algorithm with alternating direction method of multipliers (ADMM). Firstly, the generative adversarial network and comprehensive norm constraints are employed to construct renewable energy uncertainties sets and probability distributions. Subsequently, the two-stage distributionally robust optimization integrating renewable energy uncertainty, geographical differences in cooling efficiency, and data network transmission is established. Furthermore, without sharing locally sensitive data, the ADMM algorithm is utilized to optimize the spatiotemporal load balancing and energy management strategies for geo-distributed data center clusters. Case studies demonstrate that, in comparison with scenarios without spatiotemporal load balancing, the proposed approach reduces economic costs, energy purchase, and carbon trading by 13.7%, 26.4%, and 48.4%, respectively, while increasing renewable energy utilization by 2.5%. The study also investigates the impacts of delay-tolerant tasks, geographical differences in cooling efficiency, and data network transmission on system performance. Finally, Nash bargaining is employed to determine computing task transaction pricing and multi-agent benefit allocation, incentivizing data center clusters to participate in workload flexibility regulation. © 2025 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2591.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
