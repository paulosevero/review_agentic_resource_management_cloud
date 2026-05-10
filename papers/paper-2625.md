---
id: paper-2625
title: NOMA and Hybrid Beamforming Aided Secure Computation Offloading for mmWave VEC Networks With Multi-Agent DRL
authors:
- Ju, Ying
- Cao, Zhiwei
- Li, Mingdong
- Liu, Lei
- Pei, Qingqi
- Dong, Mianxiong
- Mumtaz, Shahid
- Guizani, Mohsen
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2026.3662303
url: https://www.scopus.com/pages/publications/105029971911?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6089--6103
keywords:
- deep reinforcement learning
- Millimeter Wave
- non-orthogonal multiple access (NOMA)
- physical layer security
- secure offloading
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

# paper-2625 — NOMA and Hybrid Beamforming Aided Secure Computation Offloading for mmWave VEC Networks With Multi-Agent DRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) meets the requirements of various delay-sensitive applications by providing high-speed computing services to a large number of user vehicles simultaneously. Nevertheless, the inherent open feature of wireless channels and the constraints of limited spectrum resources present significant challenges to achieving both secure offloading and high offloading rate simultaneously. Millimeter wave (mmWave) can provide user vehicles with abundant spectrum resources, but its short wavelength causes high path loss. In this paper, we utilize hybrid beamforming and non-orthogonal multiple access (NOMA) technologies to improve the offloading rate of user vehicles and to interfere with eavesdroppers, thus improving the security of the offloading process in mmWave vehicular edge computing (VEC) networks. We first use the K-means algorithm to cluster user vehicles. Then, we minimize the system delay by jointly optimizing the analog beamforming matrix, the user vehicle transmit power and the allocation ratio of the MEC server computation resource while ensuring the security of the offloading process. The above optimization problem is formulated as a Markov decision process (MDP) and a twin Delayed Deep Deterministic Policy Gradient (TD3)-Dueling Double Deep Q Network (D3QN) based multi-agent secure computation offloading scheme is proposed to solve the MDP problem. Simulation results demonstrate that the TD3-D3QN based multi-agent scheme is able to adapt to highly dynamic VEC networks when guaranteeing the security of the offloading process and low system delay.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2625.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
