---
id: paper-0320
title: Multi-agent systems in fog–cloud computing for critical healthcare task management model (CHTM) used for ECG monitoring
authors:
- Mutlag, Ammar Awad
- Ghani, Mohd Khanapi Abd
- Mohammed, Mazin Abed
- Lakhan, Abdullah
- Mohd, Othman
- Abdulkareem, Karrar Hameed
- Garcia-Zapirain, Begonya
venue: Sensors
venue_type: journal
year: 2021
doi: 10.3390/s21206923
url: https://www.scopus.com/pages/publications/85117196177?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- Balancing
- Cardiology
- Cloud computing
- Fog computing
- Multi-agent system
- Prioritization
- Scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0320 — Multi-agent systems in fog–cloud computing for critical healthcare task management model (CHTM) used for ECG monitoring

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the last decade, the developments in healthcare technologies have been increasing progressively in practice. Healthcare applications such as ECG monitoring, heartbeat analysis, and blood pressure control connect with external servers in a manner called cloud computing. The emerging cloud paradigm offers different models, such as fog computing and edge computing, to enhance the performances of healthcare applications with minimum end-to-end delay in the network. However, many research challenges exist in the fog-cloud enabled network for healthcare applications. Therefore, in this paper, a Critical Healthcare Task Management (CHTM) model is proposed and implemented using an ECG dataset. We design a resource scheduling model among fog nodes at the fog level. A multi-agent system is proposed to provide the complete management of the network from the edge to the cloud. The proposed model overcomes the limitations of providing interoperability, resource sharing, scheduling, and dynamic task allocation to manage critical tasks significantly. The simulation results show that our model, in comparison with the cloud, significantly reduces the network usage by 79%, the response time by 90%, the network delay by 65%, the energy consumption by 81%, and the instance cost by 80%. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0320.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
