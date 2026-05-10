#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Deterministic regex-based classifier for screening stages 04/05/06.

Pure function over (paper input, classifier config): given the same inputs and
the same `protocols/classifier-config.json`, produces byte-identical output on
any machine. No system time, no random seeds, no environment variables, no
network, no file order. The order of evaluation is exactly `priority_order`.

This script is pass 1 of the two-pass screening pipeline; pass 2 is the LLM
reviewer (`agents/_screening-llm-reviewer.md`). The output of this script
populates the `Proposed Decision`, `Proposed Justification`, `Evidence Trail`,
`Winning Category`, and `Overrides Applied` columns of the spreadsheet.

CLI:
    uv run scripts/deterministic_classifier.py \
        --stage {title|abstract|full_text} \
        --config protocols/classifier-config.json \
        --papers papers-input.json \
        --out screening/<stage>/proposed.json \
        [--skip-paper-ids paper-0001,paper-0042]

Self-test:
    uv run scripts/deterministic_classifier.py --self-test
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STAGE_FIELDS = {
    "title": ("title",),
    "abstract": ("title", "abstract", "keywords"),
    "full_text": ("title", "abstract", "keywords", "full_text_sections"),
}


def build_input_string(*, paper: dict[str, Any], stage: str) -> str:
    """Concatenates the stage-allowed fields of a paper into a single string for matching.

    Args:
        paper (dict): Paper input object with optional `title`, `abstract`, `keywords`, `full_text_sections`.
        stage (str): One of `title`, `abstract`, `full_text`.

    Returns:
        input_string (str): The concatenated text used for regex matching.
    """
    if stage not in STAGE_FIELDS:
        raise ValueError(f"Unknown stage: {stage}")
    fields = STAGE_FIELDS[stage]
    parts: list[str] = []
    for field in fields:
        value = paper.get(field)
        if value is None:
            continue
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, list):
            parts.append(" ".join(str(item) for item in value))
        elif isinstance(value, dict):
            parts.append(" ".join(f"{k}: {v}" for k, v in value.items()))
        else:
            parts.append(str(value))
    input_string = " \n ".join(parts)
    return input_string


def compile_regex(*, regex: str, owner: str) -> re.Pattern[str]:
    """Compiles a regex string under re.IGNORECASE, raising a fatal error with the offender id.

    Args:
        regex (str): The regex source.
        owner (str): Identifier of the regex owner (pattern_id or override.id), reported on failure.

    Returns:
        compiled (re.Pattern): Compiled pattern.
    """
    try:
        compiled = re.compile(regex, re.IGNORECASE)
    except re.error as exc:
        raise ValueError(f"Regex compilation failed for '{owner}': {exc}") from exc
    return compiled


def strip_leading_punctuation(*, text: str) -> str:
    """Removes a leading ':\\s*' from a matched substring so the user-facing span is clean.

    Args:
        text (str): The raw matched substring.

    Returns:
        cleaned (str): The substring with leading colon and whitespace stripped.
    """
    cleaned = re.sub(r"^:\s*", "", text)
    return cleaned


def find_pattern_matches(*, pattern: dict[str, Any], compiled: re.Pattern[str], input_string: str, category_id: str, stage: str) -> list[dict[str, Any]]:
    """Collects all matches of a single pattern against the input string.

    Args:
        pattern (dict): Pattern object from the config.
        compiled (re.Pattern): Pre-compiled regex for this pattern.
        input_string (str): The paper input string.
        category_id (str): The owning category id.
        stage (str): Current screening stage.

    Returns:
        matches (list): Evidence entries with category/pattern_id/matched_substring/position.
    """
    applicable = pattern.get("applicable_stages")
    if applicable is not None and stage not in applicable:
        return []
    matches: list[dict[str, Any]] = []
    for match in compiled.finditer(input_string):
        raw_substring = match.group(0)
        cleaned = strip_leading_punctuation(text=raw_substring)
        offset = raw_substring.find(cleaned) if cleaned else 0
        start = match.start() + offset
        end = start + len(cleaned)
        matches.append({
            "category": category_id,
            "pattern_id": pattern["id"],
            "matched_substring": cleaned,
            "position": [start, end],
        })
    return matches


