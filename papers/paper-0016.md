---
id: paper-0016
title: Cost-Effective Low-Delay Design for Multiparty Cloud Video Conferencing
authors:
- Hajiesmaili, Mohammad H.
- Mak, Lok To
- Wang, Zhi
- Wu, Chuan
- Chen, Minghua
- Khonsari, Ahmad
venue: IEEE Transactions on Multimedia
venue_type: conference
year: 2017
doi: 10.1109/TMM.2017.2710799
url: https://www.scopus.com/pages/publications/85040537825?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2760--2774
keywords:
- Cloud computing
- network combinatorial optimization
- parallel algorithm
- video conferencing
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

# paper-0016 — Cost-Effective Low-Delay Design for Multiparty Cloud Video Conferencing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multiparty cloud video conferencing architecture has been recently advocated to exploit rich computing and bandwidth resources in the cloud to effectively improve video conferencing performance. As a typical design in this architecture, multiple agents, i.e., virtual machines, are deployed in different cloud sites, and users are assigned to the agents. Then, the users communicate through the agents, and the agents might transcode the recorded videos given the heterogeneities among devices in terms of hardware specification and connectivity. In this architecture, two critical and nontrivial challenges are: 1) assigning users to agents to reduce the operational cost and the user-to-user conferencing delay and 2) identifying best agents to perform transcoding tasks, taking into account the heterogeneous bandwidth and processing availabilities. To address these challenges, we cast a joint problem of user-to-agent assignment and transcoding-agent selection. The ultimate objective is to simultaneously minimize the cost of the service provider and the conferencing delay. The problem is combinatorial in nature, which belongs to the NP-hard node assignment problems. We leverage the Markov approximation framework and devise an adaptive parallel algorithm that finds a close-to-optimal solution to our problem with a bounded performance guarantee. To evaluate the performance of our solution, we implement a prototype video conferencing system and carry out trace-driven experiments. In a set of large-scale experiments using PlanetLab traces, our solution decreases the operational cost by 77% and simultaneously yields lower conferencing delay compared with an existing alternative. © 2017 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0016.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
