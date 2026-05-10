---
id: paper-0254
title: Cross-Domain Resource Orchestration for the Edge-Computing-Enabled Smart Road
authors:
- Yuan, Quan
- Li, Jinglin
- Zhou, Haibo
- Luo, Guiyang
- Lin, Tao
- Yang, Fangchun
- Shen, Xuemin Sherman
venue: IEEE Network
venue_type: journal
year: 2020
doi: 10.1109/MNET.011.2000007
url: https://www.scopus.com/pages/publications/85091804040?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 60--67
keywords:
- Decision making
- Deep learning
- Edge computing
- Highway planning
- Iterative methods
- Learning systems
- Multi agent systems
- Reinforcement learning
- Roads and streets
- Computing infrastructures
- Fundamental research
- Information domains
- Reinforcement learning method
- Resource optimization
- Safety and efficiencies
- Transportation domain
- Transportation system
- Road vehicles
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0254 — Cross-Domain Resource Orchestration for the Edge-Computing-Enabled Smart Road

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent driving plays a role in significantly improving the safety and efficiency of transportation systems. As the onboard capabilities of perception, comprehension, and decision making are limited, vehicles can employ the edge computing infrastructure of the smart road to enhance their intelligence. Therefore, the smart road is considered an intelligent Internet of Things system. It provides vehicles with not only the road space in the transportation domain, but also the communication, sensing, and computing resources in the information domain to improve the composite quality of intelligent driving. However, the resources in the information and transportation domains are complicatedly coupled, and the orchestration of these cross-domain resources is confronted with the huge state-action space, which cannot be solved in a real-time manner. In this article, we investigate the fundamental research challenges in cross-domain resource orchestration for the smart road, and design a multi-agent-based framework. Within the framework, each vehicle is associated with an exclusive agent on the edge cloud, and the agents utilize swarm intelligence to jointly optimize the traffic flow and information flow for their respective vehicles. Specifically, a value iteration network is used by agents to learn the routing behavior of vehicles, and a multi-agent deep reinforcement learning method is proposed, enabling agents to cooperatively learn decentralized resource optimization policies. To verify the effectiveness of the proposed framework, a cross-domain resource orchestration prototype is implemented and evaluated.  © 1986-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0254.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
