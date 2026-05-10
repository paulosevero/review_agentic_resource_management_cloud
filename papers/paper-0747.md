---
id: paper-0747
title: Dual-Driven Resource Management for Sustainable Computing in the Blockchain-Supported Digital Twin IoT
authors:
- Wang, Dan
- Li, Bo
- Song, Bin
- Liu, Yingjie
- Muhammad, Khan
- Zhou, Xiaokang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2022.3162714
url: https://www.scopus.com/pages/publications/85127730770?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6549--6560
keywords:
- Blockchain
- data and knowledge
- reinforcement learning
- resource management
- sustainable computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0747 — Dual-Driven Resource Management for Sustainable Computing in the Blockchain-Supported Digital Twin IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, emerging sixth-generation (6G) mobile networks, the Internet of Things (IoT), and mobile-edge computing (MEC) technologies have played significant roles in developing a sustainable computing network. In sustainable computing networks, with the increasing scale of data-driven applications, massive privacy-sensitive data are generated. How to effectively process such data on resource-limited IoT devices is challenging. Although edge intelligence (EI) is designed to maintain an appropriate level of ultradelay reliability, low-latency communication (URLLC), real-time data processing, and security and privacy are concerning. In this article, we propose a novel blockchain-supported hierarchical digital twin IoT (HDTIoT) framework, which combines the digital twin to edge network and adopts blockchain technology to achieve secure and reliable real-time computation. We first propose a data and knowledge dual-driven learning solution to ensure real-time interaction and efficient optimization between the physical and the digital worlds. To improve communication and computation efficiency with data and knowledge dual-driven learning, the optimization goal is to minimize the system delay and energy consumption and ensure system reliability and the learning accuracy of IoT devices. Moreover, we propose a proximal policy optimization (PPO)-based multiagent reinforcement learning (MARL) algorithm to solve the resource allocation (RA) problem. Experimental results show that the proposed RA scheme can improve the efficiency of the HDTIoT system, guarantee learning accuracy, reliability, and security, and make a balance between system delay and energy consumption.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0747.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
