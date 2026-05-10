---
id: paper-0547
title: Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture
authors:
- Akbari, Mohammad
- Syed, Aisha
- Kennedy, W. Sean
- Erol-Kantarci, Melike
venue: IEEE Transactions on Machine Learning in Communications and Networking
venue_type: journal
year: 2023
doi: 10.1109/TMLCN.2023.3311749
url: https://www.scopus.com/pages/publications/105027867571?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers
pages: 277--295
keywords:
- age of information
- constraint MDP
- federated reinforcement learning
- Internet of Things
- network function virtualization
- UAV-Aided mobile edge computing (UAV-Aided MEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0547 — Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For a wide range of smart agriculture use cases, the prospects of utilizing the Internet of Things (IoT) are immense. Many IoT devices can be deployed for precision farming, soil management, automated irritation, information gathering, or performing some local processing to provide various services. Due to the computational capacity limitation of IoT devices and their limited power, UAV-Aided mobile-edge computing (MEC) is proposed to provide IoT nodes with additional resources by hosting their computation functions and making smart agriculture use cases more operational. On the other hand, from the implementation viewpoint, Network Function Virtualization (NFV) is an emerging approach recently proposed for flexible management of such computation functions in UAVs and MEC-server. However, efficient orchestration of the virtualized functions is a challenge. In this paper, we consider a decentralized UAV-Aided MEC system in which the NFV-enabled processing nodes manage the computational tasks. To be more specific, we consider the smart agriculture use cases that need live streaming/analysis, such as surveillance or environmental monitoring. In such a network, we propose a method for orchestrating the NFVs efficiently, while the network energy consumption throughout the network is minimized. This problem becomes even more crucial when considering a strict condition on the instantaneous AoI values. Therefore, the problem is first formulated as a Decentralized Constrained Multi-Agent Markov Decision Process (Dec-CMMDP). As the formulated problem is NEXP, in the next step, we exploit some structural features of the considered network and introduce the concept of symmetry to simplify the problem. Then, inspired by Augmented Lagrangian dual optimization, a novel decentralized, federated learning-based solution is proposed to solve the problem. Simulation results show the effectiveness of the proposed approach in minimizing the total network energy consumption, minimizing the average AoI, and satisfying the strict condition of AoI < 100 msec for supporting real-Time applications in our network parameter settings.  © 2023 CCBY.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0547.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
