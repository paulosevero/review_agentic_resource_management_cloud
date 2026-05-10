---
id: paper-1176
title: Virtual Machine Proactive Fault Tolerance Using Log-Based Anomaly Detection
authors:
- Senevirathne, Pratheek
- Cooray, Samindu
- Dinal Herath, Jerome
- Fernando, Dinuni
venue: IEEE Access
venue_type: journal
year: 2024
doi: 10.1109/ACCESS.2024.3506833
url: https://www.scopus.com/pages/publications/85210905590?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 178951--178970
keywords:
- Adaptive learning
- anomaly detection
- cloud computing
- fault tolerance
- large language models
- log analysis
- matrix profile
- natural language processing
- proactive migration
- virtual machines
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

# paper-1176 — Virtual Machine Proactive Fault Tolerance Using Log-Based Anomaly Detection

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Virtual Machine (VM) fault tolerance ensures high availability in cloud computing environments. Proactive fault tolerance strategies avert service disruptions by detecting potential failures before they occur and migrating the VMs to healthy hosts. In this paper, we propose Virtual Machine Proactive Fault Tolerance using Log-based Anomaly Detection (VMFT-LAD), a semi-supervised, real-time log anomaly detection model capable of detecting failures ahead of time to provide effective VM fault tolerance. VMFT-LAD leverages the efficiency of the Matrix Profile for anomaly detection and the log inference capability of Large Language Models (LLMs) to identify potential VM failures early, while minimizing false positives. Our improved Matrix Profile enables VMFT-LAD to continuously learn and identify potential failures, including unforeseen fault types, with minimal human intervention. Additionally, its semi-supervised nature eliminates the need for labeled failure data. Extensive evaluations on several datasets, using two distinct criteria to validate anomaly detection and early failure detection capabilities, demonstrate VMFT-LAD's outstanding performance. VMFT-LAD achieves a Numenta Anomaly Benchmark (NAB) standard score of 90.74 for predicting failures in advance, with a high early detection rate of 96.28% and a low false positive rate of 0.02%, enabling accurate and timely VM migration before failures occur. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1176.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
