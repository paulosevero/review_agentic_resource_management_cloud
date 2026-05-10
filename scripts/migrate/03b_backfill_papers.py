"""Backfill papers/paper-NNNN.md (v3.2.0) from legacy/Análise.xlsx + legacy/papers/.

For each paper-NNNN in 0001..2949:
- Metadata (frontmatter): from legacy/papers/paper-NNN.md (3-digit name); abstract
  text from the same file's body.
- Title-screening decisions: from Análise.xlsx 'Corpus' (machine_decision, score,
  disagreement_type, human_decision) and aba '04 — Title Screening' (URL,
  per-sub-agent fields, My Justification).
- Abstract-screening decisions (only for the 572 papers present in aba 05):
  Auto Decision, Auto Justification, Winning Category, Evidence, My Final
  Decision, My Justification.

The output v3 file follows templates/paper.md.template:
- frontmatter with status + screening mirrors,
- # paper-NNNN — <title>,
- ## Metadata > ### Abstract,
- ## 04 — Title Screening with `### iter-0 (migrated from legacy)` + `### final`,
- ## 05 — Abstract Screening with the same blocks (only for the 572),
- placeholder sections for stages 06/07/08.

Idempotent: writing the same file twice produces identical bytes.

Usage:
    python 03b_backfill_papers.py --sample paper-0001 paper-1157   # write 2 files
    python 03b_backfill_papers.py --all                            # write all 2949
"""

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import openpyxl
import yaml

REPO = Path('/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud')
LEGACY_PAPERS = REPO / 'legacy/papers'
LEGACY_XLSX = REPO / 'legacy/Análise.xlsx'
OUT_DIR = REPO / 'papers'
MIGRATION_TS = '2026-05-09T00:00:00+00:00'

CAP = {'include': 'Include', 'exclude': 'Exclude'}


def load_xlsx_indexes() -> dict:
    """Loads three xlsx tabs into dicts keyed by paper-NNNN."""
    wb = openpyxl.load_workbook(LEGACY_XLSX, read_only=True, data_only=True)
    out = {}
    for sheet_name, key in [('Corpus', 'corpus'), ('04 — Title Screening', 's04'), ('05 — Abstract Screening', 's05')]:
        ws = wb[sheet_name]
        rows = list(ws.iter_rows(values_only=True))
        hdr = list(rows[0])
        idx_id = hdr.index('Paper ID') if 'Paper ID' in hdr else hdr.index('id')
        index = {}
        for r in rows[1:]:
            pid = r[idx_id]
            if pid:
                index[pid] = dict(zip(hdr, r))
        out[key] = index
    return out


def extract_legacy_frontmatter(legacy_path: Path) -> tuple[dict, str]:
    """Splits legacy paper file into (frontmatter dict, body text)."""
    text = legacy_path.read_text()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
    if not m:
        raise ValueError(f'no frontmatter in {legacy_path}')
    fm = yaml.safe_load(m.group(1))
    return fm, m.group(2)


def extract_abstract(body: str) -> str:
    """Pulls the abstract text from the legacy body's '### Abstract' section."""
    m = re.search(r'###\s+Abstract\s*\n+(.+?)(?=\n##|\Z)', body, re.DOTALL)
    if not m:
        return ''
    return m.group(1).strip()


def parse_keywords(raw) -> list:
    """Normalizes legacy keyword field (list or '; '-separated string) to list."""
    if not raw:
        return []
    if isinstance(raw, list):
        return raw
    return [k.strip() for k in str(raw).split(';') if k.strip()]


def parse_authors(raw) -> list:
    """Normalizes legacy authors field to list."""
    if not raw:
        return []
    if isinstance(raw, list):
        return raw
    return [a.strip() for a in str(raw).split(';') if a.strip()]


