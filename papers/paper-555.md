---
id: "paper-555"
title: "Admission Control for Games with a Dynamic Set of Players"
authors: ["Bistritz, Ilai", "Bambos, Nicholas"]
year: 2023
venue: "Proceedings of the IEEE Conference on Decision and Control"
venue_type: "conference"
doi: "10.1109/CDC49753.2023.10383907"
url: "https://www.scopus.com/pages/publications/85184813126?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1219--1224"
keywords: ["Distributed computer systems", "Learning algorithms", "Multi agent systems", "Online systems", "Admission-control", "Best response", "Cloud-computing", "Continous time", "Exponentials", "Nash equilibria", "Online marketplaces", "Open multi-agent system", "Performance guarantees", "Poisson process", "Continuous time systems"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-555 — Admission Control for Games with a Dynamic Set of Players

## Metadata

- **Authors:** Bistritz, Ilai and Bambos, Nicholas
- **Year:** 2023
- **Venue:** Proceedings of the IEEE Conference on Decision and Control
- **DOI:** 10.1109/CDC49753.2023.10383907
- **URL:** https://www.scopus.com/pages/publications/85184813126?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1219--1224
- **Language:** English
- **Keywords:** Distributed computer systems; Learning algorithms; Multi agent systems; Online systems; Admission-control; Best response; Cloud-computing; Continous time; Exponentials; Nash equilibria; Online marketplaces; Open multi-agent system; Performance guarantees; Poisson process; Continuous time systems

### Abstract

We consider open games where players arrive according to a Poisson process with rate λ and stay in the game for an exponential random duration with rate μ. The game evolves in continuous time where each player n sets an exponential random clock and updates her action an ∈ {0,⋯, K} when it expires. The players take independent best-response actions that, uninterrupted, can converge to a Nash Equilibrium (NE). This models open multiagent systems such as wireless networks, cloud computing, and online marketplaces. When λ is small, the game spends most of the time in a (time-varying) equilibrium. This equilibrium exhibits predictable behavior and can have performance guarantees by design. However, when λ is too small, the system is under-utilized since not many players are in the game on average. Choosing the maximal λ that the game can support while still spending a target fraction 0 < ρ < 1 of the time at equilibrium requires knowing the reward functions. To overcome that, we propose an online learning algorithm that the gamekeeper uses to adjust the probability θ to admit an incoming player. The gamekeeper only observes whether an action was changed, without observing the action or who played it. We prove that our algorithm learns, with probability 1, a θ∗ such that the game is at equilibrium for at least ρ fraction of the time, and no more than ρ+ϵ(μ,ρ) < 1, where we provide an analytic expression for ϵ(μ,ρ). Our algorithm is a black-box method to transfer performance guarantees of distributed protocols from closed systems to open systems.  © 2023 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
