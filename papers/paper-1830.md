---
id: paper-1830
title: 'The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities'
authors:
- Li, Ning
- Guo, Song
- Zhang, Tuo
- Li, Muqing
- Hong, Zicong
- Zhou, Qihua
- Yuan, Xin
- Zhang, Haijun
venue: IEEE Communications Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOM.001.2400717
url: https://www.scopus.com/pages/publications/105014471164?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 164--171
keywords:
- Architecture
- Dynamics
- Memory architecture
- Mobile edge computing
- Network architecture
- Servers
- Topology
- Communication resources
- Computational resources
- Deployment architecture
- Deployment strategy
- Dynamic allocations
- Edge server
- Heterogeneous hardware
- Mixture of experts
- Property
- Ubiquitous intelligence
- Digital storage
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
    my_justification: Review
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

# paper-1830 — The MoE-Empowered Edge LLMS Deployment: Architecture, Challenges, and Opportunities

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The powerfulness of LLMS indicates that deploying various LLMS with different scales and architectures on end, edge, and cloud to satisfy different requirements and adaptive heterogeneous hardware is the critical way to achieve ubiquitous intel-ligence for 6G. However, the massive parameters of LLMS poses significant challenges in deploying them on edge servers due to high computational and storage demands. Considering that the sparse activation in Mixture of Experts (MoE) is effective on scalable and dynamic allocation of computational and communications resources at the edge, this article proposes a novel MoE-empowered col-laborative deployment framework for edge LLMS, denoted as CoEL. This framework fully leverages the properties of MoE architecture and encom-passes three key aspects: model quantization, intra-server and inter-server cooperation, and token pruning and fusion. The CoEL begins with quantizing experts based on their importance and popularity, assigning different bit widths to different experts. Then, considering the heterogeneous resources of edge servers and model deployment requirements, a multi-dimensional collaborative deployment strat-egy is proposed. This strategy employs intra-server cooperation if the compressed model can be deployed on a single edge server; otherwise, it trig-gers inter-server cooperation and deploys experts across multiple edge servers distributed. Additionally, to minimize data transmission delays between servers, a token compression approach is applied. Finally, given the dynamic of network topology, resource status, and user requirements, the deployment strategies are regularly updated to maintain its relevance and effectiveness. This article also delineates the challenges and potential research directions for the deployment of edge LLMS. © 1979-2012 IEEE.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1830.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
