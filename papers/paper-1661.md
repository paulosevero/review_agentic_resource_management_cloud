---
id: paper-1661
title: Explainable Multiagent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation in Distance and Channel-Aware NOMA Vehicular Edge Networks
authors:
- Hu, Jianqiang
- Chen, Lin
- Shen, Shigen
- Wang, Tian
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3617349
url: https://www.scopus.com/pages/publications/105018043915?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 53505--53519
keywords:
- Multiagent reinforcement learning
- nonorthogonal multiple access (NOMA)
- potential game
- resource allocation
- Shapley additive explanations (SHAP)
- vehicular edge computing (VEC)
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

# paper-1661 — Explainable Multiagent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation in Distance and Channel-Aware NOMA Vehicular Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of intelligent transportation and vehicular edge computing (VEC), efficient, fair, and interpretable task offloading has become a key challenge in dynamic and resource-constrained environments. Nonorthogonal multiple access (NOMA) can enhance connectivity and spectrum efficiency. However, conventional resource allocation strategies typically rely solely on channel gain ordering while overlooking spatial factors and fairness. In addition, the lack of transparency in multiagent deep reinforcement learning (MADRL) decision-making raises concerns regarding transparency and trustworthiness. To address these challenges, we propose a NOMA-based task offloading framework that integrates distance and channel-aware (DACA) resource allocation, and we design a distributed multiagent decision-making algorithm based on potential games (DACA-MAD4PG), further incorporating Shapley additive explanations (SHAP) to improve interpretability. The proposed framework is significantly different from existing NOMA-based task offloading approaches in the following three aspects. First, it introduces a DACA joint resource allocation mechanism to enhance both efficiency and fairness in VEC. Second, an exact potential game is incorporated to guarantee system stability and the existence of Nash equilibria. Last, SHAP is integrated to provide posthoc interpretability, thereby improving transparency in multiagent decision-making. Experiments based on real-world DiDi trajectory data demonstrate that the proposed approach significantly reduces task latency, improves service success rate, cumulative reward (CR), and fairness, and outperforms several baselines, thereby providing a stable and interpretable solution for VEC task offloading. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1661.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
