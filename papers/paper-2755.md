---
id: paper-2755
title: 'Deploying Efficient LLM Agents on Maritime Autonomous Surface Ships: Fine-Tuning, RAG, and Function Calling in a Mid-Size Model'
authors:
- Ren, Yiling
- Chen, Mozi
- Weng, Junjie
- Zhang, Shengkai
- Xiao, Xuedou
- Liu, Kezhong
venue: Information (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/info17030284
url: https://www.scopus.com/pages/publications/105033859103?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- decision support systems
- edge computing
- large language models
- low-rank adaptation
- maritime autonomous surface ships
- retrieval-augmented generation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2755 — Deploying Efficient LLM Agents on Maritime Autonomous Surface Ships: Fine-Tuning, RAG, and Function Calling in a Mid-Size Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying Large Language Models (LLMs) on Maritime Autonomous Surface Ships (MASS) entails a critical trade-off between reasoning depth, inference latency, and hardware constraints. To fill the existing gap, we introduce MARTIAN (Maritime Agent for Real-time Tactical Inference And Navigation), a 14B-parameter decision support agent engineered for edge deployment on standard vessel hardware (e.g., the NVIDIA Jetson AGX Orin). Central to our approach is the Cognitive Core architecture, which utilizes a verified dataset of 21,800 Chain-of-Thought (CoT) instruction–response pairs to align general linguistic capabilities with maritime procedural logic. Empirical evaluations demonstrate that MARTIAN achieves an overall accuracy of 73.23% (SFT only) and 81.16% (SFT + RAG) on the Bilingual Maritime Multiple-Choice Questionnaire (BM-MCQ), a standardized assessment dataset constructed based on Officer of the Watch (OOW) competencies. Notably, the SFT-only configuration attains 78.53% on pure-logic-intensive COLREG tasks—surpassing the 72B-parameter Qwen-2.5 foundation model in this domain—while maintaining a real-time inference latency of 22.4 ms/token. Crucially, our ablation studies support a nuanced Interference Hypothesis: while RAG significantly enhances factual recall in knowledge-intensive domains (boosting total accuracy from 73.23% to 81.16%), it concurrently introduces semantic noise that degrades performance in pure logic reasoning tasks (e.g., COLREG maneuvering accuracy decreases from 78.53% to 77.36%). On the basis of this finding, we identify and empirically motivate a decoupled cognitive design principle that separates procedural reflexes (via SFT) from declarative knowledge (via RAG). While the full implementation of an adaptive routing mechanism is deferred to future work, the ablation results presented herein offer a validated, cost-effective reference architecture for deploying transparent and regulation-compliant AI on resource-constrained merchant vessels. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2755.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
