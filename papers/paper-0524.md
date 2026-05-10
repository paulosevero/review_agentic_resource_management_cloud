---
id: paper-0524
title: 'Meta-MADDPG: Achieving Transfer-Enhanced MEC Scheduling via Meta Reinforcement Learning'
authors:
- Yao, Yiming
- Ren, Tao
- Cui, Meng
- Liu, Dong
- Niu, Jianwei
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-19211-1_47
url: https://www.scopus.com/pages/publications/85142864446?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 572--585
keywords:
- Deep reinforcement learning
- Meta learning
- Mobile edge computing
- Multi-agent deep deterministic policy gradient
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0524 — Meta-MADDPG: Achieving Transfer-Enhanced MEC Scheduling via Meta Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the assistance of mobile edge computing (MEC), mobile devices (MDs) can optionally offload local computationally heave tasks to edge servers that are generally deployed at the edge of networks. As thus, the latency of task and energy consumption of MDs can be both reduced, significantly improving mobile users’ quality of experience. Although considerable MEC scheduling algorithms have been designed by researchers, most of them are trained to solve specific tasks, leaving the performance in other MEC environments remaining dubious. To address the issue, this paper first formulates the optimization problem to minimize both task delay and energy consumption, and then transforms it into Markov decision problem that is further solved by using the state-of-the-art multi-agent deep reinforcement learning method, i.e., MADDPG. Furthermore, aiming at improving the overall performance in various MEC environments, we integrate MADDPG with meta-learning and propose Meta-MADDPG which is carefully designed with dedicated reward functions. The evaluation results are given to showcase the more satisfactory performances of Meta-MADDPG over the state-of-the-art algorithms when confronting new environments. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0524.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
