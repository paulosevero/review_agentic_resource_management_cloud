---
id: "paper-908"
title: "Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques"
authors: ["Feng, Kan", "Luo, Lijun", "Xia, Yongjun", "Luo, Bin", "He, Xingfeng", "Li, Kaihong", "Zha, Zhiyong", "Xu, Bo", "Peng, Kai"]
year: 2024
venue: "Symmetry"
venue_type: "journal"
doi: "10.3390/sym16111470"
url: "https://www.scopus.com/pages/publications/85210435496?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["large language models", "microservice deployment", "mobile edge computing", "retrieval augmented generation"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-908 — Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques

## Metadata

- **Authors:** Feng, Kan and Luo, Lijun and Xia, Yongjun and Luo, Bin and He, Xingfeng and Li, Kaihong and Zha, Zhiyong and Xu, Bo and Peng, Kai
- **Year:** 2024
- **Venue:** Symmetry
- **DOI:** 10.3390/sym16111470
- **URL:** https://www.scopus.com/pages/publications/85210435496?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** large language models; microservice deployment; mobile edge computing; retrieval augmented generation

### Abstract

Large Language Models (LLMs) have demonstrated impressive capabilities in autogenerating code based on natural language instructions provided by humans. We observed that in the microservice models of edge computing, the problem of deployment latency optimization can be transformed into an NP-hard mathematical optimization problem. However, in the real world, deployment strategies at the edge often require immediate updates, while human-engineered code tends to be lagging. To bridge this gap, we innovatively integrated LLMs into the decision-making process for microservice deployment. Initially, we constructed a private Retrieval Augmented Generation (RAG) database containing prior knowledge. Subsequently, we employed meticulously designed step-by-step inductive instructions and used the chain of thought (CoT) technique to enable the LLM to learn, reason, reflect, and regenerate. We decomposed the microservice deployment latency optimization problem into a collection of granular sub-problems (described in natural language), progressively providing instructions to the fine-tuned LLM to generate corresponding code blocks. The generated code blocks underwent integration and consistency assessment. Additionally, we prompted the LLM to generate code without the use of the RAG database for comparative analysis. We executed the aforementioned code and comparison algorithm under identical operational environments and simulation parameters, conducting rigorous result analysis. Our fine-tuned model significantly reduced latencies by 22.8% in handling surges in request flows, 37.8% in managing complex microservice types, and 39.5% in processing increased network nodes compared to traditional algorithms. Moreover, our approach demonstrated marked improvements in latency performance over LLMs not utilizing RAG technology and reinforcement learning algorithms reported in other literature. The use of LLMs also highlights the concept of symmetry, as the symmetrical structure of input-output relationships in microservice deployment models aligns with the LLM’s inherent ability to process and generate balanced and optimized code. Symmetry in this context allows for more efficient resource allocation and reduces redundant operations, further enhancing the model’s effectiveness. We believe that LLMs hold substantial potential in optimizing microservice deployment models. © 2024 by the authors.

## 04 — Title Screening

**Title:** Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
