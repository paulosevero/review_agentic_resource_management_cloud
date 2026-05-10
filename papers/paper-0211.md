---
id: paper-0211
title: Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]
authors:
- Jiang, Yu-Bin
- Liu, Quan
- Hu, Zhi-Hui
venue: Jisuanji Xuebao/Chinese Journal of Computers
venue_type: journal
year: 2020
doi: 10.11897/SP.J.1016.2020.01897
url: https://www.scopus.com/pages/publications/85092468719?origin=resultslist
publisher: Science Press
pages: 1897--1908
keywords:
- Actor-critic algorithm
- Deep learning
- Maximum entropy
- Policy gradient
- Reinforcement learning
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

# paper-0211 — Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, Deep Reinforcement Learning (DRL) combines deep learning with reinforcement learning, and has become one of the research hotspots in the field of artificial intelligence. Deep learning combines intensive learning with amazing results in robot control, Atari 2600 games and more. The first algorithm that combines reinforcement learning with deep learning is TD-Gammon, which surpasses professional chess players in the problem of backgammon. Then there is a series of algorithms from Deep Q-Network (DQN), which has achieved extraordinary performance in Atari 2600 games. But limited by the value function method, DQN cannot be applied to continuous motion tasks. Therefore, the Actor-Critic (AC) algorithm is widely used in DRL because of its excellent scalability. It consists of two parts: the actor and the critic. Usually, the critic uses value function methods to evaluate the action, and the actor uses policy gradient methods for the action generation. This means that the AC method can be applied to continuous motion and discrete motion tasks. Researchers have proposed many AC algorithms, such as Asynchronous Advantage Actor-Critic (A3C) using asynchronous updates, Advantage Actor-Critic (A2C) using multi-agent updates, and Proximal Policy Optimization (PPO) with guaranteed policy improvement. One of the core challenges in reinforcement learning (RL) is how to balance the exploration and exploitation. In order to ensure a high return, the algorithm needs to find those actions that expect high returns in the experience explored in the past. The Immediate rewards for certain actions are high but their expected return is low, and the Agent needs to explore all untraversed actions to prevent the policy from entering local optimum. In other words, the Agent must use the previous experience to obtain higher expectations, and on the other hand must explore to find better action options. In the policy gradient, the maximum entropy regularity term is usually used to increase the randomness of the policy to ensure exploration. The randomness of the policy enables the Agent to traverse all the actions but it will cause the underestimation of the value function and affect the convergence speed and stability of the algorithm. In order to solve the underestimation problem caused by the maximum entropy regular term in the policy gradient, the Maximum-Entropy Correction (MEC) algorithm is proposed. The algorithm has two characteristics: (1) constructing a state action value function estimation using state value function and policy function, the constructed state action value function satisfies the distribution of the real value function; (2) The Berman optimal equation is combined with the constructed state action value function as the objective function of the MEC algorithm. The performance degradation and instability caused delete u the maximum entropy regular term can be solved by using the new objective function MEC algorithm. In order to verify the effectiveness of the algorithm, the algorithm was compared with PPO and A2C on the seven Atari 2600 games: BeamRide, Breakout, Enduro, Pong, Qbert, Seaquest and SpaceInvaders. Experimental results show that MEC improves the stability of the algorithm while improving performance. © 2020, Science Press. All right reserved.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0211.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
