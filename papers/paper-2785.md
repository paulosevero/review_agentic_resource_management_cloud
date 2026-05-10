---
id: paper-2785
title: Disentangled Graph Variational Auto-encoder Based Framework to Improve the Operational Efficiency in Cloud Computing Environments
authors:
- Subramanian, Vignesh Kumar
- Bhambri, Satish
- Gajula, Sreenivasulu
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-14044-9_32
url: https://www.scopus.com/pages/publications/105030866281?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 396--407
keywords:
- Cloud Computing
- Cloud Operations
- Disentangled Graph Variational Auto-Encoder
- Large Language Models
- Site Reliability Engineering
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2785 — Disentangled Graph Variational Auto-encoder Based Framework to Improve the Operational Efficiency in Cloud Computing Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing reliance on cloud computing has increased the demand for service stability and dependability, posing problems for Site dependability Engineers (SREs) responsible with proactive monitoring and responding to possible incidents. Despite advances in monitoring tools, SREs struggle to find anomalies in a timely manner, resulting in service failures and a bad impact on customer perception, necessitating the use of an automated anomaly detection system. In this paper, Disentangled Graph Variational Auto-Encoder Based Framework for Intelligent Anomaly Detection to Strengthen Site Reliability Engineering and Improve Operational Efficiency in Cloud Computing Environments is proposed. Large Language Models is used to recognize basic components of cloud infrastructure, their fault modes and behavioural patterns, forming the basis of an innovative anomaly modeling approach. Initially, the data are collected from Infrastructure as a Service multizone regions. The gathered data is saved in Cloud Object Storage. Disentangled Graph Variational Auto-Encoder is utilized to detect anomalies by modeling the intricate relationships and identifying abnormal patterns across the cloud infrastructure environment. Then the proposed is implemented and performance metrics such as Memory Usage, Throughput and Latency are analyzed. Finally, the proposed method provides 26.68%, 25.75%, and 26.16% lower memory usage and attains 29.08%, 30.70%, and 16.26% higher throughput compared with existing methods: Reliability-aware web service composition along cost minimization perspective: a multi-objective particle swarm optimization in multi-cloud scenarios, Strategies for effectual resource management in federated cloud environs supporting Infrastructure as a Service and A Model-Based Schemes Engineering Plugin for Cloud Safety Architecture Design respectively. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2785.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
