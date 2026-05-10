---
id: paper-2745
title: 'HADA: Human-AI Agent Decision Alignment Architecture'
authors:
- Pitkäranta, Tapio
- Pitkäranta, Leena
venue: Communications in Computer and Information Science
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-15632-7_5
url: https://www.scopus.com/pages/publications/105029086318?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 78--102
keywords:
- Agentic AI
- AI Alignment Problem
- Large Language Models (LLM)
- Multi-Agent Systems (MAS)
- Natural-Language Interaction
- Reference Architecture
- Value Alignment
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

# paper-2745 — HADA: Human-AI Agent Decision Alignment Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Problem & Motivation. The generative AI boom is spawning rapid deployment of diverse LLM software agents. New standards such as the Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols let agents share data and tasks, yet organizations still lack a rigorous way to keep those agents - and legacy algorithms - aligned with organizational targets and values. Objectives of the Solution. We aim to deliver a software reference architecture that (i) provides every stakeholder natural-language interaction across planning horizons with software agents and AI algorithmic logic, (ii) provides a multi-dimensional way for aligning stakeholder targets and values with algorithms and agents, (iii) provides an example for jointly modelling AI algorithms, software agents, and LLMs, (iv) provides a way for stakeholder interaction and alignment across time scales, (v) scales to thousands of algorithms and agents while remaining auditable, (vi) remains framework-agnostic, allowing the use of any underlying LLM, agent library, or orchestration stack without requiring redesign. Design & Development. Guided by the Design-Science Research Methodology (DSRM), we engineered HADA (Human-Algorithm Decision Alignment)-a protocol-agnostic, multi-agent architecture that layers role-specific interaction agents over both Large-Language Models and legacy decision algorithms. Our reference implementation containerises a production credit-scoring model, getLoanDecision, and exposes it through stakeholder agents (business manager, data scientist, auditor, ethics lead and customer), enabling each role to steer, audit and contest every decision via natural-language dialogue. The resulting constructs, design principles and justificatory knowledge are synthesised into a mid-range design theory that generalises beyond the banking pilot. Demonstration. HADA is instantiated on a cloud-native stack-Docker, Kubernetes and Python-and embedded in a retail-bank sandbox. Five scripted scenarios show how business targets, algorithmic parameters, decision explanations and ethics triggers propagate end-to-end through the HADA architecture. Evaluation. Walkthrough observation and log inspection were used to gauge HADA against six predefined objectives. A stakeholder–objective coverage matrix showed 100 % fulfilment: every role could invoke conversational control, trace KPIs and values, detect and correct bias (ZIP-code case), and reproduce decision lineage-without dependence on a particular agent hierarchy or LLM provider. Contributions. The research delivers (i) an open-source HADA reference architecture, (ii) an evaluated mid-range design theory for human–AI alignment in multi-agent settings, and (iii) empirical evidence that framework-agnostic, protocol-compliant stakeholder agents can simultaneously enhance accuracy, transparency and ethical compliance in real-world decision pipelines. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2745.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
