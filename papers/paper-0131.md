---
id: paper-0131
title: New Distributed Constraint Reasoning Algorithms for Load Balancing in Edge Computing
authors:
- Hoang, Khoi D.
- Wayllace, Christabel
- Yeoh, William
- Beal, Jacob
- Dasgupta, Soura
- Mo, Yuanqiu
- Paulos, Aaron
- Schewe, Jon
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2019
doi: 10.1007/978-3-030-33792-6_5
url: https://www.scopus.com/pages/publications/85076505869?origin=resultslist
publisher: Springer
pages: 69--86
keywords:
- DCOPs
- DisCSPs
- Edge computing
- Multi-agent systems
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

# paper-0131 — New Distributed Constraint Reasoning Algorithms for Load Balancing in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing is a paradigm for improving the performance of cloud computing systems by performing data processing at the edge of the network, closer to the users and sources of data. As data processing is traditionally done in large data centers, typically located far from their users, the edge computing paradigm will reduce the communication bottleneck between the user and the location of data processing, thereby improving overall performance. This becomes more important as the number of Internet-of-Things (IoT) devices and other mobile or embedded devices continues to increase. In this paper, we investigate the use of distributed constraint reasoning (DCR) techniques to model and solve the distributed load balancing problem in edge computing problems. Specifically, we (i) provide a mapping of the distributed load balancing problem in edge computing to a distributed constraint satisfaction and optimization problem; (ii) propose two DCR algorithms to solve such problems; and (iii) empirically evaluate our algorithms against a state-of-the-art DCR algorithm on random and scale-free networks. © 2019, Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0131.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
