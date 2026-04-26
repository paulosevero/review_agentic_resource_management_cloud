---
id: "paper-1948"
title: "Astral: A Datacenter Infrastructure for Large Language Model Training at Scale"
authors: ["Meng, Qingkai", "Zheng, Hao", "Zhang, Zhenhui", "Lao, ChonLam", "Huang, Chengyuan", "Li, Baojia", "Zhu, Ziyuan", "Lu, Hao", "Dang, Weizhen", "Lin, Zitong", "Zhang, Weifeng", "Liu, Lingfeng", "Gong, Yuanyuan", "He, Chunzhi", "Hu, Xiaoyuan", "Xia, Yinben", "Li, Xiang", "He, Zekun", "Wang, Yachen", "Zou, Xianneng", "Yang, Kun", "Antichi, Gianni", "Chen, Guihai", "Tian, Chen"]
year: 2025
venue: "SIGCOMM 2025 - ACM SIGCOMM 2025 Conference"
venue_type: "conference"
doi: "10.1145/3718958.3750521"
url: "https://www.scopus.com/pages/publications/105016192622?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "609--625"
keywords: ["Large Language Model", "Network Architecture", "Network Infrastructure", "Network Monitoring", "Network Simulations"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1948 — Astral: A Datacenter Infrastructure for Large Language Model Training at Scale

## Metadata

- **Authors:** Meng, Qingkai and Zheng, Hao and Zhang, Zhenhui and Lao, ChonLam and Huang, Chengyuan and Li, Baojia and Zhu, Ziyuan and Lu, Hao and Dang, Weizhen and Lin, Zitong and Zhang, Weifeng and Liu, Lingfeng and Gong, Yuanyuan and He, Chunzhi and Hu, Xiaoyuan and Xia, Yinben and Li, Xiang and He, Zekun and Wang, Yachen and Zou, Xianneng and Yang, Kun and Antichi, Gianni and Chen, Guihai and Tian, Chen
- **Year:** 2025
- **Venue:** SIGCOMM 2025 - ACM SIGCOMM 2025 Conference
- **DOI:** 10.1145/3718958.3750521
- **URL:** https://www.scopus.com/pages/publications/105016192622?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 609--625
- **Language:** English
- **Keywords:** Large Language Model; Network Architecture; Network Infrastructure; Network Monitoring; Network Simulations

### Abstract

The flourishing of Large Language Models (LLMs) calls for increasingly ultra-scale training. In this paper, we share our experience in designing, deploying, and operating our novel Astral datacenter infrastructure, along with operational lessons and evolutionary insights gained from its production use. Astral has three important innovations: (i) a same-rail interconnection network architecture on tier-2, which enables the scaling of LLM training. To physically deploy this high-density infrastructure, we introduce a distributed high-voltage direct current power system and a new air-liquid integrated cooling system. (ii) a full-stack monitoring system featuring cross-host and hierarchical logging correlation, which diagnoses failures at scale and precisely localizes root causes. (iii) an operator-granular forecasting component Seer that efficiently generates operator execution timelines with acceptable accuracy, aiding in fault diagnosis, model tuning, and network architecture upgrading. Astral infrastructure has been gradually deployed over 18 months, supporting LLM training and inference for multiple customers. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Astral: A Datacenter Infrastructure for Large Language Model Training at Scale

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Astral: A Datacenter Infrastructure for Large Language Model Training at Scale
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Astral: A Datacenter Infrastructure for Large Language Model Training at Scale
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
