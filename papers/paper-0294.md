---
id: paper-0294
title: Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach
authors:
- Han, Yuqi
- Ai, Lihua
- Wang, Rui
- Wu, Jun
- Liu, Dian
- Ren, Haoqi
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2021
doi: 10.1109/TWC.2021.3090440
url: https://www.scopus.com/pages/publications/85113211162?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8119--8133
keywords:
- cooperative cache placement
- edge computing
- Multi-armed bandit
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0294 — Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Caching high-frequency reuse contents at the edge servers in the mobile edge computing (MEC) network omits the part of backhaul transmission and further releases the pressure of data traffic. However, how to efficiently decide the caching contents for edge servers is still an open problem, which refers to the cache capacity of edge servers, the popularity of each content, and the wireless channel quality during transmission. In this paper, we discuss the influence of unknown user density and popularity of content on the cache placement solution at the edge server. Specifically, towards the implementation of the cache placement solution in the practical network, there are two problems needing to be solved. First, the estimation of unknown users' preference needs a huge amount of records of users' previous requests. Second, the overlapping serving regions among edge servers cause the wrong estimation of users' preference, which hinders the individual decision of caching placement. To address the first issue, we propose a learning-based solution to adaptively optimize the cache placement policy without any previous knowledge of the user density and the popularity of the contents. We develop the extended multi-armed bandit (Extended MAB), which combines the generalized global bandit (GGB) and Standard Multi-armed bandit (MAB), to iteratively estimate both a global parameter, i.e., the user density, and individual parameters, i.e., the popularity of each content. For the second problem, a multi-agent Extended MAB based solution is presented to avoid the mis-estimation of parameters and achieve the decentralized cache placement policy. The proposed solution determines the primary time slot and secondary time slot for each edge server. The edge servers estimate expected satisfied user number of caching a content with the overlap information and determine the cache placement solution. The proposed strategies are proven to achieve the bounded regret according to the mathematical analysis. Extensive simulations verify the optimality of the proposed strategies when comparing with baselines. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0294.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
