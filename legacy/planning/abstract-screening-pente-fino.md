# Pente Fino — Aba "05 — Abstract Screening"

Plano de 3 sub-agentes especializados para uma auditoria final sobre as decisões consolidadas (auto + manual) da Stage 05. Cada sub-agente cobre uma dimensão distinta de erro, com instruções, critérios, exemplos calibrados e formato de reporte unificado.

## Visão geral

| Sub-agente | Dimensão auditada | Direção dominante de flip | Tamanho típico do output | Modelo |
| --- | --- | --- | --- | --- |
| 1. Boundary-A Auditor | Loop agentic LLM-based realmente presente? | Include → Exclude | 5–20 papers | Sonnet |
| 2. Boundary-B Auditor | Ação do agente é decisão de RM em malha fechada? | Include → Exclude | 10–30 papers | Opus |
| 3. Hard-Gate + Boundary-C + False-Negative Auditor | Tipo de documento, escopo de infra, e exclusões erradas | Mista | 5–25 papers | Sonnet (sub-modo C pode rodar com Haiku) |

Cada sub-agente roda independentemente sobre todas as 579 linhas. Resultados são consolidados em um único spreadsheet de saída para revisão humana antes de aplicar flips.

### Justificativa da escolha de modelo

- **Sub-agente 1 — Sonnet.** Mecânica predominante (matching de sinais LLM via regex + leitura curta do contexto). Ocasionalmente julga papers borderline (vision papers, terminologia não-padrão). Sonnet equilibra custo e nuance suficiente para essa fronteira. Haiku perderia casos onde o sinal LLM está embutido em parafraseamento ("autonomic computing leveraging foundation-scale models"), e Opus seria custo excessivo para a maioria dos casos triviais.
- **Sub-agente 2 — Opus.** Tarefa semanticamente mais difícil das três: distinguir "LLM-aided RM decision" vs. "LLM-served as workload" vs. "LLM-tool-only sem closed loop" exige leitura cuidadosa do que é a contribuição central do paper. População pequena (114 Includes) limita o custo. Erros aqui têm alto custo (flip injusto Include→Exclude pode descartar paper relevante; manter Include errado polui Stage 06).
- **Sub-agente 3 — Sonnet (default), Haiku para sub-modo C.** Sub-modos A (hard gates) e B (Boundary C) são regex-leaning sobre 114 papers — Sonnet basta. Sub-modo C (false negatives) varre ≈ 458 Excludes em busca de sinais LLM perdidos pelo override; é volume alto com julgamento simples (presença/ausência de keyword + sanity check). Haiku é adequado para esse scan em massa; pode-se promover papers borderline para Sonnet em segunda passada se necessário. Alternativa: dividir em 3a (Sonnet, Includes) e 3b (Haiku, Excludes) rodando como agentes separados em paralelo.

## Input compartilhado

- Arquivo: `Análise.xlsx`, aba `05 — Abstract Screening`.
- Colunas relevantes: `Paper ID` (1), `Title` (2), `Year` (3), `Abstract` (4), `Auto Decision` (5), `Auto Justification` (6), `Winning Category` (7), `Evidence` (8), `My Final Decision` (9), `My Justification` (10).
- Decisão efetiva = `My Final Decision` se ∈ {Include, Exclude}, senão `Auto Decision`.
- Protocol context: `CLAUDE.md` §2 (theme), §3 (RQs), §5 (criteria), §6 (manual review rules), §10 (formatting).

## Output compartilhado (formato unificado)

Cada sub-agente emite um arquivo JSON em `planning/audits/audit-<N>-<short-name>.json`:

```json
{
  "auditor": "boundary-a",
  "ran_at": "2026-05-03T14:00:00Z",
  "papers_reviewed": 579,
  "flips": [
    {
      "row": 401,
      "paper_id": "paper-1401",
      "current_decision": "Include",
      "recommended_decision": "Exclude",
      "confidence": "high",
      "rationale_pt": "MAS clássico com Bayesian opt + DRL; nenhum sinal de LLM/foundation model/agentic no abstract.",
      "evidence_quote": "We evaluate our framework on two applications and three optimization methods, including Bayesian optimization, chaos engineering, and a distributed reinforcement learning approach."
    }
  ],
  "borderline_kept": [
    {
      "row": 418,
      "paper_id": "paper-1722",
      "current_decision": "Include",
      "rationale_pt": "Vision paper sobre 'autonomous AI agents on edge fabric'; sem termo LLM explícito mas título e tese coerentes com agentic AI moderno. Mantido Include por doutrina."
    }
  ]
}
```

