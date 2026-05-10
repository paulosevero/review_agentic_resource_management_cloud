---
id: paper-0783
title: Energy Efficient IRS Assisted NOMA Aided Mobile Edge Computing via Heterogeneous Multi-Agent Reinforcement Learning
authors:
- Yu, Jiadong
- Li, Yang
- Liu, Xiaolan
- Sun, Bo
- Wu, Yuan
- Tsang, Danny H.K.
venue: IEEE International Conference on Communications
venue_type: conference
year: 2023
doi: 10.1109/ICC45041.2023.10279340
url: https://www.scopus.com/pages/publications/85178264650?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5352--5357
keywords:
- Benchmarking
- Computation offloading
- Lyapunov functions
- Mobile edge computing
- Multi agent systems
- Reinforcement learning
- Stochastic systems
- Computing system
- Energy efficient
- Mixed integer
- Multi agent
- Multi-agent reinforcement learning
- Multiple access
- Non-orthogonal
- Queue stability
- Reflecting surface
- Spectral efficiencies
- Energy efficiency
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

# paper-0783 — Energy Efficient IRS Assisted NOMA Aided Mobile Edge Computing via Heterogeneous Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Non-orthogonal multiple access (NOMA)-aided mobile edge computing (MEC) system can enhance the spectral-efficiency with massive tasks offloading. However, with more dynamic devices and the uncontrollable stochastic channel environment, it is even desirable to deploy appealing technique, i.e., intelligent reflecting surfaces (IRS), in the MEC system to flexibly adjust the communication environment and improve the system energy-efficiency. In this paper, we investigate the joint offloading, communication and computation resource allocation for IRS-assisted NOMA-aided MEC system. We firstly formulate a mixed integer energy-efficiency maximization problem with the system queue stability constraint. We then propose a Het-erogeneous Multi-agent Lyapunov-function-based Mixed Integer Deep Deterministic Policy Gradient (HMA-LMIDDPG) algorithm which is based on the multi-agent reinforcement learning (MARL) framework with homogeneous edge devices (EDs) and heterogeneous base station (BS) as heterogeneous multi-agent. Numerical results show that our proposed algorithms can achieve superior energy-efficiency performance to the benchmark algorithms while maintaining the queue stability.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0783.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
