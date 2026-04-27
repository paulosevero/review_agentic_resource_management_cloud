---
id: "paper-1048"
title: "Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models"
authors: ["Lin, Jianpeng", "Lin, Wenjun", "Lin, Weiwei", "Liu, Tianyi", "Wang, Jiangtao", "Jiang, Hongliang"]
year: 2024
venue: "Building Simulation"
venue_type: "journal"
doi: "10.1007/s12273-024-1185-7"
url: "https://www.scopus.com/pages/publications/85207009200?origin=resultslist"
publisher: "Tsinghua University"
pages: "2145--2161"
keywords: ["cooling control", "data center", "energy saving", "multi-objective optimization", "thermal prediction"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1048 — Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models

## Metadata

- **Authors:** Lin, Jianpeng and Lin, Wenjun and Lin, Weiwei and Liu, Tianyi and Wang, Jiangtao and Jiang, Hongliang
- **Year:** 2024
- **Venue:** Building Simulation
- **DOI:** 10.1007/s12273-024-1185-7
- **URL:** https://www.scopus.com/pages/publications/85207009200?origin=resultslist
- **Publisher:** Tsinghua University
- **Pages:** 2145--2161
- **Language:** English
- **Keywords:** cooling control; data center; energy saving; multi-objective optimization; thermal prediction

### Abstract

With the breakthroughs in generative artificial intelligence (GAI) models, the vast computational demands are placing an unprecedented burden on the data center (DC) energy supply. The cooling system is the second major energy consumer in the DC, maintaining the safe and efficient operation of computing equipment. However, time-varying temperature gradients and power distribution pose a considerable challenge for efficient cooling management in DCs. For this problem, this work proposes a multi-objective cooling control optimization (MCCO) method to minimize cooling energy consumption while maximizing the rack cooling index (RCI) to ensure energy efficiency and security of hybrid-cooled DCs. The proposed method relies on high-fidelity models that characterize the dynamic thermal evolution and cooling power. Therefore, a novel network model (TCN-BiGRU-Attention) combining temporal convolutional network (TCN), bidirectional gated recurrent unit (BiGRU), and attention mechanism is designed to capture the features of multivariate time-series to predict temperature changes in thermal environments and cooling loops. Moreover, considering the complex heat transfer and operational characteristics of hybrid cooling systems, a machine learning (ML)-based power model is constructed to evaluate the holistic cooling power. Subsequently, the NSGA-II algorithm formulates the optimal cooling decision based on the predicted thermal distribution and cooling power, realizing the trade-off between energy consumption and cooling effectiveness. The results of numerical experiments using Marconi 100 data traces suggest that the proposed MCCO significantly reduces cooling energy consumption in summer and winter while maintaining the RCI above 95%. © Tsinghua University Press 2024.

## 04 — Title Screening

**Title:** Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
