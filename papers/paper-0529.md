---
id: paper-0529
title: 5G Multi-RAT URLLC and eMBB Dynamic Task Offloading With MEC Resource Allocation Using Distributed Deep Reinforcement Learning
authors:
- Yun, Jusik
- Goh, Yunyeong
- Yoo, Wonsuk
- Chung, Jong-Moon
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3177425
url: https://www.scopus.com/pages/publications/85130827435?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20733--20749
keywords:
- 5G
- deep reinforcement learning (DRL)
- distributed learning
- enhanced mobile broadband (eMBB)
- Internet of Things (IoT)
- multiaccess edge computing (MEC)
- multiradio access technology (RAT)
- offloading
- resource allocation
- ultrareliability low-latency communication (URLLC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0529 — 5G Multi-RAT URLLC and eMBB Dynamic Task Offloading With MEC Resource Allocation Using Distributed Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, a deep reinforcement learning (DRL) control scheme is proposed to satisfy the strict Quality-of-Service (QoS) requirements of ultrareliability low-latency communication (URLLC) and enhanced mobile broadband (eMBB) using 5G multiple radio access technology (RAT)-based partial offloading and multiaccess edge-computing (MEC) resource allocation. In the proposed scheme, the user equipment (UE) makes optimal offloading decisions while the MEC server dynamically adjusts the server resources based on offloading requests from multiple UEs using DRL technology. The aim of the proposed scheme is to minimize the energy consumption of the UEs while maximizing the system utility (SU) performance, which is composed of the spectral efficiency (SE) and offloading success rate (OSR) of the MEC server. In addition, multiagent distributed learning technology and best experience push (BEP) techniques are used to enhance the learning efficiency of the DRL framework. The simulation result shows that the proposed scheme provides an improved SU and energy consumption performance compared to the benchmark offloading schemes. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0529.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