`confidence` ∈ {`high`, `medium`, `low`}. Apenas `high` deve ser aplicado automaticamente; `medium` e `low` requerem revisão humana.

---

## Sub-agente 1 — Boundary-A Auditor (verificador de loop agentic LLM-based)

### Missão

Identificar papers atualmente marcados como `Include` que não exibem evidência de loop agentic genuinamente LLM-based no abstract, devendo portanto ser flipados para `Exclude` por violação da Boundary A.

### Escopo

Auditar todas as linhas com `effective_decision == 'Include'` (≈ 114 papers no estado atual). Não tocar em Excludes — essa direção fica para o Sub-agente 3.

### Critérios de decisão

**Sinal LLM substantivo** = pelo menos UMA das ocorrências abaixo aparece no abstract (não apenas no título nem em related work):

- Termos diretos: `LLM`, `LLMs`, `GPT`, `GPT-4`, `ChatGPT`, `large language model(s)`, `foundation model(s)`, `language model(s)`, `BERT`, `LLaMA`, `Claude`, `Mistral`, `Gemini`.
- Variantes agentic: `agentic AI`, `agentic system/workflow/framework`, `LLM agent(s)`, `AI agent(s)` quando explicitamente combinado com termo LLM/GenAI.
- Famílias generativas: `generative AI`, `GenAI`, `AIGC`, `generative artificial intelligence`.
- Técnicas distintivas: `chain-of-thought`, `CoT`, `prompt engineering`, `retrieval-augmented generation`, `RAG`, `MCP`, `in-context learning`, `few-shot prompting`.
- Equivalência funcional: `intent-driven`, `intent-based`, `autonomic`, `conversational AI` quando claramente aplicado a LLM.

**Loop agentic** = o paper descreve um ciclo `perceber → raciocinar → agir` onde o componente que raciocina é um LLM/foundation model/agente generativo. Mero uso de "AI" ou "intelligent" sem referência a tecnologia LLM não conta.

**Decisão**:

- Mantém `Include` se → o abstract contém ≥ 1 sinal LLM substantivo E o LLM participa do loop de decisão.
- Flip → `Exclude` se → nenhum sinal LLM substantivo aparece no abstract OU o LLM é mencionado apenas em contexto periférico (related work, motivação genérica, ferramenta auxiliar não-decisória).
- Marcar como `borderline_kept` se → existe ambiguidade que a doutrina "when in doubt, include" resolve a favor do Include (ex.: vision paper, abstract curto demais, terminologia não-padrão).

### Procedimento

1. Para cada Include, ler o abstract integralmente (não apenas o snippet).
2. Buscar sinais LLM substantivos com word-boundary regex.
3. Se zero sinais: flip Exclude com `confidence = high`.
4. Se 1 sinal mas em contexto periférico (apenas em "related work suggests..." ou "AI techniques such as LLMs..."): flip Exclude com `confidence = medium`.
5. Se ≥ 1 sinal substantivo no contexto da contribuição: keep Include.
6. Casos ambíguos → `borderline_kept` com nota.

### Exemplos calibrados

| Paper | Decisão | Razão |
| --- | --- | --- |
| paper-1401 (Simurgh) | flip Exclude | MAS + Bayesian + DRL; zero sinal LLM. |
| paper-019 (cryptographic agent, 2017) | flip Exclude | Pré-LLM, segurança clássica. |
| paper-532 (Trust-Based MA Imitation Learning) | flip Exclude | Imitation learning sem LLM. |
| paper-1722 (Cloudless Intelligence) | borderline kept | "Autonomous AI agents" sem termo LLM mas tese coerente. |
| paper-708 (LLMs for Auto-remediation) | keep Include | LLM substantivo no loop de remediação. |
| paper-1308 (VELO) | keep Include | "LLM" + "Cloud-Edge Collaborative" no abstract. |

