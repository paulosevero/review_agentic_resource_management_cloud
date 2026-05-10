---
id: paper-2002
title: Data governance, core technologies, and application challenges of China’s agricultural large models; [中国农业大模型数据治理、核心技术与应用挑战]
authors:
- Ouyang, Zhengzheng
- Ma, Yucong
- Kou, Yuantao
- Liu, Xiaojie
venue: Nongye Gongcheng Xuebao/Transactions of the Chinese Society of Agricultural Engineering
venue_type: journal
year: 2025
doi: 10.11975/j.issn.1002-6819.202505226
url: https://www.scopus.com/pages/publications/105033041099?origin=resultslist
publisher: Chinese Society of Agricultural Engineering
pages: 153--162
keywords:
- agricultural large models
- artificial intelligence
- large language models (LLMs)
- smart agriculture
- vertical domain
language: Chinese
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2002 — Data governance, core technologies, and application challenges of China’s agricultural large models; [中国农业大模型数据治理、核心技术与应用挑战]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large agricultural models can often be required to align with the strategic outline in the National Smart Agriculture Action Plan (2024-2028). This research was performed on the architecture, key technologies, and scenario-specific adaptation of the agricultural large models. A large agricultural model was also evaluated on the construction and operational effectiveness across diverse agricultural applications. Major impediments were then identified for the large-scale adoption, thereby providing actionable insights for the full industrial chain and sustainable agriculture. Among them, 15 representative agricultural large models were selected, according to the domain specificity, scenario coverage, and technical diversity. An analytical framework was adopted, including the data architecture, model design, training schemes, and actual deployment. Each model was examined against its underlying base model, such as generating a pre-trained Transformer model (GPT), a bidirectional encoder representation of the Transformer model (BERT), or a multimodal variant, as well as its fine-tuning strategy, including supervised fine-tuning (SFT), retrieval enhancement generation (RAG), instruction, and human feedback reinforcement learning (RLHF). Evaluation criteria included the computational efficiency, support for multimodal data integration, and performance in real-world agriculture, such as crop monitoring, pest control, and decision support systems. The results show that the large language models (LLMs) were enhanced by multimodal learning and structured agricultural knowledge bases. The performance was significantly improved over the range of agricultural applications. The better performance was achieved in the model architecture with the cross-modal attention mechanisms, hybrid knowledge embedding, and Transformer fusion modules. Significant gains were observed in some tasks, including pest and disease identification from images, yield prediction, soil health prediction, irrigation planning, and personalized agronomic consulting services. For example, the retrieval enhancement generation (RAG) shared a higher accuracy in integrating the real-time sensor data, satellite imagery, and historical agronomic records for better prediction. Several challenges were also identified. A major problem was the limited generalization of the large model, due to the significant regional differences in the climate, soil properties, crop varieties, and tillage. Thus, the performance of the model was reduced when applied to untrained data. In addition, a major bottleneck was the difference in the computing resources; While the model training and complex inference tasks were required for the high-performance computing infrastructure, actual agriculture-particularly in the rural and remote areas. Some limitations were also found in the power, connectivity, and edge computing, leading to unacceptable delays in real-time applications. Semantic misalignment during multimodal fusion-particularly between textual, visual, and genomic data, continues to cause feature inconsistencies and high information loss rates in extreme cases. Some systemic issues included the fragmented and non-standardized data governance, high costs and subjectivity in data annotation, insufficient incentives for cross-institutional data sharing, and economic barriers to adoption among smallholder farmers. It was still lacking in the emerging applications, such as gene editing and agricultural drones. Generally, there was also low digital literacy among end-users. A coordinated approach is often required to effectively harness the potential of the large models in agriculture, particularly from experimental platforms to a scalable industry. Firstly, a unified hierarchical data governance can be expected for the data interoperability, privacy, and sharing, according to the standardized protocols and metadata. Secondly, the cross-modal semantic alignment can be used to realize the model's lightweight, efficient distributed training, and low-latency reasoning optimization of edge devices, such as quantification and knowledge extraction. Finally, an accessible ecosystem can be supported by the multi-stakeholder engagement (including institutions, research institutions, technology providers, and farmers' communities) under policy incentives, including affordable digital tools, capacity-building programs, and publicly verified platforms. Collectively, the AI large models can be integrated with real-world agricultural systems, thereby contributing to intelligent, efficient, and accessible agriculture. © 2025 Chinese Society of Agricultural Engineering. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2002.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
