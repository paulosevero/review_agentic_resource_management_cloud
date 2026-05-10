---
id: paper-0994
title: Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance
authors:
- Kumar, Harsh
- Tshakwanda, Petro M.
- Arzo, Sisay T.
- Devetsikiotis, Michael
- Granelli, Fabrizio
venue: 2024 IEEE 5th World AI IoT Congress, AIIoT 2024
venue_type: conference
year: 2024
doi: 10.1109/AIIoT61789.2024.10578954
url: https://www.scopus.com/pages/publications/85198830012?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 38--44
keywords:
- Artificial Intelligence
- Reinforcement Learning
- Role Delegation
- Software Defined Network
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0994 — Reinforcement Learning-Driven Adaptive Traffic Routing Role Delegation for Enhanced SDN Network Performance

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we introduce a novel method for autonomously assigning routing traffic roles in Software Defined Networks (SDN) using reinforcement learning. Our approach centers around a cloud-hosted central SDN controller interacting with two sub-SDN controllers situated in edge data centers. Each sub-controller manages three layer 2 switches and one wireless access point, connecting to five wired or wireless hosts generating randomized traffic. By collecting network data from hostto-host communications across diverse applications, we train a reinforcement learning agent to facilitate adaptive routing role delegation. The agent is tailored to identify optimal links between the main controller and subcontrollers, minimizing traffic congestion and ensuring ultra-low latency and high reliability during traffic routing. Our research aims to achieve dynamic and adaptive optimal routing, accommodating fluctuating traffic patterns and new device additions to the network. Leveraging PyTorch, we implement a neural network for the agent and employ a Q-learning algorithm for training, optimizing a reward function based on observed traffic congestion. Once trained, the agent autonomously delegates routing traffic roles to the least congested sub-controller. Performance evaluation involves analyzing traffic load and latency metrics, demonstrating the agent's proficiency in identifying optimal links and enhancing network performance, as observed through extensive experimentation and evaluation across diverse SDN scenarios. Furthermore, to foster collaboration and reproducibility within the research community, we make our implementation code and dataset publicly available on GitHub at https://github.com/your_username/project_name. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0994.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
