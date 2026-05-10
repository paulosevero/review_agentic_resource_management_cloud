---
id: paper-2513
title: Enhanced federated reinforcement learning framework for task management in fog computing using eligibility traces and targeted model dissemination
authors:
- Azarkasb, Seyed Omid
- Khasteh, Seyed Hossein
venue: Computing
venue_type: journal
year: 2026
doi: 10.1007/s00607-025-01595-9
url: https://www.scopus.com/pages/publications/105031493413?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cross-domain policy transfer
- Eligibility traces
- Exponential Random Graph Models (ERGM)
- Federated reinforcement learning
- Fog computing
- Influential nodes
- Multi-Kernel Fuzzy Clustering (MKFC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2513 — Enhanced federated reinforcement learning framework for task management in fog computing using eligibility traces and targeted model dissemination

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing supports low-latency coordination among distributed edge nodes, yet real deployments must cope with uncertain workloads, partial observability, and intermittent links. This study develops a federated reinforcement learning (FRL) framework designed to remain stable under such non-ideal conditions. The approach combines three complementary mechanisms: (i) multi-kernel fuzzy preprocessing to capture task semantics, (ii) eligibility-trace–based policy initialization for faster adaptation, and (iii) topology-aware dissemination that prioritizes structurally influential nodes during aggregation. Together, these components enable faster convergence, lower communication load, and improved allocation accuracy in heterogeneous fog settings. Simulations on dynamic fog topologies show consistent performance gains: convergence time shortened by 40.3% relative to classical RL, energy use reduced by 28.0% compared with baseline FRL, latency lowered by 18.8% versus GNN-FL, and accuracy improved by 11.2% over FedAvg. Communication volume decreased by roughly 41.5% compared with full-broadcast aggregation. Statistical significance was verified using one-way ANOVA and Mann–Whitney U tests. Beyond numerical results, the framework illustrates a cross-domain learning paradigm that links cooperative multi-agent behaviors to fog-level task orchestration in the Internet of Everything (IoE). It offers a practical, interpretable, and resource-efficient architecture, supported by a lightweight and reproducible implementation that can be readily deployed on federated fog infrastructures. © The Author(s), under exclusive licence to Springer-Verlag GmbH Austria, part of Springer Nature 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2513.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
