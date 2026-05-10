---
id: paper-2621
title: 'Blockchain-enabled Incentive Mechanism for Federated Learning: A Multi-Agent Deep Deterministic Policy Gradient Approach'
authors:
- Jain, Vibha
- Verma, Prabal
- Kumar, Mohit
- Kaushik, Aryan
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2026
doi: 10.1109/TNSM.2026.3682129
url: https://www.scopus.com/pages/publications/105035559700?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Blockchain
- Federated Learning
- Incentive Mechanism
- MA-DDPG
- Multi-Agent Deep Deterministic Policy Gradient
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2621 — Blockchain-enabled Incentive Mechanism for Federated Learning: A Multi-Agent Deep Deterministic Policy Gradient Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The expeditious growth of the Internet of Things (IoT) generates massive data, which allows advanced machine learning. However, the traditional approach of centralized model training raises the issue of high bandwidth consumption and privacy. Federated learning (FL) mitigates this by enabling local training on raw data with centralized aggregation to generate the global model. The effectiveness of FL depends upon the active participation of resource-constrained local devices. This article presents a blockchain-enabled incentive mechanism for FL leveraging the Multi-Agent Deep Deterministic Policy Gradient (MA-DDPG) algorithm. Specifically, an incentive scheme is formulated with the MEC (Mobile Edge Computing) server as the leader agent and local devices as learning agents in a cooperative environment. We formalize a two-stage Stackelberg game to establish a Nash equilibrium, which ensures fair and utility-optimized reward distribution for MEC and devices. A Markov Decision Process (MDP) is utilized to solve the equilibrium with incomplete knowledge, and utilities are optimized using the MA-DDPG algorithm. The proposed model considers data quality and device contribution to obtain optimal reward distribution and participation strategies dynamically. The experimental results show an approximate 38% improvement in MEC utility and approx 17% in device utility, with rapid convergence (approximately 300-500 episodes) at a learning rate of 0.0001. © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2621.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
