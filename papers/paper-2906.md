---
id: paper-2906
title: Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing
authors:
- Zhang, Han
- Liang, Hongbin
- Ale, Laha
- Mao, Guotao
- Hong, Xintao
- Jia, Qiong
- Zhao, Dongmei
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2025.3602016
url: https://www.scopus.com/pages/publications/105014641042?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2209--2223
keywords:
- autonomous aerial vehicles
- Computation offloading
- deep reinforcement learning
- resource allocation
- vehicle edge computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2906 — Attention-Based Deep Reinforcement Learning for Joint Trajectory Planning and Task Offloading in AAV-Assisted Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of compute-intensive and delay-sensitive applications in the Internet of Vehicles (IoV) has brought new challenges to traditional Vehicle Edge Computing (VEC). Especially during peak traffic periods, fixed base stations (BSs), due to their static deployment and limited coverage, struggle to elastically scale computing resources to meet the dynamically changing computational demands of vehicular users, which to some extent affects the overall quality of service and efficiency of system resource utilization. In this paper, we propose a hybrid edge computing framework that integrates Autonomous Aerial Vehicles (AAVs) as mobile computing nodes to complement fixed base stations. For this AAV-BS hybrid edge computing environment, we design and optimize a computation offloading model considering heterogeneous task types and AAV trajectory planning. The proposed model tackles the joint optimization of system revenue, service delay, and energy consumption, while considering practical constraints such as AAV energy limitations and base station capacity. To address this multi-objective optimization challenge, we construct a Markov Decision Process (MDP) model and develop a multi-head self-attention enhanced Multi-Agent Deep Dirichlet Deterministic Policy Gradient (MHSA-MAD3PG) algorithm. The multi-head self-attention mechanism enables agents to capture complex dependencies and interactions in the environment, leading to more effective collaborative decision-making. Comprehensive simulation results demonstrate that our proposed approach achieves superior performance in terms of system revenue, service delay, and energy efficiency compared to baseline methods.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2906.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
