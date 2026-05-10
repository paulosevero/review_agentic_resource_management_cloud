---
id: paper-2208
title: Decentralized and Dynamic Zero-Touch Provisioning of Leaf-Spine EVPN Data Centers
authors:
- Tavares, Martim
- Valadas, Rui
- Amado, Tiago
- Paz, Marlon
- Santos, Sérgio
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3589509
url: https://www.scopus.com/pages/publications/105011161483?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 125190--125206
keywords:
- cloud networks
- EVPN
- leaf-spine data center
- Network automation
- zero-touch network provisioning
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

# paper-2208 — Decentralized and Dynamic Zero-Touch Provisioning of Leaf-Spine EVPN Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data centers are becoming increasingly large and complex due to the exponential growth of data and the rising demand for cloud services. To manage this complexity, modern data center networks employ leaf-spine topologies and EVPN overlays, enabling efficient scaling and supporting multi-tenancy. These networks often include thousands of servers and network devices, making configuration and management highly challenging. This paper proposes a decentralized and dynamic Zero-Touch Provisioning (ZTP) solution for leaf-spine EVPN data centers. Our approach employs autonomous agents on each data center router to provision both the underlay and the overlay infrastructure without manual intervention, handling both initial deployments and disruptive events (e.g., router or link failures). The underlay is assumed to use a link-state routing protocol, and we introduce a novel algorithm that infers the role of each router (e.g., leaf or spine) from the network topology provided by the protocol, a feature central to our approach. We experimentally validated our solution using SR Linux, a network operating system for data centers that supports non-native agent integration. Our results demonstrate that the proposed ZTP solution can fully provision leaf-spine data center networks automatically while achieving very fast convergence times. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2208.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
