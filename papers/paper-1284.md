---
id: paper-1284
title: Collaborative Multi-Agent Deep Reinforcement Learning for Energy-Efficient Resource Allocation in Heterogeneous Mobile Edge Computing Networks
authors:
- Xiao, Yang
- Song, Yuqian
- Liu, Jun
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2023.3335597
url: https://www.scopus.com/pages/publications/85183807453?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6653--6668
keywords:
- energy efficiency
- Heterogeneous mobile edge computing (Het-MEC) network
- multi-agent deep reinforcement learning (MADRL)
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

# paper-1284 — Collaborative Multi-Agent Deep Reinforcement Learning for Energy-Efficient Resource Allocation in Heterogeneous Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is an enabling technology for next-generation network architectures to deliver more diversified communication services and meet more demanding quality-of-service (QoS) requirements. However, owing to the growing scale and heterogeneity of the networks, energy-efficient resource allocation in heterogeneous MEC (Het-MEC) networks faces great challenges. As an emerging research area, multi-agent deep reinforcement learning (MADRL) is expected to realize autonomous resource allocation in Het-MEC networks by learning from trial and error. Nevertheless, existing MADRL-based solutions are usually not applicable to practical scenarios by the limitations of centralized control schemes or massive signaling overhead. To address the issue, we first formulate the energy-efficient resource allocation problem in Het-MEC networks as a time-variant mixed-integer nonlinear programming (MINLP) problem. Then, we propose a fully decentralized collaborative MADRL-based algorithm featuring the multi-actor shared-critic (MASC) architecture and the regional training distributed execution (RTDE) framework, which effectively stabilizes model training and reduces information exchange, respectively. Finally, we conduct extensive simulations to evaluate the performance of the proposed algorithm. Numerical results demonstrate that the proposed algorithm comprehensively outperforms several mainstream baseline methods in terms of convergence performance, scalability, and robustness.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1284.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
