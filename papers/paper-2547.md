---
id: paper-2547
title: Joint Semantic Compression and Massive MIMO Transmission for Edge Video Analytics
authors:
- Cui, Peng
- Han, Shujun
- Liu, Ze
- Luo, Yunfei
- Xu, Xiaodong
- Chi, Xiaoyu
- Xu, Bingxuan
- Zhang, Ping
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2026.3666538
url: https://www.scopus.com/pages/publications/105030669756?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6509--6523
keywords:
- massive-MIMO
- multi-agent soft actor-critic
- Stochastic network calculus
- task-oriented communication
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

# paper-2547 — Joint Semantic Compression and Massive MIMO Transmission for Edge Video Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advancement of artificial intelligence (AI) technologies has catalyzed widespread deployment of emerging video analytics applications, particularly in edge computing environments requiring real-time processing capabilities. However, achieving optimal trade-off between analytical accuracy and real-time performance for edge video analytics in bandwidth-constrained conditions poses a critical challenge. To address this problem, this paper proposes a joint semantic compression and massive multiple-input and multiple-output (massive-MIMO) transmission scheme for edge video analytics. Specifically, we design a task-oriented performance metric named task reliability, jointly evaluating the stochastic delay bound of intelligent task transmission and the accuracy of intelligent task execution. By optimizing pilot sequence length, pilot power, data power, and semantic compression ratio jointly, we maximize the weighted sum task reliability. Furthermore, we propose a power and semantic compression ratio allocation (PSCRA) algorithm, which utilizes maximum entropy multi-agent reinforcement learning to balance exploration and exploitation. Numerical results demonstrate that our resource allocation scheme achieves superior system utility compared to baseline methods, while the PSCRA algorithm outperforms conventional multi-agent reinforcement learning algorithms.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2547.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
