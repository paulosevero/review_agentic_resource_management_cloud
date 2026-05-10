---
id: paper-1342
title: Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network
authors:
- Zhao, Wentao
- Jing, Wenpeng
- Lu, Zhaoming
- Wen, Xiangming
venue: International Conference on Communications in China, ICCC Workshops 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCCWorkshops62562.2024.10693742
url: https://www.scopus.com/pages/publications/85207646545?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 220--225
keywords:
- delay and energy consumption
- edge and terminal collaboration
- Large language model
- speculative decoding
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

# paper-1342 — Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent years have witnessed the remarkable emer-gence of large language models (LLMs), demonstrating exceptional capabilities in handling complex tasks such as natural language processing, computer vision, and speech processing. However, the prevalent deployment of LLMs on cloud servers poses challenges in ensuring user data privacy and minimizing computation and transmission delay. Moreover, LLM needs to read all the parameters to generate a token for each inference and then splices the original input with the generated token as a new input to generate the next token. To address these concerns, we propose a novel LLM deployment framework leveraging edge and terminal cooperation. Our proposed framework involves deploying LLMs on both edge server and terminal device, where the LLM model on the terminal generates tokens serially, while the model on the edge generates tokens in parallel. This edge-terminal cooperative and serial and parallel combination framework can effectively reduce the computation delay of token generation. To further optimize the performance of the proposed framework, we formulate an optimization problem aimed at minimizing average delay and energy consumption. Considering its integer programming property, we employ a branch and bound algorithm to efficiently solve this problem. Extensive simulation results provide compelling evidence of the effectiveness of our LLM deployment optimization algorithm. Under diverse channel conditions and terminal device computing capabilities, our proposed scheme consistently outperforms other baseline algorithms in terms of delay and energy consumption. These findings underscore the potential of our approach in facilitating the practical deployment of LLMs on edge and terminal.  © 2024 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1342.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
