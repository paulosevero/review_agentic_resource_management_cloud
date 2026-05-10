---
id: paper-0429
title: Digital Twins-based Multi-agent Deep Reinforcement Learning for UAV-assisted Vehicle Edge Computing
authors:
- Hu, Chen
- Qi, Qi
- Zhang, Lei
- Liu, Cong
- Chen, Dezhi
- Liao, Jianxin
- Zhuang, Zirui
- Wang, Jingyu
venue: Proceedings - 2022 IEEE SmartWorld, Ubiquitous Intelligence and Computing, Autonomous and Trusted Vehicles, Scalable Computing and Communications, Digital Twin, Privacy Computing, Metaverse, SmartWorld/UIC/ATC/ScalCom/DigitalTwin/PriComp/Metaverse
  2022
venue_type: conference
year: 2022
doi: 10.1109/SmartWorld-UIC-ATC-ScalCom-DigitalTwin-PriComp-Metaverse56740.2022.00192
url: https://www.scopus.com/pages/publications/85168161609?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1329--1336
keywords:
- Digital Twin
- Multi Agent Deep Q-network
- UAV-assisted
- Vehicle Edge Computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0429 — Digital Twins-based Multi-agent Deep Reinforcement Learning for UAV-assisted Vehicle Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> UAV-assisted vehicle-edge-computing (VEC) has become a viable solution for a new generation of intelligent transportation systems (ITS) and has attracted widespread attention from academia and industry. Compared with fixed ground devices, UAV can provide line-of-sight (LoS) link and has good mobility, which better matches the needs of individual wireless connectivity and high mobility of vehicle. However, the mobility of UAVs leads to dynamic changes in the network topology environment and brings new challenges in the rational path planning of UAVs, which brings new problems for network autonomous decision-making to achieve network resource allocation and load balancing. Therefore, in order to solve above problems, we introduce digital twins-based multi-agent deep Q-network (DT-based MADQN). Digital twin (DT) collects network data and reconstructs the network environment and provides the basis for Deep reinforcement learning (DRL) model training. DRL model provides a network decision-making solution based on real-time network status and empirical data. The simulation results show the effectiveness of the proposed algorithm. Compared to the baseline algorithm, it reduces the average task delay by 16.4% and improves the task completion rate by 97.6%. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0429.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
