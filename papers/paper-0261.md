---
id: paper-0261
title: 'Resource Allocation and Service Provisioning in Multi-Agent Cloud Robotics: A Comprehensive Survey'
authors:
- Afrin, Mahbuba
- Jin, Jiong
- Rahman, Akhlaqur
- Rahman, Ashfaqur
- Wan, Jiafu
- Hossain, Ekram
venue: IEEE Communications Surveys and Tutorials
venue_type: journal
year: 2021
doi: 10.1109/COMST.2021.3061435
url: https://www.scopus.com/pages/publications/85101780393?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 842--870
keywords:
- cloud computing
- computation and communication trade-off
- edge computing
- Multi-robot system
- offloading
- resource allocation
- service provisioning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-0261 — Resource Allocation and Service Provisioning in Multi-Agent Cloud Robotics: A Comprehensive Survey

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Robotic applications nowadays are widely adopted to enhance operational automation and performance of real-world Cyber-Physical Systems (CPSs) including Industry 4.0, agriculture, healthcare, and disaster management. These applications are composed of latency-sensitive, data-heavy, and compute-intensive tasks. The robots, however, are constrained in the computational power and storage capacity. The concept of multi-agent cloud robotics enables robot-to-robot cooperation and creates a complementary environment for the robots in executing large-scale applications with the capability to utilize the edge and cloud resources. However, in such a collaborative environment, the optimal resource allocation for robotic tasks is challenging to achieve. Heterogeneous energy consumption rates and application of execution costs associated with the robots and computing instances make it even more complex. In addition, the data transmission delay between local robots, edge nodes, and cloud data centres adversely affects the real-time interactions and impedes service performance guarantee. Taking all these issues into account, this paper comprehensively surveys the state-of-the-art on resource allocation and service provisioning in multi-agent cloud robotics. The paper presents the application domains of multi-agent cloud robotics through explicit comparison with the contemporary computing paradigms and identifies the specific research challenges. A complete taxonomy on resource allocation is presented for the first time, together with the discussion of resource pooling, computation offloading, and task scheduling for efficient service provisioning. Furthermore, we highlight the research gaps from the learned lessons, and present future directions deemed beneficial to further advance this emerging field.  © 1998-2012 IEEE.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0261.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
