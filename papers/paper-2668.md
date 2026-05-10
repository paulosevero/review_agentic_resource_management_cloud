---
id: paper-2668
title: Toward Practical Operation of Deep Reinforcement Learning Agents in Real-World Network Management at Open RAN Edges
authors:
- Li, Haiyuan
- Madhukumar, Hari
- Li, Peizheng
- Liu, Yuelin
- Teng, Yiran
- Wu, Yulei
- Wang, Ning
- Yan, Shuangyi
- Simeonidou, Dimitra
venue: IEEE Communications Magazine
venue_type: journal
year: 2026
doi: 10.1109/MCOM.001.2500207
url: https://www.scopus.com/pages/publications/105010689693?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 134--140
keywords:
- Deep learning
- Deep reinforcement learning
- Intelligent agents
- Life cycle
- Multi agent systems
- Network architecture
- Network management
- Topology
- Connectivity reliability
- Edge computing
- Growing demand
- Low latency
- Multiaccess
- Networks management
- Real world deployment
- Real-world networks
- Reinforcement learning agent
- Reinforcement learnings
- Reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2668 — Toward Practical Operation of Deep Reinforcement Learning Agents in Real-World Network Management at Open RAN Edges

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deep Reinforcement Learning (DRL) has emerged as a powerful solution for meeting the growing demands for connectivity, reliability, low latency and operational efficiency in advanced networks. However, most research has focused on theoretical analysis and simulations, with limited investigation into real-world deployment. To bridge the gap and support practical DRL deployment for network management, we first present an orchestration framework that integrates ETSI Multi-access Edge Computing (MEC) with Open RAN, enabling seamless adoption of DRL-based strategies across different time scales while enhancing agent lifecycle management. We then identify three critical challenges hindering DRL's real-world deployment, including asynchronous requests from unpredictable or bursty traffic, adaptability and generalization across heterogeneous topologies and evolving service demands, and prolonged convergence and service interruptions due to exploration in live operational environments. To address these challenges, we propose a three-fold solution strategy: advanced time-series integration for handling asynchronized traffic, flexible architecture design such as multi-agent DRL and incremental learning to support heterogeneous scenarios, and simulation-driven deployment with transfer learning to reduce convergence time and service disruptions. Lastly, the feasibility of the MEC-O-RAN architecture is validated on an urban-wide testing infrastructure, and two real-world use cases are presented, showcasing the three identified challenges and demonstrating the effectiveness of the proposed solutions. © 1979-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2668.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
