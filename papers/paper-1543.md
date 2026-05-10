---
id: paper-1543
title: Intelligent Optimizations for UAV, Digital Twin, and ISCC Enabled Intelligent Transportation Systems
authors:
- Du, Jianbo
- Wang, Jiaxuan
- Li, Shulei
- Liu, Lei
- Chu, Xiaoli
- Chen, Xianfu
- Dong, Mianxiong
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3619390
url: https://www.scopus.com/pages/publications/105020441032?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 23069--23083
keywords:
- deep reinforcement learning
- digital twin
- intelligent transportation systems
- ISCC
- multi-access edge computing
- UAV
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1543 — Intelligent Optimizations for UAV, Digital Twin, and ISCC Enabled Intelligent Transportation Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The evolution of intelligent transportation systems necessitate the integration of advanced technologies to address challenges in data processing, real-time decision-making, and network coverage. In this paper, we present a novel intelligent transportation system architecture that synergizes Unmanned Aerial Vehicles (UAVs), Digital Twins (DTs), and an Integrated Sensing, Communication, and Computation (ISCC) framework. In this system, UAVs equipped with edge computing capabilities collaborate with the ground-based cloud center to process data collected by perception devices (PDs). Each UAV and PD is mirrored by a Digital Twin (DT) at the base station, enabling real-time monitoring and predictive analytics. We intend to maximize the network lifetime and minimize the economic overhead, which is achieved through the joint optimization of the association policies of UEs, input data caching decisions, UAVs’ flight trajectory and speed, task processing mode selection and data unload proportion allocation under joint processing. To tackle the inherent challenges of nonlinearity, dynamic network conditions, and heterogeneous data sources, the problem is modeled as a Markov Decision Process (MDP) and solved using an enhanced Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm, adapted to handle both continuous and discrete action spaces. The experimental results show that compared to the baseline algorithm, this approach not only exhibits faster convergence but also achieves outstanding performance in maximizing system utility for intelligent transportation systems. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1543.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
