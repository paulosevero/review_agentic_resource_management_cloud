---
id: paper-0771
title: Joint Client Selection and Training optimization for Energy-Efficient Federated Learning
authors:
- Yan, Kang
- Shu, Nina
- Wu, Tao
- Liu, Chunsheng
- Huang, Jun
- Yu, Jingbo
venue: Proceedings - 2023 19th International Conference on Mobility, Sensing and Networking, MSN 2023
venue_type: conference
year: 2023
doi: 10.1109/MSN60784.2023.00125
url: https://www.scopus.com/pages/publications/85197548796?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 849--854
keywords:
- deep reinforcement learning
- energy efficiency
- Federated Learning
- mobile edge computing
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

# paper-0771 — Joint Client Selection and Training optimization for Energy-Efficient Federated Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated Learning (FL) allows multiple edge devices (EDs) to collaboratively train shared models without sharing raw data, offering a prospective privacy-preserving machine learning framework. However, energy consumption has become a major challenge due to the high energy requirements of FL tasks and the limited battery capacity of EDs. Considering the high heterogeneity of resources and data among EDs, client selection strategies and control of local iteration numbers are key factors for optimizing energy efficiency in FL. In this paper, we present Global-aware Independent Proximal Policy optimization (GIPPO), a novel deep reinforcement learning method that jointly optimizes client selection and local training in heterogeneous environments. GIPPO considers each client as an individual intelligent agent and prioritizes all the clients in each training round based on their respective states. By intelligently selecting clients and assigning appropriate local iteration numbers, the method aims to minimize system energy consumption and enhance model performance. Experimental results demonstrate that our proposed method achieves significant energy cost savings, up to 77%, compared to baseline methods. Moreover, our method effectively adapts to varying degrees of data heterogeneity. © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0771.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
