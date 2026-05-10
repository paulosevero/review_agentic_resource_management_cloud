---
id: paper-0623
title: Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks
authors:
- Jung, Soyi
- Park, Chanyoung
- Levorato, Marco
- Kim, Jae-Hyun
- Kim, Joongheon
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3283404
url: https://www.scopus.com/pages/publications/85161515015?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14889--14905
keywords:
- edge
- multi-agent deep reinforcement learning (MADRL)
- scheduling
- surveillance
- two-stage
- Unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0623 — Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper proposes a two-stage novel algorithm for intelligent edge-assisted multiple unmanned aerial vehicles (UAVs) surveillance services. In the first stage, multiple UAVs determine their optimal positions to detect as many target faces as possible for efficient surveillance using multi-agent deep reinforcement learning (MADRL). Multi-UAVs must be coordinated and optimally positioned for effective surveillance depending on the target person's location. It is also significantly important to consider the battery performance of the UAVs. In the second stage, every single UAV performs face identification in monitored areas, where two sequential scheduling methods make decisions: (i) edge selection for remote computing via max-weight scheduling and (ii) transmit power allocation scheduling to deliver the images to scheduled edges for time-average energy consumption minimization subject to stability. The identification execution requires computing power, and its complexity and time depend on the number of faces in the captured image. Consequently, the task cannot be fully executed by an individual UAV in high image arrival regimes or images with a high density of faces. In those conditions, UAVs can leverage computing support from nearby edges capable of AI-based face identification tasks. Importantly, computing task distribution should be energy-efficient and delay-minimal due to constraints imposed by the UAV system's characteristics and applications. We remark that selected edges should complete their computing tasks with similar delay to minimize idle time among the edges, which is why we chose min-max scheduling. To summarize, our proposed novel two-stage algorithm accomplishes efficient multi-UAV positioning corresponding to user-defined weight (overlapped threshold) and minimizes UAVs' transmission power while preserving stability constraints.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0623.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