def evaluate_category(*, category: dict[str, Any], compiled_patterns: dict[str, re.Pattern[str]], compiled_overrides: dict[str, re.Pattern[str]], input_string: str, stage: str) -> tuple[list[dict[str, Any]], list[str]]:
    """Evaluates one category against the input, collecting pattern matches and override hits.

    Args:
        category (dict): Category object.
        compiled_patterns (dict): Map of pattern_id → compiled regex for this category.
        compiled_overrides (dict): Map of override.id → compiled regex for this category.
        input_string (str): Paper input string.
        stage (str): Screening stage.

    Returns:
        result (tuple): (pattern_matches, override_ids_hit).
    """
    pattern_matches: list[dict[str, Any]] = []
    for pattern in category.get("patterns", []):
        compiled = compiled_patterns[pattern["id"]]
        matches = find_pattern_matches(pattern=pattern, compiled=compiled, input_string=input_string, category_id=category["id"], stage=stage)
        pattern_matches.extend(matches)
    override_ids_hit: list[str] = []
    if pattern_matches:
        for override in category.get("overrides", []):
            compiled = compiled_overrides[override["id"]]
            if compiled.search(input_string):
                override_ids_hit.append(override["id"])
    return pattern_matches, override_ids_hit


def classify_paper(*, paper: dict[str, Any], config: dict[str, Any], compiled: dict[str, dict[str, re.Pattern[str]]], stage: str) -> dict[str, Any]:
    """Classifies a single paper according to the priority order and overrides.

    Args:
        paper (dict): Paper input object with at least `paper_id`.
        config (dict): The classifier-config dict.
        compiled (dict): Pre-compiled regexes, keyed `[category_id]["patterns"|"overrides"][id]`.
        stage (str): Screening stage.

    Returns:
        result (dict): Per-paper classification with decision, justification, evidence_trail, etc.
    """
    input_string = build_input_string(paper=paper, stage=stage)
    categories_by_id = {c["id"]: c for c in config["categories"]}
    accumulated_evidence: list[dict[str, Any]] = []
    accumulated_overrides: list[str] = []
    for category_id in config["priority_order"]:
        category = categories_by_id[category_id]
        pattern_matches, override_ids_hit = evaluate_category(
            category=category,
            compiled_patterns=compiled[category_id]["patterns"],
            compiled_overrides=compiled[category_id]["overrides"],
            input_string=input_string,
            stage=stage,
        )
        accumulated_evidence.extend(pattern_matches)
        if not pattern_matches:
            continue
        if override_ids_hit:
            accumulated_overrides.extend(override_ids_hit)
            continue
        decision = "Include" if category["kind"] == "include" else "Exclude"
        return {
            "paper_id": paper["paper_id"],
            "decision": decision,
            "justification": category["justification"],
            "winning_category": category_id,
            "evidence_trail": accumulated_evidence,
            "overrides_applied": accumulated_overrides,
        }
    return {
        "paper_id": paper["paper_id"],
        "decision": config["default_decision"],
        "justification": config["default_justification"],
        "winning_category": "default",
        "evidence_trail": accumulated_evidence,
        "overrides_applied": accumulated_overrides,
    }


