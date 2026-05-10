---
id: paper-0362
title: 'ACC: Automatic ECN tuning for high-speed datacenter networks'
authors:
- Yan, Siyu
- Wang, Xiaoliang
- Zheng, Xiaolong
- Xia, Yinben
- Liu, Derui
- Deng, Weishan
venue: SIGCOMM 2021 - Proceedings of the ACM SIGCOMM 2021 Conference
venue_type: conference
year: 2021
doi: 10.1145/3452296.3472927
url: https://www.scopus.com/pages/publications/85113246703?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 384--397
keywords:
- AQM
- congestion control
- datacenter network
- ECN
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0362 — ACC: Automatic ECN tuning for high-speed datacenter networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For the widely deployed ECN-based congestion control schemes, the marking threshold is the key to deliver high bandwidth and low latency. However, due to traffic dynamics in the high-speed production networks, it is difficult to maintain persistent performance by using the static ECN setting. To meet the operational challenge, in this paper we report the design and implementation of an automatic run-time optimization scheme, ACC, which leverages the multi-agent reinforcement learning technique to dynamically adjust the marking threshold at each switch. The proposed approach works in a distributed fashion and combines offline and online training to adapt to dynamic traffic patterns. It can be easily deployed based on the common features supported by major commodity switching chips. Both testbed experiments and large-scale simulations have shown that ACC achieves low flow completion time (FCT) for both mice flows and elephant flows at line-rate. Under heterogeneous production environments with 300 machines, compared with the well-tuned static ECN settings, ACC achieves up to 20\% improvement on IOPS and 30\% lower FCT for storage service. ACC has been applied in high-speed datacenter networks and significantly simplifies the network operations.  © 2021 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0362.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
