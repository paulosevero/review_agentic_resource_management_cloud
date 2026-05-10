---
id: paper-1816
title: Polygon training architecture for foundation models with network- and device-level heterogeneity
authors:
- Li, Chuantao
- Liu, Fulai
- Wu, Xiaoming
- Huo, Jidong
- Wang, Chunxiao
- Liang, Antian
- Zhao, Zhigang
- Gao, Longxiang
venue: Information Fusion
venue_type: journal
year: 2025
doi: 10.1016/j.inffus.2025.103264
url: https://www.scopus.com/pages/publications/105004937680?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Foundation models training
- Fusion system design
- Heterogeneous training
- Parallelism optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1816 — Polygon training architecture for foundation models with network- and device-level heterogeneity

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models have experienced rapid growth, constrained by the computational limits of training foundation models. With the continuous release of new products, high-end devices are increasingly accessible, eventually transitioning into the mid-range and low-end segments. A pivotal focus in current research is the facilitation of joint training across diverse regions and devices. However, this research encounters dual-heterogeneous challenges in both network and device levels. We introduce a novel polygon training architecture for foundation models, designed to support large-scale training paradigms. Our approach integrates critical factors—including model size, network conditions, and device performance-from both global and local perspectives. Initially, we develop a lightweight polygon initialization algorithm that conceptualizes data centers as the fundamental units on a global scale. This algorithm evaluates computing power, latency, and bandwidth between units to establish an initial training strategy that leverages both pipeline and data parallelism. Following this, we consider the complexities introduced by diverse combinations of heterogeneous devices and network conditions, which give rise to intricate communication scenarios. To tackle this issue, we design a polygon local optimization algorithm-a precise search strategy that accurately assesses communication costs during model training across heterogeneous configurations. This approach identifies an efficient parallel architecture, enabling enhanced collaborative training with fine granularity. Our experimental results indicate that, compared to existing state-of-the-art methods, our algorithm expands the training scale by 1.5 × with the same computational resources, accelerates processing speed by 1.9 ×, and reduces training time by 46% for comparable tasks. © 2025 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1816.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
