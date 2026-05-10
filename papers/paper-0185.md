---
id: paper-0185
title: Artificial Intelligence Aided Joint Bit Rate Selection and Radio Resource Allocation for Adaptive Video Streaming over F-RANs
authors:
- Chen, Jienan
- Wei, Zhongxiang
- Li, Shuai
- Cao, Bin
venue: IEEE Wireless Communications
venue_type: journal
year: 2020
doi: 10.1109/MWC.001.1900351
url: https://www.scopus.com/pages/publications/85084793879?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 36--43
keywords:
- Deep learning
- Long short-term memory
- Multi agent systems
- Multimedia services
- Quality of service
- Radio
- Radio access networks
- Reinforcement learning
- Resource allocation
- Video streaming
- Accurate prediction
- Adaptive video streaming
- Computing capacity
- Conventional optimization
- Cross layer optimization
- Multi-user scenario
- Network environments
- Radio resource allocation
- Fog computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0185 — Artificial Intelligence Aided Joint Bit Rate Selection and Radio Resource Allocation for Adaptive Video Streaming over F-RANs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, fog-computing-based radio access networks (F-RANs) have been conceptualized to provide high quality of experience (QoE) for adaptive bit rate (ABR) streaming, where additional computing capacity is supplemented on fog nodes to facilitate complicated cross-layer optimization (i.e., joint bit rate selection and radio resource allocation). However, finding an optimal global solution with acceptable complexity is still infeasible by the conventional optimization methods. In this work, we propose an artificial intelligence (AI) aided joint bit rate selection and radio resource allocation scheme referred to as iABR, which provides a new vision for handling the over-complicated optimization in F-RANs. Based on multi-agent hierarchy deep reinforcement learning, the proposed iABR can dynamically allocate radio resource and select bit rate in a multiuser scenario, by perceiving the network environment and clients' player information. Moreover, long short-term memory (LSTM) is employed by the iABR algorithm, which enables accurate prediction of the change of channel quality by learning the history of the wireless channel. Hence, iABR is able to adjust the action policy in advance to accommodate the future channel quality for avoiding bit rate fluctuation. According to the experimental results, the iABR exhibits higher QoE in terms of high average bit rate, low rebuffering ratio, and average bit rate variance. Last but not least, the QoE performance of all the clients are fairly guaranteed by the iABR algorithm, enhancing the practicality of AI-driven F-RANs for multimedia service delivery. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0185.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
