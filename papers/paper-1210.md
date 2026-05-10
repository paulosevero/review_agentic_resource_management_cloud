---
id: paper-1210
title: Deep Reinforcement Learning Based Secure Communication and Computing Resource Allocation for Grid Cyber-Physical System
authors:
- Sun, Qiangqiang
- Lian, Gengxiong
- Cao, Zhiwei
- Zeng, Xiangsheng
- Lv, Zhiyao
- Liu, Lei
- Ju, Ying
- Zheng, Tong-Xing
venue: Lecture Notes in Electrical Engineering
venue_type: conference
year: 2024
doi: 10.1007/978-981-97-2757-5_29
url: https://www.scopus.com/pages/publications/85192461037?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 274--283
keywords:
- Deep reinforcement learning
- Edge computing
- Grid CPS
- Physical layer security
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1210 — Deep Reinforcement Learning Based Secure Communication and Computing Resource Allocation for Grid Cyber-Physical System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Grid Cyber-Physical System (CPS) improves the intelligence of the grid by combining computing, communication and control technologies, but this new grid CPS system may also have some new security risks, such as new types of attacks on the connection between the physical and information networks. In this paper, we propose a deep reinforcement learning-based joint optimization scheme to improve the security and resource efficiency of multiple grid sensors by exploiting physical layer security (PLS) techniques in a scenario where a malicious eavesdropper can wiretap confidential grid information. We use Wyner’s wiretap coding scheme to prevent confidential information from being decoded and eavesdropped by malicious eavesdroppers. We minimize the system processing latency while securing the wireless communication process by jointly optimizing the transmit power of the grid sensor and the allocation of computing resource blocks. The optimization problem in this paper is formulated as a multi-agent cooperative optimal decision problem and is solved using a double deep Q-network algorithm. Simulation results demonstrate the robustness and effectiveness of the scheme in ensuring information security and reducing delay. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1210.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
