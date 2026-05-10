---
id: paper-1733
title: Federated Multi-Agent Deep Reinforcement Learning for Task Offloading and Resource Allocation in Multi-WBAN MEC Systems
authors:
- Khater, Heba M.
- Sallabi, Farag
- Barka, Ezedin
- Serhani, Mohamed Adel
venue: 2025 International Conference on Cybersecurity and AI-Based Systems, Cyber-AI 2025
venue_type: conference
year: 2025
doi: 10.1109/Cyber-AI66431.2025.11233660
url: https://www.scopus.com/pages/publications/105028739222?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 256--261
keywords:
- Deep Reinforcement Learning
- Federated Learning
- Mobile Edge Computing
- Task offloading optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1733 — Federated Multi-Agent Deep Reinforcement Learning for Task Offloading and Resource Allocation in Multi-WBAN MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wireless Body Area Network applications demand reliable, low-latency task processing while operating under stringent energy and deadline constraints. Although mobile devices have achieved significant computational advances, they remain limited by processing capabilities and battery life. Mobile Edge Computing (MEC) presents a viable solution through computational task offloading; however, developing optimal offloading strategies poses considerable challenges due to the dynamic and distributed nature of WBAN environments. This paper introduces a Federated Multi-Agent Deep Deterministic Policy Gradient (FL-MADDPG) framework for intelligent task offloading and resource allocation in multi-WBAN MEC systems. Our approach simultaneously optimizes three critical objectives: minimizing mobile device energy consumption, ensuring task deadline compliance, and maximizing MEC server resource utilization efficiency. To address scalability concerns and maintain data privacy, federated learning is integrated to enable periodic parameter aggregation across distributed learning agents without exposing sensitive user data. Simulation results demonstrate the effectiveness of the proposed model in improving overall system performance.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1733.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
