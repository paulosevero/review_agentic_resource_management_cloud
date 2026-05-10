---
id: paper-1145
title: Learning-Based Multi-Drone Network Edge Orchestration for Video Analytics
authors:
- Qu, Chengyi
- Singh, Rounak
- Esquivel-Morel, Alicia
- Calyam, Prasad
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2024
doi: 10.1109/TNSM.2024.3440883
url: https://www.scopus.com/pages/publications/85200809383?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6331--6348
keywords:
- machine learning
- Multi-access edge computing
- multi-drone networks
- network characterization
- network protocols
- reinforcement learning
- video analytics
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

# paper-1145 — Learning-Based Multi-Drone Network Edge Orchestration for Video Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (also known as drones) equipped with high-resolution video cameras have become increasingly popular for applications such as public safety and smart farming. However, inefficient configurations in drone video analytics due to misconfigured edge networks can lead to degraded video quality and inefficient resource utilization. In this paper, we propose a novel scheme for network edge orchestration that utilizes both offline and online learning-based approaches to achieve pertinent selections of network protocols and video properties in multi-drone-based video analytics. Our approach utilizes both supervised and unsupervised machine learning algorithms to make decisions regarding network protocols and video properties during the pre-takeoff stage of the drones (i.e., offline stage). Additionally, our approach incorporates a reinforcement learning-based multi-agent deep Q-network algorithm for drone trajectory optimization during flights (i.e., online stage) and a memory-to-memory multi-hop data forwarding strategy for drone swarm video transmission. Our evaluation results demonstrate that our offline orchestration approach can suitably choose network protocols (i.e., among TCP/HTTP, UDP/RTP, QUIC), while our unsupervised learning approach outperforms existing methods and achieves efficient offloading while improving network performance (i.e., throughput and round-trip time) by at least 25%, with satisfactory video quality. Furthermore, we demonstrate through trace-based and real-field experiment testbeds how our online orchestration in terms of decision-making and data forwarding strategies achieves 91% of the oracle baseline network throughput performance with comparable video quality. Overall, our approach offers a promising solution for optimizing drone video analytics and enhancing the overall performance of drone-swarm-based applications. © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1145.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
