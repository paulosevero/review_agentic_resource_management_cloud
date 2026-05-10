---
id: paper-2348
title: 'Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach'
authors:
- Yahya, Widhi
- Lai, Yuan-Cheng
- Lin, Ying-Dar
- Rohmatillah, Mahdin
- Kar, Binayak
venue: Journal of Network and Computer Applications
venue_type: journal
year: 2025
doi: 10.1016/j.jnca.2025.104277
url: https://www.scopus.com/pages/publications/105012613745?origin=resultslist
publisher: Academic Press
pages: ''
keywords:
- Central Office Re-Architected as a Data Center (CORD)
- Edge computing
- Offloading
- Optimization
- Reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2348 — Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In a distributed edge system, such as the Central Office Re-architected as a Datacenter (CORD), traffic offloading is crucial for minimizing latency by redistributing traffic from overloaded edge sites to less congested sites. The control plane must make rapid decisions to accommodate fluctuating traffic rates. Traditional optimization methods, such as Simulated Annealing (SA), often require significant time to converge in this complex environment. This study proposes the Weighted Action Twin Delayed Deep Deterministic Policy Gradient (WA-TD3), a weighted action approach that optimizes the exploration stage to reduce the exploration space of the original TD3 algorithm in continuous action spaces, resulting in faster convergence. WA-TD3 enhances decision-making in edge offloading by effectively addressing the continuous search space problem and enabling quicker decision-making compared to traditional optimization methods. Evaluation results indicate that WA-TD3 achieves decision times measured in milliseconds, making it five orders of magnitude faster than SA, which has decision times ranging from minutes to hours, despite WA-TD3 exhibiting slightly higher average packet latency. In addition to its performance advantages, the offloading agent can be implemented in a centralized cloud (single agent) or across multiple core networks (multi-agent) with varying coverage. In CORD with 50 sites, the convergence times for SA, single-agent WA-TD3, and multi-agent WA-TD3 are 47,813 s, 1,302 s, and 929 s, respectively. © 2025 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2348.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
