---
id: paper-1483
title: 'Service migration with edge collaboration: Multi-agent deep reinforcement learning approach combined with user preference adaptation'
authors:
- Chen, Shiyou
- Rui, Lanlan
- Gao, Zhipeng
- Yang, Yang
- Qiu, Xuesong
- Guo, Shaoyong
venue: Future Generation Computer Systems
venue_type: journal
year: 2025
doi: 10.1016/j.future.2024.107612
url: https://www.scopus.com/pages/publications/85210040507?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Edge computing
- Mobility
- Multi-agent reinforcement learning
- Service migration
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

# paper-1483 — Service migration with edge collaboration: Multi-agent deep reinforcement learning approach combined with user preference adaptation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing provides proximate intelligent services for distributed users. Due to the user's mobility and highly dynamic network, edge servers with limited coverage cannot ensure continuity of running services and maintain high-level Quality of Service. To tackle this issue, an effective service migration strategy is of paramount importance. However, the current approach ignores the cooperation between multiple edge servers and independent users. In this article, we study service migration with edge collaboration to realize lightweight migration by layer-sharing framework of containers, saving redundant transmissions of migration. Then, we formalize the migration decision problem as maximizing the migration utility problem. To obtain efficient online decisions, we proposed a dynamic service migration strategy (MA-DSM) based on multi-agent proximal policy optimization (MAPPO) algorithm, which leverages a flexible multi-policy framework to achieve user preference adaptation. Specifically, we improve the basic MAPPO by devising a context-aware grouping method to cluster agents with user's mobility patterns and service preferences. Parameter sharing is introduced into the actor–critic network to learn customized policies for different clusters, facilitating cooperation among users in the same cluster. Extensive experiments demonstrate that our proposed approach outperforms baselines in terms of convergence, latency and migration utility. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1483.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
