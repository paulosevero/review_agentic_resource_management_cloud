---
id: paper-2155
title: GenAI-Enhanced Federated Multiagent DRL for Digital-Twin-Assisted IoV Networks
authors:
- Singh, Piyush
- Hazarika, Bishmita
- Singh, Keshav
- Huang, Wan-Jen
- Duong, Trung Q.
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3526150
url: https://www.scopus.com/pages/publications/85215599028?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4834--4851
keywords:
- Digital twin (DT)
- federated learning (FL)
- Internet of Vehicles (IoV)
- mobile-edge computing (MEC)
- multiagent reinforcement learning (MARL)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2155 — GenAI-Enhanced Federated Multiagent DRL for Digital-Twin-Assisted IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Achieving real-time decision-making and efficient resource management in dynamic, large-scale Internet-of-Vehicles (IoV) networks is a significant challenge due to their inherent complexity and scale. To address this, we propose a digital twin (DT)-assisted IoV framework that integrates a novel semi-synchronous adaptive federated learning (AdFL) approach with multiagent deep reinforcement learning, enhanced by generative artificial intelligence (GenAI) techniques, specifically conditional variational autoencoders (CVAEs). The framework optimizes partial task offloading across distributed mobile-edge computing (MEC) servers, ensuring scalable, efficient, and accurate decision-making in heterogeneous vehicular networks. By continuously mirroring the real-time states of vehicles and roadside units (RSUs), the DT framework enables precise resource allocation and adaptive task management. To tackle the complexities of dynamic environments, we design a global model with transformer layers embedded in the federated learning (FL) process, capturing long-range dependencies. A novel semi-synchronous aggregation mechanism is introduced to balance timely updates with model quality. The proposed adaptive federated multiagent reinforcement learning (AF-MARL) algorithm facilitates decentralized, collaborative learning among vehicles and RSUs, optimizing overall cost, and energy efficiency, reducing delay, and improving task completion rates. Extensive simulations demonstrate the effectiveness of the proposed framework against other existing approaches, highlighting its potential to transform real-time decision-making in IoV networks.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2155.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
