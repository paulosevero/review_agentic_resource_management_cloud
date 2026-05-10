"""Builds protocols/classifier-config-abstract.json by extending the title config.

Inherits all title-stage categories with their patterns, then:
  - Adds abstract-specific patterns to existing categories
  - Adds LLM-presence overrides to Cat 3 (RL) and Cat 5 (Classical agents)
  - Adds three new categories: Classical agents (Exclude), MAS LLM-based (Include),
    Agent LLM-based (Include)
  - Reorders priorities so the new categories sit in the correct positions

Run once to regenerate the abstract config from the title config baseline.
"""

import copy
import json
from pathlib import Path

LLM_SIGNAL_REGEX = (
    r"\b(?:llms?|gpts?|chatgpt|llama|bert|edgebert|netgpt|"
    r"foundation(?:al)?\s+model[s]?|large\s+language\s+model[s]?|"
    r"language\s+model[s]?|small\s+language\s+model[s]?|slm[s]?|"
    r"large\s+vision\s+model[s]?|vision[-\s]language\s+model[s]?|vlm[s]?|mllm[s]?|"
    r"agentic|generative\s+ai|generative\s+artificial\s+intelligence|genai|gen[\s-]?ai|aigc|"
    r"transformer[s]?|"
    r"llm[\s-]?(?:agent|driven|empowered|powered|aided|enabled|based|guided|augmented)|"
    r"prompt[\s-]?(?:driven|based|engineering)|chain[\s-]?of[\s-]?thought|"
    r"retrieval[\s-]augmented\s+generation|\brag\b|"
    r"\bai[-\s](?:driven|based|powered|assisted|augmented|native|enabled|optimized|infused)\b|"
    r"\bai\s+agent[s]?\b|\bagent\s+ai\b|\bllm\s+agent[s]?\b|"
    r"chatbot[s]?|conversational\s+ai|"
    r"natural\s+language\s+processing|\bnlp\b|"
    r"intent[-\s]?(?:driven|based)|autonomic|neurosymbolic|language[-\s]augmented)\b"
)

MAS_TERM_REGEX = r"\b(?:multi[\s\-–—]?agent[s]?|multiagent[s]?|MAS|multi[\s\-–—]?agent\s+system[s]?)\b"
AGENT_TERM_REGEX = r"\bagent[s]?\b"


def add_review_abstract_patterns(category: dict) -> None:
    """Adds abstract-specific review phrases to the Review category."""
    category["patterns"].extend([
        {"id": "rev_abs_this_survey", "regex": r"\bthis\s+(?:survey|review|article\s+(?:reviews|surveys|provides\s+an?\s+overview))", "description": "this survey/review (abstract)"},
        {"id": "rev_abs_we_present_overview", "regex": r"\bwe\s+(?:present|provide)\s+(?:a\s+)?(?:comprehensive\s+)?(?:overview|survey|review|systematic\s+review)", "description": "we present overview"},
        {"id": "rev_abs_state_of_the_art", "regex": r"\bstate[-\s]of[-\s]the[-\s]art\s+(?:in|on|review|survey)", "description": "state-of-the-art review"},
        {"id": "rev_abs_systematic_mapping", "regex": r"\bsystematic\s+mapping", "description": "systematic mapping"},
        {"id": "rev_abs_we_review", "regex": r"\bwe\s+(?:systematically\s+)?review\b", "description": "we review"},
    ])


