---
id: "paper-1260"
title: "PancakeFS: A Write Efficiently and Read Optimized Filesystem"
authors: ["Wang, Yongkang", "Liu, Yang", "Chen, Zhiguang"]
year: 2024
venue: "2024 4th International Conference on Consumer Electronics and Computer Engineering, ICCECE 2024"
venue_type: "conference"
doi: "10.1109/ICCECE61317.2024.10504183"
url: "https://www.scopus.com/pages/publications/85192395878?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "196--199"
keywords: ["component", "Key-Value Filesystem", "LSM-Tree", "Read-optimized", "Subtree Partitioning", "Write-efficiently"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1260 — PancakeFS: A Write Efficiently and Read Optimized Filesystem

## Metadata

- **Authors:** Wang, Yongkang and Liu, Yang and Chen, Zhiguang
- **Year:** 2024
- **Venue:** 2024 4th International Conference on Consumer Electronics and Computer Engineering, ICCECE 2024
- **DOI:** 10.1109/ICCECE61317.2024.10504183
- **URL:** https://www.scopus.com/pages/publications/85192395878?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 196--199
- **Language:** English
- **Keywords:** component; Key-Value Filesystem; LSM-Tree; Read-optimized; Subtree Partitioning; Write-efficiently

### Abstract

With the development of emerging technologies such as cloud computing and large AI models (such as LLM), many applications have placed higher demands on the intensive read and write processing of massive data. Addressing the limitations of traditional file systems, we propose PancakeFS, an LSM-Tree-based file system. Leveraging the write-friendly characteristics of LSM-Tree, PancakeFS exhibits efficient write performance. We improve read performance through the design of an inode allocation algorithm based on subtree partitioning and optimization of the disk layout for hot data reconstruction. Our experimental results demonstrate that PancakeFS outperforms Ext4 and TableFS in terms of both read and write performance.  © 2024 IEEE.

## 04 — Title Screening

**Title:** PancakeFS: A Write Efficiently and Read Optimized Filesystem

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** PancakeFS: A Write Efficiently and Read Optimized Filesystem
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** PancakeFS: A Write Efficiently and Read Optimized Filesystem
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
