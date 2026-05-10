---
id: paper-0153
title: Efficient data integrity and data replication in cloud using stochastic diffusion method
authors:
- Ramanan, M.
- Vivekanandan, P.
venue: Cluster Computing
venue_type: journal
year: 2019
doi: 10.1007/s10586-018-2480-9
url: https://www.scopus.com/pages/publications/85044088915?origin=resultslist
publisher: Springer
pages: 14999--15006
keywords:
- Cloud computing
- Cloud services
- Data integrity
- Data replication and stochastic diffusion search (SDS)
- Data storage
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

# paper-0153 — Efficient data integrity and data replication in cloud using stochastic diffusion method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing will provide scalable computing as well as storage resources where more data intensive applications will be developed in a computing environment. Owing to the existence of such security threats in the cloud, several mechanisms are being proposed for allowing the users to audit the integrity of data along with the public key of the owner of the data even before making use of the cloud data. Replicating of data in cloud servers through multiple data centers offers better availability, scalability, and durability. The correctness of choice of the right type of public key of the previous mechanisms is based on the security of the public key infrastructure (PKI). Although traditional PKI has been widely used in the construction of public key cryptography, it still faces many security risks, especially in the aspect of managing certificates. There are different applications having different types of quality of service (QoS) needs. In order to support the QoS requirement continuously, the application of such data corruption for this work will be an efficient integrity of data replication that makes use of a stochastic diffusion search (SDS) algorithm that has been proposed. This SDS is that technique of a multi-agent global optimisation which has been based on the behaviour of ants that has been rooted in the partial evaluation of that of an objective function along with direct communication among agents. The proposed SDS algorithm will minimize the replication cost of data. The results of these experiments have shown that the mechanism will be able to demonstrate the effectiveness of this proposed algorithm which is in the replication of data as well as its recovery. The proposed method when appropriately compared with the cost effective replication of dynamic data given by Li et al. proves that the average recovery time is less by 18.18% for the 250 number of requested nodes, by 14.28% for the 500 number of requested nodes, by 11.11% for the 750 number of requested nodes and by 8.69% for the 1000 number of requested nodes. © 2018, Springer Science+Business Media, LLC, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0153.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