def add_workload_abstract_patterns(category: dict) -> None:
    """Adds abstract-specific LLM-as-workload phrases."""
    category["patterns"].extend([
        {"id": "wl_abs_serving_llms", "regex": r"\b(?:serving|serve|deploying|deploy|hosting|host)\s+(?:of\s+)?(?:llms?|large\s+language\s+models?|foundation\s+models?|generative\s+ai)", "description": "serving/deploying LLMs"},
        {"id": "wl_abs_llm_infra", "regex": r"\b(?:llm|large\s+language\s+model|foundation\s+model)\s+(?:inference\s+)?(?:engine|system|platform|infrastructure|stack|pipeline)", "description": "LLM inference engine/infra"},
        {"id": "wl_abs_for_llm_workload", "regex": r"\bfor\s+(?:efficient\s+|scalable\s+)?(?:llm|large\s+language\s+model|foundation\s+model)\s+(?:inference|serving|training|fine[\s-]?tuning|deployment)", "description": "for LLM inference/serving (workload)"},
        {"id": "wl_abs_we_propose_llm_serving", "regex": r"\bwe\s+(?:propose|present|introduce|design)\s+(?:a\s+)?(?:novel\s+|new\s+)?(?:framework|system|method|approach|scheme|technique|architecture)\s+(?:for|to)\s+(?:efficient\s+|scalable\s+)?(?:serving|inference|deploy(?:ing|ment)|train(?:ing)|fine[\s-]?tuning)\s+(?:of\s+)?(?:llms?|large\s+language\s+models?|foundation\s+models?|generative\s+ai)", "description": "we propose system for LLM serving (workload)"},
    ])
    category["overrides"].extend([
        {"id": "ovr_abs_llm_decides", "regex": r"\b(?:llms?|large\s+language\s+models?|foundation\s+models?|generative\s+ai)\b[^.]{0,100}\b(?:decides?|selects?|chooses?|determines?|recommends?|generates?\s+(?:a\s+)?(?:plan|policy|placement|schedule|allocation))", "description": "LLM decides/selects/generates plan"},
        {"id": "ovr_abs_llm_orchestrates", "regex": r"\b(?:llms?|large\s+language\s+models?|foundation\s+models?)\b[^.]{0,100}\b(?:orchestrate|control|manage|govern|reason|plan)", "description": "LLM orchestrates/manages"},
        {"id": "ovr_abs_agentic_workflow", "regex": r"\bagentic\s+(?:workflow|pipeline|loop|architecture|framework)", "description": "agentic workflow"},
        {"id": "ovr_abs_using_llms_to_decide", "regex": r"\busing\s+(?:llms?|large\s+language\s+models?|foundation\s+models?)\s+to\s+(?:decide|select|recommend|plan|schedule|allocate|orchestrate)", "description": "using LLMs to decide"},
    ])


def add_rl_overrides(category: dict) -> None:
    """Adds LLM-presence override so RL+LLM hybrids escape Cat 3 exclusion."""
    category["overrides"].extend([
        {"id": "ovr_rl_llm_present", "regex": LLM_SIGNAL_REGEX, "description": "LLM signal present (RL+LLM hybrid)"},
    ])


