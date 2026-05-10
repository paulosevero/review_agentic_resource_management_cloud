---
id: paper-0686
title: A new fog computing resource management (FRM) model based on hybrid load balancing and scheduling for critical healthcare applications
authors:
- Mutlag, Ammar Awad
- Ghani, Mohd Khanapi Abd
- Mohd, Othman
- Abdulkareem, Karrar Hameed
- Mohammed, Mazin Abed
- Alharbi, Meshal
- Al-Araji, Zaid J.
venue: Physical Communication
venue_type: journal
year: 2023
doi: 10.1016/j.phycom.2023.102109
url: https://www.scopus.com/pages/publications/85163490079?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Critical healthcare applications
- Fog computing
- Fog computing resource management (FRM)
- Load balancing
- Multi-agent system
- Tasks scheduling
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

# paper-0686 — A new fog computing resource management (FRM) model based on hybrid load balancing and scheduling for critical healthcare applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Critical healthcare application tasks require a real-time response because it affects patients’ life. Fog computing is the best solution to get a fast response and less energy consumption in healthcare. However, current solutions face difficulties in scheduling the tasks to the correct computing devices based on their priorities and capacity to meet the tasks’ deadlines and resource limitations with minimal latency. Furthermore, challenges of load balancing and prioritization are raised when dealing with inadequate computing resources and telecommunication networks while obtaining the best scheduling of emergency healthcare tasks. In this study, a fog computing resource management (FRM) model is proposed, which the proposed model has three main solutions. Firstly, resource availability is calculated according to the average execution time of each task. Secondly, load balancing is enhanced by proposing a hybrid approach that combines the multi-agent load balancing algorithm and the throttled load balancing algorithm. Thirdly, task scheduling is done based on priority, resource availability, and load balancing. The results have been acquired using the iFogSim toolkit. Two datasets are used in this study, the blood pressure dataset was acquired from the UTeM clinic, and the ECG dataset was acquired from the University of California at Irvine. Both datasets are integrated to enlarge the attributes and get accurate results. The results demonstrate the effectiveness of managing resources and optimizing task scheduling and balancing in a fog computing environment. In comparison with other research studies, the FRM model outperforms delay by 55%, response time by 72%, cost by 72%, and energy consumption by 70%. © 2023 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0686.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
