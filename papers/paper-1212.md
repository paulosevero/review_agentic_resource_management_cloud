---
id: paper-1212
title: 'Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach'
authors:
- Sun, Haifeng
- Zhou, Yuqiang
- Zhang, Hui
- Ale, Laha
- Dai, Hongning
- Zhang, Ning
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3456846
url: https://www.scopus.com/pages/publications/85204154729?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 40996--41007
keywords:
- Aerial access networks (AANs)
- joint optimization
- mobile edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1212 — Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The 6G network is expected to accommodate a wide array of connected devices, supporting diverse services from any location at any time. In this article, we introduce an aerial mobile edge computing (MEC) framework composed of high-altitude platforms (HAPs) and low-altitude unmanned aerial vehicles (UAVs), to cater to computing offloading for Internet of Things (IoT) devices, particularly in rural/remote areas or disaster zones. The framework accommodates various types of tasks, each computed by the corresponding Docker container. The objective is to achieve optimal workload fairness for UAVs while simultaneously minimizing the weighted processing costs among IoT devices in terms of task computation latency and energy consumption over the long term. This is achieved by jointly optimizing the flight trajectories and Docker image caching decisions of the UAVs with limited storage capacities, alongside ensuring service fairness for IoT devices. We tailor a multiagent deep deterministic policy gradient (MADDPG)-based approach to solve the long-term joint optimization problem, normalizing continuous actions and sampling discrete actions by generalizing the Gumbel-Softmax reparameterization trick. Experimental results indicate that our approach significantly outperforms benchmark schemes in terms of processing delay, energy consumption, and fairness.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1212.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
