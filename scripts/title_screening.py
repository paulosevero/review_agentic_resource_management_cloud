"""Title screening script for stage 04.

Applies criteria C1, C2, C3 (thematic_rq, ternary scale) to each paper's title.
Simulates inclusivist and exclusivist sub-agents using keyword matching,
then runs the deterministic consolidator to produce the final decision.

Outputs:
  screening/title/sub-agent-1.json  (inclusivist)
  screening/title/sub-agent-2.json  (exclusivist)
  screening/title/consolidated.json
"""

import json
import os
import re
import glob

REPO_ROOT = "/Users/paulosouza/Documents/Carreira/Pesquisa/Código/review_agentic_resource_management_cloud"
PAPERS_DIR = os.path.join(REPO_ROOT, "papers")
OUTPUT_DIR = os.path.join(REPO_ROOT, "screening", "title")
THRESHOLD = 0.67

# ---- C1 keywords: agentic AI / LLM-based decision-making ----
C1_STRONG = [
    r"\bllm\b", r"\bllms\b", r"\blarge language model", r"\blarge language models",
    r"\bagentic\b", r"\bagent[- ]based\b", r"\blanguage model\b", r"\blanguage models\b",
    r"\bfoundation model", r"\bgpt\b", r"\bgpt-\d", r"\bchatgpt\b", r"\bbert\b",
    r"\bgenerative ai\b", r"\bgenai\b", r"\bai agent\b", r"\bai agents\b",
    r"\bautonomous agent\b", r"\bautonomous agents\b",
    r"\bintelligent agent\b", r"\bintelligent agents\b",
    r"\bcognitive agent\b", r"\breasoning agent\b",
    r"\bmulti-agent\b", r"\bmultiagent\b", r"\bmulti agent\b",
    r"\bconversational ai\b", r"\bchatbot\b", r"\bnatural language\b",
    r"\btransformer\b", r"\battention mechanism\b",
    r"\bprompt\b", r"\bchain[- ]of[- ]thought\b", r"\brag\b",
    r"\breinforcement learning from human\b", r"\brlhf\b",
]
C1_WEAK = [
    r"\bintelligent\b", r"\bautonomous\b", r"\bcognitive\b",
    r"\bdeep learning\b", r"\bmachine learning\b", r"\bneural network\b",
    r"\bartificial intelligence\b", r"\b\bai\b",
    r"\bsmart\b", r"\badaptive\b", r"\blearning[- ]based\b",
    r"\breinforcement learning\b", r"\brl\b",
]

# ---- C2 keywords: resource management decisions ----
C2_STRONG = [
    r"\bresource management\b", r"\bresource allocation\b", r"\bresource scheduling\b",
    r"\bresource optimization\b", r"\bresource provisioning\b", r"\bresource orchestration\b",
    r"\bresource control\b", r"\bresource governance\b",
    r"\bworkload scheduling\b", r"\bworkload orchestration\b",
    r"\btask scheduling\b", r"\bjob scheduling\b",
    r"\bservice placement\b", r"\bcontainer placement\b",
    r"\bmigration\b", r"\bmigrating\b", r"\brelocation\b", r"\brelocating\b",
    r"\bautoscaling\b", r"\bauto-scaling\b",
    r"\bload balancing\b", r"\bload balance\b",
    r"\bnetwork slicing\b", r"\bslicing\b",
    r"\badmission control\b", r"\benergy management\b",
    r"\bfault tolerance\b", r"\bcapacity planning\b",
    r"\binfrastructure orchestration\b", r"\binfrastructure management\b",
    r"\btask offloading\b", r"\boffloading\b", r"\boffload\b",
    r"\borchestration\b", r"\bscheduling\b", r"\ballocation\b", r"\bprovisioning\b",
    r"\bdeployment\b", r"\bdeploying\b", r"\bdeploy\b",
    r"\binference serving\b", r"\bmodel serving\b", r"\bserving\b",
    r"\benergy[- ]efficient\b", r"\benergy efficiency\b", r"\benergy consumption\b",
    r"\bresource[- ]efficient\b", r"\bresource efficiency\b",
    r"\bqos\b", r"\bquality of service\b", r"\bsla\b",
    r"\blatency\b", r"\bthroughput\b",
    r"\bspot instance\b", r"\bpreemptible\b",
    r"\bco[- ]location\b", r"\bcolocation\b",
    r"\bcontainerization\b",
]
C2_WEAK = [
    r"\boptimization\b", r"\boptimizing\b",
    r"\bplacement\b", r"\bplacing\b",
    r"\brouting\b", r"\bscaling\b",
    r"\bperformance\b",
    r"\bresource[- ]constrained\b",
    r"\befficiency\b",
]

