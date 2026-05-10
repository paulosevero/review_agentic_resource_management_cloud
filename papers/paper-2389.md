---
id: paper-2389
title: Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing
authors:
- You, Feiran
- Yuan, Xin
- Ni, Wei
- Jamalipour, Abbas
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2024.3499342
url: https://www.scopus.com/pages/publications/85210284778?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1887--1901
keywords:
- game theory
- local differential privacy (LDP)
- Multi-access edge computing (MEC)
- multi-agent deep deterministic policy gradient (MADDPG)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2389 — Privacy-Preserving Multi-Agent Deep Reinforcement Learning for Effective Resource Auction in Multi-Access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) offloads services for mobile users to facilitate the integration of idle cloudlet resources and bring cloud services closer to users. Existing studies have focused primarily on task coordination and resource allocation with strict time constraints, and typically overlooked the potential privacy leakage of users’ participation strategies in MEC. This paper proposes a novel solution to computation offloading and privacy protection in MEC networks using a Multi-agent Deep Deterministic Policy Gradient (MADDPG) framework. Our approach utilizes game theory to encourage computation offloading by modeling the interaction between cloudlets, Data Center Operators (DCOs), and users as a stochastic auction game. We formulate the computation offloading as an auction game with multiple bidders and incomplete information, and use MADDPG to find an optimal solution. To ensure privacy protection, we design a local Differential Privacy (DP) method in the MADDPG algorithm. With an (∈, δ) -DP mechanism, the local DP ensures that the sampled transitions, including the information on users’ actions, states, and corresponding rewards, are protected from exploitation. Analyses corroborate the effectiveness of our approach in satisfying DP and converging to an equilibrium. Simulations demonstrate the approach achieves 126.75% better quality-of-experience than a knapsack-based benchmark, when there are 60 cloudlets and up to 100 users. © 2015 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2389.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
