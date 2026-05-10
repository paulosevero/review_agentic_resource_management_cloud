---
id: paper-1910
title: 'Blockchain-Enabled Secure Offloading for VEC: A Multi-Agent Reinforcement Learning Approach'
authors:
- Lu, Xiaozhen
- Xiao, Liang
- Xiao, Yilin
- Xiong, Zehui
- Liu, Zhe
- Zhang, Yanyong
- Zhuang, Weihua
venue: IEEE Transactions on Dependable and Secure Computing
venue_type: journal
year: 2025
doi: 10.1109/TDSC.2024.3523561
url: https://www.scopus.com/pages/publications/85213428243?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2978--2995
keywords:
- multi-agent reinforcement learning
- safe exploration
- Secure offloading
- smart contract
- vehicular edge computing
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

# paper-1910 — Blockchain-Enabled Secure Offloading for VEC: A Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) helps improve the task computational performance of vehicles on roads but has difficulty in defending against eavesdropping and selfish attacks simultaneously. In this paper, we design a reputation-based smart contract with blockchain and propose a multi-agent reinforcement learning (RL) based secure offloading scheme for VEC against both eavesdropping and selfish attacks. This scheme has a three-level hierarchical structure for each vehicle and uses the reputations obtained from the blockchain as the basis to optimize the edge node selection, offloading ratio, and power allocation, which aims to reduce the task computational latency, the vehicle energy consumption and eavesdropping rate. By using a punishment function based on the constraints, this scheme avoids exploring dangerous policies that can cause task failure or severe data leakage. A multi-agent deep RL-based secure offloading scheme is proposed for vehicles with sufficient resources, which evaluates the long-term risk rather than the punishment function to further improve the secure offloading performance. The regret bound is analyzedand the cumulative reward upper bound is provided. Simulation results verify the effectiveness of our schemes as compared with the benchmark. © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1910.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
