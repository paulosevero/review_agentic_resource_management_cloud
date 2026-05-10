---
id: paper-2899
title: Transformer-Based Scalable Multi-Agent Reinforcement Learning for Joint Resource Optimization in Cloud–Edge–End Video Streaming Systems
authors:
- Yuan, Shijing
- Chen, Xiang
- Xing, Suchuan
- Li, Jie
- Chen, Hongyang
- Liu, Zhi
- Guo, Song
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2025.3612689
url: https://www.scopus.com/pages/publications/105017136359?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3482--3496
keywords:
- multi-agent reinforcement learning
- potential game
- resource allocation
- transformer
- Video streaming
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

# paper-2899 — Transformer-Based Scalable Multi-Agent Reinforcement Learning for Joint Resource Optimization in Cloud–Edge–End Video Streaming Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-edge-end (CEE) collaboration has demonstrated significant potential in video streaming analysis. However, dynamic wireless environments, lack of incentive mechanisms, and constrained resources (e.g., transmission power, bandwidth, and computing resources) remain the primary bottlenecks for achieving efficient CEE-based video processing. To address these challenges, this paper focuses on a multi-user CEE scenario with dynamic wireless channels and investigates the joint optimization of adaptive incentives, cooperative offloading, and resource allocation. We propose a novel framework, called JROC, to motivate edge devices (EDs) to participate in collaborative computation within CEE, thereby enhancing system utility. Specifically, JROC encompasses a smart contract-based adaptive incentive mechanism and an Adaptive Transformer-based multi-agent reinforcement Learning Algorithm (ATLA). The incentive mechanism leverages blockchain to ensure trustworthy and automated incentive distribution, while ATLA captures long-term dependencies and global state features among agents to guide video tasks in dynamic environments through adaptive compression, cooperative offloading, and resource allocation. Moreover, we discuss key steps for deploying the proposed algorithm in a real CEE prototype, including lightweight actor inference at the terminal side and training at the edge. Experimental results based on a real-world operator dataset show that, compared to existing methods, JROC achieves higher long-term system utility while maintaining favorable scalability, thereby validating its effectiveness in resource-constrained and under-incentivized CEE video streaming scenarios. © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2899.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
