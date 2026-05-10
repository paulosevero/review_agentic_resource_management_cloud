---
id: paper-0802
title: Improved Conflict-Based Search for the Virtual Network Embedding Problem
authors:
- Zheng, Yi
- Ravi, Srivatsan
- Kline, Erik
- Thurlow, Lincoln
- Koenig, Sven
- Satish Kumar, T.K.
venue: Proceedings - International Conference on Computer Communications and Networks, ICCCN
venue_type: conference
year: 2023
doi: 10.1109/ICCCN58024.2023.10230188
url: https://www.scopus.com/pages/publications/85173574645?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- conflict-based heuristic search
- network virtualization
- virtual network embedding
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0802 — Improved Conflict-Based Search for the Virtual Network Embedding Problem

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Virtualization is the mechanism of creating virtual representations of physical resources. It is now integrated into almost every facet of computing and is pervasive on the Internet: ranging from data center services and cloud computing services to services on our phones. The common goal for virtualization providers is to ensure that the physical resources are managed efficiently and effectively. This goal induces the Virtual Network Embedding (VNE) problem: the task of properly allocating the physical resources of a network to satisfy virtual requests for resources under various constraints while ensuring the quality of service and maximizing resource utilization. The VNE problem captures many resource allocation tasks arising in computer systems and computer networks. In this paper, we present Improved VNE-CBS (iVNE-CBS) as an efficient and effective algorithm for solving the VNE problem. iVNE-CBS builds on Conflict-Based Search (CBS), a heuristic search framework borrowed from the Multi-Agent Path Finding literature. We show that iVNECBS significantly outperforms popular baseline VNE algorithms: it scales to networks with several hundreds of vertices and thousands of edges, while also producing better-quality solutions. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0802.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
