---
id: paper-0756
title: Multi-agent DRL for joint completion delay and energy consumption with queuing theory in MEC-based IIoT
authors:
- Wu, Guowen
- Xu, Zhiqi
- Zhang, Hong
- Shen, Shigen
- Yu, Shui
venue: Journal of Parallel and Distributed Computing
venue_type: journal
year: 2023
doi: 10.1016/j.jpdc.2023.02.008
url: https://www.scopus.com/pages/publications/85149278228?origin=resultslist
publisher: Academic Press Inc.
pages: 80--94
keywords:
- Industrial Internet of things
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Queuing theory
- Task offloading
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

# paper-0756 — Multi-agent DRL for joint completion delay and energy consumption with queuing theory in MEC-based IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the Industrial Internet of Things (IIoT), there exist numerous sensor devices with weak computing power and small energy storage. To meet the real-time and big data computing requirements of industrial production, EIIoT (Edge computing-based IIoT) that combines mobile edge computing with IIoT has emerged. It is necessary to offload computing tasks to nearby edge servers for data storage and processing in EIIoT, thus inevitably causing the edge servers to overload. To this end, we propose a jointly constrained optimization model of delay and energy consumption based on queuing theory; this model can effectively solve the task offloading problem in EIIoT. Subsequently, to satisfy the unique offloading requirements of EIIoT, we improve the MAPPO (multi agent proximal policy optimization) algorithm structure to form a lightweight optimal task offloading algorithm called Multi-Agent Deep Reinforcement Learning based on Queuing theory (MAQDRL), which is more suitable for EIIoT. In the algorithm, we systematically integrate queuing theory and use Multi-Agent Deep Reinforcement Learning (MADRL) to obtain the optimal offloading strategy in dynamic and random multiuser offloading environments. We also improve the structure of neural networks of MADRL by analyzing the structural characteristics of the input data. As a result, the algorithm that we proposed exhibits good convergence and exceptional performance in terms of the task arrival rate, bandwidth, energy consumption, latency and other indicators. The simulation results indicate that compared with other classical algorithms, MAQDRL is effective for solving the EIIoT offloading problem. © 2023 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0756.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
