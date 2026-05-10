---
id: paper-0114
title: 'Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach'
authors:
- Chen, Xianfu
- Zhao, Zhifeng
- Wu, Celimuge
- Bennis, Mehdi
- Liu, Hang
- Ji, Yusheng
- Zhang, Honggang
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2019
doi: 10.1109/JSAC.2019.2933893
url: https://www.scopus.com/pages/publications/85070673256?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2377--2392
keywords:
- deep reinforcement learning
- Markov decision process
- mobile-edge computing
- Network slicing
- packet scheduling
- radio access networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0114 — Multi-Tenant Cross-Slice Resource Orchestration: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the cellular networks becoming increasingly agile, a major challenge lies in how to support diverse services for mobile users (MUs) over a common physical network infrastructure. Network slicing is a promising solution to tailor the network to match such service requests. This paper considers a system with radio access network (RAN)-only slicing, where the physical infrastructure is split into slices providing computation and communication functionalities. A limited number of channels are auctioned across scheduling slots to MUs of multiple service providers (SPs) (i.e., the tenants). Each SP behaves selfishly to maximize the expected long-term payoff from the competition with other SPs for the orchestration of channels, which provides its MUs with the opportunities to access the computation and communication slices. This problem is modelled as a stochastic game, in which the decision makings of a SP depend on the global network dynamics as well as the joint control policy of all SPs. To approximate the Nash equilibrium solutions, we first construct an abstract stochastic game with the local conjectures of channel auction among the SPs. We then linearly decompose the per-SP Markov decision process to simplify the decision makings at a SP and derive an online scheme based on deep reinforcement learning to approach the optimal abstract control policies. Numerical experiments show significant performance gains from our scheme. © 1983-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0114.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
