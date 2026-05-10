## Critérios C18/C19 (full-text screening, weighted)

### Sub-RQ critérios (peso 0.7 cada — escala weighted)
- C4–C17 (RQ1.1–RQ5.2): o paper aborda arquitetura agentic, coupling a infra, guardrails, classes de decisão de RM, condições operacionais, processos de raciocínio (CoT/ReAct/Reflexion), grounding (RAG/memory), domain knowledge, metodologia/ambiente de avaliação, métricas (RM, overhead, safety/governance), tensões abertas, e gaps de governança.

### QA critérios (full-text only)
- C18 (peso 0.6): design agentic-AI-for-RM descrito com detalhe suficiente.
- C19 (peso 0.4): avaliação do sistema agentic é apresentada.

### Threshold full-text: 0.55 (weighted).

## Boundary essencial

INCLUDE quando o paper apresenta um agente agentic AI (LLM-based) cujo loop autônomo (perceive → reason → tool-use → act) DIRIGE decisões de resource management (scheduling, placement, scaling, admission, energy, fault response) em cloud/edge/fog/continuum.

EXCLUDE quando:
- LLM apenas DÁ SUPORTE (gera heurísticas/embeddings/features/recompensas) a outro método (RL/MARL/optimization clássica) que toma a decisão de RM. **O loop agentic não está no LLM.**
- Tarefas de DevOps/observabilidade (incident triage, log summarization, RCA, IaC generation) — não são decisões de RM.
- Estritamente RAN/5G/6G/spectrum sem substrato cloud/edge.
- LLM é o WORKLOAD sendo gerenciado (LLM serving/inference), não o agente decisor.
- MAS clássico, RL/MARL clássico sem LLM-driven reasoning.
- Out-of-scope: HPC, dispositivos embarcados isolados, healthcare/business apps sem RM de infra.
- Surveys/reviews/editoriais/posters/demos sem evaluation (gate manual).

## Hint do usuário (se presente)
O usuário pré-flagou alguns papers como CANDIDATOS A EXCLUSÃO. Verifique no full-text se a flag procede:
- `support`: LLM apenas dá suporte a outro método.
- `devops`: tarefa de DevOps, não RM.
- `networks`: estritamente redes/telecom.
- `quality`: qualidade duvidosa (escrita ruim, evaluation fraco, claims sem evidência).
