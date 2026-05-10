"""Update paper-NNN.md files with stage 04 title screening results.

Reads screening/title/consolidated.json and for each paper:
  1. Updates status.04-title-screening in frontmatter.
  2. Adds screening.04-title-screening block to frontmatter.
  3. Populates the '## 04 — Title Screening' section in the body.
"""

import json
import os
import re
import glob

REPO_ROOT = "/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud"
PAPERS_DIR = os.path.join(REPO_ROOT, "papers")
CONSOLIDATED_PATH = os.path.join(REPO_ROOT, "screening", "title", "consolidated.json")
SUB_AGENT_1_PATH = os.path.join(REPO_ROOT, "screening", "title", "sub-agent-1.json")
SUB_AGENT_2_PATH = os.path.join(REPO_ROOT, "screening", "title", "sub-agent-2.json")

THRESHOLD = 0.67


def load_data():
    """Load consolidated and sub-agent results indexed by paper_id."""
    with open(CONSOLIDATED_PATH, encoding="utf-8") as f:
        consolidated = {d["paper_id"]: d for d in json.load(f)}
    with open(SUB_AGENT_1_PATH, encoding="utf-8") as f:
        sub1 = {d["paper_id"]: d for d in json.load(f)}
    with open(SUB_AGENT_2_PATH, encoding="utf-8") as f:
        sub2 = {d["paper_id"]: d for d in json.load(f)}
    return consolidated, sub1, sub2


def update_frontmatter_status(frontmatter, new_status):
    """Replace status.04-title-screening value in frontmatter YAML string."""
    return re.sub(
        r'("04-title-screening":\s*)pending',
        rf'\g<1>{new_status}',
        frontmatter
    )


def insert_screening_block(frontmatter, cons, sub1_data, sub2_data):
    """Insert the screening.04-title-screening block before the closing --- marker."""
    human_decision = cons["machine_decision"]
    block = (
        f'screening:\n'
        f'  "04-title-screening":\n'
        f'    final_score: {cons["final_score"]}\n'
        f'    threshold_used: {THRESHOLD}\n'
        f'    machine_decision: "{cons["machine_decision"]}"\n'
        f'    disagreement_type: "{cons["disagreement_type"]}"\n'
        f'    human_decision: ""\n'
        f'    human_justification: ""\n'
    )
    return frontmatter + "\n" + block


def build_section_body(cons, sub1_data, sub2_data):
    """Build the ## 04 — Title Screening markdown section body."""
    lines = [
        f"**Title:** {cons['title']}",
        "",
        "### Machine Screening",
        "",
        f"- **Final Score:** {cons['final_score']} (threshold: {THRESHOLD})",
        f"- **Machine Decision:** {cons['machine_decision']}",
        f"- **Disagreement Type:** {cons['disagreement_type']}",
        "",
        "### Sub-Agent 1 (Inclusivist)",
        "",
        f"- **Scores:** C1={sub1_data['c1']} C2={sub1_data['c2']} C3={sub1_data['c3']}",
        f"- **Final Score:** {sub1_data['final_score']}",
        f"- **Decision:** {sub1_data['decision']}",
        f"- **Evidence Excerpt:** {sub1_data['evidence_excerpt']}",
        f"- **Rationale:** {sub1_data['rationale']}",
        "",
        "### Sub-Agent 2 (Exclusivist)",
        "",
        f"- **Scores:** C1={sub2_data['c1']} C2={sub2_data['c2']} C3={sub2_data['c3']}",
        f"- **Final Score:** {sub2_data['final_score']}",
        f"- **Decision:** {sub2_data['decision']}",
        f"- **Evidence Excerpt:** {sub2_data['evidence_excerpt']}",
        f"- **Rationale:** {sub2_data['rationale']}",
        "",
        "### Human Review",
        "",
        "- **My Final Decision:** _(fill in spreadsheet)_",
        "- **My Justification:** _(fill in spreadsheet)_",
    ]
    return "\n".join(lines)


def update_paper_file(filepath, cons, sub1_data, sub2_data):
    """Update a single paper-NNN.md file with screening results."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    match = re.match(r"^(---\n)(.*?)(\n---\n)(.*)", content, re.DOTALL)
    if not match:
        print(f"WARNING: Could not parse frontmatter in {filepath}")
        return False

    opening_sep = match.group(1)
    frontmatter = match.group(2)
    closing_sep = match.group(3)
    body = match.group(4)

    # Skip if already processed
    if '"04-title-screening": include' in frontmatter or '"04-title-screening": exclude' in frontmatter:
        return False

    # Update status
    new_status = cons["machine_decision"]
    frontmatter = update_frontmatter_status(frontmatter, new_status)

    # Insert screening block (after status block, before end of frontmatter)
    frontmatter = insert_screening_block(frontmatter, cons, sub1_data, sub2_data)

    # Update the ## 04 — Title Screening section in body
    section_body = build_section_body(cons, sub1_data, sub2_data)
    body = re.sub(
        r"(## 04 — Title Screening\n\n)<!-- Populated by /04-title-screening -->",
        r"\g<1>" + section_body,
        body
    )

    new_content = opening_sep + frontmatter + closing_sep + body
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    """Run the paper update pipeline."""
    consolidated, sub1, sub2 = load_data()
    paper_files = sorted(glob.glob(os.path.join(PAPERS_DIR, "paper-*.md")))
    print(f"Found {len(paper_files)} paper files to update.")

    updated = 0
    skipped = 0
    errors = 0

    for filepath in paper_files:
        paper_id = os.path.basename(filepath).replace(".md", "")
        if paper_id not in consolidated:
            print(f"WARNING: No screening data for {paper_id}")
            errors += 1
            continue

        try:
            result = update_paper_file(
                filepath=filepath,
                cons=consolidated[paper_id],
                sub1_data=sub1[paper_id],
                sub2_data=sub2[paper_id],
            )
            if result:
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"ERROR updating {paper_id}: {e}")
            errors += 1

        if updated % 500 == 0 and updated > 0:
            print(f"  Progress: {updated} updated...")

    print(f"Done. Updated: {updated}, Skipped (already done): {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()
