---
id: paper-1040
title: Secure Offloading With Adversarial Multi-Agent Reinforcement Learning Against Intelligent Eavesdroppers in UAV-Enabled Mobile Edge Computing
authors:
- Li, Xulong
- Huangfu, Wei
- Xu, Xinyi
- Huo, Jiahao
- Long, Keping
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2024
doi: 10.1109/TMC.2024.3439016
url: https://www.scopus.com/pages/publications/85200803693?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13914--13928
keywords:
- Mobile edge computing (MEC)
- multi-agent reinforcement learning (MARL)
- resource allocation
- unmanned aerial vehicle (UAV)
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
    my_justification: RL
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

# paper-1040 — Secure Offloading With Adversarial Multi-Agent Reinforcement Learning Against Intelligent Eavesdroppers in UAV-Enabled Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has attracted widespread attention due to its ability to effectively alleviate the cloud computing load and significantly reduce latency. However, the potential eavesdroppers challenge the security of the MEC systems and the rapid development of artificial intelligence (AI) has made this security situation more severe. In most existing studies, the eavesdroppers are non-intelligent and it is assumed that they are fixed or move in a simple manner. Obviously, there is a gap from such an assumption to the real conditions that the eavesdropping unmanned aerial vehicles (UAVs) may adjust their flight paths intelligently. To better reflect real-world scenarios, we consider a multi-UAV-assisted MEC system in the presence of intelligent eavesdroppers and propose an adversarial multi-agent reinforcement learning (MARL)-based scheme for secure computational offloading and resource allocation. With this scheme, we aim to solve the zero-sum game between the legitimate UAVs and the eavesdropping UAVs, in which the two types of UAVs take turns acting as the agents of MARL to alternately optimize their respective opposing objectives. The simulation experimental results indicate that the proposed scheme significantly outperforms the existing baseline methods in dealing with the intelligent eavesdropping UAVs, and ensures high energy efficiency of Internet of Things (IoT) devices even in the worst-case scenario when dealing with potential eavesdropping threats.  © 2002-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1040.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
