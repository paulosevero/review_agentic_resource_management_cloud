---
id: paper-1903
title: 'Vehicular Computing Power Networks for IoT-Driven Edge Intelligence: MA-DDPG-Based Robust Task Offloading and Resource Allocation'
authors:
- Liu, Yi
- Jiang, Li
- Yuen, Chau
- Zhang, Yan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3580736
url: https://www.scopus.com/pages/publications/105008556605?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 36868--36879
keywords:
- Edge intelligence
- Internet of Things (IoT)
- multiagent deep reinforcement learning (DRL)
- resource allocation
- robust task offloading
- vehicular computing power networks (VCPNs)
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

# paper-1903 — Vehicular Computing Power Networks for IoT-Driven Edge Intelligence: MA-DDPG-Based Robust Task Offloading and Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deep integration of Internet of Things (IoT) and vehicular networks demands ultrareliable, low-latency computing paradigms to support emerging applications like autonomous driving and smart traffic management. Existing mobile-edge computing (MEC) frameworks, however, struggle with dynamic resource heterogeneity, intermittent connectivity, and inefficient coordination among distributed nodes. To address these challenges, this article proposes vehicular computing power networks (VCPNs), an IoT-driven edge intelligence framework that orchestrates computational resources from mobile user equipments (MUEs), connected vehicles, and edge servers. We formulate a joint optimization problem to minimize end-to-end task latency by finding optimal task offloading decisions and resource allocation (e.g., CPU and bandwidth) policies under time-varying IoT channel conditions and node mobility. To enable decentralized coordination in IoT environment, we model the problem as a multiagent Markov decision process (MDP) and propose a multiagent deep deterministic policy gradient (MA-DDPG) algorithm in which agents (MUEs, vehicles, servers) collaboratively learn policies to optimize task scheduling and resource sharing. Furthermore, we design a robust MA-DDPG variant with error-resilient experience replay and channel-adaptive reward mechanisms to ensure reliable training under packet loss and unstable connectivity. Numerical results demonstrate that VCPN reduces average task latency and improves energy efficiency compared to federated MEC baselines. The proposed MA-DDPG algorithm achieves convergence stability in high-mobility scenarios, outperforming conventional deep reinforcement learning methods. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1903.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
