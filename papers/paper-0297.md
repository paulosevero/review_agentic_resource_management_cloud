---
id: paper-0297
title: Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning
authors:
- Hu, Shucheng
- Ren, Tao
- Niu, Jianwei
- Hu, Zheyuan
- Xing, Guoliang
venue: Proceedings - 2021 17th International Conference on Mobility, Sensing and Networking, MSN 2021
venue_type: conference
year: 2021
doi: 10.1109/MSN53354.2021.00089
url: https://www.scopus.com/pages/publications/85128718512?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 575--583
keywords:
- mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0297 — Distributed Task Offloading based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent years have witnessed the increasing popularity of mobile applications, e.g., virtual reality, unmanned driving, which are generally computation-intensive and latency-sensitive, posing a major challenge for resource-limited user equipment (UE). Mobile edge computing (MEC) has been proposed as a promising approach to alleviate the problem, by offloading mobile tasks to the edge server (ES) deployed in close proximity to UE. However, most existing task offloading algorithms are primarily based on centralized scheduling, which could suffer from the 'curse of dimensionality' in large MEC environments. To address this issue, this paper proposes a fully distributed task offloading approach based on multi-agent deep reinforcement learning, whose critic and actor neural networks are trained under the assistance of global and local network states, respectively. In addition, we design a model parameter aggregation mechanism, along with a normalized fine-tuned reward function, to further improve the learning efficiency of the training process. Simulation results show that our proposed approach could achieve substantial performance improvements over baseline approaches.  © 2021 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0297.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
