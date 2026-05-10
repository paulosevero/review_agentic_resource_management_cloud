---
id: paper-0460
title: DRL-Based Long-Term Resource Planning for Task Offloading Policies in Multiserver Edge Computing Networks
authors:
- Li, Haiyuan
- Assis, Karcius Day R.
- Yan, Shuangyi
- Simeonidou, Dimitra
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2022
doi: 10.1109/TNSM.2022.3191748
url: https://www.scopus.com/pages/publications/85135227419?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4151--4164
keywords:
- deep reinforcement learning
- long-term scheduling policy
- Multi-access network
- resource optimization
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0460 — DRL-Based Long-Term Resource Planning for Task Offloading Policies in Multiserver Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) has been regarded as one of the essential technologies for mobile networks, by providing computing resources and services close to users, thereby, avoiding extra energy consumption and fitting the low-latency ultra-reliable requirements for emerging 5G applications. Task offloading policy plays a pivotal role in handling offloading requests and maximizing the network computing performance. Most recently developed offloading solutions are designed for instant rewards, therefore, neglecting the long-term computing resource optimization at the edge, which fail to deliver optimized network performance when a significant increase of computing requests appears. In this paper, with the objective of maximizing long-term offloading benefits on delay and energy consumption, task offloading policies are proposed to firstly avoid resource over-distribution through deep reinforcement learning (DRL) based resource reservation and server cooperation, and secondly maximize the average instant reward and the utilization of reserved resources by an optimization-based joint policy consisting of offloading decision, transmission power allocation and resource distribution. The DRL-based joint policy is evaluated in a simulated multi-server edge computing network. Compared to previous solutions, the DRL-based algorithms achieve higher and more reliable overall rewards. Of the implemented three DRL-based algorithms, fully cooperative multi-agent DRL accounts for cooperation between servers, achieving a 70.5% reduction in reward variance and a 13.4% increase in average rewards over 500 continuous operations. Resource balanced policies on long-term rewards help edge networks handle the explosive growth of 5G computing-intensive applications in the future.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0460.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
