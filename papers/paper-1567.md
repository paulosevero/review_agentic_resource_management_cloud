---
id: paper-1567
title: 'Service Registration, Indexing, Discovery, and Selection: An Architectural Survey Toward a GenAI-Driven Future'
authors:
- Farhoudi, Mohammad
- Shokrnezhad, Masoud
- Taleb, Tarik
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3642631
url: https://www.scopus.com/pages/publications/105024604690?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 209680--209722
keywords:
- 6G networks
- edge-cloud continuum
- generative AI
- security and trust
- semantic-awareness
- service discovery
- service indexing
- Service orchestration
- service provisioning
- service registration
- service selection
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-1567 — Service Registration, Indexing, Discovery, and Selection: An Architectural Survey Toward a GenAI-Driven Future

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of sixth-generation (6G) networks marks a paradigm shift: by unifying an edge-to-cloud computing continuum with ultra-high-performance networking, 6G will enable capabilities far beyond today’s boundaries. As use-case diversity grows exponentially and user adoption drives traffic to unprecedented and highly dynamic levels, novel service orchestration mechanisms are indispensable. In this paper, we adopt an architectural viewpoint, examining Service Registration, Indexing, Discovery, and Selection (SRIDS) as fundamental elements of 6G service provision. We first establish the theoretical foundations of SRIDS in 6G by defining its core concepts, detailing its end-to-end workflow, reviewing current standardization efforts, and projecting its future design objectives, including reliability, scalability, automaticity and adaptability, determinism, efficiency, sustainability, semantic-awareness, security, privacy, and trust. We then perform a comprehensive literature review and gap analysis encompassing both existing surveys and recent research efforts, identifying conceptual and methodological gaps that hinder unified SRIDS in 6G. Next, we introduce a taxonomy that classifies SRIDS mechanisms into centralized, distributed, decentralized, and hybrid architectures, and systematically examine the relevant studies within each category. Each work is evaluated against the extracted design objectives. Building on these findings, we propose a hybrid architectural framework, combining centralized data management to ensure consistency and agility with distributed coordination to enhance scalability in emerging 6G use cases. The framework incorporates innovative technologies, such as Generative Artificial Intelligence (GenAI). We conclude by highlighting open challenges and suggesting directions for future research. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1567.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
