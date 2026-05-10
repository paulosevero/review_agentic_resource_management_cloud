---
id: paper-1097
title: A Cascaded Multi-Agent Reinforcement Learning-Based Resource Allocation for Cellular-V2X Vehicular Platooning Networks
authors:
- Narayanasamy, Iswarya
- Rajamanickam, Venkateswari
venue: Sensors
venue_type: journal
year: 2024
doi: 10.3390/s24175658
url: https://www.scopus.com/pages/publications/85203868969?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- Age of Information
- Multi-Access Edge Computing
- Multi-Agent Reinforcement Learning
- radio resource management
- vehicle platooning
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

# paper-1097 — A Cascaded Multi-Agent Reinforcement Learning-Based Resource Allocation for Cellular-V2X Vehicular Platooning Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The platooning of cars and trucks is a pertinent approach for autonomous driving due to the effective utilization of roadways. The decreased gas consumption levels are an added merit owing to sustainability. Conventional platooning depended on Dedicated Short-Range Communication (DSRC)-based vehicle-to-vehicle communications. The computations were executed by the platoon members with their constrained capabilities. The advent of 5G has favored Intelligent Transportation Systems (ITS) to adopt Multi-access Edge Computing (MEC) in platooning paradigms by offloading the computational tasks to the edge server. In this research, vital parameters in vehicular platooning systems, viz. latency-sensitive radio resource management schemes, and Age of Information (AoI) are investigated. In addition, the delivery rates of Cooperative Awareness Messages (CAM) that ensure expeditious reception of safety-critical messages at the roadside units (RSU) are also examined. However, for latency-sensitive applications like vehicular networks, it is essential to address multiple and correlated objectives. To solve such objectives effectively and simultaneously, the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) framework necessitates a better and more sophisticated model to enhance its ability. In this paper, a novel Cascaded MADDPG framework, CMADDPG, is proposed to train cascaded target critics, which aims at achieving expected rewards through the collaborative conduct of agents. The estimation bias phenomenon, which hinders a system’s overall performance, is vividly circumvented in this cascaded algorithm. Eventually, experimental analysis also demonstrates the potential of the proposed algorithm by evaluating the convergence factor, which stabilizes quickly with minimum distortions, and reliable CAM message dissemination with (Formula presented.) probability. The average AoI quantity is maintained within the 5–10 ms range, guaranteeing better QoS. This technique has proven its robustness in decentralized resource allocation against channel uncertainties caused by higher mobility in the environment. Most importantly, the performance of the proposed algorithm remains unaffected by increasing platoon size and leading channel uncertainties. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1097.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
