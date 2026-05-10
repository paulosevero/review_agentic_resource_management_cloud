---
id: "paper-2911"
title: "FedFA: Efficient federated large language models with feature adapters"
authors: ["Zhang, Lijia", "Ao, Xiang", "Guo, Songtao", "Qiao, Dewen"]
year: 2026
venue: "Expert Systems with Applications"
venue_type: "journal"
doi: "10.1016/j.eswa.2025.130894"
url: "https://www.scopus.com/pages/publications/105027437885?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Convergence analysis", "Edge computing", "Federated learning", "Large language models", "Resources optimization"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2911 — FedFA: Efficient federated large language models with feature adapters

## Metadata

- **Authors:** Zhang, Lijia and Ao, Xiang and Guo, Songtao and Qiao, Dewen
- **Year:** 2026
- **Venue:** Expert Systems with Applications
- **DOI:** 10.1016/j.eswa.2025.130894
- **URL:** https://www.scopus.com/pages/publications/105027437885?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Convergence analysis; Edge computing; Federated learning; Large language models; Resources optimization

### Abstract

The on-device deployment of federated large language models (FLLM) at edge terminals presents a promising paradigm for distributed intelligence. Yet it faces three critical challenges: resource-constrained edge devices, device heterogeneity, and non-independent and identically distributed (non-IID) data distributions. To address these challenges, this paper proposes an efficient FLLM optimization scheme (FedFA) tailored for resource-constrained scenarios. The scheme achieves dual enhancement of resource efficiency and model accuracy through dynamic parameter update strategies and resource-aware collaborative training mechanisms. Specifically, we first establish the necessity of adaptive local training iterations by profiling the computational capabilities of heterogeneous edge devices. A hybrid parameter update mechanism is then designed, where the backbone parameters of pre-trained language models are kept frozen to minimize computational overhead, while knowledge transfer is achieved through momentum-accelerated adapter fine-tuning. Furthermore, we derive the convergence upper bound under resource constraints and reformulate the global loss minimization problem as a constrained optimization task with the number of local iterations as decision variables, effectively balancing contribution disparities among participants. Experimental results confirm that FedFA achieves substantial performance gains over baseline methods, including up to 80.95% improvement in accuracy, along with a reduction of 93.45% in time consumption and 93.06% in energy consumption. © 2025 Elsevier Ltd

## 04 — Title Screening

**Title:** FedFA: Efficient federated large language models with feature adapters

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** FedFA: Efficient federated large language models with feature adapters
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** FedFA: Efficient federated large language models with feature adapters
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
