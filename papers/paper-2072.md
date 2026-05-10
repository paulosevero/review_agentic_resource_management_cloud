---
id: paper-2072
title: Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments
authors:
- Rasool, Hussein Ali
- Abdul-Sadah, Ali Muhssen
- Taha, Mohand S.
- Najim, Ali Hamzah
- Said, Maizatul Alice Meor
venue: International Journal of Intelligent Engineering and Systems
venue_type: journal
year: 2025
doi: 10.22266/ijies2025.1130.62
url: https://www.scopus.com/pages/publications/105019569945?origin=resultslist
publisher: Intelligent Network and Systems Society
pages: 987--999
keywords:
- Adaptive traffic management
- City traffic
- Intelligent signals
- Learning agents
- Real-time response
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2072 — Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growth of urban mobility and networked vehicles has expedited the need for smart traffic management systems that can operate optimally in the next-generation wireless environment. This paper introduces an innovative Multi-Agent Reinforcement Learning (MARL) system for real-time traffic signal control in 6G-enabled Vehicular Ad Hoc Networks (VANETs). In contrast to conventional approaches that optimize solely traffic-related metrics like delay or queue length, the presented system adopts traffic-oriented and communication-aware metrics such as average waiting time, congestion index, packet delivery ratio, and bandwidth utilization under a common reward framework. Dynamic scalarization allows MARL agents to adaptively weigh these objectives based on real-time traffic and network conditions. The proposed framework was validated using four datasets: the Vehicular Network State Dataset (Kaggle), Secure VANET Vehicle Dataset, VANET Real-Time Route Optimization Dataset, and 5G-VANET MEC Dataset. All traffic signals are designed as independent MARL agents, learning signal phases based on local observations and fast inter-agent communication via 6G links. The innovation is the simultaneous optimization of vehicle flow and network-level performance for end-to-end real-time coordination and scalability in highly dense urban VANET environments. Compared to standard fixed-time control algorithms, MA2C, DQN-based controllers on the same dataset, the suggested framework provides an 32.6% decrease in mean waiting time, a noteworthy reduction in congestion, a 21.4% increase in packet delivery ratio, and a 27.8% increase in bandwidth efficiency. The results confirm the framework’s robustness and generalizability across diverse VANET scenarios. © This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. License details: https://creativecommons.org/licenses/by-sa/4.0/

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2072.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