def parse_evidence_to_overrides(evidence: Optional[str]) -> tuple[list, list]:
    """Parses Análise's Evidence column into (overrides_applied, evidence_trail).

    Evidence format: 'category/pattern_id=matched_substring, category/pattern_id=…'.
    Returns override ids (de-duplicated) and the full evidence trail.
    """
    if not evidence:
        return [], []
    overrides = []
    trail = []
    for piece in str(evidence).split(','):
        piece = piece.strip()
        if not piece or '=' not in piece:
            continue
        left, _, matched = piece.partition('=')
        cat_pat = left.strip()
        if '/' in cat_pat:
            cat, pat = cat_pat.split('/', 1)
        else:
            cat, pat = 'unknown', cat_pat
        trail.append({
            'category': cat,
            'pattern_id': pat,
            'matched_substring': matched.strip(),
        })
        if pat.startswith('ovr_') and pat not in overrides:
            overrides.append(pat)
    return overrides, trail


def build_frontmatter(pid: str, legacy_fm: dict, corpus_row: Optional[dict], s04_row: Optional[dict], s05_row: Optional[dict]) -> dict:
    """Constructs the v3 frontmatter dict for paper-NNNN."""
    # Status block.
    s04_status = (corpus_row or {}).get('04.status') or 'pending'
    # Corpus.05.status was not populated in legacy; derive from aba 05's My Final Decision.
    if s05_row and s05_row.get('My Final Decision'):
        s05_status = str(s05_row['My Final Decision']).strip().lower()
    else:
        s05_status = 'pending'
    status = {
        '04-title-screening':      s04_status,
        '05-abstract-screening':   s05_status,
        '06-full-text-screening':  'pending',
        '07-taxonomy-development': 'pending',
        '08-analysis':             'pending',
    }

    # Stage 04 screening mirror.
    s04_machine = (corpus_row or {}).get('04.machine_decision')
    s04_human = (corpus_row or {}).get('04.human_decision')
    s04_my_just = (s04_row or {}).get('My Justification') or ''
    s04_screening = {
        'last_iteration':         0,
        'proposed_decision':      CAP.get(s04_machine),
        'proposed_justification': (s04_row or {}).get('Explanation Sub-Agent 1') or 'Migrated from legacy v2.',
        'winning_category':       None,
        'overrides_applied':      [],
        'my_final_decision':      CAP.get(s04_human),
        'my_justification':       s04_my_just,
        'agrees_with_regex':      (s04_machine == s04_human) if s04_machine and s04_human else None,
        'divergence_reason':      None,
        'locked_at_iteration':    'iter-0',
        'locked_at':              MIGRATION_TS,
    }

    # Stage 05 screening mirror (only for the 572 in aba 05).
    if s05_row:
        s05_auto = (s05_row.get('Auto Decision') or '').strip()
        s05_my = (s05_row.get('My Final Decision') or '').strip()
        overrides, _ = parse_evidence_to_overrides(s05_row.get('Evidence'))
        s05_screening = {
            'last_iteration':         0,
            'proposed_decision':      s05_auto or None,
            'proposed_justification': s05_row.get('Auto Justification') or '',
            'winning_category':       s05_row.get('Winning Category'),
            'overrides_applied':      overrides,
            'my_final_decision':      s05_my or None,
            'my_justification':       s05_row.get('My Justification') or '',
            'agrees_with_regex':      (s05_auto == s05_my) if s05_auto and s05_my else None,
            'divergence_reason':      None,
            'locked_at_iteration':    'iter-0',
            'locked_at':              MIGRATION_TS,
        }
    else:
        # Stage 05 was never run for this paper.
        s05_screening = {
            'last_iteration':         0,
            'proposed_decision':      None,
            'proposed_justification': None,
            'winning_category':       None,
            'overrides_applied':      [],
            'my_final_decision':      None,
            'my_justification':       None,
            'agrees_with_regex':      None,
            'divergence_reason':      None,
            'locked_at_iteration':    None,
            'locked_at':              None,
        }

    s06_screening = {
        'last_iteration':         0,
        'proposed_decision':      None,
        'proposed_justification': None,
        'winning_category':       None,
        'overrides_applied':      [],
        'my_final_decision':      None,
        'my_justification':       None,
        'agrees_with_regex':      None,
        'divergence_reason':      None,
        'locked_at_iteration':    None,
        'locked_at':              None,
    }

    fm = {
        'id':         pid,
        'title':      legacy_fm.get('title', ''),
        'authors':    parse_authors(legacy_fm.get('authors')),
        'venue':      legacy_fm.get('venue', ''),
        'venue_type': legacy_fm.get('venue_type', ''),
        'year':       int(legacy_fm['year']) if str(legacy_fm.get('year', '')).isdigit() else legacy_fm.get('year'),
        'doi':        legacy_fm.get('doi', ''),
        'url':        legacy_fm.get('url', ''),
        'publisher':  legacy_fm.get('publisher', ''),
        'pages':      legacy_fm.get('pages', ''),
        'keywords':   parse_keywords(legacy_fm.get('keywords')),
        'language':   legacy_fm.get('language', ''),
        'source':     legacy_fm.get('source', {'databases': [], 'exports': [], 'imported_at': '', 'dedup': {'merged_from': [], 'merge_reason': ''}}),
        'status':     status,
        'screening': {
            '04-title-screening':     s04_screening,
            '05-abstract-screening':  s05_screening,
            '06-full-text-screening': s06_screening,
        },
        'taxonomy': {},
    }
    return fm


