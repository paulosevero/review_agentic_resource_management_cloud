---
id: "paper-215"
title: "Efficient transformer-based large scale language representations using hardware-friendly block structured pruning"
authors: ["Li, Bingbing", "Kong, Zhenglun", "Zhang, Tianyun", "Li, Ji", "Li, Zhengang", "Liu, Hang", "Ding, Caiwen"]
year: 2020
venue: "Findings of the Association for Computational Linguistics Findings of ACL: EMNLP 2020"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85118457910?origin=resultslist"
publisher: "Association for Computational Linguistics (ACL)"
pages: "3187--3199"
keywords: ["Computational linguistics", "Distillation", "Block structured", "Block structures", "Compression rates", "Computational speed", "Edge computing", "Group lassos", "Hardware platform", "High-accuracy", "Language model", "Large-scales", "Natural language processing systems"]
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
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-215 — Efficient transformer-based large scale language representations using hardware-friendly block structured pruning

## Metadata

- **Authors:** Li, Bingbing and Kong, Zhenglun and Zhang, Tianyun and Li, Ji and Li, Zhengang and Liu, Hang and Ding, Caiwen
- **Year:** 2020
- **Venue:** Findings of the Association for Computational Linguistics Findings of ACL: EMNLP 2020
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85118457910?origin=resultslist
- **Publisher:** Association for Computational Linguistics (ACL)
- **Pages:** 3187--3199
- **Language:** English
- **Keywords:** Computational linguistics; Distillation; Block structured; Block structures; Compression rates; Computational speed; Edge computing; Group lassos; Hardware platform; High-accuracy; Language model; Large-scales; Natural language processing systems

### Abstract

Pre-trained large-scale language models have increasingly demonstrated high accuracy on many natural language processing (NLP) tasks. However, the limited weight storage and computational speed on hardware platforms have impeded the popularity of pre-trained models, especially in the era of edge computing. In this work, we propose an efficient transformer-based large-scale language representation using hardware-friendly block structure pruning. We incorporate the reweighted group Lasso into block-structured pruning for optimization. Besides the significantly reduced weight storage and computation, the proposed approach achieves high compression rates. Experimental results on different models (BERT, RoBERTa, and DistilBERT) on the General Language Understanding Evaluation (GLUE) benchmark tasks show that we achieve up to 5.0× with zero or minor accuracy degradation on certain task(s). Our proposed method is also orthogonal to existing compact pre-trained language models such as DistilBERT using knowledge distillation, since a further 1.79× average compression rate can be achieved on top of DistilBERT with zero or minor accuracy degradation. It is suitable to deploy the final compressed model on resource-constrained edge devices. We share the related codes and models at: https://bit.ly/3cvs2N2 © 2020 Association for Computational Linguistics

## 04 — Title Screening

**Title:** Efficient transformer-based large scale language representations using hardware-friendly block structured pruning

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Efficient transformer-based large scale language representations using hardware-friendly block structured pruning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Efficient transformer-based large scale language representations using hardware-friendly block structured pruning
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
