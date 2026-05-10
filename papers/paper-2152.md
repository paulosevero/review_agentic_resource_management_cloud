---
id: paper-2152
title: Digital Twin-Assisted Adaptive Federated Multi-Agent DRL with GenAI for Optimized Resource Allocation in IoV Networks
authors:
- Singh, Piyush
- Hazarika, Bishmita
- Singh, Keshav
- Huang, Wan-Jen
- Duong, Trung Q.
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2025
doi: 10.1109/WCNC61545.2025.10978333
url: https://www.scopus.com/pages/publications/105006408906?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- and Mobile Edge Computing (MEC)
- Digital Twin (DT)
- Federated Learning (FL)
- Internet of Vehicles (IoV)
- Multi-Agent Reinforcement Learning (MARL)
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

# paper-2152 — Digital Twin-Assisted Adaptive Federated Multi-Agent DRL with GenAI for Optimized Resource Allocation in IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this study, we introduce a digital twin (DT)-assisted IoV framework that combines a semi-synchronous adaptive federated learning (AdFL) method with multi-agent deep reinforcement learning, enhanced by generative artificial intelligence (GenAI) techniques, specifically conditional variational autoencoders (CVAE). This framework optimizes partial task offloading across distributed mobile edge computing (MEC) servers, ensuring scalable and efficient decision-making in diverse vehicular networks. By continuously reflecting the real-time conditions of vehicles and roadside units (RSUs), the DT framework ensures precise resource distribution and adaptive task handling. To handle the complexity of dynamic environments, we develop a global model that includes transformer layers in the federated learning (FL) process, which captures long-range dependencies. A semi-synchronous aggregation mechanism is introduced to maintain a balance between timely updates and model quality. The adaptive federated multi-agent reinforcement learning (AF-MARL) algorithm enables decentralized, collaborative learning among vehicles and RSUs, optimizing overall cost and energy use, reducing delays, and improving task completion rates. Comprehensive simulations show the framework's effectiveness compared to existing methods, emphasizing its potential to revolutionize real-time decision-making in IoV networks. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2152.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
