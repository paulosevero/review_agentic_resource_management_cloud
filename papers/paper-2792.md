---
id: paper-2792
title: Priority-Based VM Migration with Dynamic Load Balancing in Cloud Environment
authors:
- Swarnakar, Soumen
- Banerjee, Chandan
- Bhattacharjee, Debak
- Dhar, Subhrajit
- Dhar, Ankita
- Roy, Siddharth
- Dutta, Tanmay
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2026
doi: 10.1007/978-981-96-6060-5_5
url: https://www.scopus.com/pages/publications/105019644738?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 57--68
keywords:
- Cloud computing
- Dynamic load balancing
- Efficient load balancing
- Multi-agent
- Priority based
- Resource allocation
- Virtual machines
- VM migration
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

# paper-2792 — Priority-Based VM Migration with Dynamic Load Balancing in Cloud Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing involves using internet-based remote servers for data storage, management, and processing. This on-demand service allows users to make payments for simply that which they utilize. Since users of cloud computing are widespread globally, managing this vast amount of data presents a significant challenge. Load balancing efficiently allocates workloads across multiple computing resources, such as online servers. The load balancer's resources can be changed or added based on user requirements. The primary goals of load balancing are to optimize resource usage, costs, to enhance throughput, and to prevent VMs from being overloaded. This research work introduces a migration of jobs in virtual machines using the priority of tasks, remaining execution time as well as migration time for the cloud dynamic load balancing. The proposed method shows better result in comparison with some existing cloud load-balancing algorithms in respect of average makespan time, average response time. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2792.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
