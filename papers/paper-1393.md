---
id: paper-1393
title: Optimizing Computation Offloading with Explainable Multi-Agent Deep Q-Networks
authors:
- Amarasooriya, Rasini
- Gregory, Mark A.
- Li, Shuo
venue: 2025 IEEE 35th International Telecommunication Networks and Applications Conference, ITNAC 2025
venue_type: conference
year: 2025
doi: 10.1109/ITNAC66378.2025.11302726
url: https://www.scopus.com/pages/publications/105032082364?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computation Offloading
- Explainable AI (XAI)
- Mobile Edge Computing (MEC)
- Multi-Agent Reinforcement Learning (MARL)
- Resource Allocation
- SHAP Feature Selection
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1393 — Optimizing Computation Offloading with Explainable Multi-Agent Deep Q-Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computation offloading in Mobile Edge Computing (MEC) is vital for IoT networks, but existing Deep Reinforcement Learning (DRL) models face inefficiency due to high-dimensional state spaces. This paper introduces a framework combining Explainable AI (XAI) with a Multi-Agent Deep Q-Network (MADQN) under a Centralized Training and Decentralized Execution (CTDE) setup. Using SHAP (Shapley Additive Explanations) for iterative feature selection, the model systematically removes less impactful features. Experiments show a 69.2% task completion rate, outperforming Random (40.4%) and Round-Robin (35.5%) baselines. The SHAP-simplified version used 19.4% fewer features with only a 2% performance drop (67.2%), demonstrating that XAI-based simplification can reduce complexity with minimal performance loss, enabling more efficient and scalable multi-agent edge systems. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1393.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
