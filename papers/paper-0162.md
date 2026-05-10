---
id: paper-0162
title: Energy efficient load balancing in cloud data center using clustering technique
authors:
- Thilagavathi, N.
- Divya Dharani, D.
- Sasilekha, R.
- Suruliandi, Vasundhara
- Rhymend Uthariaraj, V.
venue: International Journal of Intelligent Information Technologies
venue_type: journal
year: 2019
doi: 10.4018/IJIIT.2019010104
url: https://www.scopus.com/pages/publications/85060776073?origin=resultslist
publisher: IGI Global
pages: 84--100
keywords:
- Agent-based model
- Cloud computing
- Clustering
- Energy consumption
- Energy efficiency
- Load balancing
- Migration
- Server consolidation
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

# paper-0162 — Energy efficient load balancing in cloud data center using clustering technique

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing has seen tremendous growth in recent days. As a result of this, there has been a great increase in the growth of data centers all over the world. These data centers consume a lot of energy, resulting in high operating costs. The imbalance in load distribution among the servers in the data center results in increased energy consumption. Server consolidation can be handled by migrating all virtual machines in those underutilized servers. Migration causes performance degradation of the job, based on the migration time and number of migrations. Considering these aspects, the proposed clustering agent-based model improves energy saving by efficient allocation of the VMs to the hosting servers, which reduces the response time for initial allocation. Middle VM migration (MVM) strategy for server consolidation minimizes the number of VM migrations. Further, randomization of extra resource requirement done to cater to real-time scenarios needs more resource requirements than the initial requirement. Simulation results show that the proposed approach reduces the number of migrations and response time for user request and improves energy saving in the cloud environment. Copyright © 2019, IGI Global.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0162.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
