---
id: paper-1050
title: 'SGCS: An Intelligent Stackelberg-Game-Based Computation Offloading and Resource Pricing Scheme in Blockchain-Enabled MEC for IIoT'
authors:
- Lin, Bing
- Chen, Xuzhan
- Chen, Xing
- Ma, Yun
- Xiong, Neal N.
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3360152
url: https://www.scopus.com/pages/publications/85186990468?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 26727--26740
keywords:
- Computation offloading
- Industrial Internet of Things (IIoT)
- mobile edge computing (MEC)
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Game theory.
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

# paper-1050 — SGCS: An Intelligent Stackelberg-Game-Based Computation Offloading and Resource Pricing Scheme in Blockchain-Enabled MEC for IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) offers low-latency and flexible computing services for mobile devices (MDs) in Industrial Internet of Things (IIoT). Edge servers (ESs) in general belong to different subjects and will focus on their own interests. They may be reluctant to provide computation resources to MDs without appropriate incentives. Meanwhile, there is a trust issue in trading computation resources between ESs and MDs. Due to the complex interaction between ESs and MDs, it is a challenge for ESs to gain satisfactory revenue through reasonable resource pricing strategies, and for MDs to improve their Quality of Experience (QoE) through efficient computation offloading strategies. This article proposes a Stackelberg game-based computation offloading and resource pricing scheme (SGCS) in blockchain-enable MEC for IIoT. First, a blockchain-based resource trading framework is designed to enable trusted resource transactions. Second, a multileader multifollower Stackelberg game is presented to analyze the complex interactions in the multi-ES and multi-MD environments. Finally, the iterative proximal algorithm (IPA) for MDs' offloading decision and the subgradient-based iterative pricing algorithm (SIPA) for ESs' pricing decision are proposed, respectively, which guarantees that the game converges to a Stackelberg equilibrium (SE). Compared with multiagent deep deterministic policy gradient, genetic algorithm and PSO-GA (i.e., benchmark strategies), the average disutility of MDs with our proposed scheme is reduced by 6.95%-13.07%, 3.09%-20.41%, and 2.36%-17.22%, respectively. Moreover, with the increase of the number of MDs, our proposed scheme has better robustness, which can effectively deal with large-scale scenarios.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Game theory."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1050.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
