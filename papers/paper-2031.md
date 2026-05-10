---
id: paper-2031
title: Automated Lifting for Cloud Infrastructure-as-Code Programs
authors:
- Peng, Jingjia
- Qiu, Yiming
- Kon, Patrick Tser Jern
- Zhao, Pinhan
- Huang, Yibo
- Guo, Zheng
- Wang, Xinyu
- Chen, Ang
venue: Proceedings - 2025 IEEE/ACM International Workshop on Cloud Intelligence and AIOps, AIOps 2025
venue_type: conference
year: 2025
doi: 10.1109/AIOps66738.2025.00007
url: https://www.scopus.com/pages/publications/105009460224?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4--9
keywords:
- AIOps
- Cloud Management
- Infrastructure-as-Code
- Program Lifting
- Reverse Engineering
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

# paper-2031 — Automated Lifting for Cloud Infrastructure-as-Code Programs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Infrastructure-as-code (IaC) is reshaping how cloud resources are managed. IaC users write high-level programs to define their desired infrastructure, and the underlying IaC platforms automatically deploy the constituent resources into the cloud. While proven powerful at creating greenfield deployments (i.e., deployments from scratch), existing IaC platforms provide limited support for managing brownfield infrastructure (i.e., existing, non-IaC deployments). This hampers migration from legacy management approaches to an IaC workflow and hinders wider IaC adoption. Managing brownfield deployments requires techniques to lift low-level cloud states and translate them into corresponding IaC programs - the reversal of the regular deployment process. Existing tools rely heavily on rule-based reverse engineering, which suffers from the lack of automation, limited resource coverage, and prevalence of errors. In this work, we lay out the vision for Lilac, an approach that frees IaC lifting from extensive manual engineering. Lilac brings the best of both worlds: leveraging LLMs to automate lifting rule extraction, coupled with symbolic methods to provide correctness assurance. We envision that Lilac would enable the construction of an automated and provider-agnostic lifting tool with high coverage and accuracy. A prototype of LILAC is available here.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2031.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
