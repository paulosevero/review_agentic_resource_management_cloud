---
id: paper-1630
title: AES Cryptography Enabled Responsible Federated Foundation Model Using Transformer LLM and LSTM for Smart Grid IIoT Networks
authors:
- Hasan, Mohammad Kamrul
- Rayhan Kabir, S.
- Islam, Shayla
- Abdullah, Salwani
- Abbas, Huda Saleh
- Pandey, Bishwajeet
- Gadekallu, Thippa Reddy
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3608807
url: https://www.scopus.com/pages/publications/105015985546?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cyber Security
- Distributed Deep Learning
- Foundation Model
- IIoT
- LLM
- LSTM
- Responsible AI
- Smart Grid
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1630 — AES Cryptography Enabled Responsible Federated Foundation Model Using Transformer LLM and LSTM for Smart Grid IIoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The use of SCADA and AMI systems in smart grid-based Industrial Internet-of-Things (SG-IIoT) networks for proper energy supply are noteworthy. Inaccurate energy load forecasts, cyber-threats, and energy load-based sustainability issues in smart grids hinder SG-IIoT operations. To mitigate these challenges, a federated-learning approach is developed by integrating LSTM (Long-Short-Term-Memory), Transformer-LLM (Larger Language Model) based Foundation-Model, and AES (Advanced-Encryption-Standard) cryptography. The proposed approach is named Responsible-Federated-Foundation-Model (ResFedFM). To ensure secure federated learning computation as well as data security at the edge (smart meter), fog (SCADA-based substation grid) and cloud (grid cloud server) layers of the SG-IIoT, a self-parent keys-based cryptography method has been developed by combining AES with HMAC (Hash-based-Message-Authentication-Code). A load forecasting algorithm called LSTM-LLM-GenResAI-Forecasting has been developed for computation at each end node of the federated learning process. The edge node forecast outputs are encrypted and aggregated at the fog node. At the fog node, the data are decrypted, and aggregation algorithm of federated-learning process are used to generate overall load forecasting of each sub-station grid. Again, the forecast data from these fog nodes are aggregated in an encrypted state at the cloud level and overall load forecasts are generated for multiple fog nodes. The result of proposed approach provides responsible forecasting (High accuracy, green computing-based energy demand, optimization of AI-hallucination, and grid data security), demonstrating enhanced performance over seven significant models. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1630.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
