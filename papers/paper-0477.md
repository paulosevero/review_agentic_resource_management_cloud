---
id: paper-0477
title: Automated Deployment of Virtual Network Function in 5G Network Slicing Using Deep Reinforcement Learning
authors:
- Othman, Anuar
- Nayan, Nazrul A.
- Abdullah, Siti N. H. S.
venue: IEEE Access
venue_type: journal
year: 2022
doi: 10.1109/ACCESS.2022.3178157
url: https://www.scopus.com/pages/publications/85132836534?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 61065--61079
keywords:
- 5G mobile communication
- decision support systems
- edge computing
- intelligent agents
- machine learning
- multi-layer neural network
- network function virtualization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0477 — Automated Deployment of Virtual Network Function in 5G Network Slicing Using Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fifth-generation mobile technologies introduce the concept of network slicing, which allows the creation of logical networks consisting of network services and the associated physical and virtual network functions. The early form of network slicing allowed for fixed resource allocation and static network function deployment. However, this approach can lead to inefficiency and service degradation. This study aims to optimize the deployment of virtual network functions within a hybrid cloud infrastructure from the perspective of mission-critical communications. The first task involves designing a deep reinforcement learning-based scheme to determine a significant deployment policy that minimizes the overall delays and costs of logical networks. The scheme performance is evaluated by using a simulated traffic dataset that followed Poisson distributions for a wide range of configurations. In dynamic environments with stationary traffic patterns, simulation results show that the scheme outperforms the one-step look-ahead and fixed-location algorithms by 35.80% and 52.16%, respectively, on average. A value iteration-based scheme is used as a benchmark and only surpasses the proposed scheme by 3.5% on average. Simulation results using a real-world traffic dataset show that the scheme can support nonstationary traffic patterns and cater to large-scale scenarios with many suitable deployment locations by leveraging a function that indicates the relative importance of selecting one location over the others.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0477.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
