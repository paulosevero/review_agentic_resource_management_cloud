---
id: paper-0461
title: 'MEC-Based Dynamic Controller Placement in SD-IoV: A Deep Reinforcement Learning Approach'
authors:
- Li, Bo
- Deng, Xiaoheng
- Chen, Xuechen
- Deng, Yiqin
- Yin, Jian
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2022
doi: 10.1109/TVT.2022.3182048
url: https://www.scopus.com/pages/publications/85139241697?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10044--10058
keywords:
- controller placement
- Internet of vehicles (IoV)
- mobile edge computing (MEC)
- multi-agent deep Q-learning networks (MADQN)
- software defined network (SDN)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0461 — MEC-Based Dynamic Controller Placement in SD-IoV: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The flow fluctuations in the highly dynamic Internet of Vehicles (IoV) make the IoV difficult to provide reliable and scalable wireless network services for the emerging applications in the 5 G and beyond era. The software-defined networks (SDN) could feasibly manage and optimize the network according to the network load. Controller placement is a critical problem in SDN to achieve its robustness and flexibility with the changes of network status. Motivated by the advantages of SDN and Mobile-edge computing (MEC), this paper aims at enhancing the performance of IoV with the assistance of these two. Specifically, we consider a three-layer hierarchical SDN control plane for the IoV, where the SDN controllers are placed at the edge of networks. Under this framework, we investigate a multi-objective optimization problem on controller placement problem including delay, load balancing, and path reliability. To efficiently solve the formulated NP-hard problems, we develop an algorithm based on multi-agent deep Q-learning networks (MADQN) because of its advantages for large-scale combinatorial optimization. At last, we use multi-process technology to accelerate the operation of the algorithm, so as to complete the algorithm iteration faster. Numerical results show that the proposed methods achieve better performances than three baselines. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0461.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
