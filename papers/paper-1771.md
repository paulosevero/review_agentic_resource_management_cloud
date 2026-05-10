---
id: paper-1771
title: A Blockchain-Empowered Multiaggregator Federated Learning Architecture in Edge Computing With Deep Reinforcement Learning Optimization
authors:
- Li, Xiao
- Wu, Weili
venue: IEEE Transactions on Computational Social Systems
venue_type: journal
year: 2025
doi: 10.1109/TCSS.2024.3481882
url: https://www.scopus.com/pages/publications/105002396102?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 645--657
keywords:
- Blockchain
- deep reinforcement learning (DRL)
- distributed machine learning
- edge computing
- federated learning (FL)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1771 — A Blockchain-Empowered Multiaggregator Federated Learning Architecture in Edge Computing With Deep Reinforcement Learning Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated learning (FL) is emerging as a sought-after distributed machine learning architecture, offering the advantage of model training without direct exposure to raw data. With advancements in network infrastructure, FL has been seamlessly integrated into edge computing. However, the limited resources on edge devices introduce security vulnerabilities to FL in the context. While blockchain technology promises to bolster security, practical deployment on resource-constrained edge devices remains a challenge. Moreover, the exploration of FL with multiple aggregators in edge computing is still new in the literature. Addressing these gaps, we introduce the blockchain-empowered heterogeneous multiaggregator federated learning architecture (BMA-FL). We design a novel lightweight Byzantine consensus mechanism, namely PBCM, to enable secure and fast model aggregation and synchronization in BMA-FL. We study the heterogeneity problem in BMA-FL that the aggregators are associated with varied number of connected trainers with non-IID data distributions and diverse training speed. We propose a multiagent deep reinforcement learning algorithm (MASB-DRL) to help aggregators decide the best training strategies. Experiments on real-word datasets demonstrate the efficiency of BMA-FL to achieve better models faster than baselines, showing the efficacy of PBCM and MASB-DRL. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1771.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
