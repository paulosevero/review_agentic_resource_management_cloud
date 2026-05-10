---
id: paper-0358
title: Blockchain-based secure energy policy and management of renewable-based smart microgrids
authors:
- Xu, Weicheng
- Li, Jiahui
- Dehghani, Moslem
- GhasemiGarpachi, Mina
venue: Sustainable Cities and Society
venue_type: journal
year: 2021
doi: 10.1016/j.scs.2021.103010
url: https://www.scopus.com/pages/publications/85106233426?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- AC renewable microgrid
- Blockchain technology
- Energy policy
- Microgrid economic
- Secure energy policy
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0358 — Blockchain-based secure energy policy and management of renewable-based smart microgrids

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Industrial Internet of Things (IIoT) has been defined as an architecture that uses the Internet of Things (IoT) and cloud computing to facilitate distributed control of modern industrial systems like AC smart microgrids (MGs). This paper proposes a novel secure energy policy and load sharing approach for renewable MGs for independent utilization of off-grid MGs with power electronic jointing (PEJ) on the basis of master-slave (M-S) which is formed in the IIoT environment. Assume that computations for system dispatch are performed by an upper layer however a lower layer calculates proper control proceedings for the PEJ. A decentralized multi-agent system (MAS) realizes the upper layer of intelligent control on the basis of communication. The layer has 2 control mechanisms: economic dispatch and MAS power balance control. Numerous operating, controlling, and planning to be in the energy industry pay special attention to Blockchain technology. In addition to allowing a common and distributed database, Blockchain technology (B.CT) enables safe, automated, transparent, and economic operations in power distribution systems. If a hacker manipulates and alters the data exchanged between agents, it will result in disrupting system performance in terms of economy and stability MG voltage profile, load distribution, optimized parameters including cost, environmental pollution, and unit output. Therefore, it is necessary to maintain the cyber security of AC smart MG and increase the security of data measured in the sensors and the transaction data between agents. In this paper, B.CT is presented to secure the exchanged data against malicious cyber-attacks in an AC smart MG whose control layers are M-S organized. The simulated system consists of the MG with several distributed generation units that examine cyber-attack points and then compare the results in normal mode and cyber-attack mode and B.CT is presented to increase the cyber security of AC smart MG. © 2021

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0358.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