def render_frontmatter(fm: dict) -> str:
    """YAML-dumps the frontmatter with the v3 key order preserved."""
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=200)


def render_iter0_block(stage: str, screening: dict, evidence_trail: list) -> str:
    """Renders the `### iter-0 (migrated from legacy)` body block for a stage."""
    lines = []
    lines.append('### iter-0 (migrated from legacy)')
    lines.append('')
    lines.append(f"- **regex_decision:** {screening['proposed_decision']}")
    lines.append(f"- **regex_justification:** \"{screening['proposed_justification']}\"")
    lines.append(f"- **winning_category:** {screening['winning_category']!r}")
    lines.append(f"- **overrides_applied:** {screening['overrides_applied']}")
    lines.append('- **evidence_trail:**')
    if evidence_trail:
        for e in evidence_trail:
            lines.append(f"  - `{{ category: {e['category']}, pattern_id: {e['pattern_id']}, matched_substring: \"{e['matched_substring']}\" }}`")
    else:
        lines.append('  - _(not preserved from legacy)_')
    lines.append(f"- **llm_decision:** {screening['proposed_decision']}")
    lines.append(f"- **llm_justification:** \"Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents.\"")
    lines.append(f"- **agrees_with_regex:** {screening['agrees_with_regex']}")
    lines.append(f"- **divergence_reason:** {screening['divergence_reason']}")
    lines.append('- **model:** legacy-v2')
    lines.append(f"- **timestamp:** {MIGRATION_TS}")
    return '\n'.join(lines)


def render_final_block(screening: dict) -> str:
    """Renders the `### final` body block for a stage."""
    lines = [
        '### final',
        '',
        f"- **my_final_decision:** {screening['my_final_decision']}",
        f"- **my_justification:** \"{screening['my_justification']}\"",
        f"- **locked_at_iteration:** {screening['locked_at_iteration']}",
        f"- **locked_at:** {screening['locked_at']}",
    ]
    return '\n'.join(lines)


