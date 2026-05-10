---
id: paper-1545
title: MADDPG-Based Resource Allocation for Integrated Communication, Sensing and Computing in UAV-Assisted IoV Networks
authors:
- Du, Pengfei
- Xiao, Tingyue
- Cao, Haotong
- Qing, Chaojin
- Mumtaz, Shahid
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3633518
url: https://www.scopus.com/pages/publications/105022464860?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- ISAC
- MADDPG
- MEC
- re source allocation
- UAV-assisted IoV networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1545 — MADDPG-Based Resource Allocation for Integrated Communication, Sensing and Computing in UAV-Assisted IoV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integrated sensing and communication (ISAC) has emerged as a pivotal technology in the internet of vehicles (IoV) domain, particularly due to its rapid advancements. However, as IoV networks expand, they encounter numerous challenges, including the increased communication traffic, ele vated communication latency, and insufficient sensing capabilities in critical emergency scenarios. To tackle these challenges, we propose a multi-unmanned aerial vehicle (Multi-UAV) assisted ISAC framework that synergistically combines the UAV-assisted mobile edge computing (MEC) and radar sensing technologies. This framework allows for a comprehensive investigation into the interactions among sensing, communication and computation through a joint optimization approach. First, to achieve a balance between communication performance, economic expenditure and radar mutual information (MI), we propose a Cobb-Douglas utility function and integrate it with a multi-agent deep reinforcement learning algorithm, which jointly takes the access control, instance selection, task offloading, UAV transmit power, and computational resource into consideration. Second, we reformulate this mixed-integer nonlinear programming (MINLP) problem as a markov decision process (MDP), and then propose a multi-agent deep deterministic policy gradient (MADDPG)-based resource allocation algorithm, which focuses on the simultaneous improvement of both communication quality and sensing accuracy. Finally, extensive simulation results demonstrate that the proposed algorithm markedly outperforms the existing baseline algorithms, achieving reductions of 73% in processing delay and 44% in total cost. This work not only fills a critical gap in current UAV-assisted IoV networks but also sets a foundation for future research into integrated sensing and communication systems in large-scale vehicular networks.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1545.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
