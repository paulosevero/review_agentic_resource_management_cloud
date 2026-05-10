---
id: paper-0317
title: Multi-Agent Meta-Reinforcement Learning for Self-Powered and Sustainable Edge Computing Systems
authors:
- Munir, Md. Shirajum
- Tran, Nguyen H.
- Saad, Walid
- Hong, Choong Seon
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2021
doi: 10.1109/TNSM.2021.3057960
url: https://www.scopus.com/pages/publications/85100863396?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3353--3374
keywords:
- demand response
- meta-reinforcement learning
- Mobile edge computing (MEC)
- self-powered
- stochastic optimization
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

# paper-0317 — Multi-Agent Meta-Reinforcement Learning for Self-Powered and Sustainable Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The stringent requirements of mobile edge computing (MEC) applications and functions fathom the high capacity and dense deployment of MEC hosts to the upcoming wireless networks. However, operating such high capacity MEC hosts can significantly increase energy consumption. Thus, a base station (BS) unit can act as a self-powered BS. In this article, an effective energy dispatch mechanism for self-powered wireless networks with edge computing capabilities is studied. First, a two-stage linear stochastic programming problem is formulated with the goal of minimizing the total energy consumption cost of the system while fulfilling the energy demand. Second, a semi-distributed data-driven solution is proposed by developing a novel multi-agent meta-reinforcement learning (MAMRL) framework to solve the formulated problem. In particular, each BS plays the role of a local agent that explores a Markovian behavior for both energy consumption and generation while each BS transfers time-varying features to a meta-agent. Sequentially, the meta-agent optimizes (i.e., exploits) the energy dispatch decision by accepting only the observations from each local agent with its own state information. Meanwhile, each BS agent estimates its own energy dispatch policy by applying the learned parameters from meta-agent. Finally, the proposed MAMRL framework is benchmarked by analyzing deterministic, asymmetric, and stochastic environments in terms of non-renewable energy usages, energy cost, and accuracy. Experimental results show that the proposed MAMRL model can reduce up to 11% non-renewable energy usage and by 22.4% the energy cost (with 95.8% prediction accuracy), compared to other baseline methods. © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0317.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
