---
id: paper-1822
title: 'ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services'
authors:
- Li, Yiting
- Wang, Desheng
- Zhang, Weizhe
- Chen, Sichao
- Feng, Yuming
venue: Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS
venue_type: conference
year: 2025
doi: 10.1109/ICPADS67057.2025.11323056
url: https://www.scopus.com/pages/publications/105032492705?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Cold Start
- LLM inference
- Scalability
- Serverless
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

# paper-1822 — ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Inference of large language models (LLMs) is common in cloud environments. As the elastic resource management capabilities and the flexible pay-as-you-go billing model offered by serverless, LLM inference services are increasingly migrated to serverless platforms. However, the increasing size of LLMs in recent years has introduced a new cold start issue for serverless frameworks, which in turn impacts their scalability under dynamic workloads. To address these issues, we propose ServerlessLego, an elastic serverless computing framework. ServerlessLego partitions LLMs into layers, then groups and deploys them to different instances, and loads these groups in parallel. These instances perform a subscription-based pipeline. To address dynamically request loads, ServerlessLego models the incoming request patterns and the inference time of running requests, providing an SLO-Aware instance scheduling. Experiments show that ServerlessLego reduces the cold start time of serverless frameworks by 58.15 % and improves throughput by 43.39 % compared to the baseline for dynamic workloads. Moreover, ServerlessLego can horizontally schedule instance based on request SLOs and arrival rates. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1822.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
