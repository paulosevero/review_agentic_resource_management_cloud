---
id: paper-2220
title: Towards Orchestrating Agentic Applications as FaaS Workflows
authors:
- Tokal, Shiva Sai Krishna Anand
- Jha, Vaibhav
- Eswaran, Anand
- Jayachandran, Praveen
- Simmhan, Yogesh
venue: Proceedings - 2025 IEEE International Parallel and Distributed Processing Symposium Workshops, IPDPSW 2025
venue_type: conference
year: 2025
doi: 10.1109/IPDPSW66978.2025.00156
url: https://www.scopus.com/pages/publications/105015528025?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1003--1010
keywords:
- agent
- faas
- llm
- workflow
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

# paper-2220 — Towards Orchestrating Agentic Applications as FaaS Workflows

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Agentic applications consist of multiple agents that encapsulate tools that can be selected by an Large Language Model (LLM) to execute real-world tasks while also collaborating with other agents to solve complex applications, including scientific tasks. However, creating these agentic applications require substantial user effort, involving model selection, prompt engineering and guardrails. There are also limitation in deploying these applications on cloud platforms. In this early work, we take a step towards addressing these limitations by proposing an intuitive pattern comprising of a planner, executor, evaluator and judge agents to compose these as agentic workflows with simple prompt specifications. We also propose to model these as Function as a Service (FaaS) workflows on public/private clouds to simplify their deployment and outsourcing their orchestration. A preliminary implementation of our AgentX platform provides Python modules for these roles, which are used to compose AWS Step Functions. Our initial results on local machine and AWS using Open AI and Claude show promise in simpler compositions, but also expose challenges due to diverse behavior of LLMs. As future work, we will explore the use of our XFaaS hybrid cloud orchestration platform to deploy these on hybrid public/private clouds to leverage cost arbitrage, and offer flexible and automated selection of model to trade-off latency, accuracy and reliability.  © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2220.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
