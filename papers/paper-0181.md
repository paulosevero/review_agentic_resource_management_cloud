---
id: paper-0181
title: Enabling Discoverable Trusted Services for Highly Dynamic Decentralized Workflows
authors:
- Barclay, Iain
- Simpkin, Chris
- Bent, Graham
- Porta, Tom La
- Millar, Declan
- Preece, Alun
- Taylor, Ian
- Verma, Dinesh
venue: 'Proceedings of 15th Workshop on Workflows in Support of Large-Scale Science, WORKS 2020 - Held in conjunction with SC 2020: The International Conference for High Performance Computing, Networking,
  Storage and Analysis'
venue_type: conference
year: 2020
doi: 10.1109/WORKS51914.2020.00011
url: https://www.scopus.com/pages/publications/85099743597?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 41--48
keywords:
- linked data
- semantic web
- trusted services
- verifiable credentials
- web of things
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

# paper-0181 — Enabling Discoverable Trusted Services for Highly Dynamic Decentralized Workflows

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fifth generation (5G) mobile networks will revolutionize edge-based computing by providing fast and reliable network capabilities to remote sensors, devices and microservices. This heralds new opportunities for researchers, allowing remote instrumentation and analytic capabilities to be as accessible as local resources. The increased availability of remote data and services presents new opportunities for collaboration, yet introduces challenges for workflow orchestration, which will need to adapt to consider an increased choice of available services, including those from trusted partners and the wider community. In this paper we outline a workflow approach that provides decentralized discovery and orchestration of verifiably trustable services in support of multi-party operations. We base this work on the adoption of standardised data models and protocols emerging from hypermedia research, which has demonstrated success in using combinations of Linked Data, Web of Things (WoT) and semantic technologies to provide mechanisms for autonomous goal-directed agents to discover, execute and reuse new heterogeneous resources and behaviours in large-scale, dynamic environments. We adopt Verifiable Credentials (VCs) to securely share information amongst peers based on prior service usage in a cryptographically secure and tamperproof way, providing a trust-based framework for ratifying service qualities. Collating these new service description channels and integrating with existing decentralized workflow research based on vector symbolic architecture (VSA) provides an enhanced semantic search space for efficient and trusted service discovery that will be necessary for 5G edge-computing environments.  © 2020 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0181.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
