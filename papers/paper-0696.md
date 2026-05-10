---
id: paper-0696
title: Learning to Harness Bandwidth with Multipath Congestion Control and Scheduling
authors:
- Pokhrel, Shiva Raj
- Walid, Anwar
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2023
doi: 10.1109/TMC.2021.3085598
url: https://www.scopus.com/pages/publications/85107343246?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 996--1009
keywords:
- access traffic steering switching splitting (ATSSS)
- deep Q-learning
- Multipath TCP
- stability analysis
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0696 — Learning to Harness Bandwidth with Multipath Congestion Control and Scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multipath TCP (MPTCP) has emerged as a facilitator for harnessing and pooling available bandwidth in wireless/wireline communication networks and in data centers. Existing implementations of MPTCP such as, Linked Increase Algorithm (LIA), Opportunistic LIA (OLIA) and BAlanced LInked Adaptation (BALIA) include separate algorithms for congestion control and packet scheduling, with pre-selected control parameters. We propose a Deep Q-Learning (DQL) based framework for joint congestion control and packet scheduling for MPTCP. At the heart of the solution is an intelligent agent for interface, learning and actuation, which learns from experience optimal congestion control and scheduling mechanism using DQL techniques with policy gradients. We provide a rigorous stability analysis of system dynamics which provides important practical design insights. In addition, the proposed DQL-MPTCP algorithm utilizes the 'recurrent neural network' and integrates it with 'long short-Term memory' for continuously i) learning dynamic behavior of subflows (paths) and ii) responding promptly to their behavior using prioritized experience replay. With extensive emulations, we show that the proposed DQL-based MPTCP algorithm outperforms MPTCP LIA, OLIA and BALIA algorithms. Moreover, the DQL-MPTCP algorithm is robust to time-varying network characteristics, and provides dynamic exploration and exploitation of paths.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0696.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
