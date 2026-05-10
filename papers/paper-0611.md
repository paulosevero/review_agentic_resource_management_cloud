---
id: paper-0611
title: 'CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network'
authors:
- Hu, Shi-Hong
- Luo, Qu-Yuan
- Li, Guang-Hui
- Shi, Weisong
- Ye, Bao-Liu
venue: Journal of Computer Science and Technology
venue_type: journal
year: 2023
doi: 10.1007/s11390-023-2839-0
url: https://www.scopus.com/pages/publications/85178659413?origin=resultslist
publisher: Springer
pages: 1113--1131
keywords:
- deep reinforcement learning
- edge computing
- task scheduling
- vehicular edge computing
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0611 — CA-DTS: A Distributed and Collaborative Task Scheduling Algorithm for Edge Computing Enabled Intelligent Road Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing enabled Intelligent Road Network (EC-IRN) provides powerful and convenient computing services for vehicles and roadside sensing devices. The continuous emergence of transportation applications has caused a huge burden on roadside units (RSUs) equipped with edge servers in the Intelligent Road Network (IRN). Collaborative task scheduling among RSUs is an effective way to solve this problem. However, it is challenging to achieve collaborative scheduling among different RSUs in a completely decentralized environment. In this paper, we first model the interactions involved in task scheduling among distributed RSUs as a Markov game. Given that multi-agent deep reinforcement learning (MADRL) is a promising approach for the Markov game in decision optimization, we propose a collaborative task scheduling algorithm based on MADRL for EC-IRN, named CA-DTS, aiming to minimize the long-term average delay of tasks. To reduce the training costs caused by trial-and-error, CA-DTS specially designs a reward function and utilizes the distributed deployment and collective training architecture of counterfactual multi-agent policy gradient (COMA). To improve the stability of performance in large-scale environments, CA-DTS takes advantage of the action semantics network (ASN) to facilitate cooperation among multiple RSUs. The evaluation results of both the testbed and simulation demonstrate the effectiveness of our proposed algorithm. Compared with the baselines, CA-DTS can achieve convergence about 35% faster, and obtain average task delay that is lower by approximately 9.4%, 9.8%, and 6.7%, in different scenarios with varying numbers of RSUs, service types, and task arrival rates, respectively. © 2023, Institute of Computing Technology, Chinese Academy of Sciences.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0611.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