### Anti-patterns (não flipar erroneamente)

- "Federated learning" sozinho não é LLM. Mas "federated fine-tuning of LLMs" é sinal LLM (e provavelmente cai em workload — Sub-agente 2).
- "Reinforcement learning" não é LLM. Mas "LLM-aided RL" ou "Generative AI-aided RL" é sinal LLM válido.
- "Agent-based" sozinho ≠ agentic AI. Combinar com sinal LLM separado.
- "Transformer" sozinho pode ser arquitetura ML clássica (Vision Transformer, etc.); só conta como sinal LLM se contextualizado como language model ou usado para texto/raciocínio.

---

## Sub-agente 2 — Boundary-B Auditor (verificador de RM como loop fechado)

### Missão

Identificar papers Include onde o sistema LLM/agentic existe mas suas ações não constituem decisão de resource management em malha fechada. Direção dominante: Include → Exclude por violação da Boundary B.

### Escopo

Mesma população do Sub-agente 1 (todos os Includes). Roda em paralelo. Pode haver sobreposição com Sub-agente 1 — ambos podem flagar o mesmo paper, com motivos distintos.

### Critérios de decisão

**RM como loop fechado** = a ação do agente afeta diretamente uma das classes de decisão abaixo, e o sistema observa o efeito da ação (closed loop):

- Scheduling de tarefas/jobs/workflows.
- Placement de containers/VMs/funções/microserviços.
- Scaling (autoscaling, vertical/horizontal).
- Migration/relocation.
- Admission control.
- Load balancing/routing.
- Slicing (network slicing).
- Energy management/orchestration.
- Capacity planning/provisioning.
- Fault response/recovery.
- Resource allocation (CPU/memória/disco/banda) entre múltiplos consumidores.

**Sub-modo A — LLM-as-workload (mais comum)**:

O LLM é o workload sendo servido/treinado/deployado pelo sistema, não o cérebro que toma decisões. Sinais:

- "We propose a system to serve/deploy/host LLMs"
- "LLM inference engine/serving infrastructure/pipeline"
- "Efficient LLM serving/inference/training/fine-tuning/deployment"
- "Optimizing LLM workload sustainability/cost/latency"
- "AIGC services" (quando o paper otimiza a entrega desses serviços)
- "Scheduling/placement of LLM/GAI jobs"

Override: se o paper menciona LLM-as-workload mas a contribuição é claramente um agente LLM tomando decisões sobre essa infraestrutura, manter Include.

**Sub-modo B — LLM-as-tool sem closed loop**:

O LLM analisa, sumariza, gera relatórios, mas a ação de RM é tomada por outro componente (humano ou heurística separada):

- "LLM for log summarization / anomaly explanation / RCA report generation"
- "LLM-powered observability / monitoring / dashboard"
- "LLM for security threat analysis / vulnerability detection"
- "LLM for code review / smell detection / quality assessment"
- "LLM for incident triage / alert clustering"

Override: se o paper conecta a saída do LLM diretamente a uma ação de RM automatizada (ex.: anomaly → autoscaling), manter Include.

**Sub-modo C — Tarefa fora de RM**:

LLM aplicado a tarefa não-RM, mesmo que rode em cloud/edge:

- Resume parsing / NLP de RH.
- Geração de documentação / requisitos.
- Tradução / chatbot puro.
- Recomendação offline / análise de sentimento.
- Geração de imagens / áudio.
- Federated learning de LLMs como contribuição central (≠ usar LLM para gerenciar federated learning).

### Procedimento

1. Para cada Include, ler abstract.
2. Identificar a contribuição central: o que o sistema proposto FAZ?
3. Verificar se a ação resultante recai em uma das classes de RM listadas.
4. Se a ação é serving/training/deploying o próprio LLM → Sub-modo A → flip Exclude.
5. Se a ação é gerar relatório/análise sem fechar loop com ação automatizada → Sub-modo B → flip Exclude.
6. Se a ação é fora de RM → Sub-modo C → flip Exclude.
7. Caso contrário → keep Include.

