---
id: paper-0124
title: Mobility-aware resource allocation in multi-access edge computing using deep reinforcement learning
authors:
- Din, Najamul
- Chen, Haopeng
- Khan, Daud
venue: Proceedings - 2019 IEEE Intl Conf on Parallel and Distributed Processing with Applications, Big Data and  Cloud Computing, Sustainable Computing and Communications, Social Computing and Networking,
  ISPA/BDCloud/SustainCom/SocialCom 2019
venue_type: conference
year: 2019
doi: 10.1109/ISPA-BDCloud-SustainCom-SocialCom48970.2019.00038
url: https://www.scopus.com/pages/publications/85085499734?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 202--209
keywords:
- Deep q-network
- Deep reinforcement learning
- Multi-access edge computing
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

# paper-0124 — Mobility-aware resource allocation in multi-access edge computing using deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (also known as Multi-access Edge Computing) brings computation and storage resources to the edge of a mobile network, allowing mobile devices (MDs) to offload high demanding tasks while meeting strict delay requirements. In this paper, we study the problem of efficient allocation of computational resources while considering the mobility information using deep reinforcement learning. An optimal policy considering the dynamics of the network is very difficult to achieve. Our objective is to develop an intelligent agent to optimize the decision-making process and the allocation of resources. To address this problem, we have proposed a solution based on the Deep Reinforcement Learning(DRL) method. DRL implements a deep Q-network that can consider a long-term goal and learns from the experience. The proposed method also considers the time-varying workloads of MEC servers and learns a policy to transfer tasks from one MEC server to another which further maximizes the system gain by avoiding unnecessary queue waiting time. The results of the simulation show that our proposed scheme reduces the cost of the system considerably as compared to the other baselines. © 2019 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0124.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
