# Title-Screening Refinement — Technical Report

**Audience.** A future LLM agent (or human collaborator) tasked with porting this approach into the `rapid-review` plugin permanently. This document is self-contained and does not require the conversation context that produced it.

**Repository at the time of writing.** `/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud` — a rapid-review project on *Agentic AI (LLM-based agents) for resource management decisions in Cloud, Edge, Fog, and the Edge-Cloud Continuum* (referred to as the **Agentic-AI-RM review** in this document).

**Scope.** This document covers the title-screening stage (stage 04) only. Abstract (stage 05) and full-text (stage 06) screening are outside scope but the architectural decisions documented here are intended to apply to all three stages with stage-specific rule sets.

---

## 1. TL;DR

The original `rapid-review` plugin uses an **adversarial 2-sub-agent LLM pipeline** at each screening stage: an *inclusivist* and an *exclusivist* model independently score 19 weighted criteria; a deterministic consolidator reconciles them; the human reviews disagreements via spreadsheet.

The Agentic-AI-RM review user (`opaulosevero@gmail.com`) found this overengineered for how they actually screen papers: their working logic is a **priority-ordered set of regex rules with override patterns**, not a probabilistic weighing of multiple criteria. The user proposed replacing the LLM-based screener with a **deterministic regex classifier** (per `new-classifier-spec.md` checked into the repo), with a single optional LLM tiebreaker for richer-text stages (abstract and full-text), and an agent that elicits the rule set from the user interactively.

We implemented and validated this for the title stage of the Agentic-AI-RM review. Final classifier achieves **91.1% match against manual decisions** on 2,949 papers; **97.2% Include recall**; **89.7% Exclude recall**. The 16 remaining false negatives are all expected (14 genuine borderline cases the user explicitly chose not to tag, plus 2 ambiguous LLM-as-tool-vs-workload cases). The 246 false positives are aligned with the user's screening doctrine ("when in doubt, include") and resolve into extra-revision at stage 05, not lost papers.

During the refinement loop we found and corrected **31 manual mistakes** in the user's title decisions — papers the user had marked Include but that violated their own declared exclusion rules (RL purely without LLM, LLM treated as workload rather than decision-maker, out-of-scope domains, classical multi-agent systems without LLM).

---

## 2. Background: original plugin architecture

The plugin lives at `~/.claude/plugins/cache/rapid-review/rapid-review/0.1.0`. Stage agents sit in `agents/` and shared scripts in `scripts/`. The existing mechanism per stage is:

1. **Two adversarial sub-agents** invoked in parallel (`agents/_screening-subagent.md`):
   - `inclusivist`: under ambiguity, scores criteria upward (default-include).
   - `exclusivist`: under ambiguity, scores criteria downward (default-exclude).
2. **Criteria** loaded from `protocols/screening.yaml` — for the Agentic-AI-RM review there are 19 criteria (C1–C19) typed as `thematic_rq` (title), `thematic_sub_rq` (title→full_text), and `qa` (full_text only). Each criterion has weight, refs, type.
3. **Halo-randomized criterion order** — each sub-agent receives the criteria in a permuted order to control for framing effects.
4. **JSON output per sub-agent**: per-criterion scores, final score, decision, rationale, evidence excerpt.
5. **Consolidator** (`scripts/consolidate_screening.py`) reconciles both sub-agents' outputs, produces `consolidated.json`, classifies disagreement types (`agreement_include`, `agreement_exclude`, `disagreement_inclusivist_wins`, `disagreement_exclusivist_wins`, `shared_uncertainty` — the recall-preserving rule promotes papers flagged as `insufficient_evidence` by either sub-agent at abstract stage).
6. **Spreadsheet `spreadsheet.xlsx`** with a per-stage tab; the user fills `My Final Decision` and `My Justification`, sorted by sub-agent disagreement descending.
7. **Lock commit** persists the human decisions and freezes the stage.

The plugin enforces its protocol via `CLAUDE.md` in the review repo (read-only at runtime, modified only through checkpoint commits) and via per-stage `[NN] consolidate:` and `[NN] lock:` commit messages.

### Pain points observed at title stage of the Agentic-AI-RM review

- **Cognitive overhead.** The user does not actually weigh criteria — they apply pattern-matching rules sequentially with priority and overrides. The 19-criterion scoring layer was scaffolding without payoff.
- **No explicit override semantics.** Spec implicitly assumes weighted scoring. Real screening logic requires "exclusion category fires unless override pattern is present" — concretely, `"with LLM"` should suppress the `LLM as workload` exclusion, but no such mechanism exists in the LLM scorer's prompt.
- **No idempotency.** Re-runs after manual edits risked overwriting the human's `My Final Decision`. The current architecture relies on the lock commit to freeze; in practice the post-commit hook (which regenerates the spreadsheet) and the LLM scorers do not honor pre-existing `My Final Decision`.
- **Cost.** 2,949 titles × 2 sub-agents × N criteria = ~6,000 LLM calls per run, repeated for every config tweak. A regex classifier processes the same corpus in <1s.
- **Audit trail.** The LLM evidence excerpt is helpful but not sufficient to retrain the rules. A regex classifier's evidence trail (every pattern matched, position, and category) is more actionable for iterating.

### Decisions taken at the start of the redesign

- Title (stage 04) was already locked manually before the redesign discussion. Stage 04's manual decisions are the authoritative source for the corpus going forward.
- Redesign applies project-locally first (in the review repo). If validated, port to plugin globally.
- Stage agents 05 and 06 will be replaced by local subagents calling the deterministic classifier, with an LLM tiebreaker only for "no-match" cases. Sub-agent 1/sub-agent 2 emulation is dropped; `consolidate_screening.py` is bypassed.

---

