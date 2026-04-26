---
id: "paper-1891"
title: "OPS: Outlier-Aware Precision-Slice Framework for LLM Acceleration"
authors: ["Liu, Fangxin", "Yang, Ning", "Wang, Zongwu", "Zhu, Xuanpeng", "Yao, Haidong", "Xiong, Xiankui", "Sun, Qi", "Jiang, Li"]
year: 2025
venue: "Proceedings -Design, Automation and Test in Europe, DATE"
venue_type: "conference"
doi: "10.23919/DATE64628.2025.10993106"
url: "https://www.scopus.com/pages/publications/105006925128?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AI applications", "Cloud computing costs", "Encoding/decoding", "Hardware resources", "High-order", "Higher-order", "Language model", "Model size", "Modeling accuracy", "User privacy"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-1891 — OPS: Outlier-Aware Precision-Slice Framework for LLM Acceleration

## Metadata

- **Authors:** Liu, Fangxin and Yang, Ning and Wang, Zongwu and Zhu, Xuanpeng and Yao, Haidong and Xiong, Xiankui and Sun, Qi and Jiang, Li
- **Year:** 2025
- **Venue:** Proceedings -Design, Automation and Test in Europe, DATE
- **DOI:** 10.23919/DATE64628.2025.10993106
- **URL:** https://www.scopus.com/pages/publications/105006925128?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AI applications; Cloud computing costs; Encoding/decoding; Hardware resources; High-order; Higher-order; Language model; Model size; Modeling accuracy; User privacy

### Abstract

Large language models (LLMs) have transformed numerous AI applications, with on-device deployment becoming increasingly important for reducing cloud computing costs and protecting user privacy. However, the astronomical model size and limited hardware resources pose significant deployment challenges. Model quantization is a promising approach to mitigate this gap, but the presence of outliers in LLMs reduces its effectiveness. Previous efforts addressed this issue by employing compression-based encoding for mixed-precision quantization. These approaches struggle to balance model accuracy with hard-ware efficiency due to their value-wise outlier granularity and complex encoding/decoding hardware logic. To address this, we propose OPS (Outlier-aware Precision-Slicing), an acceleration framework that exploits massive sparsity in the higher-order part of LLMs by splitting 16-bit values into a 4-bit/12-bit format. Crucially, OPS introduces an early bird mechanism that leverages the high-order 4-bit computation to predict the importance of the full calculation result. This mechanism enables efficient computational skips by continuing execution only for important computations and using preset values for less significant ones. This scheme can be efficiently integrated with existing hardware accelerators like systolic arrays without complex encoding/decoding. As a result, OPS outperforms state-of-the-art outlier-aware accelerators, achieving a 1.3 - 4.3× performance boost with minimal model accuracy loss. This approach enables more efficient on-device LLM deployment, effectively balancing computational efficiency and model accuracy. © 2025 EDAA.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
