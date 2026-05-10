---
id: paper-2939
title: 'Model Fusion for Scalable and Sustainable Artificial Intelligence: A Review and Outlook'
authors:
- Zhou, Qi
- Zhang, Yiming
- Gu, Yanggan
- Wang, Yuanyi
- Yan, Zhaoyi
- Li, Zhen
- Chung, Chi Yung
- Yang, Hongxia
venue: Journal of Modern Power Systems and Clean Energy
venue_type: journal
year: 2026
doi: 10.35833/MPCE.2025.000973
url: https://www.scopus.com/pages/publications/105029983368?origin=resultslist
publisher: State Grid Electric Power Research Institute Nanjing Branch
pages: 37--49
keywords:
- Artificial intelligence (AI)
- large language model (LLM)
- model fusion
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2939 — Model Fusion for Scalable and Sustainable Artificial Intelligence: A Review and Outlook

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have achieved remarkable progress in recent years. Nevertheless, the prevailing centralized paradigm for training generative artificial intelligence (AI) is increasingly approaching its structural limits. First, the concentration of large-scale graphics processing unit (GPU) clusters restricts the access to the pretraining stage, confining the fundamental model development to a small number of resource-rich institutions. Second, the economic and energy costs associated with operating massive data centers render this paradigm progressively less sustainable. Third, the hardware gatekeeping narrows the participation to computer science specialists, limiting the involvement of domain experts who are essential for high-impact applications. Finally, small- and mediumsized enterprises remain dependent on expensive application programming interface (APIs) or shallow fine-tuning methods that are insufficient to modify the core knowledge of a model. Together, these constraints impede innovation and hinder equitable access to next-generation AI systems. Model fusion offers a scalable alternative by integrating multiple specialized models without retraining from scratch. This paper analyzes the current landscape of model fusion, outlining the strengths and limitations of existing methods and discussing future directions. We highlight recent advances such as InfiFusion, InfiGFusion, and InfiFPO, which improve the alignment and scalability through techniques like top-K logit selection, graph-based distillation, and preference optimization. These techniques demonstrate substantial efficiency and reasoning gains, pointing toward a more accessible and resource-aware paradigm for large-scale model development. Finally, we discuss the practical applicability of model fusion, using the energy domain as an illustrative example. © 2013 State Grid Electric Power Research Institute.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2939.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
