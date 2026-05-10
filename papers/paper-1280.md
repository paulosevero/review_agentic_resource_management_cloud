---
id: paper-1280
title: Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge
authors:
- Wu, Hai
- Chen, Xu
- Huang, Kaibin
venue: International Conference on Communications in China, ICCC Workshops 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCCWorkshops62562.2024.10693756
url: https://www.scopus.com/pages/publications/85207647933?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 226--231
keywords:
- 6G
- Edge AI
- fine-tuning
- Foundation models
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1280 — Multi-Device Cooperative Fine-Tuning of Foundation Models at the Network Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of large-scale foundation models (FoMo's) that can perform human-like intelligence inspires edge devices to access state-of-the-art artificial intelligence (AI) applications. For a better user experience, the pre-trained FoMo needs to be adapted for specialized downstream tasks through fine-tuning techniques. To transcend a single device's memory and computation limitations, we propose a multi-device cooperation mechanism within the device-edge cooperative fine-tuning (DEFT) paradigm, where devices distributed at the wireless edge simultaneously optimize different parts of fine-tuning parameters within a FoMo. The edge server is responsible for coordination and update aggregation. However, the parameter blocks resided in different depths within a FoMo architecture, leading to varied computation latency and memory consumption due to the adoption of gradient backpropagation-based calculations. The hetero-geneous on-device computation capability and memory budget, block calculation latency, and uploading channel conditions, necessitate an integrated communication-and-computation (C2) allocation of local computation loads and uplink communication resources to achieve low-latency DEFT (LoLa-DEFT). To address this issue, a depth-aware block allocation problem is formulated and solved optimally, which aims to pick up the device-block pairs with the best C2 performance while satisfying related constraints. Through extensive experiments conducted on the GLUE benchmark, our results demonstrate the proposed depth-aware block allocation for LoLa DEFT achieves a substantial acceleration in fine-tuning a RoBERTa model compared with traditional computation offloading scheme.  © 2024 IEEE.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1280.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
