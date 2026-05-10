---
id: paper-2684
title: Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers
authors:
- Liu, Hao
- Hu, Xiaonyu
- Wang, Ran
- Hao, Jie
- Wu, Qiang
- Zhang, Hongke
venue: Digital Communications and Networks
venue_type: journal
year: 2026
doi: 10.1016/j.dcan.2025.11.006
url: https://www.scopus.com/pages/publications/105030166188?origin=resultslist
publisher: KeAi Communications Co.
pages: 236--251
keywords:
- Geographically distributed data center
- Green communication
- Large language model
- Multi-agent reinforcement learning
- Task scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2684 — Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The explosive proliferation of Large Language Models (LLMs) imposes significant energy and operational burdens on Geographically Distributed Data Centers (GDDCs), thereby demanding an efficient mechanism for LLMs task scheduling. While prior geo-distributed scheduling methods reduce cost and carbon emissions by exploiting regional heterogeneity, they largely overlook model and data reuse opportunities and the uncertainty of LLM execution times. In this paper, we introduce GCOS, to the best of our knowledge, the first green scheduling framework that incorporates a dual-cache system for both data and models, while jointly optimizing task assignment and cache migration. We firstly propose a dual-cache mechanism that decouples model and data caching to enable fine-grained reuse and minimize redundant transmissions. Subsequently, we propose the Multi-Agent Cache-aware Cooperative Scheduling (MACCS) algorithm, which leverages reinforcement learning to optimize task placement with a focus on minimizing both carbon emissions and cost. Additionally, we design a lightweight execution time predictor, DiPTree, to address the high variability in task execution times. Extensive experiments on real-world datasets demonstrate that GCOS reduces overall cost by up to 92.6 % and carbon emissions by 90.3 %, significantly outperforming existing baselines. © 2025 Chongqing University of Posts and Telecommunications.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2684.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
