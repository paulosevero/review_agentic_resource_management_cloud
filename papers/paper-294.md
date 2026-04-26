---
id: "paper-294"
title: "Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach"
authors: ["Han, Yuqi", "Ai, Lihua", "Wang, Rui", "Wu, Jun", "Liu, Dian", "Ren, Haoqi"]
year: 2021
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2021.3090440"
url: "https://www.scopus.com/pages/publications/85113211162?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "8119--8133"
keywords: ["cooperative cache placement", "edge computing", "Multi-armed bandit"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-294 — Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach

## Metadata

- **Authors:** Han, Yuqi and Ai, Lihua and Wang, Rui and Wu, Jun and Liu, Dian and Ren, Haoqi
- **Year:** 2021
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2021.3090440
- **URL:** https://www.scopus.com/pages/publications/85113211162?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 8119--8133
- **Language:** English
- **Keywords:** cooperative cache placement; edge computing; Multi-armed bandit

### Abstract

Caching high-frequency reuse contents at the edge servers in the mobile edge computing (MEC) network omits the part of backhaul transmission and further releases the pressure of data traffic. However, how to efficiently decide the caching contents for edge servers is still an open problem, which refers to the cache capacity of edge servers, the popularity of each content, and the wireless channel quality during transmission. In this paper, we discuss the influence of unknown user density and popularity of content on the cache placement solution at the edge server. Specifically, towards the implementation of the cache placement solution in the practical network, there are two problems needing to be solved. First, the estimation of unknown users' preference needs a huge amount of records of users' previous requests. Second, the overlapping serving regions among edge servers cause the wrong estimation of users' preference, which hinders the individual decision of caching placement. To address the first issue, we propose a learning-based solution to adaptively optimize the cache placement policy without any previous knowledge of the user density and the popularity of the contents. We develop the extended multi-armed bandit (Extended MAB), which combines the generalized global bandit (GGB) and Standard Multi-armed bandit (MAB), to iteratively estimate both a global parameter, i.e., the user density, and individual parameters, i.e., the popularity of each content. For the second problem, a multi-agent Extended MAB based solution is presented to avoid the mis-estimation of parameters and achieve the decentralized cache placement policy. The proposed solution determines the primary time slot and secondary time slot for each edge server. The edge servers estimate expected satisfied user number of caching a content with the overlap information and determine the cache placement solution. The proposed strategies are proven to achieve the bounded regret according to the mathematical analysis. Extensive simulations verify the optimality of the proposed strategies when comparing with baselines. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cache Placement Optimization in Mobile Edge Computing Networks with Unaware Environment - An Extended Multi-Armed Bandit Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
