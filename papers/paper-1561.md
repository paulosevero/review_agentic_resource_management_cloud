---
id: paper-1561
title: Collaborative Multi-Agent Reinforcement Learning Approach for Elastic Cloud Resource Scaling
authors:
- Fang, Bruce
- Gao, Danyi
venue: 2025 7th International Conference on Artificial Intelligence Technologies and Applications, ICAITA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAITA67588.2025.11137847
url: https://www.scopus.com/pages/publications/105017971887?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 415--419
keywords:
- elastic expansion
- Multi-agent system
- reinforcement learning
- resource scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1561 — Collaborative Multi-Agent Reinforcement Learning Approach for Elastic Cloud Resource Scaling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper addresses the challenges of rapid resource variation and highly uncertain task loads in cloud computing environments. It proposes an optimization method for elastic cloud resource scaling based on a multi-agent system. The method deploys multiple autonomous agents to perceive resource states in parallel and make local decisions. While maintaining the distributed nature of the system, it introduces a collaborative value function to achieve global coordination. This improves the responsiveness of resource scheduling and enhances overall system performance. To strengthen system foresight, a lightweight state prediction model is designed. It assists agents in identifying future workload trends and optimizes the selection of scaling actions. For policy training, the method adopts a centralized training and decentralized execution reinforcement learning framework. This enables agents to learn effectively and coordinate strategies under conditions of incomplete information. The paper also constructs typical cloud scenarios, including multi-tenancy and burst traffic, to evaluate the proposed method. The evaluation focuses on resource isolation, service quality assurance, and robustness. Experimental results show that the proposed multi-agent scaling strategy outperforms existing methods in resource utilization, SLA violation control, and scheduling latency. The results demonstrate strong adaptability and intelligent regulation. This provides an efficient and reliable new approach to solving the problem of elastic resource scaling in complex cloud platforms.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1561.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