### Exemplos calibrados

| Paper | Decisão | Sub-modo | Razão |
| --- | --- | --- | --- |
| paper-2209 (Multigranularity Edge DC) | flip Exclude | A | Rede óptica para acelerar GAI jobs (workload). |
| paper-2881 (LEAF) | flip Exclude | A | Framework para deployar SLM agents em IIoT. |
| paper-1205 (Titanic Federated LLMs) | flip Exclude | A | Federated fine-tuning de LLMs. |
| paper-2381 (AIGC Services Optimization) | flip Exclude | A | Otimiza entrega de serviços AIGC. |
| paper-2027 (LLMs for Anomaly Detection) | flip Exclude | B | Detecção sem closed loop de ação RM. |
| paper-2090 (GenAI bottleneck Detection) | flip Exclude | B | Detecção de gargalos, não decisão de RM. |
| paper-1083 (Resume Parsing LLMs) | flip Exclude | C | NLP de RH, fora de RM. |
| paper-847 (AI-CRAS Requirement Analysis) | flip Exclude | C | Engenharia de requisitos, fora de RM. |
| paper-708 (LLMs Auto-remediation) | keep Include | — | LLM gera ação de remediação aplicada ao sistema. |
| paper-909 (Intent-Driven Deployment & Migration) | keep Include | — | LLM decide deployment + migration. |

### Anti-patterns

- Não confundir "LLM-aided" (LLM ajuda na decisão) com "LLM-served" (LLM é o objeto da decisão). O primeiro é Include; o segundo é Exclude.
- "Anomaly detection" é Sub-modo B somente quando termina em alerta/relatório. Se segue ação automatizada (ex.: trigger autoscaling), é Include.
- "Container orchestration" é RM. Mas "code smell detection in container manifests" não é RM (é code quality).
- "Federated learning" pode ser Include se o paper usa LLM para orquestrar o processo federado (ex.: client selection via LLM). É Exclude se o LLM é o modelo sendo treinado federadamente.

---

## Sub-agente 3 — Hard-Gate + Boundary-C + False-Negative Auditor

### Missão

Cobrir três áreas que os Sub-agentes 1 e 2 não cobrem:

1. **Hard gates documentais**: tipo de documento e qualidade de fonte (manual review rules do CLAUDE.md §5).
2. **Boundary C**: escopo de infraestrutura (cloud/edge/fog/continuum vs. fora de escopo).
3. **False negatives**: papers Excluídos que deveriam ser Include.

Diferente dos outros dois, este sub-agente tem direção mista: pode flipar Include→Exclude OU Exclude→Include.

### Escopo

- Sub-modo A (Hard gates) e Sub-modo B (Boundary C): rodam sobre os 114 Includes.
- Sub-modo C (False negatives): roda sobre os ≈ 458 Excludes, com prioridade para os de categorias `classical_agents`, `rl`, `llm_as_workload` (onde o override pode ter falhado).

### Critérios — Sub-modo A (Hard gates documentais)

Flagar Include → Exclude se o abstract/título indica:

**Survey/review/taxonomy/mapping**:

- "this survey", "we survey", "this paper surveys"
- "this review", "we review", "literature review", "systematic review", "comprehensive review", "state-of-the-art review"
- "systematic mapping study"
- "we present an overview", "this article overviews"
- "challenges and future directions" como tese central (não apenas seção final)

**Poster / demo / tutorial / editorial**:

- Título começa com `Poster:`, `Demo:`, `Tutorial:`, `Work-in-progress:`.
- Abstract muito curto (< 80 palavras) sem avaliação experimental.

**Livro / capítulo / não-peer-reviewed**:

