---
id: "paper-1026"
title: "Filling the Missing: Exploring Generative AI for Enhanced Federated Learning over Heterogeneous Mobile Edge Devices"
authors: ["Li, Peichun", "Zhang, Hanwen", "Wu, Yuan", "Qian, Liping", "Yu, Rong", "Niyato, Dusit", "Shen, Xuemin"]
year: 2024
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2024.3371772"
url: "https://www.scopus.com/pages/publications/85187012754?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10001--10015"
keywords: ["data compensation", "Federated learning", "generative AI", "resource management"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1026 — Filling the Missing: Exploring Generative AI for Enhanced Federated Learning over Heterogeneous Mobile Edge Devices

## Metadata

- **Authors:** Li, Peichun and Zhang, Hanwen and Wu, Yuan and Qian, Liping and Yu, Rong and Niyato, Dusit and Shen, Xuemin
- **Year:** 2024
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2024.3371772
- **URL:** https://www.scopus.com/pages/publications/85187012754?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10001--10015
- **Language:** English
- **Keywords:** data compensation; Federated learning; generative AI; resource management

### Abstract

Distributed Artificial Intelligence (AI) model training over mobile edge networks encounters significant challenges due to the data and resource heterogeneity of edge devices. The former hampers the convergence rate of the global model, while the latter diminishes the devices' resource utilization efficiency. In this paper, we propose a generative AI-empowered federated learning to address these challenges by leveraging the idea of FIlling the MIssing (FIMI) portion of local data. Specifically, FIMI can be considered as a resource-aware data augmentation method that effectively mitigates the data heterogeneity while ensuring efficient FL training. We first quantify the relationship between the training data amount and the learning performance. We then study the FIMI optimization problem with the objective of minimizing the device-side overall energy consumption subject to required learning performance constraints. The decomposition-based analysis and the cross-entropy searching method are leveraged to derive the solution, where each device is assigned suitable AI-synthetic data and resource utilization policy. Experiment results demonstrate that FIMI can save up to 50% of the device-side energy to achieve the target global test accuracy in comparison with the existing methods. Meanwhile, FIMI can significantly enhance the converged global accuracy under the non-independently-and-identically distribution (non-IID) data.  © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

## 04 — Title Screening

**Title:** Filling the Missing: Exploring Generative AI for Enhanced Federated Learning over Heterogeneous Mobile Edge Devices

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Filling the Missing: Exploring Generative AI for Enhanced Federated Learning over Heterogeneous Mobile Edge Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Filling the Missing: Exploring Generative AI for Enhanced Federated Learning over Heterogeneous Mobile Edge Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
