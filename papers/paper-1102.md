---
id: paper-1102
title: Intelligent Heterogeneous Aerial Edge Computing for Advanced 5G Access
authors:
- Nguyen, Tri-Hai
- Truong, Thanh Phung
- Tran, Anh-Tien
- Dao, Nhu-Ngoc
- Park, Laihyuk
- Cho, Sungrae
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2024
doi: 10.1109/TNSE.2024.3371434
url: https://www.scopus.com/pages/publications/85187003354?origin=resultslist
publisher: IEEE Computer Society
pages: 3398--3411
keywords:
- Aerial computing platform
- multi-agent deep deterministic policy gradient
- non-orthogonal multiple access
- resource allocation
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

# paper-1102 — Intelligent Heterogeneous Aerial Edge Computing for Advanced 5G Access

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of the Internet of Things (IoT), aerial computing platforms (ACPs), such as unmanned aerial vehicles and high-altitude platforms with edge computing capabilities have the potential to significantly expand coverage, enhance performance, and handle complex computational tasks for IoT devices (IoTDs). Non-orthogonal multiple access (NOMA) has also emerged as a promising multiple access technology for advanced 5G networks. This paper presents a multi-ACP-enabled NOMA edge network, which enables heterogeneous ACPs to provide computational assistance to IoTDs. To minimize delay and energy consumption, we formulate a joint task offloading and resource allocation problem that considers IoTD association, offloading ratio, transmit power, and computational resource allocation variables. To address the complexity of the optimization problem, it is modeled as a multi-agent Markov decision process and solved using a multi-agent deep deterministic policy gradient (MADDPG)-based solution. Extensive simulation results demonstrate that the proposed MADDPG-based framework can remarkably adapt to the dynamic nature of multi-ACP-enabled NOMA edge networks. It consistently outperforms various benchmark schemes regarding energy efficiency and task processing delay across different simulated scenarios.  © 2013 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1102.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
