---
id: "paper-528"
title: "Decentralized Training of Foundation Models in Heterogeneous Environments"
authors: ["Yuan, Binhang", "He, Yongjun", "Davis, Jared Quincy", "Zhang, Tianyi", "Dao, Tri", "Chen, Beidi", "Liang, Percy", "Re, Christopher", "Zhang, Ce"]
year: 2022
venue: "Advances in Neural Information Processing Systems"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85144991242?origin=resultslist"
publisher: "Neural information processing systems foundation"
pages: ""
keywords: ["Evolutionary algorithms", "Foundations", "Graphics processing unit", "Program processors", "Scheduling algorithms", "Data parallel", "Data parallelism", "Decentralised", "Foundation models", "Heterogeneous environments", "Homogeneous interconnects", "Low-bandwidth", "Pipeline parallelisms", "Software-systems", "State-of-the-art scheme", "Heterogeneous networks"]
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

# paper-528 — Decentralized Training of Foundation Models in Heterogeneous Environments

## Metadata

- **Authors:** Yuan, Binhang and He, Yongjun and Davis, Jared Quincy and Zhang, Tianyi and Dao, Tri and Chen, Beidi and Liang, Percy and Re, Christopher and Zhang, Ce
- **Year:** 2022
- **Venue:** Advances in Neural Information Processing Systems
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85144991242?origin=resultslist
- **Publisher:** Neural information processing systems foundation
- **Pages:** 
- **Language:** English
- **Keywords:** Evolutionary algorithms; Foundations; Graphics processing unit; Program processors; Scheduling algorithms; Data parallel; Data parallelism; Decentralised; Foundation models; Heterogeneous environments; Homogeneous interconnects; Low-bandwidth; Pipeline parallelisms; Software-systems; State-of-the-art scheme; Heterogeneous networks

### Abstract

Training foundation models, such as GPT-3 and PaLM, can be extremely expensive, often involving tens of thousands of GPUs running continuously for months. These models are typically trained in specialized clusters featuring fast, homogeneous interconnects and using carefully designed software systems that support both data parallelism and model/pipeline parallelism. Such dedicated clusters can be costly and difficult to obtain. Can we instead leverage the much greater amount of decentralized, heterogeneous, and lower-bandwidth interconnected compute? Previous works examining the heterogeneous, decentralized setting focus on relatively small models that can be trained in a purely data parallel manner. State-of-the-art schemes for model parallel foundation model training, such as Megatron and Deepspeed, only consider the homogeneous data center setting. In this paper, we present the first study of training large foundation models with model parallelism in a decentralized regime over a heterogeneous network. Our key technical contribution is a scheduling algorithm that allocates different computational “tasklets” in the training of foundation models to a group of decentralized GPU devices connected by a slow heterogeneous network. We provide a formal cost model and further propose an efficient evolutionary algorithm to find the optimal allocation strategy. We conduct extensive experiments that represent different scenarios for learning over geo-distributed devices simulated using real-world network measurements. In the most extreme case, across 8 different cities spanning 3 continents, our approach is 4.8× faster than prior state-of-the-art training systems. © 2022 Neural information processing systems foundation. All rights reserved.

## 04 — Title Screening

**Title:** Decentralized Training of Foundation Models in Heterogeneous Environments

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Decentralized Training of Foundation Models in Heterogeneous Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Decentralized Training of Foundation Models in Heterogeneous Environments
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
