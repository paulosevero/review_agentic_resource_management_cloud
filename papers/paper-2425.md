---
id: paper-2425
title: 'DeepRB: Deep Resource Broker Based on Clustered Federated Learning for Edge Video Analytics'
authors:
- Zhang, Xiaojie
- Debroy, Saptarshi
- Wang, Peng
- Li, Keqin
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2025
doi: 10.1109/TNSM.2025.3560657
url: https://www.scopus.com/pages/publications/105002748525?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3325--3340
keywords:
- edge computing
- Energy efficiency
- real-time video analytics
- resource management
- service placement
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

# paper-2425 — DeepRB: Deep Resource Broker Based on Clustered Federated Learning for Edge Video Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing plays a crucial role in large-scale and real-time video analytics for smart cities, particularly in environments with massive machine-type communications (mMTC) among IoT devices. Due to the dynamic nature of mMTC, one of the main challenges is to achieve energy-efficient resource allocation and service placement in resource—constrained edge computing environments. In this paper, we introduce DeepRB, a deep learning-based resource broker framework designed for real-time video analytics in edge-native environments. DeepRB employs a two-stage algorithm to address both resource allocation and service placement efficiently. First, it uses a Residual Multilayer Perceptron (ResMLP) network to approximate traditional iterative resource allocation policies for IoT devices that frequently transition between active and idle states. Second, for service placement, DeepRB leverages a multi-agent federated deep reinforcement learning (DRL) approach that incorporates clustering and knowledge-aware model aggregation. Through extensive simulations, we demonstrate the effectiveness of DeepRB in improving schedulability and scalability compared to baseline edge resource management algorithms. Our results highlight the potential of DeepRB for optimizing resource allocation and service placement for real-time video analytics in dynamic and resource-constrained edge computing environments. © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2425.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