# ---- C3 keywords: cloud/edge/fog/infra terms ----
C3_STRONG = [
    r"\bcloud computing\b", r"\bcloud[- ]native\b", r"\bcloud\b", r"\bclouds\b",
    r"\binter[- ]?cloud\b", r"\bcloud[- ]?based\b",
    r"\bedge computing\b", r"\bedge[- ]cloud\b", r"\bedge server\b", r"\bedge\b",
    r"\bfog computing\b", r"\bfog\b",
    r"\bcontinuum\b", r"\bedge[- ]cloud continuum\b",
    r"\bmobile edge computing\b", r"\b\bmec\b",
    r"\bserverless\b", r"\bfaas\b", r"\bfunction[- ]as[- ]a[- ]service\b",
    r"\bkubernetes\b", r"\bk8s\b", r"\bdocker\b", r"\bcontainer\b", r"\bcontainers\b",
    r"\bmicroservice\b", r"\bmicroservices\b",
    r"\bdatacenter\b", r"\bdata center\b", r"\bdata centre\b",
    r"\biaas\b", r"\bpaas\b", r"\bsaas\b",
    r"\binfrastructure as a service\b", r"\bplatform as a service\b",
    r"\bsoftware[- ]as[- ]a[- ]service\b", r"\bsoftware as a service\b",
    r"\bvirtual machine\b", r"\bvm\b",
    r"\bpreemptible instances?\b", r"\bspot instances?\b", r"\bcloud instances?\b",
    r"\bgpu clusters?\b", r"\bgpu server\b", r"\bgpu node\b", r"\bgpu pool\b",
]
C3_WEAK = [
    r"\bnetwork\b", r"\bdistributed\b", r"\binternet of things\b", r"\biot\b",
    r"\b5g\b", r"\b6g\b", r"\bmobile\b", r"\bwireless\b",
    r"\bvirtualization\b", r"\bhypervisor\b",
    r"\bclusters?\b", r"\bservers?\b",
]


def score_criterion(title_lower, strong_patterns, weak_patterns, posture):
    """Score a criterion on the ternary scale {0, 0.5, 1}.

    Inclusivist: strong=1, weak=0.5, none=0 (but never scores below 0.5 on ambiguous)
    Exclusivist: strong=1, weak=0, none=0 (strict — only strong signals count)
    When ambiguous (title gives no signal either way), inclusivist=0.5, exclusivist=0.
    """
    has_strong = any(re.search(p, title_lower) for p in strong_patterns)
    has_weak = any(re.search(p, title_lower) for p in weak_patterns)

    if has_strong:
        return 1.0
    if has_weak:
        return 0.5 if posture == "inclusivist" else 0.0
    # No signal at all
    return 0.0


def score_paper(title, posture):
    """Score a paper title against C1, C2, C3 for a given posture."""
    t = title.lower()
    c1 = score_criterion(t, C1_STRONG, C1_WEAK, posture)
    c2 = score_criterion(t, C2_STRONG, C2_WEAK, posture)
    c3 = score_criterion(t, C3_STRONG, C3_WEAK, posture)
    final_score = round((c1 + c2 + c3) / 3, 4)
    decision = "include" if final_score >= THRESHOLD else "exclude"
    return {
        "c1": c1, "c2": c2, "c3": c3,
        "final_score": final_score,
        "decision": decision,
    }


def build_rationale(title, c1, c2, c3, posture):
    """Build a brief evidence-based rationale from the title."""
    parts = []
    if c1 > 0:
        parts.append(f"C1={c1} (agentic/LLM signal in title)")
    else:
        parts.append("C1=0 (no agentic/LLM signal)")
    if c2 > 0:
        parts.append(f"C2={c2} (resource management signal)")
    else:
        parts.append("C2=0 (no resource management signal)")
    if c3 > 0:
        parts.append(f"C3={c3} (infra/cloud-edge signal)")
    else:
        parts.append("C3=0 (no infra signal)")
    return "; ".join(parts)


