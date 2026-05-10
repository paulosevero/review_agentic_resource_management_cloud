---
id: paper-1655
title: A Cloud–Edge Collaborative Architecture for Multimodal LLM-Based Advanced Driver Assistance Systems in IoT Networks
authors:
- Hu, Yaqi
- Ye, Dongdong
- Kang, Jiawen
- Wu, Maoqiang
- Yu, Rong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3509628
url: https://www.scopus.com/pages/publications/85211225296?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13208--13221
keywords:
- Advanced driver assistance systems (ADASs)
- DDPG
- diffusion model
- edge computing
- Internet of Things (IoT) networks
- multimodal large language models (MLLMs)
- task offloading
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: true
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

# paper-1655 — A Cloud–Edge Collaborative Architecture for Multimodal LLM-Based Advanced Driver Assistance Systems in IoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Advanced driver assistance systems (ADASs) enhance driving safety and convenience by providing auxiliary functions. However, traditional rule-based or learning-based ADAS lack the capability for commonsense-based environmental understanding and multisensor data fusion, which leads to limitations in complex dynamic environments. Multimodal large language models (MLLMs) can effectively integrate data from different modalities and possess strong environmental perception and commonsense reasoning abilities, offering more intelligent driver assistance services within Internet of Things (IoT) networks. In this article, we propose a cloud-edge collaborative ADAS based on MLLMs, utilizing IoT networks by deploying a smaller model, CogVLM2, at the edge and a larger model, ChatGPT-4o, in the cloud to achieve collaborative driver assistance services. Specifically, we first reannotate the BDD-X dataset and use it to fine-tune CogVLM2 with LoRA, while applying few-shot learning to ChatGPT-4o to enhance their understanding and decision-making capabilities in traffic scenarios. We then formulate service latency, energy consumption, and Quality-of-Service (QoS) models for the cloud-edge collaborative ADAS in IoT networks, optimizing the combination of these models. Finally, we design an improved DDPG-based task offloading algorithm by introducing a multistep reward mechanism and using a diffusion model to generate noise, aiming to determine the optimal execution location (i.e., cloud, edge, or local) for each task. Experimental results show that both CogVLM2 and ChatGPT-4o can achieve basic ADAS functionality. After fine-tuning and few-shot learning, their task success rates were significantly improved. Moreover, compared to other mainstream deep reinforcement learning-based task offloading algorithms, the improved DDPG task offloading algorithm demonstrates better performance in latency, energy consumption, and QoS within IoT networks. © 2014 IEEE.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1655.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
