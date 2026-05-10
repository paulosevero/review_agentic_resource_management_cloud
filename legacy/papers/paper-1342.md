---
id: "paper-1342"
title: "Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network"
authors: ["Zhao, Wentao", "Jing, Wenpeng", "Lu, Zhaoming", "Wen, Xiangming"]
year: 2024
venue: "International Conference on Communications in China, ICCC Workshops 2024"
venue_type: "conference"
doi: "10.1109/ICCCWorkshops62562.2024.10693742"
url: "https://www.scopus.com/pages/publications/85207646545?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "220--225"
keywords: ["delay and energy consumption", "edge and terminal collaboration", "Large language model", "speculative decoding"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1342 — Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network

## Metadata

- **Authors:** Zhao, Wentao and Jing, Wenpeng and Lu, Zhaoming and Wen, Xiangming
- **Year:** 2024
- **Venue:** International Conference on Communications in China, ICCC Workshops 2024
- **DOI:** 10.1109/ICCCWorkshops62562.2024.10693742
- **URL:** https://www.scopus.com/pages/publications/85207646545?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 220--225
- **Language:** English
- **Keywords:** delay and energy consumption; edge and terminal collaboration; Large language model; speculative decoding

### Abstract

Recent years have witnessed the remarkable emer-gence of large language models (LLMs), demonstrating exceptional capabilities in handling complex tasks such as natural language processing, computer vision, and speech processing. However, the prevalent deployment of LLMs on cloud servers poses challenges in ensuring user data privacy and minimizing computation and transmission delay. Moreover, LLM needs to read all the parameters to generate a token for each inference and then splices the original input with the generated token as a new input to generate the next token. To address these concerns, we propose a novel LLM deployment framework leveraging edge and terminal cooperation. Our proposed framework involves deploying LLMs on both edge server and terminal device, where the LLM model on the terminal generates tokens serially, while the model on the edge generates tokens in parallel. This edge-terminal cooperative and serial and parallel combination framework can effectively reduce the computation delay of token generation. To further optimize the performance of the proposed framework, we formulate an optimization problem aimed at minimizing average delay and energy consumption. Considering its integer programming property, we employ a branch and bound algorithm to efficiently solve this problem. Extensive simulation results provide compelling evidence of the effectiveness of our LLM deployment optimization algorithm. Under diverse channel conditions and terminal device computing capabilities, our proposed scheme consistently outperforms other baseline algorithms in terms of delay and energy consumption. These findings underscore the potential of our approach in facilitating the practical deployment of LLMs on edge and terminal.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge and Terminal Cooperation Enabled LLM Deployment Optimization in Wireless Network
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
