---
id: paper-0446
title: 'Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks'
authors:
- Kattepur, Ajay
- David, Sushanth
venue: Proceedings - 2022 IEEE 46th Annual Computers, Software, and Applications Conference, COMPSAC 2022
venue_type: conference
year: 2022
doi: 10.1109/COMPSAC54236.2022.00109
url: https://www.scopus.com/pages/publications/85137006932?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 624--629
keywords:
- 5G Service
- Data-center Networks
- Kubernetes
- Multi-Agent Reinforcement Learning
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

# paper-0446 — Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data-center network configurations are crucial in ensuring end-to-end differentiated service performance within 5G. Data-center networks encom-pass two domains: (i) the fat-tree networking fabric with leaf, spine and super-spine layers (ii) data-center server nodes with container and workload placement policies. These have traditionally been managed within silos with context and configurations driven within each domain. In this work, we examine the effect of configuration changes in one domain and its effect on the other. We develop Madelyn, a multi-domain multi-agent rein-forcement learning framework for data-center networks that can propose network-aware, virtual network function placement. This framework takes into account the data-center fabric wights, drop rates, capacities, load balancing and traffic shaping. It also considers the network function pod placements based on affinity / anti-affinity rules, node capacities and taints/tolerations. Using this multi-agent framework, we provide network aware scheduling policies for differentiated network function virtualization services running on Kubernetes pods within data-center networks. The results are demonstrated over a real traffic dataset collected over Ericsson's testbed networks. © 2022 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0446.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
