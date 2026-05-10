---
id: paper-1464
title: Defending Against APT Attacks in Cloud Computing Environments Using Grouped Multiagent Deep Reinforcement Learning
authors:
- Chen, Jialin
- Lan, Xiaolong
- Zhang, Qingquan
- Ma, Wengang
- Fang, Wenbo
- He, Junjiang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3542119
url: https://www.scopus.com/pages/publications/85218722494?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19459--19470
keywords:
- Advanced persistent threat (APT)
- cloud security
- deep reinforcement learning (RL)
- multiagent systems
- resource allocation strategy
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1464 — Defending Against APT Attacks in Cloud Computing Environments Using Grouped Multiagent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Advanced persistent threats (APTs) pose a significant challenge to cloud computing security in the evolving landscape of cyber threats. Traditional defense models rely heavily on the attacker’s historical attack information, which greatly limits the effectiveness of actually dealing with APT attacks. To address this issues, we investigate an attack-defense game model in clouding computing environments, where multiple attackers and multiple defenders are supposed to compete for resource allocation on the cloud servers. In order to develop more effective defense strategies, we formulate the optimization problem to maximize the average rewards of defenders under constraints of the maximum available resource and acceptable cost. To solve this, we propose to use the multiagent deep reinforcement learning (RL) method to cope with the high uncertainty and dynamics of attack behavior. Then it is proposed to divide all defenders into cooperative groups and allow defenders within each group can jointly optimize the defense strategy through sharing information and experience. On this basis, we propose a novel grouped multiagent deep RL defense (GMADRLD) algorithm, which can effectively mitigate the issue of state space explosion while achieving good defense effect. Simulation results not only demonstrate the effectiveness of the proposed GMADRLD algorithm in dealing with the attacker’s ever-changing strategies, but also show that it is able to strike a balance between defense performance and computational complexity. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1464.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