def precompile_config(*, config: dict[str, Any]) -> dict[str, dict[str, dict[str, re.Pattern[str]]]]:
    """Pre-compiles every regex in the config into a nested map keyed by category id.

    Args:
        config (dict): The classifier-config dict.

    Returns:
        compiled (dict): `compiled[category_id]["patterns" | "overrides"][id] = re.Pattern`.
    """
    compiled: dict[str, dict[str, dict[str, re.Pattern[str]]]] = {}
    for category in config["categories"]:
        category_compiled: dict[str, dict[str, re.Pattern[str]]] = {"patterns": {}, "overrides": {}}
        for pattern in category.get("patterns", []):
            owner = f"category={category['id']} pattern={pattern['id']}"
            category_compiled["patterns"][pattern["id"]] = compile_regex(regex=pattern["regex"], owner=owner)
        for override in category.get("overrides", []):
            owner = f"category={category['id']} override={override['id']}"
            category_compiled["overrides"][override["id"]] = compile_regex(regex=override["regex"], owner=owner)
        compiled[category["id"]] = category_compiled
    return compiled


def validate_config(*, config: dict[str, Any]) -> None:
    """Validates the structural invariants of `protocols/classifier-config.json`.

    Args:
        config (dict): The classifier-config dict.

    Returns:
        None. Raises ValueError on the first violation.
    """
    required_top = {"version", "default_decision", "default_justification", "proximity_window", "priority_order", "categories"}
    missing = required_top - set(config.keys())
    if missing:
        raise ValueError(f"Missing top-level keys: {sorted(missing)}")
    if config["proximity_window"] < 200:
        raise ValueError("proximity_window must be >= 200")
    if config["default_decision"] not in {"Include", "Exclude"}:
        raise ValueError("default_decision must be 'Include' or 'Exclude'")
    declared_ids = [c["id"] for c in config["categories"]]
    if sorted(declared_ids) != sorted(config["priority_order"]):
        raise ValueError("priority_order must list every category.id exactly once")
    has_include = any(c["kind"] == "include" for c in config["categories"])
    has_exclude = any(c["kind"] == "exclude" for c in config["categories"])
    if not (has_include and has_exclude):
        raise ValueError("At least one include category and one exclude category are required")
    for index, category_id in enumerate(config["priority_order"]):
        category = next(c for c in config["categories"] if c["id"] == category_id)
        if category.get("priority_index") != index:
            raise ValueError(f"Category '{category_id}' priority_index ({category.get('priority_index')}) does not match priority_order position ({index})")


def classify_papers(*, papers: list[dict[str, Any]], config: dict[str, Any], stage: str, skip_paper_ids: set[str]) -> list[dict[str, Any]]:
    """Classifies a batch of papers, skipping those already decided by the user.

    Args:
        papers (list): Paper input objects, each with `paper_id` plus stage-relevant fields.
        config (dict): The classifier-config dict (already validated).
        stage (str): One of `title`, `abstract`, `full_text`.
        skip_paper_ids (set): Paper ids to bypass (their `My Final Decision` is already filled).

    Returns:
        results (list): Per-paper classification objects, sorted by `paper_id` ascending.
    """
    compiled = precompile_config(config=config)
    results: list[dict[str, Any]] = []
    for paper in papers:
        if paper["paper_id"] in skip_paper_ids:
            continue
        result = classify_paper(paper=paper, config=config, compiled=compiled, stage=stage)
        results.append(result)
    results = sorted(results, key=lambda r: r["paper_id"])
    return results


def serialize(*, results: list[dict[str, Any]]) -> str:
    """Serializes results as canonical JSON (sorted keys, two-space indent, trailing newline).

    Args:
        results (list): Classification result objects.

    Returns:
        text (str): Canonical JSON text.
    """
    text = json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    return text


def parse_skip_ids(*, raw: str | None) -> set[str]:
    """Parses a comma-separated `--skip-paper-ids` argument into a set.

    Args:
        raw (str | None): Comma-separated list, or None.

    Returns:
        ids (set): Paper ids to skip.
    """
    if raw is None or raw.strip() == "":
        return set()
    ids = {part.strip() for part in raw.split(",") if part.strip()}
    return ids


