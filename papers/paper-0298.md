---
id: paper-0298
title: Multi-Agent Deep Reinforcement Learning for Computation Offloading and Interference Coordination in Small Cell Networks
authors:
- Huang, Xiaoyan
- Leng, Supeng
- Maharjan, Sabita
- Zhang, Yan
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2021
doi: 10.1109/TVT.2021.3096928
url: https://www.scopus.com/pages/publications/85110794106?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9282--9293
keywords:
- computation offloading
- interference coordination
- Mobile edge computing
- multi-agent deep reinforcement learning
- small cell networks
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

# paper-0298 — Multi-Agent Deep Reinforcement Learning for Computation Offloading and Interference Coordination in Small Cell Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Integrating mobile edge computing (MEC) with small cell networks has been conceived as a promising solution to provide pervasive computing services. However, the interactions among small cells due to inter-cell interference, the diverse application-specific requirements, as well as the highly dynamic wireless environment make it challenging to design an optimal computation offloading scheme. In this paper, we focus on the joint design of computation offloading and interference coordination for edge intelligence empowered small cell networks. To this end, we propose a distributed multi-agent deep reinforcement learning (DRL) scheme with the objective of minimizing the overall energy consumption while ensuring the latency requirements. Specifically, we exploit the collaboration among small cell base station (SBS) agents to adaptively adjust their strategies, considering computation offloading, channel allocation, power control, and computation resource allocation. Further, to decrease the computation complexity and signaling overhead of the training process, we design a federated DRL scheme which only requires SBS agents to share their model parameters instead of local training data. Numerical results demonstrate that our proposed schemes can significantly reduce the energy consumption and effectively guarantee the latency requirements compared with the benchmark schemes.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0298.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