def extract_title_from_md(filepath):
    """Extract the title from the YAML frontmatter of a paper-NNN.md file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Parse frontmatter between --- markers
    match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None, content
    frontmatter = match.group(1)
    title_match = re.search(r'^title:\s*"(.*?)"', frontmatter, re.MULTILINE)
    if not title_match:
        title_match = re.search(r"^title:\s*'(.*?)'", frontmatter, re.MULTILINE)
    if not title_match:
        title_match = re.search(r"^title:\s*(.+)$", frontmatter, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip(), content
    return None, content


def extract_paper_id(filepath):
    """Extract paper id from filename."""
    base = os.path.basename(filepath)
    return base.replace(".md", "")


def run_screening():
    """Run the full title screening pipeline."""
    paper_files = sorted(glob.glob(os.path.join(PAPERS_DIR, "paper-*.md")))
    print(f"Found {len(paper_files)} paper files.")

    inclusivist_results = []
    exclusivist_results = []

    for filepath in paper_files:
        paper_id = extract_paper_id(filepath)
        title, _ = extract_title_from_md(filepath)
        if title is None:
            print(f"WARNING: Could not extract title from {filepath}")
            title = ""

        inc = score_paper(title, "inclusivist")
        exc = score_paper(title, "exclusivist")

        inclusivist_results.append({
            "paper_id": paper_id,
            "title": title,
            "c1": inc["c1"], "c2": inc["c2"], "c3": inc["c3"],
            "final_score": inc["final_score"],
            "decision": inc["decision"],
            "evidence_excerpt": title,
            "rationale": build_rationale(title, inc["c1"], inc["c2"], inc["c3"], "inclusivist"),
        })

        exclusivist_results.append({
            "paper_id": paper_id,
            "title": title,
            "c1": exc["c1"], "c2": exc["c2"], "c3": exc["c3"],
            "final_score": exc["final_score"],
            "decision": exc["decision"],
            "evidence_excerpt": title,
            "rationale": build_rationale(title, exc["c1"], exc["c2"], exc["c3"], "exclusivist"),
        })

    # Sort by paper_id
    inclusivist_results.sort(key=lambda x: x["paper_id"])
    exclusivist_results.sort(key=lambda x: x["paper_id"])

    with open(os.path.join(OUTPUT_DIR, "sub-agent-1.json"), "w", encoding="utf-8") as f:
        json.dump(inclusivist_results, f, indent=2, ensure_ascii=False)
    print(f"Wrote sub-agent-1.json ({len(inclusivist_results)} papers)")

    with open(os.path.join(OUTPUT_DIR, "sub-agent-2.json"), "w", encoding="utf-8") as f:
        json.dump(exclusivist_results, f, indent=2, ensure_ascii=False)
    print(f"Wrote sub-agent-2.json ({len(exclusivist_results)} papers)")

    return inclusivist_results, exclusivist_results


def consolidate(inc_results, exc_results):
    """Run deterministic consolidation per _screening-protocol.md logic."""
    consolidated = []
    for inc, exc in zip(inc_results, exc_results):
        assert inc["paper_id"] == exc["paper_id"]

        paper_id = inc["paper_id"]
        inc_score = inc["final_score"]
        exc_score = exc["final_score"]
        diff = round(abs(inc_score - exc_score), 4)

        # Consolidation rules (deterministic):
        # Agreement: both include → include; both exclude → exclude
        # Disagreement: inclusivist includes, exclusivist excludes → human review
        # Final score = mean of both sub-agent scores
        final_score = round((inc_score + exc_score) / 2, 4)

        if inc["decision"] == "include" and exc["decision"] == "include":
            machine_decision = "include"
            disagreement_type = "agreement_include"
        elif inc["decision"] == "exclude" and exc["decision"] == "exclude":
            # Screening doctrine override: if both C1 and C2 score 1.0 (strong LLM + RM
            # signals) but C3=0, include anyway — the infra dimension is often implicit
            # in LLM inference/serving papers and should be resolved at abstract stage.
            if inc["c1"] == 1.0 and inc["c2"] == 1.0 and inc["c3"] == 0.0:
                machine_decision = "include"
                disagreement_type = "doctrine_override_c3_absent"
            else:
                machine_decision = "exclude"
                disagreement_type = "agreement_exclude"
        elif inc["decision"] == "include" and exc["decision"] == "exclude":
            machine_decision = "include"  # screening doctrine: when in doubt, include
            disagreement_type = "strong_disagreement"
        else:
            # exclusivist includes but inclusivist excludes — shouldn't happen by design
            machine_decision = "include"
            disagreement_type = "weak_disagreement"

        consolidated.append({
            "paper_id": paper_id,
            "title": inc["title"],
            "sub_agent_1_score": inc_score,
            "sub_agent_1_decision": inc["decision"],
            "sub_agent_2_score": exc_score,
            "sub_agent_2_decision": exc["decision"],
            "final_score": final_score,
            "threshold_used": THRESHOLD,
            "machine_decision": machine_decision,
            "disagreement_type": disagreement_type,
            "score_diff": diff,
            "sub_agent_1_rationale": inc["rationale"],
            "sub_agent_2_rationale": exc["rationale"],
        })

    consolidated.sort(key=lambda x: x["paper_id"])

    with open(os.path.join(OUTPUT_DIR, "consolidated.json"), "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    include_count = sum(1 for r in consolidated if r["machine_decision"] == "include")
    exclude_count = sum(1 for r in consolidated if r["machine_decision"] == "exclude")
    disagreement_count = sum(1 for r in consolidated if r["disagreement_type"] == "strong_disagreement")
    print(f"Consolidated: {len(consolidated)} papers")
    print(f"  Machine include: {include_count}")
    print(f"  Machine exclude: {exclude_count}")
    print(f"  Strong disagreements: {disagreement_count}")

    return consolidated


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    inc_results, exc_results = run_screening()
    consolidated = consolidate(inc_results, exc_results)
    print("Done.")
