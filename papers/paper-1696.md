---
id: paper-1696
title: 'Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach'
authors:
- Jia, Difei
- Hu, Fengye
- Ling, Zhuang
- Li, Hailong
- Gao, Yang
venue: IEEE Transactions on Communications
venue_type: journal
year: 2025
doi: 10.1109/TCOMM.2025.3577638
url: https://www.scopus.com/pages/publications/105008030172?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11528--11544
keywords:
- computation offloading
- deep reinforcement learning (DRL)
- High-speed railway (HSR)
- resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1696 — Computation Offloading and Resource Allocation in Symbiotic Radio-Assisted HSR Networks: A Fingerprint-Based Distributed D3QN Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates a symbiotic radio (SR)-assisted mobile edge computing (MEC) network for railway Internet of Things (RIoT) services, where IoT devices parasitize in a train-ground primary network for passively modulating their computation tasks over computation offloading by associating a mobile relay (MR) on the high-speed railway (HSR). The multi-antenna base station (BS) integrated with the MEC server recovers computation task data from MRs and IoT devices through joint decoding. With the objective of maximizing the total computation efficiency (CE) of all MRs while satisfying the computation requirements of IoT devices, we formulate a computation offloading and resource allocation problem that jointly optimizes the association strategy between MRs and IoT devices, the received beamforming of the BS, the transmission power and computation frequency of MRs. However, since the rapid variation of channel conditions in HSRs poses difficulties to centralized optimization methods in terms of both accurate model acquisition and computation overhead, we utilize a model-free deep reinforcement learning (DRL) approach to propose a fingerprint-based distributed dueling double deep Q-network (FD<sup>4</sup>QN)-based computation offloading and resource allocation scheme to solve the above problem. In particular, this scheme describes the original problem as a partially observable Markov decision process (POMDP), and then incorporates low-dimensional fingerprint markers in each computing agent to stabilize the experience replay mechanism in a multi-agent environment, thereby enhancing training robustness. Moreover, each agent makes a decision for each MR at each time frame by using a dueling double deep Q-network (D3QN) framework based on the local observation state. Simulation results show that the proposed scheme achieves superior performance compared to other benchmark schemes. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1696.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
