---
id: paper-0387
title: 'MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture'
authors:
- Boubin, Jayson
- Burley, Codi
- Han, Peida
- Li, Bowen
- Porter, Barry
- Stewart, Christopher
venue: Proceedings - 2022 IEEE/ACM 7th Symposium on Edge Computing, SEC 2022
venue_type: conference
year: 2022
doi: 10.1109/SEC54971.2022.00013
url: https://www.scopus.com/pages/publications/85145584862?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 68--81
keywords:
- Autonomy
- Edge Computing
- Multi agent Reinforcement Learning
- UAV
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0387 — MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital agriculture, hailed as the fourth great agricultural revolution, employs software-driven autonomous agents for in-field crop management. Edge computing resources deployed near crop fields support autonomous agents with substantial computational needs for tasks such as AI inference. In large fields, using multiple autonomous agents, called swarms, can speed up crop management tasks if sufficient edge resources are provisioned. However, to use swarms today, farmers and software developers craft their own standalone solutions that are either simple and ineffective or complicated and hard-to-reproduce. We present MARbLE, a platform for developing and managing swarms. MARbLE provides an easy-to-use programming paradigm that helps users build swarm workloads using multi-agent reinforcement learning. Developers supply just two functions Map() and Eval(). The platform automatically compiles and deploys swarms and continuously updates the reinforcement learning models that govern their actions. Developers can experiment with multiple swarm and edge resource configurations both in simulation and with actual in-field runs. We studied real UAV swarms conducting digital agriculture missions. We observe that swarms demanded edge computing resources in bursts; the ratio of average to peak demand was 2.9X. MARbLE uses energy-saving load balancing policies to duty cycle machines during workload demand troughs, leveraging workload patterns to save edge energy. Using MARbLE, we found that four-agent swarms with load balancing techniques sped up missions by 2.1X and reduced edge energy usage by up to 2X compared to state of the art autonomous swarms.  © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0387.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
