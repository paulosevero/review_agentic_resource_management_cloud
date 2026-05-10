---
id: paper-2412
title: 'LLMCatalyst: A Novel Incentive Mechanism for Client-Assisted Foundation Model Training'
authors:
- Zeng, Rongfei
- Zhao, Mingyang
- Han, Jinpeng
- Bi, Yuanguo
- Wang, Xingwei
venue: IEEE International Workshop on Quality of Service, IWQoS
venue_type: conference
year: 2025
doi: 10.1109/IWQoS65803.2025.11143425
url: https://www.scopus.com/pages/publications/105017008490?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- auction
- client-assisted training
- LLMs
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
    my_justification: LLM as workload
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

# paper-2412 — LLMCatalyst: A Novel Incentive Mechanism for Client-Assisted Foundation Model Training

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large foundation models, such as SORA and GPT-4, have emerged as a mainstream and promising trend in the deep learning community. Many evidences have showcased that the training of these large models can be facilitated by leveraging vast numbers of consumer-grade GPUs from client devices, rather than relying solely on high-end GPUs in centralized data centers. Although previous studies have primarily focused on the technical aspects of client-assisted model training, the incentive mechanisms for this scenario remain largely unexplored. Insights from P2P networks suggest that a well-designed incentive mechanism is both catalytic and indispensable for the widespread adoption of client-assisted model training. In this paper, we explore the incentive design problem of client-assisted model training and envision a novel hierarchical procurement auction that captures some properties of client-assisted model training, such as asynchronous client arrivals, synchronous training processes, and complex resource requirements. We formulate the incentive design problem as a social cost minimization problem with l<sub>∞</sub>-norm constraints and transform it into an approximation problem with an l2-norm objective function which facilitates the design of an efficient approximation algorithm. Subsequently, we propose a primal-dual approximation algorithm for client selection and payment allocation, which guarantees a small competitive ratio and truthfulness. Both theoretical studies and experiments using real-world trace data are conducted to demonstrate the efficacy of our method. © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2412.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
