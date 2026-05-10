---
id: paper-0094
title: A Holistic Approach for Collaborative Workload Execution in Volunteer Clouds
authors:
- Sebastio, Stefano
- Amoretti, Michele
- Lafuente, Alberto Lluch
- Scala, Antonio
venue: ACM Transactions on Modeling and Computer Simulation
venue_type: journal
year: 2018
doi: 10.1145/3155336
url: https://www.scopus.com/pages/publications/105006704799?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- ant colony optimization (ACO)
- autonomic computing
- cloud computing
- collaborative computing
- Collective adaptive systems
- computational fields
- multiagent optimization
- peer-to-peer (P2P)
- task scheduling
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

# paper-0094 — A Holistic Approach for Collaborative Workload Execution in Volunteer Clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The demand for provisioning, using, and maintaining distributed computational resources is growing hand in hand with the quest for ubiquitous services. Centralized infrastructures such as cloud computing systems provide suitable solutions for many applications, but their scalability could be limited in some scenarios, such as in the case of latency-dependent applications. The volunteer cloud paradigm aims at overcoming this limitation by encouraging clients to offer their own spare, perhaps unused, computational resources. Volunteer clouds are thus complex, large-scale, dynamic systems that demand for self-adaptive capabilities to offer effective services, as well as modeling and analysis techniques to predict their behavior. In this article, we propose a novel holistic approach for volunteer clouds supporting collaborative task execution services able to improve the quality of service of compute-intensive workloads. We instantiate our approach by extending a recently proposed ant colony optimization algorithm for distributed task execution with a workload-based partitioning of the overlay network of the volunteer cloud. Finally, we evaluate our approach using simulation-based statistical analysis techniques on a workload benchmark provided by Google. Our results show that the proposed approach outperforms some traditional distributed task scheduling algorithms in the presence of compute-intensive workloads.  © 2018 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0094.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
