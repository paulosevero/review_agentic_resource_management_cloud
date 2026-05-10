---
id: paper-2304
title: 'Toward Energy-Efficiency: Integrating MATD3 Reinforcement Learning Method for Computational Offloading in RIS-Aided UAV-MEC Environments'
authors:
- Wu, Liangshun
- Zhang, Cong
- Zhang, Bin
- Du, Jianbo
- Qu, Junsuo
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3560835
url: https://www.scopus.com/pages/publications/105003371847?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 26582--26595
keywords:
- Concave-convex procedure (CCCP)
- mobile edge computing (MEC)
- multiagent twin delayed deep deterministic policy gradients
- reconfigurable intelligent surfaces (RIS)
- uncrewed aerial vehicles (UAVs)
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

# paper-2304 — Toward Energy-Efficiency: Integrating MATD3 Reinforcement Learning Method for Computational Offloading in RIS-Aided UAV-MEC Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the proliferation of Internet of Things (IoT) devices, there is an escalating demand for enhanced computing and communication capabilities. Mobile edge computing (MEC) addresses this need by relocating computing resources to the network edge, thereby delivering swifter and more efficient services. This article introduces a computation offloading and energy consumption optimization framework that leverages Reconfigurable intelligent surfaces (RIS), uncrewed aerial vehicles (UAVs), and MEC. The scheme aims to maximize energy efficiency through the optimization of task allocation, RIS phase shifts, and UAV trajectories. By employing the Multiagent twin delayed deep deterministic policy gradient (MATD3) reinforcement learning algorithm, this article further refines UAV trajectories and RIS configurations. The simulation results indicate that the proposed method surpasses the traditional Concave-convex procedure (CCCP) algorithm in both UAV trajectory control and RIS configuration, demonstrating quicker convergence and enhanced stability. The method proves to be adaptable to diverse environments and tasks, showcasing notable benefits in RIS-assisted interference suppression, particularly with large RIS, thereby enhancing UAV data reception rates. Additionally, MATD3 exhibits faster and smoother convergence for extended task durations and smaller RIS scenarios. Simulation results reveal that UAVs tend to move closer to RIS, with energy efficiency falling as IoT tasks increase, affirming the proposed algorithm’s high energy efficiency and effectiveness. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2304.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
