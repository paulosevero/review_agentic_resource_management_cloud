---
id: paper-2563
title: 'RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks'
authors:
- El-Khatib, Rawan F.
- Zorba, Nizar
- Hassanein, Hossam S.
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3621342
url: https://www.scopus.com/pages/publications/105019580227?origin=resultslist
publisher: IEEE Computer Society
pages: 3828--3845
keywords:
- alternating direction method of multipliers (ADMM)
- computing power networks (CPNs)
- eXtreme edge computing (XEC)
- generative artificial intelligence (GenAI)
- task allocation
- uncertainty-aware systems
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2563 — RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computing Power Networks (CPNs) emerged as a promising architectural paradigm that unifies the edge and user-owned eXtreme Edge Devices (XEDs) into an orchestrated compute fabric. By leveraging opportunistic idle resources at the eXtreme Edge (XE), CPNs offer a pathway to democratize generative AI and reduce reliance on cloud monopolies. However, inference delegation within CPNs is hindered by the volatile and user-dependent nature of compute availability of XEDs. In this work, we propose RobGenX, a robust task allocation framework tailored for inference in XE-enabled CPNs under stochastic compute capacity constraints. To the best of our knowledge, RobGenX is the first work to explicitly model the uncertainty of XEDs' compute capacity. RobGenX integrates Recourse Programming (RP) to penalize overassignment and Chance-Constrained Programming (CCP) to enforce probabilistic workload guarantees, respectively. We model the task allocation problem as a two-stage chance-constrained program and obtain an equivalent deterministic reformulation using a scenario-based approach. To overcome the computational burden of the resulting Integer Linear Program (ILP), we develop a decomposition-based solution using the Alternating Direction Method of Multipliers (ADMM), which decouples the relaxed problem into parallelizable subproblems across uncertainty scenarios. Simulation results demonstrate that RobGenX and its lower complexity ADMM-based solution consistently outperform the state-of-the-art task allocation baselines, achieving up to 58% improvement in inference completion rates and 55% in assignment stability. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2563.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
