---
id: paper-2318
title: Research on dynamic resource allocation optimization in 6G networks based on deep reinforcement learning
authors:
- Xie, Jinghong
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2025
doi: 10.1117/12.3070417
url: https://www.scopus.com/pages/publications/105022629018?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- 6G Networks
- Deep Q-Network
- Deep Reinforcement Learning
- Dynamic Resource Allocation
- Energy Efficiency
- Transmission Rate
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2318 — Research on dynamic resource allocation optimization in 6G networks based on deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper proposes a dynamic resource allocation optimization method based on deep reinforcement learning to address the challenges of signal interference, latency sensitivity, and energy consumption in 6G networks caused by ultra-dense deployment and diverse applications. First, it elaborates on the challenges posed by the surge in IoT devices and data traffic to traditional communication models, as well as the role of edge computing, fog computing, and emerging technologies such as Cybertwin in mitigating network latency and computational pressure. Then, the paper details the principles of using Deep Q-Network (DQN) and its variants for channel estimation, interference detection, and resource scheduling, analyzing the advantages of reinforcement learning methods such as value iteration and policy gradient in complex multi-cell scenarios. Additionally, it discusses the application of multi-agent collaboration in vehicular network resource allocation. Simulation results demonstrate that the proposed scheme significantly improves network transmission rate, energy efficiency, and system utility, offering better stability and robustness compared to traditional modular optimization methods. Finally, the paper explores the potential applications of deep reinforcement learning in more complex network environments and its integration with other optimization algorithms, providing theoretical foundations and technical support for the efficient operation of 6G networks. © 2025 SPIE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2318.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
