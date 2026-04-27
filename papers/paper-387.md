---
id: "paper-387"
title: "MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture"
authors: ["Boubin, Jayson", "Burley, Codi", "Han, Peida", "Li, Bowen", "Porter, Barry", "Stewart, Christopher"]
year: 2022
venue: "Proceedings - 2022 IEEE/ACM 7th Symposium on Edge Computing, SEC 2022"
venue_type: "conference"
doi: "10.1109/SEC54971.2022.00013"
url: "https://www.scopus.com/pages/publications/85145584862?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "68--81"
keywords: ["Autonomy", "Edge Computing", "Multi agent Reinforcement Learning", "UAV"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-387 — MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture

## Metadata

- **Authors:** Boubin, Jayson and Burley, Codi and Han, Peida and Li, Bowen and Porter, Barry and Stewart, Christopher
- **Year:** 2022
- **Venue:** Proceedings - 2022 IEEE/ACM 7th Symposium on Edge Computing, SEC 2022
- **DOI:** 10.1109/SEC54971.2022.00013
- **URL:** https://www.scopus.com/pages/publications/85145584862?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 68--81
- **Language:** English
- **Keywords:** Autonomy; Edge Computing; Multi agent Reinforcement Learning; UAV

### Abstract

Digital agriculture, hailed as the fourth great agricultural revolution, employs software-driven autonomous agents for in-field crop management. Edge computing resources deployed near crop fields support autonomous agents with substantial computational needs for tasks such as AI inference. In large fields, using multiple autonomous agents, called swarms, can speed up crop management tasks if sufficient edge resources are provisioned. However, to use swarms today, farmers and software developers craft their own standalone solutions that are either simple and ineffective or complicated and hard-to-reproduce. We present MARbLE, a platform for developing and managing swarms. MARbLE provides an easy-to-use programming paradigm that helps users build swarm workloads using multi-agent reinforcement learning. Developers supply just two functions Map() and Eval(). The platform automatically compiles and deploys swarms and continuously updates the reinforcement learning models that govern their actions. Developers can experiment with multiple swarm and edge resource configurations both in simulation and with actual in-field runs. We studied real UAV swarms conducting digital agriculture missions. We observe that swarms demanded edge computing resources in bursts; the ratio of average to peak demand was 2.9X. MARbLE uses energy-saving load balancing policies to duty cycle machines during workload demand troughs, leveraging workload patterns to save edge energy. Using MARbLE, we found that four-agent swarms with load balancing techniques sped up missions by 2.1X and reduced edge energy usage by up to 2X compared to state of the art autonomous swarms.  © 2022 IEEE.

## 04 — Title Screening

**Title:** MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MARbLE: Multi-Agent Reinforcement Learning at the Edge for Digital Agriculture
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
