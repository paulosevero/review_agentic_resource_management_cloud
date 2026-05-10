---
id: paper-0806
title: Hierarchical Multi-Agent Deep Reinforcement Learning for Energy-Efficient Hybrid Computation Offloading
authors:
- Zhou, Hang
- Long, Yusi
- Gong, Shimin
- Zhu, Kun
- Hoang, Dinh Thai
- Niyato, Dusit
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2022.3202525
url: https://www.scopus.com/pages/publications/85137562894?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 986--1001
keywords:
- Backscatter communications
- mobile edge computing
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

# paper-0806 — Hierarchical Multi-Agent Deep Reinforcement Learning for Energy-Efficient Hybrid Computation Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) provides an economical way for the resource-constrained edge users to offload computational workload to MEC servers co-located with the access point (AP). In this article, we consider a hybrid computation offloading scheme that allows edge users to offload workloads by using active RF communications and backscatter communications. We aim to maximize the overall energy efficiency subject to the completion of all workload by jointly optimizing the AP's beamforming and the users' offloading decisions. Considering a dynamic environment, we propose a hierarchical multi-agent deep reinforcement learning (H-MADRL) framework to solve this problem. The high-level agent resides in the AP and optimizes the beamforming strategy, while the low-level user agents learn and adapt individuals' offloading strategies. To further improve the learning efficiency, we propose a novel optimization-driven learning algorithm that allows the AP to estimate the low-level users' actions by solving approximate optimization problem efficiently. Then, the action estimation can be shared with all users and drive them to update individuals' actions independently. Simulation results reveal that our algorithm can improve the system performance by 50%. The learning efficiency and reliability are also improved significantly comparing to the model-free learning methods.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0806.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
