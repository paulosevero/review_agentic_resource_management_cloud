---
id: paper-2855
title: Optimizing Dependency-Aware Age of Information in STCC Systems via MADRL
authors:
- Xia, Changqing
- Yu, Jisong
- Xu, Chi
- Jin, Xi
- Zeng, Peng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3654899
url: https://www.scopus.com/pages/publications/105027969980?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Dependency-Aware Age of Information
- Industrial Internet of Things
- Manufacturing
- Multi-Agent Deep Reinforcement Learning
- Sensing-Transmission-Computation-Control Co-Design
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2855 — Optimizing Dependency-Aware Age of Information in STCC Systems via MADRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the new generation of information technology, modern manufacturing is shifting from traditional rigid production to flexible, customized models. This transformation imposes higher demands on systems' dynamic adaptability and real-time responsiveness. The emergence of Edge Computing (EC) and the Age of Information (AoI) offers promising solutions to these challenges. Significant progress has been made in areas such as edge resource allocation and information update strategies, contributing to enhanced system responsiveness. However, most existing studies assume task independence, which limits their applicability in complex scenarios (such as high-end manufacturing), where task dependency is dynamic and ubiquitous. In addition, ensuring end-to-end integration of sensing, transmission, computation, and control (STCC) remains a major challenge. To address this gap, this study proposes a collaborative framework focusing on sensing, transmission, computation, and control (STCC), centering around task chains. For the first time, it introduces and defines the Dependency-Aware Age of Information (DAoI) metric to quantify inter-task dependencies and the effects of delay propagation, thereby enabling a more accurate assessment of data timeliness. Additionally, an optimal controller using the Linear Quadratic Regulator (LQR) is designed. Our model optimizes control performance and energy consumption through a Markov Decision Process (MDP). The proposed Dependency-Aware Heterogeneous Task and Resource Co-scheduling (MAPPO-DHTCO) algorithm efficiently manages task dependencies and resource allocation. Experimental results show that this method has significantly improved performance compared to the benchmark method. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2855.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
