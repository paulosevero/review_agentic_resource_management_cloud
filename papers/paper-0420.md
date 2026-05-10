---
id: paper-0420
title: Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning
authors:
- Guo, Yingya
- Ma, Yulong
- Luo, Huan
- Wu, Jianping
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2022
doi: 10.1109/TNSE.2022.3172283
url: https://www.scopus.com/pages/publications/85129633172?origin=resultslist
publisher: IEEE Computer Society
pages: 2870--2881
keywords:
- deep reinforcement learning
- egress selection
- Inter-DC WAN
- routing optimization
- traffic engineering
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0420 — Traffic Engineering in a Shared Inter-DC WAN via Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To reduce the investment on network infrastructure, many online service providers have begun to adopt the shared inter-DataCenter Wide Area Network (inter-DC WAN) that connects different datacenters and Internet Service Providers (ISPs). The shared inter-DC WAN accommodates two kinds of traffic, i.e. delay-sensitive ISP-facing traffic and high-throughput inter-DC traffic. Traffic Engineering (TE) in the shared inter-DC WAN should determine the routing paths for all traffic to achieve link load balancing, while select lower-latency egress routers for ISP-facing traffic to guarantee the Quality of Service (QoS). Therefore, this paper mainly focuses on jointly optimizing routing paths selection and egress router selection to strike a balance between QoS and link load balancing. Specifically, we first formulate the TE problem in the shared inter-DC WAN as a mixed integer nonlinear programming problem. Then, a TED method is proposed to jointly optimize the egress router selection and routing path selection by learning an intelligent agent with Deep Reinforcement Learning (DRL). The learnt agent can self-adaptively and rapidly select the optimal egress routers by considering the utilization-latency balance when traffic demand changes. Finally, we conduct extensive evaluations on Alibaba WAN with real traffic traces to demonstrate the effectiveness and superiority of the proposed method.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0420.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
