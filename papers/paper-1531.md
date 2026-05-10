---
id: paper-1531
title: Intelligence-Based Active Inference for Robots with Multimodal Large Language Models and Edge Computing
authors:
- Dong, Huorong
- He, Ying
- Yu, F. Richard
- Zhang, Guangzheng
- He, Biao
- Wang, Jia
venue: IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
venue_type: conference
year: 2025
doi: 10.1109/INFOCOMWKSHPS65812.2025.11152914
url: https://www.scopus.com/pages/publications/105017958799?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Active inference
- intelligence
- multimodal large language models
- resource allocation
- robots
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1531 — Intelligence-Based Active Inference for Robots with Multimodal Large Language Models and Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of artificial intelligence technologies, multimodal large language models (MLLMs) have demonstrated outstanding performance in handling various complex tasks. Robots, which are crucial for automated production, rely on path planning for efficiency and precision. Thus, applying MLLMs to the path planning of robots is a natural technological progression. However, the limited hardware in robots poses challenges for efficient and timely MLLMs-based inference. While traditional deep reinforcement learning (DRL) methods can offload these inference tasks to servers, existing DRL solutions often suffer from low data efficiency and are insensitive to users' demands. To address these issues, this paper introduces an intelligence-based active inference (IAI) approach for offloading inference tasks and optimizing resource allocation in cloud-edge networks. Experimental results demonstrate that our proposed method outperforms mainstream DRL approaches in terms of data efficiency and better accommodates user dynamic requirements. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1531.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
