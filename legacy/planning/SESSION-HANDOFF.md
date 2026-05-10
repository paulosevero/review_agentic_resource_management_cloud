# Session Handoff — Stage 05 Abstract Screening

Snapshot do trabalho até 2026-05-03. Carregue este arquivo no início de uma sessão nova para retomar do mesmo ponto.

## Contexto do projeto

Rapid review systematic literature review sobre **Agentic AI (LLM-based agents) for resource management in Cloud/Edge/Fog/Edge-Cloud Continuum**. Repositório em `/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud`. Protocolo completo em `CLAUDE.md` (RQs, critérios, boundaries A/B/C, doutrina "when in doubt, include" no estágio 04 e regra estrita no 05).

Estágio atual: **05 — Abstract Screening** (bloqueio em `pending`). Total: 579 papers (passaram do estágio 04). Aba principal: `Análise.xlsx` aba `05 — Abstract Screening`.

## Estado atual da planilha

- **Total**: 579 linhas.
- **Includes (efetivos)**: 114.
- **Excludes (efetivos)**: 458.
- **Não-decididos**: 7.
- **Manual overrides aplicados** (`My Final Decision` ≠ `Auto Decision`): 162.

Distribuição prévia do classificador (antes dos overrides):

```
classical_agents       193 Exclude
llm_agentic_ai_generic 187 Include
rl                      68 Exclude
agent_llm_based         40 Include
mas_llm_based           37 Include
llm_as_workload         31 Exclude
review                  13 Exclude
out_of_scope             2 Exclude
no_signal                1 tiebreaker (Exclude)
```

## O que já foi feito

### 1. Auditoria de flips (concluída)

Compilei lista consolidada de 68 Include→Exclude + 1 Exclude→Include sobre 579 linhas. **Todos aplicados** (39 pelo user na sessão prévia + 29 por mim). Plus auditoria pós-aplicação encontrou mais 3 flips recomendados ainda não aplicados:

- **paper-1401** (row 401) — Simurgh: Multi-Agent Adversarial Benchmarking → flip Exclude (sem LLM, MAS+DRL clássico).
- **paper-2209** (row 485) — Multigranularity Edge DC Network → flip Exclude (rede óptica para GAI jobs = workload).
- **paper-2881** (row 534) — LEAF: Lightweight Edge Agent Framework → flip Exclude (deploy de SLM agents em IIoT = workload).
- **paper-1722** (row 418) — Cloudless Intelligence → manter Include (borderline, doutrina).

Esses 3 flips ficaram para serem confirmados/aplicados pelo pente fino dos sub-agentes (próxima fase).

### 2. Refinamento de bolding (concluído)

Problema original: bolding cego com substring match (palavras comuns como "with", "of", "This" sendo destacadas; plurais e termos hifenizados quebrados).

Solução implementada e aplicada:

- **`protocols/bolding-keywords.yaml`** — lista curada com 7 grupos (~287 termos), construída a partir de análise de doc-frequency sobre 579 títulos + 250 abstracts (incluídos) e 2.621 documentos excluídos. Grupos: scope_infrastructure, agentic_ai_llm, resource_management, classical_ml_rl, domain_subscope, llm_as_workload, document_type. Plus strip_patterns (regex que removem © + boilerplate de editora) e stopword_trim.
- **`scripts/refine_bolding.py`** — pipeline spaCy (`en_core_web_sm`) + PhraseMatcher: case-insensitive, longest-match, merge de spans separados por hífen/espaço, extensão de plural, trim de stopwords nas pontas, density cap 50%.
- Aplicado em todas as 579 linhas da aba `05 — Abstract Screening`. Editorial noise removido. Bold refinado. Backup em `Análise.bolding-backup.xlsx`.

### 3. Plano de pente fino (concluído, ainda não executado)

Documentado em **`planning/abstract-screening-pente-fino.md`**. 4 sub-agentes especializados:

| Sub-agente | Foco | Direção | Modelo | Pop. |
| --- | --- | --- | --- | --- |
| 1. Boundary-A Auditor | Loop agentic LLM-based real? | Include → Exclude | Sonnet | 114 Includes |
| 2. Boundary-B Auditor | Ação é decisão de RM em malha fechada? | Include → Exclude | Opus | 114 Includes |
| 3a. Hard-Gate + Boundary-C | Surveys/posters/livros + escopo de infra | Include → Exclude | Sonnet | 114 Includes |
| 3b. False-Negatives | Excludes que deveriam ser Include | Exclude → Include | Haiku | 458 Excludes |

Cada um emite JSON em `planning/audits/audit-<N>-*.json`. Formato compartilhado com `flips` + `borderline_kept`, cada item com `row`, `paper_id`, `current_decision`, `recommended_decision`, `confidence` (high/medium/low), `rationale_pt`, `evidence_quote`.

