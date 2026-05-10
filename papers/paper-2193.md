---
id: paper-2193
title: 'Optimizing the Ratio-Based Offloading in Federated Cloud-Edge Systems: A MADRL Approach'
authors:
- Tadele, Seifu Birhanu
- Yahya, Widhi
- Kar, Binayak
- Lin, Ying-Dar
- Lai, Yuan-Cheng
- Wakgra, Frezer Guteta
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2025
doi: 10.1109/TNSE.2024.3501398
url: https://www.scopus.com/pages/publications/85210041641?origin=resultslist
publisher: IEEE Computer Society
pages: 463--475
keywords:
- Cloud computing
- DRL
- edge computing
- offloading
- optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2193 — Optimizing the Ratio-Based Offloading in Federated Cloud-Edge Systems: A MADRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the evolving landscape of cloud-edge federated systems, Multi-Access Edge Computing (MEC) plays a crucial role by being closer to user equipment (UEs). However, it has limited capacity compared to the cloud, leading to challenges during periods of high network traffic, commonly referred to as hotspot traffic, when MEC resources can become overwhelmed. To mitigate this issue, horizontal and vertical traffic offloading between edges and core sites, and from core sites to the cloud, respectively, is employed. The offloading decisions, crucial for ensuring network efficiency, must be made within seconds. Traditional optimization techniques are unsuitable due to their computational intensity and time-consuming nature, necessitating a shift toward machine learning methods. This research introduces a ratio-based offloading approach, leveraging a multi-agent deep reinforcement learning (MADRL) approach based on the twin-delayed deep deterministic policy gradient (TD3) algorithm. In a comparative evaluation against the simulated annealing (SA) algorithm and single-agent deep reinforcement learning (DRL) approaches, our proposed solution exhibits superior performance, particularly in terms of decision time. The DRL-based approach achieves convergence within seconds, whereas SA takes minutes. Additionally, the average latency experienced by traffic in the multi-agent TD3 configuration is approximately 3-4 times less than in the single-agent configuration.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2193.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