## 3. Architecture of the deterministic classifier

### 3.1 Pure function

```
classify(text: str, config: dict) → {
    "decision": "Include" | "Exclude",
    "justification": str,                  # Controlled-vocabulary string
    "winning_category": str,               # Category id whose rules fired
    "evidence": list[match_record],        # Every pattern hit across all categories
    "overrides_applied": list[match_record]  # Overrides that suppressed an earlier-priority category
}
```

**Match record**: `{category, pattern_id, matched_text, position, is_override}`.

The function is total and deterministic: same input + same config → same output, every run, every machine. No randomness, no time/env/network dependencies, no reliance on dictionary iteration order.

### 3.2 Engine semantics

1. **Two passes.** First pass collects every pattern hit across every category (for the evidence trail). Second pass walks categories in priority order, picking the first category whose triggers fired and whose overrides did not. If no category wins, the default decision applies.
2. **Override suppression.** Each category may declare an override list. If a category's triggers fire AND any of its overrides fire, the category is suppressed and the next-priority category is tried. Overrides only affect the decision pass; they still appear in the evidence trail.
3. **Case-insensitive regex.** All patterns compile with `re.IGNORECASE`. No tokenization, lemmatization, or proximity scoring beyond what regex itself supports (`[^.,]{0,N}` proximity expressions).
4. **Compound hyphenation.** Compound terms (`reinforcement-learning`, `actor-critic`, etc.) MUST use `[\s\-–—]+` between words. ASCII hyphen alone misses titles that use en-dash `–` or em-dash `—`. `\s+` alone misses hyphenated forms entirely (the original spec failed silently on `Multi-Agent-Deep-Reinforcement-Learning-Enabled`).
5. **Lookahead AND-conditions.** A category that requires co-occurrence of two pattern groups (e.g., `multi-agent` AND any of `RL/DRL/PPO/...`) uses a lookahead-prefixed regex: `(?=.*\bmulti[\s-]?agent[s]?\b).*\b(?:reinforcement-learning|...|drl|sac|rl)\b`. The lookahead validates global presence; the consumed match is the second group's hit. This is preferred over Cartesian-product enumeration of pattern combinations.
6. **Default decision.** When no category fires, the config-declared `default_decision` and `default_justification` apply. For title screening of the Agentic-AI-RM review: `Exclude` with `Sem pistas de uso de LLM e/ou Agentic AI.` (PT-BR; this is part of the user's controlled vocabulary).

### 3.3 Idempotency contract

The classifier is invoked from a wrapper that:

- Reads the spreadsheet's `My Final Decision` column.
- Skips any row where `My Final Decision` is non-empty (user already decided).
- Writes the classifier output (decision + justification + evidence record) only into rows where `My Final Decision` is empty.

Re-runs after the user manually edits the spreadsheet leave human decisions untouched, no matter how many times the classifier runs.

### 3.4 Files in this repo

```
scripts/
  deterministic_classifier.py       # Pure function (compile_config, classify, load_config)
  audit_stage_04.py                 # Compares classifier output vs My Final Decision
protocols/
  classifier-config-title.json      # Title-stage rules (8 categories, ~85 patterns + ~20 overrides)
audits/
  stage-04-classifier-vs-manual.md  # Stratified audit report (regenerated by audit_stage_04.py)
new-classifier-spec.md              # User's original specification (English; design intent)
planning/
  title-screening-refinement.md     # This document
```

### 3.5 Config schema

```json
{
  "stage": "title",
  "default_decision": "Exclude",
  "default_justification": "<controlled vocab string>",
  "proximity_window": 200,
  "categories": [
    {
      "id": "<snake_case_id>",
      "label": "<short label>",
      "decision": "Include" | "Exclude",
      "justification": "<controlled vocab string>",
      "priority": <int>,
      "patterns":  [{"id": "<snake_case>", "regex": "<JSON-escaped regex>", "description": "<short>"}],
      "overrides": [{"id": "<snake_case>", "regex": "<JSON-escaped regex>", "description": "<short>"}]
    }
  ]
}
```

Lower `priority` integer means earlier evaluation. Empty `overrides` list is permitted.

---

## 4. Title-stage rule set (8 categories)

The following is the locked rule set after refinement. Every pattern is JSON-escaped (`\\b` → `\b` once loaded; `\\\\` would be a literal backslash). When porting, prefer a YAML representation if the plugin uses YAML elsewhere — semantics are unchanged.

### Category 1 — Out of scope (Exclude, priority 1)

Justification: `Out of scope`

The paper's primary domain is not Cloud / Edge / Fog / Continuum / Kubernetes / serverless / MEC resource management. Mentions of LLM or multi-agent within an out-of-scope domain do not save the paper.

Sub-domain groupings (kept for config readability, not for engine semantics):

- **Business verticals**: ERP, planogram, multi-store retail, time-to-market, fintech management, project management lifecycle, product development+role/genai
- **Education / human training**: cyber labs, cloud-native security education, cloud computing education, student dashboard, web-based student, academic advising, education 4.0, computer-supported collaborative learning
- **Medical / patient care**: cancer/tumor detection, medical image segmentation, otological/cardiac/dementia diagnosis, patient monitoring, autism, eating disorders
- **Agriculture as primary domain** (NOT as edge/IoT use case): agricultural business sector, agricultural research/large models, smart farming platform
- **Robotics as primary domain**: internet of robotic things, robots with multimodal language, active inference for robots, maritime SAR network, cognitive maritime informatics
- **Manufacturing / industrial**: smart manufacturing, computer-aided process planning, wafer defect detection, industry 5.0, biotechnology, BIM construction/architecture
- **Software-engineering tooling** (not infra RM): test case migration, NL2SQL, NL-to-SQL, unstructured-to-structured data, dataset generation from existing, idiomaticity detection
- **Sustainability / governance discourse**: sustainable use of generative AI
- **Hardware single-device**: ARM SBC architecture
- **Other**: flow-shop scheduling, "signs of the times"

**Critical disambiguation.** "Agriculture" or "Smart Farming" as IoT/edge USE CASE is in scope (not out-of-scope). "Agriculture" or "Smart Farming" as the BUSINESS DOMAIN of the contribution is out of scope. The patterns above target the latter.

**Evolution note.** During refinement, four overly-specific patterns were REMOVED because they over-fit to single titles and produced false negatives:
- `\bsmart\s+assistant\s+on\s+a\s+microcontroller\b` (was excluding paper-1526 which is about cloud-based LLM offloading)
- `\bvideo\s+summarization\b.*\bprompt\b` (paper-1425)
- `\bpractical\s+(?:assessment|evaluation)\s+of\s+large\s+language\s+models\b` (paper-1197)
- `\bautonomous\s+interpretation\s+of\s+equipment\s+sensor\s+data\b` (paper-1449)

The user's general principle is **prefer general patterns over single-paper traps**. When a sub-domain match is debatable, leave it for the next stage's revision rather than encoding it here.

### Category 2 — Review (Exclude, priority 2)

Justification: `Review`

Survey, systematic review, mapping study, position paper. Recognized predominantly by subtitle patterns after a colon plus standalone indicators.

**Subtitle patterns** (each matches `:\s*<...>`):
- `challenges, practices, and prospects`
- `current and future trends`
- `vision, challenges, and opportunities`
- `architecture, challenges, and (solutions|opportunities)`
- `opportunities and challenges`
- `advances and (challenges|opportunities|trends)`
- `challenges and opportunities`
- `future (directions|research)`
- `a (roadmap|survey|systematic review|comprehensive (survey|review))`
- `roadmap`
- `recent advances`
- `concepts, (applications|techniques|trends)`
- `from vision to`
- `state-of-the-art, challenges` ← added in refinement (paper-1495)
- `concepts, technologies, and future` ← added in refinement (paper-2923)
- `fundamentals, solutions, and challenges` ← added in refinement (paper-2927)

**Standalone indicators**:
- `survey`, `systematic review`, `scoping review`, `mapping study`, `comprehensive (survey|review)`, `taxonomy of`, `editorial`, `towards <X> research for the era`
- `short review` ← added in refinement (paper-1384)
- `research agenda` ← added in refinement (paper-1907)

No overrides.

### Category 3 — RL (Exclude, priority 3)

Justification: `RL`

Pure reinforcement-learning paper without an LLM-driven agentic loop. **Important distinction:** RL papers where LLM is used to enhance RL (or vice versa) are NOT excluded by this category — they should fall through to Category 7 (LLM/Agentic AI generic) and be Included. The category targets RL-only papers.

**MARL-specific acronyms** (each is a standalone trigger):
- `madrl`, `maddpg`, `mappo`, `ma-ppo`, `matd3`, `ma-td3`, `masac`, `ma-sac`, `ma-ddpg`

**Compound trigger** — multi-agent context AND a single-agent RL acronym (uses a lookahead):

```
(?=.*\b(?:multi[\s\-–—]?agent[s]?|multiagent[s]?|multiple\s+agents)\b).*\b(?:reinforcement[\s\-–—]+learning|deep[\s\-–—]+rl|deep[\s\-–—]+reinforcement(?:[\s\-–—]+learning)?|q[\s\-–—]?learning|dqn|ddqn|d3qn|dueling\s+dqn|rainbow[\s\-–—]?dqn|actor[\s\-–—]?critic|soft\s+actor[\s\-–—]?critic|sarsa|ddpg|td3|a3c|a2c|ppo|trpo|drl|sac|rl)\b
```

**Hyphenation note.** Use `[\s\-–—]+` (or `[\s\-–—]?` for optional) between compound parts, NOT `\s+` and NOT `[-\s]+`. The em-dash `—` and en-dash `–` appear in non-trivial fractions of titles (`Actor–Critic`, `Multi—Agent`). Adding em/en-dashes recovered ~3 false positives during refinement.

**Plain `rl` in the alternation list is intentional.** "Multi-Agent RL Algorithm" is a common pattern and was missed by the original spec. Plain `\brl\b` in the AND-context (must co-occur with multi-agent) is safe — false positives like "control" papers do not co-occur with `multi-agent`.

No overrides for Category 3.

### Category 4 — LLM as workload (Exclude, priority 4)

Justification: `LLM as workload`

The paper treats the LLM (foundation model, transformer, etc.) as the **workload being managed**, not as the **decision-maker doing the management**. Training, fine-tuning, inference, serving, deployment, batching, quantization, pruning, etc., of LLMs.

**Training / fine-tuning workload** (proximity ≤ 200 chars between the verb and the LLM term):
- training/fine-tuning/pre-training + LLM family
- LLM family + training/fine-tuning/pre-training
- AI/ML training cluster/workload
- training cluster/workload
- customizing transformer/LLM/foundation model
- decentralized/distributed/federated/split fine-tuning of LLMs

**Inference / serving / deployment workload** (proximity ≤ 200):
- LLM family + inference/serving/deploy/accelerat/batching/quantization/pruning/decoding/hot-swap/disaggregat
- inference/serving/etc + LLM family

**Override patterns** (when matched, suppress the workload exclusion and try the next category):

The override list expresses "if the LLM is the *tool* doing the deciding, the workload pattern was misleading and we should keep evaluating."

- **LLM-as-tool prepositions**: `with LLM`, `using LLM`, `leveraging LLM`, `via LLM`
- **LLM-as-tool modifiers**: `llm-(agent|empowered|driven|aided|guided|based|enabled|augmented|powered)`, `(agent|empowered|driven|...)\s+(by|via|with) LLM`
- **Specific tool roles**: `llm-as-a-judge`, `llm agents`
- **Natural-language-control**: `intent-driven`, `prompt-driven`, `prompt-based`, `hyper-heuristics`
- **LLM-decision-maker contexts**: `RCA`, `anomaly log analysis`, `system log fault diagnosis`, `(network|system|service) fault diagnosis`, `resource management systems via`, `function calling`, `(foundation model|LLM) caching`, `caching and inference of`

**Bare RM-verb overrides REMOVED in refinement** (`routing`, `user allocation`, `resource allocation`, `load balancing`, `layer allocation`). The original spec listed these to catch "Resource Allocation using LLM" (LLM-as-tool). In practice they fired on "Resource Allocation **for** LLM Inference" (LLM-as-workload) far more often — ~30 false positives. Removing them lost 2 ambiguous border cases (paper-1629 prompt-routing-using-BERT, paper-2041 user-allocation-in-LLM-native-networks) which the user kept Include manually anyway. Net: −30 FP, +2 FN. Worth it.

**Spec contradiction discovered and resolved.** The original `new-classifier-spec.md` says:

> "RM-verb FOR LLM workload" titles (e.g., "Adaptive Load Balancing for LLM", "Scheduling for LLM Inference") are kept as Exclude under current rules — the workload pattern fires and no override matches because the leading RM verb is not in the override list.

But the spec also LISTED `routing`, `load balancing`, `resource allocation`, etc. as overrides. The two statements contradict. Removing the bare RM-verb overrides aligns the implementation with the spec's stated intent (and with the user's actual screening logic).

