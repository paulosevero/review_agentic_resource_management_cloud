---
id: "paper-1407"
title: "Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach"
authors: ["Baccour, Emna", "Erbad, Aiman", "Mohamed, Amr", "Hamdi, Mounir", "Guizani, Mohsen"]
year: 2025
venue: "IEEE Wireless Communications and Networking Conference, WCNC"
venue_type: "conference"
doi: "10.1109/WCNC61545.2025.10978306"
url: "https://www.scopus.com/pages/publications/105006470020?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["BSUM", "collaborative edge computing", "Generative AI", "LLM", "prompts caching", "RL"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1407 — Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach

## Metadata

- **Authors:** Baccour, Emna and Erbad, Aiman and Mohamed, Amr and Hamdi, Mounir and Guizani, Mohsen
- **Year:** 2025
- **Venue:** IEEE Wireless Communications and Networking Conference, WCNC
- **DOI:** 10.1109/WCNC61545.2025.10978306
- **URL:** https://www.scopus.com/pages/publications/105006470020?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** BSUM; collaborative edge computing; Generative AI; LLM; prompts caching; RL

### Abstract

Generative AI (GAI) and Large Language Models (LLMs) have revolutionized natural language processing and content creation. However, their significant computational demands during inference often require cloud servers, which are currently the only viable option for handling complex multi-modal models like GPT-4. The inherent complexity of these models increases latency, posing challenges even within cloud environments. Furthermore, cloud reliance brings other challenges, including high bandwidth consumption to transfer diverse data types. Worse, in personalized GAI applications like virtual assistants, similar prompts frequently occur, causing redundant transmission and computation of replies, which further increases overhead. Accelerating the inference of multi-modal systems is, therefore, critical in artificial intelligence. In this paper, we aim to improve the inference efficiency through prompt caching; if a current prompt is semantically similar to a previous one, the system can reuse the earlier response without invoking the model again. We leverage collaborative edge computing to cache popular replies and store their request embeddings. New prompts are locally processed to extract embeddings, with their qualities determined by the resources available on edge servers. Our problem is formulated as an optimization to manage offloading decisions for GAI tasks, aiming to avoid cloud inferences and minimize latency while maximizing reply quality. Given its non-convex nature, we propose to solve it via Block Successive Upper Bound Minimization (BSUM). Reinforcement learning is employed to actively pre-cache prompts, tackling the complexity of unknown prompt popularity. Our approach demonstrates near-optimal performance, significantly outperforming cloud-only solutions. © 2025 IEEE.

## 04 — Title Screening

**Title:** Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach
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
