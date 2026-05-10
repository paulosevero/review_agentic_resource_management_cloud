---
id: paper-2154
title: 'Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches'
authors:
- Singh, Aditi
- Ehtesham, Abul
- Lambe, Mahesh
- Grogan, Jared
- Singh, Abhishek
- Kumar, Saket
- Muscariello, Luca
- Pandey, Vijoy
- De Saint Marc, Guillaume Sauvage
- Chari, Pradyumna
- Raskar, Ramesh
venue: Proceedings - 2025 IEEE 7th International Conference on Cognitive Machine Intelligence, CogMI 2025
venue_type: conference
year: 2025
doi: 10.1109/CogMI67134.2025.00067
url: https://www.scopus.com/pages/publications/105036090987?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 507--515
keywords:
- Agentic web
- decentralized identity
- Healthcare AI
- registry
- trust
- verifiable credentials
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2154 — Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous AI agents now operate across cloud, enterprise, and decentralized domains, creating demand for registry infrastructures that enable trustworthy discovery, capability negotiation, and identity assurance. We analyze five prominent approaches: (1) MCP Registry (centralized publication of mcp.json descriptors), (2) A2A Agent Cards (decentralized self-describing JSON capability manifests), (3) AGNTCY Agent Directory Service (IPFS Kademlia DHT content routing extended for semantic taxonomy-based content discovery, OCI artifact storage, and Sigstore-backed integrity), (4) Microsoft Entra Agent ID (enterprise SaaS directory with policy and zero-trust integration), and (5) NANDA Index AgentFacts (cryptographically verifiable, privacy-preserving fact model with credentialed assertions). Using four evaluation dimensions - security, authentication, scalability, and maintainability - we surface architectural trade-offs between centralized control, enterprise governance, and distributed resilience. We conclude with design recommendations for an emerging Internet of AI Agents requiring verifiable identity, adaptive discovery flows, and interoperable capability semantics. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2154.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
