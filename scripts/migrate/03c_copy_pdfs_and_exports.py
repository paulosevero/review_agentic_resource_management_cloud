"""Copy PDFs, fulltext MDs, and Scopus exports from legacy/ to v3 layout.

Mapping:
- legacy/raw/pdfs/[paper-NNNN] <title>.pdf -> raw/pdfs/paper-NNNN.pdf
- legacy/raw/pdfs/[paper-NNNN] <title>.md  -> papers/paper-NNNN.fulltext.md
- legacy/raw/exports/*.bib                  -> raw/exports/<basename>

Idempotent: re-running overwrites destinations with the same source bytes.
"""

import re
import shutil
from pathlib import Path

REPO = Path('/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud')
LEGACY_PDFS = REPO / 'legacy/raw/pdfs'
LEGACY_EXPORTS = REPO / 'legacy/raw/exports'
OUT_PDFS = REPO / 'raw/pdfs'
OUT_PAPERS = REPO / 'papers'
OUT_EXPORTS = REPO / 'raw/exports'

ID_RE = re.compile(r'^\[(paper-\d{4})\]')


def main():
    pdf_count = 0
    md_count = 0
    for entry in sorted(LEGACY_PDFS.iterdir()):
        if not entry.is_file():
            continue
        m = ID_RE.match(entry.name)
        if not m:
            print(f'  skip (no id): {entry.name}')
            continue
        pid = m.group(1)
        if entry.suffix == '.pdf':
            dst = OUT_PDFS / f'{pid}.pdf'
            shutil.copy2(entry, dst)
            pdf_count += 1
        elif entry.suffix == '.md':
            dst = OUT_PAPERS / f'{pid}.fulltext.md'
            shutil.copy2(entry, dst)
            md_count += 1

    bib_count = 0
    for bib in sorted(LEGACY_EXPORTS.glob('*.bib')):
        dst = OUT_EXPORTS / bib.name
        shutil.copy2(bib, dst)
        bib_count += 1

    print(f'PDFs copied:        {pdf_count}')
    print(f'fulltext MDs copied:{md_count}')
    print(f'bib exports copied: {bib_count}')


if __name__ == '__main__':
    main()
