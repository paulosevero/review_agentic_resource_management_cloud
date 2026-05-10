---
id: paper-2536
title: MADDPG-based edge offloading algorithm assisted by vehicle clustering and UAV trajectory optimization; [车辆聚类及UAV轨迹优化辅助下基于MADDPG的边缘卸载算法]
authors:
- Chen, Geng
- Xia, Conghui
- Kong, Lingzhi
- Zeng, Qingtian
venue: Tongxin Xuebao/Journal on Communications
venue_type: journal
year: 2026
doi: 10.11959/j.issn.1000-436x.2026058
url: https://www.scopus.com/pages/publications/105035012557?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 137--155
keywords:
- clustering mechanism
- edge offloading
- multi-agent learning
- trajectory optimization
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

# paper-2536 — MADDPG-based edge offloading algorithm assisted by vehicle clustering and UAV trajectory optimization; [车辆聚类及UAV轨迹优化辅助下基于MADDPG的边缘卸载算法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In order to solve the problems of overload of roadside units and blind area coverage of ground nodes in existing edge computing, a multi-agent deep deterministic policy gradient (MADDPG)-based edge offloading optimization algorithm assisted by vehicle clustering and unmanned aerial vehicle (UAV) trajectory optimization (VCTOEM) was proposed. Firstly, a "vehicle-road-air" joint edge offloading system was constructed, and a multi-objective optimization model was established. Secondly, a vehicle clustering mechanism was designed to aggregate vehicles with remaining resources into groups. In addition, an improved particle swarm optimization (PSO) algorithm was introduced to optimize the trajectory of UAV, ensuring efficient coverage of ground computing power blind spots while reducing flight energy consumption and transmission delays during task offloading. Finally, a collaborative offloading algorithm based on multi-agent learning was designed for final decision-making. Simulation results showed that the proposed algorithm could effectively adapt to the dynamic changes in the network caused by high-speed vehicle movement, maintaining excellent convergence stability in high load scenarios. The average rewards were about 10.5, 29.7, 22.8, 9.1, 6.7 and 9.9 higher than the other six benchmark algorithms, respectively. © 2026, Editorial Board of Journal on Communications. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2536.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
