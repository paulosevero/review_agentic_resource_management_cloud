# Spreadsheet Formatting Requirements

These rules apply to every per-stage screening tab (04 — Title Screening, 05 — Abstract Screening, 06 — Full-Text Screening). They were first applied manually to the title-screening tab and must be reproduced automatically by the stage 05 and 06 agents when they write their respective tabs.

## 1. Color coding (background fill on ID and Title columns)

After decisions are resolved, paint the background of the paper ID cell and the title cell according to the final decision:

| Decision | Background color |
|----------|-----------------|
| Include  | `#e7ffee` (light green) |
| Exclude  | `#ffeff0` (light red) |

Apply color based on `My Final Decision` when filled; fall back to the machine decision when `My Final Decision` is blank.

Rationale: the reviewer can scan the title column visually and only dive into other columns when a color surprises them (red when they expected green, or vice versa).

## 2. Sort order

Rows must be sorted so that all Excluded papers appear first (red block), followed by all Included papers (green block). Within each block, sort by the sub-agent disagreement score descending (highest disagreement first).

Rationale: the reviewer can finish all red papers in one pass and then switch context to the green papers, avoiding the visual disruption of alternating colors.

## 3. Bold keywords in Title and Abstract columns

When writing the title and abstract text into the spreadsheet, wrap strategically important keywords in bold (using rich-text cell formatting, not markdown asterisks) to help the reviewer immediately see why the paper was included or excluded.

Examples of keywords to bold:
- Terms that triggered C1 (agentic AI signal): "LLM", "language model", "agent", "agentic", "GPT", "foundation model"
- Terms that triggered C2 (resource management signal): "scheduling", "placement", "migration", "autoscaling", "orchestration"
- Terms that triggered C3 (infrastructure signal): "edge", "cloud", "fog", "Kubernetes", "MEC", "serverless"
- Terms that led to exclusion: "reinforcement learning", "deep RL", "survey", "systematic review"

Apply bold consistently across the column. Do not bold every occurrence — only bold the first occurrence in each cell, or the occurrence most relevant to the screening decision.

Rationale: the reviewer can identify the reason for inclusion/exclusion at a glance without reading the full title or abstract.
