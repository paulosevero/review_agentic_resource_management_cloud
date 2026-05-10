---
id: paper-1810
title: 'MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds'
authors:
- Li, Qixin
- Ren, Xiaoxu
- Wang, Zhongyuan
- Yao, Haipeng
- He, Yuan
- Liu, Yunhao
venue: IEEE International Workshop on Quality of Service, IWQoS
venue_type: conference
year: 2025
doi: 10.1109/IWQoS65803.2025.11143291
url: https://www.scopus.com/pages/publications/105016996899?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Containerized AI
- Edge Clouds Network
- LLM
- Microservices Deployment
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1810 — MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have emerged as a transformative advancement in artificial intelligence (AI). To fully leverage their potential, Docker containers, serving as a lightweight, portable, and isolated framework, facilitate the seamless deployment of LLM-based applications. However, the deployment of containerized AI microservices faces challenges such as heavy network loads, delayed image loading, and redundancy. In this paper, we introduce MetaPipe, an innovative incremental deployment approach for containerized AI microservices in edge cloud environments. MetaPipe aims to optimize startup times through a dynamic workflow that incorporates proactive layer pre-fetching and reinforcement layer re-scheduling. The proactive pre-fetching reduces service deployment time through layer caching prediction and pre-scheduling before requests arrive, while the reinforcement re-scheduling addresses inaccuracies by dynamically adjusting layer scheduling strategies after requests arrive. Extensive experiments on realworld datasets show that MetaPipe significantly outperforms traditional methods, achieving 83.58% reduction in initialization startup time and 85.58% reduction in cold startup time. These results highlight its effectiveness in enhancing the performance of AI microservices deployment within edge cloud environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1810.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
