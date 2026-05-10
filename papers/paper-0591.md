---
id: paper-0591
title: Game-Combined Multi-Agent DRL for Tasks Offloading in Wireless Powered MEC Networks
authors:
- Gao, Ang
- Zhang, Shuai
- Hu, Yansu
- Liang, Wei
- Ng, Soon Xin
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3250274
url: https://www.scopus.com/pages/publications/85149392501?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9131--9144
keywords:
- backscatter communication
- game
- multi-agent DRL
- tasks offloading
- Wireless power transfer
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

# paper-0591 — Game-Combined Multi-Agent DRL for Tasks Offloading in Wireless Powered MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wireless powered mobile edge computing (MEC) networks have been envisaged as a promising technology to ensure the ultra-low-power requirement and enhance the continuous work capacity of wireless devices (WDs). However, when multiple WDs coexist in the network, it is non-trivial to minimize the total tasks delay since the optimization variables are intrinsically coupled. Even more, channels are dynamically varying from time to time and the tasks are unpredictable, which aggravates the difficulty to obtain the closed-form solution. This paper considers a challenging hybrid tasks offloading scenario, where offloading tasks can be partially executed locally and remotely in parallel, and each WD is endowed to take both the active RF-transmission and passive backscatter communication (BackCom) for remote tasks offloading. Furthermore, a game-combined multi-agent deep deterministic policy gradient (MADDPG) algorithm is proposed to minimize the total tasks delay with the fairness consideration of multiple WDs, i.e., potential game for offloading decision and MADDPG for time scheduling and harvested energy splitting. Equipped with the feature of 'centralized training with decentralized execution', once well trained, each agent in MADDPG can figure out the proper time scheduling and harvested energy splitting independently without sharing information with others. Besides the unilateral contention among WDs for the offloading decision by potential game, a fully decentralized framework is finally designed for the proposed algorithm. Numerical results demonstrate that the game-combined MADDPG algorithm can achieve the near-optimal performance compared with existing centralized approaches, and reduce the convergence time compared with other no-game learning approaches. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0591.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
