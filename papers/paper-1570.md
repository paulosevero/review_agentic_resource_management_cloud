---
id: paper-1570
title: 'Toward Deterministic Path Placement in AI Backends: A Practical SRv6-Based Architecture'
authors:
- Filsfils, Clarence
- Camarillo, Pablo
- Abdelsalam, Ahmed
- Quinci, Arianna
- Tulumello, Angelo
- Mayer, Andrea
- Loreti, Pierpaolo
- Bracciale, Lorenzo
- Salsano, Stefano
venue: 'Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025'
venue_type: conference
year: 2025
doi: 10.23919/CNSM67658.2025.11297568
url: https://www.scopus.com/pages/publications/105032117663?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI workloads
- congestion control
- datacenter fabrics
- programmable networks
- RoCEv2
- SRv6
- traffic engineering
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1570 — Toward Deterministic Path Placement in AI Backends: A Practical SRv6-Based Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed training of artificial intelligence models, such as Large Language Models (LLMs), generates highly structured and intense traffic patterns between GPUs, with synchronous and repetitive flows that can easily cause congestion and bottlenecks in data center networks. In this context, currently adopted protocols, such as RoCEv2, show significant limitations in the presence of bursty traffic and low entropy, compromising overall system efficiency. Segment Routing over IPv6 (SRv6) offers a programmable mechanism to steer AI workload traffic along explicitly chosen paths, enabling precise and congestion-aware routing under dynamic conditions. Lightweight monitoring modules can detect congestion conditions in real time and report them to the orchestrator or NICs, enabling dynamic rerouting decisions without requiring control-plane signaling or state in the fabric. SRv6 micro-segment (uSID) encoding allows the NIC to steer traffic along alternate, congestion-free paths simply by updating the IPv6 destination address, preserving RoCEv2 semantics while ensuring rapid adaptability. This work provides a practical implementation and experimental validation of the recent IETF Internet-Draft 'SRv6 for Deterministic Path Placement in AI Backends', demonstrating its feasibility and performance benefits in RoCEv2-based infrastructures. The results highlight the potential of SRv6 as a practical and vendor-agnostic solution to enhance networking efficiency in modern AI datacenters.  © 2025 IFIP.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1570.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
