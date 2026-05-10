---
id: paper-2511
title: 'AI-native cloud-edge orchestration for 6G metaverse networks: an LLM-guided multi-agent DRL approach'
authors:
- Ayepah-Mensah, Daniel
- Ghebreziabiher, Amine Kidane
- Boateng, Gordon Owusu
- Mizouni, Rabeb
- Mourad, Azzam
- Otrok, Hadi
- Bentahar, Jamal
venue: Complex and Intelligent Systems
venue_type: journal
year: 2026
doi: 10.1007/s40747-026-02249-9
url: https://www.scopus.com/pages/publications/105034872052?origin=resultslist
publisher: Springer International Publishing
pages: ''
keywords:
- AI-native orchestration
- Deep reinforcement learning
- Edge computing
- Large language models
- Microservice placement
- Retrieval-augmented generation (RAG)
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2511 — AI-native cloud-edge orchestration for 6G metaverse networks: an LLM-guided multi-agent DRL approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Emerging metaverse experiences, including interactive extended reality (XR) sessions and live holographic telepresence, necessitate motion-to-photon latencies of less than 10 ms. These applications must also manage the continuous streaming of multi-gigabit data volumes to thousands of mobile users. To meet these extreme requirements, an orchestration layer capable of instantly decomposing, placing, and adapting the dependency structures of microservices formally modeled as directed acyclic graphs (DAGs) underlying computationally intensive artificial intelligence (AI)-driven immersive applications is required. We propose an AI-native cloud-edge orchestration framework in which a Large Language Model (LLM) based cloud planner serves as a cognitive conductor. This planner uses Topology-Aware Retrieval-Augmented Generation (TopoRAG) to retrieve and interpret historical deployment traces to create latency-optimized orchestration plans. Trust-weighted logits, semantic cost estimates, and initial node bindings are output as soft priors and streamed to decentralized edge workers powered by deep reinforcement learning (DRL) with multiple agents. These DRL agents integrate global intentions with rapidly changing local conditions to enable real-time context-aware planning. In addition, we introduce a deviation-based reward mechanism that compares actual execution costs with estimates predicted by the LLM, providing dense and informative feedback that effectively halves the DRL convergence time. Simulations in urban-scale 6G networks with real-time volumetric video stitching and multiuser XR gaming workloads show a significant reduction in SLA violations and significantly lower end-to-end latency compared to baseline schedulers, while maintaining optimal motion-to-photon latency. © The Author(s) 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2511.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
