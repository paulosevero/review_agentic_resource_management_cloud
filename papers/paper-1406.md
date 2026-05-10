---
id: paper-1406
title: 'CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis'
authors:
- Azhari, Michael Meier
- Soussi, Wissem
- Gur, Gurkan
venue: 2025 IEEE Conference on Network Function Virtualization and Software-Defined Networking, NFV-SDN 2025
venue_type: conference
year: 2025
doi: 10.1109/NFV-SDN66355.2025.11349649
url: https://www.scopus.com/pages/publications/105033359273?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Digital forensics
- Forensic engineering
- Network security
- Defense strategy
- Defensive mechanism
- Forensic analysis
- Future networks
- Incident analysis
- Live migrations
- Moving target defense
- Near-real time
- Offline
- On-line analysis
- Containers
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    - ovr_with_llm
    - ovr_using_llm
    - ovr_llm_modifier
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1406 — CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Future networks are expected to rely heavily on cloud-native technologies. However, the security and resilience of those systems deserve more attention. CubeMig presents an approach to enhancing security in Kubernetes environments, enabling pods to live migrate, leveraged as part of a Moving Target Defense (MTD) strategy. CubeMig showcases reactive defensive mechanisms by incorporating automated live migrations as a response to threats detected in near real-time at the OS kernel level, using an eBPF-based approach. The mitigation process is further enhanced with forensic analysis on the checkpoint of the migrated container, providing insights into the compromised containers offline and instantiating the container in a sandboxed environment for further online analysis. Finally, we augment the forensic analysis output using LLMs, generating human-explainable analysis from the forensic logs to support post-incident investigation and providing relevant security recommendations. Experimental results validate the approach's effectiveness in a human-in-the-loop setting, showcasing the system's ability to detect and respond to attack scenarios such as reverse shell execution, log tampering, and system destruction. © 2025 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_with_llm', 'ovr_using_llm', 'ovr_llm_modifier']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: llm_as_workload, pattern_id: ovr_with_llm, matched_substring: "with LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_using_llm, matched_substring: "using LLMs" }`
  - `{ category: llm_as_workload, pattern_id: ovr_llm_modifier, matched_substring: "LLM-Augmented" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1406.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
