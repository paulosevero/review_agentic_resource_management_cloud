---
id: paper-1252
title: LEO satellite computation offloading and resource allocation algorithm based on multiagent reinforcement learning
authors:
- Wang, Shuai
- Guo, Xiye
- Li, Changgeng
- Ma, Xiaotian
- Li, Xuan
- Liu, Jiayang
- Han, Xiaohe
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2024
doi: 10.1117/12.3034960
url: https://www.scopus.com/pages/publications/85200484911?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- computation offloading
- edge computing
- inter-satellite links
- MAPPO
- offloading strategy optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1252 — LEO satellite computation offloading and resource allocation algorithm based on multiagent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> An important direction for future 6G mobile communication networks is achieving global wireless coverage. To realize comprehensive access services, research has been conducted on multi-satellite cooperative computation offloading and resource allocation issues based on inter-satellite links (ISL). Ground users adopt a partial offloading scheme, aiming to minimize the weighted sum of ground user latency and system energy consumption, and an optimization problem is established. A joint optimization algorithm for low earth orbit (LEO) satellite task offloading and resource allocation based on the Multi-Agent Proximal Policy Optimization (MAPPO) framework is proposed. For the joint computing issue among LEO satellites, a Kuhn-Munkres algorithm (KM) based on a greedy algorithm for pre-allocation results followed by a secondary allocation has been designed. On the other hand, to accelerate the convergence speed of the reinforcement learning algorithm, an action masking mechanism is introduced. The action space of agents was optimized using the Particle Swarm Optimization algorithm (PSO), obtaining a prior distribution of the action space, thereby narrowing the search space of the algorithm. Simulation results indicate that, compared to the MAPPO method without the use of trajectory rehearsal action masks, the proposed method demonstrates approximately a 51.5% improvement in convergence performance and a 6.4% enhancement in convergence outcomes. Additionally, the average computational delay for tasks remains stable at around 0.32 seconds, which represents a reduction of up to 5.4% compared to PSO. © 2024 SPIE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1252.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
