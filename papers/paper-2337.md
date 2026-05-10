---
id: paper-2337
title: 'MADRL-Based Edge Computing: Joint Energy-Latency Optimization for Marine Internet of Things'
authors:
- Xu, Weijian
- Luo, Wenqian
- Sun, Yanglong
- Gao, Zhibin
- Wu, Bing
- Lai, Lianyou
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3570031
url: https://www.scopus.com/pages/publications/105005170462?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 30228--30241
keywords:
- Edge computing
- Marine Internet of Things (MIoT)
- multiagent deep reinforcement learning (MADRL)
- task offloading
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

# paper-2337 — MADRL-Based Edge Computing: Joint Energy-Latency Optimization for Marine Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) technology has facilitated the deployment of high computational algorithms on Marine Internet of things (MIoT) devices that equipped with limited computing resources. However, the dynamic changes in the network environment, the strict requirements of system latency and energy consumption of mobile devices, restrict the task execution in MIoT. This article proposes an offloading framework in a marine MEC scenario, which is assisted by sea buoys and uncrewed aerial vehicles (UAVs). Aiming to achieve long-term system optimization goals under resource-constrained conditions, with task partitioning, user scheduling, and resource allocation joint optimization under the constraints of UAV residual battery life, system latency, and energy consumption. This article specifically introduces a network partition point reservation algorithm (NPPR) that reduces the solution space of the problem through preprocessing. Subsequently, this article presents a multiagent deep deterministic policy gradient (MADDPG) algorithm, enhanced with standardization and adaptive learning rate decay (SA-MADDPG), to address task heterogeneity and environmental dynamics. Simulation results demonstrate that, compared to existing algorithms, the SA-MADDPG algorithm proposed in this article reduces system latency and energy consumption by 34.7% and 61.2%, respectively. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2337.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
