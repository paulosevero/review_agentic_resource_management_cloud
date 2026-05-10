---
id: paper-0649
title: Multi-cloud service provision based on decision tree and two-layer Restricted Monte Carlo Tree Search
authors:
- Li, Wenjuan
- Cao, Jian
- Zhou, Bin
- Deng, Shuiguang
- Zhang, Qifei
- Hu, Keyong
- Li, Jing
- Zhao, Haili
venue: Internet of Things (Netherlands)
venue_type: journal
year: 2023
doi: 10.1016/j.iot.2023.100751
url: https://www.scopus.com/pages/publications/85150808701?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Monte Carlo tree search
- Service preference learning
- Service provision in a multi-cloud environment
- Unified cloud API
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

# paper-0649 — Multi-cloud service provision based on decision tree and two-layer Restricted Monte Carlo Tree Search

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Compared with traditional service provision methods, cloud computing has many advantages, such as on-demand services and flexible pricing systems, attracting widespread attention from both academia and industry. However, the abundance of cloud services makes it difficult for users to choose suitable ones. Furthermore, the cloud is usually a dynamically changing execution environment, requiring users to constantly switch service carriers for the best experience. Therefore, to improve the efficiency of service interactions in a multi-cloud environment and cope with the high concurrency demands, this paper proposes a multi-agent and distributed broker-based cloud service provisioning model. Equipped with a decision tree-based user preference learning module, brokers in the proposed model can continuously adjust their resource introduction strategy through training on historical data. In the process of cloud service interaction, brokers select the best cost-effective service for users within a limited time through a two-layer Restricted Monte Carlo Tree Search (RMTCS) algorithm. This paper develops a multi-cloud service interconnection system based on the Libcloud framework. Shielding the different interfaces of different cloud service providers in cloud virtual machine and storage services provides the most suitable services for users and realizes the unified cloud federation service supply. The experiment results prove that the proposed model achieves better performance over the traditional methods and can better meet the service requirements of users. © 2023 The Author(s)

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0649.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
