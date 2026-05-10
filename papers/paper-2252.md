---
id: paper-2252
title: Adaptive offloading in multi-access edge networks via hierarchical federated learning and real-time system adaptation
authors:
- Wang, Jie
- Liang, Qiao
- Mohajer, Amin
venue: International Journal of Sensor Networks
venue_type: journal
year: 2025
doi: 10.1504/IJSNET.2025.148455
url: https://www.scopus.com/pages/publications/105015427874?origin=resultslist
publisher: Inderscience Publishers
pages: 1--17
keywords:
- digital twin modelling
- federated learning
- GATs
- graph attention networks
- intelligent network orchestration
- multi-agent deep reinforcement learning
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

# paper-2252 — Adaptive offloading in multi-access edge networks via hierarchical federated learning and real-time system adaptation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Achieving ultra-reliable real-time digital twin (DT) adaptation in mobile edge environments requires intelligent orchestration of computation and communication under user heterogeneity and dynamic mobility. This paper introduces GADENet, a graph attention-enhanced digital twin evolution network that fuses graph neural modelling, multi-agent actor-critic learning, and hierarchical federated personalisation to enable seamless digital representations of user equipment (UE) in distributed edge networks. At its core, GADENet employs a GAT-assisted multi-agent deep deterministic policy gradient (MADDPG) framework to jointly learn optimal DT migration and personalisation strategies across edge servers, guided by real-time traffic topologies and resource interdependencies. Each DT model is modularised into generalisable and adaptive subspaces, trained collaboratively through a three-tier edge-cloud federated loop and refined using localised attention-based updates. For efficient mobility handling, we propose a parameter-sliced DT relay protocol that selectively migrates the minimal personalisation subset across servers, leveraging learned action-value functions to minimise response latency. Extensive simulations on CIFAR-based datasets and synthetic edge workloads demonstrate that GADENet achieves up to 30% reduction in interaction latency and significantly boosts modelling fidelity versus strong federated and DRL-based baselines. This work offers a principled blueprint for intelligent DT deployment under the constraints of 6G and next-gen IoT fabrics. Copyright © 2025 Inderscience Enterprises Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2252.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
