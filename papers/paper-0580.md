---
id: paper-0580
title: A Heuristic Deep Q Learning for Offloading in Edge Devices in 5 g Networks
authors:
- Dong, YanRu
- Alwakeel, Ahmed M.
- Alwakeel, Mohammed M.
- Alharbi, Lubna A.
- Althubiti, Sara A
venue: Journal of Grid Computing
venue_type: journal
year: 2023
doi: 10.1007/s10723-023-09667-w
url: https://www.scopus.com/pages/publications/85163929242?origin=resultslist
publisher: Springer Science and Business Media B.V.
pages: ''
keywords:
- Double deep Q network
- Karush-Kuhn-Tucker
- Mobile edge computing
- Partial offloading
- Wireless node
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0580 — A Heuristic Deep Q Learning for Offloading in Edge Devices in 5 g Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The 5G Wireless Environments have huge data transmission; therefore, there is an increase in the requests for computational tasks from Intelligent Wireless Mobile Nodes. This computational capability leads to high reliability and low latency in a 5G network. Mobile edge computing (MEC) allows end systems with constrained computing capacity to handle computationally demanding tasks and offer accurate alternatives. The MEC server’s physical position is nearer to WN than other servers, which satisfies the demands for low latency and excellent dependability. To overcome the issues of existing work, such as low latency, offloading and task scheduling, the proposed method provides efficient results. In this work for job scheduling, Multi-agent Collaborative Deep Reinforcement Learning based Scheduling Algorithm with a double deep Q network (DQN) is used in the MEC system. To minimize the total Latency in Wireless Nodes, it uses Karush-Kuhn-Tucker (KKT) approach. This approach provides the optimum solutions to the partial and complete offloading tasks. The double deep Q network (DQN) reduces energy consumption and offers better convergence Between the Wireless Nodes. Compared to traditional algorithms like DeMDRL and BiDRL, the proposed MDRL-DDQN demonstrates superior performance. © 2023, The Author(s), under exclusive licence to Springer Nature B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0580.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
