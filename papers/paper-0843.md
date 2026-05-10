---
id: paper-0843
title: Privacy-Driven Security-Aware Task Scheduling Mechanism for Space-Air-Ground Integrated Networks
authors:
- Cai, Yunfei
- Yao, Haipeng
- Gong, Yongkang
- Wang, Fu
- Zhang, Ni
- Guizani, Mohsen
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3392389
url: https://www.scopus.com/pages/publications/85191335664?origin=resultslist
publisher: IEEE Computer Society
pages: 4704--4718
keywords:
- encryption configuration
- multi-agent proximal policy optimization (MAPPO)
- privacy
- Space-air-ground integrated networks (SAGIN)
- task scheduling
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

# paper-0843 — Privacy-Driven Security-Aware Task Scheduling Mechanism for Space-Air-Ground Integrated Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To implement ubiquitous intelligence of the sixth generation mobile networks (6G), space-air-ground integrated networks (SAGIN) have emerged as a promising infrastructure to provide globally seamless coverage and powerful cloud computing services. With SAGIN, Internet of Things (IoT) devices can offload compute-intensive tasks to unmanned aerial vehicles (UAVs) and satellites. However, due to the vulnerability of wireless communications to eavesdropping attacks, privacy-preserving task scheduling in SAGIN is of great challenge. To address this problem, we propose a privacy-driven multi-agent proximal policy optimization-based security-aware SAGIN task scheduling mechanism, where we jointly optimize the delay, energy consumption and security utility of tasks considering different privacy protection needs. In this mechanism, privacy protection is accomplished from two aspects. First, the privacy level of tasks and the privacy leakage risks of the communication link are fully considered in the selection of the scheduling destination. Second, we employ cryptography techniques and conceive an optimal encryption configuration scheme to achieve the most cost-effective privacy protection. Moreover, a convex optimization method is utilized to allocate CPU-cycle frequencies for computing services. In the end, simulation results demonstrate that our proposed algorithm outperforms other benchmarks in terms of convergence speed, offloading overhead and security utility of IoT devices. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0843.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
