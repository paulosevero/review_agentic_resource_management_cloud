---
id: paper-0629
title: Distributed Multi-Agent Approach for Achieving Energy Efficiency and Computational Offloading in MECNs Using Asynchronous Advantage Actor-Critic
authors:
- Khan, Israr
- Raza, Salman
- Khan, Razaullah
- Rehman, Waheed ur
- Rahman, G. M. Shafiqur
- Tao, Xiaofeng
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12224605
url: https://www.scopus.com/pages/publications/85178336723?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- advanced asynchronous advantage actor-critic (A3C)
- cloud computing
- computational offloading
- deep reinforcement learning
- energy efficiency
- mobile edge computing
- multi-agent system
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

# paper-0629 — Distributed Multi-Agent Approach for Achieving Energy Efficiency and Computational Offloading in MECNs Using Asynchronous Advantage Actor-Critic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing networks (MECNs) based on hierarchical cloud computing have the ability to provide abundant resources to support the next-generation internet of things (IoT) network, which relies on artificial intelligence (AI). To address the instantaneous service and computation demands of IoT entities, AI-based solutions, particularly the deep reinforcement learning (DRL) strategy, have been intensively studied in both the academic and industrial fields. However, there are still many open challenges, namely, the lengthening convergence phenomena of the agent, network dynamics, resource diversity, and mode selection, which need to be tackled. A mixed integer non-linear fractional programming (MINLFP) problem is formulated to maximize computing and radio resources while maintaining quality of service (QoS) for every user’s equipment. We adopt the advanced asynchronous advantage actor-critic (A3C) approach to take full advantage of distributed multi-agent-based solutions for achieving energy efficiency in MECNs. The proposed approach, which employs A3C for computing offloading and resource allocation, is shown through numerical results to significantly reduce energy consumption and improve energy efficiency. This method’s effectiveness is further shown by comparing it to other benchmarks. © 2023 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0629.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
