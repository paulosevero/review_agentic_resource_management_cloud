---
id: paper-1681
title: Design and Implementation of Distributed Web Application Vulnerability Assessment Tools for Securing Complex Microservices Environment
authors:
- Izzat, Muhammad
- Saputra, Ferry Astika
- Syarif, Iwan
venue: International Journal of Safety and Security Engineering
venue_type: journal
year: 2025
doi: 10.18280/ijsse.150207
url: https://www.scopus.com/pages/publications/105001095052?origin=resultslist
publisher: International Information and Engineering Technology Association
pages: 267--273
keywords:
- distributed vulnerability management
- nuclei scanner
- OWASP security framework
- real-time vulnerability detection
- web application security testing
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

# paper-1681 — Design and Implementation of Distributed Web Application Vulnerability Assessment Tools for Securing Complex Microservices Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern web applications with complex distributed architectures present significant challenges in vulnerability assessment that traditional approaches fail to address effectively. This research introduces the Distributed Vulnerability Management System (DVMS), implementing a multi-agent architecture to enhance vulnerability detection while eliminating single points of failure. The methodology employs the Nuclei vulnerability scanner across five Open Web Application Security Project (OWASP) security domains, expanding beyond conventional vulnerabilities to include Security Misconfiguration, Vulnerable Components, and Sensitive Data Exposure. Experimental results demonstrate detection accuracies of 80% for Injection, 85.71% for XSS, 80% for Security Misconfiguration, 50% for Vulnerable Components, and 90.91% for Sensitive Data Exposure. The distributed architecture enables parallel processing and optimizes security resource allocation across network infrastructures. While showing promising results in comprehensive security coverage, the system identifies areas for future enhancement in detection accuracy and vulnerability scope expansion. This research contributes a scalable, distributed approach to vulnerability management particularly suited for modern web applications, providing organizations with enhanced security assessment capabilities in complex technological environments. ©2025 The authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1681.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
