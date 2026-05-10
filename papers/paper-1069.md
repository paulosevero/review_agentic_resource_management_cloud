---
id: paper-1069
title: 'Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Liu, Wenshuai
- Fu, Yaru
- Guo, Yongna
- Lee Wang, Fu
- Sun, Wen
- Zhang, Yan
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2024.3452689
url: https://www.scopus.com/pages/publications/85204248889?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17294--17309
keywords:
- Digital twin (DT)
- DT migration
- DT synchronization
- heterogeneous agent proximal policy optimization (HAPPO)
- multi-access edge computing (MEC)
- resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1069 — Two-Timescale Synchronization and Migration for Digital Twin Networks: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital twins (DTs) have emerged as a promising enabler for representing the real-time states of physical worlds and realizing self-sustaining systems. In practice, DTs of physical devices, such as mobile users (MUs), are commonly deployed in multi-access edge computing (MEC) networks for the sake of reducing latency. To ensure the accuracy and fidelity of DTs, it is essential for MUs to regularly synchronize their status with their DTs. However, MU mobility introduces significant challenges to DT synchronization. Firstly, MU mobility triggers DT migration which could cause synchronization failures. Secondly, MUs require frequent synchronization with their DTs to ensure DT fidelity. Nonetheless, DT migration among MEC servers, caused by MU mobility, may occur infrequently. Accordingly, we propose a two-timescale DT synchronization and migration framework with reliability consideration by establishing a non-convex stochastic problem to minimize the long-term average energy consumption of MUs. We use Lyapunov theory to convert the reliability constraints and reformulate the new problem as a partially observable Markov decision-making process (POMDP). Furthermore, we develop a heterogeneous agent proximal policy optimization with Beta distribution (Beta-HAPPO) method to solve it. Numerical results show that our proposed Beta-HAPPO method achieves significant improvements in energy savings when compared with other benchmarks.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1069.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