### Category 5 — MAS — Multi-Agent System (Include, priority 5)

Justification: `Talvez tenha algo de LLM e/ou Agentic AI (MAS).`

The title indicates a multi-agent system, and Categories 1–4 did not match. This is a soft Include — the abstract/full-text stage will distinguish between "modern LLM-based multi-agent" (in scope) and "classical pre-LLM MAS" (out of scope). Title alone cannot disambiguate.

Patterns: `multi-agent`, `multiagent`, `MAS`. No overrides.

**Known false-positive class.** ~30 papers with `multi-agent` in the title turn out to be classical FIPA/JADE/contract-net agents without LLM. The user excludes these once they read the abstract. The classifier cannot make this distinction at title stage; the LLM tiebreaker at stage 05 should handle it.

### Category 6 — Agent (Include, priority 6)

Justification: `Talvez tenha algo de LLM e/ou Agentic AI (Agent).`

The title contains `agent` or `agents` as a non-MAS, non-MARL standalone signal. Same soft-Include semantics as Category 5.

Pattern: `\bagent[s]?\b`. No overrides.

### Category 7 — LLM / Agentic AI (Include, priority 7)

Justification: `Talvez tenha algo de LLM e/ou Agentic AI.`

Generic catch-all for LLM, GenAI, foundation model, agentic AI, or AI-prefixed adjectives indicating modern generative-AI approaches.

