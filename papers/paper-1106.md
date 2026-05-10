---
id: paper-1106
title: Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services
authors:
- Ning, Zhaolong
- Yang, Yuxuan
- Wang, Xiaojie
- Song, Qingyang
- Guo, Lei
- Jamalipour, Abbas
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2023.3312276
url: https://www.scopus.com/pages/publications/85171532752?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5818--5834
keywords:
- game theory
- Multi-access edge computing
- multi-agent DRL
- UAV-assisted communications
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1106 — Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the increasing computational demand of real-time mobile applications, Unmanned Aerial Vehicle (UAV) assisted Multi-access Edge Computing (MEC) has been envisioned as a promising paradigm for pushing computational resources to network edges and constructing high-throughput line-of-sight links for ground users. Most exsiting studies consider simplified scenarios, such as a single UAV, Service Provider (SP) or service type, and centralized UAV trajectory control. In order to be more in line with real-world cases, we intend to achieve distributed trajectory control of multiple UAVs in UAV-assisted MEC networks with multiple SPs providing differentiated services. Our objective is to minimize the short-term computational costs of ground users and the long-term computational cost of UAVs, simultaneously based on incomplete information. We first solve the formulated problem by reaching the Nash Equilibrium (NE) of the game among SPs based on complete information. We further formulate a Markov game model and propose a Deep Reinforcement Learning (DRL)-based UAV trajectory optimization algorithm, where only local observations of each UAV are required for each SP's flying action execution. Theoretical analysis and performance evaluation demonstrate the convergence, efficiency, scalability, and robustness of our algorithm compared with other representative algorithms. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1106.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
