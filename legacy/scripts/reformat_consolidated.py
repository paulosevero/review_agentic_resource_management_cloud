"""Reformat screening/title/consolidated.json to match the plugin's expected schema.

The plugin's regenerate_spreadsheet.py expects:
{
  "threshold": 0.67,
  "papers": [
    {
      "paper_id": "paper-001",
      "sub_agent_1": {
        "final_score": 1.0,
        "decision": "include",
        "rationale": "...",
        "criterion_scores": [
          {"criterion_id": "C1", "score": 1.0},
          {"criterion_id": "C2", "score": 1.0},
          {"criterion_id": "C3", "score": 1.0}
        ]
      },
      "sub_agent_2": { ... },
      "score_difference": 0.0,
      "disagreement_type": "agreement_include"
    },
    ...
  ]
}
"""

import json
import os

REPO_ROOT = "/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud"
CONSOLIDATED_PATH = os.path.join(REPO_ROOT, "screening", "title", "consolidated.json")
SUB_AGENT_1_PATH = os.path.join(REPO_ROOT, "screening", "title", "sub-agent-1.json")
SUB_AGENT_2_PATH = os.path.join(REPO_ROOT, "screening", "title", "sub-agent-2.json")
THRESHOLD = 0.67


def main():
    """Convert flat array format to plugin's expected dict format."""
    with open(CONSOLIDATED_PATH, encoding="utf-8") as f:
        flat = json.load(f)

    with open(SUB_AGENT_1_PATH, encoding="utf-8") as f:
        sub1_by_id = {d["paper_id"]: d for d in json.load(f)}

    with open(SUB_AGENT_2_PATH, encoding="utf-8") as f:
        sub2_by_id = {d["paper_id"]: d for d in json.load(f)}

    papers = []
    for record in flat:
        paper_id = record["paper_id"]
        s1 = sub1_by_id[paper_id]
        s2 = sub2_by_id[paper_id]

        papers.append({
            "paper_id": paper_id,
            "machine_decision": record["machine_decision"],
            "final_score": record["final_score"],
            "score_difference": record["score_diff"],
            "disagreement_type": record["disagreement_type"],
            "sub_agent_1": {
                "final_score": s1["final_score"],
                "decision": s1["decision"],
                "rationale": s1["rationale"],
                "evidence_excerpt": s1["evidence_excerpt"],
                "criterion_scores": [
                    {"criterion_id": "C1", "score": s1["c1"]},
                    {"criterion_id": "C2", "score": s1["c2"]},
                    {"criterion_id": "C3", "score": s1["c3"]},
                ],
            },
            "sub_agent_2": {
                "final_score": s2["final_score"],
                "decision": s2["decision"],
                "rationale": s2["rationale"],
                "evidence_excerpt": s2["evidence_excerpt"],
                "criterion_scores": [
                    {"criterion_id": "C1", "score": s2["c1"]},
                    {"criterion_id": "C2", "score": s2["c2"]},
                    {"criterion_id": "C3", "score": s2["c3"]},
                ],
            },
        })

    output = {
        "threshold": THRESHOLD,
        "stage": "title",
        "total_papers": len(papers),
        "include_count": sum(1 for p in papers if p["machine_decision"] == "include"),
        "exclude_count": sum(1 for p in papers if p["machine_decision"] == "exclude"),
        "papers": papers,
    }

    with open(CONSOLIDATED_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Reformatted consolidated.json: {len(papers)} papers")
    print(f"  include: {output['include_count']}, exclude: {output['exclude_count']}")


if __name__ == "__main__":
    main()
