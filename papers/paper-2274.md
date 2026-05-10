---
id: paper-2274
title: Multi-agent Independent PPO-based Automatic ECN Tuning for High-Speed Data Center Networks
authors:
- Wang, Ting
- Cheng, Kai
- Du, Xiao
venue: Proceedings - IEEE International Conference on Cluster Computing, ICCC
venue_type: conference
year: 2025
doi: 10.1109/CLUSTER59342.2025.11186496
url: https://www.scopus.com/pages/publications/105019740951?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Bioinformatics
- Congestion control (communication)
- Intelligent agents
- Internet protocols
- Mammals
- Packet networks
- Traffic congestion
- Tuning
- Control schemes
- Data center networks
- Decentralised
- Explicit congestion notification
- Explicit congestion notification marking
- High-speed data
- Marking threshold
- Multi agent
- Network dynamics
- Queue lengths
- Multi agent systems
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

# paper-2274 — Multi-agent Independent PPO-based Automatic ECN Tuning for High-Speed Data Center Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Explicit Congestion Notification (ECN)-based congestion control schemes have been widely adopted in high-speed data center networks (DCNs), where the ECN marking threshold plays a determinant role in guaranteeing a packet lossless DCN. However, existing approaches either employ static settings with immutable thresholds that cannot be dynamically self-adjusted to adapt to network dynamics, or fail to take into account many-to-one traffic patterns and different requirements of different types of traffic, resulting in relatively poor performance. To address these problems, this paper proposes a novel learningbased automatic ECN tuning scheme, named PET, based on the multi-agent Independent Proximal Policy Optimization (IPPO) algorithm. PET dynamically adjusts ECN thresholds by fully considering pivotal congestion-contributing factors, including queue length, output data rate, output rate of ECN-marked packets, current ECN threshold, the extent of incast, and the ratio of mice and elephant flows. PET adopts the Decentralized Training and Decentralized Execution (DTDE) paradigm and combines offline and online training to accommodate network dynamics. PET is also fair and readily deployable with commodity hardware. Comprehensive experimental results demonstrate that, compared with state-of-the-art static schemes and the learningbased automatic scheme, our PET achieves better performance in terms of flow completion time, convergence rate, queue length variance, and system robustness. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2274.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
