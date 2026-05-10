---
id: paper-0974
title: 'CVALLM: A Cloud Platform Security Assessment Framework Based on Large Language Models'
authors:
- Jing, Wangyuan
- Zhang, Chi
- Zhang, Bingbing
- Wei, Lingbo
venue: Proceedings of the IEEE International Conference on Trust, Security and Privacy in Computing and Communications, TrustCom
venue_type: conference
year: 2024
doi: 10.1109/TrustCom63139.2024.00283
url: https://www.scopus.com/pages/publications/105006508021?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2039--2044
keywords:
- Cloud Security
- Large Language Model
- Vulnerability Assessment
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: Out of scope (LLM para avaliação de segurança — não é RM)
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0974 — CVALLM: A Cloud Platform Security Assessment Framework Based on Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing has revolutionized computing and data storage by providing flexible resource management and on-demand services. However, the centralized nature of cloud computing results in significant security issues that pose significant threats to cloud services. The security threat can be alleviated to a certain extent through the cloud platform security assessment. However, the existing cloud platform security assessment framework mainly measures security from the enterprise perspective and lacks methods from the user perspective. For users, much information is internal to the enterprise and cannot be obtained. To address these challenges, we propose a framework called CVALLM to measure cloud platform security from the user's perspective, which uses a large language model to automatically complete a cloud platform security assessment. First, we utilize a large language model to complete cloud platform information extraction and vulnerability collection from SLA agreements and product description documents that the user can access. Second, to solve the vulnerability assessment problem, we propose a vulnerability severity prediction method based on deep learning. This method considers both the textual description characteristics and the source code characteristics of the vulnerability. Finally, we propose an overall security assessment method for the cloud platform based on a large language model, design quantitative indicators to measure the security of the cloud platform, and automatically generate security reports to facilitate users' ability to quickly compare and choose the right cloud service. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "Large Language Models

Cloud c" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope (LLM para avaliação de segurança — não é RM)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0974.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
