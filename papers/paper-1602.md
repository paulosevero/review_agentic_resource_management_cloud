---
id: paper-1602
title: Directed Graph and Convolutional Network Reinforcement Learning for Terminal-Side Collaborative Computing Resource Allocation Scheme; [基于有向图与卷积网络强化学习的端侧协同算力资源分配方法]
authors:
- Gu, Jian-hua
- Feng, Jian-hua
- Xu, Hui-yang
- Liu, Tong-tong
- Zhou, Ting
venue: Tien Tzu Hsueh Pao/Acta Electronica Sinica
venue_type: journal
year: 2025
doi: 10.12263/DZXB.20251106
url: https://www.scopus.com/pages/publications/105027477708?origin=resultslist
publisher: Chinese Institute of Electronics
pages: 1771--1783
keywords:
- directed graph convolutional network
- multi hop D2D
- terminal collaboration
- terminal-side computing power
- terminal-side computing power allocation
- 多跳D2D
- 有向图卷积网络
- 端侧算力
- 端算力分配
- 终端协同
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1602 — Directed Graph and Convolutional Network Reinforcement Learning for Terminal-Side Collaborative Computing Resource Allocation Scheme; [基于有向图与卷积网络强化学习的端侧协同算力资源分配方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the concentrated surge of AI application scenarios, the increasing requirements on data commu⁃ nication and computation in mobile applications is growing, the traditional cloud computing which relies on remote process⁃ ing, often fails to meet low-latency requirements. Therefore, a new paradigm has emerged: terminal-side computing power that aggregate the vast terminal devices (including computing, storage, communication, etc) through distributed collabora⁃ tion to efficiently execute computational tasks. However, constrained by the limited resource of standalone device and pro⁃ hibitive communication overhead that impairs task coordination, such terminals still face significant challenges in achieving efficient collaboration for highly complex computing tasks.This paper presents device-to-device (D2D) communication as⁃ sisted terminal devices collaborative computing, and a multi-agent soft actor-critic (MA-SAC) based on directed graph con⁃ volutional network (DGCN) is designed to solve this problem.The subtasks included in directed acyclic graph (DAG) tasks were deployed to multiple terminals for collaborative computing, it is introduced to cater to the exigencies of task transmis⁃ sion between disparate nodes within the DAG, and reduces the communication overhead when data transmission in the net⁃ work. Through the simulations, the efficacy of the proposed scheme is demonstrated. The proposed scheme reduces network communication overhead by 38.2% and effectively improve resource utilization by 31.9%. © (2025), (Chinese Institute of Electronics). All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1602.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
