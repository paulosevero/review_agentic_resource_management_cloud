---
id: "paper-1280"
title: "Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge"
authors: ["Wu, Hai", "Chen, Xu", "Huang, Kaibin"]
year: 2024
venue: "International Conference on Communications in China, ICCC Workshops 2024"
venue_type: "conference"
doi: "10.1109/ICCCWorkshops62562.2024.10693756"
url: "https://www.scopus.com/pages/publications/85207647933?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "226--231"
keywords: ["6G", "Edge AI", "fine-tuning", "Foundation models"]
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
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1280 — Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge

## Metadata

- **Authors:** Wu, Hai and Chen, Xu and Huang, Kaibin
- **Year:** 2024
- **Venue:** International Conference on Communications in China, ICCC Workshops 2024
- **DOI:** 10.1109/ICCCWorkshops62562.2024.10693756
- **URL:** https://www.scopus.com/pages/publications/85207647933?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 226--231
- **Language:** English
- **Keywords:** 6G; Edge AI; fine-tuning; Foundation models

### Abstract

The emergence of large-scale foundation models (FoMo's) that can perform human-like intelligence inspires edge devices to access state-of-the-art artificial intelligence (AI) applications. For a better user experience, the pre-trained FoMo needs to be adapted for specialized downstream tasks through fine-tuning techniques. To transcend a single device's memory and computation limitations, we propose a multi-device cooperation mechanism within the device-edge cooperative fine-tuning (DEFT) paradigm, where devices distributed at the wireless edge simultaneously optimize different parts of fine-tuning parameters within a FoMo. The edge server is responsible for coordination and update aggregation. However, the parameter blocks resided in different depths within a FoMo architecture, leading to varied computation latency and memory consumption due to the adoption of gradient backpropagation-based calculations. The hetero-geneous on-device computation capability and memory budget, block calculation latency, and uploading channel conditions, necessitate an integrated communication-and-computation (C2) allocation of local computation loads and uplink communication resources to achieve low-latency DEFT (LoLa-DEFT). To address this issue, a depth-aware block allocation problem is formulated and solved optimally, which aims to pick up the device-block pairs with the best C2 performance while satisfying related constraints. Through extensive experiments conducted on the GLUE benchmark, our results demonstrate the proposed depth-aware block allocation for LoLa DEFT achieves a substantial acceleration in fine-tuning a RoBERTa model compared with traditional computation offloading scheme.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge
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
