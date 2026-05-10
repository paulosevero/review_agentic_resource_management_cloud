---
id: "paper-1475"
title: "Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices"
authors: ["Chen, Xiaopei", "Li, Liang", "Ji, Fei", "Wu, Wen"]
year: 2025
venue: "IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025"
venue_type: "conference"
doi: "10.1109/INFOCOMWKSHPS65812.2025.11152998"
url: "https://www.scopus.com/pages/publications/105017952522?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Federated learning", "Mobile computing", "Mobile edge computing", "Adaptation module", "Edge server", "Fine tuning", "Heterogeneous mobile devices", "Language model", "Learning frameworks", "Memory efficient", "Memory pressure", "Sequential manners", "Training efficiency", "Personnel training"]
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
    human_justification: "LLMs é o workload não o tomador de decisões"

---

# paper-1475 — Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices

## Metadata

- **Authors:** Chen, Xiaopei and Li, Liang and Ji, Fei and Wu, Wen
- **Year:** 2025
- **Venue:** IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
- **DOI:** 10.1109/INFOCOMWKSHPS65812.2025.11152998
- **URL:** https://www.scopus.com/pages/publications/105017952522?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Federated learning; Mobile computing; Mobile edge computing; Adaptation module; Edge server; Fine tuning; Heterogeneous mobile devices; Language model; Learning frameworks; Memory efficient; Memory pressure; Sequential manners; Training efficiency; Personnel training

### Abstract

In this paper, we propose an edge-assisted split federated learning framework to facilitate large language model (LLM) fine-tuning on heterogeneous mobile devices while alleviating memory pressures on both mobile devices and the edge server. Specifically, mobile devices perform low-rank adaptation (LoRA) fine-tuning on only a subset of lower layers of the pre-trained LLM, tailored to their individual capacities. On the server, a full LLM is maintained, and the corresponding LoRA modules are selectively fine-tuned in a sequential manner for each device. To further enhance training efficiency, we propose a server-side training scheduling method that optimizes the processing order of devices for accelerating fine-tuning. Extensive experiments demonstrate that compared to the baselines, our scheme can reduce 79% memory footprint and 6% training time while achieving comparable performance. © 2025 IEEE.

## 04 — Title Screening

**Title:** Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