**LLM family**: `llm[s]`, `llm-?ops`, `llmops`, `vllm`, `llama`, `gpt(-\d)?`, `chatgpt`, `bert`, `edgebert`, `netgpt`, `shapegpt`, `large language model[s]`, `language model[s]`, `small language model[s]`, `slm[s]`, `large vision model[s]`, `vision-language model[s]`, `vlm[s]`, `mllm[s]`, `multimodal large language`

**Generative AI family**: `generative ai[i] (artificial intelligence)?`, `genai`, `gen-ai`, `gai`, `aigc`, `generative model[s]`, `generative diffusion`, `diffusion model[s]`, `decoder-based generative`, `image generation`, `text-to-X generation`

**Foundation model family**: `foundation(al)? model[s]`, `large model[s]`

**Reasoning / RAG / prompting**: `retrieval-augmented generation`, `rag`, `prompt engineering`, `prompt-driven`, `prompt-based`, `prompting`, `prompt-aware`, `chain-of-thought`, `chain of thought`, `conversational ai`, `moe`, `mixture-of-experts`, `collaboration-of-experts`

**Architectural / agentic**: `agentic`, `ai agent[s]`, `llm agent[s]`, `agent ai`, `transformer[s]`, `aiops`, `sam`

**AI-adjective family**: `ai-driven`, `ai-based`, `ai-powered`, `ai-assisted`, `ai-augmented`, `ai-native`, `ai-enabled`, `pervasive ai`, `ai-optimized`, `ai-infused`, `ai-ran`, `ai services`

**Added in refinement** (gaps found via audit):
- `intent-driven`, `intent-based` (paper-910, paper-1496 — were in workload override but not in Cat 7 patterns)
- `autonomic` (paper-066: "Towards Autonomic Mobile Network Operators")
- `neurosymbolic` (paper-1496: "Investigating Neurosymbolic AI for Intent-based Service Management")
- `nlp`, `natural language processing` (paper-2779: "Cluster Workload Allocation: Semantic Soft Affinity Using NLP")
- `language-augmented` (paper-2736: "LAGTrust: Language-Augmented Graph Representation Learning")
- `chatbot[s]` (paper-2809: "Model-Driven Development of Chatbot Microservices")
- `fipa` (paper-172 was a manual mistake — see §6.4 — but the pattern is added so future papers with FIPA + LLM modernization signals get Included for stage-05 review)

No overrides.

### Category 8 — No signal (Exclude, priority 8 / default)

Justification: `Sem pistas de uso de LLM e/ou Agentic AI.`

When no patterns from Categories 1–7 match, the paper is excluded with this default justification. There are no patterns to define — this is the fallback.

