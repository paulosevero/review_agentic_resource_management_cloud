---
id: paper-1890
title: Multi-UAV-Assisted MEC in Internet of Vehicles With Combined Multi-Modal Semantic Communication Under Jamming Attacks
authors:
- Liu, Shuai
- Yang, Helin
- Zheng, Mengting
- Xiao, Liang
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3550965
url: https://www.scopus.com/pages/publications/105000199791?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7600--7614
keywords:
- anti-jamming
- deep reinforcement learning
- Internet of vehicles
- Multi-modal semantic communication
- UAV-assisted MEC
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

# paper-1890 — Multi-UAV-Assisted MEC in Internet of Vehicles With Combined Multi-Modal Semantic Communication Under Jamming Attacks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Semantic communication technology, which transmits only relevant semantic information, can significantly conserve communication resources and reduce service time. This technology is particularly promising for unpilotedaerial vehicle (UAV)-assisted mobile edge computing (MEC) in the internet of vehicles (IoV). However, integrating semantic communication with UAV-assisted vehicle MEC is susceptible to malicious jamming. This paper introduces a reliable communication method that combines multi-modal semantic communication with UAV-assisted vehicle MEC to minimize delays in communication and computation while maintaining semantic accuracy during jamming attacks. Our approach optimizes UAV trajectories, user associations, and channel selections, enabling the UAV to select optimal positions when associating with different modal users and reducing the impact of jammers during multi-modal task reception. Due to the non-convex nature of the optimization problem and the highly dynamic environment, we employ the semantic communication combined with the multi-agent twin delayed deep deterministic policy gradient (SC-MA-TD3) approach, a multi-agent deep reinforcement learning (DRL) strategy that fosters UAV cooperation for efficient resource allocation. Simulation results show that our approach outperforms existing approaches in reducing delays and enhancing semantic accuracy. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1890.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
