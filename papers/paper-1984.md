---
id: paper-1984
title: Knowledge Graphs-Driven Intelligence for Distributed Decision Systems
authors:
- Napoli, Rosario
- Morabito, Gabriele
- Celesti, Antonio
- Villari, Massimo
- Fazio, Maria
venue: Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
venue_type: conference
year: 2025
doi: 10.1145/3773274.3774268
url: https://www.scopus.com/pages/publications/105027113611?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: ''
keywords:
- Distributed Decision Systems
- Distributed Systems
- Knowledge Engineering
- Knowledge Sharing
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

# paper-1984 — Knowledge Graphs-Driven Intelligence for Distributed Decision Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern distributed decision-making systems face significant challenges arising from data heterogeneity, dynamic environments, and the need for decentralized coordination. This paper introduces the Knowledge Sharing paradigm as an innovative approach that uses the semantic richness of Knowledge Graphs (KGs) and the representational power of Graph Embeddings (GEs) to achieve decentralized intelligence. Our architecture empowers individual nodes to locally construct semantic representations of their operational context, iteratively aggregating embeddings through neighbor-based exchanges using GraphSAGE. This iterative local aggregation process results in a dynamically evolving global semantic abstraction called Knowledge Map, enabling coordinated decision-making without centralized control. To validate our approach, we conduct extensive experiments under a distributed resource orchestration use case. We simulate different network topologies and node workloads, analyzing the local semantic drift of individual nodes. Experimental results confirm that our distributed knowledge-sharing mechanism effectively maintains semantic coherence and adaptability, making it suitable for complex and dynamic environments such as Edge Computing, IoT, and multi-agent systems. © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1984.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
