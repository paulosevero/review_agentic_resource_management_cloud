---
id: paper-1238
title: Actor-Critic Deep RL for Vehicular Edge Computing Optimization
authors:
- Wang, Bingxin
- Tu, Dan
- Wang, Jie
venue: 20th International Wireless Communications and Mobile Computing Conference, IWCMC 2024
venue_type: conference
year: 2024
doi: 10.1109/IWCMC61514.2024.10592616
url: https://www.scopus.com/pages/publications/85199992085?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 291--295
keywords:
- Deep Reinforcement Learning (DRL)
- Multi-Agent Systems
- Resource Allocation
- Task Offloading
- Vehicular Edge Computing (VEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1238 — Actor-Critic Deep RL for Vehicular Edge Computing Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing (VEC) seeks adept task offloading strategies to streamline resource allocation and elevate vehicular application performance. This paper delves into scrutinizing the effectiveness of an Actor-Critic-based Multi-Agent Deep Reinforcement Learning (MADRL) framework in orchestrating cost-minimized task offloading within VEC domains. Embracing the MADRL paradigm, this framework empowers adaptive decision-making for task allocation and execution in highly dynamic vehicular environments. By integrating deep reinforcement learning methodologies into multi-agent systems, the study endeavors to bolster the efficiency of task offloading strategies operating within VEC realms. The research emphasizes MADRL's role in fostering agile and responsive task allocation paradigms within VEC, aiming to optimize resource utilization while curtailing costs associated with task execution. Through adaptive decision mechanisms, MADRL facilitates dynamic task allocation, enabling vehicles to seamlessly distribute computational tasks among onboard systems and proximal edge resources. This exploration illuminates the potential of MADRL-based strategies in refining task offloading efficiency, presenting a promising avenue for enhancing VEC's computational resource management and overall performance.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1238.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
