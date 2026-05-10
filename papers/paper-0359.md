---
id: paper-0359
title: Cybertwin Assisted Wireless Asynchronous Federated Learning Mechanism for Edge Computing
authors:
- Xu, Yunting
- Zhou, Haibo
- Chen, Jiacheng
- Ma, Ting
- Shen, Sherman
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2021
doi: 10.1109/GLOBECOM46510.2021.9685076
url: https://www.scopus.com/pages/publications/85184642787?origin=resultslist
publisher: ''
pages: ''
keywords:
- Asynchronous Federated Learning
- Cybertwin
- Edge Intelligence
- Resource Allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0359 — Cybertwin Assisted Wireless Asynchronous Federated Learning Mechanism for Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The significant advances in wireless communication together with edge intelligent (EI) technology have facilitated the decentralized edge computing paradigm for data-intensive and delay-sensitive solution on massive Internet of Things (IoT) devices. In this paper, a Cybertwin assisted asynchronous federated learning (AFL) mechanism is proposed for realizing efficient edge computing by taking full advantage of local computation capability under heterogeneous wireless environment. First, Cybertwin is introduced as intermediary communication assistant to coordinate individual model aggregation between the users and the cloud server under AFL training process. Second, for the sake of flexible and effective utilization of communication-computation resources for edge computing, Cybertwin plays the role of intelligent agent to jointly take the local computing and up-link transmission into consideration. A resource optimization problem considering the diversified computing power, varied data size, and available communication bandwidth is formulated and we leverage the block coordinate descent (BCD) method to obtain optimal resource management solution. Extensive simulations are conducted to demonstrate the effectiveness of our proposed Cybertwin assisted AFL mechanism, which can shed further light on the application of data-intensive edge computing paradigm over wireless communication network. © 2021 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0359.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