def run_cli(*, args: argparse.Namespace) -> int:
    """Runs the CLI: load config, load papers, classify, write JSON.

    Args:
        args (argparse.Namespace): Parsed CLI arguments.

    Returns:
        exit_code (int): 0 on success, non-zero on validation failure.
    """
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    validate_config(config=config)
    papers = json.loads(Path(args.papers).read_text(encoding="utf-8"))
    skip = parse_skip_ids(raw=args.skip_paper_ids)
    results = classify_papers(papers=papers, config=config, stage=args.stage, skip_paper_ids=skip)
    output_text = serialize(results=results)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(output_text, encoding="utf-8")
    return 0


def fixture_config_canonical() -> dict[str, Any]:
    """Returns a canonical fixture config for self-tests covering hyphenation and overrides."""
    return {
        "version": "1.0",
        "default_decision": "Exclude",
        "default_justification": "Sem pistas de inclusão.",
        "proximity_window": 240,
        "priority_order": ["off_topic", "agentic_ai"],
        "categories": [
            {
                "id": "off_topic",
                "label": "Off-topic",
                "kind": "exclude",
                "justification": "Domínio fora de escopo.",
                "priority_index": 0,
                "patterns": [
                    {"id": "bioinformatics", "regex": r"\bbioinform[aá]tics?\b", "description": "Bioinformatics studies."}
                ],
                "overrides": [
                    {"id": "bio_at_edge", "regex": r"\bedge\s+(deployment|inference|computing)\b", "description": "Bioinformatics deployed at edge."}
                ],
            },
            {
                "id": "agentic_ai",
                "label": "Agentic AI",
                "kind": "include",
                "justification": "Trabalho central em Agentic AI.",
                "priority_index": 1,
                "patterns": [
                    {"id": "agentic_terms", "regex": r"\b(agentic[-\s]+ai|llm[-\s]+agents?|multi[-\s]+agent[-\s]+(orchestrat\w+|deep[-\s]+reinforcement[-\s]+learning))\b", "description": "Canonical agentic AI terms."}
                ],
                "overrides": [],
            },
        ],
    }


