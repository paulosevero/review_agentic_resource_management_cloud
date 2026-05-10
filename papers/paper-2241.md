---
id: paper-2241
title: Autonomous Recovery and Monitoring in AI Workflows with Generative AI
authors:
- Vinoth Kumar, K.
- Barakkath Nisha, U.
- Yasir Abdullah, R.
venue: Proceedings of the 6th International Conference on Electronics and Sustainable Communication Systems, ICESC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICESC65114.2025.11212528
url: https://www.scopus.com/pages/publications/105022650427?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2080--2085
keywords:
- anomaly detection
- automated recovery
- generative AI
- resource optimization
- self-healing
- workflow monitoring
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2241 — Autonomous Recovery and Monitoring in AI Workflows with Generative AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed AI workflows deployed across cloud-agnostic environments face frequent anomalies and failures, yet existing monitoring approaches remain largely reactive issuing alerts only after performance degrades and relying on static recovery rules that fail to adapt to dynamic workload fluctuations. This lack of proactive, intelligent recovery leads to prolonged downtime, inefficient resource utilization, and higher operational costs. To overcome these shortcomings, this research introduces a self-healing monitoring framework that integrates generative AI at every stage of anomaly management. The framework detects irregularities before they escalate, forecasts resource demands, and automatically executes remediation policies such as service scaling, restarts, or rollbacks. Architected using microservices and containerized deployment, the system combines statistical anomaly detection with generative diagnostics for root-cause analysis and actionable recovery planning. In experimental evaluations with benchmark AI pipelines, the proposed framework improved detection precision by 25%, reduced mean recovery time by 40%, and enhanced resource utilization by up to 30%, all while sustaining high throughput under variable loads. These outcomes confirm that embedding generative intelligence transforms monitoring from a passive observer into an active, resilient guardian of distributed AI workflows. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2241.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
