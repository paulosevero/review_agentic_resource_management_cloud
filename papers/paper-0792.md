---
id: paper-0792
title: Multi-agent deep reinforcement learning for online request scheduling in edge cooperation networks
authors:
- Zhang, Yaqiang
- Li, Ruyang
- Zhao, Yaqian
- Li, Rengang
- Wang, Yanwei
- Zhou, Zhangbing
venue: Future Generation Computer Systems
venue_type: journal
year: 2023
doi: 10.1016/j.future.2022.11.017
url: https://www.scopus.com/pages/publications/85143790115?origin=resultslist
publisher: Elsevier B.V.
pages: 258--268
keywords:
- Deep reinforcement learning
- Edge cooperation networks
- Long-term performance
- Multi-agent system
- Online request scheduling
- Value decomposition
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

# paper-0792 — Multi-agent deep reinforcement learning for online request scheduling in edge cooperation networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing as a complementary paradigm of cloud computing has gained more attention by providing mobile users with diversified services at the network edge. However, the increasingly complex mobile applications put a heavier load on edge networks. It is challenging to provide concurrency requests with high-quality service processing, especially when the edge networks are dynamically changing. To address the above issues, this paper investigates the online concurrent user requests scheduling optimization problem in edge cooperation networks. We model it as an online multi-stage decision-making problem, where requests are divided into a group of independent and logically related sub-tasks. We proposed a centralized training distributed execution based multi-agent deep reinforcement learning technique to realize the implicit cooperation scheduling decision-making policy learning among edge nodes. At the centralized training stage of the proposed mechanism, a value-decomposition-based policy learning technique is adopted to improve the long-term system performance, while at the distributed execution stage, only local environment status information is needed for each edge node to make the request scheduling decision. Extensive experiments are conducted, and simulation results demonstrate that the proposed mechanism outperforms other request scheduling mechanisms in reducing the long-term average system delay and energy consumption while improving the throughput rate of the system. © 2022 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0792.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
