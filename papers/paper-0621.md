---
id: paper-0621
title: 'Joint Secure Offloading and Resource Allocation for Vehicular Edge Computing Network: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Ju, Ying
- Chen, Yuchao
- Cao, Zhiwei
- Liu, Lei
- Pei, Qingqi
- Xiao, Ming
- Ota, Kaoru
- Dong, Mianxiong
- Leung, Victor C. M.
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2023
doi: 10.1109/TITS.2023.3242997
url: https://www.scopus.com/pages/publications/85149407165?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5555--5569
keywords:
- deep reinforcement learning
- multi-user cooperative offloading
- physical layer security
- spectrum sharing
- Vehicular edge computing
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

# paper-0621 — Joint Secure Offloading and Resource Allocation for Vehicular Edge Computing Network: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The mobile edge computing (MEC) technology can simultaneously provide high-speed computing services for multiple vehicular users (VUs) in vehicular edge computing (VEC) networks. Nevertheless, due to the open feature of the wireless offloading channels and the high mobility of the vehicles, the security and stability of the offloading process would be seriously degraded. In this paper, by utilizing the physical layer security (PLS) technique and spectrum sharing architecture, we propose a deep reinforcement learning based joint secure offloading and resource allocation (SORA) scheme to improve the secrecy performance and resource efficiency of the multi-user VEC networks, where the VU offloading links share the frequency spectrum preoccupied with the vehicle-to-vehicle (V2V) communication links. We use Wyner's wiretap coding scheme to obtain the achievable secrecy rate and guarantee that confidential information cannot be decoded by multiple mobile eavesdroppers. We aim at minimizing the system processing delay while securing the wireless offloading process, by jointly optimizing the transmit power, the frequency spectrum selection and the computation resource allocation. We formulate the optimization problem as a multi-agent collaborative optimal decision problem and solve it with a double deep Q-learning algorithm. Besides, we set a punishment mechanism for the rate degradation to guarantee the communication quality of each V2V link. Simulation results demonstrate that multiple VU agents adopting the SORA scheme can rapidly adapt to the highly dynamic VEC networks and cooperate to improve the system delay performance while increasing the secrecy probability. © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0621.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
