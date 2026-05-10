---
id: paper-2833
title: Proactive Resource Allocation in Time-Sensitive Mobile-Edge Computing Using LLM-Guided Hierarchical Multi-Agent Reinforcement Learning
authors:
- Wang, Cong
- Hao, Jianbao
- Peng, Sancheng
- Yuan, Ying
- Li, Guorui
- Wang, Guojun
venue: IEEE Network
venue_type: journal
year: 2026
doi: 10.1109/MNET.2025.3643160
url: https://www.scopus.com/pages/publications/105026362333?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Decision making
- Intelligent agents
- Internet of things
- Machine learning
- Macros
- Mobile edge computing
- Mobile telecommunication systems
- Multi agent systems
- Network layers
- Resource allocation
- Computing system
- Decisions makings
- Dynamic network environment
- Edge computing
- Language model
- Mobile communication technology
- Multi-agent reinforcement learning
- Resources allocation
- Semantic reasoning
- Semantics understanding
- Antennas
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2833 — Proactive Resource Allocation in Time-Sensitive Mobile-Edge Computing Using LLM-Guided Hierarchical Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of sixth-generation mobile communication technology, a huge intelligent society composed of billions of Internet of Things (IoT) devices is rapidly emerging. It results in mobile edge computing systems facing two challenges: limited resources and highly dynamic network environments. Recent advances in large language models (LLMs) show strong abilities in decision-making, semantic understanding, and reasoning. These abilities enable LLMs to improve global coordination and proactive scheduling in communication-computation integrated IoT systems. This paper proposes a novel semantics-enhanced hierarchical multi-agent reinforcement learning framework for uncrewed aerial vehicle-assisted mobile edge computing systems, which innovatively incorporates a pretrained LLM as the global situational awareness module in the macro-coordination layer. We design a spatio- temporal decision network that integrates a graph attention network and a temporal convolutional network, leveraging the semantic reasoning of LLM to enable proactive global resource allocation. To address the combinatorial explosion in decision spaces, we develop a heuristic-guided hypergraph network at the micro-execution layer to improve learning efficiency. Experimental results demonstrate that our proposed framework achieves a 21.3% reduction in the average age of information and a 12.5% improvement in task completion rate compared with classical hierarchical reinforcement learning models, showing clear advantages in both stability and overall performance. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2833.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
