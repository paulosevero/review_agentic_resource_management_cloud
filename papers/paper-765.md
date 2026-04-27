---
id: "paper-765"
title: "Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence"
authors: ["Xu, Minrui", "Niyato, Dusit", "Zhang, Hongliang", "Kang, Jiawen", "Xiong, Zehui", "Mao, Shiwen", "Han, Zhu"]
year: 2023
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM54140.2023.10436771"
url: "https://www.scopus.com/pages/publications/85187323575?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3548--3553"
keywords: ["generative artificial intelligence", "joint foundation model caching and inference", "Mobile edge computing", "pretrained foundation models"]
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

# paper-765 — Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence

## Metadata

- **Authors:** Xu, Minrui and Niyato, Dusit and Zhang, Hongliang and Kang, Jiawen and Xiong, Zehui and Mao, Shiwen and Han, Zhu
- **Year:** 2023
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM54140.2023.10436771
- **URL:** https://www.scopus.com/pages/publications/85187323575?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3548--3553
- **Language:** English
- **Keywords:** generative artificial intelligence; joint foundation model caching and inference; Mobile edge computing; pretrained foundation models

### Abstract

With the rapid development of artificial general intelligence (AGI), various multimedia services based on pretrained foundation models (PFMs) need to be effectively deployed. With edge servers that have cloud-level computing power, edge intelligence can extend the capabilities of AGI to mobile edge networks. However, compared with cloud data centers, resource-limited edge servers can only cache and execute a small number of PFMs, which typically consist of billions of parameters and require intensive computing power and GPU memory during inference. To address this challenge, in this paper, we propose a joint foundation model caching and inference framework that aims to balance the tradeoff among inference latency, accuracy, and resource consumption by managing cached PFMs and user requests efficiently during the provisioning of generative AI services. Specifically, considering the in-context learning ability of PFMs, a new metric named the Age of Context (AoC), is proposed to model the freshness and relevance between examples in past demonstrations and current service requests. Based on the AoC, we propose a least context caching algorithm to manage cached PFMs at edge servers with historical prompts and inference results. The numerical results demonstrate that the proposed algorithm can reduce system costs compared with existing baselines by effectively utilizing contextual information. © 2023 IEEE.

## 04 — Title Screening

**Title:** Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence
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
