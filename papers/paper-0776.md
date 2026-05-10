---
id: paper-0776
title: Blockchain-Enabled Intelligent IoT
authors:
- Yao, Haipeng
- Guizani, Mohsen
venue: Wireless Networks (United Kingdom)
venue_type: book-chapter
year: 2023
doi: 10.1007/978-3-031-26987-5_7
url: https://www.scopus.com/pages/publications/85162112417?origin=resultslist
publisher: Springer Nature
pages: 351--391
keywords:
- Blockchain
- Cloud mining pool
- Evolutionary game
- Stackelberg game
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0776 — Blockchain-Enabled Intelligent IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The past few years have witnessed an exponential growth of diverse Internet of Things (IoT) devices as well as compelling applications ranging from industrial production, intelligent transport, and warehouse logistics to medical care. Dramatic advances in IoT technology not only bring enormous economic opportunities but also challenges. Recently, with the appearance of blockchain technology, the integration of IoT and blockchain (BCoT) is considered a promising solution to address these issues. Blockchain provides a secure and scalable data management framework for IoT devices. However, the huge computation and energy cost of the consensus process in blockchain prevents it from being directly applied as a generic platform. To overcome this challenge, we first propose a cloud mining pool-aided BCoT architecture. Based on this architecture, we study the mining pool selection problem and analyze the colony behaviors of IoT devices with different pooling strategies. We propose a centralized evolutionary game-based pool selection algorithm for the sake of maximizing the system utility. Secondly, to overcome the power and computation constraints of the IoT devices in the blockchain platform, we introduce the cloud computing service to the blockchain platform for the sake of assisting to offload computational task from the IIoT network itself. Also, we study the resource management and pricing problem between the cloud provider and miners. And a multi-agent reinforcement learning algorithm is conceived for searching the near-optimal policy. © 2023, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0776.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
