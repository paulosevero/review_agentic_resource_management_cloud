"""Parse raw/exports/*.bib files, deduplicate records, and materialize papers/paper-NNN.md.

Approach:
  1. Load all BibTeX files with bibtexparser.
  2. Normalize fields to a canonical schema.
  3. Deduplicate: DOI match first, then title+year+first-author, then title+year.
  4. Assign stable IDs (paper-001, paper-002, ...) in import order after dedup.
  5. Render each unique record to papers/paper-NNN.md using the template.

Outputs:
  - papers/paper-NNN.md for every unique record
  - stages/03-parse-references-metadata.md with import summary and dedup log
"""

import argparse
import json
import os
import re
import unicodedata
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORTS_DIR = REPO_ROOT / "raw" / "exports"
PAPERS_DIR = REPO_ROOT / "papers"
TEMPLATE_PATH = REPO_ROOT / "plugin" / "templates" / "paper.md.template"
STAGE_LOG_PATH = REPO_ROOT / "stages" / "03-parse-references-metadata.md"


def normalize_str(text: str) -> str:
    """Normalize a string for fuzzy matching: lowercase, strip accents, collapse whitespace."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def first_author_surname(authors_raw: str) -> str:
    """Extract the normalized surname of the first author from a raw authors string."""
    if not authors_raw:
        return ""
    first = authors_raw.split(" and ")[0].strip()
    # Scopus format: "Surname, Firstname" or "Firstname Surname"
    if "," in first:
        surname = first.split(",")[0].strip()
    else:
        parts = first.split()
        surname = parts[-1] if parts else ""
    return normalize_str(surname)


def parse_list_field(raw: str) -> list[str]:
    """Split a semicolon- or comma-separated field into a list of stripped strings."""
    if not raw:
        return []
    separators = r"[;]"
    items = re.split(separators, raw)
    return [item.strip() for item in items if item.strip()]


def parse_authors(raw: str) -> list[str]:
    """Split a BibTeX author string (separated by ' and ') into a list."""
    if not raw:
        return []
    return [a.strip() for a in raw.split(" and ") if a.strip()]


def detect_venue_type(entry_type: str, type_field: str) -> str:
    """Infer venue_type from BibTeX entry type and Scopus 'type' field."""
    entry_type = (entry_type or "").lower()
    type_field = (type_field or "").lower()
    if "conference" in entry_type or "inproceedings" in entry_type:
        return "conference"
    if "book" in entry_type and "chapter" not in type_field:
        return "book"
    if "chapter" in type_field:
        return "book_chapter"
    if "review" in type_field and "conference" in type_field:
        return "conference_proceedings_book"
    if "conference" in type_field:
        return "conference"
    return "journal"


def normalize_record(entry: dict, source_file: str) -> dict:
    """Normalize a raw bibtexparser v1 entry (plain dict) to the canonical schema."""
    def get(key: str) -> str:
        val = entry.get(key, "")
        return str(val).strip() if val else ""

    title = get("title")
    year_raw = get("year")
    try:
        year = int(year_raw)
    except ValueError:
        year = 0

    venue = get("journal") or get("booktitle") or get("series") or ""
    entry_type = entry.get("ENTRYTYPE", "article")
    type_field = get("type")
    venue_type = detect_venue_type(entry_type, type_field)

    authors_raw = get("author")
    authors = parse_authors(authors_raw)
    doi = get("doi")
    url = get("url")
    publisher = get("publisher")
    pages = get("pages")
    keywords_raw = get("author_keywords") or get("keywords") or ""
    keywords = parse_list_field(keywords_raw)
    abstract = get("abstract")
    language = get("language") or "English"
    # Strip braces that bibtexparser v1 leaves in some fields
    title = title.strip("{}")
    abstract = abstract.strip("{}")

    return {
        "title": title,
        "title_norm": normalize_str(title),
        "authors": authors,
        "first_author_surname": first_author_surname(authors_raw),
        "year": year,
        "venue": venue,
        "venue_type": venue_type,
        "doi": doi.lower().strip() if doi else "",
        "url": url,
        "publisher": publisher,
        "pages": pages,
        "keywords": keywords,
        "abstract": abstract,
        "language": language,
        "source": {
            "databases": ["Scopus"],
            "exports": [source_file],
        },
        "dedup": {
            "merged_from": [],
            "merge_reason": "",
        },
    }


def record_completeness(record: dict) -> int:
    """Score how complete a record's metadata is (higher = more fields filled)."""
    score = 0
    for field in ["doi", "abstract", "authors", "venue", "publisher", "pages", "keywords", "url"]:
        val = record.get(field)
        if val:
            score += 1
    return score


