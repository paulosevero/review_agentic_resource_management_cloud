---
id: paper-0637
title: 'Maritime Search and Rescue Leveraging Heterogeneous Units: A Multi-Agent Reinforcement Learning Approach'
authors:
- Lei, Chengjia
- Wu, Shaohua
- Yang, Yi
- Xue, Jiayin
- Zhang, Qinyu
venue: 2023 IEEE/CIC International Conference on Communications in China, ICCC 2023
venue_type: conference
year: 2023
doi: 10.1109/ICCC57788.2023.10233604
url: https://www.scopus.com/pages/publications/85172993407?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- efficiency
- fault-tolerant communication
- Maritime search and rescue
- multi-agent reinforcement learning
- rescue ship
- unmanned aerial vehicle
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

# paper-0637 — Maritime Search and Rescue Leveraging Heterogeneous Units: A Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, with the continuous growth of offshore operations, maritime search and rescue (MSAR) has received widespread attention as a crucial guarantee for safety. In this paper, we aim to achieve efficient and communication fault-tolerant MSAR operations by employing trajectory planning and resource scheduling for heterogeneous units involving observation unmanned aerial vehicles (UAVs), router UAVs, and rescue ships equipped with mobile edge computing (MEC). Firstly, we model several essential components related to MSAR, including the ocean current environment, UAVs for observing, fault tolerance of routing network, MEC scheduling, and energy consumption of UAVs. Secondly, we formulate the optimization problem into a decentralized partially observable Markov Decision Process (Dec-POMDP) and then introduce the multi-agent reinforcement learning (MARL) approach to search for an optimal joint strategy. Finally, experimental results demonstrate that in the model of MSAR we constructed, our improved MARL approach, named IPPO-nGAE, outperforms other benchmarks in both efficiency and fault tolerance.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0637.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
