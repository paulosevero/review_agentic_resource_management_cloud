---
id: paper-2449
title: 'Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding'
authors:
- Zhang, Jingjing
- Deng, Xiaoheng
- Gui, Jinsong
- Chen, Xuechen
- Wan, Shaohua
- Min, Geyong
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2025
doi: 10.1109/TCC.2025.3571095
url: https://www.scopus.com/pages/publications/105005465650?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 854--866
keywords:
- Cloud gaming
- deep reinforcement learning
- quality-of-experience (QoE)
- resource allocation
- video encoding configuration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2449 — Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud gaming represents a major part of contemporary gaming. To boost the Quality-of-Experience (QoE) of cloud gaming, the integration of Dynamic Adaptive Video Encoding (DAVE) with Multi-access Edge Computing (MEC) has become the natural candidate owing to its flexibility and reliable transmission support for real-time interactions. However, as multiple gamers compete for limited resources to achieve personalized QoE, such as ultra-high video quality and ultra-low latency, how to support efficient edge resource optimization is a fundamental and important problem. Furthermore, determining the optimal game video encoding configuration in real-time poses significant challenges, especially when lacking the information on future video and edge network resources. To address these key issues, we jointly optimize the video encoding as well as computing and communication resource allocation by active mutual adaptation of video coding configurations and physical resources in a Software Defined Networking (SDN)-assisted edge network. This eliminates the performance bottleneck caused by decoupling optimization of coding parameter configuration and physical resource allocation. The SDN-assisted edge network architecture supports efficient on-demand resource management, provides global network information, and meets the stringent time-varying game requests. Due to the significant time scale difference between video chunk and physical resource block, we propose a novel Asynchronous Decision-Making Multi Agent Proximal Policy Optimization algorithm (AD-MAPPO), which can address the credit assignment problem with a single agent. It can also adapt to the highly dynamic cloud gaming environment without prior knowledge and a deterministic environmental model. Extensive experimentation based on real cloud gaming datasets convincingly demonstrates that our approach can significantly enhance the overall QoE of gamers. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2449.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
