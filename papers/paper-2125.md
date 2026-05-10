---
id: paper-2125
title: Intelligent Latency-Oriented Optimization for Multi-UAV-Assisted Mobile Edge Computing in Space-Air-Ground Integrated Networks
authors:
- Shao, Ziling
- Yang, Helin
- Xiong, Zehui
venue: IEEE Transactions on Communications
venue_type: journal
year: 2025
doi: 10.1109/TCOMM.2025.3597807
url: https://www.scopus.com/pages/publications/105013135092?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13384--13398
keywords:
- anti-jamming
- deep reinforcement learning
- latency minimization
- mobile edge computing
- Space-air-ground integration networks
- uncrewed aerial vehicle
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

# paper-2125 — Intelligent Latency-Oriented Optimization for Multi-UAV-Assisted Mobile Edge Computing in Space-Air-Ground Integrated Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Uncrewed aerial vehicles (UAV)-assisted mobile edge computing (MEC) in space-air-ground integrated networks (SAGINs) provide a promising solution for enhancing communication, computing, and storage services for the increased number of Internet of Things (IoT) devices. However, jamming attacks and co-channel interference severely degrade the network performance due to wide field of line of sight. In this work, we propose a resource scheduling method to jointly optimize the channel selection, UAV deployment and task offloading to minimize both the communication and computing latency, under the malicious jamming attacks and resource constraints. Considering the highly dynamic and complex nature of the SAGIN environment and the multi-UAV collaboration framework, we then design an advanced anti-jamming-driven multi-agent deep reinforcement learning (MADRL) method based on the multi-agent twin-delayed deep deterministic policy gradient (MATD3) algorithm. This method adaptively adjusts the resource scheduling strategy to enhance the network’s ability to withstand jamming attacks, reduce total network latency, and maintain real-time services even under unfavorable conditions. Simulation results show that our proposed method significantly outperforms existing benchmark methods in terms of latency reduction, signal-to-interference-plus-noise ratio (SINR) improvement, and overall network robustness under jamming attacks. For example, the proposed MATD3-SAGAJ method reduces latency by about 10% and improves the SINR satisfaction ratio from around 91% to nearly 95% compared to the current optimal benchmark method. © 1972-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2125.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
