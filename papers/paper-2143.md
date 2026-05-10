---
id: paper-2143
title: Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage
authors:
- Silva, Willian P.
- Rocha, Helder O.
- Faber, Menno
- Deters, Jan K.
- Bergsma, Ewout
- Silva, Jair L.
venue: 2025 16th IEEE International Conference on Industry Applications, INDUSCON 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.1109/INDUSCON66435.2025.11241782
url: https://www.scopus.com/pages/publications/105029903177?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2214--2219
keywords:
- bandwidth optimization
- dementia monitoring
- edge computing
- fine-tuning
- LLM
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

# paper-2143 — Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we propose a novel edge-AI architecture for real-time monitoring of dementia patients using finetuned Large Language Models (LLMs) to detect and classify high-risk scenarios in a low-bandwidth environment. We use LLaMA 3.8B with 4-bit quantization and Low-Rank Adaptation (LoRA) to fine-tune the pre-trained model effectively on a specialized 'Dementia Risk Dataset' of 50,000 labeled text samples. The optimized LLM is built to execute on the network edge (e.g., on border routers), with real-time transcriptions of patient speech analyzed for identifying key events such as disorientation, wandering, refusal of care, and medication management errors, and short, structured alerts sent to the cloud. Experimental results provide quick convergence at training, accurate classification of different risk categories, and reduction in message length compared to lengthy raw transcripts. Our approach ensures patient confidentiality by avoiding continuous audio streaming, reduces communication overhead in lowbandwidth networks, and enables timely intervention by clinical professionals and caregivers. The proposed system offers an extensible solution to cognitive dementia care and demonstrates the viability of LLM deployment on low-resource edge devices for domain-specific use cases.  © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2143.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
