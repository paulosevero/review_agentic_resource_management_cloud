---
id: paper-0336
title: Deep Reinforcement Learning Based Computation Offloading in Fog Enabled Industrial Internet of Things
authors:
- Ren, Yijing
- Sun, Yaohua
- Peng, Mugen
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2021
doi: 10.1109/TII.2020.3021024
url: https://www.scopus.com/pages/publications/85104190707?origin=resultslist
publisher: IEEE Computer Society
pages: 4978--4987
keywords:
- Computation offloading
- fog computing
- industrial Internet of Things (IIoT)
- multi-agent deep reinforcement learning (DRL)
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

# paper-0336 — Deep Reinforcement Learning Based Computation Offloading in Fog Enabled Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing is seen as a key enabler to meet the stringent requirements of industrial Internet of Things (IIoT). Specifically, lower latency and IIoT devices' energy consumption can be achieved by offloading computation-intensive tasks to fog access points (F-APs). However, traditional computation offloading optimization methods often possess high complexity, making them inapplicable in practical IIoT. To overcome this issue, this article proposes a deep reinforcement learning (DRL) based approach to minimize long-term system energy consumption in a computation offloading scenario with multiple IIoT devices and multiple F-APs. The proposal features a multi-agent setting to deal with the curse of dimensionality of the action space by creating a DRL model for each IIoT device, which identifies its serving F-AP based on network and device states. After F-AP selection is finished, a low complexity greedy algorithm is executed at each F-AP under a computation capability constraint to determine which offloading requests are further forwarded to the cloud. By conducting offline training in the cloud and then making decisions online, iterative online optimization procedures are avoided and, hence, F-APs can quickly adjust F-AP selection for each device with trained DRL models. Via simulation, the impact of batch size on system performance is demonstrated and the proposed DRL-based approach shows competitive performance compared to various baselines including exhaustive search and genetic algorithm based approaches. In addition, the generalization capability of the proposal is verified as well.  © 2005-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0336.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
