---
id: paper-1369
title: Deep Reinforcement Learning for Delay Minimization in Slotted ALOHA Terahertz MEC Networks
authors:
- Ahmadi, Arian
- Shirazi, Mojtaba
venue: IEEE Asia Pacific Conference on Wireless and Mobile, APWiMob
venue_type: conference
year: 2025
doi: 10.1109/APWiMob67231.2025.11269170
url: https://www.scopus.com/pages/publications/105032643521?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 148--153
keywords:
- Deep learning
- Mobile telecommunication systems
- Multi agent systems
- Next generation networks
- Optimal systems
- Optimization
- Random errors
- Signal interference
- Delay minimization
- Delivery delay
- Edge computing
- High data rate
- Multiaccess
- Power allocations
- Random multiple access
- Reinforcement learnings
- Tera Hertz
- Terahertz band
- Economic and social effects
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

# paper-1369 — Deep Reinforcement Learning for Delay Minimization in Slotted ALOHA Terahertz MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —Communication in terahertz bands is a promising solution to achieve extremely high data rates in next-generation wireless networks. Random multiple access is now considered a key technology for 6G communication scenarios due to its simplicity and flexibility. Random multiple access slotted ALOHA has recently attracted much attention. However, a significant drawback of slotted ALOHA is the exceedingly high probability of packet collisions when large number of devices attempt to access the base station simultaneously. This leads to system performance degradation. In this work, we investigate the combined offloading decisions, blocklength optimization, computation, and power allocation in a multi-access edge computing (MEC) network operating with finite blocklength (FBL) codes where slotted ALOHA is employed to manage the random access process. In particular, first we derive the closed-form expression of signal-to-interference plus noise ratio threshold for short packets and analyze the trade-off between transmission errors caused by FBL, collision errors affected by FBL and the resulting delivery delay. Then, we propose an optimal system design aims to minimize system delivery delay by selecting the ideal blocklength and the optimal computation and power allocation using multi-agent deep reinforcement learning (DRL). Via numerical analysis, we validate the analytical model and investigate the system performance. © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1369.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
