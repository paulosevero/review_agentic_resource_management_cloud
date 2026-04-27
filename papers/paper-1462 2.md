---
id: "paper-1462"
title: "Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices"
authors: ["Chen, Yuhao", "Yan, Yuxuan", "Ge, Shuowei", "Qin, Yuyang", "Zheng, Yue", "Yang, Qianqian", "He, Shibo", "Shi, Zhiguo", "Chen, Jiming", "Shu, Yuanchao"]
year: 2025
venue: "ACM MobiCom 2025 - Proceedings of the 2025 the 31st Annual International Conference on Mobile Computing and Networking"
venue_type: "conference"
doi: "10.1145/3680207.3723487"
url: "https://www.scopus.com/pages/publications/105023823310?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "483--497"
keywords: ["Edge Collaborative Training", "Large Language Models"]
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

# paper-1462 — Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices

## Metadata

- **Authors:** Chen, Yuhao and Yan, Yuxuan and Ge, Shuowei and Qin, Yuyang and Zheng, Yue and Yang, Qianqian and He, Shibo and Shi, Zhiguo and Chen, Jiming and Shu, Yuanchao
- **Year:** 2025
- **Venue:** ACM MobiCom 2025 - Proceedings of the 2025 the 31st Annual International Conference on Mobile Computing and Networking
- **DOI:** 10.1145/3680207.3723487
- **URL:** https://www.scopus.com/pages/publications/105023823310?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 483--497
- **Language:** English
- **Keywords:** Edge Collaborative Training; Large Language Models

### Abstract

Large language models (LLMs) have emerged as a cornerstone for advancing AI technologies. It revolutionizes the way we interact with devices, websites, and information, and paves the way for the development of highly intuitive and capable virtual assistants. Training of today’s LLMs happens in cloud data centers due to the requirement of enormous data and a significant amount of computing power. Despite extensive research in mobile edge computing, fine-tuning pre-trained LLMs using resource-constrained devices like commodity smartphones remains highly under-explored. In this paper, we propose Confidant, a practical collaborative training framework that allows modern LLMs to be fine-tuned across multiple off-the-shelf mobile devices. To this end, Confidant partitions an LLM into several sub-models, allowing each of them to fit in the memory of a mobile device. Multiple mobile devices then collaborate to train the LLM by employing a novel pipeline parallel training approach. In specific, Confidant encompasses a memory-aware dynamic model partitioning and intra-device multi-processor scheduler to minimize the training time across heterogeneous platforms. To ensure resilient distributed training, a hybrid fault tolerance mechanism is devised to proactively manage potential device and network failures. We fully implemented Confidant in C++/Python, and built a cross-framework adapter, enabling collaborative training on a variety of mobile platforms. Experimental results show that Confidant excels in achieving computation-, memory-efficient, and robust customization of LLMs - it manages to train state-of-the-art billion-sized LLMs including BERT, GPT-2, Phi2, and LLaMA3, and fine-tunes Phi2-2.7B on Alpaca in just 40.1 hours using three consumer-grade mobile devices. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices
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