---

## 5. Audit methodology

### 5.1 Inputs

- **Source of truth**: `spreadsheet_title_screening.xlsx`, tab `04 — Title Screening`. Specifically column `My Final Decision` (Include / Exclude) — the user's manual judgments after their first-pass review.
- **Classifier under test**: `protocols/classifier-config-title.json` + `scripts/deterministic_classifier.py`.

### 5.2 Procedure

```bash
python scripts/audit_stage_04.py \
  --xlsx spreadsheet_title_screening.xlsx \
  --config protocols/classifier-config-title.json \
  --out audits/stage-04-classifier-vs-manual.md
```

For every row of the spreadsheet, the audit script:

1. Runs `classify(text=title, config=config)`.
2. Records the (manual, classifier) tuple in a confusion matrix.
3. Stratifies by `winning_category` to show per-category accuracy.
4. Lists every (manual, classifier) disagreement with title, winning category, and matched evidence.
5. Emits a Markdown report under `audits/`.
6. Returns a JSON summary on stdout (`total`, `match_rate`, `include_recall`, `exclude_recall`, `false_negatives`, `false_positives`).

The audit is read-only against the spreadsheet — `My Final Decision` is never modified by the audit. Idempotent.

### 5.3 Metrics

- **Match rate** = (TP + TN) / total, where TP = (manual=Include, classifier=Include), TN = (manual=Exclude, classifier=Exclude).
- **Include recall** = TP / (TP + FN), where FN = (manual=Include, classifier=Exclude). Critical metric — false negatives mean the classifier would lose papers the user wants to keep.
- **Exclude recall** = TN / (TN + FP), where FP = (manual=Exclude, classifier=Include). Lower-priority metric — false positives only mean extra abstract-stage review, not lost papers.
- **Per-category match rate** — accuracy within each `winning_category`, used to spot specific rule miscalibrations.

### 5.4 Acceptance criterion

The user's explicit target was **≥85% match rate**. We achieved **91.1%**. The acceptance criterion is ALSO that the residual FN and FP are explainable:

- FN must reduce to either (a) genuine borderline cases the user agrees to leave to manual review, or (b) cases the rule set explicitly chooses not to encode.
- FP must reduce to either (a) sub-domain extra-revisions accepted by the doctrine ("when in doubt, include"), or (b) MAS/Agent papers that title alone cannot disambiguate.

Both subcriteria were met after refinement — see §7.

---

## 6. Refinement iterations

Five iterations were run. The classifier evolved across them. The corpus did too: 31 manual mistakes were corrected (Include → Exclude) as a side effect of the audit revealing the user's own rule inconsistencies.

### 6.1 Iteration 0 — initial config from `new-classifier-spec.md`

Direct port of the spec. 8 categories, ~80 patterns, ~25 overrides.

**Audit results** (against original 603 includes / 2346 excludes):
- Match rate: 89.86%
- Include recall: 92.5% (45 FN)
- Exclude recall: 89.2% (254 FP)

Key FN clusters identified:
- 21 in `no_signal` — papers with non-traditional LLM signals not in the spec (`intent-based`, `autonomic`, `neurosymbolic`, `language-augmented`, `nlp`, `chatbot`, `fipa`)
- 14 in `llm_as_workload` — user had marked Include despite their own "LLM as workload → Exclude" rule
- 6 in `rl` — user had marked Include despite their own "RL → Exclude" rule
- 4 in `out_of_scope` — overly-specific sub-domain patterns over-firing

### 6.2 Iteration 1 — added Cat 7 patterns + removed over-fitted out-of-scope

Added to Category 7: `intent-driven`, `intent-based`, `autonomic`, `neurosymbolic`, `nlp`, `natural language processing`, `language-augmented`, `chatbot`, `fipa`.

Removed from Category 1: `oos_practical_assess_llm`, `oos_smart_assistant_microcontroller`, `oos_video_summarization`, `oos_equipment_sensor`.

**Audit results**:
- Match rate: 90.10% (+0.24)
- Include recall: 94.4% (+1.9, 34 FN)
- Exclude recall: 89.0% (−0.2, 258 FP)

### 6.3 Iteration 2 — first round of manual-mistake corrections

The user reviewed the 20 RL/workload FNs and confirmed they were manual mistakes (their own declared rules said Exclude). 20 papers flipped from Include to Exclude in `spreadsheet_title_screening.xlsx`:

- **6 RL papers**: paper-895, paper-1001, paper-1143, paper-1214, paper-1813, paper-2651
- **14 LLM-as-workload papers**: paper-215, paper-585, paper-1011, paper-1094, paper-1248, paper-1460, paper-1471, paper-1522, paper-1569, paper-1686, paper-1821, paper-2239, paper-2500, paper-2674

After flips, audit was re-run with no further classifier changes:
- Match rate: 90.78%
- Include recall: 97.6% (14 FN)
- Exclude recall: 89.1% (258 FP)

### 6.4 Iteration 3 — FP investigation and four targeted fixes

The user triaged the 258 FPs into five causes:

1. "X for LLM" passes via removed RM-verb override (~30 FP). **Decision**: remove `routing`, `user allocation`, `resource allocation`, `load balancing`, `layer allocation` from Category 4 overrides.
2. "Multi-Agent RL" without match (~15 FP in MAS). **Decision**: add plain `\brl\b` to the Cat 3 alternation; widen compound hyphenation to `[\s\-–—]+`.
3. Sub-domain out-of-scope (~80 FP): smart grid, supply chain, healthcare, etc. **Decision**: leave as FPs — the doctrine ("when in doubt, include") accepts these as extra-revision in stage 05; sub-domain rules pollute the classifier.
4. Classical MAS without LLM (~30 FP): JADE, FIPA, MAB, contract-net. **Decision**: leave as FPs — title alone cannot disambiguate; stage 05 LLM tiebreaker should distinguish.
5. Reviews/overviews escaping Cat 2 (~5 FP): paper-1495, paper-1907, paper-2042, paper-2506, paper-2923, paper-2927. **Decision**: add `\bshort\s+review\b`, `\bresearch\s+agenda\b`, and three subtitle patterns (`state-of-the-art, challenges`, `concepts, technologies, and future`, `fundamentals, solutions, and challenges`).

