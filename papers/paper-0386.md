---
id: paper-0386
title: Intelligent multi-agent reinforcement learning model for resources allocation in cloud computing
authors:
- Belgacem, Ali
- Mahmoudi, Saïd
- Kihl, Maria
venue: Journal of King Saud University - Computer and Information Sciences
venue_type: journal
year: 2022
doi: 10.1016/j.jksuci.2022.03.016
url: https://www.scopus.com/pages/publications/85128308530?origin=resultslist
publisher: King Saud bin Abdulaziz University
pages: 2391--2404
keywords:
- Cloud computing
- Energy consumption
- Fault tolerance
- Load balancing
- Multi-agent system
- Q-learning
- Resource allocation
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

# paper-0386 — Intelligent multi-agent reinforcement learning model for resources allocation in cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Now more than ever, optimizing resource allocation in cloud computing is becoming more critical due to the growth of cloud computing consumers and meeting the computing demands of modern technology. Cloud infrastructures typically consist of heterogeneous servers, hosting multiple virtual machines with potentially different specifications, and volatile resource usage. This makes the resource allocation face many issues such as energy conservation, fault tolerance, workload balancing, etc. Finding a comprehensive solution that considers all these issues is one of the essential concerns of cloud service providers. This paper presents a new resource allocation model based on an intelligent multi-agent system and reinforcement learning method (IMARM). It combines the multi-agent characteristics and the Q-learning process to improve the performance of cloud resource allocation. IMARM uses the properties of multi-agent systems to dynamically allocate and release resources, thus responding well to changing consumer demands. Meanwhile, the reinforcement learning policy makes virtual machines move to the best state according to the current state environment. Also, we study the impact of IMARM on execution time. The experimental results showed that our proposed solution performs better than other comparable algorithms regarding energy consumption and fault tolerance, with reasonable load balancing and respectful execution time. © 2022 The Author(s)

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0386.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
