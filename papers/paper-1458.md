---
id: paper-1458
title: Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration
authors:
- Che, Chang
- Xiang, Luping
- Hu, Jie
- Yang, Kun
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2025
doi: 10.1109/ICCT67417.2025.11374267
url: https://www.scopus.com/pages/publications/105034107938?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1913--1918
keywords:
- causal inference
- Digital twin
- large-scale networks
- multi-agent reinforcement learning
- service migration
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1458 — Digital Twin-Assisted Causal Multi-Agent Reinforcement Learning for Large-Scale Network Service Migration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic service migration is essential for guaranteeing quality of service (QoS) for mobile users in multi-access edge computing (MEC). However, conventional reinforcement learning and other strategies frequently result in suboptimal policies. These methods are unable to differentiate between actual cause-and-effect relationships and fake patterns due to their reliance on correlational data, resulting in inefficient and expensive migrations. This paper introduces a novel digital twinassisted causal multi-agent reinforcement learning (DT-CausalMARL) framework to address this fundamental limitation. We change the optimization objective from minimizing direct system cost to maximizing the causal gain of migration actions. This is accomplished by employing a digital twin as a counterfactual analysis engine to assess the actual consequences of decisions in comparison to a baseline policy. This causal gain is subsequently employed as a robust reward signal by a causal multi-agent deep deterministic policy gradient (Causal-MADDPG) algorithm to train cooperative agents. Our framework outperforms standard MARL baselines by reducing harmful 'regretful migrations' and improving system stability under dynamic traffic loads. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1458.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
