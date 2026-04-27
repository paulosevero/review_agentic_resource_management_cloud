---
id: "paper-623"
title: "Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks"
authors: ["Jung, Soyi", "Park, Chanyoung", "Levorato, Marco", "Kim, Jae-Hyun", "Kim, Joongheon"]
year: 2023
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2023.3283404"
url: "https://www.scopus.com/pages/publications/85161515015?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "14889--14905"
keywords: ["edge", "multi-agent deep reinforcement learning (MADRL)", "scheduling", "surveillance", "two-stage", "Unmanned aerial vehicles (UAVs)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-623 — Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks

## Metadata

- **Authors:** Jung, Soyi and Park, Chanyoung and Levorato, Marco and Kim, Jae-Hyun and Kim, Joongheon
- **Year:** 2023
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2023.3283404
- **URL:** https://www.scopus.com/pages/publications/85161515015?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 14889--14905
- **Language:** English
- **Keywords:** edge; multi-agent deep reinforcement learning (MADRL); scheduling; surveillance; two-stage; Unmanned aerial vehicles (UAVs)

### Abstract

This paper proposes a two-stage novel algorithm for intelligent edge-assisted multiple unmanned aerial vehicles (UAVs) surveillance services. In the first stage, multiple UAVs determine their optimal positions to detect as many target faces as possible for efficient surveillance using multi-agent deep reinforcement learning (MADRL). Multi-UAVs must be coordinated and optimally positioned for effective surveillance depending on the target person's location. It is also significantly important to consider the battery performance of the UAVs. In the second stage, every single UAV performs face identification in monitored areas, where two sequential scheduling methods make decisions: (i) edge selection for remote computing via max-weight scheduling and (ii) transmit power allocation scheduling to deliver the images to scheduled edges for time-average energy consumption minimization subject to stability. The identification execution requires computing power, and its complexity and time depend on the number of faces in the captured image. Consequently, the task cannot be fully executed by an individual UAV in high image arrival regimes or images with a high density of faces. In those conditions, UAVs can leverage computing support from nearby edges capable of AI-based face identification tasks. Importantly, computing task distribution should be energy-efficient and delay-minimal due to constraints imposed by the UAV system's characteristics and applications. We remark that selected edges should complete their computing tasks with similar delay to minimize idle time among the edges, which is why we chose min-max scheduling. To summarize, our proposed novel two-stage algorithm accomplishes efficient multi-UAV positioning corresponding to user-defined weight (overlapped threshold) and minimizes UAVs' transmission power while preserving stability constraints.  © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Two-Stage Self-Adaptive Task Outsourcing Decision Making for Edge-Assisted Multi-UAV Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
