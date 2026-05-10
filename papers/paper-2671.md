---
id: paper-2671
title: 'EC-MADRL: AI-Enhanced Edge Cooperation Caching Based on Multi-agent Deep Reinforcement Learning'
authors:
- Liang, Yuzhu
- Zeng, Jiandian
- Zou, Haodong
- Mei, Yaxin
- Zhang, Guangxue
- Wang, Tian
venue: Communications in Computer and Information Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-3483-8_38
url: https://www.scopus.com/pages/publications/105028298004?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 510--523
keywords:
- Artificial Intelligence
- Cooperative edge caching
- Deep Reinforcement Learning
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

# paper-2671 — EC-MADRL: AI-Enhanced Edge Cooperation Caching Based on Multi-agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of multimedia content and online gaming, traditional cloud computing faces difficulties in meeting real-time requirements, particularly in optimizing caching strategies, managing dynamic environments, and handling user location uncertainties. To overcome these limitations, we propose a novel AI-Enhanced Edge Cooperation framework based on Multi-Agent Deep Reinforcement Learning (EC-MADRL) to optimize scheduling and resource allocation across edge nodes. This framework enables adaptive caching and replenishment strategies in a cooperative environment, modeled as a multi-agent Markov Decision Process (MDP). By integrating an online MADRL approach, the EC-MADRL algorithm allows edge nodes to collaboratively learn optimal policies for caching and resource distribution. We analyze the time complexity and convergence of the algorithm, demonstrating its effectiveness in improving edge node performance. Experimental results show a 30.12% increase in edge node profits, a 20.67% reduction in user latency, and a 24.31% decrease in user costs, highlighting the superior performance of our AI-enhanced approach over baseline methods, including DDQN-ECMP, MADRL-ECMP, and P4LRU algorithms. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2671.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
