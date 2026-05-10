---
id: paper-1475
title: Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices
authors:
- Chen, Xiaopei
- Li, Liang
- Ji, Fei
- Wu, Wen
venue: IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
venue_type: conference
year: 2025
doi: 10.1109/INFOCOMWKSHPS65812.2025.11152998
url: https://www.scopus.com/pages/publications/105017952522?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Federated learning
- Mobile computing
- Mobile edge computing
- Adaptation module
- Edge server
- Fine tuning
- Heterogeneous mobile devices
- Language model
- Learning frameworks
- Memory efficient
- Memory pressure
- Sequential manners
- Training efficiency
- Personnel training
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLMs é o workload não o tomador de decisões
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

# paper-1475 — Memory-Efficient Split Federated Learning for LLM Fine-Tuning on Heterogeneous Mobile Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we propose an edge-assisted split federated learning framework to facilitate large language model (LLM) fine-tuning on heterogeneous mobile devices while alleviating memory pressures on both mobile devices and the edge server. Specifically, mobile devices perform low-rank adaptation (LoRA) fine-tuning on only a subset of lower layers of the pre-trained LLM, tailored to their individual capacities. On the server, a full LLM is maintained, and the corresponding LoRA modules are selectively fine-tuned in a sequential manner for each device. To further enhance training efficiency, we propose a server-side training scheduling method that optimizes the processing order of devices for accelerating fine-tuning. Extensive experiments demonstrate that compared to the baselines, our scheme can reduce 79% memory footprint and 6% training time while achieving comparable performance. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLMs é o workload não o tomador de decisões"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1475.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
