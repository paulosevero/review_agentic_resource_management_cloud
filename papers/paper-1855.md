---
id: paper-1855
title: MARL-Based Joint Optimization of Service Migration and Resource Allocation in MEC
authors:
- Lin, Ziqi
- He, Zhenli
- Zhai, Xiaolong
- Xiao, Yuanfei
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-2864-3_3
url: https://www.scopus.com/pages/publications/105002578934?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 28--39
keywords:
- Mobile Edge Computing
- Multi-Agent Reinforcement Learning
- Resource Allocation
- Service Migration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1855 — MARL-Based Joint Optimization of Service Migration and Resource Allocation in MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) extends computational resources to the network edge, enabling low-latency services for users and IoT devices. While existing research advances service migration, it often isolates migration from resource allocation, leading to suboptimal edge server utilization and increased response delays. Moreover, the impact of migrating user-specific service contexts within network topologies is often overlooked, which undermines the effectiveness of migration strategies and increases costs. To address these issues, we propose a joint optimization of service migration and resource allocation in MEC, modeled as a Multi-Agent Markov Decision Process (MAMDP). We propose an algorithm based on Multi-Agent Reinforcement Learning (MARL). By employing Multi-Agent Proximal Policy Optimization (MAPPO) and Karush-Kuhn-Tucker (KKT) conditions, our approach optimizes both service migration and resource allocation strategies, thereby enhancing service quality. Simulations demonstrate that our method significantly outperforms benchmarks, achieving substantial reductions in response delays, service failures, and migration costs. © IFIP International Federation for Information Processing 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1855.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
