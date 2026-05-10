---
id: paper-1002
title: Multi-Agent Reinforcement Learning for Cooperative Task Offloading in Internet-of-Vehicles
authors:
- Lei, Yuchen
- Jiang, Kai
- Wang, Zhenning
- Cao, Yue
- Lin, Hai
- Chen, Liang
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2024
doi: 10.1109/WCNC57260.2024.10571109
url: https://www.scopus.com/pages/publications/85198828035?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- internet of vehicle
- mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1002 — Multi-Agent Reinforcement Learning for Cooperative Task Offloading in Internet-of-Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Internet of Vehicles (IoV) has witnessed a significant growth in the number of participants. This rapid expansion has increased demands for computing resources and quality of service (QoS), posing challenges for mobile edge computing (MEC) in the IoV domain. Efficiently allocating computing power to meet these service demands has become a crucial concern. Therefore, joint optimization of offloading decisions and power allocation is required to achieve the tradeoff between task latency and energy consumption. To address the above challenge, we propose a multi-agent reinforcement learning (MARL) method called multi-agent twin delayed deep deterministic policy gradient (MA-TD3) in this paper. Compared to its predecessor, multi-agent deep deterministic policy gradient (MADDPG), this algorithm improves performance and execution speed. It solves the slow convergence problem caused by Q-value overestimation and reduces the computational cost. The experimental results illustrate that the proposed algorithm reaches an observable performance improvement.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1002.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
