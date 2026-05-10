---
id: paper-1269
title: 'Many-to-Many Task Offloading in Vehicular Fog Computing: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Wei, Zhiwei
- Li, Bing
- Zhang, Rongqing
- Cheng, Xiang
- Yang, Liuqing
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2023.3250495
url: https://www.scopus.com/pages/publications/85149401987?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2107--2122
keywords:
- many-to-many
- multi-agent deep reinforcement learning
- POMDP
- task offloading
- vehicular fog computing
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

# paper-1269 — Many-to-Many Task Offloading in Vehicular Fog Computing: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular fog computing (VFC) has emerged as a promising solution to mitigate vehicular network computation load. In the hierarchical VFC, vehicles are employed as mobile fog nodes at the edge to provide reliable and low-latency services. Particularly, since privately-owned vehicles are rational nodes, their intentions for both computation provision and service demand should be considered instead of overestimating their willingness. To remunerate the participation intentions of vehicles as well as improve vehicular fog resource utilization in the large-scale VFC, the trading-based mechanism is a potential solution. In this article, we propose a many-to-many task offloading framework based on the vehicular trading paradigm. This framework enables computational resource trading across different VFC subsystems and decides the multi-tier task offloading results based on the trading consensus. The trading process is viewed as a partially observable Markov decision process (POMDP) and a Multi-Agent Gated actor Attention Critic (MA-GAC) approach is designed to reach an effective and stable offload-and -serve cooperation among vehicles. Theoretical analyses and experiments verify the feasibility and efficiency of the proposed framework, and simulation results demonstrate that the coordinated MA-GAC approach not only benefits vehicles with higher long-term rewards but also optimizes the system social welfare in a distributed manner.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1269.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
