---
id: paper-2666
title: Reliable Federated Multi-View Learning for Heterogeneous Information Fusion in Mobile Edge Computing
authors:
- Li, Daoyuan
- Yang, Zuyuan
- Kang, Jiawen
- Xiong, Zehui
- Niyato, Dusit
- Xie, Shengli
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3640705
url: https://www.scopus.com/pages/publications/105024110218?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7062--7076
keywords:
- Federated learning
- mobile computing
- multi-view data fusion
- trusted learning
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

# paper-2666 — Reliable Federated Multi-View Learning for Heterogeneous Information Fusion in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rising data demands of generative AI models, such as large language models (LLMs), underscore the value of utilizing edge device data in mobile computing, where federated learning (FL) provides a privacy-preserving approach via decentralized model training. To address data heterogeneity across edge devices, federated multi-view learning (FedMVL) has been proposed to improve global model performance by capturing consistency and complementarity among diverse data views. However, existing methods often assume ideal conditions and neglect data uncertainty in mobile edge devices environments. To overcome these challenges, we propose Federated Reliable Multi-view Classification (FedRMVL), a vertical FedMVL framework incorporates Subjective Logic for lightweight uncertainty quantification at local edge devices and applies the Dempster-Shafer combination rule for adaptive and reliable multi-view opinion fusion at the server. Additionally, a partial parameter-sharing strategy is introduced to address feature dimension heterogeneity during federated optimization. The effectiveness and robustness of FedRMVL are validated through theoretical analysis and extensive experiments on real-world datasets. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2666.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
