---
id: paper-2607
title: Game-Based LLM Inference Task Offloading for Edge Computing System
authors:
- Hou, Shoulu
- Gan, Min
- Ni, Wei
- Zhai, Zhongyi
- Liu, Xiulei
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TGCN.2026.3676823
url: https://www.scopus.com/pages/publications/105034545687?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2490--2502
keywords:
- Edge computing
- game theory
- LLM inference task offloading
- quantization
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

# paper-2607 — Game-Based LLM Inference Task Offloading for Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs), with their powerful capabilities, are fundamentally transforming society. Cloud-based LLM deployment has drawbacks, including latency, lack of offline functionality, and high long-term costs. Edge computing-based LLM solutions address these issues by offloading inference tasks to edge servers. This paper formulates and optimizes an LLM inference framework that jointly accounts for inference time and predictive quality. Specifically, to address the natural tendency of selfish users for personal utility maximization, we develop a Game-theoretic Offloading Algorithm (GOALIT) to optimize LLM inference offloading. The approach enables distributed users to iteratively adjust their strategies and converge to a Nash equilibrium. Compared to the optimal tree-based search (OT-GAH), the proposed approach yields a 27% increase in token throughput and shortens inference latency by 20%, while maintaining lower perplexity under dynamic system loads. These findings confirm the effectiveness of our approach in resource-constrained edge environments.  © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2607.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
