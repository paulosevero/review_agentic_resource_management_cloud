---
id: paper-0865
title: 'OTAS: An Elastic Transformer Serving System via Token Adaptation'
authors:
- Chen, Jinyu
- Xu, Wenchao
- Hong, Zicong
- Guo, Song
- Wang, Haozhao
- Zhang, Jie
- Zeng, Deze
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2024
doi: 10.1109/INFOCOM52122.2024.10621087
url: https://www.scopus.com/pages/publications/85201819755?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1021--1030
keywords:
- cloud computing
- elastic computing
- model serving
- transformer
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

# paper-0865 — OTAS: An Elastic Transformer Serving System via Token Adaptation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Transformer model empowered architectures have become a pillar of cloud services that keeps reshaping our society. However, the dynamic query loads and heterogeneous user requirements severely challenge current transformer serving systems, which rely on pre-training multiple variants of a foundation model, i.e., with different sizes, to accommodate varying service demands. Unfortunately, such a mechanism is unsuitable for large transformer models due to the additional training costs and excessive I/O delay. In this paper, we introduce OTAS, the first elastic serving system specially tailored for transformer models by exploring lightweight token management. We develop a novel idea called token adaptation that adds prompting tokens to improve accuracy and removes redundant tokens to accelerate inference. To cope with fluctuating query loads and diverse user requests, we enhance OTAS with application-aware selective batching and online token adaptation. OTAS first batches incoming queries with similar service-level objectives to improve the ingress throughput. Then, to strike a tradeoff between the overhead of token increment and the potentials for accuracy improvement, OTAS adaptively adjusts the token execution strategy by solving an optimization problem. We implement and evaluate a prototype of OTAS with multiple datasets, which show that OTAS improves the system utility by at least 18.2%. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0865.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
