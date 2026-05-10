---
id: paper-2201
title: Incentivizing Crowdsourcing Workers via Social Networks in Edge Computing
authors:
- Tang, Wenjun
- Chen, Rong
- Zhang, Zhikang
- Guo, Shikai
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2024.3515145
url: https://www.scopus.com/pages/publications/85212088400?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5653--5665
keywords:
- crowdsourcing incentive
- Crowdsourcing worker collaboration
- edge computing
- graph matching network
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

# paper-2201 — Incentivizing Crowdsourcing Workers via Social Networks in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Crowdsourcing has proven to be an effective approach for leveraging collective intelligence to solve tasks. However, in edge computing environments, crowdsourcing platforms often face challenges such as insufficient worker participation and weak collaboration. Existing incentive mechanisms focus on individual contributions, which leads to inefficient collaboration and suboptimal resource utilization, particularly on resource-constrained edge devices. Furthermore, limited computational capacity and budget constraints hinder widespread participation, negatively impacting task performance and overall engagement. This paper introduces the Agent Cooperation Model (ACM), which enhances worker collaboration and task completion through a distributed, agent-based approach to task allocation. We also propose the Deep Reinforcement Learning-based Dynamic Worker Incentive Mechanism (DDWM) to optimize incentive distribution using social network data, ensuring more effective incentives and fostering greater participation and collaboration. Cooperation Optimization through Multi-Agent Reinforcement Learning (MARL), allowing ACM to dynamically improve resource allocation and cooperation efficiency. The expansion of high-influence worker incentives through DDWM, driving broader participation via social networks. Experiments conducted on real-world datasets confirm that ACM and DDWM consistently enhance worker collaboration and participation across diverse and complex social networks. Compared to other incentive methods, these models exhibit superior stability and convergence, particularly in larger and denser networks, validating the effectiveness of our approach in fostering efficient crowdsourcing cooperation. © 1975-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2201.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
