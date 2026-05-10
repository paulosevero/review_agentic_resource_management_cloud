---
id: paper-1256
title: Multi-Agent Reinforcement Learning-Based Computation Offloading for Unmanned Aerial Vehicle Post-Disaster Rescue
authors:
- Wang, Lixing
- Jiao, Huirong
venue: Sensors
venue_type: journal
year: 2024
doi: 10.3390/s24248014
url: https://www.scopus.com/pages/publications/85213245912?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- computation offloading
- mobile edge computing
- multi-agent reinforcement learning
- post-disaster rescue
- unmanned aerial vehicle
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1256 — Multi-Agent Reinforcement Learning-Based Computation Offloading for Unmanned Aerial Vehicle Post-Disaster Rescue

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Natural disasters cause significant losses. Unmanned aerial vehicles (UAVs) are valuable in rescue missions but need to offload tasks to edge servers due to their limited computing power and battery life. This study proposes a task offloading decision algorithm called the multi-agent deep deterministic policy gradient with cooperation and experience replay (CER-MADDPG), which is based on multi-agent reinforcement learning for UAV computation offloading. CER-MADDPG emphasizes collaboration between UAVs and uses historical UAV experiences to classify and obtain optimal strategies. It enables collaboration among edge devices through the design of the ’critic’ network. Additionally, by defining good and bad experiences for UAVs, experiences are classified into two separate buffers, allowing UAVs to learn from them, seek benefits, avoid harm, and reduce system overhead. The performance of CER-MADDPG was verified through simulations in two aspects. First, the influence of key hyperparameters on performance was examined, and the optimal values were determined. Second, CER-MADDPG was compared with other baseline algorithms. The results show that compared with MADDPG and stochastic game-based resource allocation with prioritized experience replay, CER-MADDPG achieves the lowest system overhead and superior stability and scalability. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1256.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
