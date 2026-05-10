---
id: paper-0833
title: 'RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics'
authors:
- Basit, Abdul
- Hussain, Khizar
- Hanif, Muhammad Abdullah
- Shafique, Muhammad
venue: 2024 18th International Conference on Control, Automation, Robotics and Vision, ICARCV 2024
venue_type: conference
year: 2024
doi: 10.1109/ICARCV63323.2024.10821547
url: https://www.scopus.com/pages/publications/85217420538?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 710--717
keywords:
- Automatic Speech Recognition
- Healthcare Assistance Robot
- Large language Models
- Low-Rank Adaptation (LoRA)
- Preliminary Diagnosis
- Reinforcement Learning from Human Feedback (RLHF)
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

# paper-0833 — RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) are revolutionizing numerous domains with their remarkable natural language processing (NLP) capabilities, attracting significant interest and widespread adoption. However, deploying LLMs in resource-constrained environments, such as edge computing and robotics systems without server infrastructure, while also aiming to minimize latency, presents significant challenges. Another challenge lies in delivering medical assistance to remote areas with limited healthcare facilities and infrastructure. To address this, we introduce RoboMed, an on-premise healthcare robot that utilizes compact versions of large language models (tiny-LLMs) integrated with LangChain as its backbone. Moreover, it incorporates automatic speech recognition (ASR) models for user interface, enabling efficient, edge-based preliminary medical diagnostics and support. RoboMed employs model optimizations to achieve minimal memory footprint and reduced latency during inference on embedded edge devices. The training process optimization involves low-rank adaptation (LoRA), which reduces the model's complexity without significantly impacting its performance. For fine-tuning, the LLM is trained on a diverse medical dataset compiled from online health forums, clinical case studies, and a distilled medicine corpus. This fine-tuning process utilizes reinforcement learning from human feedback (RLHF) to further enhance its domain-specific capabilities. The system is deployed on Nvidia Jetson development board and achieves 78% accuracy in medical consultations and scores 56 in USMLE benchmark, enabling an resource-efficient healthcare assistance robot that alleviates privacy concerns due to edge-based deployment, thereby empowering the community.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0833.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
