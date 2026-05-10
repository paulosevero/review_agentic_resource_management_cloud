---
id: paper-0801
title: Computation Offloading and Beamforming Optimization for Energy Minimization in Wireless-Powered IRS-Assisted MEC
authors:
- Zhao, Songhan
- Liu, Yue
- Gong, Shimin
- Gu, Bo
- Fan, Rongfei
- Lyu, Bin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3265011
url: https://www.scopus.com/pages/publications/85153394082?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19466--19478
keywords:
- Deep reinforcement learning (DRL)
- intelligent reflecting surface (IRS)
- mobile-edge computing (MEC)
- symbiotic radio (SR)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0801 — Computation Offloading and Beamforming Optimization for Energy Minimization in Wireless-Powered IRS-Assisted MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent reflecting surface (IRS) has been recently exploited as a symbiotic radio (SR) technology to improve energy and spectral efficiencies in wireless systems. In this article, we consider a symbiotic IRS-assisted mobile-edge computing (MEC) system that allows edge users to first harvest RF power from a hybrid access point (HAP) and then offload its computational workload to the MEC server associated with the HAP. We aim to minimize the HAP's energy consumption by jointly optimizing the users' offloading schemes, the HAP's active beamforming, and the IRS's passive beamforming strategies. We propose an optimization-driven hierarchical deep deterministic policy gradient (OH-DDPG) framework to decompose the energy minimization problem into the optimization and the learning subproblems, respectively. The outer loop DDPG learning method adapts the IRS's passive beamforming strategy, while the inner loop optimization deals with the other control variables with reduced dimensionality. Moreover, to improve the learning efficiency, we extend OH-DDPG to the multiagent scenario. In particular, the HAP first estimates the users' offloading strategy by the inner-loop optimization and shares it with all user agents. Then, each user agent refines its offloading decision using the DDPG algorithm independently. This can avoid signaling overhead among users and improve the multiuser learning efficiency. Simulation results show that the proposed OH-DDPG and the multiuser extension can achieve significant performance gains compared to the conventional model-free learning algorithms.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0801.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
