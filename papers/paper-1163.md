---
id: "paper-1163"
title: "Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations"
authors: ["Rovnyagin, Mikhail. M.", "Sinelnikov, Dmitry M.", "Eroshev, Artem A.", "Rovnyagina, Tatyana A.", "Tikhomirov, Alexander V."]
year: 2024
venue: "Proceedings of the 2024 Conference of Young Researchers in Electrical and Electronic Engineering, ElCon 2024"
venue_type: "conference"
doi: "10.1109/ElCon61730.2024.10468250"
url: "https://www.scopus.com/pages/publications/85189968004?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "277--280"
keywords: ["ChatGPT", "Context Embedding", "Large Language Model", "Memory Allocation", "Transformer-type Neural Network"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1163 — Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations

## Metadata

- **Authors:** Rovnyagin, Mikhail. M. and Sinelnikov, Dmitry M. and Eroshev, Artem A. and Rovnyagina, Tatyana A. and Tikhomirov, Alexander V.
- **Year:** 2024
- **Venue:** Proceedings of the 2024 Conference of Young Researchers in Electrical and Electronic Engineering, ElCon 2024
- **DOI:** 10.1109/ElCon61730.2024.10468250
- **URL:** https://www.scopus.com/pages/publications/85189968004?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 277--280
- **Language:** English
- **Keywords:** ChatGPT; Context Embedding; Large Language Model; Memory Allocation; Transformer-type Neural Network

### Abstract

Recently, LLM models have become widespread in industry. They are used as the basis for voice assistants, troubleshooting systems, chatbots and much more. The work of LLM is based on the architecture of transformer-type neural networks, where text is supplied as input (for example, text chat), and the model, estimating the character-by-character probability, returns the result also in the form of text. In this case, the model does not retrain. And the context itself is constantly accumulating. This paper proposes two ways to reduce the memory allocated for storing the test chat context. The first method is to periodically launch additional training in order to embed the chat context into the core of the model itself. The article discusses the pros and cons of this approach. The second method is to save in the text chat cache only with those users where this context has already been formed. The article describes the layout for conducting the experiment, provides the results of the experimental study and describes the method for assessing the 'maturity' of the chat correspondence context. © 2024 IEEE.

## 04 — Title Screening

**Title:** Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations
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
