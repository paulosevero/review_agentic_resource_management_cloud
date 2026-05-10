---
id: "paper-1359"
title: "Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization"
authors: ["Zhu, Yan", "Yang, Peng", "Zhu, Jingyang", "Wen, Dingzhu", "Wang, Ting", "Zhou, Yong", "Shi, Yuanming", "Jiang, Chunxiao"]
year: 2024
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM52923.2024.10901682"
url: "https://www.scopus.com/pages/publications/105000825669?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5030--5035"
keywords: ["Edge computing", "Integrated circuit design", "Network security", "Privacy by design", "Satellite communication systems", "Tropics", "Architecture designs", "Design optimization", "Fine tuning", "Foundation models", "Intelligence models", "Low earth orbit satellites", "Modeling architecture", "Proposed architectures", "Satellite data", "System optimizations", "Satellite ground stations"]
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

# paper-1359 — Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization

## Metadata

- **Authors:** Zhu, Yan and Yang, Peng and Zhu, Jingyang and Wen, Dingzhu and Wang, Ting and Zhou, Yong and Shi, Yuanming and Jiang, Chunxiao
- **Year:** 2024
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM52923.2024.10901682
- **URL:** https://www.scopus.com/pages/publications/105000825669?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5030--5035
- **Language:** English
- **Keywords:** Edge computing; Integrated circuit design; Network security; Privacy by design; Satellite communication systems; Tropics; Architecture designs; Design optimization; Fine tuning; Foundation models; Intelligence models; Low earth orbit satellites; Modeling architecture; Proposed architectures; Satellite data; System optimizations; Satellite ground stations

### Abstract

With the surge in the number of low earth orbit (LEO) satellites, continuous research has emerged on using satellite data to train artificial intelligence models. On one hand, traditional centralized training on the ground is not feasible due to privacy concerns and limited bandwidth for downloading raw satellite data. On the other hand, due to the limited energy and computational capability of satellites, training directly on satellites suffers from prolonged latency, especially for large models. To alleviate these issues, we propose a novel satellite-ground collaborative federated fine-tuning architecture, where ground stations (GSs) and satellites collaboratively train a global model without the need for data downloads. In this proposed architecture, satellites serve as edge devices and the ground server serves as a coordinator. However, the short satellite-ground communication windows caused by the high mobility of satellites and the substantial intra-orbit data transmission bring special challenges to the transmission process of federated edge learning. To tackle these challenges, we carefully design the satellite-ground collaborative fine-tuning architecture and utilize an optimized ring all-reduce algorithm and network flow algorithm to enhance the intra-orbit and ground-satellite transmissions, respectively. Experimental results demonstrate that our proposed architecture significantly reduces the training time by 40% compared to training solely on satellite. © 2024 IEEE.

## 04 — Title Screening

**Title:** Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization
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
