---
id: paper-2120
title: 'AI and Generative AI-Driven Automation for Multi-Cloud and Hybrid Cloud Architectures:
  Enhancing Security, Performance, and Operational Efficiency'
authors:
- Seth, Dhruv Kumar
- Ratra, Karan Kumar
- Sundareswaran, Aneeshkumar P
venue: 2025 IEEE 15th Annual Computing and Communication Workshop and Conference,
  CCWC 2025
venue_type: conference
year: 2025
doi: 10.1109/CCWC62904.2025.10903928
url: https://www.scopus.com/pages/publications/105001166441?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 784--793
keywords:
- AI-based cloud management
- AI-driven automation
- Cloud orchestration
- Cloud performance monitoring
- Cloud scalability
- Cloud security
- Cloud security automation
- Generative AI
- Hybrid cloud
- Infrastructure automation
- Machine learning in cloud
- Multi-cloud architecture
- Operational efficiency
- Performance optimization
- Resource allocation optimization Introduction
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
  05-abstract-screening: include
  06-full-text-screening: exclude
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Tarefa de DevOps/observabilidade (incident triage, RCA,
      geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: 'Paper trata automação em multi-cloud/hybrid-cloud via Generative
      AI, mas foco principal é em tarefas DevOps/observabilidade (incident triage,
      RCA, geração de manifestos Kubernetes, fraud detection) — não em decisões de
      resource management (scheduling, placement, scaling). Sec. II-C descreve ''anomaly
      detection'', ''incident detection'', ''prediction of system failures'', ''configuration
      generation'' como aplicações do LLM. Não há um loop agentic LLM-driven que dirige
      alocação/orquestração de recursos em cloud/edge/continuum. Validado contra critério
      boundary: LLM é suporte a DevOps, não tomador de decisão de RM.'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2120 — AI and Generative AI-Driven Automation for Multi-Cloud and Hybrid Cloud Architectures: Enhancing Security, Performance, and Operational Efficiency

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of cloud and hybrid cloud structures presents eCommerce firms with the adaptability and robustness needed to manage expansion and varying user requirements effectively. However, this also brings about challenges concerning security enhancements, distribution of workloads, and cost-effectiveness optimization. Traditional cloud management models often need help to meet these evolving demands efficiently. This research presents a system that leverages Artificial Intelligence (AI) and Generative AI (Gen AI) to effectively automate and enhance cloud and hybrid infrastructures for ecommerce websites. The system adapts infrastructure to traffic times like holidays or sales events by utilizing AI to scale resources as needed. It conserves resources during low user activity periods such as overnight. Ensuring optimal system performance and availability during peak traffic times while cutting costs during traffic periods is essential for cost-effectiveness and efficient resource management. In addition, AI-powered security automation safeguards against changing cyber dangers, and compliance automation guarantees conformity with rules like PCI DSS for payment handling. This report also delves into merging Gen AI into cloud coordination systems, facilitating workflows, and enhancing eCommerce processes. The outcome is a significant drop in operational expenses, a quicker service rollout, and decreased security breaches. Through real-world eCommerce case studies, this paper provides actionable insights for cloud engineers and architects on leveraging AI-driven cloud management to enhance performance, security, and cost-efficiency in multi-cloud and hybrid environments, ensuring seamless user experiences and business continuity. © 2025 IEEE.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-powered" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management."
- **winning_category:** 'D_devops_or_logs_not_rm'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: D_devops_or_logs_not_rm, pattern_id: deployment_assistant_no_rm, matched_substring: "configuration generation" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Paper trata automação em multi-cloud/hybrid-cloud via Generative AI, mas foco principal é em tarefas DevOps/observabilidade (incident triage, RCA, geração de manifestos Kubernetes, fraud detection) — não em decisões de resource management (scheduling, placement, scaling). Sec. II-C descreve 'anomaly detection', 'incident detection', 'prediction of system failures', 'configuration generation' como aplicações do LLM. Não há um loop agentic LLM-driven que dirige alocação/orquestração de recursos em cloud/edge/continuum. Validado contra critério boundary: LLM é suporte a DevOps, não tomador de decisão de RM.
- **agrees_with_regex:** True
- **addressed_hint:** pre_flagged_quality - confirm; paper shows hints of low evaluation rigor (case studies vagos, sem métricas quantitativas), mas primary exclusion reason é scope (DevOps, não RM).
- **evidence_sections:** ['Case Study 1-4 (Sec. VII)', 'Sec. II-C Role of AI/Generative AI (configuration generation, anomaly detection, incident triage)']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
