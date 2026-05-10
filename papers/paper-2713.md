---
id: paper-2713
title: Multi-agent reinforcement learning driven resource game optimization for network slicing in MEC-enabled HetNets
authors:
- Mao, Kai
venue: Scientific Reports
venue_type: journal
year: 2026
doi: 10.1038/s41598-025-33190-5
url: https://www.scopus.com/pages/publications/105028439083?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Evolutionary game theory (EGT)
- Intelligent optimization
- Mobile edge computing (MEC)
- Multi-intelligence reinforcement learning (MARL)
- Network slicing
- Quality of service (QoS)
- Resource allocation
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

# paper-2713 — Multi-agent reinforcement learning driven resource game optimization for network slicing in MEC-enabled HetNets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of Mobile Edge Computing (MEC) and network slicing technologies is critical to meet the diverse quality of service (QoS) requirements of 5G/6G.However,multi-tenancy (eMBB/uRLLC/mMTC) competition for resources in dynamic environments challenges traditional centralised allocation methods.In this paper, we propose a cooperative optimization framework for edge network slicing resources based on the fusion of multi-intelligence reinforcement learning (MARL) and evolutionary game theory (MARL-EGT).The framework models each slice tenant as an intelligent body with autonomous decision-making capability, which explores the optimal resource requesting strategy through interactive learning; meanwhile, evolutionary game dynamics is introduced to model the imitation, learning and evolution process of the slice population strategy, which guides the system to converge to an efficient evolutionary stable equilibrium (ESS).In order to cope with the problem of too large environment state space and intelligence coordination, a hierarchical attention mechanism and a credit-based contribution evaluation algorithm are innovatively designed to significantly improve the learning efficiency and convergence speed. In simulation experiments, under the MEC scenario constructed based on real data, the MARL-EGT scheme significantly outperforms benchmark methods such as federated reinforcement learning (FRL) and non-cooperative gaming (NCG) in terms of key metrics, such as total system utility, slicing SLA satisfaction rate, and resource utilization, and demonstrates superior dynamic environment adaptability, which provides large-scale, intelligent edge network slicing resource management new ideas. © The Author(s) 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2713.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
