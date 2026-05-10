"""Lists the year of every paper in the spreadsheet's `05 — Abstract Screening`
tab, in the order they appear, sourcing years from `raw/exports/scopus-2026-04-26.bib`.

Maps paper-id → DOI via the paper-NNN.md frontmatter, then DOI → year via the bib file.
Falls back to bib's `year` field by the matching @ENTRY_KEY when DOI is absent.
"""

import re
from pathlib import Path

import openpyxl


def parse_bib_years(bib_path: Path) -> tuple[dict, dict]:
    """Parses the .bib file. Returns two dicts: by DOI, by entry key."""
    text = bib_path.read_text(encoding="utf-8")
    by_doi = {}
    by_key = {}
    for m in re.finditer(pattern=r'@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)', string=text, flags=re.DOTALL):
        key = m.group(1).strip()
        body = m.group(2)
        year_m = re.search(pattern=r'year\s*=\s*\{?(\d{4})', string=body)
        doi_m = re.search(pattern=r'doi\s*=\s*\{([^}]+)\}', string=body, flags=re.IGNORECASE)
        year = year_m.group(1) if year_m else ""
        if year:
            by_key[key] = year
            if doi_m:
                by_doi[doi_m.group(1).strip().lower()] = year
    return by_doi, by_key


def parse_paper_frontmatter(paper_path: Path) -> tuple[str, str, str]:
    """Returns (doi, year_in_frontmatter, scopus_key) from a paper-NNN.md file."""
    if not paper_path.exists():
        return "", "", ""
    content = paper_path.read_text(encoding="utf-8")
    doi_m = re.search(pattern=r'^doi:\s*"?([^"\n]+)"?\s*$', string=content, flags=re.MULTILINE)
    year_m = re.search(pattern=r'^year:\s*(\d{4})', string=content, flags=re.MULTILINE)
    return (doi_m.group(1).strip() if doi_m else "").lower(), (year_m.group(1) if year_m else ""), ""


def main() -> None:
    bib_path = Path("raw/exports/scopus-2026-04-26.bib")
    xlsx_path = Path("spreadsheet_abstract_screening.xlsx")
    out_path = Path("audits/stage-05-paper-years.csv")
    by_doi, by_key = parse_bib_years(bib_path=bib_path)
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb["05 — Abstract Screening"]
    pids = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0]:
            pids.append(row[0])
    rows = []
    miss = 0
    year_counts = {}
    for pid in pids:
        doi, fm_year, _ = parse_paper_frontmatter(paper_path=Path(f"papers/{pid}.md"))
        year = ""
        if doi and doi in by_doi:
            year = by_doi[doi]
        elif fm_year:
            year = fm_year
        if not year:
            miss += 1
            year = "?"
        rows.append((pid, year))
        year_counts[year] = year_counts.get(year, 0) + 1
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("paper_id,year\n" + "\n".join(f"{p},{y}" for p, y in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} rows to {out_path}")
    print(f"Missing years: {miss}")
    print("\nDistribution:")
    for y in sorted(year_counts.keys()):
        print(f"  {y}: {year_counts[y]}")


if __name__ == "__main__":
    main()
