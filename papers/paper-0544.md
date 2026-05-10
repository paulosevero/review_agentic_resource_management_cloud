---
id: paper-0544
title: 'When Multi-access Edge Computing Meets Multi-area Intelligent Reflecting Surface: A Multi-agent Reinforcement Learning Approach'
authors:
- Zhuang, Shen
- He, Ying
- Yu, F. Richard
- Gao, Chengxi
- Pan, Weike
- Ming, Zhong
venue: 2022 IEEE/ACM 30th International Symposium on Quality of Service, IWQoS 2022
venue_type: conference
year: 2022
doi: 10.1109/IWQoS54832.2022.9812883
url: https://www.scopus.com/pages/publications/85135378676?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Intelligent reflecting surface
- Multi-agent reinforcement learning
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

# paper-0544 — When Multi-access Edge Computing Meets Multi-area Intelligent Reflecting Surface: A Multi-agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, multi-access edge computing (MEC) is emerging to provide computation and storage capabilities to the Internet of things (IoT) devices to improve the quality of service (QoS) of IoT applications. In addition, intelligent reflecting surface (IRS) techniques have attracted great interests from both academia and industry to improve the communication efficiency. Although existing works leverage the IRS technique in MEC networks, they mainly focus on the single-IRS single-area scenario. However, in practice, multi-IRS will be deployed in multi-area scenarios in future networks. Consequently, considering the single-IRS single-area scenario will have inferior performance. In this paper, to address the aforementioned issue, we propose an efficient resource provisioning scheme for multi-IRS multi-area scenarios in MEC networks. We first model the problem as a cooperative multi-agent reinforcement learning process, where each agent manages one area and all agents share the network bandwidth and computation resources. Then, we propose a multi-agent actor-critic method with an attention mechanism for resource management with latency guarantee. Finally, we conduct extensive simulations to verify the effectiveness of the proposed scheme. Our scheme can reduce the required computation resources by up to 11.84% when compared with the benchmark works. It is also shown that our proposed scheme can improve the efficiency of resource allocation and scale well with the increasing demand from IoT devices.  © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0544.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
