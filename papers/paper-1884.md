---
id: paper-1884
title: 'GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing'
authors:
- Liu, Xiaoke
- Teng, Wenjie
- Yu, Haoran
- Yao, Zhuoyi
- Wang, Chengzhen
- Peng, Yuzhong
- Han, Xiaoqing
- Liu, Jianming
venue: Frontiers in Plant Science
venue_type: journal
year: 2025
doi: 10.3389/fpls.2025.1712432
url: https://www.scopus.com/pages/publications/105023909405?origin=resultslist
publisher: Frontiers Media SA
pages: ''
keywords:
- edge computing
- lightweight YOLO
- multimodal detection
- plant phenotyping
- tomato smart agriculture
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1884 — GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Introduction: The advancement of smart agriculture has witnessed increasing applications of computer vision in crop monitoring and management. However, existing approaches remain challenged by high computational complexity, limited real-time capability, and poor multi-task coordination in tomato cultivation scenarios. Methods: To address these limitations, an intelligent tomato management system is proposed based on the Ghost-based Adaptive Efficient You Only Look Once (GAE-YOLO) algorithm. The lightweight architecture of the GAE-YOLO framework is achieved through the replacement of standard convolutional layers with Ghost Convolution (GhostConv) modules, while detection accuracy is significantly improved by the integration of both AReLU activation functions and Effective Intersection over Union (E-IoU) loss optimization. The system, implemented on a Jetson TX2 embedded platform, also incorporates ZED stereo vision for 3D localization and a PyQt6-based visualization platform. Results: When implemented on Jetson TX2, the system achieving 93.5% mean Average Precision at 50% intersection over union (mAP@50) at 10.2 frames per second (FPS), which can be optimized to 27 FPS by employing TensorRT acceleration and 720p resolution for scenarios demanding higher throughput. Furthermore, it establishes standardized assessment systems for tomato maturity and yield prediction, and offers integrated modules for disease diagnosis and agricultural large language model consultation. Discussion: This work establishes a new paradigm for edge computing in agriculture while providing critical technical support for smart farming development. Copyright © 2025 Liu, Teng, Yu, Yao, Wang, Peng, Han and Liu.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1884.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
