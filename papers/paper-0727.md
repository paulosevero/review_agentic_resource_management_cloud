---
id: paper-0727
title: Federated Deep Reinforcement Learning for Recommendation-Enabled Edge Caching in Mobile Edge-Cloud Computing Networks
authors:
- Sun, Chuan
- Li, Xiuhua
- Wen, Junhao
- Wang, Xiaofei
- Han, Zhu
- Leung, Victor C. M.
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2023.3235443
url: https://www.scopus.com/pages/publications/85147301164?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 690--705
keywords:
- discrete soft actor-critic
- federated learning
- Multi-tier computing
- recommendation-enabled edge caching
- soft hits
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0727 — Federated Deep Reinforcement Learning for Recommendation-Enabled Edge Caching in Mobile Edge-Cloud Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To support rapidly increasing services and applications from users, multi-tier computing is emerged as a promising system-level computing architecture by distributing computing/caching/communication/networking capabilities between cloud servers to users, especially deploying edge servers at network edges (e.g., base stations). However, due to heterogeneous content requests of users and a high-cost hit manner with direct hits, edge caching is still a most serious issue to be addressed. In this paper, we investigate the issue of recommendation-enabled edge caching in mobile two-tier (edge-cloud) computing networks. Particularly, we integrate recommender systems and edge caching to support both direct hits and soft hits and thus improve the resource utilization of edge servers. We model the factors affecting the user quality of experience as a comprehensive system cost and further formulate the problem as a multi-agent Markov decision process with the goal of minimizing the long-term average system cost. To address the formulated problem, we propose a decentralized recommendation-enabled edge caching framework that leverages a discrete multi-agent variant of soft actor-critic and federated learning. The proposed framework enables each edge server to learn its best policy locally and generate judicious decisions independently. Finally, trace-driven simulation results demonstrate that the proposed framework converges to a better caching policy and outperforms several existing algorithms on average system cost reduction.  © 1983-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0727.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
