---
id: paper-1840
title: Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments
authors:
- Liang, Yi
- Xu, Guimei
- Wang, Yinzhou
- Ruan, NianYi
venue: ICCCR 2025 - 2025 5th International Conference on Computer, Control and Robotics
venue_type: conference
year: 2025
doi: 10.1109/ICCCR65461.2025.11072649
url: https://www.scopus.com/pages/publications/105012139600?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 483--488
keywords:
- cumulative data processing applications
- multi-agent reinforcement learning
- multi-cloud
- scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1840 — Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cumulative Data Processing (CDP) is a typical application in multi-cloud environments, where efficient job scheduling is crucial for achieving high performance and low-cost operation. However, existing multi-cloud job scheduling approaches fail to address the unique characteristics of CDP applications, such as long-term execution, dynamic job generation, and stage-wise differentiated resource demands, as they lack the capability to collaboratively optimize long-term scheduling decisions. To solve this, we propose CDP-MARL, a multi-agent reinforcement learning approach for job scheduling of CDP applications in multi-cloud environments. Built on the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm, CDP-MARL enables autonomous and collaborative decision-making for data center schedulers in distributed multi-cloud environments and employs MAPPO to solve the optimized scheduling strategy. It utilizes the simplified global state representation to reduce the training cost of the Actor and Critic networks in MAPPO. Additionally, a self-attention mechanism is integrated into the Critic network to improve global state representation, while a GRU-based Dynamic Policy Sub-Network (GRU-DPSN) is introduced in the Actor network to address the delayed reward issue in long-term scheduling. Experimental results demonstrate that, compared to state-of-the-art approaches, CDP-MARL reduces the resource cost by 35.97% and the Service Level Agreement (SLA) violation rate by 25.25% on average for CDP applications.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1840.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
