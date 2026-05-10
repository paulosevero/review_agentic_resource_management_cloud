---
id: paper-2112
title: Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems
authors:
- Seisa, Achilleas Santi
- Kotpalliwar, Shruti
- Satpute, Sumeet Gajanan
- Nikolakopoulos, George
venue: European Control Conference (Piscataway, N.J. Online), ECC
venue_type: conference
year: 2025
doi: 10.23919/ECC65951.2025.11187111
url: https://www.scopus.com/pages/publications/105030960225?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2907--2913
keywords:
- Closed loop control systems
- Control theory
- Controllers
- Covariance matrix
- Curve fitting
- Memory architecture
- Parameter estimation
- Regression analysis
- Resource allocation
- Collision-free trajectory
- Computational resources
- Covariance matrices
- Edge-based
- Least square minimization techniques
- Multiagent systems (MASs)
- Parameters estimates
- Polynomial regression models
- Resources allocation
- Second-order polynomial
- Multi agent systems
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2112 — Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article presents a novel edge-based architecture to dynamically allocate resources to edge-offloaded controllers for multi-agent systems. The proposed controllers are designed to generate collision-free trajectories to track the desired reference positions. The computational complexity of the controllers' problem is estimated by a second-order polynomial regression model, while the Least Squares (LS) minimization technique is employed for the coefficients' estimation. The covariance matrix plays an essential role in assessing the confidence in the parameter estimates and in investigating correlations among parameters. Through this curve fitting process, we can dynamically estimate the complexity of the controllers' problem as conditions change, enabling effective and responsive resource allocation. Furthermore, a novel control law is designed to control the dynamic resource allocation, based on the measured communication and processing time delays. This approach allows us to control the controllers' response time, thereby ensuring the closed-loop system's stability. The overall architecture is enabled through a Kubernetes (k8s) cluster and is experimentally evaluated.  © 2025 EUCA.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2112.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
