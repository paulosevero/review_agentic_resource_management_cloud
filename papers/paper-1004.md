---
id: paper-1004
title: A Crowdsensing Service Pricing Method in Vehicular Edge Computing
authors:
- Li, Zheng
- Tang, Sizhe
- Tian, Hao
- Xiang, Haolong
- Xu, Xiaolong
- Dou, Wanchun
venue: Proceedings - 2024 IEEE International Symposium on Parallel and Distributed Processing with Applications, ISPA 2024
venue_type: conference
year: 2024
doi: 10.1109/ISPA63168.2024.00019
url: https://www.scopus.com/pages/publications/105000203221?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 82--89
keywords:
- crowdsensing
- game theory
- multi-agent reinforcement learning
- Vehicular edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1004 — A Crowdsensing Service Pricing Method in Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancements in vehicular networking technology have enabled onboard users to access a variety of emerging services like precise navigation and real-time hazard avoidance. However, as the diversity and volume of required data expand and demands intensify, most of vehicular services are unable to satisfy user expectations. Although crowdsensing architectures based on edge computing have been proposed in vehicular networks, how to optimally allocate the sensing service time of roadside units and set appropriate prices for services to maximize user benefits still remain significant challenges. To solve the above issue, in this paper, a crowdsensing service pricing method is proposed in vehicular edge computing. Specifically, a vehicular networking crowdsensing framework based on the edge computing is designed. Then, the optimization problem of perception time pricing during the crowdsensing process is modeled into a Stackelberg game and further the multi-agent deep deterministic policy gradient-based algorithm is employed to obtain the optimal pricing strategy with user profits maximization. Finally, simulation results demonstrate that the proposed method significantly increases the payoff for all participants during the crowdsensing process.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1004.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
