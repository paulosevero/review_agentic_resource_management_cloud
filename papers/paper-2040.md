---
id: paper-2040
title: A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks
authors:
- Picano, Benedetta
- Hoang, Dinh Thai
- Nguyen, Diep N.
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2025
doi: 10.1109/OJCOMS.2025.3561605
url: https://www.scopus.com/pages/publications/105002837963?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3795--3805
keywords:
- distributed inference
- edge intelligence
- Foundation models
- matching theory
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
    my_justification: LLM as workload
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

# paper-2040 — A Matching Game for LLM Layer Deployment in Heterogeneous Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the growing demand for computational and storage capabilities of modern learning models, performing their computation exclusively in a centralized manner has become increasingly impractical. Executing the inference of foundation models in a distributed manner presents significant challenges, particularly in optimizing both computing and communication resources. This work introduces a novel deployment scheme for large language model (LLM) layers that jointly considers computation and communication efficiency within an edge network environment to address these issues. Specifically, we resort to the matching theory to effectively orchestrate the distributed deployment of the LLM layers across the edge nodes of the networks, where nodes have varying computational capacities and communication speed. This framework is based on a two-sided game, enabling each layer to express its individual preferences for node allocation while allowing nodes to prioritize their preferred layers. This mutual selection process minimizes inference latency in the learning process and models the bubble time as game externalities, assuming a sequential pipeline execution. The algorithmic solution reaches a stable matching outcome. Performance evaluation was conducted considering both simulations and a small-scale testbed to measure the effectiveness of the proposed algorithm compared to state-of-the-art alternatives. In particular, the small-scale testbed was developed to distribute an LLM to support autonomous driving, leveraging the vision-language model paradigm. The results highlight performance improvements of up to around 10% in comparison to the Koklata game alternative. © 2020 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2040.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
