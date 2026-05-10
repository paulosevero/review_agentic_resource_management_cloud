---
id: paper-2484
title: Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems
authors:
- Zhu, Shuntao
- Wang, Dan
venue: E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems
venue_type: conference
year: 2025
doi: 10.1145/3679240.3734609
url: https://www.scopus.com/pages/publications/105016379923?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 407--414
keywords:
- Immersion Cooling
- LLM Training
- Thermal Control
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2484 — Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increase in AI applications, the energy consumption of datacenters that run AI jobs is greatly increasing. The overall energy consumption of a datacenter is closely linked with that of its cooling system. Recently, there has been a revolution in immersion cooling technologies, in which servers can be directly immersed in dielectric cooling liquid (coolant). However, there is a lack of understanding of how the performance of AI jobs is affected by immersion cooling systems. While the physics behind immersion cooling is understood, in this paper we observe key restricting factors: (1) the boiling state of the coolant and (2) the heat removal rate of the coolant may not match the heat generation rate of the GPUs, triggering the thermal-throttle mechanisms of the GPUs. In this paper, we study the energy-efficient and delay-ensured computing of large language model (LLM) training jobs over a cluster of GPUs in immersion cooling systems. We model the thermal characteristics of the system (e.g., heat generation, heat removal, and temperature) and develop an algorithm with workload assignment and frequency scaling to avoid the delay incurred by the thermal-throttle mechanisms and to execute the workloads in energy-efficient frequencies. In our evaluation, we simulate the computational fluid dynamics (CFD) of the immersion cooling systems through the Ansys Fluent software. We show that we outperform baseline algorithms by up to 53.2% in energy and 22.5% in delays. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2484.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
