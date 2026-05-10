---
id: paper-2177
title: The Role of Autonomous Agents in Agent-as-a-Service Cloud Service Model
authors:
- Su, Muthu Aanand
- Niharika, G.L.K.
venue: 2025 International Conference on Computing and Communication Technologies, ICCCT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCCT63501.2025.11020097
url: https://www.scopus.com/pages/publications/105009025759?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Artificial Intelligence
- Autonomous Agents
- Cloud Computing
- Cloud Service Models
- Intel-ligent Agents
- Machine Learning
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2177 — The Role of Autonomous Agents in Agent-as-a-Service Cloud Service Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is a technology that enables the availability of services such as storage, server, and software from a virtually shared pool of resources. It is an on-demand service that makes it vastly available and configurable. There are three main traditional service models of the cloud that are classified according to the usage and configurations that are possible by the user. These service models are arranged in a layered architecture one on the top of another, and thus referred to sometimes as cloud computing stack. IaaS (Infrastructure-as-a-Service) provides virtual infrastructure components such as servers, network, operating systems, storage and many more at an on-demand service. PaaS (Platform-as-a-Service) offers platforms for development of the application and manages all the under-lying infrastructure of the application by the cloud provider. SaaS (Software-as-a-Service) offers software applications to the users where all the infrastructure, patches and updates are managed by the cloud provider. AaaS (Agent-as-a-Service) is an innovative and rapidly growing service that utilizes the power of autonomous artificial agents to deliver cloud services. AaaS employs the various characteristics of autonomous agents such as NLP (Natural Language Processing), data-driven insights, and anytime availability to provide cloud services to users that may lack the required domain knowledge that is required for utilizing other cloud service models. AaaS will deliver better results compared to the traditional service models because of automation of tasks, personalization of cloud services, business need -specific course of actions, quick resolution of issues, and efficient resource management. AaaS models will be offering a result-based service rather than a usage-based service compared to traditional cloud service models, where the user or organization will be paying for the outcomes of using the model rather than the amount of usage of the model. AaaS will be playing a key role in small startups and businesses where the required workforce for people managing the application or the required knowledge for configuring the cloud services is not available, as it eliminates these challenges and drives the organization to better results. AaaS is not limited to a single agent, but multiple agents can be created and each of them be assigned a scope of controls to manage and optimize the cloud services. This multi-agent environment in the cloud will help in efficient communication between agents so that if an issue or service cannot be resolved within the current agent's scope, it invokes the respective agent that has the scope of controls to resolve the issue or service. Thus, AaaS can be viewed as a technological advancement and a potential option to replace the traditional cloud service models.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2177.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