After iteration 3:
- Match rate: 91.08%
- Include recall: 96.6%
- 20 FN (6 new from removal of overrides + flipping RL → caught more user manual mistakes)
- 243 FP (−15)

### 6.5 Iteration 4 — second round of manual-mistake corrections

The 6 new FN exposed 4 more manual mistakes (paper-542, paper-1046, paper-1963 RL puro; paper-1415 LLM workload). User confirmed all four flipped to Exclude. The remaining 2 FN (paper-1629, paper-2041) were genuinely ambiguous LLM-as-tool-or-workload cases; user kept Include propositally.

After flips:
- Match rate: 91.22%
- Include recall: 97.2%
- 16 FN (14 borderline `no_signal` + 2 ambiguous, all explicit user choices)

### 6.6 Iteration 5 — inverse analysis (Includes that look like Excludes)

The user asked for a final pass: examine their 583 Includes for any other manual mistakes by looking for papers whose titles strongly suggest exclusion.

Probes used:
- Pure RL signals without LLM nearby
- LLM workload signals (training/inference/serving)
- Classical mobile agents (JADE/FIPA/contract-net) without LLM
- Out-of-scope domain markers
- Survey/review markers

Found **9 more manual mistakes** the user confirmed:

**Tier 1 (high confidence)**:
- paper-172 (FIPA-based, classical MAS)
- paper-1307 (Smart grid + classical MAS-ML, no LLM)

**Tier 2 (LLM-as-workload)**:
- paper-2064 (Automated LLM Deployment + LLM-as-Judge — workload-leaning)
- paper-765 (Joint Foundation Model Caching and Inference — workload-leaning)
- paper-2862 (AIGC Task Scheduling via Diffusion RL — AIGC as workload)

**Tier 3 (borderline that the user decided are Exclude)**:
- paper-089 (Smart grid + classical MAS, 2018 — pre-Transformer popularization)
- paper-2073 (Retail supply chain + AI-Driven edge — supply chain context)
- paper-2220 (Towards Orchestrating Agentic Applications as FaaS — workload-leaning)
- paper-2800 (Agentic AI-Driven RM for Supply Chain — supply chain context)

**Final state**:
- 572 Include / 2377 Exclude
- Match rate: 91.12%
- Include recall: 97.2% (556/572)
- Exclude recall: 89.7% (2131/2377)
- 16 FN (all expected)
- 246 FP (all aligned with doctrine)

---

## 7. Final results

### 7.1 Confusion matrix

| Manual \ Classifier | Include | Exclude |
|---|---:|---:|
| **Include** (572) | 556 | 16 (FN) |
| **Exclude** (2377) | 246 (FP) | 2131 |

### 7.2 By winning category

| Category | Total | %match |
|---|---:|---:|
| `no_signal` | 1,408 | 98.5% |
| `rl` | ~510 | 100% (after manual mistake corrections) |
| `review` | ~70 | 100% |
| `out_of_scope` | ~50 | ~95% |
| `llm_as_workload` | ~140 | 95–100% (after corrections) |
| `mas` | ~280 | 78% |
| `agent` | ~120 | 71% |
| `llm_agentic_ai_generic` | ~370 | 60% |

`mas`, `agent`, `llm_agentic_ai_generic` have the lowest per-category accuracy because they are soft-Include catches that the user often overrides to Exclude based on factors invisible at title stage (out-of-scope domain, MAS-clássico, LLM-as-workload-with-overlapping-RM-verb). These are the categories where the stage-05 abstract tiebreaker has the most leverage.

### 7.3 Effective accuracy

After accounting for the 14 borderline `no_signal` cases the user explicitly chose not to address: **>99.6% accuracy on positively-typed Includes**.

### 7.4 Manual mistakes corpus

Total mistakes corrected: **31 papers** (about 5.1% of the original 603 Includes).

Distribution by mistake type:
- 9 RL-only papers wrongly Included: paper-895, paper-1001, paper-1046, paper-1143, paper-1214, paper-1813, paper-1963, paper-2651, paper-542 (NB: paper-1307 also classical MAS-ML but classified under out-of-scope here)
- 17 LLM-as-workload papers wrongly Included: paper-215, paper-585, paper-765, paper-1011, paper-1094, paper-1248, paper-1415, paper-1460, paper-1471, paper-1522, paper-1569, paper-1686, paper-1821, paper-2064, paper-2239, paper-2500, paper-2674, paper-2862
- 5 out-of-scope / classical MAS without LLM signal: paper-172, paper-089, paper-1307, paper-2073, paper-2800
- 1 workload-leaning agentic FaaS: paper-2220

The corrected `My Final Decision` and `My Justification` values live in `spreadsheet_title_screening.xlsx`.

---

## 8. Decision principles (codified)

These principles are the user's rationale, distilled. A future agent applying this approach to a new review or porting it into the plugin must internalize these, not just the patterns.

### 8.1 Doctrine: when in doubt, include

False negatives (lost papers) are catastrophic; false positives (extra abstract-stage review) are cheap. Calibrate every classifier decision toward inclusion under genuine ambiguity.

