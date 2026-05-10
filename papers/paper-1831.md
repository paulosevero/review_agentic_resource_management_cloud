---
id: paper-1831
title: 'Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method'
authors:
- Li, Shichao
- Lu, Bingji
- Ale, Laha
- Chen, Hongbin
- Tan, Fangqing
- Huang, Jingyue
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3548088
url: https://www.scopus.com/pages/publications/86000448616?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 21443--21456
keywords:
- Independent proximal policy optimization (IPPO)
- mobile edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- partial task offloading
- uncrewed aerial vehicles (UAVs) trajectory design
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

# paper-1831 — Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of mobile edge computing (MEC) and air-ground integrated network is viewed as a crucial technology for Internet of Remote Things (IoRT) devices. It provides widespread service coverage and allows the tasks of IoRT devices to be executed by the uncrewed aerial vehicles (UAVs) and the high altitude platforms (HAPs). In this article, we investigate a joint partial task offloading, resource allocation, and UAV trajectory design problem to minimize the total task offloading delay of all IoRT devices in the air-ground integrated MEC network. Given that the problem is nonconvex and hard to solve by the traditional methods, we convert it into a Markov decision process (MDP) and leverage the deep reinforcement learning method to address it. Considering the complexity of the MDP grows with the number of the IoRT devices and the UAVs increasing, the primal problem is decomposed into two subproblems: 1) the UAV trajectory design and IoRT device power control subproblem, and 2) the partial task offloading and resource allocation subproblem. To address these two subproblems, we apply the basic concepts of the multiagent deep deterministic policy gradient (MADDPG) and the independent proximal policy optimization (IPPO) methods, respectively. Additionally, we introduce the enhanced prioritized experience replay and noise value to improve both the convergence performance and rate. This leads to the development of the MADDPG-improved prioritized experience replay (MADDPG-IPER) algorithm and noise value-IPPO (NV-IPPO) algorithm. Based on the solution of these two subproblems, a joint partial task offloading, resource allocation, and UAV trajectory design (JPTORAUTD) algorithm is proposed. Simulation results present that the proposed JPTORAUTD algorithm outperforms other benchmark algorithms in terms of reducing the total task offloading delay. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1831.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
