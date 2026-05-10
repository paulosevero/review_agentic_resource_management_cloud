---
id: paper-0466
title: Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning
authors:
- Lin, Liduo
- Pan, Li
- Liu, Shijun
venue: Information Sciences
venue_type: journal
year: 2022
doi: 10.1016/j.ins.2022.10.071
url: https://www.scopus.com/pages/publications/85141235781?origin=resultslist
publisher: Elsevier Inc.
pages: 480--496
keywords:
- Auto-scaling
- Heterogeneous instances
- On-demand instance
- Reinforcement learning
- Spot instance
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

# paper-0466 — Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Designing auto-scaling frameworks using spot and on-demand instances while considering their heterogeneity, can help Software-as-a-Service (SaaS) providers provide services with high availability to meet dynamic workloads and achieve significant cost savings. However, designing such an auto-scaling framework is difficult due to the lack of prior knowledge of the cloud. In this work, we propose an algorithm called SpotRL to solve the auto-scaling problem using heterogeneous spot and on-demand instances. Reinforcement learning (RL) approaches have been shown to be able to make effective decisions in highly dynamic environments, as they can learn step-by-step and find solutions without prior knowledge. SpotRL uses an RL-based approach for the scaling of heterogeneous spot instances. In the complex cloud environment, the training speed of RL agents is generally slow. Considering this issue, we use a multi-agent approach to decompose tasks to help agents learn faster. To reduce the negative impact of low service availability due to agents’ random explorations as they interact with the cloud environment, SpotRL uses a passive approach for the scaling of heterogeneous on-demand instances. Our experimental results show that the SpotRL approach can significantly reduce the deployment cost of SaaS providers while complying with high service availability. © 2022 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0466.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
