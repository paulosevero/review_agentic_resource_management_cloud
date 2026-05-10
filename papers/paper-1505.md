---
id: paper-1505
title: 'Optimizing computational efficiency in 6G IoT networks: a multi-agent deep reinforcement learning approach for multi-MEC systems'
authors:
- Darem, Abdulbasit A.
- Alhashmi, Asma A.
- Alanazi, Fawaz
- Alkhaldi, Tareq M.
- Alghawli, Abed Saif Ahmed
- Alalayah, Khaled M.
- Abdullah, Monir
venue: Journal of Supercomputing
venue_type: journal
year: 2025
doi: 10.1007/s11227-025-08003-1
url: https://www.scopus.com/pages/publications/105022611913?origin=resultslist
publisher: Springer
pages: ''
keywords:
- 6G Networks
- Energy-efficient offloading
- High-altitude platforms (HAPs)
- Internet of Things (IoT)
- Mobile edge computing (MEC)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1505 — Optimizing computational efficiency in 6G IoT networks: a multi-agent deep reinforcement learning approach for multi-MEC systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In future sixth-generation (6G) communication networks, the Internet of Things (IoT) is expected to play a crucial role, necessitating energy-efficient computation despite challenges such as limited battery life and resource constraints. Mobile edge computing (MEC) offers a promising solution by providing on-demand computation capabilities to low-power IoT devices. However, as the number of IoT devices increases, congestion and performance degradation can occur in single-MEC server systems. This study proposes a novel multi-MEC network architecture that leverages a realistic path loss model and a dynamic offloading strategy, incorporating both partial and binary offloading schemes to enhance computational energy efficiency. We formulate a joint optimization problem that addresses user association, offloading volume, offloading strategy, and the allocation of computational and communication resources. To solve this complex problem, we employ a multi-agent deep reinforcement learning (MADRL) approach using the multi-agent deep deterministic policy gradient (MADDPG) algorithm. Extensive simulations demonstrate that our proposed approach outperforms traditional algorithms such as deep Q-network (DQN), proximal policy optimization (PPO), and asynchronous advantage actor-critic (A3C), as well as conventional binary and partial offloading strategies. Numerical results reveal that our scheme improves performance by approximately 22.01% compared to the binary scheme and 8.26% compared to the partial offloading scheme. Furthermore, statistical analysis shows the effectiveness of the proposed framework, reducing outage probability to 0.01% at 30 dBm and achieving a task completion ratio of 99% with the deployment of 18 MEC servers. These results confirm the potential of MADRL-based methods to optimize resource allocation and enhance computational efficiency, paving the way for more resilient and effective frameworks to address the constraints of low-power IoT devices in future communication networks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1505.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