- Sinais editoriais: "Key Features:", "● Learn", "Embark on the journey", "this book covers", "this guide", tabela de conteúdo no abstract.
- Editora de livro técnico (Packt, O'Reilly, Apress, BPB Publications, Springer Briefs).
- Origem não-peer-reviewed (arXiv-only, technical report, white paper).

**Idioma não-inglês**: abstract claramente em outro idioma com tradução parcial.

### Critérios — Sub-modo B (Boundary C — Infrastructure scope)

Flagar Include → Exclude se a infraestrutura alvo está claramente fora do escopo (cloud / edge / fog / continuum):

- **HPC / supercomputing**: clusters HPC tradicionais sem framing de cloud/edge.
- **Single-device embedded**: sistemas em um único device IoT sem cloud/edge layer.
- **End-user device puro**: smartphone/laptop sem componente edge.
- **HVAC building only**: controle de prédio único sem edge/cloud.
- **Single-domain healthcare**: imageamento médico sem deployment cloud/edge significativo.
- **Smart-grid only**: gestão de energia sem aspecto computacional cloud/edge.
- **Supply chain / finance / agriculture**: aplicação de domínio sem componente RM cloud/edge central.

Manter Include se: o paper aplica LLM/agentic AI em domínio específico mas a infraestrutura alvo é cloud/edge/fog/continuum (ex.: "LLM-driven scheduling em edge-cloud continuum para healthcare workflows" — Include).

### Critérios — Sub-modo C (False negatives — Excludes errados)

Foco em três tipos de exclusão suspeita:

**C.1 — `classical_agents` Exclude com sinal LLM no abstract**:

Buscar termos LLM substantivos (ver Sub-agente 1) em papers excluídos por `classical_agents`. Se encontrar, o override LLM deveria ter disparado e o paper ser reavaliado em `mas_llm_based`/`agent_llm_based`.

**C.2 — `rl` Exclude com hibridização LLM**:

Buscar `LLM-aided`, `LLM-guided`, `generative AI-aided`, `LLM-enhanced` + termos RL. Esses são RL+LLM hybrids que devem ser Include.

**C.3 — `llm_as_workload` Exclude que na verdade decide RM**:

Re-ler abstracts de Excludes em `llm_as_workload` checando se o sistema usa LLM para tomar decisão de RM (override que falhou). Sinais: "LLM decides/selects/orchestrates", "agentic workflow controls placement", "using LLMs to schedule/allocate/migrate".

### Procedimento

1. Sub-modo A: scan de regex sobre títulos + primeiras 3 sentenças do abstract.
2. Sub-modo B: ler abstract, identificar infra alvo, comparar com taxonomia de escopo.
3. Sub-modo C: amostrar 30–50 Excludes por categoria + busca por keywords LLM nos `classical_agents` e `rl` Excludes + leitura completa dos `llm_as_workload` Excludes (≈ 31).

### Exemplos calibrados

| Paper | Decisão | Sub-modo | Razão |
| --- | --- | --- | --- |
| paper-1196 (Generative AI for Cloud Solutions) | flip Exclude | A | Livro Packt (já flipado). |
| paper-983 (Mastering Snowflake) | flip Exclude | A | Livro (já flipado). |
| paper-1084 (Poster: Multi-Agent Transformer) | flip Exclude | A | Poster (já flipado). |
| paper-1588 (Demo: Conversational AI Agent) | flip Exclude | A | Demo (já flipado). |
| paper-1172 (Office HVAC Control) | flip Exclude | B | HVAC building único (já flipado). |
| paper-1083 (Resume Parsing) | flip Exclude | B | NLP RH fora de escopo (já flipado). |
| paper-1314 (GenAI-aided RL Computation Offloading) | mantém Include | C.2 | RL+LLM hybrid corretamente incluído. |
| Hipotético: `paper-XXX classical_agents` excluído mas com "LLM" no abstract | flip Include | C.1 | Override falhou. |

### Anti-patterns

- "Smart cities" como aplicação não exclui automaticamente — verificar se a infra é edge/cloud (geralmente é).
- "Internet of Vehicles" / "vehicular edge" são cloud-edge continuum — Include válido.
- Surveys que apresentam contribuição original (taxonomia + experimentos novos) são borderline; aplicar doutrina do estágio 05 (Boundary A precisa estar presente; surveys puros são Exclude).
- Não confundir "comprehensive evaluation" com "comprehensive review" — o primeiro é avaliação experimental (Include válido).

---

## Pipeline de execução

### Sequência sugerida

1. **Rodar os 3 sub-agentes em paralelo**, cada um produzindo seu JSON.
2. **Consolidar** em um único spreadsheet `audits/consolidated.xlsx` com colunas: `row | paper_id | current | rec_A | rec_B | rec_C | conjunto_motivos | confidence_max`.
3. **Resolver conflitos**: se dois sub-agentes recomendam a mesma direção, alta confiança. Se um recomenda Exclude e outro mantém Include, marcar para revisão humana.
4. **Aplicar flips** apenas onde `confidence == high` em ≥ 1 sub-agente E não há contradição.
5. **Logar** as decisões em `planning/audits/applied-flips.md` para histórico.

### Spawn dos agentes

Os três sub-agentes podem ser spawnados em paralelo via `Agent(subagent_type=general-purpose, model=<modelo>)` com os prompts abaixo. O parâmetro `model` sobrescreve o default herdado do parent — defina explicitamente conforme tabela "Visão geral".

```
Agent(subagent_type="general-purpose", model="sonnet", description="...", prompt=<prompt 1>)
Agent(subagent_type="general-purpose", model="opus",   description="...", prompt=<prompt 2>)
Agent(subagent_type="general-purpose", model="sonnet", description="...", prompt=<prompt 3>)  # ou "haiku" se rodar só sub-modo C
```

#### Prompt — Sub-agente 1

```
Você é o Boundary-A Auditor da Stage 05 do rapid review em
/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud.

Leia planning/abstract-screening-pente-fino.md §"Sub-agente 1" para suas
instruções completas. Audite todas as linhas com decisão efetiva == Include
na aba "05 — Abstract Screening" de Análise.xlsx. Para cada caso suspeito,
emita um item de flip em planning/audits/audit-1-boundary-a.json conforme
formato compartilhado. Use openpyxl + Python para ler a planilha. Não
modifique a planilha — apenas gere o JSON. Reporte ao final: total revisado,
total de flips, total de borderline_kept.
```

#### Prompt — Sub-agente 2

```
Você é o Boundary-B Auditor da Stage 05 do rapid review em
/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud.

Leia planning/abstract-screening-pente-fino.md §"Sub-agente 2" para suas
instruções completas. Audite todas as linhas Include verificando se a ação
do agente LLM constitui decisão de resource management em malha fechada.
Cubra os Sub-modos A (LLM-as-workload), B (LLM-as-tool sem closed loop),
C (tarefa fora de RM). Emita planning/audits/audit-2-boundary-b.json no
formato compartilhado. Não modifique a planilha. Reporte totais ao final.
```

#### Prompt — Sub-agente 3

```
Você é o Hard-Gate + Boundary-C + False-Negative Auditor da Stage 05 do
rapid review em /Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud.

Leia planning/abstract-screening-pente-fino.md §"Sub-agente 3" para suas
instruções completas. Cubra três sub-modos: A (hard gates documentais)
e B (Boundary C — escopo infra) sobre os Includes; C (false negatives)
sobre os Excludes, com prioridade nas categorias classical_agents, rl e
llm_as_workload. Emita planning/audits/audit-3-hardgate-scope-fn.json no
formato compartilhado, com flips em ambas as direções (Include→Exclude
e Exclude→Include). Não modifique a planilha. Reporte totais por sub-modo.
```

### Consolidação

Após os 3 JSONs, rodar `scripts/consolidate_audits.py` (a ser implementado) para gerar `audits/consolidated.xlsx` com:

- Aba 1 — `flips_high_confidence`: a aplicar diretamente.
- Aba 2 — `flips_review`: medium/low confidence, requerem human-in-the-loop.
- Aba 3 — `conflicts`: papers com recomendações divergentes entre sub-agentes.
- Aba 4 — `borderline_kept`: papers mantidos por doutrina, listados para visibilidade.

## Métrica de qualidade

Após aplicar os flips de alta confiança, calcular Cohen's κ entre:

- Sub-agente 1 vs. revisão manual prévia.
- Sub-agente 2 vs. revisão manual prévia.
- Sub-agente 3 vs. revisão manual prévia.

κ < 0.4 indica que o sub-agente está sistematicamente desalinhado com a doutrina humana e suas recomendações devem ser revistas antes de aplicar.