### 4. Scripts de consolidação e aplicação (concluídos)

- **`scripts/consolidate_audits.py`** — merge dos 4 JSONs por paper_id, gera `planning/audits/consolidated.xlsx` com 4 abas: `flips_high_confidence` (auto-aprovado), `flips_review`, `conflicts`, `borderline_kept`.
- **`scripts/apply_audit_flips.py`** — lê consolidated.xlsx filtrando `Approved by Reviewer == TRUE`, aplica em `Análise.xlsx`. Backup → `Análise.audit-backup.xlsx`. Log → `planning/audits/applied-flips.md`.

Smoke test rodado com mocks. Funcional.

## O que falta fazer

### Fase 1 — Executar os 4 sub-agentes em paralelo

Spawnar via `Agent(subagent_type=general-purpose, model=<modelo>)`. Prompts prontos em `planning/abstract-screening-pente-fino.md` §"Spawn dos agentes". Cada sub-agente lê o spec do MD, audita sua população, e grava seu JSON em `planning/audits/`.

Os 4 sub-agentes podem rodar em paralelo (chamada única do Agent tool com 4 blocos). Tempo esperado: 5-10 min total.

Os 3 mock JSONs em `planning/audits/audit-*.json` devem ser sobrescritos pelos outputs reais.

### Fase 2 — Consolidação e revisão

```bash
. /tmp/refine_env/bin/activate  # venv com openpyxl + pyyaml + spacy + en_core_web_sm
cd /Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud
python scripts/consolidate_audits.py
```

Abrir `planning/audits/consolidated.xlsx`. Aba 1 (`flips_high_confidence`) tem `Approved=TRUE` por default. Abas 2–3 (`flips_review`, `conflicts`) ficam vazias para revisão humana. User marca `TRUE` nas que aprova.

### Fase 3 — Aplicação

```bash
python scripts/apply_audit_flips.py --dry-run    # preview
python scripts/apply_audit_flips.py --apply      # escrita + log + backup
```

### Fase 4 — Métrica de qualidade (opcional)

Calcular Cohen's κ entre cada sub-agente e os 162 manual overrides prévios. κ < 0.4 = sub-agente desalinhado, recomendações futuras precisam recalibração.

## Ambiente Python

Venv pronto em `/tmp/refine_env`:

```bash
. /tmp/refine_env/bin/activate
# Instalado: openpyxl, pyyaml, spacy, en_core_web_sm
```

Se a sessão nova não tiver mais o venv (foi /tmp), recriar:

```bash
uv venv /tmp/refine_env
. /tmp/refine_env/bin/activate
uv pip install openpyxl pyyaml spacy
python -m spacy download en_core_web_sm
```

## Arquivos-chave

```
review_agentic_resource_management_cloud/
├── CLAUDE.md                                    # Protocolo (RQs, critérios, boundaries)
├── Análise.xlsx                                 # Planilha principal
├── Análise.bolding-backup.xlsx                  # Backup pré-bolding
├── protocols/
│   ├── screening.yaml                           # Critérios formais
│   └── bolding-keywords.yaml                    # Keywords + strip_patterns + stopwords
├── scripts/
│   ├── refine_bolding.py                        # Bolding refinado (já aplicado)
│   ├── consolidate_audits.py                    # Merge dos 4 JSONs
│   └── apply_audit_flips.py                     # Aplica flips aprovados
└── planning/
    ├── abstract-screening-decisions.md          # Design da Stage 05
    ├── abstract-screening-pente-fino.md         # Spec dos 4 sub-agentes
    ├── SESSION-HANDOFF.md                       # Este arquivo
    └── audits/
        ├── audit-1-boundary-a.json              # Mock — sobrescrever com real
        ├── audit-2-boundary-b.json              # Mock — sobrescrever com real
        ├── audit-3a-hardgate-scope.json         # Mock — sobrescrever com real
        ├── audit-3b-false-negatives.json        # Mock — sobrescrever com real
        ├── consolidated.xlsx                    # Output do consolidate (mock atual)
        └── applied-flips.md                     # Log de aplicação (criado no apply)
```

## Convenções confirmadas com o user

- PT-BR para conversa, EN-US para texto acadêmico.
- Justificativas de exclusão/inclusão em PT-BR.
- Doutrina Stage 05: "when in doubt, include" aplicado com tolerância média (mais estrita que estágio 04 para MAS/agent sem sinal LLM).
- Boundary A: loop agentic LLM-based obrigatório.
- Boundary B: ação do agente deve afetar decisão de RM em malha fechada.
- Boundary C: cloud / edge / fog / continuum apenas (HPC, single-device, smart-grid-only fora).
- Manual review rules: excluir surveys, posters, demos sem avaliação, livros, não-peer-reviewed, não-inglês.
