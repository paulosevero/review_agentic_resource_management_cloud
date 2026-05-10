---
id: paper-0878
title: Decentralized computation offloading via multi-agent deep reinforcement learning for NOMA-assisted mobile edge computing with energy harvesting devices
authors:
- Daghayeghi, Atousa
- Nickray, Mohsen
venue: Journal of Systems Architecture
venue_type: journal
year: 2024
doi: 10.1016/j.sysarc.2024.103139
url: https://www.scopus.com/pages/publications/85190481127?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Energy harvesting
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Non-orthogonal multiple access
- Resource allocation
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

# paper-0878 — Decentralized computation offloading via multi-agent deep reinforcement learning for NOMA-assisted mobile edge computing with energy harvesting devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Supporting latency-sensitive and computation-intensive applications is hardly possible for mobile devices (MDs) with limited battery capacity and low computing resources. Therefore, mobile edge computing (MEC) and wireless power transfer (WPT) have emerged as promising technologies that allow MDs to offload part or all of their workloads to MEC servers and harvest energy for prolonging their battery lifetime. However, the MEC server's limited computing resources, available communication channel quality, and time-limited energy harvesting (EH) challenge the computation offloading. In this paper, we study the joint problem of decentralized computation offloading and resource allocation (JDCORA) in the environment of non-orthogonal multiple access (NOMA)-assisted MEC with multiple EH-enabled MDs. To learn decentralized offloading policies, we propose a multi-agent deep reinforcement learning (MADRL)-based scheme towards minimizing energy consumption and task completion time, which considers the cooperation between MDs to adjust their strategies. In particular, we improve the multi-agent deep deterministic policy gradient (MADDPG) by applying the features of double actors, double centralized critics, soft value estimation, critic regularization and proportional-based prioritized experience replay (pPER) and propose an algorithm called multi-agent twin actors regularized critics (MATARC). Simulation results demonstrate that the proposed MATARC has a better convergence performance compared to other baseline methods and also reduces the average energy consumption, task completion time and task drop rate. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0878.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
