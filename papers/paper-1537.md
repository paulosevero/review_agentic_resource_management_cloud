---
id: paper-1537
title: Distributed allocation and resource scheduling algorithms resilient to link failure
authors:
- Doostmohammadian, Mohammadreza
- Pequito, Sergio
venue: European Journal of Control
venue_type: journal
year: 2025
doi: 10.1016/j.ejcon.2025.101405
url: https://www.scopus.com/pages/publications/105019366708?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Convex optimization
- Distributed resource allocation
- Graph theory
- Percolation theory
- Time-delay
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1537 — Distributed allocation and resource scheduling algorithms resilient to link failure

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed resource allocation (DRA) is fundamental to modern networked systems, spanning applications from economic dispatch in smart grids to CPU scheduling in data centers. Conventional DRA approaches require reliable communication, yet real-world networks frequently suffer from link failures, packet drops, and communication delays due to environmental conditions, network congestion, and security threats. We introduce a novel resilient DRA algorithm that addresses these critical challenges, and our main contributions are as follows: (1) guaranteed constraint feasibility at all times, ensuring resource-demand balance even during algorithm termination or network disruption; (2) robust convergence despite sector-bound nonlinearities at nodes/links, accommodating practical constraints like quantization and saturation; and (3) optimal performance under merely uniformly-connected networks, eliminating the need for continuous connectivity. Unlike existing approaches that require persistent network connectivity and provide only asymptotic feasibility, our graph-theoretic solution leverages network percolation theory to maintain performance during intermittent disconnections. This makes it particularly valuable for mobile multi-agent systems where nodes frequently move out of communication range. Theoretical analysis and simulations demonstrate that our algorithm converges to optimal solutions despite heterogeneous time delays and substantial link failures, significantly advancing the reliability of distributed resource allocation in practical network environments. © 2025 European Control Association

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1537.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
