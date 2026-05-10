---
id: paper-1806
title: 'IPCS: Interior-Point Method based Client Selection for Federated Learning'
authors:
- Li, Xuerui
- Zhao, Yangming
- Qiao, Chunming
venue: 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCC65529.2025.11148666
url: https://www.scopus.com/pages/publications/105017802401?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Client Selection
- Convex Optimization
- Federated Learning
- Reinforcement Learning
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1806 — IPCS: Interior-Point Method based Client Selection for Federated Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) excel in many applications, but their centralized training limits access to distributed data and computational resources, hindering scalability. Federated learning (FL) offers a promising solution by enabling collaborative training. In practical large-scale implementations, federated learning typically adopts a multitiered architecture rather than a conventional flat structure. This hierarchical approach incorporates multiple layers of edge servers that mediate between the cloud server and end devices, forming the multi-level federated learning. However, optimizing client and server selection in such complex systems remains a critical challenge. Traditional Multi-armed Bandit (MAB)based client selection methods yield suboptimal local choices in multi-level FL systems due to their inability to account for global constraints imposed by neighboring nodes. To overcome this limitation, we introduce Interior-Point Method based Client Selection (IPCS), a novel approach that leverages Interior-point Policy Convex Optimization (IPO) to enhance client and server selection in real-world multi-level federated learning. Unlike MAB-based methods, IPCS transforms the selection objective into a logarithmic barrier function, enabling it to efficiently identify the global optimum under complex hierarchical constraints. Our experiments demonstrate that IPCS significantly outperforms MAB-based methods and another state-of-the-art baseline, achieving higher model accuracy, faster convergence, and lower communication costs. These results highlight the effectiveness of IPCS in optimizing largescale, multi-level federated learning systems, paving the way for more scalable and efficient LLM training frameworks.  © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1806.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