def make_classical_agents_category() -> dict:
    """Creates Cat 5: Classical/non-LLM agents (Exclude). Fires on any MAS or agent term;
    suppressed by any LLM signal. Treats MAS/agent without LLM context as classical/MARL.
    """
    return {
        "id": "classical_agents",
        "label": "Classical agents or MAS (no LLM signal)",
        "decision": "Exclude",
        "justification": "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)",
        "priority": 5,
        "patterns": [
            {"id": "cls_mas_term", "regex": MAS_TERM_REGEX, "description": "MAS / multi-agent / multiagent term"},
            {"id": "cls_agent_term", "regex": AGENT_TERM_REGEX, "description": "agent / agents term"},
            {"id": "cls_jade", "regex": r"\bJADE\s+(?:framework|platform|agent|toolkit)|\bjava\s+agent\s+development\s+(?:environment|framework)", "description": "JADE framework/platform"},
            {"id": "cls_fipa", "regex": r"\bFIPA[-\s]?(?:compliant|protocol|standard|acl|specification)|\bFIPA\s+agent\b", "description": "FIPA-compliant"},
            {"id": "cls_contract_net", "regex": r"\bcontract[\s\-–—]net\s+(?:protocol|interaction)", "description": "contract-net protocol"},
            {"id": "cls_holonic", "regex": r"\bholonic\s+(?:agent|system|architecture|control)", "description": "holonic agent/system"},
            {"id": "cls_bdi", "regex": r"\bBDI\s+(?:agent|architecture|model|framework)", "description": "BDI architecture"},
            {"id": "cls_behavior_based", "regex": r"\bbehavior[\s\-–—]based\s+(?:agent|robot|control|architecture)", "description": "behavior-based agent"},
            {"id": "cls_aglet", "regex": r"\baglet[s]?\s+(?:framework|platform|agent)", "description": "Aglets mobile agents"},
            {"id": "cls_mobile_agents_classic", "regex": r"\bmobile\s+agent[s]?\s+(?:platform|framework|paradigm|migration|cloning|cooperation)", "description": "classical mobile agent platforms"},
            {"id": "cls_blackboard", "regex": r"\bblackboard\s+(?:system|architecture|agent)", "description": "blackboard system"},
            {"id": "cls_auction_protocol", "regex": r"\bauction[\s\-–—]based\s+(?:protocol|negotiation|allocation\s+protocol|coordination)", "description": "auction-based protocol"},
            {"id": "cls_negotiation_protocol", "regex": r"\bnegotiation\s+protocol\s+(?:among|between)\s+agent", "description": "negotiation protocol among agents"},
            {"id": "cls_agent_oriented", "regex": r"\bagent[\s\-–—]oriented\s+(?:software\s+engineering|programming|methodology)", "description": "agent-oriented software engineering"},
            {"id": "cls_kqml", "regex": r"\bKQML\b|\bknowledge\s+query\s+manipulation\s+language\b", "description": "KQML"},
        ],
        "overrides": [
            {"id": "ovr_cls_llm_present", "regex": LLM_SIGNAL_REGEX, "description": "LLM signal present (classical+LLM modernization → Include downstream)"},
        ],
    }


def make_mas_llm_category() -> dict:
    """Creates Cat 6: MAS LLM-based (Include). Requires MAS term AND LLM term in abstract."""
    return {
        "id": "mas_llm_based",
        "label": "MAS LLM-based",
        "decision": "Include",
        "justification": "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).",
        "priority": 6,
        "patterns": [
            {"id": "mas_llm_combo", "regex": rf"(?=.*{MAS_TERM_REGEX})(?=.*{LLM_SIGNAL_REGEX}).+", "description": "MAS term + LLM signal co-occur in abstract"},
        ],
        "overrides": [],
    }


def make_agent_llm_category() -> dict:
    """Creates Cat 7: Agent LLM-based (Include). Requires agent term AND LLM term in abstract."""
    return {
        "id": "agent_llm_based",
        "label": "Agent LLM-based",
        "decision": "Include",
        "justification": "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).",
        "priority": 7,
        "patterns": [
            {"id": "agent_llm_combo", "regex": rf"(?=.*{AGENT_TERM_REGEX})(?=.*{LLM_SIGNAL_REGEX}).+", "description": "agent term + LLM signal co-occur in abstract"},
        ],
        "overrides": [],
    }


def main() -> None:
    title_path = Path("protocols/classifier-config-title.json")
    abstract_path = Path("protocols/classifier-config-abstract.json")
    with open(title_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    config["stage"] = "abstract"
    config["proximity_window"] = 400
    title_categories_by_id = {c["id"]: c for c in config["categories"]}
    add_review_abstract_patterns(category=title_categories_by_id["review"])
    add_workload_abstract_patterns(category=title_categories_by_id["llm_as_workload"])
    add_rl_overrides(category=title_categories_by_id["rl"])
    new_categories = [make_classical_agents_category(), make_mas_llm_category(), make_agent_llm_category()]
    config["categories"] = [c for c in config["categories"] if c["id"] not in {"mas", "agent"}]
    title_categories_by_id["llm_agentic_ai_generic"]["priority"] = 8
    config["categories"].extend(new_categories)
    config["categories"].sort(key=lambda c: c["priority"])
    with open(abstract_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    total = sum(len(c.get("patterns", [])) + len(c.get("overrides", [])) for c in config["categories"])
    print(f"Wrote {abstract_path}: {len(config['categories'])} categories, {total} total rules")


if __name__ == "__main__":
    main()
