---
id: paper-2474
title: Deploying Edge LLMs for Wafer Defect Detection in Chip Manufacturing
authors:
- Zhou, Xiaolei
- Zhang, Yuanjie
- Sun, Songyu
- Wen, Chenyi
- Yan, Zheyu
venue: 2025 International Symposium of Electronics Design Automation, ISEDA 2025
venue_type: conference
year: 2025
doi: 10.1109/ISEDA65950.2025.11100398
url: https://www.scopus.com/pages/publications/105014239130?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7--11
keywords:
- defect detection
- edge devices
- large language model
- model compression
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-2474 — Deploying Edge LLMs for Wafer Defect Detection in Chip Manufacturing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wafer defect detection in chip manufacturing is critical to ensuring yield and minimizing costly production delays. However, traditional cloud-based methods face challenges related to latency and data privacy constraints. This work investigates the deployment of edge-optimized large language models (LLMs) to enable localized, low-latency anomaly detection across fabrication processes. It analyzes existing edge AI frameworks for manufacturing analytics, emphasizing their limitations in processing scanning electron microscopy (SEM) image data with dynamic process variations. The integration of lightweight LLMs with edge computing architectures is proposed as a solution, leveraging model compression and hardware-aware optimization to balance accuracy and inference speed. By integrating the widely adopted FabGPT model into edge platforms, this approach compresses the model size by 3.12× and achieves a 6.87× speedup, and achieves a model size of 2.40 GB and a response throughput of 3.06 token/s on Jetson Nano. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2474.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
