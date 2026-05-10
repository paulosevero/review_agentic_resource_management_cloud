---
id: paper-2473
title: Collaborative Video Streaming with Super-Resolution in Multi-User MEC Networks
authors:
- Zhou, Xiaobo
- Zeng, Jiaxin
- Ge, Shuxin
- Liu, Xilai
- Qiu, Tie
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3461685
url: https://www.scopus.com/pages/publications/85204795325?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 571--584
keywords:
- Multi-access edge computing (MEC)
- multi-agent soft actor-critic
- Quality of Experience (QoE)
- super-resolution
- video streaming
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

# paper-2473 — Collaborative Video Streaming with Super-Resolution in Multi-User MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The ever-increasing quality of experience (QoE) demand for video streaming has prompted the integration of video super-resolution and multi-access edge computing networks (MEC). With super-resolution, the low-resolution frames can be reconstructed into high-resolution ones by edge node and end device collaboratively, which is beneficial in improving QoE. However, the existing works focus on designing video streaming strategies in single-user scenarios, which cannot be applied to multi-user scenarios due to the resource contention among users, as well as the huge solution space of coupled bitrate selection and workload share between edge-end. To fill this gap, we propose a collaborative video streaming strategy with super-resolution in multi-user MEC networks, named Co-Video, to maximize the average QoE by making optimal bitrate selection and workload share. We first formulate the problem as an optimization problem towards maximum average QoE, where the QoE incorporates playback delay, video quality, and smoothness. Then, we transform the optimization problem into a partially observable Markov decision process (POMDP) and exploit the Co-Video strategy based on the multi-agent soft actor-critic (MASAC) algorithm. Specifically, Co-Video utilizes the branching actor network to converge to good policy stably. Finally, trace-driven simulations on real-world bandwidth traces demonstrate that Co-Video outperforms the state-of-the-art baselines. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2473.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
