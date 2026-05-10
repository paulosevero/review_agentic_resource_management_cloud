---
id: paper-0419
title: Lyapunov-Based Partial Computation Offloading for Multiple Mobile Devices Enabled by Harvested Energy in MEC
authors:
- Guo, Min
- Wang, Wei
- Huang, Xing
- Chen, Yanru
- Zhang, Lei
- Chen, Liangyin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2021.3118016
url: https://www.scopus.com/pages/publications/85119621893?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9025--9035
keywords:
- Data-partition applications
- energy harvesting (EH)
- Lyapunov optimization
- mobile-edge computing (MEC)
- partial computation offloading
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

# paper-0419 — Lyapunov-Based Partial Computation Offloading for Multiple Mobile Devices Enabled by Harvested Energy in MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile-edge computing (MEC) has been garnering considerable level of interests by processing computation tasks nearby mobile devices (MDs). With limited computation and communication resources and strict task deadline, balancing the energy consumption and time delay of computational tasks will be highly focused. MDs deployed energy harvesting (EH) modules can always provide service to continuous task requests, and finer-grained offloading schemes of the MEC system will significantly affect the time delay of computation tasks. However, when combined them together, the energy causal constraint and the coupling between offloading ratios and resources allocation will cause new challenges for the computation offloading problem. To address these issues, we investigate the partial computation offloading schemes for multiple MDs enabled by harvested energy in MEC. Specifically, we build models for two computing modes and EH process. Subsequently, we formulate a nonconvex optimization problem by minimizing the energy consumption of all the MDs while satisfying the constraint of time delay. Furthermore, we propose and design a novel algorithm based on the Lyapunov optimization to achieve optimal solution, that is, Lyapunov-optimization-based partial computation offloading for multiuser (LOMUCO). Then, we take the long-term average energy consumption and the discarding ratio of computation tasks as the quantitative metrics and conduct extended simulation experiments to confirm the performance of LOMUCO. Finally, compared to several baseline or state-of-the-art algorithms, including local computing all (LCA), offloading computing all (OCA), randomly partial computation offloading (RPCO), and Lyapunov-optimization-based dynamic computation offloading (LODCO), we can demonstrate the superiority of LOMUCO.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0419.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
