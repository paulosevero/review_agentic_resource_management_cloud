---
id: paper-0863
title: Multi-Agent Deep Reinforcement Learning for Computation Offloading in Multi-IRS Assisted Mobile Edge Computing Networks
authors:
- Chen, Lingxiao
- Li, Xiuhua
- Sun, Chuan
- Fan, Qilin
- Wang, Xiaofei
- Leung, Victor C. M.
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2024
doi: 10.1109/WCNC57260.2024.10570561
url: https://www.scopus.com/pages/publications/85198853232?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Data communication systems
- Data transfer
- Deep learning
- Mobile edge computing
- Multi agent systems
- Reinforcement learning
- Computation offloading
- Data-transmission
- Multi agent
- Network edges
- Potential technologies
- Reflecting surface
- Reinforcement learnings
- Task executions
- Transmission security
- User devices
- Computation offloading
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

# paper-0863 — Multi-Agent Deep Reinforcement Learning for Computation Offloading in Multi-IRS Assisted Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) as a potential technology can offload tasks from user devices (UDs) to network edges to alleviate network congestion and reduce task execution delay. However, computation offloading faces two challenges: 1) Poor wireless channel quality causes high transmission delay; 2) Computing tasks may be obtained by eavesdroppers (Eves) during task offloading. Therefore, we consider deploying intel-ligent reflecting surface (IRS) in MEC networks to increase data transmission rate and ensure data transmission security. This paper investigates the issue of joint computation offloading and resource allocation in a multi-IRS assisted MEC network. Our goal is to minimize task execution delay. To address this problem, we propose a multi-agent deep deterministic policy gradient algorithm to determine the optimal offloading strategy for each UD. Simulation results show that the proposed algorithm can significantly reduce task execution delay and ensure data transmission security.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0863.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
