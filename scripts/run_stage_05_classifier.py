"""Runs the deterministic classifier over abstract texts of stage-04-included papers.

Reads `papers/paper-NNN.md` files where `status["04-title-screening"] == include`,
extracts title + abstract, applies the abstract-stage classifier, and writes
JSON output. Papers that produce `winning_category == "no_signal"` are listed
separately as candidates for the LLM tiebreaker.

This script is read-only against the corpus. It does NOT write decisions back to
paper files or to the spreadsheet — that is `apply_decisions_to_spreadsheet.py`'s job.
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
from deterministic_classifier import classify, load_config


def extract_title_and_abstract(content: str) -> tuple[str, str]:
    """Pulls the title from frontmatter and the abstract from the body.

    Args:
        content (str): Raw paper-NNN.md file content.

    Returns:
        title (str): Title string (empty if not found).
        abstract (str): Abstract string (empty if not found).
    """
    title_match = re.search(pattern=r'^title:\s*"(.+?)"', string=content, flags=re.MULTILINE)
    title = title_match.group(1) if title_match else ""
    abstract_match = re.search(
        pattern=r'###\s*Abstract\s*\n+(.+?)(?=\n###|\n##|\Z)',
        string=content,
        flags=re.DOTALL,
    )
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    return title, abstract


def is_stage_04_include(content: str) -> bool:
    """Checks whether a paper file has stage-04 status include."""
    return '"04-title-screening": include' in content


def run_classifier_on_corpus(papers_dir: Path, config: dict) -> list[dict]:
    """Applies the classifier to every stage-04-included paper.

    Args:
        papers_dir (Path): Directory with paper-NNN.md files.
        config (dict): Compiled classifier config.

    Returns:
        decisions (list[dict]): One dict per paper with id, title, abstract, classifier output.
    """
    decisions = []
    for path in sorted(papers_dir.glob("paper-[0-9]*.md")):
        content = path.read_text(encoding="utf-8")
        if not is_stage_04_include(content=content):
            continue
        title, abstract = extract_title_and_abstract(content=content)
        classified_text = f"{title}\n\n{abstract}"
        result = classify(text=classified_text, config=config)
        decisions.append({
            "paper_id": path.stem,
            "title": title,
            "abstract_preview": abstract[:200],
            "decision": result["decision"],
            "justification": result["justification"],
            "winning_category": result["winning_category"],
            "evidence": [
                {"category": m["category"], "pattern_id": m["pattern_id"], "matched_text": m["matched_text"][:80]}
                for m in result["evidence"][:8]
            ],
            "needs_tiebreaker": result["winning_category"] == "no_signal",
        })
    return decisions


def write_outputs(decisions: list[dict], out_dir: Path) -> dict:
    """Persists classifier output and prints a distribution summary.

    Args:
        decisions (list[dict]): Output of run_classifier_on_corpus.
        out_dir (Path): Directory to write JSON files into.

    Returns:
        summary (dict): Distribution by winning category and needs-tiebreaker count.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    out_dir.joinpath("classifier-decisions.json").write_text(
        json.dumps(decisions, indent=2, ensure_ascii=False), encoding="utf-8",
    )
    no_match = [d for d in decisions if d["needs_tiebreaker"]]
    out_dir.joinpath("no-match-papers.json").write_text(
        json.dumps(no_match, indent=2, ensure_ascii=False), encoding="utf-8",
    )
    distribution = Counter(d["winning_category"] for d in decisions)
    decision_dist = Counter(d["decision"] for d in decisions)
    summary = {
        "total_papers": len(decisions),
        "by_winning_category": dict(distribution.most_common()),
        "by_decision": dict(decision_dist),
        "needs_tiebreaker": len(no_match),
    }
    return summary


def main(papers_dir: str, config_path: str, out_dir: str) -> None:
    config = load_config(path=config_path)
    decisions = run_classifier_on_corpus(papers_dir=Path(papers_dir), config=config)
    summary = write_outputs(decisions=decisions, out_dir=Path(out_dir))
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--papers-dir", default="papers")
    parser.add_argument("--config", default="protocols/classifier-config-abstract.json")
    parser.add_argument("--out-dir", default="screening/abstract")
    args = parser.parse_args()
    main(papers_dir=args.papers_dir, config_path=args.config, out_dir=args.out_dir)
