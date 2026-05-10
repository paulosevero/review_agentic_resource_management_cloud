---
id: paper-1201
title: STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning
authors:
- Song, Boxuan
- Wang, Fei
venue: Ad Hoc Networks
venue_type: journal
year: 2024
doi: 10.1016/j.adhoc.2023.103370
url: https://www.scopus.com/pages/publications/85178585212?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- DDPG
- MADRL
- Mobile edge computing
- Multi-cell communication systems
- Secure communications
- STAR-RISs
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

# paper-1201 — STAR-RIS-aided secure communications for MEC with delay/energy-constrained QoS using multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The poor propagation environment between user equipments (UEs) and mobile edge computing (MEC) servers may lead to UEs’ high energy consumptions and task delay. Reconfigurable intelligent surface (RIS) can significantly improve the quality of wireless propagation environment by intelligently adjusting the phase-shifts and amplitudes of its reflecting elements. However, the passive or active RISs can only reflect signals, i.e., the transmitters and receivers must be located on the same side of RISs. Simultaneous transmitting and reflecting (STAR) RIS, which can transmit and reflect incident signals simultaneously, has been recognized a promising solution to solve the above problem. For STAR-RIS-aided multi-cell secure communications MEC systems, we first formulate an optimization problem to minimize the sum of weighted delay and energy consumptions of all UEs, by jointly optimizing the phase-shifts and amplitudes of STAR-RISs and system spectrum and computation resource allocations. Second, under the practical coupled phase-shift model of STAR-RIS, we develop a multi-agent deep reinforcement learning (MADRL) based scheme, where the access point (AP) in each cell acts an agent to decide phase-shifts, amplitudes, computation task offloading proportions, etc, for the STAR-RIS and UEs within its coverage based on deep deterministic policy gradient (DDPG), by taking into account interference among multiple cells and possible information leakage of UEs. Finally, we verify and evaluate the performance of the proposed scheme through extensive simulations. The simulation results show that our proposed MADRL-based scheme outperforms the existing benchmarks by employing multiple agents and considering co-channel interference among cells. Moreover, simulation results also show that the performance of our developed scheme can indeed be improved by using STAR-RISs. © 2023 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1201.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
