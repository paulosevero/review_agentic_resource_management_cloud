---
id: paper-2026
title: Hybrid Quantum Approximate Optimization Algorithm (HQAOA) for Efficient Blockchain Transaction Scheduling
authors:
- Paul, Soumyadip
- Chakraborty, Sarit
venue: Proceedings of 2025 3rd International Conference on Intelligent Systems, Advanced Computing, and Communication, ISACC 2025
venue_type: conference
year: 2025
doi: 10.1109/ISACC65211.2025.10969380
url: https://www.scopus.com/pages/publications/105005200039?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 864--869
keywords:
- AL-QAOA
- Blockchain
- HQAOA
- MA-QAOA
- Quantum computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2026 — Hybrid Quantum Approximate Optimization Algorithm (HQAOA) for Efficient Blockchain Transaction Scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Quantum technology offers a transformative approach to solving complex computational challenges in decentralized systems, particularly in blockchain transaction scheduling. Efficient transaction scheduling is critical in distributed ledger systems, which often face challenges like dynamic transaction loads. This work proposes a novel approach namely Hybrid Quantum Approximate Optimization Algorithm (HQAOA) which combines Multi-Agent QAOA (MA-QAOA) and Adaptive Layer QAOA (AL-QAOA) to provide a robust solution to such issues. HQAOA leverages a decentralized optimization framework where multiple agents, each representing a node in the network, optimize local transaction scheduling while considering global constraints. Additionally, HQAOA adapts to varying transaction loads by dynamically adjusting the number of quantum layers for each agent, ensuring computational efficiency under different conditions. Such dynamic layer adjustment mechanisms mitigate the adverse effects of quantum noise and ensures optimal performance in scenarios with fluctuating transaction loads. In contrast to traditional QAOA, which struggles with noise and scaling issues, HQAOA provides improved performance by balancing the complexity of the problem with available quantum resources. Experimental results signify the future potential of HQAOA to outperform QAOA, particularly in noisy environments and irregular transaction conditions. This work demonstrates the potential of HQAOA to optimize blockchain transaction scheduling in decentralized systems. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2026.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
