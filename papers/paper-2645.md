---
id: paper-2645
title: 'InfrastructureSentinel: Policy Enforced Guardrails for Secure MCP-driven Infrastructure Agents'
authors:
- Kumar, Tarun
- Tripathy, Aalap
- Saranathan, Gayathri
- Foltin, Martin
- Bhattacharya, Suparna
- Hinchley, Scott
- Bahls, Donald M.
- Brookshire, David
- Kaplan, Larry
- Wisniewski, Robert W.
venue: Proceedings of the AAAI Conference on Artificial Intelligence
venue_type: conference
year: 2026
doi: 10.1609/aaai.v40i47.41468
url: https://www.scopus.com/pages/publications/105034265138?origin=resultslist
publisher: Association for the Advancement of Artificial Intelligence
pages: 40295--40301
keywords:
- Critical infrastructures
- Cybersecurity
- Decision making
- Formal logic
- Formal verification
- Hierarchical systems
- High level languages
- Middleware
- Network security
- Context-Aware
- Contextual reasoning
- Cyber security
- Infrastructure managements
- Model contexts
- Multi-layered
- Multi-layers
- Natural language policy
- Secure modeling
- Security vulnerabilities
- Agents
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: InfrastructureSentinel é middleware de SEGURANÇA/guardrails para agentes MCP — interpreta políticas de segurança e bloqueia ações maliciosas (command injection, privilege escalation).
      É sobre Boundary controle, não sobre o agente que decide RM.
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

# paper-2645 — InfrastructureSentinel: Policy Enforced Guardrails for Secure MCP-driven Infrastructure Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proliferation of Model Context Protocol (MCP) servers in enterprise infrastructure management has revolutionized AI-driven automation while introducing critical multilayered security vulnerabilities that traditional cybersecurity frameworks cannot adequately address. This paper presents InfrastructureSentinel, a novel security middleware that uniquely translates high-level, natural-language policies into context-aware, multi-layer enforcement for MCP-driven agents. Our solution employs a dedicated guardian LLM that interprets natural language policies and applies contextual reasoning to complex infrastructure scenarios, providing dynamic policy enforcement that adapts to user roles, operational timing, and system context. Unlike existing defenses that rely on formal-logic verification or hard-coded rules, our approach implements guardrails at four distinct control points: input message filtering, tool selection validation, execution-time verification, and post-action auditing. The system addresses critical gaps in existing security solutions by providing infrastructure-specific threat modeling, real-time policy adaptation, and comprehensive audit trails with explainable decision making through confidence scores and detailed reasoning. Our evaluation demonstrates the system’s effectiveness in preventing command injection, privilege escalation, and tool poisoning attacks across various enterprise infrastructure scenarios while maintaining operational agility essential for modern data center management. © 2026, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "LLM that interprets natural la" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "InfrastructureSentinel é middleware de SEGURANÇA/guardrails para agentes MCP — interpreta políticas de segurança e bloqueia ações maliciosas (command injection, privilege escalation). É sobre Boundary controle, não sobre o agente que decide RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2645.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
