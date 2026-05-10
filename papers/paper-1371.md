---
id: paper-1371
title: Multiagent Reinforcement Learning for Joint Spectrum and Energy Optimization in CR-NOMA Enabled Internet of Unmanned Agents
authors:
- Ahmed, Saleha
- Uzair, Muhammad
- Ullah, Syed Asad
- Dev, Kapal
- Mahmood, Aamir
- Gidlund, Mikael
- Hassan, Syed Ali
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3624882
url: https://www.scopus.com/pages/publications/105019957422?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 55283--55296
keywords:
- Deep reinforcement learning (DRL)
- energy efficiency (EE)
- energy harvesting (EH)
- Internet of autonomous agents (IAAs)
- nonorthogonal multiple access (NOMA)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1371 — Multiagent Reinforcement Learning for Joint Spectrum and Energy Optimization in CR-NOMA Enabled Internet of Unmanned Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of Internet of Things (IoT) devices and autonomous agents (AAs), there is a rising need for energy- and spectrum-efficient wireless networks that can support large-scale, resource-constrained deployments. To meet this demand, integration of deep reinforcement learning (DRL), nonorthogonal multiple access (NOMA), and energy harvesting (EH) offers a promising approach to enhance energy efficiency (EE) and spectrum utilization in future sixth-generation (6G) networks, particularly for sustainable Internet of UA (IAA) communications. In this article, we investigate an IAA network where multiple low-power secondary users (SUs), equipped with radio frequency EH (RF-EH) antennas, use a cognitive radio-inspired nonorthogonal multiple access (CR-NOMA) scheme to share uplink channels with nearby primary users (PUs). We formulate a joint transmit power control and EH scheduling problem to maximize the long-term EE of the SUs and spectrum utilization of the network, subject to quality-of-service (QoS) constraints. To address the decentralized nature of the problem, we model the environment as a multiagent system where each SU independently optimizes its transmission and EH strategies. A range of DRL and non-DRL algorithms is then applied to solve this optimization problem. We also explore different RF-EH diversity combining techniques to further boost system performance. Simulation results highlight the impact of these techniques on EE of SU, offering insights for optimizing performance under dynamic EH conditions.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1371.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
