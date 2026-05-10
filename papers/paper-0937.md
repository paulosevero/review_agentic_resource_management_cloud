---
id: paper-0937
title: 'AI-Enhanced Cloud-Edge-Terminal Collaborative Network: Survey, Applications, and Future Directions'
authors:
- Gu, Huixian
- Zhao, Liqiang
- Han, Zhu
- Zheng, Gan
- Song, Shenghui
venue: IEEE Communications Surveys and Tutorials
venue_type: journal
year: 2024
doi: 10.1109/COMST.2023.3338153
url: https://www.scopus.com/pages/publications/85184489215?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1322--1385
keywords:
- applications
- Cloud-edge-terminal collaborative network (CETCN)
- collaborative caching
- mobility management
- multiagent reinforcement learning (MARL)
- network architecture
- resource allocation
- security
- single-agent reinforcement learning (SARL)
- standards
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-0937 — AI-Enhanced Cloud-Edge-Terminal Collaborative Network: Survey, Applications, and Future Directions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The cloud-edge-terminal collaborative network (CETCN) is considered as a novel paradigm for emerging applications owing to its huge potential in providing low-latency and ultra-reliable computing services. However, achieving such benefits is very challenging due to the heterogeneous computing power of terminal devices and the complex environment faced by the CETCN. In particular, the high-dimensional and dynamic environment states cause difficulties for the CETCN to make efficient decisions in terms of task offloading, collaborative caching and mobility management. To this end, artificial intelligence (AI), especially deep reinforcement learning (DRL) has been proven effective in solving sequential decision-making problems in various domains, and offers a promising solution for the above-mentioned issues due to several reasons. Firstly, accurate modelling of the CETCN, which is difficult to obtain for real-world applications, is not required for the DRL-based method. Secondly, DRL can effectively respond to high-dimensional and dynamic tasks through iterative interactions with the environment. Thirdly, due to the complexity of tasks and the differences in resource supply among different vendors, collaboration is required between different vendors to complete tasks. The multi-agent DRL (MADRL) methods are very effective in solving collaborative tasks, where the collaborative tasks can be jointly completed by cloud, edge and terminal devices which provided by different vendors. This survey provides a comprehensive overview regarding the applications of DRL and MADRL in the context of CETCN. The first part of this survey provides a depth overview of the key concepts of the CETCN and the mathematical underpinnings of both DRL and MADRL. Then, we highlight the applications of RL algorithms in solving various challenges within CETCN, such as task offloading, resource allocation, caching and mobility management. In addition, we extend discussion to explore how DRL and MADRL are making inroads into emerging CETCN scenarios like intelligent transportation system (ITS), the industrial Internet of Things (IIoT), smart health and digital agriculture. Furthermore, security considerations related to the application of DRL within CETCN are addressed, along with an overview of existing standards that pertain to edge intelligence. Finally, we list several lessons learned in this evolving field and outline future research opportunities and challenges that are critical for the development of the CETCN. We hope this survey will attract more researchers to investigate scalable and decentralized AI algorithms for the design of CETCN.  © 1998-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0937.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
