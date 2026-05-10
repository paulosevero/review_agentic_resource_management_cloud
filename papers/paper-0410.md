---
id: paper-0410
title: 'Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach'
authors:
- Gao, Lynn
- Chen, Yutian
- Tang, Bin
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-23141-4_22
url: https://www.scopus.com/pages/publications/85148698291?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 291--309
keywords:
- Data centers
- k-stroll Problem
- Reinforcement learning
- Service function chaining
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0410 — Service Function Chain Placement in Cloud Data Center Networks: A Cooperative Multi-agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Service function chaining (SFC), consisting of a sequence of virtual network functions (VNFs) (i.e., firewalls and load balancers), is an effective service provision technique in modern data center networks. By requiring cloud user traffic to traverse the VNFs in order, SFC improves the security and performance of the cloud user applications. In this paper, we study how to place an SFC inside a data center to minimize the network traffic of the virtual machine (VM) communication. We take a cooperative multi-agent reinforcement learning approach, wherein multiple agents collaboratively figure out the traffic-efficient route for the VM communication. Underlying the SFC placement is a fundamental graph-theoretical problem called the k-stroll problem. Given a weighted graph G(V, E), two nodes s, and an integer k, the k-stroll problem is to find the shortest path from s to t that visits at least k other nodes in the graph. Our work is the first to take a multi-agent learning approach to solve k-stroll problem. We compare our learning algorithm with an optimal and exhaustive algorithm and an existing dynamic programming(DP)-based heuristic algorithm. We show that our learning algorithm, although lacking the complete knowledge of the network assumed by existing research, delivers comparable or even better VM communication time while taking two orders of magnitude of less execution time. © 2022, ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0410.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
