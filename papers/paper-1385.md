---
id: paper-1385
title: 'Techie: Tackling Video Prefetching at Edge Networks as POMDP Via an Intrinsically Motivated RL Agent'
authors:
- Alkassab, Nawras
- Huang, Chin-Tser
- Botran, Tania Lorido
venue: SIGIR 2025 - Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval
venue_type: conference
year: 2025
doi: 10.1145/3726302.3730089
url: https://www.scopus.com/pages/publications/105011828772?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 948--957
keywords:
- Content Delivery Networks
- Deep Reinforcement Learning
- Edge Computing
- Fog Computing
- Intrinsic Rewards
- Prefetching
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1385 — Techie: Tackling Video Prefetching at Edge Networks as POMDP Via an Intrinsically Motivated RL Agent

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Video prefetching techniques play a critical role in hiding the I/O latency of video delivery from cloud networks to access networks by optimizing edge networks. Content Delivery Networks rely on edge computing to improve Quality of Experience at the client-side, and improve resource utilization at edge and cloud networks simultaneously by utilizing prefetching optimization techniques. Recently, we have witnessed a trend in shifting intelligence to edge networks by building video prefetchers that utilize deep reinforcement learning to make online prefetching decisions. Unfortunately, these methods often lack generalization to different workloads when dealing with long sequences, rendering them incapable of adapting to distribution shifts and various changes in users’ requests which represent a non i.i.d distribution. In this work, we tackle video prefetching at edge networks as a Partially Observable Markov Decision Process, and propose Techie, an intrinsically motivated policy-gradient reinforcement learning agent that differentiates intrinsic rewards from extrinsic rewards based on their availability to edge networks. Techie is adaptive to unseen user requests by prefetching aggressively to handle randomization in workloads, achieving 52.27% of prefetching accuracy and 34.34% of prefetching coverage. Our results show that Techie improves prefetching accuracy and coverage by at least 16.12% and 6.57%, respectively, compared to baseline approaches that utilize deep learning, deep reinforcement learning, or video popularity to build prefetching algorithms. Consequently, Techie minimizes end-to-end latency by at least 7.5% and reduces cache pollution with an improvement of at least 13.1% on unseen user requests compared to baselines. © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1385.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
