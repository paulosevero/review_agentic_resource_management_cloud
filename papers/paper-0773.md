---
id: paper-0773
title: Toward cooperative multi-agent video streaming perception; [面向多设备协同场景的实时视频流分析系统]
authors:
- Yang, Zheng
- Dong, Liang
- Cai, Xinjun
venue: Scientia Sinica Informationis
venue_type: journal
year: 2023
doi: 10.1360/SSI-2021-0179
url: https://www.scopus.com/pages/publications/85147954520?origin=resultslist
publisher: Science Press (China)
pages: 46--65
keywords:
- edge computing
- multi-agent cooperation
- multi-objective optimization
- Pareto optimal state
- real-time video analysis
language: Chinese
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

# paper-0773 — Toward cooperative multi-agent video streaming perception; [面向多设备协同场景的实时视频流分析系统]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Video streaming perception ability is critical for AI applications on resource-constrained devices (agents), which prefers to offload video streams from devices to edge servers for real-time inference by deep neural networks (DNNs). Meanwhile, the multi-agent system (MAS) community is attempting to run DNNs on multiple cooperative agents to enable improved swarm intelligence-based tasks (e.g., drone swarm intelligence, self-driving fleet collaboration, and multi-agent robot cooperation). However, transferring video streaming perception capability from single-agent systems to MASs is extremely difficult due to spontaneous competition-induced trade-offs between the desired goals of accuracy, consistency, and capacity, which are three critical but conflicting measuring indexes. In this paper, we present the design and implementation of MASSIVE, an edge-assisted cooperative multi-agent video streaming perception system that simultaneously achieves all three desired goals. In our design, we consider the performance characteristics of video streaming perception and the insight of its periodic offloading pattern. On this basis, we develop a Pareto improvement scheduler to eliminate spontaneous competition among agents, allowing multi-objective optimization to achieve an ideal Pareto optimal state. Finally, we propose a virtual traffic shaper based on the mainstream 802.11 MAC protocol to ensure deterministic periodic video stream offloading in an uncertain wireless network. Our experiments demonstrate that MASSIVE achieves 122.7% accuracy and 1.8x capacity compared to the closest baseline on multiple actual cooperative vision tasks with even better consistency, and achieves an ideal Pareto optimal state in a wireless environment. © 2022 National Research Ogarev Mordovia State University. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0773.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
