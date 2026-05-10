---
id: paper-1213
title: 'Cooperative Task Offloading for Multi-Access Edge-Cloud Networks: A Multi-Group Multi-Agent Deep Reinforcement Learning'
authors:
- Suzuki, Akito
- Kobayashi, Masahiro
- Oki, Eiji
venue: Proceedings - International Conference on Computer Communications and Networks, ICCCN
venue_type: conference
year: 2024
doi: 10.1109/ICCCN61486.2024.10637522
url: https://www.scopus.com/pages/publications/85203277211?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud computing
- deep reinforcement learning
- multi-access edge computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1213 — Cooperative Task Offloading for Multi-Access Edge-Cloud Networks: A Multi-Group Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing (CC) and edge computing (EC) enhance the performance of end devices (EDs) with limited computational power by offloading tasks to cloud and edge servers, respectively. Multi-access edge computing (MEC) further advances EC by integrating wireless network resources, thus improving mobile service efficiency. While CC is well-suited for intensive computational tasks, it may face latency issues due to geographical distances. EC and MEC aim to minimize this latency by deploying server resources closer to EDs, but they encounter challenges due to the limited resources of edge servers. Cooperative task offloading emerges as a solution to address the above challenges of optimizing resource allocation across cloud and edge based on task characteristics. Despite numerous research, existing methods often cover only a portion of the networks and servers, leading to sub-optimal task allocation. Therefore, we propose a cooperative task-offloading method for multi-access edge-cloud networks, simultaneously considering server and link resources, base station (BS), and wireless channel allocation. This method improves task-offloading efficiency by utilizing cooperative multi-group multi-agent deep reinforcement learning (CMG-MADRL) with different agent groups for BS and server allocation. Simulations have demonstrated that our method effectively reduces resource utilization and task latency while minimizing constraint violations.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1213.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
