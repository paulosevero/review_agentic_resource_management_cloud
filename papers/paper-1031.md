---
id: paper-1031
title: Multi-agent reinforcement learning based computation offloading and resource allocation for LEO Satellite edge computing networks
authors:
- Li, Hai
- Yu, Jinyang
- Cao, Lili
- Zhang, Qin
- Song, Zhengyu
- Hou, Shujuan
venue: Computer Communications
venue_type: journal
year: 2024
doi: 10.1016/j.comcom.2024.05.008
url: https://www.scopus.com/pages/publications/85192895281?origin=resultslist
publisher: Elsevier B.V.
pages: 268--276
keywords:
- Computation offloading
- LEO satellite
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Resource allocation
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

# paper-1031 — Multi-agent reinforcement learning based computation offloading and resource allocation for LEO Satellite edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the limitations caused by geographical conditions and economic requirements, it is difficult to provide computing services by terrestrial networks for mobile terminals in remote areas. To address this issue, mobile edge computing (MEC) servers can be deployed in the low earth orbit (LEO) satellites to act as a complement and accommodate the unserved terminals. However, offloading computing tasks to servers in satellites may increase the energy consumption of ground terminals. Considering the limited battery capacity of ground terminals, how to perform the computation offloading and resource allocation are key challenges in the LEO satellite edge computing networks. Therefore, in this paper, we investigate the energy minimization problem for LEO satellite edge computing networks, where a multi-agent deep reinforcement learning algorithm with global rewards is proposed to optimize the transmit power, CPU frequency, bit allocation, offloading decision and bandwidth allocation via a decentralized method. Simulation results show that our proposed algorithm can converge faster. Most importantly, compared with the random algorithm, the proximal policy optimization (PPO) algorithm, and the deep deterministic policy gradient (DDPG) algorithm, the ground terminals’ energy consumption can be effectively reduced by our proposed algorithm. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1031.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
