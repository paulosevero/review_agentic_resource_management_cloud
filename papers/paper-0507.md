---
id: paper-0507
title: Joint resource management for mobility supported federated learning in Internet of Vehicles
authors:
- Wang, Ge
- Xu, Fangmin
- Zhang, Hengsheng
- Zhao, Chenglin
venue: Future Generation Computer Systems
venue_type: journal
year: 2022
doi: 10.1016/j.future.2021.11.020
url: https://www.scopus.com/pages/publications/85121229056?origin=resultslist
publisher: Elsevier B.V.
pages: 199--211
keywords:
- Distributed dynamic resource management
- Federated learning
- Internet of Vehicles
- Multi-access Edge Computing
- Multi-agent deep reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0507 — Joint resource management for mobility supported federated learning in Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, the powerful combination of Multi-access Edge Computing (MEC) and Artificial Intelligence (AI), called edge intelligence, promotes the development of Intelligent Transportation Systems (ITS). However, there is a mismatch between the ever-increasing consumer privacy awareness and the data leakage risk in centralized AI training solutions in vehicular edge scenarios, which has become a new obstacle to satisfying the user experience. As a promising privacy-preserving paradigm, federated learning synthesizes a global model only with the parameters of decentralized trained local models, avoiding the exposure of sensitive data. Given this, we introduce federated learning into the proposed two-level MEC-assisted vehicular network framework. This paper aims to address the challenges posed by adopting federated learning into the Internet of Vehicles (IoV) scenario. Firstly, as the entity of the participant (the local model training node of federated learning), vehicles have high mobility. We design a mobility supported federated learning participant decision algorithm to pick out participants from candidate vehicles. Secondly, federated learning is rather resource-consuming, inevitably incurring considerable costs to participants. We focus on the joint resource allocation problem to optimize the federated learning cost. Finally, considering the limitations of centralized resource allocation, we propose a fully distributed resource allocation method inspired by multi-agent deep reinforcement learning. Simulation results are presented to demonstrate the feasibility and effectiveness of the proposed schemes. © 2021

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0507.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
