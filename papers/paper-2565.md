---
id: paper-2565
title: Enhancing Serverless Function Resilience Against Vulnerabilities with MoFaaS
authors:
- Escaleira, Pedro
- Cunha, Vitor A.
- Barraca, João P.
- Gomes, Diogo
- Aguiar, Rui L.
venue: Journal of Network and Systems Management
venue_type: journal
year: 2026
doi: 10.1007/s10922-026-10054-5
url: https://www.scopus.com/pages/publications/105034875664?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cloud computing
- Cloud security
- Function as a service (FaaS)
- Moving target defense (MTD)
- N-version programming (NVP)
- Serverless
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

# paper-2565 — Enhancing Serverless Function Resilience Against Vulnerabilities with MoFaaS

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing has revolutionized cloud application development by eliminating infrastructure management complexities. However, its dynamic and ephemeral nature introduces security challenges that are difficult to mitigate using traditional mechanisms. In particular, function vulnerabilities remain a critical concern, as attackers can exploit them to compromise applications and escalate attacks across multi-tenant environments. To address these challenges, we propose an enhanced version of Moving Functions as a Service (MoFaaS), a security mechanism that leverages Moving Target Defense (MTD) and N-Version Programming (NVP) to introduce execution diversity and improve fault tolerance in serverless applications. Additionally, we incorporate a Large Language Model (LLM)-based feedback loop to assist developers in generating diverse function variants with reduced effort. We validate our contributions through open-source Proof of Concept (PoC) implementations on Knative and conduct an extensive security and performance evaluation on a realistic serverless application. The results demonstrate that our approach effectively increases attack complexity while maintaining performance within acceptable bounds. © The Author(s) 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2565.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
