---
id: paper-0764
title: 'Edge Learning for B5G Networks With Distributed Signal Processing: Semantic Communication, Edge Computing, and Wireless Sensing'
authors:
- Xu, Wei
- Yang, Zhaohui
- Ng, Derrick Wing Kwan
- Levorato, Marco
- Eldar, Yonina C.
- Debbah, Merouane
venue: IEEE Journal on Selected Topics in Signal Processing
venue_type: journal
year: 2023
doi: 10.1109/JSTSP.2023.3239189
url: https://www.scopus.com/pages/publications/85147274563?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9--39
keywords:
- Artificial intelligence (AI)
- beyond 5G (B5G)
- communication optimization
- deep learning (DL)
- edge learning (EL)
- federated learning (FL)
- Internet-of-Everything (IoE)
- multi-agent reinforcement learning (MARL)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0764 — Edge Learning for B5G Networks With Distributed Signal Processing: Semantic Communication, Edge Computing, and Wireless Sensing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To process and transfer large amounts of data in emerging wireless services, it has become increasingly appealing to exploit distributed data communication and learning. Specifically, edge learning (EL) enables local model training on geographically disperse edge nodes and minimizes the need for frequent data exchange. However, the current design of separating EL deployment and communication optimization does not yet reap the promised benefits of distributed signal processing, and sometimes suffers from excessive signalling overhead, long processing delay, and unstable learning convergence. In this paper, we provide an overview on practical distributed EL techniques and their interplay with advanced communication optimization designs. In particular, typical performance metrics for dual-functional learning and communication networks are discussed. Also, recent achievements of enabling techniques for the dual-functional design are surveyed with exemplifications from the mutual perspectives of 'communications for learning' and 'learning for communications.' The application of EL techniques within a variety of future communication systems are also envisioned for beyond 5G (B5G) wireless networks. For the application in goal-oriented semantic communication, we present a first mathematical model of the goal-oriented source entropy as an optimization problem. In addition, from the viewpoint of information theory, we identify fundamental open problems of characterizing rate regions for communication networks supporting distributed learning-and-computing tasks. We also present technical challenges as well as emerging application opportunities in this field, with the aim of inspiring future research and promoting widespread developments of EL in B5G.  © 2007-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0764.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
