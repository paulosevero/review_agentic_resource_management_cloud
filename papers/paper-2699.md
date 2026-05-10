---
id: paper-2699
title: 'SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks'
authors:
- Luo, Wangqing
- Hu, Jinbin
- Sun, Hua
- Sharma, Pradip Kumar
- Wang, Jin
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2026
doi: 10.1109/TNSM.2026.3678979
url: https://www.scopus.com/pages/publications/105035331212?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Data Security
- Datacenter Networks
- Deep Reinforcement Learning
- Load Balancing
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
    my_justification: LLM as workload
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

# paper-2699 — SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To meet the massive compute and high-speed communication demands of Large Language Model (LLM) training, modern datacenters typically adopt multipath topologies such as Fat-Tree and Clos to host parallel jobs across hundreds to thousands of GPUs. However, LLM training exhibits periodic, high-bandwidth communication patterns. Existing load-balancing schemes become misaligned under dynamic congestion and anomalous surges: they struggle to promptly mitigate iteration-peak congestion and lack effective isolation of anomalous traffic. To address this, we propose Security-Aware Load Balancing (SALB) for LLM training. SALB leverages a Deep Reinforcement Learning (DRL) controller with queue and delay signals for packet-level multipath load balancing and employs path binding to confine suspicious flows. By integrating data security into load balancing, SALB simultaneously achieves high throughput and robust traffic isolation. NS-3 simulation results show that, compared with CONGA, Hermes, and ConWeave, SALB reduces the 99<sup>th</sup>-percentile flow completion time (FCT) of short flows by an average of 65% and increases the throughput of long flows by an average of 54%. It further outperforms the baselines in aggregate throughput, path utilization, and packet loss rate, thereby significantly enhancing system stability, robustness, and data security. © 2004-2012 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2699.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
