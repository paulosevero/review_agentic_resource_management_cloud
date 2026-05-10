---
id: paper-1038
title: Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence
authors:
- Li, Danyang
- Zhao, Yishujie
- Xu, Jingao
- Zhang, Shengkai
- Shangguan, Longfei
- Ma, Qiang
- Ding, Xuan
- Yang, Zheng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2024.3424452
url: https://www.scopus.com/pages/publications/105002087773?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12983--12997
keywords:
- drone-based applications
- Edge computing
- multi-agent collaboration
- software and hardware co-design
- visual SLAM
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1038 — Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge-assisted visual SLAM plays a crucial role in enabling innovative mobile applications, such as autonomous swarm inspection, search-and-rescue, and smart logistics. Constrained by the computational capacities of lightweight mobile devices, current approaches delegate lightweight, time-sensitive tracking tasks to the mobile end while offloading resource-intensive, latency-tolerant map optimization tasks to the edge. However, our pilot study reveals several limitations of the tracking-optimization decoupled paradigm, stemming from the disruption of inter-dependencies between the two tasks. In this paper, we design and implement edgeSLAM2, an innovative system that reshapes the edge-assisted visual SLAM paradigm by tightly integrating tracking and partial-yet-crucial optimization on mobile. edgeSLAM2 harnesses the heterogeneous computing units offered by the commercial systems-on-chip (SoCs) to enhance the computational capacity of mobile devices, which in turn, allows edgeSLAM2 to design a suit of novel algorithms for map sync, optimization, and tracking that accommodate such architectural upgrade. By capitalizing on the full potential of on-chip intelligence, edgeSLAM2 supports both solitary and collaborative SLAM with accuracy and immediacy, underpinned by a cohesive software-hardware co-design. We deploy edgeSLAM2 on drones for industrial inspection. Comprehensive experiments in one of the world's largest oil fields over three months demonstrate its superior performance.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1038.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