def assert_eq(*, expected: Any, actual: Any, label: str) -> None:
    """Asserts equality with a labelled error message."""
    if expected != actual:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def run_self_test() -> int:
    """Runs internal self-tests covering hyphenation, priority order, overrides, idempotency, determinism.

    Returns:
        exit_code (int): 0 if all tests pass, 1 otherwise.
    """
    config = fixture_config_canonical()
    validate_config(config=config)

    papers = [
        {"paper_id": "paper-0001", "title": "Multi-Agent Orchestration for Edge Computing"},
        {"paper_id": "paper-0002", "title": "Multi-Agent-Deep-Reinforcement-Learning-Enabled Caching"},
        {"paper_id": "paper-0003", "title": "Bioinformatics Pipeline for Genomics"},
        {"paper_id": "paper-0004", "title": "Bioinformatics with Edge Deployment"},
        {"paper_id": "paper-0005", "title": "Survey of Database Indexing Techniques"},
        {"paper_id": "paper-0006", "title": "LLM Agents Coordinating Bioinformatics Pipelines at the Edge Deployment"},
    ]

    results = classify_papers(papers=papers, config=config, stage="title", skip_paper_ids=set())
    by_id = {r["paper_id"]: r for r in results}

    assert_eq(expected="Include", actual=by_id["paper-0001"]["decision"], label="paper-0001 multi-agent space-separated")
    assert_eq(expected="Include", actual=by_id["paper-0002"]["decision"], label="paper-0002 multi-agent hyphenated chain")
    assert_eq(expected="Exclude", actual=by_id["paper-0003"]["decision"], label="paper-0003 bioinformatics off-topic")
    assert_eq(expected="off_topic", actual=by_id["paper-0003"]["winning_category"], label="paper-0003 winning category")
    assert_eq(expected="Exclude", actual=by_id["paper-0004"]["decision"], label="paper-0004 override suppresses exclude, falls to default")
    assert_eq(expected="default", actual=by_id["paper-0004"]["winning_category"], label="paper-0004 winning category default after override")
    assert_eq(expected=["bio_at_edge"], actual=by_id["paper-0004"]["overrides_applied"], label="paper-0004 overrides_applied recorded")
    assert_eq(expected="Exclude", actual=by_id["paper-0005"]["decision"], label="paper-0005 default decision when nothing matches")
    assert_eq(expected="default", actual=by_id["paper-0005"]["winning_category"], label="paper-0005 winning category default")
    assert_eq(expected="Include", actual=by_id["paper-0006"]["decision"], label="paper-0006 override on off_topic + agentic include match")
    assert_eq(expected="agentic_ai", actual=by_id["paper-0006"]["winning_category"], label="paper-0006 winning category after fall-through")
    assert_eq(expected=["bio_at_edge"], actual=by_id["paper-0006"]["overrides_applied"], label="paper-0006 overrides_applied carried forward")

    skipped = classify_papers(papers=papers, config=config, stage="title", skip_paper_ids={"paper-0001", "paper-0003"})
    assert_eq(expected={"paper-0002", "paper-0004", "paper-0005", "paper-0006"}, actual={r["paper_id"] for r in skipped}, label="skip-paper-ids honored")

    first = serialize(results=classify_papers(papers=papers, config=config, stage="title", skip_paper_ids=set()))
    second = serialize(results=classify_papers(papers=papers, config=config, stage="title", skip_paper_ids=set()))
    assert_eq(expected=first, actual=second, label="determinism: byte-identical output")

    config_priority_swapped = {
        **config,
        "priority_order": ["agentic_ai", "off_topic"],
        "categories": [
            {**c, "priority_index": 0 if c["id"] == "agentic_ai" else 1} for c in config["categories"]
        ],
    }
    validate_config(config=config_priority_swapped)
    swapped_results = classify_papers(papers=[{"paper_id": "p", "title": "Multi-Agent Orchestration in Bioinformatics"}], config=config_priority_swapped, stage="title", skip_paper_ids=set())
    assert_eq(expected="Include", actual=swapped_results[0]["decision"], label="priority swap: agentic_ai now wins")

    stage_scoped_config = {
        **config,
        "categories": [
            (c if c["id"] != "agentic_ai" else {**c, "patterns": [{**c["patterns"][0], "applicable_stages": ["abstract", "full_text"]}]})
            for c in config["categories"]
        ],
    }
    validate_config(config=stage_scoped_config)
    title_results = classify_papers(papers=[{"paper_id": "p", "title": "LLM Agents at the Edge"}], config=stage_scoped_config, stage="title", skip_paper_ids=set())
    assert_eq(expected="Exclude", actual=title_results[0]["decision"], label="applicable_stages: agentic pattern idle at title")

    print("self-test: all checks passed")
    return 0


def parse_args(*, argv: list[str]) -> argparse.Namespace:
    """Parses CLI arguments.

    Args:
        argv (list): Argument vector excluding the program name.

    Returns:
        args (argparse.Namespace): Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Deterministic regex classifier for screening stages 04/05/06.")
    parser.add_argument("--stage", choices=["title", "abstract", "full_text"], help="Screening stage.")
    parser.add_argument("--config", help="Path to protocols/classifier-config.json.")
    parser.add_argument("--papers", help="Path to JSON array of paper input objects.")
    parser.add_argument("--out", help="Output JSON path for the classification results.")
    parser.add_argument("--skip-paper-ids", default=None, help="Comma-separated paper ids whose `My Final Decision` is already filled.")
    parser.add_argument("--self-test", action="store_true", help="Run internal self-tests and exit.")
    args = parser.parse_args(argv)
    return args


def main(*, argv: list[str]) -> int:
    """Entry point: dispatches between self-test and the CLI."""
    args = parse_args(argv=argv)
    if args.self_test:
        return run_self_test()
    required = ("stage", "config", "papers", "out")
    missing = [name for name in required if getattr(args, name) is None]
    if missing:
        raise SystemExit(f"Missing required arguments: {missing}. Use --self-test to run internal checks.")
    return run_cli(args=args)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
