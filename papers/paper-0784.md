---
id: paper-0784
title: 'IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning'
authors:
- Yu, Jiadong
- Li, Yang
- Liu, Xiaolan
- Sun, Bo
- Wu, Yuan
- Hin-Kwok Tsang, Danny
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2023
doi: 10.1109/TWC.2022.3224291
url: https://www.scopus.com/pages/publications/85144061172?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4296--4312
keywords:
- deep deterministic policy gradient
- IRS
- mobile edge computing
- NOMA
- reinforcement learning
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

# paper-0784 — IRS Assisted NOMA Aided Mobile Edge Computing with Queue Stability: Heterogeneous Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> By employing powerful edge servers for data processing, mobile edge computing (MEC) has been recognized as a promising technology to support emerging computation-intensive applications. Besides, non-orthogonal multiple access (NOMA)-aided MEC system can further enhance the spectral efficiency with massive tasks offloading. However, with more dynamic devices brought online and the uncontrollable stochastic channel environment, it is even desirable to deploy appealing technique, i.e., intelligent reflecting surfaces (IRS), in the MEC system to flexibly tune the communication environment and improve the system energy efficiency. In this paper, we investigate the joint offloading, communication and computation resource allocation for the IRS-assisted NOMA MEC system. We first formulate a mixed integer energy efficiency maximization problem with system queue stability constraint. We then propose the Lyapunov-function-based Mixed Integer Deep Deterministic Policy Gradient (LMIDDPG) algorithm which is based on the centralized reinforcement learning (RL) framework. To be specific, we design the mixed integer action space mapping which contains both continuous mapping and integer mapping. Moreover, the award function is defined as the upper-bound of the Lyapunov drift-plus-penalty function. To enable end devices (EDs) to choose actions independently at the execution stage, we further propose the Heterogeneous Multi-agent LMIDDPG (HMA-LMIDDPG) algorithm based on distributed RL framework with homogeneous EDs and heterogeneous base station (BS) as heterogeneous multi-agent. Numerical results show that our proposed algorithms can achieve superior energy efficiency performance to the benchmark algorithms while maintaining the queue stability. Specially, the distributed structure HMA-LMIDDPG can acquire more energy efficiency gain than the centralized structure LMIDDPG.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0784.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
