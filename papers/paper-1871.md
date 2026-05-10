---
id: paper-1871
title: Contract-Inspired Contest Theory for Controllable Image Generation in Mobile Edge Metaverse
authors:
- Liu, Guangyuan
- Du, Hongyang
- Wang, Jiacheng
- Niyato, Dusit
- Kim, Dong In
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3550815
url: https://www.scopus.com/pages/publications/105000066834?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7389--7405
keywords:
- contest theory
- Generative AI
- image generation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1871 — Contract-Inspired Contest Theory for Controllable Image Generation in Mobile Edge Metaverse

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of immersive technologies has propelled the development of the Metaverse, where the convergence of virtual and physical realities necessitates the generation of high-quality, photorealistic images to enhance user experience. However, generating these images, especially through Generative Diffusion Models (GDMs), in mobile edge computing environments presents significant challenges due to the limited computing resources of edge devices and the dynamic nature of wireless networks. This paper proposes a novel framework that integrates contract-inspired contest theory, Deep Reinforcement Learning (DRL), and GDMs to optimize image generation in these resource-constrained environments. The framework addresses the critical challenges of resource allocation and semantic data transmission quality by incentivizing edge devices to efficiently transmit high-quality semantic data, which is essential for creating realistic and immersive images. The use of contest and contract theory ensures that edge devices are motivated to allocate resources effectively, while DRL dynamically adjusts to network conditions, optimizing the overall image generation process. Experimental results demonstrate that the proposed approach not only improves the quality of generated images but also achieves superior convergence speed and stability compared to traditional methods. This makes the framework particularly effective for optimizing complex resource allocation tasks in mobile edge Metaverse applications, offering enhanced performance and efficiency in creating immersive virtual environments. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1871.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
