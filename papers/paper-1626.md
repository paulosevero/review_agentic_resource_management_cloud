---
id: paper-1626
title: MATD3-Based End-Edge Collaborative Resource Optimization for NOMA-Assisted Industrial Wireless Networks
authors:
- Hao, Ru
- Xu, Chi
- Liu, Jing
venue: Computers, Materials and Continua
venue_type: journal
year: 2025
doi: 10.32604/cmc.2024.059689
url: https://www.scopus.com/pages/publications/85218123631?origin=resultslist
publisher: Tech Science Press
pages: 3203--3222
keywords:
- Industrial wireless networks (IWNs)
- multi-access edge computing (MEC)
- non-orthogonal multiple access (NOMA)
- resource allocation
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1626 — MATD3-Based End-Edge Collaborative Resource Optimization for NOMA-Assisted Industrial Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Non-orthogonal multiple access (NOMA) technology has recently been widely integrated into multi-access edge computing (MEC) to support task offloading in industrial wireless networks (IWNs) with limited radio resources. This paper minimizes the system overhead regarding task processing delay and energy consumption for the IWN with hybrid NOMA and orthogonal multiple access (OMA) schemes. Specifically, we formulate the system overhead minimization (SOM) problem by considering the limited computation and communication resources and NOMA efficiency. To solve the complex mixed-integer nonconvex problem, we combine the multi-agent twin delayed deep deterministic policy gradient (MATD3) and convex optimization, namely MATD3-CO, for iterative optimization. Specifically, we first decouple SOM into two sub-problems, i.e., joint sub-channel allocation and task offloading sub-problem, and computation resource allocation sub-problem. Then, we propose MATD3 to optimize the sub-channel allocation and task offloading ratio, and employ the convex optimization to allocate the computation resource with a closed-form expression derived by the Karush-Kuhn-Tucker (KKT) conditions. The solution is obtained by iteratively solving these two sub-problems. The experimental results indicate that the MATD3-CO scheme, when compared to the benchmark schemes, significantly decreases system overhead with respect to both delay and energy consumption. Copyright © 2025 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1626.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
