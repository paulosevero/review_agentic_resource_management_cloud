---
id: paper-2529
title: 'Decentralized Task Offloading in Collaborative Edge Computing: A Digital Twin Assisted Multi-Agent Reinforcement Learning Approach'
authors:
- Chen, Xiangchun
- Cao, Jiannong
- Cao, Rui
- Sahni, Yuvraj
- Zhang, Mingjin
- Ji, Yusheng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3628502
url: https://www.scopus.com/pages/publications/105020886821?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4776--4790
keywords:
- decentralized task offloading
- digital twin
- Edge computing
- multi-agent reinforcement learning
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

# paper-2529 — Decentralized Task Offloading in Collaborative Edge Computing: A Digital Twin Assisted Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Decentralized Edge Computing (DEC) has emerged as a computing paradigm leveraging computational resources of edge nodes for complex, data-intensive applications. Decentralized task offloading decides when and at which edge node each task is executed without a central coordinator. However, ensuring reliability for decentralized task offloading is crucial, especially in critical applications like video analytics. Existing centralized approaches often face single points of failure and high communication overhead. Current decentralized methods often ignore task dependencies and bandwidth allocation, leading to suboptimal resource utilization and low reliability. We address the Reliability-aware Dependent Task Offloading (RDTO) problem in DEC, jointly optimizing bandwidth allocation, to maximize task success rate. The challenge of RDTO lies in optimizing dynamic task offloading and bandwidth allocation with task dependencies. We propose a Digital Twin assisted Multi-agent Reinforcement Learning (DT-MARL) algorithm. Our approach integrates a novel digital twin model that provides real-time estimation of task completion time and edge node failure rates. By integrating digital twin with multi-agent reinforcement learning, we enable each edge node to make informed decisions for offloading strategies, effectively improving the task success rate. Extensive experiments using real-world and synthetic datasets demonstrate that DT-MARL outperforms state-of-the-art baselines on task success rate up to 32.00% and 32.43%, respectively.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2529.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
