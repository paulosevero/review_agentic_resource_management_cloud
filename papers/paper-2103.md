---
id: paper-2103
title: Delay Optimized VNF Placement in 5G-Enabled Industry 4.0 Networks Using DRL With Wireless Reliability and Cyberattack Resilience
authors:
- Saqib, Nauman
- Abdullah, Nor Fadzilah
- Abu-Samah, Asma
- Nordin, Rosdiadee
venue: IEEE Sensors Journal
venue_type: journal
year: 2025
doi: 10.1109/JSEN.2025.3604001
url: https://www.scopus.com/pages/publications/105015066279?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 39064--39081
keywords:
- Adversarial training
- cybersecurity
- deep reinforcement learning (DRL)
- fifth generation (5G)
- Industry 4.0
- ultrareliable low-latency communication (URLLC)
- virtual network function (VNF)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2103 — Delay Optimized VNF Placement in 5G-Enabled Industry 4.0 Networks Using DRL With Wireless Reliability and Cyberattack Resilience

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing reliance on fifth-generation (5G) networks in Industry 4.0 has introduced significant challenges in virtual network function (VNF) placement, where low-latency communication and system resilience are critical. This study proposes a deep reinforcement learning (DRL)-based framework for optimizing VNF placement in 5G-enabled industrial environments to minimize delays while ensuring wireless connection reliability and resilience against cyberattacks. By integrating edge computing and network virtualization, the framework dynamically adapts to varying network traffic, mobility patterns, and wireless channel conditions. A custom simulation environment is designed to model industrial dynamics, including sensor traffic, automated guided vehicle (AGV) mobility, and degraded gNodeB availability to simulate cyberattacks. The study benchmarks Double deep Q network (DQN) and proximal policy optimization (PPO) against heuristic baselines, demonstrating their adaptability and scalability. Additionally, the robustness of the proposed framework is evaluated under simulated cyberattacks affecting gNode availability, highlighting its resilience in maintaining low-latency communication. The simulation results show that the trained Double DQN and PPO agents achieved a mean absolute percentage error within 3.58% and 4.22% of the established baseline, demonstrating their ability to approximate optimal VNF placement decisions. Furthermore, the adversarially trained PPO agent achieved a 24.3% lower mean delay in a 10% gNodeB availability scenario compared to the normally trained agent, demonstrating enhanced robustness under adversarial conditions. This research highlights the capability of DRL for intelligent and adaptive VNF placement, contributing to the development of robust and efficient next-generation industrial networks. © 2001-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2103.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
