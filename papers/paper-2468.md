---
id: paper-2468
title: Blockchain and Multi-Agent Reinforcement Learning Framework for V2G benefit optimization
authors:
- Zheng, Yuting
- Liu, Bozhi
- Fan, Ke
- Guo, Min
- Hu, Zhuo
venue: 2025 9th International Conference on Power Energy Systems and Applications, ICoPESA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICoPESA65876.2025.11234340
url: https://www.scopus.com/pages/publications/105029629734?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 617--622
keywords:
- Blockchain
- Electric Vehicles (EVs)
- Multi-Agent Reinforcement Learning
- Vehicle-to-Grid (V2G)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2468 — Blockchain and Multi-Agent Reinforcement Learning Framework for V2G benefit optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous growth of renewable energy integration, power systems face increasing challenges in flexible regulation and frequency stability. Electric Vehicles (EVs), as mobile energy storage units with two-way power regulation functions, have shown significant potential as resources for grid ancillary frequency regulation due to their dynamic response advantages and spatial distribution characteristics. However, the current Vehicle-to-Grid (V2G) model, dominated by traditional aggregators, has several implementation constraints: trust deficits from information asymmetry, communication delays from centralized scheduling, and low user participation due to an imperfect economic compensation mechanism, which have severely hindered its practical application.To address these issues, this study develops a blockchain-based framework to enhance V2G benefits. It leverages Mobile Edge Computing (MEC), as public infrastructure, to form a decentralized computing network. By applying multi-agent reinforcement learning algorithms, idle computing power from EVs is utilized to reduce centralised computational latency. MEC nodes are also deployed as blockchain nodes to ensure end-to-end transaction data traceability. Furthermore, a virtual aggregator is designed to replace traditional centralised aggregators, and a dynamic incentive mechanism based on contribution is established. This rewards EV users providing computing resources and frequency regulation services, effectively boosting user participation.Based on the PJM frequency regulation data from Philadelphia, USA, we set up a V2G response ancillary frequency regulation market system that includes passenger cars, buses, and ambulances. We compared the performance of three common reinforcement learning algorithms in the decentralized architecture. Results indicate that the SAC algorithm is the most effective in optimizing grid frequency fluctuations and improving overall system benefits. It can effectively optimize EVs charging/discharging. Moreover, it showcases the changes in the battery State of Charge (SOC) for 20 vehicles under the SAC algorithm. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2468.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
