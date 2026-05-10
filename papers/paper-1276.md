---
id: paper-1276
title: Attention-Augmented MADDPG in NOMA-Based Vehicular Mobile Edge Computational Offloading
authors:
- Wu, Liangshun
- Qu, Junsuo
- Li, Shilin
- Zhang, Cong
- Du, Jianbo
- Sun, Xiang
- Zhou, Jiehan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3397648
url: https://www.scopus.com/pages/publications/85192998652?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 27000--27014
keywords:
- Attention mechanism
- computational offloading
- deep reinforce learning
- multiagent deep deterministic policy gradient (MADDPG)
- nonorthogonal multiple access (NOMA)
- vehicular Mobile Edge Computing (vMEC)
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

# paper-1276 — Attention-Augmented MADDPG in NOMA-Based Vehicular Mobile Edge Computational Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular mobile edge computing (vMEC) and nonorthogonal multiple access (NOMA) have emerged as promising technologies for enabling low-latency and high-throughput applications in vehicular networks. In this article, we propose a novel multiagent deep deterministic policy gradient (MADDPG) approach for resource allocation in NOMA-based vMEC systems. Our approach leverages deep reinforcement learning (DRL) to enable vehicles to offload computation-intensive tasks to nearby edge servers, optimizing resource allocation decisions while ensuring low-latency communication. We introduce an attention mechanism within the MADDPG model to dynamically focus on relevant information from the input state and joint actions, enhancing the model's predictive accuracy. Additionally, we propose an attention-based experience replay method to expedite network convergence. The simulation results highlight the effectiveness of multiagent reinforcement learning (MARL) algorithms, such as MADDPG with attention, in achieving better convergence and performance in various scenarios. The influence of different model parameters, such as input data volumes, task load levels, and resource configurations, on optimization results is also evident. The decision making processes of agents are dynamic and depend on factors specific to the task and environment.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1276.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
