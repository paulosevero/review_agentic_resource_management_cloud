---
id: paper-0901
title: Self-Learning Multi-Mode Slicing Mechanism for Dynamic Network Architectures
authors:
- Esmat, Haitham H.
- Lorenzo, Beatriz
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2023.3305975
url: https://www.scopus.com/pages/publications/85168672924?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1048--1063
keywords:
- Dynamic network architectures
- fog/edge/cloud
- multi-agent actor-critic
- network slicing
- risk model
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

# paper-0901 — Self-Learning Multi-Mode Slicing Mechanism for Dynamic Network Architectures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic network architectures that utilize communication, computing, and storage resources at the wireless edge are key to delivering emerging services in next-generation networks (e.g., AR/VR, 3D video, intelligent cars, etc). Network slicing can be significantly enhanced by including dynamically available resources throughout the fog/edge/cloud continuum and using mmWave/THz bands. However, network slicing of dynamic multi-tier computing networks remains under-explored. In this paper, we present a self-learning end-to-end network slicing mechanism (SELF-E2E-NS) that facilitates collaboration between the Infrastructure Provider (InP) and tenants to slice their subscribers' resources (i.e., radio, computing, and storage) as fog resources. To adapt to the uncertain availability of resources at the edge and minimize the risk of non-satisfying service level agreements (SLAs), our slicing mechanism has two operational modes. Operational mode 1 is for joint network slicing (JNS) in which the InP infrastructure is augmented with fog resources and jointly sliced to meet high throughput and delay tolerant requirements. Operational mode 2 is for independent network slicing (INS) in which the InP infrastructure and fog resources are sliced separately to achieve high throughput, low-latency, and high-reliability requirements. Our schemes leverage mmWave/THz, fog/edge/cloud computing, and caching to achieve new service requirements. We design a DQ-E2E-JNS algorithm that uses Deep Dueling network and a MAAC-E2E-INS algorithm based on multi-agent actor-critic, which incorporate service-aware pricing feedback and fog trading matching, respectively. These algorithms find the optimal slice request admission and collaboration policy that maximizes the long-term revenue of the InP and tenants for each mode. The simulation results show that our novel slicing mechanism can serve up to 4 times more requests and effectively exploits different spectrum bands and fog resources to improve revenue and performance.  © 1993-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0901.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
