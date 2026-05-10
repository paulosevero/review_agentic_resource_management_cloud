---
id: paper-1757
title: Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning
authors:
- Lai, Junyu
- Liu, Huashuo
- Xu, Guoyao
- Jiang, Weiwei
- Wang, Xiong
- Jiang, Dingde
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2024.3510562
url: https://www.scopus.com/pages/publications/85211213580?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2554--2567
keywords:
- computation offloading
- edge computing
- hierarchical reinforcement learning
- LEO satellite network
- load balance
- resource allocation
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

# paper-1757 — Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of edge computing with LEO satellite broadband networks (LSBNs) offers a transformative potential, yet remains underexplored in the optimization of joint computation offloading and resource allocation (JCORA). This problem is compounded by the issues of load imbalance and hybrid action spaces. To tackle them, we firstly propose a multi-level edge computing architecture that leverages the inter-satellite links to enable collaborative offloading among neighboring satellites, thereby enhancing global resource utilization and load balance in LSBNs. Moreover, existing studies demonstrate the benefits of deep reinforcement learning (DRL) for JCORA optimization but struggle with the complexities of hybrid action spaces. To address this, we elaborate a novel hierarchical multi-agent DRL (HMADRL) framework that decomposes the JCORA problem into two-layered subproblems, namely global computation offloading and local resource allocation. This decomposition effectively mitigates the challenge posed by hybrid action spaces. The computation offloading subproblem is formulated as a delayed-reward partially observable Markov decision process, optimized by using multi-agent deep Q-networks specialized in discrete action outputs. Meanwhile, the resource allocation subproblem is addressed through the deep deterministic policy gradient model, adept at handling continuous actions. Extensive experiments validate our approach, demonstrating improvements in delay reduction, outrage rate, and load balancing compared to baselines. © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1757.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
