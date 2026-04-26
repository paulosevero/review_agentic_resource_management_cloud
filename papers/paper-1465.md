---
id: "paper-1465"
title: "Demo: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices"
authors: ["Chen, Yuhao", "Zheng, Yue", "Yan, Yuxuan", "Ge, Shuowei", "Li, Shun", "Yang, Qianqian", "He, Shibo", "Shi, Zhiguo", "Chen, Jiming", "Shu, Yuanchao"]
year: 2025
venue: "ACM MobiCom 2025 - Proceedings of the 2025 the 31st Annual International Conference on Mobile Computing and Networking"
venue_type: "conference"
doi: "10.1145/3680207.3765599"
url: "https://www.scopus.com/pages/publications/105023830483?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "1228--1230"
keywords: ["Edge Collaborative Training, Large Language Models"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1465 — Demo: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices

## Metadata

- **Authors:** Chen, Yuhao and Zheng, Yue and Yan, Yuxuan and Ge, Shuowei and Li, Shun and Yang, Qianqian and He, Shibo and Shi, Zhiguo and Chen, Jiming and Shu, Yuanchao
- **Year:** 2025
- **Venue:** ACM MobiCom 2025 - Proceedings of the 2025 the 31st Annual International Conference on Mobile Computing and Networking
- **DOI:** 10.1145/3680207.3765599
- **URL:** https://www.scopus.com/pages/publications/105023830483?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 1228--1230
- **Language:** English
- **Keywords:** Edge Collaborative Training, Large Language Models

### Abstract

Despite large language models (LLMs) being an essential part of our lives, training of LLMs still needs to be done in cloud data centers due to the large requirements of data and computing power, leaving fine-tuning pre-trained LLMs on resource-constrained mobile devices remains highly underexplored. In this demo, we present Confidant, a practical collaborative training system that allows modern LLMs to be fine-tuned across multiple off-the-shelf mobile devices. Confidant partitions an LLM into several sub-models, deploying each of them to a mobile device. Multiple mobile devices then collaborate to train the LLM by employing a novel pipeline parallel training approach. Specifically, Confidant encompasses a memory-aware dynamic model partitioning and intra-device multi-processor scheduler to minimize the training time across heterogeneous platforms. A hybrid fault tolerance mechanism is also devised to proactively manage potential device and network failures. By building a cross-framework adapter and fully implementing Confidant on smartphones and laptops, we present the demo of collaborative training on a variety of mobile platforms. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Demo: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Demo: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Demo: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices
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