def merge_into_winner(winner: dict, loser: dict, reason: str) -> None:
    """Merge loser into winner: fill blanks and record in dedup log."""
    for field in ["doi", "url", "abstract", "venue", "publisher", "pages", "language"]:
        if not winner.get(field) and loser.get(field):
            winner[field] = loser[field]
    # Merge keywords
    winner_kws = set(winner.get("keywords", []))
    winner_kws.update(loser.get("keywords", []))
    winner["keywords"] = sorted(winner_kws)
    # Merge source exports
    for exp in loser["source"]["exports"]:
        if exp not in winner["source"]["exports"]:
            winner["source"]["exports"].append(exp)
    # Record merge
    winner["dedup"]["merged_from"].append({
        "title": loser["title"],
        "doi": loser["doi"],
        "reason": reason,
    })


def deduplicate(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Deduplicate records. Returns (unique_records, merge_log_entries)."""
    unique: list[dict] = []
    merge_log: list[dict] = []

    # Index structures for fast lookup
    doi_index: dict[str, int] = {}        # doi -> index in unique
    title_year_author_index: dict[tuple, int] = {}
    title_year_index: dict[tuple, int] = {}

    for record in records:
        doi = record["doi"]
        title_norm = record["title_norm"]
        year = record["year"]
        surname = record["first_author_surname"]
        tya_key = (title_norm, year, surname)
        ty_key = (title_norm, year)

        matched_idx = None
        merge_reason = ""

        if doi and doi in doi_index:
            matched_idx = doi_index[doi]
            merge_reason = "same_doi"
        elif surname and tya_key in title_year_author_index:
            matched_idx = title_year_author_index[tya_key]
            merge_reason = "same_title_year_first_author"
        elif ty_key in title_year_index:
            matched_idx = title_year_index[ty_key]
            merge_reason = "same_title_year"

        if matched_idx is not None:
            winner = unique[matched_idx]
            loser_completeness = record_completeness(record)
            winner_completeness = record_completeness(winner)
            if loser_completeness > winner_completeness:
                # Swap: loser becomes winner, old winner becomes loser
                merge_into_winner(record, winner, merge_reason + "_swapped")
                # Carry over existing merged_from
                record["dedup"]["merged_from"].extend(winner["dedup"]["merged_from"])
                record["dedup"]["merge_reason"] = winner.get("dedup", {}).get("merge_reason", "")
                unique[matched_idx] = record
                # Update indexes
                if doi:
                    doi_index[doi] = matched_idx
                if surname:
                    title_year_author_index[tya_key] = matched_idx
                title_year_index[ty_key] = matched_idx
                merge_log.append({"winner": record["title"], "loser": winner["title"], "reason": merge_reason})
            else:
                merge_into_winner(winner, record, merge_reason)
                merge_log.append({"winner": winner["title"], "loser": record["title"], "reason": merge_reason})
        else:
            idx = len(unique)
            unique.append(record)
            if doi:
                doi_index[doi] = idx
            if surname:
                title_year_author_index[tya_key] = idx
            title_year_index[ty_key] = idx

    return unique, merge_log


def render_paper(record: dict, paper_id: str, template: str) -> str:
    """Render a paper markdown from the template."""
    authors_yaml = json.dumps(record["authors"], ensure_ascii=False)
    keywords_yaml = json.dumps(record["keywords"], ensure_ascii=False)
    databases_yaml = json.dumps(record["source"]["databases"], ensure_ascii=False)
    exports_yaml = json.dumps(record["source"]["exports"], ensure_ascii=False)
    merged_from_yaml = json.dumps(record["dedup"]["merged_from"], ensure_ascii=False)

    # Build metadata body
    abstract_text = record.get("abstract", "").strip()
    dedup_notes = ""
    if record["dedup"]["merged_from"]:
        merged_titles = [m["title"] for m in record["dedup"]["merged_from"]]
        dedup_notes = f"\n\n**Dedup:** Merged {len(merged_titles)} duplicate(s): {'; '.join(merged_titles[:3])}{'...' if len(merged_titles) > 3 else ''}."

    if abstract_text:
        metadata_body = f"**Abstract:** {abstract_text}{dedup_notes}"
    else:
        metadata_body = f"Abstract not available in export. Requires manual retrieval before stage 05.{dedup_notes}"

    rendered = template
    rendered = rendered.replace("{{id}}", paper_id)
    rendered = rendered.replace("{{title}}", record["title"].replace('"', '\\"'))
    rendered = rendered.replace("{{authors}}", authors_yaml)
    rendered = rendered.replace("{{year}}", str(record["year"]))
    rendered = rendered.replace("{{venue}}", record["venue"].replace('"', '\\"'))
    rendered = rendered.replace("{{venue_type}}", record["venue_type"])
    rendered = rendered.replace("{{doi}}", record["doi"])
    rendered = rendered.replace("{{url}}", record["url"])
    rendered = rendered.replace("{{publisher}}", record["publisher"].replace('"', '\\"'))
    rendered = rendered.replace("{{pages}}", record["pages"])
    rendered = rendered.replace("{{keywords}}", keywords_yaml)
    rendered = rendered.replace("{{language}}", record["language"])
    rendered = rendered.replace("{{source_databases}}", databases_yaml)
    rendered = rendered.replace("{{source_exports}}", exports_yaml)
    rendered = rendered.replace("{{dedup_merged_from}}", merged_from_yaml)
    rendered = rendered.replace("{{dedup_merge_reason}}", record["dedup"]["merge_reason"])
    rendered = rendered.replace("{{metadata_body}}", metadata_body)
    return rendered


def write_stage_log(
    total_raw: int,
    total_unique: int,
    merge_log: list[dict],
    missing_abstract: list[str],
    source_file: str,
    search_date: str,
) -> None:
    """Write the stage 03 log to stages/03-parse-references-metadata.md."""
    duplicates = total_raw - total_unique
    lines = [
        "# Stage 03 — Parse References Metadata",
        "",
        "## Import Summary",
        "",
        f"- **Search date:** {search_date}",
        f"- **Source file:** {source_file}",
        f"- **Database:** Scopus",
        f"- **Total records in export:** {total_raw}",
        f"- **Duplicates merged:** {duplicates}",
        f"- **Unique papers materialized:** {total_unique}",
        "",
        "## Dedup Log",
        "",
    ]
    if merge_log:
        lines.append(f"Total merge events: {len(merge_log)}")
        lines.append("")
        for i, event in enumerate(merge_log[:100], 1):
            reason = event["reason"].replace("_", " ")
            lines.append(f"{i}. [{reason}] Winner: \"{event['winner'][:80]}\" | Loser: \"{event['loser'][:80]}\"")
        if len(merge_log) > 100:
            lines.append(f"... and {len(merge_log) - 100} more merge events (truncated for readability).")
    else:
        lines.append("No duplicates found.")

    lines += [
        "",
        "## Papers Missing Abstract",
        "",
    ]
    if missing_abstract:
        lines.append(f"The following {len(missing_abstract)} papers have no abstract in the export.")
        lines.append("They carry `status.05-abstract-screening: pending` and must be resolved manually")
        lines.append("(retrieve abstract or route directly to stage 06).")
        lines.append("")
        for pid in missing_abstract:
            lines.append(f"- {pid}")
    else:
        lines.append("All papers have abstracts.")

    STAGE_LOG_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(search_date: str) -> None:
    """Parse exports, deduplicate, and materialize paper markdown files."""
    bib_files = sorted(EXPORTS_DIR.glob("*.bib"))
    ris_files = sorted(EXPORTS_DIR.glob("*.ris"))
    csv_files = sorted(EXPORTS_DIR.glob("*.csv"))

    all_records: list[dict] = []
    source_files: list[str] = []

    # Parsing BibTeX files
    try:
        import bibtexparser
        from bibtexparser.middlewares.names import SeparateCoAuthors, MergeCoAuthors
    except ImportError:
        print("ERROR: bibtexparser not installed. Run: pip install bibtexparser")
        return

    for bib_path in bib_files:
        print(f"Parsing {bib_path.name} ...")
        library = bibtexparser.parse_file(str(bib_path))
        records_before = len(all_records)
        for entry in library.entries:
            # Build fields_dict from entry
            entry_dict = {
                "type": entry.type,
                "fields_dict": {field.key: field for field in entry.fields},
            }
            record = normalize_record(entry_dict, bib_path.name)
            all_records.append(record)
        count = len(all_records) - records_before
        source_files.append(bib_path.name)
        print(f"  -> {count} records loaded from {bib_path.name}")

    total_raw = len(all_records)
    print(f"\nTotal raw records: {total_raw}")

    print("Deduplicating ...")
    unique_records, merge_log = deduplicate(all_records)
    total_unique = len(unique_records)
    duplicates = total_raw - total_unique
    print(f"  -> {duplicates} duplicates merged, {total_unique} unique records remain")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    PAPERS_DIR.mkdir(exist_ok=True)

    missing_abstract: list[str] = []

    print("Materializing paper files ...")
    for i, record in enumerate(unique_records, 1):
        paper_id = f"paper-{i:03d}"
        paper_path = PAPERS_DIR / f"{paper_id}.md"
        content = render_paper(record, paper_id, template)
        paper_path.write_text(content, encoding="utf-8")
        if not record.get("abstract"):
            missing_abstract.append(paper_id)

    print(f"  -> {total_unique} files written to papers/")

    source_file_display = ", ".join(source_files) if source_files else "unknown"
    write_stage_log(
        total_raw=total_raw,
        total_unique=total_unique,
        merge_log=merge_log,
        missing_abstract=missing_abstract,
        source_file=source_file_display,
        search_date=search_date,
    )
    print(f"  -> Stage log written to stages/03-parse-references-metadata.md")
    print(f"\nDone. {total_unique} papers, {duplicates} duplicates, {len(missing_abstract)} missing abstracts.")
    print(f"missing_abstract_count={len(missing_abstract)}")
    print(f"total_raw={total_raw}")
    print(f"total_unique={total_unique}")
    print(f"duplicates={duplicates}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse BibTeX exports and materialize paper markdowns.")
    parser.add_argument("--search-date", required=True, help="Date the database search was executed (YYYY-MM-DD)")
    args = parser.parse_args()
    main(search_date=args.search_date)
