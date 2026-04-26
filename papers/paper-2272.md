---
id: "paper-2272"
title: "Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks"
authors: ["Wang, Yuxiang", "Zhang, Jiao", "Wan, Zirui", "Cai, Leixin", "Wang, Shuo", "Huang, Tao"]
year: 2025
venue: "Proceedings - International Conference on Computer Communications and Networks, ICCCN"
venue_type: "conference"
doi: "10.1109/ICCCN65249.2025.11133854"
url: "https://www.scopus.com/pages/publications/105016222647?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Congestion Control", "Data-center networks", "Packet Spraying", "RDMA"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2272 — Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks

## Metadata

- **Authors:** Wang, Yuxiang and Zhang, Jiao and Wan, Zirui and Cai, Leixin and Wang, Shuo and Huang, Tao
- **Year:** 2025
- **Venue:** Proceedings - International Conference on Computer Communications and Networks, ICCCN
- **DOI:** 10.1109/ICCCN65249.2025.11133854
- **URL:** https://www.scopus.com/pages/publications/105016222647?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Congestion Control; Data-center networks; Packet Spraying; RDMA

### Abstract

Due to the low entropy traffic characteristics of LLM (Large Language Model) training, existing load balancing mechanisms such as Equal-Cost Multi-Path (ECMP) fail to fully utilize the redundant bandwidth between computing nodes in RDMA over Converged Ethernet (RoCE). Packet spraying mechanism has become a typical solution to the load balancing problem in RoCEs. However, it has a negative effect on congestion control mechanisms and suffers severe out-of-order problems.In this paper, we propose Mercury, an host-driven spraying scheme that synergizes congestion feedback and reordering control. Mercury selects paths by leveraging ECN, RTT, and reordering metrics, adjusts rates via multi-metric window. It also employs receiver-side buffers with priority-based dropping to mitigate out-of-order penalties. Evaluations in ns-3 under AllReduce/All-to-All traffic show Mercury reduces maximum flow completion time (Max FCT) by 40%-63% compared to ECMP-based DCQCN/TIMELY/HPCC. It also achieves at least 10%-20% improvement against switch-based spraying. © 2025 IEEE.

## 04 — Title Screening

**Title:** Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks
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
