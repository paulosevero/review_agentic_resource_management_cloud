---
id: paper-0607
title: Hypergraph convolution mix DDPG for multi-aerial base station deployment
authors:
- He, Haoran
- Zhou, Fanqin
- Zhao, Yikun
- Li, Wenjing
- Feng, Lei
venue: Journal of Cloud Computing
venue_type: journal
year: 2023
doi: 10.1186/s13677-023-00556-x
url: https://www.scopus.com/pages/publications/85178945637?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Aerial base station (AeBS)
- Hypergraph convolution (HGCN)
- Multi-agent deep reinforcement learning (MADRL)
- Value decomposition, energy efficiency optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0607 — Hypergraph convolution mix DDPG for multi-aerial base station deployment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aerial base stations (AeBS), as crucial components of air-ground integrated networks, can serve as the edge nodes to provide flexible services to ground users. Optimizing the deployment of multiple AeBSs to maximize system energy efficiency is currently a prominent and actively researched topic in the AeBS-assisted edge-cloud computing network. In this paper, we deploy AeBSs using multi-agent deep reinforcement learning (MADRL). We describe the multi-AeBS deployment challenge as a decentralized partially observable Markov decision process (Dec-POMDP), taking into consideration the constrained observation range of AeBSs. The hypergraph convolution mix deep deterministic policy gradient (HCMIX-DDPG) algorithm is designed to maximize the system energy efficiency. The proposed algorithm uses the value decomposition framework to solve the lazy agent problem, and hypergraph convolutional (HGCN) network is introduced to strengthen the cooperative relationship between agents. Simulation results show that the suggested HCMIX-DDPG algorithm outperforms alternative baseline algorithms in the multi-AeBS deployment scenario. © 2023, The Author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0607.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
