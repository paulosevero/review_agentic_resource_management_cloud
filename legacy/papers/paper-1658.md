---
id: "paper-1658"
title: "Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks"
authors: ["Hu, Zihao", "Yan, Jia", "Zhang, Ying-Jun Angela"]
year: 2025
venue: "IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025"
venue_type: "conference"
doi: "10.1109/INFOCOMWKSHPS65812.2025.11152878"
url: "https://www.scopus.com/pages/publications/105017957435?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["edge intelligence", "federated prompt-tuning", "knowledge distillation", "model compression", "Vision-language foundation models"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1658 — Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks

## Metadata

- **Authors:** Hu, Zihao and Yan, Jia and Zhang, Ying-Jun Angela
- **Year:** 2025
- **Venue:** IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
- **DOI:** 10.1109/INFOCOMWKSHPS65812.2025.11152878
- **URL:** https://www.scopus.com/pages/publications/105017957435?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** edge intelligence; federated prompt-tuning; knowledge distillation; model compression; Vision-language foundation models

### Abstract

Federated prompt-tuning over edge networks opens up potential benefits for communication-efficient fine-tuning of the vision-language foundation model (VLFM) by leveraging the distributed data across edge devices. However, resource constraints on edge devices prevent the full deployment and execution of VLFMs locally, hindering local prompt updates before the global prompt aggregation. To tackle this challenge, we propose a computation-efficient federated prompt-tuning approach over resource-limited edge networks without the local placement of the full VLFM. Specifically, we first propose a computation-efficient knowledge distillation (KD) approach for VLFM model compression, which fine-tunes the splitting-based light-weight model over an unlabeled public dataset at the edge server by optimizing the associated low-dimensional prompts under the guidance of the full pretrained model. Building upon the optimized prompts as a good initialization, the textual and visual prompts are simultaneously updated locally, followed by which the edge server enhances the aggregated global prompts via KD in order to compensate for the compressed VLFM deployed at edge devices. Numerical results underscore the effectiveness of the proposed approach, showcasing the improvement of fine-tuning accuracy and communication efficiency compared with representative benchmarks. © 2025 IEEE.

## 04 — Title Screening

**Title:** Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks
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
