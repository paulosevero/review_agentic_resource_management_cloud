---
id: paper-1279
title: Mean-Field Game-Based Task-Offloaded Load Balance for Industrial Mobile Edge Computing Systems Using Software-Defined Networking
authors:
- Wu, Guowen
- Wang, Hui
- Zhang, Hong
- Shen, Yizhou
- Shen, Shigen
- Yu, Shui
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2024.3437761
url: https://www.scopus.com/pages/publications/85200265638?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13773--13786
keywords:
- Game theory
- load balance
- mean field game
- mobile edge computing
- multi-agent reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1279 — Mean-Field Game-Based Task-Offloaded Load Balance for Industrial Mobile Edge Computing Systems Using Software-Defined Networking

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Smart devices (SDs) used in the Industrial Internet of Things can generate computational tasks for processing the data generated during production. However, due to the limited processing power of SDs, it is necessary to transfer these computational tasks to more powerful devices for processing. To this end, we propose a Mobile Edge Computing (MEC) system based on a Software Defined Network (SDN) for SDs to offload their computational tasks. This MEC system includes multiple MEC servers to handle numerous SDs, which leads to load-balancing challenges among these servers. To tackle this problem, we develop a computational offloading model based on mean-field game theory and introduce a mean-field game-based load-balancing algorithm (MFGLB), which reduces processing latency and facilitates task scheduling through Multi-Agent Deep Reinforcement Learning. Each SD in the MEC system is considered a participant in the mean-field game, simplifying the complex stochastic game into a more manageable dual-agent game. We then prove the existence of Nash Equilibrium for this mean-field game. To evaluate the effectiveness of our MFGLB algorithm, we compare its performance with traditional load-balancing algorithms and a stochastic game-based load-balancing algorithm. Our experimental results demonstrate the superiority of MFGLB in reducing processing latency and addressing load imbalances.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1279.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
