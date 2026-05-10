---
id: paper-1020
title: DRL-Based Joint Task Scheduling and Trajectory Planning Method for UAV-Assisted MEC Scenarios
authors:
- Li, Fan
- Gu, Cheng
- Liu, Dong-Sheng
- Wu, Yi-Xuan
- Wang, He-Xing
venue: IEEE Access
venue_type: journal
year: 2024
doi: 10.1109/ACCESS.2024.3479312
url: https://www.scopus.com/pages/publications/85207707400?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 156224--156234
keywords:
- deep deterministic policy gradient
- Mobile edge computing
- task offloading
- trajectory planning
- UAV
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

# paper-1020 — DRL-Based Joint Task Scheduling and Trajectory Planning Method for UAV-Assisted MEC Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proliferation of Internet of Things (IoT) devices has resulted in a massive increase in data generation, necessitating robust solutions for real-time data processing and analysis. The integration of Unmanned Aerial Vehicles (UAVs) with MEC systems presents a promising enhancement, providing dynamic, mobile edge computing capabilities that can adapt to changing conditions and demands. However, efficiently managing the task offloading and trajectory planning of UAVs in such scenarios poses significant challenges, particularly in maximizing coverage while minimizing time and energy consumption. In this context, this paper proposes a novel UAV-based MEC model utilizing the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) reinforcement learning algorithm to optimize task scheduling and UAV trajectory in real-time. Our model enables UAVs to function as mobile edge servers, dynamically processing and routing tasks between terminal devices and edge servers based on real-time device demands. By incorporating a sophisticated reward function that prioritizes the minimization of system costs-including energy, time, and throughput maximization-our approach not only enhances the operational efficiency of UAV-assisted MEC systems but also improves the quality and responsiveness of edge computing services. After training the MADDPG model in the simulated environment, the experiments show that our approach significantly improved the performance of UAV-assisted MEC systems in real-time scenarios, converging after 50 learning episodes and achieving 90% task completion rate.  © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1020.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
