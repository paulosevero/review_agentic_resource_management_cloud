---
id: paper-2931
title: 'MECOS: Cooperative Multi-UAV-Assisted Cross-Boundary Maritime Data Collection Leveraging MARL and LLM'
authors:
- Zhao, Yang
- Luo, Hanjiang
- Tao, Hang
- Wang, Jingjing
- Zhou, Jiehan
- Wu, Kaishun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3642563
url: https://www.scopus.com/pages/publications/105024826883?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8561--8577
keywords:
- Deep reinforcement learning
- Internet of Things (IoT)
- large language model (LLM)
- maritime data collection
- uncrewed aerial vehicles (UAVs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2931 — MECOS: Cooperative Multi-UAV-Assisted Cross-Boundary Maritime Data Collection Leveraging MARL and LLM

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The direct cross-boundary communication between uncrewed aerial vehicles (UAVs) and autonomous underwater vehicles (AUVs) is a pivotal component in establishing the 6G integrated air–sea–space network, holding significant importance for applications such as marine data collection and maritime collaborative search and rescue. Nevertheless, existing solutions exhibit pronounced deficiencies in path planning efficiency, the coverage range of wireless optical communication (WOC), and edge computing load balancing, which result in a high age of information (AoI), severely compromising the performance of time-sensitive maritime missions. To address these challenges, this article proposes a maritime data collection scheme (MECOS), which includes the LMAR2P algorithm for UAVs’ path planning and the MAPBal algorithm for UAVs to deal with the load balancing issue. In LMAR2P, a multiagent deep reinforcement learning (MARL) architecture is adopted, in which we leverage the global understanding capability of large language models (LLMs) to provide state representation for MARL, in order to improve path planning efficiency. Furthermore, to solve the unbalanced computational load problem, we design a Kullback–Leibler (KL) divergence-based reward correction mechanism and propose a distributed adaptive offloading balancing algorithm, MAPBal, which enables resource-aware task allocation to ensure load balancing and reduce data processing latency. The simulation results indicate that the MECOS scheme reduces the AoI by 23.6% and 26.4% during the data collection and data processing phases of maritime missions, respectively. This research provides a viable technical solution for practical applications such as maritime monitoring, demonstrating significant scientific value and promising application prospects. © 2025 IEEE. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2931.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
