---
id: paper-2375
title: Joint node selection and task offloading via evolutionary game and MATD3 in UAV-assisted MEC networks
authors:
- Yao, Zheng
- Chang, Puqing
- Khalil, Fahad Khan
- Duan, Changhao
venue: Journal of King Saud University - Computer and Information Sciences
venue_type: journal
year: 2025
doi: 10.1007/s44443-025-00248-3
url: https://www.scopus.com/pages/publications/105017075340?origin=resultslist
publisher: Springer International Publishing
pages: ''
keywords:
- Evolutionary game theory
- Multi-agent reinforcement learning
- Node selection
- Resource allocation
- Task offloading
- UAV-assisted MEC
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

# paper-2375 — Joint node selection and task offloading via evolutionary game and MATD3 in UAV-assisted MEC networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of local congestion and imbalanced resource allocation in UAV-assisted air-ground integrated networks, this study constructs a three-layer network architecture comprising ground edge servers, UAVs, and users. A two-stage optimization framework is proposed, incorporating the node selection and task offloading strategies. First, to mitigate the computational resource limitations arising from the dynamic distribution of multiple users, an evolutionary game-based node selection algorithm is developed to achieve effective dynamic load balancing across offloading nodes. Subsequently, the joint task offloading and power allocation problem is formulated as a Markov decision process, and a reinforcement learning algorithm based on MATD3 is designed to attain the joint optimal control of user offloading ratios and transmission power levels. Simulation results demonstrate that the proposed framework reduces total delay and energy consumption by approximately 33.4% and 29.4%, respectively, outperforming the existing strategies. The framework demonstrates superior scalability and energy efficiency in task-intensive scenarios. © The Author(s) 2025.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2375.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
