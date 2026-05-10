---
id: paper-0657
title: HAP-assisted multi-aerial base station deployment for capacity enhancement via federated deep reinforcement learning
authors:
- Liu, Lei
- He, Haoran
- Qi, Fei
- Zhao, Yikun
- Xie, Weiliang
- Zhou, Fanqin
- Feng, Lei
venue: Journal of Cloud Computing
venue_type: journal
year: 2023
doi: 10.1186/s13677-023-00512-9
url: https://www.scopus.com/pages/publications/85173586693?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Aerial base station (AeBS)
- Capacity enhancement
- Deep reinforcement learning (DRL)
- Federated reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0657 — HAP-assisted multi-aerial base station deployment for capacity enhancement via federated deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aerial base stations (AeBSs), as crucial components of air-ground integrated networks, are widely employed in cloud computing, disaster relief, and various applications. How to quickly and efficiently deploy multi-AeBSs for higher capacity gain has become a key research issue. In this paper, we address the 3D deployment optimization problem of multi-AeBSs with the objective of maximizing system capacity. To overcome communication overhead and privacy challenges in multi-agent deep reinforcement learning (MADRL), we propose a federated deep deterministic policy gradient (Fed-DDPG) algorithm for the multi-AeBS deployment decision. Specifically, a high-altitude platform (HAP)-assisted multi-AeBS deployment architecture is designed, in which low-altitude AeBS act as the local nodes to train its own deployment decision model, while the HAP acts as the global node to aggregate the weights of local models. In this architecture, AeBSs do not exchange raw data, addressing data privacy concerns and reducing communication overhead. Simulation results show that the proposed algorithm outperforms fully distributed MADRL algorithms and closely approximates the performance of multi-agent deep deterministic policy gradient (MADDPG), which requires global information during training, but with less training time. © 2023, Springer-Verlag GmbH Germany, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0657.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
