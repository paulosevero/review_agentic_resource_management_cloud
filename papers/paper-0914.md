---
id: paper-0914
title: 'Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings'
authors:
- Gajewski, Darek
- Arju, Muhammad Ashfakur Rahman
- Abdelfattah, Amr S.
- Cerny, Tomas
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2024
doi: 10.1007/978-3-031-70797-1_2
url: https://www.scopus.com/pages/publications/85203601811?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 20--36
keywords:
- Canary Testing
- Case Study
- Cloud Systems
- Container Right-sizing Optimization
- Enterprise Architecture
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

# paper-0914 — Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In 2018, Ancestry migrated into Amazon’s public cloud. Hundreds of applications that were hosted on physical hardware were migrated to the cloud onto internally supported Kubernetes environments. This established a microservice architecture for many applications at Ancestry. In 2020, Ancestry’s cloud expenses goals were set at $12M in Operating expenses savings over 2 years. To overcome the problem of scale, an automated right-sizing effort needed to take place. Ancestry purchased a tool called Opsani. Opsani allowed the team to use dynamic canary testing in combination with a CanaryAdvisor to act as the AI agent. Opsani was integrated into Ancestry’s continuous integration and continuous delivery platform to automate right-sizing and help reach cost optimization targets with limited resources. After a successful proof of concept was developed by the DNA Matches agile team, there was a company-wide integration of Opsani into Ancestry’s CI/CD platform. The tool would need to scale out continuous optimization efforts across many of the teams utilizing Kubernetes and virtual machine infrastructure. This case study details the experience and knowledge gained from scaling automation optimizations using an AI agent with more than 200 individual applications across 30 agile teams. The challenges introduced by the rate of changes in the system and monitoring feedback delays began to affect the customer experience with the product. As teams adopted optimization changes at higher rates, new guard rails were introduced to control the release cycles and ensure stability for paying customers. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0914.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
