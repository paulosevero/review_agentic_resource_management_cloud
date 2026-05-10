---
id: paper-1729
title: Asynchronous Federated Learning-Based Energy Scheduling for Microgrid-Enabled MEC Network
authors:
- Khan, Haneef
- Consul, Prakhar
- Jabbari, Abdoh
- Duraibi, Salahaldeen
- Zangoti, Hussein
- Budhiraja, Ishan
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2025.3560427
url: https://www.scopus.com/pages/publications/105003029525?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9133--9144
keywords:
- energy management
- federated learning
- microgrid
- Mobile edge computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1729 — Asynchronous Federated Learning-Based Energy Scheduling for Microgrid-Enabled MEC Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) is well known for its critical role in controlling the growth of Internet of Things (IoT) applications, even though energy demand forecasting is inherently challenging because of multiple task-specific factors. Including a microgrid as a backup energy source offers a chance to improve the effectiveness of energy distribution, but it also raises concerns about using non-renewable energy sources. This study explores the complex task of managing energy scheduling in a microgrid-enabled MEC network. It does this by minimizing residual planned energy using the conditional value at risk (CVaR) measure and illuminate the complexity of this NP-hard problem. To address this complex problem, a multi-agent stochastic game framework is implemented to achieve a Nash equilibrium for collective policies and prove model convergence, revealing the novel Asynchronous Federated Learning framework for Microgrid-Enabled MEC Network (AFFIN). A device selection strategy and a multi-agent Asynchronous Advantage Actor-Critic (A3C) algorithm with shared neural networks are employed to enhance learning efficiency. The proposed scheme enables localized model training and parameter sharing with the MEC server. The results demonstrated the exceptional effectiveness of incorporating CVaR into energy scheduling, surpassing the performance of random agent and single-agent models in terms of optimizing energy distribution in the MEC network. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1729.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
