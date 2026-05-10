---
id: paper-1981
title: Multi agent deep reinforcement learning for resource allocation in container-based clouds environments
authors:
- Nagarajan, S.
- Rani, P. Shobha
- Vinmathi, M.S.
- Subba Reddy, V.
- Saleth, Angel Latha Mary
- Abdus Subhahan, D.
venue: Expert Systems
venue_type: journal
year: 2025
doi: 10.1111/exsy.13362
url: https://www.scopus.com/pages/publications/85161726174?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- cloud services
- multi agent deep reinforcement learning
- resource allocation in container-based clouds (RAC)
- service level agreement (SLA)
- virtual machines (VMs)
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

# paper-1981 — Multi agent deep reinforcement learning for resource allocation in container-based clouds environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Virtualization enables the deployment of several virtual servers on the same physical layer, critical component of the cloud. As cloud services advance, more apps that use repositories are developed, which adds to the overburden. Containers have evolved into the most reliable and lightweight virtualization technology for cloud services thanks to their flexible sorting, mobility, and scalability. In container-based clouds, containers can potentially cut data centre energy usage more than virtual machines (VMs) do. Containers are less energy intensive than VMs. Resource allocation is the most prevalent method in cloud systems. However, resource allocation in container-based clouds (RAC) is innovative and complicated due to its two-level architecture. This includes the pairing of virtual machines and physical computers with containers. In cloud container services, planner components are essential. This lowers expenses while improving the performance and variety of workloads using cloud resources. The cloud infrastructure resource allocation framework is gaining popularity since it is energy-efficient and focuses on cloud data management to maximize income and minimize costs. In this paper, we proposed a deep learning-based architecture capable of achieving high data centre energy efficiency and preventing Service Level Agreement (SLA) violations from deploying green cloud resources. This research describes a hybrid optimum and multi-agent deep reinforcement learning (MADRL) technique for dynamic task scheduling (DTS) in a container cloud environment. The MADRL-DTS model for the RAC problem considers VM overheads, VM types, and an affinity restriction. Then, to address the RAC issue, we develop a DTS hyper-heuristic technique. MADRL-RAC may give allocation rules by recognizing workload trends and VM types from previous workload traces. Compared to modern procedures, the results demonstrate a significant reduction in energy consumption. The evaluation for energy-efficient resource allocation is tested in several virtualized environments to get a high power usage effectiveness and CPU usage. © 2023 John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1981.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
