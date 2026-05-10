---
id: paper-2601
title: 'Real-Time Scheduling of CPU/GPU Heterogeneous Tasks in Dynamic IoT Systems: Enhancing GPU and Memory Efficiency'
authors:
- He, Xiao
- Pang, Shanchen
- Qiao, Sibo
- Gui, Haiyuan
- Yu, Shihang
- Rodrigues, Joel J. P.C.
- Mumtaz, Shahid
- Lyu, Zhihan
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3593250
url: https://www.scopus.com/pages/publications/105012247662?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 583--598
keywords:
- deep reinforcement learning
- GPU fragmentation
- IoT system
- memory control
- Mobile edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2601 — Real-Time Scheduling of CPU/GPU Heterogeneous Tasks in Dynamic IoT Systems: Enhancing GPU and Memory Efficiency

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The real-time processing of large-scale, heterogeneous tasks—including CPU-only, general-purpose GPU, and specialized GPU tasks—poses significant challenges in Internet of Things (IoT) systems, driven by severe GPU resource fragmentation, inefficient CPU and memory resource utilization on edge servers. These issues often compromise system processing performance and server stability. To address these issues, we formulate a multi-stage mixed-integer nonlinear programming (MINLP) model, to jointly optimize GPU fragmentation rate and system processing capability. We then introduce a novel deviation-based Lyapunov optimization framework that explicitly maintains memory utilization around a predefined optimal threshold, effectively balancing resource usage and system stability. Finally, to achieve real-time decision-making for massive tasks in dynamic systems with randomly arriving tasks, we propose the MA-LHTO algorithm, a multi-agent deep reinforcement learning approach that incorporates a multi-head architecture, entropy-based exploration, and a parameter reset mechanism. Experimental results confirm that our algorithm significantly improves resource utilization, and exhibits good performance under various working conditions. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2601.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
