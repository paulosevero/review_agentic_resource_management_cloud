---
id: paper-1179
title: Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming
authors:
- Shao, Ziling
- Yang, Helin
- Xiao, Liang
- Su, Wei
- Chen, Yifan
- Xiong, Zehui
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2024.3432491
url: https://www.scopus.com/pages/publications/85200241000?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13358--13374
keywords:
- Anti-jamming
- deep reinforcement learning
- energy and latency minimization
- mobile edge computing
- resource management
- unmanned aerial vehicle
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

# paper-1179 — Deep Reinforcement Learning-Based Resource Management for UAV-Assisted Mobile Edge Computing Against Jamming

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC) systems, multiple unmanned aerial vehicles (UAVs) can be utilized as aerial servers to provide computing, communication, and storage services for edge users, called UAV-assisted MEC, which has emerged as a promising technology to improve both the computing and communication performances. Unlike existing works without considering jamming attacks, we investigate a multi-UAV-assisted-MEC scenario under multiple malicious jammers and then propose a resource management approach with the objective of minimizing both the system energy consumption and latency. Due to the time-varying nature of communication environments, we design a multi-agent deep reinforcement learning (MADRL)-based resource management approach to dynamically adjust the CPU frequency, communication bandwidth, and channel access selection of UAVs to enhance the system performance against jamming attacks. On this basis, in order to enhance the algorithm learning efficiency, we propose a multi-agent twin-delayed deep deterministic policy algorithm in combination with the prioritized experience replay mechanism (PER-MATD3) to effectively search for the joint resource management strategy under high-dimensional state and action spaces, where the time-varying channel state information and imperfect attack behavior information are also effectively trained to improve the learning capacity and convergence speed. Simulation and experimental results verify that the proposed approach can significantly decrease the overall system latency (i.e., computing and communication latency) and energy consumption compared to other benchmark algorithms under different real-world settings.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1179.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
