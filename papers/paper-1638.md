---
id: paper-1638
title: Large Language Model Offloading using Active Inference in 6G Symbiotic IoT
authors:
- He, Xiaoming
- Jiang, Yunzhe
- Xu, Xiaoming
- Cui, Huajun
- Liu, Yinqiu
- Chen, Mingkai
- Hong, Yan
- Zhang, Jie
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3588832
url: https://www.scopus.com/pages/publications/105011832629?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6G
- Active Inference
- Cloud-to-Edge
- Large Language Model Offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1638 — Large Language Model Offloading using Active Inference in 6G Symbiotic IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing demand for Large Language Model (LLM) applications in mobile computing poses a challenge for devices with limited resources, as they struggle to efficiently handle complex inference tasks. Despite its traditional use for offloading tasks to remote servers, Deep Reinforcement Learning (DRL) exhibits notable limitations, such as data inefficiency, latency insensitivity, and poor adaptability to variable workloads, thereby adversely impacting the performance of LLMs. Deep Reinforcement Learning (DRL) is traditionally used to offload tasks to remote servers. However, it has several limitations which negatively affect the performance of LLMs. We present an approach which is based on active inference for task offloading in LLM and cloud-edge computing resource scheduling, especially relevant to emerging 6G networks. These networks are designed to provide enhanced connectivity, reduced latency, and increased data rates. Our approach capitalizes on these strengths to optimize task distribution and maximize resource utilization, fostering a symbiotic relationship between devices and networks. Simulations demonstrate that our method outperforms standard DRL by enhancing data efficiency and better adapting to varying loads, aligning with 6G’s emphasis on flexible and responsive networks. By integrating active inference into cloud-edge systems, we develop a more robust and adaptable LLM strategy that is well-suited for the 6G era, promoting a Symbiotic Internet-of-Things (IoT) where devices and networks dynamically collaborate and share resources to fulfill the requirements of advanced applications. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1638.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
