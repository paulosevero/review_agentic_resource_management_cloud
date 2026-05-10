---
id: paper-0003
title: Use of reactive and proactive elasticity to adjust resources provisioning in the cloud provider
authors:
- Bouabdallah, Raouia
- Lajmi, Soufiene
- Ghedira, Khaled
venue: Proceedings - 18th IEEE International Conference on High Performance Computing and Communications, 14th IEEE International Conference on Smart City and 2nd IEEE International Conference on Data Science
  and Systems, HPCC/SmartCity/DSS 2016
venue_type: conference
year: 2017
doi: 10.1109/HPCC-SmartCity-DSS.2016.0162
url: https://www.scopus.com/pages/publications/85013670520?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1155--1162
keywords:
- Cloud computing
- Cloud infrastructure provider
- Multi-agent system (MAS)
- Proactive elasticity
- Reactive elasticity
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

# paper-0003 — Use of reactive and proactive elasticity to adjust resources provisioning in the cloud provider

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Elasticity is the most important feature that differentiatescloud computing from traditional IT infrastructure. Itdefines the capacity of cloud infrastructure provider to acceleratethe provision or the deprovision of the resources needed to deployclient's services. Auto-scaling resource is typically done usingtwo models: reactive and proactive. Most previous researchesmanage elasticity with a single model (reactive or proactive) inisolation without taking into account the combination of both. Inthis context, this paper presents the ElasticCloud system used tomanage elasticity in the cloud provider. This system proposesa hybrid methodology that incorporates a reactive elasticitycoupled with a proactive elasticity to, respectively, scale up andscale down resources running a web application hosted in thecloud. We evaluate the efficiency of our methodology through aset of experiments with a testbed based on a cloud managementsystem and a synthetic workload. We have proved that ourmethodology reduces the number of CPU bottlenecks, the scaledown mistakes and the scale operations compared to existingelasticity approaches. © 2016 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0003.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
