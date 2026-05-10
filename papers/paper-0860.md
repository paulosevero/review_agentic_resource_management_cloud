---
id: paper-0860
title: Human-Aware Dynamic Hierarchical Network Control for Distributed Metaverse Services
authors:
- Chen, Qimei
- Li, Ruixue
- Xu, Xiaoxia
- Wu, Jing
- Jiang, Hao
- Qiu, Meikang
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2024
doi: 10.1109/JSAC.2023.3345399
url: https://www.scopus.com/pages/publications/85184814384?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 629--642
keywords:
- distributed coordination
- dynamic network control
- Human-aware
- metaverse
- multi-agent
- NR-U
- RIS
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0860 — Human-Aware Dynamic Hierarchical Network Control for Distributed Metaverse Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Metaverse has emerged as a revolutionary technique for transforming the way people interact with digital content, which relies on a distributed computing and communication infrastructure, encompassing terminal users, edge servers, and cloud servers. However, the rapid evolution of the Metaverse presents challenges that surpass the capabilities of existing communication and network infrastructures, particularly on network bandwidth and latency. Additionally, human experience becomes a critical factor in this domain. Therefore, we introduce a human-aware hierarchical software defined network (SDN) architecture consisting of a Metaverse cloud layer, a mobile edge computing (MEC) server empowered edge layer, and a distributed terminal layer. Each MEC server dynamically controls a multi-antenna base station (BS) and several reconfigurable intelligent surfaces (RISs) according to the terminal immersive experience requirements in real-time. To overcome the bandwidth limitation, we propose a novel smart reconfigurable spatial reuse new radio in unlicensed spectrum (NR-U) framework, which can realize customizable communications through flexibly and coordinately reconfiguring beams among the coordination between BSs and RISs. The objective function is formulated as a Lyapunov optimization based decentralized partially-observable Markov decision process (Dec-POMDP) problem to maximize the spectral efficiency while guaranteeing the latency and reliability requirements in Metaverse, via a joint user selection, phase-shift control, and beam coordination strategy. To solve the above non-convex, strongly coupled, and mixed integer nonlinear programming (MINLP), we propose a novel multi-agent hierarchical deep reinforcement learning (MAHDRL) algorithm that integrates deep Q-network (DQN) to solve discrete problems, deep deterministic policy gradient (DDPG) to solve continuous problems, and mixing network to capture complex interactions between multiple agents. Numerical results demonstrate the effectiveness of the proposed algorithm and verify the performance improvements compared to traditional multi-agent deep reinforcement learning (MADRL) algorithms.  © 1983-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0860.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
