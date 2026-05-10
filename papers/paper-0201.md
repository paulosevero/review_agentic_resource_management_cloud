---
id: paper-0201
title: 'DeepHop on Edge: Hop-by-hop Routing byDistributed Learning with Semantic Attention'
authors:
- He, Bo
- Wang, Jingyu
- Qi, Qi
- Sun, Haifeng
- Zhuang, Zirui
- Liu, Cong
- Liao, Jianxin
venue: ACM International Conference Proceeding Series
venue_type: conference
year: 2020
doi: 10.1145/3404397.3404425
url: https://www.scopus.com/pages/publications/85090579496?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- distributed routing
- multi-agent reinforcement learning
- self-attention
- wireless edge networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0201 — DeepHop on Edge: Hop-by-hop Routing byDistributed Learning with Semantic Attention

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access Edge Computing (MEC) and ubiquitous smart devices help serve end-users efficiently and optimally through providing emerging edge-deployed services. Meanwhile, heavy and time-varying traffic loads are produced in the edge network, so that an efficient traffic forwarding mechanism is required. In this paper, we propose a parallel and distributed learning approach, DeepHop, to adapt to the volatile environments and realize hop-by-hop routing. The Multi-Agent Deep Reinforcement Learning (MADRL) is used to alleviate the edge network congestion and maximize the utilization of network resources. DeepHop determines the routing among edge network nodes for heterogeneous types of traffic according to the current workload and capability. By joining with an attention mechanism, DeepHop obtains the semantics from the elements of the network state to help the agents learn the importance of each element on routing. Experiment results show that DeepHop achieves the increase of successfully transmitted packets by 15% compared with the state-of-the-art algorithms. Besides, DeepHop with an attention mechanism reduces convergence time by nearly half compared with the common-used structures of neural networks. © 2020 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0201.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
