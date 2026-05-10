---
id: paper-0698
title: A Cluster-Based Cooperative Co-Evolutionary Algorithm for Multiobjective Workflow Scheduling in a Cloud Environment
authors:
- Qin, Shuo
- Pi, Dechang
- Shao, Zhongshi
- Xu, Yue
venue: IEEE Transactions on Automation Science and Engineering
venue_type: journal
year: 2023
doi: 10.1109/TASE.2022.3183681
url: https://www.scopus.com/pages/publications/85133815925?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1648--1662
keywords:
- cloud computing
- cooperative co-evolutionary algorithm
- multiobjective optimization
- security threats
- Workflow scheduling
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0698 — A Cluster-Based Cooperative Co-Evolutionary Algorithm for Multiobjective Workflow Scheduling in a Cloud Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The cloud workflow scheduling problem has important applications in modern commercial and industrial areas. In the public cloud environment, the workflow suffers from security threats because of the multiple tenants and the distribution of computational resources. This paper models cloud workflow scheduling as a novel multi-objective optimization problem that aims to minimize execution time, cost, and risk. Due to the complexity of the considered problem, a multi-objective cluster-based cooperative co-evolutionary (CBCC) algorithm with several novel designs is proposed. First, a new initialization strategy is presented to generate potential non-dominated solutions. Based on the cluster-based multi-objective optimization framework, a novel collaboration model is proposed, and it adopts four populations to address the subproblems, respectively. Moreover, a diversification strategy is designed to maintain the diversity of the global archive. Furthermore, a problem-specific intensification strategy is designed to intensify the potential solutions. A comprehensive computational and statistical campaign was carried out to verify the performance of CBCC. The results show that the proposed CBCC outperforms several meta-heuristics adapted from closely related scheduling models in the literature by a significantly considerable margin. Note to Practitioners - This paper describes a novel approach called CBCC for minimizing the cost, time, and risk when scheduling a workflow in the cloud environment. CBCC seamlessly combines the cluster-based multi-objective optimization framework and several problem-specific components such as initialization, diversification, and intensification strategies. As the considered problem has not been previously addressed in the literature, five state-of-the-art algorithms for closely related problems, which include I_MaOPSO (improved many objective particle swarm optimization), EMS-C (evolutionary multi-objective scheduling for cloud), ch-PICEA-g (enhanced multi-objective co-evolutionary algorithm), VaEA (vector angle-based evolutionary algorithm), and DQN-based MARL (Deep-Q-network-based Multi-agent Reinforcement Learning) are adopted as baselines. The results demonstrate that CBCC significantly outperforms the baselines with a 95% confidence level.  © 2004-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0698.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
