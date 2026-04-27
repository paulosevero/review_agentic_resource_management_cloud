# Abstract-Screening Design Decisions — Stage 05

**Audience.** The user (`opaulosevero@gmail.com`), as a reference document during the manual review of `spreadsheet_abstract_screening.xlsx` aba `05 — Abstract Screening`. A future LLM agent reading this in a separate conversation should also understand the design without further context.

**State.** Stage 05 consolidate is committed (`[05] consolidate`, hash `7df6821`). Awaiting human review of `My Final Decision` / `My Justification` before lock.

---

## 1. Inputs

- **Corpus**: 572 papers with `status["04-title-screening"] == include` (i.e., the user's stage-04 includes after 31 manual mistakes were corrected during refinement — see `planning/title-screening-refinement.md`).
- **Source text**: title + full abstract (extracted from the `### Abstract` section of each `papers/paper-NNN.md`).
- **Classifier**: `scripts/deterministic_classifier.py` (same engine as title stage; pure function `(text, config) → decision`).
- **Config**: `protocols/classifier-config-abstract.json` (10 priority levels, 220 patterns + overrides).
- **Tiebreaker LLM**: Sonnet 4.6 (Medium effort) via the Agent tool in this conversation. Used only on `winning_category == "no_signal"` papers.

---

## 2. Architectural deltas vs stage 04

Stage 05 inherits the title-stage architecture (priority-ordered regex with override suppression) and adds three structural changes:

### 2.1 Cat 3 (RL) gains an LLM-presence override

Title-stage behavior: pure RL/MARL papers were excluded at Cat 3; RL+LLM hybrids were caught later by Cat 7 (LLM/Agentic AI generic) → Include.

Abstract-stage behavior: same triggers, but with a new override pattern that matches any LLM signal (LLM, GPT, foundation model, agentic, generative AI, RAG, prompt engineering, etc.). When the override fires, Cat 3 is suppressed and the paper continues evaluation in lower-priority categories. **Practical effect**: papers like "LLM-Guided DRL for Resource Allocation" cleanly fall through to `agent_llm_based` or `llm_agentic_ai_generic` instead of being misclassified as RL.

### 2.2 Cat 4 (LLM as workload) gets richer override patterns

Added abstract-specific overrides that recognize LLM-as-decision-maker contexts:

- "LLM decides / selects / orchestrates / generates a placement plan / generates a policy / reasons about ..."
- "agentic workflow / agentic pipeline / agentic loop / agentic architecture"
- "using LLMs to decide / select / recommend / plan / schedule / allocate / orchestrate"

Conversely, the trigger set was widened to better catch workload framing in richer text:

- "we propose a system to serve / deploy / host LLMs"
- "LLM inference engine / serving infrastructure / pipeline"
- "for efficient/scalable LLM inference / serving / training / fine-tuning / deployment"

### 2.3 Three NEW categories: classical_agents (Exclude), mas_llm_based (Include), agent_llm_based (Include)

The most consequential change. At title stage, `mas` and `agent` were soft-Includes (the title alone could not distinguish modern LLM-based agents from classical ones). At abstract stage, the richer text usually reveals the answer — so the soft-Include is replaced by three explicit categories:

**Cat 5 — `classical_agents` (Exclude)**

Decision: `Exclude`  
Justification: `MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)`  
Priority: 5

Triggers (any one fires the category):

- Plain MAS / multi-agent / multiagent term
- Plain agent / agents term
- Explicit classical-MAS markers: JADE framework, FIPA-compliant, contract-net protocol, holonic agent, BDI architecture, behavior-based agent, Aglets, classical mobile-agent platforms, blackboard system, auction-based protocol, negotiation protocol among agents, agent-oriented software engineering, KQML

Override (suppresses the exclusion):

- Any LLM signal anywhere in the abstract (LLM, GPT, ChatGPT, LLaMA, BERT, foundation/large-language/small-language/vision-language model, transformer, agentic, generative AI, GenAI, AIGC, llm-driven/empowered/aided/etc., prompt-driven/based/engineering, chain-of-thought, RAG, retrieval-augmented, AI-driven/based/powered/assisted/etc., AI agent, LLM agent, agent AI, chatbot, conversational AI, NLP, intent-driven/based, autonomic, neurosymbolic, language-augmented)

**Why this design.** Per the user's screening rules, a paper that mentions MAS/agent **but no LLM signal anywhere in the abstract** is overwhelmingly classical or pure-MARL — so default Exclude. If the abstract DOES contain an LLM signal, the override suppresses the exclusion and the paper falls to Cat 6 / Cat 7 / Cat 8 (LLM-based Include categories).

**Effect on the corpus.** 193 of 572 papers (~34%) hit `classical_agents`. This was confirmed via sampling: every sampled paper-1350 (UAV MAS), paper-1431 (urban-public-health MAS), paper-609 (load-balancing MAS), paper-389 (autonomous Edge MAS), paper-950 (multi-agent routing), paper-423 (multi-agent ML for energy), paper-208 (intelligent agent for energy savings), paper-2647 (agent-based data dissemination), paper-334 (agent-based SLA negotiation) was indeed classical without LLM.

**Cat 6 — `mas_llm_based` (Include)**

Decision: `Include`  
Justification: `Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).`  
Priority: 6

Single AND-pattern using positive lookaheads:

```
(?=.*\b(?:multi-agent|multiagent|MAS|multi-agent system)\b)(?=.*<LLM_SIGNAL_REGEX>).+
```

Both lookaheads must succeed (MAS term present AND LLM signal present, anywhere in the abstract). The `.+` consumes one character so the regex engine produces a positive match.

**Effect.** 37 papers fired this category. Sampled: paper-1588 (Conversational AI multi-agent for ML infra monitoring), paper-1689 (Autonomous Security Orchestration with Multi-Agent Systems), paper-1469 (NetGPT-Enabled Dynamic RM with multi-agent).

**Cat 7 — `agent_llm_based` (Include)**

Same shape, but with `\bagent[s]?\b` instead of MAS. Priority 7 (after `mas_llm_based`) so MAS+LLM gets the more specific justification when both apply.

**Effect.** 40 papers. Sampled: paper-2028 (LLM-based cost-aware task scheduling), paper-1780 (Agent-as-a-Service AI-Native Edge), paper-1722 (Autonomous AI Agents on Edge Fabric).

### 2.4 Removed `mas` and `agent` standalone categories

The old Cat 5 (`mas`) and Cat 6 (`agent`) from title stage are dropped at abstract stage. Their previous behavior (soft-Include for any MAS/agent term) is now subsumed by the override mechanism: papers that hit MAS/agent triggers AND have an LLM signal escape `classical_agents` via the override and land in `mas_llm_based` / `agent_llm_based` / `llm_agentic_ai_generic`. Papers that hit MAS/agent triggers but NO LLM signal are now correctly classified as `classical_agents` Exclude.

---

## 3. Final priority order (abstract stage)

| Priority | Category | Decision | Notes |
|---:|---|---|---|
| 1 | `out_of_scope` | Exclude | inherited from title (with 4 over-fitted patterns removed during refinement; see title doc §6.2) |
| 2 | `review` | Exclude | inherited + abstract phrases ("this survey", "we present an overview", "state-of-the-art review", "systematic mapping", "we systematically review") + 4 review subtitles added during title refinement (`research agenda`, `state-of-the-art, challenges`, `concepts, technologies, and future`, `fundamentals, solutions, and challenges`) |
| 3 | `rl` | Exclude | inherited + LLM-presence override (RL+LLM hybrids escape Exclude) |
| 4 | `llm_as_workload` | Exclude | inherited + abstract-specific workload phrases + abstract-specific tool-context overrides |
| 5 | **`classical_agents`** | **Exclude** | **NEW**. Broad-trigger (any MAS/agent term or classical marker), suppressed by LLM signal |
| 6 | **`mas_llm_based`** | **Include** | **NEW**. AND-condition: MAS term + LLM signal |
| 7 | **`agent_llm_based`** | **Include** | **NEW**. AND-condition: agent term + LLM signal |
| 8 | `llm_agentic_ai_generic` | Include | inherited from title (Cat 7) — catches LLM signal alone (no MAS/agent context) |
| (default) | `no_signal` | tiebreaker | When no category fires, the LLM tiebreaker decides |

---

## 4. Distribution after dry run

572 input papers, classifier output (before user manual review):

| Category | Decision | Count |
|---|---|---:|
| `classical_agents` | Exclude | 193 |
| `llm_agentic_ai_generic` | Include | 187 |
| `rl` | Exclude | 68 |
| `agent_llm_based` | Include | 40 |
| `mas_llm_based` | Include | 37 |
| `llm_as_workload` | Exclude | 31 |
| `review` | Exclude | 13 |
| `out_of_scope` | Exclude | 2 |
| `no_signal` | tiebreaker | 1 |
| **TOTAL Exclude** | | **308** |
| **TOTAL Include** | | **264** |

Tiebreaker decision: `paper-034` (Elastic & Load-Spike Proof One-to-Many Negotiation for SaaS, 2017) → **Exclude** (high confidence). Justification: classical pre-LLM negotiation mechanism without any LLM, foundation-model, or modern agentic-AI signal.

---

## 5. Decision principles codified for stage 05

### 5.1 Doctrine: when in doubt, include — REVISED

At title stage the doctrine was applied with high tolerance because titles are short and ambiguous. At abstract stage, the doctrine is **applied more strictly to MAS/agent papers without LLM signal**. Rationale:

- Abstracts are 200–400 words and almost always disclose the method.
- A paper that genuinely uses LLM but never says "LLM", "agent", "GPT", "language model", "foundation model", "agentic", "generative AI", "transformer", or any of the 30+ LLM-family terms in 200–400 words is vanishingly rare.
- Including all 195 MAS/agent-without-LLM papers would lose precision for marginal recall gain (~10 papers maybe lost vs ~185 needlessly Included for full-text review).

**Operationalization**: `mas` and `agent` standalone soft-Includes from title stage are dropped. Default for MAS/agent without LLM signal is Exclude (`classical_agents` category).

### 5.2 RL exclusion rule — UNCHANGED

> "Não quero incluir RL a não ser que LLM esteja sendo usado para melhorar o RL ou o contrário."

Implementation: Cat 3 fires on pure RL signals (MADRL, MASAC, multi-agent + DRL, etc.) but is **suppressed by an LLM-presence override**. RL+LLM hybrid papers (e.g., "LLM-Guided DRL", "Generative AI-aided RL", "GRACE: Strategic LLM-Enhanced Graph RL") escape Cat 3 and are Included via Cat 6, 7, or 8.

### 5.3 LLM-as-workload exclusion rule — STRENGTHENED

> "Se o artigo só fala de LLM/Agentic AI como workload, sem usar LLM/Agentic AI para gerenciar recursos, ele não é relevante."

Implementation: Cat 4 expanded with abstract-specific triggers ("we propose a system to serve LLMs", "LLM inference engine", "for efficient LLM serving") and abstract-specific overrides that protect LLM-as-decision-maker abstracts ("agentic workflow", "LLM decides/selects/orchestrates", "using LLMs to decide"). The bare RM-verb overrides (`routing`, `resource allocation`, `load balancing`, etc.) remain absent — they were removed during stage-04 refinement (see title doc §6.4) and not reintroduced.

### 5.4 Out-of-scope handling — UNCHANGED

Same patterns as title stage. The user's directive ("Concordo que adicionar padrões específicos para cada sub-domínio pode poluir o classificador") still holds. Sub-domain papers (smart grid, biomedical, supply chain, etc.) that survived title-stage Inclusion will appear in stage 05 as `llm_agentic_ai_generic` Include or as `classical_agents` Exclude depending on whether their abstract has an LLM signal. The user resolves these manually in the spreadsheet review.

### 5.5 Tiebreaker LLM — Sonnet 4.6 (Medium effort) via Agent tool

- Invoked when `winning_category == "no_signal"` (no regex pattern matches).
- Receives: paper ID, title, year, full abstract, plus the inclusion criteria (boundary A — agentic AI required; boundary B — RM as the closed loop; boundary C — cloud/edge/fog/continuum scope) and the exclusion list (RL pure, LLM-as-workload, classical MAS, surveys, out-of-scope).
- Returns: `{"decision": "Include" | "Exclude", "justification": "<PT-BR>", "confidence": "high|medium|low"}`.
- Result is annotated in `My Justification` column with prefix `[Tiebreaker LLM, conf=<X>]`.

---

## 6. What to look for during manual review

Numbered guidance based on the categories' likely error rates.

### 6.1 Top of red block — `classical_agents` (193 papers)

This is the spot-check group. Skim title + bold-highlighted evidence. **Flip to Include only if** the abstract clearly indicates LLM/foundation-model/agentic-AI usage that the regex missed. Likely causes for missed signals:
- Typos ("Genrative AI" instead of "Generative AI")
- Unusual term combinations not yet in the LLM signal regex
- Acronyms specific to a 2024–2025 model not yet listed (e.g., a new GPT variant)

If you find a paper with clear LLM signal that the classifier missed, the pattern should be added to the abstract config's LLM_SIGNAL_REGEX (in `scripts/build_abstract_config.py`) for future runs.

### 6.2 `rl` (68 papers)

Should be near-100% correct (RL+LLM hybrids escape via override). Skim quickly. If you find a paper that's actually RL+LLM but the classifier called it pure RL, the LLM signal is probably weakly worded — flag for review.

### 6.3 `llm_as_workload` (31 papers)

Watch for the LLM-as-tool / LLM-as-workload boundary. Some borderline cases from stage 04 reappear here:
- paper-2041 (LLM Native Networks) — kept Include at stage 04, now classifier says Exclude (workload-leaning). Your call.
- paper-1629 (Prompt Routing using BERT) — kept Include at stage 04. Check whether the classifier here agrees.

### 6.4 `review` (13) and `out_of_scope` (2)

Should be near-100% correct. Quick verification only.

### 6.5 Top of green block — `mas_llm_based` (37) and `agent_llm_based` (40)

High-confidence Includes. Skim to confirm both signals (MAS or agent + LLM) are genuine. False positives here would be papers that mention "LLM" peripherally in related work but the contribution is classical — rare in abstracts.

### 6.6 `llm_agentic_ai_generic` (187 papers)

Largest Include category. LLM signal alone, no MAS/agent context. Most likely error mode: paper is about LLM-as-workload but the classifier missed the workload trigger because the abstract uses non-standard phrasing. Skim and flip to Exclude if the contribution is clearly serving/deploying/training/fine-tuning LLMs as the workload.

Some papers in this group will be **out-of-scope domains** (smart grid, supply chain, healthcare) where LLM is being applied — the user explicitly chose at stage 04 not to encode sub-domain Excludes, so these stay in the corpus and resolve here. If any feels too far out of scope (e.g., clearly biomedical), flip to Exclude.

### 6.7 `no_signal` → tiebreaker (1 paper)

paper-034 was decided as Exclude by the tiebreaker (high confidence). If you disagree, flip to Include.

---

## 7. After your review

1. Save `spreadsheet_abstract_screening.xlsx`.
2. Reply `pronto` / `done` / `confirmo`.
3. I will then:
   a. Persist your decisions (My Final Decision / My Justification) into `screening["05-abstract-screening"]["human_decision"]` and `["human_justification"]` in each `papers/paper-NNN.md`.
   b. Update `status["05-abstract-screening"]` with the lowercase decision.
   c. Run the post-commit regenerator (which will rebuild `spreadsheet.xlsx` reading the now-populated paper files — preserving your decisions in the main file).
   d. Commit `[05] lock: <count> include / <count> exclude` and update `locks.05-abstract-screening: locked` in `CLAUDE.md`.

---

## 8. Open questions for stage 06

Not for now, but to anticipate:

1. **Full-text classifier config**: needs another elicitation pass. The categories will be similar (out_of_scope, review, rl, llm_as_workload, classical_agents, mas_llm_based, agent_llm_based, llm_generic) but patterns will scan section names, methodology phrases, and evaluation context.
2. **QA criteria (C18, C19)** at full-text stage: regex doesn't cover "described with sufficient detail" (C18) or "evaluation presented" (C19). Likely requires an LLM pass for QA scoring per paper, separate from the regex classifier for thematic_sub_rq.
3. **PDF availability**: stage 06 requires every Include from stage 05 to have its PDF in `raw/pdfs/paper-NNN.pdf`. The user will need to download these manually before stage 06 can run.
