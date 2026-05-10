---
id: paper-1154
title: 'JDACO: Joint Data Aggregation and Computation Offloading in UAV-Enabled Internet of Things for Post-Disaster Scenarios'
authors:
- Raivi, Asif Mahmud
- Moh, Sangman
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3354950
url: https://www.scopus.com/pages/publications/85182935596?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16529--16544
keywords:
- Computation offloading
- data aggregation
- Internet of Things (IoT)
- mobile edge computing (MEC)
- multiagent reinforcement learning
- unmanned aerial vehicle (UAV)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1154 — JDACO: Joint Data Aggregation and Computation Offloading in UAV-Enabled Internet of Things for Post-Disaster Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Owing to high flexibility and rapid deployment, unmanned aerial vehicles (UAVs) can offer network coverage for Internet of Things (IoT) devices in post-disaster scenarios. UAV-aided mobile edge computing (MEC) provides computational support and facilitates optimal decision-making processes for ground-based IoT devices. However, existing literature has separately examined both data aggregation and computational offloading. In this article, we introduce a joint data aggregation and computational offloading (JDACO) scheme for UAV-enabled IoT systems in post-disaster scenarios. JDACO's primary objective is to minimize the overall energy consumption and latency in the aggregation and computation processes. It achieves this by employing UAVs as MEC servers and deploying multiple UAVs. We initially design an objective function to assess the costs associated with the aggregation and offloading processes. Subsequently, we frame the optimization problem as a Markov model and employ a multiagent deep reinforcement learning algorithm. This approach utilizes value decomposition with the double deep {Q} -Network algorithm to optimize data aggregation and enable a cost-effective offloading process through cooperative learning. Our experimental results demonstrate that our proposed JDACO scheme surpasses existing methods in terms of training time reduction, processed data volume, energy efficiency, and mission duration by 20%, 11.4%, 5.6%, and 11.2%, respectively, compared to the conventional schemes while serving up to 98% of IoT devices. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1154.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
