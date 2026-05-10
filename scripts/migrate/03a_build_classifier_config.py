"""Build protocols/classifier-config.json from legacy abstract-stage config.

Strategy: stages 04 (title) and 05 (abstract) are already locked. The legacy
abstract config is a superset of title (more categories, more patterns). We
adopt it as the v3 baseline. Stage 06 (full-text) will refine this file via
the regular Q&A flow when /04-screen --stage full-text runs for the first time.

Schema translation (legacy v2 -> plugin v3.2.0):
- Drop top-level 'stage' key (no longer needed).
- Add 'version': '1.0'.
- Add 'priority_order' from each category's legacy 'priority' field, sorted.
- For each category:
    * 'decision' (Include|Exclude) -> 'kind' (include|exclude).
    * 'priority' (1-based) -> 'priority_index' (0-based, == position in
      priority_order).
    * Inject 'label' (humanized from id).
    * Inject 'justification' from legacy 'justification' (already present per
      category, otherwise default to legacy default_justification).
"""

import json
from pathlib import Path

REPO = Path('/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud')
LEGACY = REPO / 'legacy/protocols/classifier-config-abstract.json'
OUT = REPO / 'protocols/classifier-config.json'

LABEL_OVERRIDES = {
    'out_of_scope': 'Domínio fora de escopo',
    'review': 'Survey/review/mapping/tutorial',
    'rl': 'Reinforcement learning sem LLM',
    'llm_as_workload': 'LLM como workload (servir/treinar), não como agente',
    'classical_agents': 'Agentes clássicos (não-LLM)',
    'mas_llm_based': 'Multi-agent system baseado em LLM',
    'agent_llm_based': 'Single-agent baseado em LLM',
    'llm_agentic_ai_generic': 'Agentic AI / LLM (genérico)',
}

DECISION_TO_KIND = {'Include': 'include', 'Exclude': 'exclude'}


def main():
    legacy = json.loads(LEGACY.read_text())

    cats_sorted = sorted(legacy['categories'], key=lambda c: c['priority'])
    priority_order = [c['id'] for c in cats_sorted]

    new_categories = []
    for idx, c in enumerate(cats_sorted):
        new_c = {
            'id': c['id'],
            'label': LABEL_OVERRIDES.get(c['id'], c['id']),
            'kind': DECISION_TO_KIND[c['decision']],
            'justification': c.get('justification', legacy['default_justification']),
            'priority_index': idx,
            'patterns': c.get('patterns', []),
            'overrides': c.get('overrides', []),
        }
        new_categories.append(new_c)

    out = {
        'version': '1.0',
        'default_decision': legacy['default_decision'],
        'default_justification': legacy['default_justification'],
        'proximity_window': legacy['proximity_window'],
        'priority_order': priority_order,
        'categories': new_categories,
    }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))

    # Quick self-check against schema rules.
    print('written:', OUT)
    print('version:', out['version'])
    print('default_decision:', out['default_decision'])
    print('proximity_window:', out['proximity_window'])
    print('categories:', len(out['categories']))
    print('  by kind:', {k: sum(1 for c in out['categories'] if c['kind'] == k) for k in ['include', 'exclude']})
    print('priority_order:', out['priority_order'])
    print('priority_index match:', all(c['priority_index'] == i for i, c in enumerate(out['categories'])))
    pat_total = sum(len(c['patterns']) for c in out['categories'])
    ovr_total = sum(len(c['overrides']) for c in out['categories'])
    print(f'patterns: {pat_total}; overrides: {ovr_total}')


if __name__ == '__main__':
    main()
