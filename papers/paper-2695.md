---
id: "paper-2695"
title: "Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation"
authors: ["Lu, Nan", "Yao, Ruiyang", "Wang, Zhaoyang", "Yan, Yuejun", "Wang, Yi"]
year: 2026
venue: "Applied Energy"
venue_type: "journal"
doi: "10.1016/j.apenergy.2025.127132"
url: "https://www.scopus.com/pages/publications/105024717054?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Computing power", "Data center", "Deep reinforcement learning", "Low-carbon operation", "Task scheduling", "Task splitting"]
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

# paper-2695 — Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation

## Metadata

- **Authors:** Lu, Nan and Yao, Ruiyang and Wang, Zhaoyang and Yan, Yuejun and Wang, Yi
- **Year:** 2026
- **Venue:** Applied Energy
- **DOI:** 10.1016/j.apenergy.2025.127132
- **URL:** https://www.scopus.com/pages/publications/105024717054?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Computing power; Data center; Deep reinforcement learning; Low-carbon operation; Task scheduling; Task splitting

### Abstract

Artificial intelligence (AI) techniques have shown impressive performance in both industry and academia. In recent years, the energy consumption of AI tasks has experienced exponential growth, and how to schedule arriving AI tasks in a low-carbon manner is worth investigating for data centers. However, due to the computationally intensive and resource-demanding properties of AI tasks, current deferral-based scheduling methods cannot efficiently fit a large AI task (e.g., training a large language model) into low-carbon periods, so the temporal flexibility cannot be fully utilized to reduce carbon emissions. To this end, we propose a low-carbon and quality-of-service (QoS)-aware operation framework for data centers based on AI task splitting and allocation. Specifically, a fine-grained estimation approach is first designed for computing resource requirements of AI tasks under various split strategies; on this basis, each AI task is then split into a varying number of subtasks that can satisfy heterogeneous resource constraints and be smoothly fitted into low-carbon time slots, which is done by our proposed DRL-based scheduler. Extensive comparison experiments are conducted on a publicly available dataset to validate the superiority of the proposed framework, verifying that our proposed method can achieve a significant reduction in carbon emissions and an improvement in QoS. © 2025 Elsevier Ltd

## 04 — Title Screening

**Title:** Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Low-carbon and QoS-aware operation of data centers by AI task splitting and allocation
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