def render_paper(pid: str, legacy_fm: dict, abstract_text: str, corpus_row: Optional[dict], s04_row: Optional[dict], s05_row: Optional[dict]) -> str:
    """Builds the full v3 markdown for one paper."""
    fm = build_frontmatter(pid, legacy_fm, corpus_row, s04_row, s05_row)
    title = fm['title']
    body_parts = []

    body_parts.append(f'# {pid} — {title}')
    body_parts.append('')
    body_parts.append('## Metadata (from `/03-parse-references-metadata`)')
    body_parts.append('')
    body_parts.append('Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.')
    body_parts.append('')
    body_parts.append('**Abstract**')
    body_parts.append('')
    body_parts.append(f'> {abstract_text}' if abstract_text else '> _(abstract not available)_')
    body_parts.append('')
    body_parts.append('**Dedup notes**')
    body_parts.append('')
    merged = (legacy_fm.get('source') or {}).get('dedup', {}).get('merged_from') or []
    body_parts.append('no duplicates found' if not merged else f'merged from: {merged}')

    # Stage 04 — always backfilled.
    body_parts.append('')
    body_parts.append('---')
    body_parts.append('')
    body_parts.append('## 04 — Title Screening')
    body_parts.append('')
    s04 = fm['screening']['04-title-screening']
    body_parts.append(render_iter0_block('04', s04, []))
    body_parts.append('')
    body_parts.append(render_final_block(s04))

    # Stage 05 — only when the paper went through abstract screening.
    body_parts.append('')
    body_parts.append('---')
    body_parts.append('')
    body_parts.append('## 05 — Abstract Screening')
    body_parts.append('')
    if s05_row:
        s05 = fm['screening']['05-abstract-screening']
        _, evidence_trail = parse_evidence_to_overrides(s05_row.get('Evidence'))
        body_parts.append(render_iter0_block('05', s05, evidence_trail))
        body_parts.append('')
        body_parts.append(render_final_block(s05))
    else:
        body_parts.append('_(stage 05 not run for this paper — excluded at title screening)_')

    # Stages 06/07/08 placeholders.
    body_parts.append('')
    body_parts.append('---')
    body_parts.append('')
    body_parts.append('## 06 — Full-Text Screening')
    body_parts.append('')
    body_parts.append(f'_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/{pid}.pdf`)_')
    body_parts.append('')
    body_parts.append('---')
    body_parts.append('')
    body_parts.append('## 07 — Taxonomy')
    body_parts.append('')
    body_parts.append('_(populated by `/05-code-taxonomy` after stage 06 lock.)_')
    body_parts.append('')
    body_parts.append('---')
    body_parts.append('')
    body_parts.append('## 08 — Analysis contributions')
    body_parts.append('')
    body_parts.append('_(populated by `/06-analyze` after taxonomy lock.)_')
    body_parts.append('')

    body = '\n'.join(body_parts)
    return f'---\n{render_frontmatter(fm)}---\n\n{body}'


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--sample', nargs='+', help='Paper IDs to backfill (paper-NNNN)')
    g.add_argument('--all', action='store_true', help='Backfill every paper-NNNN found')
    args = ap.parse_args()

    indexes = load_xlsx_indexes()
    print(f'loaded indexes: corpus={len(indexes["corpus"])}, s04={len(indexes["s04"])}, s05={len(indexes["s05"])}')

    if args.all:
        targets = sorted(indexes['corpus'].keys())
    else:
        targets = args.sample

    written = 0
    skipped = 0
    for pid in targets:
        # Map paper-NNNN -> legacy paper-NNN name (strip leading zeros from the digits).
        m = re.match(r'^paper-(\d{4})$', pid)
        if not m:
            print(f'  skip (bad id): {pid}')
            skipped += 1
            continue
        legacy_n = int(m.group(1))
        legacy_path = LEGACY_PAPERS / f'paper-{legacy_n:03d}.md'
        if not legacy_path.exists():
            # Fallback: try any width.
            for cand in [f'paper-{legacy_n:04d}.md', f'paper-{legacy_n}.md']:
                p = LEGACY_PAPERS / cand
                if p.exists():
                    legacy_path = p
                    break
        if not legacy_path.exists():
            print(f'  skip (no legacy file for {pid}): looked for paper-{legacy_n:03d}.md')
            skipped += 1
            continue

        legacy_fm, body = extract_legacy_frontmatter(legacy_path)
        abstract_text = extract_abstract(body)
        corpus_row = indexes['corpus'].get(pid)
        s04_row = indexes['s04'].get(pid)
        s05_row = indexes['s05'].get(pid)

        text = render_paper(pid, legacy_fm, abstract_text, corpus_row, s04_row, s05_row)
        out_path = OUT_DIR / f'{pid}.md'
        out_path.write_text(text)
        written += 1

    print(f'written: {written}, skipped: {skipped}')


if __name__ == '__main__':
    main()
