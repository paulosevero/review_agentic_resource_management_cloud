---
id: paper-0693
title: Admission control policy and key agreement based on anonymous identity in cloud computing
authors:
- Paulraj, D.
- Neelakandan, S.
- Prakash, M.
- Baburaj, E.
venue: Journal of Cloud Computing
venue_type: journal
year: 2023
doi: 10.1186/s13677-023-00446-2
url: https://www.scopus.com/pages/publications/85158132627?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Admission control policy (ACP)
- Cloud computing
- Cross-cloud data migration
- Key agreement
- Multi-agent reinforcement learning algorithm (MARL)
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

# paper-0693 — Admission control policy and key agreement based on anonymous identity in cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing has completely revolutionized the concept of computing by providing users with always-accessible resources. In terms of computational, storage, bandwidth, and transmission costs, cloud technology offers its users an entirely new set of advantages and cost savings. Cross-cloud data migration, required whenever a user switches providers, is one of the most common issues the users encounter. Due to smartphones’ limited local storage and computational power, it is often difficult for users to back up all data from the original cloud servers to their mobile phones to upload and download the data to the new cloud provider. Additionally, the user must remember numerous tokens and passwords for different applications. In many instances, the anonymity of users who access any or all services provided by this architecture must be ensured. Outsourcing IT resources carries risks, particularly regarding security and privacy, because cloud service providers manage and control all data and resources stored in the cloud. However, cloud users would prefer that cloud service providers not know the services they employ or the frequency of their use. Consequently, developing privacy protections takes a lot of work. We devised a system of binding agreements and anonymous identities to address this problem. Based on a binding contract and admission control policy (ACP), the proposed model facilitates cross-cloud data migration by fostering cloud provider trust. Finally, Multi-Agent Reinforcement Learning Algorithm (MARL) is applied to identify and classify anonymity in the cloud by conducting various pre-processing techniques, feature selection, and dimensionality reduction. © 2023, The Author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0693.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
