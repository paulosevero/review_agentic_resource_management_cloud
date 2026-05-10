---
id: "paper-1834"
title: "HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment"
authors: ["Lian, Zirui", "Cao, Qianyue", "Liang, Chao", "Cao, Jing", "Zhu, Zongwei", "Yang, Zhi", "Ji, Cheng", "Li, Changlong", "Zhou, Xuehai"]
year: 2025
venue: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
venue_type: "journal"
doi: "10.1109/TCAD.2025.3548003"
url: "https://www.scopus.com/pages/publications/86000654880?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3518--3531"
keywords: ["Dynamic scenarios", "edge computing", "embedded systems", "federated learning (FL)", "heterogeneous training"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-1834 — HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment

## Metadata

- **Authors:** Lian, Zirui and Cao, Qianyue and Liang, Chao and Cao, Jing and Zhu, Zongwei and Yang, Zhi and Ji, Cheng and Li, Changlong and Zhou, Xuehai
- **Year:** 2025
- **Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- **DOI:** 10.1109/TCAD.2025.3548003
- **URL:** https://www.scopus.com/pages/publications/86000654880?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3518--3531
- **Language:** English
- **Keywords:** Dynamic scenarios; edge computing; embedded systems; federated learning (FL); heterogeneous training

### Abstract

Federated learning (FL) is an advanced framework that enables collaborative training of machine learning models across edge devices. An effective strategy to enhance training efficiency is to allocate the optimal submodel based on each device’s resource capabilities. However, system heterogeneity significantly increases the difficulty of allocating submodel parameter budgets appropriately for each device, leading to the straggler problem. Meanwhile, data heterogeneity complicates the selection of the optimal submodel structure for specific devices, thereby impacting training performance. Furthermore, the dynamic nature of edge environments, such as fluctuations in network communication and computational resources, exacerbates these challenges, making it even more difficult to precisely extract appropriately sized and structured submodels from the global model. To address the challenges in heterogeneous training environments, we propose an efficient FL framework, namely, HaloFL. The framework dynamically adjusts the structure and parameter budget of submodels during training by evaluating three dimensions: 1) model-wise performance; 2) layer-wise performance; and 3) unit-wise performance. First, we design a data-aware model unit importance evaluation method to determine the optimal submodel structure for different data distributions. Next, using this evaluation method, we analyze the importance of model layers and reallocate parameters from noncritical layers to critical layers within a fixed parameter budget, further optimizing the submodel structure. Finally, we introduce a resource-aware dual-UCB multiarmed bandit agent, which dynamically adjusts the total parameter budget of submodels according to changes in the training environment, allowing the framework to better adapt to the performance differences of heterogeneous devices. Experimental results demonstrate that HaloFL exhibits outstanding efficiency in various dynamic and heterogeneous scenarios, achieving up to a 14.80% improvement in accuracy and a 3.06× speedup compared to existing FL frameworks. © 1982-2012 IEEE.

## 04 — Title Screening

**Title:** HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment
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
