---
id: "paper-1884"
title: "GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing"
authors: ["Liu, Xiaoke", "Teng, Wenjie", "Yu, Haoran", "Yao, Zhuoyi", "Wang, Chengzhen", "Peng, Yuzhong", "Han, Xiaoqing", "Liu, Jianming"]
year: 2025
venue: "Frontiers in Plant Science"
venue_type: "journal"
doi: "10.3389/fpls.2025.1712432"
url: "https://www.scopus.com/pages/publications/105023909405?origin=resultslist"
publisher: "Frontiers Media SA"
pages: ""
keywords: ["edge computing", "lightweight YOLO", "multimodal detection", "plant phenotyping", "tomato smart agriculture"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1884 — GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing

## Metadata

- **Authors:** Liu, Xiaoke and Teng, Wenjie and Yu, Haoran and Yao, Zhuoyi and Wang, Chengzhen and Peng, Yuzhong and Han, Xiaoqing and Liu, Jianming
- **Year:** 2025
- **Venue:** Frontiers in Plant Science
- **DOI:** 10.3389/fpls.2025.1712432
- **URL:** https://www.scopus.com/pages/publications/105023909405?origin=resultslist
- **Publisher:** Frontiers Media SA
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; lightweight YOLO; multimodal detection; plant phenotyping; tomato smart agriculture

### Abstract

Introduction: The advancement of smart agriculture has witnessed increasing applications of computer vision in crop monitoring and management. However, existing approaches remain challenged by high computational complexity, limited real-time capability, and poor multi-task coordination in tomato cultivation scenarios. Methods: To address these limitations, an intelligent tomato management system is proposed based on the Ghost-based Adaptive Efficient You Only Look Once (GAE-YOLO) algorithm. The lightweight architecture of the GAE-YOLO framework is achieved through the replacement of standard convolutional layers with Ghost Convolution (GhostConv) modules, while detection accuracy is significantly improved by the integration of both AReLU activation functions and Effective Intersection over Union (E-IoU) loss optimization. The system, implemented on a Jetson TX2 embedded platform, also incorporates ZED stereo vision for 3D localization and a PyQt6-based visualization platform. Results: When implemented on Jetson TX2, the system achieving 93.5% mean Average Precision at 50% intersection over union (mAP@50) at 10.2 frames per second (FPS), which can be optimized to 27 FPS by employing TensorRT acceleration and 720p resolution for scenarios demanding higher throughput. Furthermore, it establishes standardized assessment systems for tomato maturity and yield prediction, and offers integrated modules for disease diagnosis and agricultural large language model consultation. Discussion: This work establishes a new paradigm for edge computing in agriculture while providing critical technical support for smart farming development. Copyright © 2025 Liu, Teng, Yu, Yao, Wang, Peng, Han and Liu.

## 04 — Title Screening

**Title:** GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
