"""Deterministic regex-based classifier for screening academic papers.

Pure function over (text, config) → (decision, justification, evidence). The
config encodes ordered exclusion/inclusion categories with regex patterns and
optional override patterns; the first matching category wins, subject to
override suppression. Same input + same config always produces the same output.

The classifier is stage-agnostic — title, abstract, and full-text screening
share the same engine; only the input granularity and the loaded config differ.
"""

import json
import re


def compile_config(config: dict) -> dict:
    """Compiles all regex patterns in the config in place and returns the config.

    Args:
        config (dict): Raw config dict loaded from JSON.

    Returns:
        config (dict): Same dict, with each pattern entry augmented with a `compiled` re.Pattern object.
    """
    for category in config["categories"]:
        for pat in category.get("patterns", []):
            pat["compiled"] = re.compile(pat["regex"], re.IGNORECASE)
        for ov in category.get("overrides", []):
            ov["compiled"] = re.compile(ov["regex"], re.IGNORECASE)
    return config


def collect_all_matches(text: str, config: dict) -> list:
    """Collects every pattern hit (triggers and overrides) across all categories.

    Args:
        text (str): The input text to classify.
        config (dict): Compiled config.

    Returns:
        all_matches (list): One dict per regex hit with category, pattern_id, matched_text, position, is_override.
    """
    all_matches = []
    for category in config["categories"]:
        for pat in category.get("patterns", []):
            for m in pat["compiled"].finditer(text):
                all_matches.append({
                    "category": category["id"],
                    "pattern_id": pat["id"],
                    "matched_text": m.group(0),
                    "position": m.start(),
                    "is_override": False,
                })
        for ov in category.get("overrides", []):
            for m in ov["compiled"].finditer(text):
                all_matches.append({
                    "category": category["id"],
                    "pattern_id": ov["id"],
                    "matched_text": m.group(0),
                    "position": m.start(),
                    "is_override": True,
                })
    return all_matches


def classify(text: str, config: dict) -> dict:
    """Applies the priority-ordered classifier to the input text.

    Args:
        text (str): The input text (title for stage 04, title+abstract+keywords for 05, full text for 06).
        config (dict): Compiled config with categories sorted by priority.

    Returns:
        result (dict): Decision, justification, winning_category, evidence (all matches), overrides_applied.
    """
    all_matches = collect_all_matches(text=text, config=config)
    sorted_categories = sorted(config["categories"], key=lambda c: c["priority"])
    overrides_applied = []
    winning_category = None
    for category in sorted_categories:
        triggers = [m for m in all_matches if m["category"] == category["id"] and not m["is_override"]]
        if not triggers:
            continue
        category_overrides = [m for m in all_matches if m["category"] == category["id"] and m["is_override"]]
        if category_overrides:
            overrides_applied.extend(category_overrides)
            continue
        winning_category = category
        break
    if winning_category is None:
        result = {
            "decision": config["default_decision"],
            "justification": config["default_justification"],
            "winning_category": "no_signal",
            "evidence": all_matches,
            "overrides_applied": overrides_applied,
        }
        return result
    result = {
        "decision": winning_category["decision"],
        "justification": winning_category["justification"],
        "winning_category": winning_category["id"],
        "evidence": all_matches,
        "overrides_applied": overrides_applied,
    }
    return result


def load_config(path: str) -> dict:
    """Loads a config file from disk and compiles all regex patterns.

    Args:
        path (str): Filesystem path to the JSON config.

    Returns:
        config (dict): Compiled config ready for classification.
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    config = compile_config(config=raw)
    return config
