---
id: paper-2187
title: 'SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation'
authors:
- Sun, Shuyi
- Chen, Zhiyuan
- Shi, Dina
- Li, Chaofan
- Wu, Zhenghao
- Malazi, Hadi Tabatabaee
venue: Proceedings - 2025 IEEE International Conference on Cloud Computing Technology and Science, CloudCom 2025
venue_type: conference
year: 2025
doi: 10.1109/CloudCom67567.2025.11331438
url: https://www.scopus.com/pages/publications/105034656576?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Building automation
- Edge intelligence
- Event-driven architecture
- Intent-based systems
- Internet of things
- Large language models
- Real-time command interpretation
- Serverless computing
- Sustainable computing
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

# paper-2187 — SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Building automation is a representative AIoT-driven cyber-physical scenario, where intelligent systems interact with physical devices to manage lighting, climate, and appliances in real time. Traditional machine learning struggles with ambiguous, multilingual, and colloquial user inputs, limiting effectiveness in dynamic building environments. Recent advances in large language models (LLMs) enable more natural command interpretation, but high resource demands challenge their sustainable deployment on edge nodes. This paper proposes a serverless architecture based on event-driven microservices and container orchestration that dynamically manages the deployment, execution, and scaling of compact, fine-tuned LLMs across distributed edge nodes for building automation. We fine-tune compact LLMs with ambiguous and colloquial command examples to enhance robustness and enable context-aware deployment at the edge. Platform elasticity, enabled by Knative, allows rapid model adaptation without persistent resource allocation. We evaluate the system on a multilingual building automation dataset (Chinese, English, French) with ambiguous and colloquial commands, using an automated framework to assess interpretation and execution. Results show that the fine-tuned model outperforms the baseline Qwen-2.5-14B on five of six metrics and performs comparably on output format compliance. It also generalizes well across languages, although fuzzy instructions remain challenging. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2187.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
