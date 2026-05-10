---
id: paper-2378
title: A Deep Reinforcement Learning-Based Service Function Chain Placement Strategy for Latency-Sensitive Tasks in Power Information Networks
authors:
- Ye, Shengyong
- Long, Chuan
- Yang, Xinting
- Li, Ting
- Liu, Xuna
- Liu, Liyang
- Han, Yuqi
- Li, Da
venue: Proceedings of 2025 IEEE 4th International Conference of Safe Production and Informatization, IICSPI 2025
venue_type: conference
year: 2025
doi: 10.1109/IICSPI66775.2025.11437737
url: https://www.scopus.com/pages/publications/105036003380?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 69--72
keywords:
- Deep Reinforcement Learning
- Edge Computing
- Latency Optimization
- Power Information Networks
- Resource Allocation
- Service Function Chain
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2378 — A Deep Reinforcement Learning-Based Service Function Chain Placement Strategy for Latency-Sensitive Tasks in Power Information Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> While the performance of power information networks is critical for real-time smart grid applications, existing task placement strategies suffer from high latency and poor scalability by treating complex computations as monolithic blocks and using static allocation heuristics. To address this, we propose a novel framework that uniquely models complex tasks as decomposable Service Function Chains (SFCs) and utilizes a deep reinforcement learning (DRL) agent to learn an adaptive placement policy across the cloud-edge continuum. We evaluate our approach through extensive simulations in a custom-built, discrete-event network environment, comparing it against random, greedy, and cloud-first baseline algorithms under diverse workloads and network scales. The results demonstrate exceptional scalability, showing that as the network scales from 5 to 25 edge nodes, our proposed method improves average end-to-end latency by 12.4% and increases system throughput by over 297%, in stark contrast to baseline methods whose performance degrades significantly. This work provides a robust and highly scalable solution for dynamic service placement and offers a new paradigm for designing intelligent, autonomous resource management systems for latency-critical applications in power systems and other industrial IoT domains. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2378.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
