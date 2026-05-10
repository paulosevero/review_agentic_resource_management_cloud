---
id: paper-2597
title: Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing
authors:
- He, Yifan
- Xu, Zhan
- Lin, Jian
- Li, Yuanzhuang
- Zhang, Shiyu
venue: Neurocomputing
venue_type: journal
year: 2026
doi: 10.1016/j.neucom.2026.133115
url: https://www.scopus.com/pages/publications/105030879198?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Dynamic workflow scheduling
- Fog computing
- Genetic programming
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

# paper-2597 — Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic workflow scheduling in distributed fog computing (DWSDFC) is a critical optimization problem with significant implications for meeting the computational demands of modern applications. The dynamic and distributed nature of DWSDFC renders it a highly challenging task, particularly difficult to address using traditional scheduling methods. Recently, deep reinforcement learning (DRL) has emerged as a powerful solution for dynamic scheduling problems, selecting appropriate scheduling rules as actions at various decision points. The effectiveness of DRL is largely determined by these scheduling rules. However, these scheduling rules are often manually designed and require substantial domain expertise. For this reason, this study concentrates on automating the design of DRL actions to boost its problem-solving performance. First, DWSDFC is formulated as a decentralized partially observable Markov decision process. Then, a multi-agent DRL framework is proposed, incorporating a routing agent and a sequencing agent to tackle DWSDFC. Specifically, the actions in the sequencing agent are generated using an evolutionary algorithm known as genetic programming (GP). To enhance the diversity of this evolved action set and consequently the performance of DRL, a niching technique based on behavioral differences between actions is integrated into GP. Extensive experimental results on a variety of DWSDFC instances demonstrate the effectiveness of the proposed method over common scheduling rules as well as the state-of-the-art DRL and GP methods. © 2026 Elsevier B.V.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2597.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
