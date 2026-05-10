---
id: paper-0864
title: Optimization of Computing Power Network Routing Strategies based on Multi-Agent Soft Actor-Critic
authors:
- Chen, Zhongyue
- Zhang, Shicong
- Tang, Ying
- Xu, Mengke
- Wu, Xiaoqing
- Ye, Minchao
- Zhang, Zhaojuan
- Qi, Yaping
- Lu, Huijuan
- Huo, Wanli
venue: 2024 9th International Conference on Intelligent Computing and Signal Processing, ICSP 2024
venue_type: conference
year: 2024
doi: 10.1109/ICSP62122.2024.10743909
url: https://www.scopus.com/pages/publications/85211443511?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 426--430
keywords:
- Computing Power Network
- Deep Reinforcement Learning
- Multi-Agent Soft Actor-Critic
- Optimization of Routing Strategy
- Software-Defined Networking
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0864 — Optimization of Computing Power Network Routing Strategies based on Multi-Agent Soft Actor-Critic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Despite rapid developments in cloud computing, big data, and artificial intelligence, the Computing Power Network, as a new type of information infrastructure supporting the digital transformation and upgrading of various industries, faces significant challenges in efficiently scheduling, and managing computing and network resources. This paper introduces an optimization method for the ComputingRoute algorithm based on the Multi-Agent Soft Actor-Critic algorithm, operating within a Software-Defined Networking (SDN) architecture to address the efficiency issues in data transmission within the computing power network. The method leverages collaboration among multiple intelligent agents and employs deep reinforcement learning to optimize routing paths. Experimental results indicate that the MASAC algorithm, compared to traditional Actor-Critic algorithms, shows a 43.63 % improvement in stable average reward values, demonstrating better learning efficiency and performance. Furthermore, the soft policy updates, entropy regularization, and the use of target networks in the MASAC algorithm enhance its stability, improving training efficiency and performance. In performance comparisons with other computing power network routing strategies, the proposed ComputingRoute solution minimizes computing power requirements while reducing latency by 39.06% compared to DRL-TE and 21.42% compared to SmartPath. However, ComputingRoute exhibits a slightly higher packet loss rate than SmartPath. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0864.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
