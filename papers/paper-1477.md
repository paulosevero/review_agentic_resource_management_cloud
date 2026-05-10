---
id: paper-1477
title: 'MS_M2ATD3: A master-slave multi-agent reinforcement learning for energy-efficient task offloading in LEO satellite edge computing'
authors:
- Chen, Juan
- Chen, Yujie
- Wu, Zongling
- Tian, Di
- Zhong, Jie
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.103987
url: https://www.scopus.com/pages/publications/105012873453?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Multi-agent
- Resource allocation
- Satellite edge computing
- Task offloading
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

# paper-1477 — MS_M2ATD3: A master-slave multi-agent reinforcement learning for energy-efficient task offloading in LEO satellite edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low earth orbit (LEO) satellites can break through geographical constraints and achieve global wireless coverage. In this paper, we propose a LEO satellite edge-cloud computing network that provides computing resources for ground users. However, mobile LEO satellites and unstable communication make the task of offloading challenging. Recently, multi-agent deep reinforcement learning (MADRL) was introduced to solve the dynamic task offloading and resource allocation problem. Nevertheless, due to overestimating or underestimating the target network, traditional MADRL may have low convergence and stability. To address this problem, we propose the master–slave mutual estimation multi-agent based on the twin delayed deep deterministic policy gradient (MS_MATD3) algorithm. Specifically, the master agent is deployed on the satellite edge computing (SEC) server, taking into account server constraints and coordinating slave agents’ decisions. Meanwhile, multiple slave agents are distributed across user equipment (UE), carrying out specific task offloading operations. By combining the mutual estimation of Q-values among agents and the minimum estimate of the twin Q-network, multiple agents use a weighted approach to balance the overestimation and underestimation problems. Experimental results show that our proposed algorithm is superior to typical MADRL algorithms. It not only improves the convergence performance by 50% but also achieves significant improvements in reducing task completion latency and UE's energy consumption. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1477.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
