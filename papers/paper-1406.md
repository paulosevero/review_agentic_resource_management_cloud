---
id: "paper-1406"
title: "CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis"
authors: ["Azhari, Michael Meier", "Soussi, Wissem", "Gur, Gurkan"]
year: 2025
venue: "2025 IEEE Conference on Network Function Virtualization and Software-Defined Networking, NFV-SDN 2025"
venue_type: "conference"
doi: "10.1109/NFV-SDN66355.2025.11349649"
url: "https://www.scopus.com/pages/publications/105033359273?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Digital forensics", "Forensic engineering", "Network security", "Defense strategy", "Defensive mechanism", "Forensic analysis", "Future networks", "Incident analysis", "Live migrations", "Moving target defense", "Near-real time", "Offline", "On-line analysis", "Containers"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1406 — CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis

## Metadata

- **Authors:** Azhari, Michael Meier and Soussi, Wissem and Gur, Gurkan
- **Year:** 2025
- **Venue:** 2025 IEEE Conference on Network Function Virtualization and Software-Defined Networking, NFV-SDN 2025
- **DOI:** 10.1109/NFV-SDN66355.2025.11349649
- **URL:** https://www.scopus.com/pages/publications/105033359273?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Digital forensics; Forensic engineering; Network security; Defense strategy; Defensive mechanism; Forensic analysis; Future networks; Incident analysis; Live migrations; Moving target defense; Near-real time; Offline; On-line analysis; Containers

### Abstract

Future networks are expected to rely heavily on cloud-native technologies. However, the security and resilience of those systems deserve more attention. CubeMig presents an approach to enhancing security in Kubernetes environments, enabling pods to live migrate, leveraged as part of a Moving Target Defense (MTD) strategy. CubeMig showcases reactive defensive mechanisms by incorporating automated live migrations as a response to threats detected in near real-time at the OS kernel level, using an eBPF-based approach. The mitigation process is further enhanced with forensic analysis on the checkpoint of the migrated container, providing insights into the compromised containers offline and instantiating the container in a sandboxed environment for further online analysis. Finally, we augment the forensic analysis output using LLMs, generating human-explainable analysis from the forensic logs to support post-incident investigation and providing relevant security recommendations. Experimental results validate the approach's effectiveness in a human-in-the-loop setting, showcasing the system's ability to detect and respond to attack scenarios such as reverse shell execution, log tampering, and system destruction. © 2025 IEEE.

## 04 — Title Screening

**Title:** CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** CubeMig: MTD Live Migration in Kubernetes with LLM-Augmented Post-Incident Analysis
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
