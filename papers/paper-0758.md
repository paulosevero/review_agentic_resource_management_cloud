---
id: paper-0758
title: A Two-Stage GCN-Based Deep Reinforcement Learning Framework for SFC Embedding in Multi-Datacenter Networks
authors:
- Xiao, Da
- Zhang, J. Andrew
- Liu, Xin
- Qu, Yiwen
- Ni, Wei
- Liu, Ren Ping
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2023
doi: 10.1109/TNSM.2023.3284293
url: https://www.scopus.com/pages/publications/85162655394?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4297--4312
keywords:
- graph convolutional network
- multi-agent
- multi-datacenter
- Network function virtualization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0758 — A Two-Stage GCN-Based Deep Reinforcement Learning Framework for SFC Embedding in Multi-Datacenter Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Network Function Virtualization (NFV), which decouples network functions from hardware and transforms them into Virtual Network Functions (VNFs), is a crucial technology for data center (DC) networks. A service function chain (SFC) is composed of an ordered set of VNFs and virtual links (VLs) connecting them. To optimize the resource allocation in DC networks, we need to efficiently map SFCs onto the physical network. Nevertheless, the dynamics and diversity of SFC requests in multi-datacenter (MDC) networks pose a significant challenge in embedding SFCs. To overcome this challenge, we design a two-stage graph convolutional network (GCN) assisted deep reinforcement learning (DRL) scheme. This framework aims to maximize the overall acceptance ratio of SFC requests while minimizing the total cost in an MDC network. In the first stage, we propose a GCN-based DRL algorithm as a coarse granularity solution to the SFC embedding problem from the macro perspective. This solution outlines a local observation scope (LOS) for each agent in the multi-agent system of the second stage, where all agents simultaneously handle SFC requests from their respective DCs using a multi-agent framework from the micro perspective. Numerical evaluations show that, compared to state-of-the-art methods, the proposed scheme improves the acceptance ratio by approximately 13% compared with the Kolin algorithm and 18% compared with the DQN algorithm and saves the cost by around 28% compared with the Kolin and the DQN.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0758.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
