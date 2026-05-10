---
id: paper-2273
title: ML-Assistant Service Function Chaining Workload Scheduler for Cloud-Native inFrastructure
authors:
- Wang, Ziqiang
- Lung, Chung-Horng
- Huang, Changcheng
venue: Proceedings of IEEE/IFIP Network Operations and Management Symposium 2025, NOMS 2025
venue_type: conference
year: 2025
doi: 10.1109/NOMS57970.2025.11073743
url: https://www.scopus.com/pages/publications/105012161516?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud-native infrastructure
- Long-Short Term Memory
- Scheduler
- Service Function Chaining
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

# paper-2273 — ML-Assistant Service Function Chaining Workload Scheduler for Cloud-Native inFrastructure

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Service Function Chaining (SFC) has the potential to revolutionize cloud computing and containerization paradigm. SFC jobs, predominantly deployed as containers within cloud-native infrastructures, require substantial computing, memory, and storage resources to operate Virtual Network Functions (VNFs) efficiently. However, scheduling SFC workloads in cloud-native infrastructures, such as Kubernetes clusters spanning geographically distributed data centers, presents significant chal-lenges. These challenges arise not only from the diverse scheduling strategies employed by each data center but also from the vast number of jobs processed on a daily basis. Furthermore, SFC tasks have stringent requirements for computing resources and network bandwidth, which complicates the scheduling process. This paper introduces a machine learning-based (ML-based) scheduling approach to address these challenges by employing the Long Short Term Memory (LSTM) model. This paper makes two main contributions. First, we formulate the dynamic SFC mapping problem by modeling SFC jobs in terms of computing and memory resources. Then, we use a decentralized multiagent LSTM framework to predict the hardware resource usages of nodes for each incoming SFC job, in order to select the most suitable node to optimize system resource utilization and minimize the job wait time. Our results demonstrate a 6%-20% improvement in scheduling efficiency and accuracy compared to non-machine learning-based schedulers.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2273.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
