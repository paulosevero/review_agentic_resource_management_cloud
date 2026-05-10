---
id: paper-2258
title: Dynamic Power Management Through Multi-agent Deep Reinforcement Learning for Heterogeneous Systems
authors:
- Wang, Yiming
- Zhang, Weizhe
- Hao, Meng
- Kong, Weizhi
- Wen, Yuan
venue: ACM Transactions on Architecture and Code Optimization
venue_type: journal
year: 2025
doi: 10.1145/3716872
url: https://www.scopus.com/pages/publications/105010710472?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- Energy and performance optimization
- heterogeneous system
- multiple agent deep reinforcement learning
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

# paper-2258 — Dynamic Power Management Through Multi-agent Deep Reinforcement Learning for Heterogeneous Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Power management and optimization play a significant role in modern computer systems, from battery-powered devices to servers running in data centers. Existing approaches for power capping fail to meet the requirements presented by dynamic workloads, and the situation becomes even more severe, given the divergent energy efficiency of workloads on heterogeneous hardware platforms. Adaptively optimizing energy consumption for dynamic workloads presents a great challenge to heterogeneous systems. To tackle this challenge, we present a machine learning based method to improve system-level power efficiency. We employ multi-agent deep reinforcement learning (MADRL) to automatically explore the relationship between long-term performance and the power budget for workloads of different types on classic CPU-GPU heterogeneous platforms. Our framework equips each device with an agent, enabling decentralized control over its power budget while maintaining centralized coordination to maximize the running time of applications within a power cap. We evaluate our approach against state-of-the-art methods on CPU-GPU platforms. Experimental results show that our method improves performance by an average of 8.5%. Additionally, our method is significantly more stable compared to the state-of-the-art heuristic approach.  © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2258.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