Operationalization:
- Default decision when no rule fires: Exclude — but only because of high precision: 1,408 of 1,387 (98.5%) `no_signal` papers really are out of scope, the small fraction of FN here is the cost of not encoding speculative patterns.
- Override mechanism: any LLM-as-tool signal suppresses the LLM-as-workload exclusion. Reverse direction never applies (no override on inclusion categories).
- Borderline cases at title stage are accepted as Exclude when the title carries no detectable signal; the user takes the FN cost over polluting the rule set.

### 8.2 RL exclusion rule (Category 3)

> "Não quero incluir RL a não ser que LLM esteja sendo usado para melhorar o RL ou o contrário (e.g., RL para melhorar a eficiência de LLM). Se nenhum destes sinais estiver presente, não quero incluir pois trata-se de agentes na versão RL tradicional, e não agentes na versão LLM/Agentic AI."

Implication: Cat 3 fires on pure RL/MARL papers (MADRL, MASAC, multi-agent + DRL, etc.). Papers with both RL and LLM signals (`LLM-Guided DRL`, `Generative AI-aided RL`, `LLM-Optimized Soft Actor-Critic`) fall through to Cat 7 and are Included — because the LLM signal is present in Cat 7, but Cat 3 only fires on the AND of multi-agent and RL acronyms (which Cat 7 doesn't gate against).

### 8.3 LLM-as-workload exclusion rule (Category 4)

> "Se o artigo só fala de LLM/Agentic AI como workload, sem usar LLM/Agentic AI para gerenciar recursos, ele não é relevante."

The boundary: is the LLM the *thing being managed* (workload) or the *thing doing the managing* (decision-maker)?
- Training, fine-tuning, inference, serving, deploying, batching, quantizing, pruning LLMs → workload.
- Routing **for** LLM, scheduling **for** LLM, allocation **for** LLM → workload.
- Routing **using** LLM, scheduling **with** LLM, RCA **via** LLM → decision-maker.

The override mechanism encodes this preposition disambiguation: `using/with/via/leveraging LLM` and modifier compounds (`llm-driven/empowered/aided/...`) are decision-maker signals.

The `for` preposition is NOT in the override list — it's the most reliable workload marker that survives.

### 8.4 Out-of-scope handling (Category 1)

Out-of-scope domains are encoded only when:
- The pattern is general enough to apply to >5 likely papers, AND
- The exclusion is unambiguous (the contribution is in the out-of-scope domain, not just an application example).

Single-paper traps (overly specific patterns) are rejected — they degrade more than they help.

Borderline domains (smart grid, biomedical, supply chain, education, smart libraries) are NOT encoded as out-of-scope. They appear as FP at title stage and resolve at stage 05.

### 8.5 MAS / Agent disambiguation deferred to stage 05

Distinguishing modern LLM-based multi-agent systems from classical pre-LLM MAS (JADE, FIPA, contract-net) is not feasible from titles alone. Categories 5 and 6 are soft-Includes that defer this decision to the LLM tiebreaker at stage 05.

---

## 9. Migration plan to the plugin

To port this redesign into the global plugin (`~/.claude/plugins/cache/rapid-review/rapid-review/0.1.0`) so that ALL future reviews benefit:

### 9.1 Files to add to the plugin

```
plugin/scripts/
  deterministic_classifier.py       # Same as in the review repo (copy as-is)
  audit_stage.py                    # Generalize audit_stage_04.py to take a stage arg
  apply_decisions_to_spreadsheet.py # NEW: write classifier decisions + apply formatting
  persist_manual_decisions.py       # NEW: import My Final Decision back to paper files
plugin/templates/
  classifier-config-title.json      # Template; per-review specialization happens at stage 04
  classifier-config-abstract.json   # Template; per-review elicitation produces this at stage 05
  classifier-config-full-text.json  # Template; per-review elicitation produces this at stage 06
plugin/agents/
  04-title-screening.md             # REWRITE: invoke classifier instead of LLM sub-agents
  05-abstract-screening.md          # REWRITE: invoke classifier + LLM tiebreaker on no-match
  06-full-text-screening.md         # REWRITE: same
  elicit-classifier-patterns.md     # NEW: subagent that interviews the user for patterns
plugin/scripts/regenerate_spreadsheet.py
                                    # MODIFY: emit color-coded fills and bold spans per protocols/spreadsheet-formatting.md
```

### 9.2 Files to remove or deprecate

```
plugin/agents/_screening-subagent.md
                                    # No longer used (replaced by deterministic classifier)
plugin/scripts/consolidate_screening.py
                                    # No longer used (no two-sub-agent reconciliation)
```

The 19-criterion `protocols/screening.yaml` machinery can stay for backward compatibility but the new agents should ignore it in favor of the per-stage classifier configs. Or strip it down to just the bare metadata (RQs, sub-RQs, doctrine) and drop criteria/weights/thresholds.

### 9.3 New stage-04 agent flow (suggested)

```
1. Verify locks.03 == locked, locks.04 ∈ {pending, iterating}.
2. Ask the user which model to use (default: Sonnet 4.6 / Medium effort).
3. Check whether protocols/classifier-config-title.json exists.
   - If not: spawn elicit-classifier-patterns subagent in 'title' mode.
     The subagent walks the user through the 8 categories (or however many they want),
     proposes patterns, optionally reads sample paper titles to suggest more,
     iterates until the user approves, writes the JSON.
   - If yes: confirm with the user whether to re-elicit or reuse.
4. Run the deterministic classifier over all stage-03 papers.
5. Write decisions to spreadsheet 04-tab via apply_decisions_to_spreadsheet.py
   (color codes, sort order, bold keywords per protocols/spreadsheet-formatting.md).
6. Pause for human review. Idempotency rule: any non-empty My Final Decision
   is preserved across re-runs.
7. After confirmation, run persist_manual_decisions.py to copy My Final Decision /
   My Justification into papers/paper-NNN.md frontmatter (status, screening blocks).
8. Commit [04] lock.
```

### 9.4 New stage-05 agent flow (suggested)

Same as stage 04 but with two additions:

- The classifier config is for `abstract` (different patterns than `title`).
- Papers with NO regex match in any category are routed to a single LLM tiebreaker (default: Haiku 4.5). The tiebreaker reads the abstract and emits Include or Exclude with one-sentence justification. The output goes into `My Final Decision` with an annotation in `My Justification` like `[no regex match → LLM tiebreaker decided] <reason>` so the user knows to scrutinize these rows.

### 9.5 Spreadsheet formatting (already specced)

`protocols/spreadsheet-formatting.md` in the review repo (and replicated in plugin templates) covers:
1. Background fill: `#e7ffee` (Include) / `#ffeff0` (Exclude) on Paper ID and Title columns.
2. Sort order: Excluded rows first (red block), then Included (green block); within each block sort by sub-agent disagreement (or now: by classifier confidence proxy — number of evidence hits).
3. Bold strategic keywords in Title and Abstract cells (rich-text formatting, not markdown asterisks). Bold the matched evidence substrings to surface the reason for inclusion/exclusion at a glance.

The regenerator must use `openpyxl` rich-text support (`load_workbook(..., rich_text=True)` and `CellRichText`).

### 9.6 Risks during migration

1. **Loss of pre-existing reviews' state.** Existing reviews have `protocols/screening.yaml` and `screening/<stage>/{sub-agent-1,sub-agent-2,consolidated}.json`. Migration must either (a) keep the old code path for backward compat, or (b) provide a one-shot conversion script.
2. **Different stages need different patterns.** The 8 categories of title screening are not directly applicable to abstract or full-text. A future LLM running stage 05 must elicit a new (possibly larger) pattern set with the user. This is a *human-in-the-loop* requirement, not optional.
3. **No two-sub-agent emulation.** The plugin's `consolidate_screening.py` and `Difference in Final Score Between Sub-Agents` column become meaningless. Either remove or repurpose those columns.
4. **Spreadsheet regenerator is a chronic data-loss source.** If the regenerator runs after a manual edit but before the manual edit is persisted to paper files, it overwrites the user's edits. **The migration must enforce: every commit that lock-completes a stage MUST first persist manual decisions to paper files, then commit, then let the hook regenerate.** This is a hard ordering constraint.

---

## 10. Open questions for stages 05 and 06

1. **What does the abstract-stage rule set look like?** It should reuse the title categories conceptually (review, RL, LLM-as-workload, MAS, Agent, LLM/Agentic AI generic, out-of-scope) but with patterns tuned for ~150-word abstracts instead of ~12-word titles. The elicit-classifier-patterns subagent should walk the user through this from scratch.
2. **Does the LLM tiebreaker handle ALL no-match cases or only some?** Recommend ALL, but with a confidence threshold under which the row goes to manual review (`My Final Decision` left blank).
3. **How does the QA criterion (C18, C19 — "described with sufficient detail" and "evaluation presented") fit in at full-text stage?** Not regex-amenable. May need to keep an LLM scorer just for QA criteria, separate from the regex classifier for thematic_sub_rq.
4. **Should the classifier config files be versioned per-review or per-stage globally?** Recommend per-review (`protocols/classifier-config-{title,abstract,full_text}.json` in each review repo). Different reviews have different scopes.
5. **How is the audit re-run after each iteration of the config?** The audit script is idempotent. Re-running is cheap (<1s for 2,949 papers). Recommend running it after every config change AND after every manual-mistake correction batch.

---

## 11. Reproducibility checklist

To replicate this exact state of the title-stage classifier on the Agentic-AI-RM review:

```bash
cd /Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud

# Sanity check that all artifacts are present
ls scripts/deterministic_classifier.py scripts/audit_stage_04.py
ls protocols/classifier-config-title.json
ls spreadsheet_title_screening.xlsx

# Run the audit
python3 scripts/audit_stage_04.py --xlsx spreadsheet_title_screening.xlsx
# Expected:
#   total: 2949
#   match_rate: 0.9112
#   include_recall: 0.972
#   exclude_recall: 0.897
#   FN: 16
#   FP: 246
```

The 16 FN are exactly: paper-014, paper-015, paper-034, paper-468, paper-497, paper-571, paper-608, paper-635, paper-751, paper-853, paper-983, paper-1532, paper-1596, paper-1629, paper-1866, paper-2041.

If your audit produces different numbers, something has drifted (config, spreadsheet, or classifier code).

---

## 12. Glossary

- **Manual mistake** — a row where the user marked Include or Exclude that contradicts their own declared screening rules. Found by inspecting classifier disagreements.
- **Borderline** — a row where the user marks Include based on speculative/weak signal that the rules cannot reasonably encode. Accepted as residual FN.
- **Override** — a regex pattern within a category that, when matched, suppresses the category's exclusion and forces evaluation to continue to the next-priority category.
- **Soft Include** — a category whose triggers are deliberately broad (e.g., `\bagent[s]?\b`) because finer disambiguation is deferred to the next stage.
- **Doctrine** — the user's stated principle "when in doubt, include." Calibrates the classifier toward Include under ambiguity.
- **Recall-preserving rule** — the original plugin's mechanism (at abstract stage) of auto-including any paper where an LLM sub-agent flagged `insufficient_evidence`. The deterministic classifier replaces this with the LLM tiebreaker mechanism for no-match rows.
- **Tiebreaker** — a single LLM call invoked only on rows where the regex classifier produced no match in any category. Used at abstract and full-text stages, not at title.
