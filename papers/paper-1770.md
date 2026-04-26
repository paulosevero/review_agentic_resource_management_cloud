---
id: "paper-1770"
title: "Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters"
authors: ["Lettich, Francesco", "Carlini, Emanuele", "Nardini, Franco Maria", "Perego, Raffaele", "Trani, Salvatore"]
year: 2025
venue: "Proceedings - 2025 IEEE 25th International Symposium on Cluster, Cloud and Internet Computing, CCGrid 2025"
venue_type: "conference"
doi: "10.1109/CCGRID64434.2025.00015"
url: "https://www.scopus.com/pages/publications/105010817541?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "43--52"
keywords: ["GPU Datacenter", "GPU Fragmentation", "GPU-sharing", "Green Computing", "Online Scheduling", "Power-aware Scheduling", "Sustainable Computing"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1770 — Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters

## Metadata

- **Authors:** Lettich, Francesco and Carlini, Emanuele and Nardini, Franco Maria and Perego, Raffaele and Trani, Salvatore
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE 25th International Symposium on Cluster, Cloud and Internet Computing, CCGrid 2025
- **DOI:** 10.1109/CCGRID64434.2025.00015
- **URL:** https://www.scopus.com/pages/publications/105010817541?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 43--52
- **Language:** English
- **Keywords:** GPU Datacenter; GPU Fragmentation; GPU-sharing; Green Computing; Online Scheduling; Power-aware Scheduling; Sustainable Computing

### Abstract

The rise of Artificial Intelligence and Large Language Models is driving increased GPU usage in data centers for complex training and inference tasks, impacting operational costs, energy demands, and the environmental footprint of large-scale computing infrastructures. This work addresses the online scheduling problem in GPU datacenters, which involves scheduling tasks without knowledge of their future arrivals. We focus on two objectives: minimizing GPU fragmentation and reducing power consumption. GPU fragmentation occurs when partial GPU allocations hinder the efficient use of remaining resources, especially as the datacenter nears full capacity. A recent scheduling policy, Fragmentation Gradient Descent (FGD), leverages a fragmentation metric to address this issue. Reducing power consumption is also crucial due to the significant power demands of GPUs. To this end, we propose PWR, a novel scheduling policy to minimize power usage by selecting power-efficient GPU and CPU combinations. This involves a simplified model for measuring power consumption integrated into a Kubernetes score plugin. Through an extensive experimental evaluation in a simulated cluster, we show how PWR, when combined with FGD, achieves a balanced trade-off between reducing power consumption and minimizing GPU fragmentation.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Power- and Fragmentation-Aware Online Scheduling for GPU Datacenters
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
