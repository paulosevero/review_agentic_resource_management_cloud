---
id: paper-2247
title: LLM-Based V2X Multi-Model Sensor Data Fusion for Improved Road Safety and Data Privacy
authors:
- Wan, Zhengyu
- Guo, Chengpeng
- Hu, Bintao
- Du, Jianbo
- Mou, Xiaolin
- Zhang, Junwei
venue: Proceedings - International Conference on Computer Communications and Networks, ICCCN
venue_type: conference
year: 2025
doi: 10.1109/ICCCN65249.2025.11133978
url: https://www.scopus.com/pages/publications/105016155796?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- data fusion
- large language models (LLM)
- multi-model sensor
- V2X driving assistance
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2247 — LLM-Based V2X Multi-Model Sensor Data Fusion for Improved Road Safety and Data Privacy

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of large language models (LLMs) with mobile edge computing (MEC) systems presents a novel approach to enhancing vehicle-to-everything (V2X) connected autonomous driving. This study aims to address the prevalent challenges in multi-model sensor data fusion, such as latency, privacy preservation, and the need for dynamic adaptation to evolving environmental conditions, by leveraging real-time data from LiDAR sensors. We propose an LLM-based framework to improve V2X driving assistance systems' operational efficiency, safety, and reliability, where pictures and image recognition work as integrated data from multiple sensors to train various vehicle and lane detection models. Based on the benefits of federated learning, i.e., distributed at each MEC server and optimising models accordingly, these training models can avoid the data privacy issue in V2X driving assistance implementation. The application of generated test data significantly improves the success rate of the lane detection feature and pedestrian detection, by 95% and 85%, respectively. The experiment results demonstrate that our proposed framework is effective and feasible. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2247.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
