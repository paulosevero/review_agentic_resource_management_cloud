---
id: paper-2444
title: 'LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration'
authors:
- Zhang, Yingyi
- Jia, Pengyue
- Li, Xianneng
- Xu, Derong
- Wang, Maolin
- Wang, Yichao
- Du, Zhaocheng
- Guo, Huifeng
- Liu, Yong
- Tang, Ruiming
- Zhao, Xiangyu
venue: Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining
venue_type: conference
year: 2025
doi: 10.1145/3711896.3737036
url: https://www.scopus.com/pages/publications/105014588850?origin=resultslist
publisher: Association for Computing Machinery
pages: 3889--3900
keywords:
- cloud-device framework
- large language model
- privacy-preserving
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

# paper-2444 — LSRP: A Leader-Subordinate Retrieval Framework for Privacy-Preserving Cloud-Device Collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-device collaboration leverages on-cloud Large Language Models (LLMs) for handling public user queries and on-device Small Language Models (SLMs) for processing private user data, collectively forming a powerful and privacy-preserving solution. However, existing approaches often fail to fully leverage the scalable problem-solving capabilities of on-cloud LLMs while underutilizing the advantage of on-device SLMs in accessing and processing personalized data. This leads to two interconnected issues: 1) Limited utilization of the problem-solving capabilities of on-cloud LLMs, which fail to align with personalized user-task needs, and 2) Inadequate integration of user data into on-device SLM responses, resulting in mismatches in contextual user information. In this paper, we propose a Leader-Subordinate Retrieval framework for Privacy-preserving cloud-device collaboration (LSRP), a novel solution that bridges these gaps by: 1) enhancing on-cloud LLM guidance to on-device SLM through a dynamic selection of task-specific leader strategies named as user-to-user retrieval-augmented generation (U-U-RAG), and 2) integrating the data advantages of on-device SLMs through small model feedback Direct Preference Optimization (SMFB-DPO) for aligning the on-cloud LLM with the on-device SLM. Experiments on two datasets demonstrate that LSRP consistently outperforms state-of-the-art baselines, significantly improving question-answer relevance and personalization, while preserving user privacy through efficient on-device retrieval. Our code is available at: https://github.com/Applied-Machine-Learning-Lab/LSRP. © 2025 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2444.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
